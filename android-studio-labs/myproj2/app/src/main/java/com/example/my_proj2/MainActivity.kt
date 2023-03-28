package com.example.my_proj2

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.KeyEvent
import android.view.View
import android.widget.TextView
import androidx.appcompat.content.res.AppCompatResources
import kotlin.math.abs
import kotlin.math.sqrt

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val elemA: TextView = findViewById(R.id.formulaEl1)
        val elemB: TextView = findViewById(R.id.formulaEl2)
        val elemC: TextView = findViewById(R.id.formulaEl3)
        val myRes: TextView = findViewById(R.id.myResult)
        val countX: View = findViewById(R.id.countX)

        fun checkD(myD: Double): Int {
            return if (myD > 0.0) 1
            else if (myD == 0.0) 0
            else -1
        }

        fun doWork() {
            myRes.setTextColor(AppCompatResources.getColorStateList(this, R.color.black))

            val a: Double = elemA.text.toString().toDouble()
            val b: Double = elemB.text.toString().toDouble()
            val c: Double = elemC.text.toString().toDouble()
            val descr = (b * b - 4 * a * c)

            when (checkD(descr)) {
                1 -> {
                    if (a == 0.0) {
                        val x = -c / b
                        myRes.text = "Линейное уравнение,\nx = $x"
                    }
                    else {
                        val x1 = String.format("%.3f", ((-b + sqrt(descr)) / (2 * a))).toDouble()
                        val x2 = String.format("%.3f", ((-b - sqrt(descr)) / (2 * a))).toDouble()
                        myRes.text = "x1 = $x1\nx2 = + $x2"
                    }
                }
                0 -> {
                    if (a == 0.0 || c == 0.0 && b == 0.0) {
                        myRes.setTextColor(AppCompatResources.getColorStateList(this, R.color.red))
                        myRes.text = "На ноль делить нельзя"
                    }
                    else {
                        val x = String.format("%.3f", (-b / (2 * a))).toDouble()
                        myRes.text = "x1 = x2 = ${abs(x)}"
                    }
                }
                -1 -> {
                    myRes.text = "Корней нет"
                }
            }
        }

        elemC.setOnKeyListener(View.OnKeyListener { v, keyCode, event ->
            if (keyCode == KeyEvent.KEYCODE_ENTER && event.action == KeyEvent.ACTION_UP) {
                doWork()
                return@OnKeyListener true
            }
            false
        })

        countX.setOnClickListener {
            doWork()
        }
    }
}