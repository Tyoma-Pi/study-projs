using Inheritance.Geometry.Virtual;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Inheritance.Geometry.Visitor
{
    public interface IVisitor
    {
        Body Visit(Ball ball);
        Body Visit(RectangularCuboid rectangularCuboid);
        Body Visit(Cylinder cylinder);
        Body Visit(CompoundBody compoundBody);
    }

    public abstract class Body
    {
        public Vector3 Position { get; }

        protected Body(Vector3 position)
        {
            Position = position;
        }

        public abstract Body Accept(IVisitor visitor);
    }

    public class Ball : Body
    {
        public double Radius { get; }

        public Ball(Vector3 position, double radius) : base(position)
        {
            Radius = radius;
        }

        public override Body Accept(IVisitor visitor)
        {
            return visitor.Visit(this);
        }
    }

    public class RectangularCuboid : Body
    {
        public double SizeX { get; }
        public double SizeY { get; }
        public double SizeZ { get; }

        public RectangularCuboid(Vector3 position, double sizeX, double sizeY, double sizeZ) : base(position)
        {
            SizeX = sizeX;
            SizeY = sizeY;
            SizeZ = sizeZ;
        }

        public override Body Accept(IVisitor visitor)
        {
            return visitor.Visit(this);
        }
    }

    public class Cylinder : Body
    {
        public double SizeZ { get; }

        public double Radius { get; }

        public Cylinder(Vector3 position, double sizeZ, double radius) : base(position)
        {
            SizeZ = sizeZ;
            Radius = radius;
        }

        public override Body Accept(IVisitor visitor)
        {
            return visitor.Visit(this);
        }
    }

    public class CompoundBody : Body
    {
        public IReadOnlyList<Body> Parts { get; }

        public CompoundBody(IReadOnlyList<Body> parts) : base(parts[0].Position)
        {
            Parts = parts;
        }

        public override Body Accept(IVisitor visitor)
        {
            return visitor.Visit(this);
        }
    }

    public class BoundingBoxVisitor : IVisitor
    {
        public Body Visit(Ball ball)
        {
            return new RectangularCuboid(ball.Position, ball.Radius * 2, ball.Radius * 2, ball.Radius * 2);
        }

        public Body Visit(RectangularCuboid rectangularCuboid)
        {
            return rectangularCuboid;
        }

        public Body Visit(Cylinder cylinder)
        {
            return new RectangularCuboid(cylinder.Position, cylinder.Radius * 2, cylinder.Radius * 2, cylinder.SizeZ);
        }

        public Body Visit(CompoundBody compoundBody)
        {
            RectangularCuboid arg1 = null;

            foreach (Body part in compoundBody.Parts)
            {
                RectangularCuboid arg2 = part.TryAcceptVisitor<RectangularCuboid>(this);
                if (arg1 == null)
                {
                    arg1 = arg2;
                    continue;
                }

                Vector3 deltaForArg1 = new Vector3(arg1.SizeX / 2, arg1.SizeY / 2, arg1.SizeZ / 2);
                Vector3 deltaForArg2 = new Vector3(arg2.SizeX / 2, arg2.SizeY / 2, arg2.SizeZ / 2);

                Vector3 minForArg1 = arg1.Position - deltaForArg1;
                Vector3 maxForArg1 = arg1.Position + deltaForArg1;
                Vector3 minForArg2 = arg2.Position - deltaForArg2;
                Vector3 maxForArg2 = arg2.Position + deltaForArg2;

                arg1 = GetBoundingBox(minForArg1, minForArg2, maxForArg1, maxForArg2);
            }

            return arg1;
        }

        /* 
         public Body Visit(CompoundBody compoundBody)
        {
            RectangularCuboid arg1 = null;

            foreach (Body part in compoundBody.Parts)
            {
                RectangularCuboid arg2 = part.TryAcceptVisitor<RectangularCuboid>(this);
                if (arg1 == null)
                {
                    arg1 = arg2;
                    continue;
                }

                Vector3 deltaForArg1 = new Vector3(arg1.SizeX / 2, arg1.SizeY / 2, arg1.SizeZ / 2);
                Vector3 deltaForArg2 = new Vector3(arg2.SizeX / 2, arg2.SizeY / 2, arg2.SizeZ / 2);

                Vector3 minForArg1 = arg1.Position - deltaForArg1;
                Vector3 maxForArg1 = arg1.Position + deltaForArg1;
                Vector3 minForArg2 = arg2.Position - deltaForArg2;
                Vector3 maxForArg2 = arg2.Position + deltaForArg2;

                arg1 = HelpBoundingBox(minForArg1, minForArg2, maxForArg1, maxForArg2);
            }
            return arg1;
        }

        public RectangularCuboid HelpBoundingBox(Vector3 minForArg1, Vector3 minForArg2,
        Vector3 maxForArg1, Vector3 maxForArg2)
        {
            double minX = Math.Min(minForArg1.X, minForArg2.X);
            double minY = Math.Min(minForArg1.Y, minForArg2.Y);
            double minZ = Math.Min(minForArg1.Z, minForArg2.Z);

            double maxX = Math.Max(maxForArg1.X, maxForArg2.X);
            double maxY = Math.Max(maxForArg1.Y, maxForArg2.Y);
            double maxZ = Math.Max(maxForArg1.Z, maxForArg2.Z);

            var helpingBoundingBox = new RectangularCuboid(
                new Vector3(
                (minX + maxX) / 2,
                (minY + maxY) / 2,
                (minZ + maxZ) / 2),
                maxX - minX,
                maxY - minY,
                maxZ - minZ);

            return helpingBoundingBox;
        }
        */

        public RectangularCuboid GetBoundingBox(
            Vector3 minForArg1,
            Vector3 minForArg2,
            Vector3 maxForArg1,
            Vector3 maxForArg2)
        {
            double minX = Math.Min(minForArg1.X, minForArg2.X);
            double minY = Math.Min(minForArg1.Y, minForArg2.Y);
            double minZ = Math.Min(minForArg1.Z, minForArg2.Z);

            double maxX = Math.Max(maxForArg1.X, maxForArg2.X);
            double maxY = Math.Max(maxForArg1.Y, maxForArg2.Y);
            double maxZ = Math.Max(maxForArg1.Z, maxForArg2.Z);

            var vectorBox = new Vector3((minX + maxX) / 2, (minY + maxY) / 2, (minZ + maxZ) / 2);
            var pointX = maxX - minX;
            var pointY = maxY - minY;
            var pointZ = maxZ - minZ;

            return new RectangularCuboid(vectorBox, pointX, pointY, pointZ);
        }
    }

    public class BoxifyVisitor : IVisitor
    {
        public Body Visit(Ball ball)
        {
            return new RectangularCuboid(ball.Position, ball.Radius * 2, ball.Radius * 2, ball.Radius * 2);
        }

        public Body Visit(RectangularCuboid rectangularCuboid)
        {
            return rectangularCuboid;
        }

        public Body Visit(Cylinder cylinder)
        {
            return new RectangularCuboid(cylinder.Position, cylinder.Radius * 2, cylinder.Radius * 2, cylinder.SizeZ);
        }

        public Body Visit(CompoundBody compoundBody)
        {
            List<Body> newParts = new List<Body>();

            foreach (Body part in compoundBody.Parts)
                newParts.Add(part.TryAcceptVisitor<Body>(this));

            var resultCompound = new CompoundBody(newParts);
            return resultCompound;
        }
    }
}