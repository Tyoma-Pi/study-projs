package com.example.my_proj2

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.KeyEvent
import androidx.appcompat.content.res.AppCompatResources
import com.example.my_proj2.databinding.ActivityMainBinding
import kotlin.math.abs
import kotlin.math.sqrt

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        val view = binding.root
        setContentView(view)

        fun checkD(myD: Double): Int {
            return if (myD > 0.0) 1
            else if (myD == 0.0) 0
            else -1
        }

        fun doWork() {
            binding.myResult.setTextColor(AppCompatResources.getColorStateList(this, R.color.black))

            val a: Double = binding.formulaEl1.text.toString().toDouble()
            val b: Double = binding.formulaEl2.text.toString().toDouble()
            val c: Double = binding.formulaEl3.text.toString().toDouble()
            val descr = (b * b - 4 * a * c)

            when (checkD(descr)) {
                1 -> {
                    if (a == 0.0) {
                        val x = -c / b
                        binding.myResult.text = "Линейное уравнение,\nx = $x"
                    }
                    else {
                        val x1 = String.format("%.3f", ((-b + sqrt(descr)) / (2 * a))).toDouble()
                        val x2 = String.format("%.3f", ((-b - sqrt(descr)) / (2 * a))).toDouble()
                        binding.myResult.text = "x1 = $x1\nx2 = $x2"
                    }
                }
                0 -> {
                    if (a == 0.0 || c == 0.0 && b == 0.0) {
                        binding.myResult.setTextColor(AppCompatResources.getColorStateList(this, R.color.red   ))
                        binding.myResult.text = "На ноль делить нельзя"
                    }
                    else {
                        val x = String.format("%.3f", (-b / (2 * a))).toDouble()
                        binding.myResult.text = "x1 = x2 = ${abs(x)}"
                    }
                }
                -1 -> {
                    binding.myResult.text = "Корней нет"
                }
            }
        }

        binding.formulaEl3.setOnKeyListener{ _, keyCode, event ->
            if (keyCode == KeyEvent.KEYCODE_ENTER && event.action == KeyEvent.ACTION_UP) {
                doWork()
            }
            false
        }

        binding.countX.setOnClickListener {
            doWork()
        }
    }
}