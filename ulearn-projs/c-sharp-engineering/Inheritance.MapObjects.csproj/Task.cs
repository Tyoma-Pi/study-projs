using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance.MapObjects
{
    interface IOwnable
    {
        int Owner { get; set; }
    }

    interface IArmed
    {
        Army Army { get; set; }
    }

    interface IGotTreasure
    {
        Treasure Treasure { get; set; }
    }

    class Dwelling : IOwnable
    {
        public int Owner { get; set; }
    }

    class Mine : IOwnable, IArmed, IGotTreasure
    {
        public int Owner { get; set; }
        public Army Army { get; set; }
        public Treasure Treasure { get; set; }
    }

    class Creeps : IArmed, IGotTreasure
    {
        public Army Army { get; set; }
        public Treasure Treasure { get; set; }
    }

    class Wolves : IArmed
    {
        public Army Army { get; set; }
    }

    class ResourcePile : IGotTreasure
    {
        public Treasure Treasure { get; set; }
    }

    public static class Interaction
    {
        public static void Make(Player player, object mapObject)
        {
            if (mapObject is IArmed armed && !player.CanBeat(armed.Army))
            {
                player.Die();
            }
            else
            {
                if (mapObject is IGotTreasure treasure)
                {
                    player.Consume(treasure.Treasure);
                }
                if (mapObject is IOwnable ownable)
                {
                    ownable.Owner = player.Id;
                }
            }
        }
    }
}