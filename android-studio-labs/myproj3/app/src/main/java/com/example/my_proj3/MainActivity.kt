package com.example.my_proj3

import android.content.res.ColorStateList
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.graphics.drawable.Drawable
import android.graphics.drawable.TransitionDrawable
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.my_proj3.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding: ActivityMainBinding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val myMBBtransition = TransitionDrawable(
            arrayOf(
                ColorDrawable(Color.parseColor("#FFFF9600")),
                ColorDrawable(Color.parseColor("#FFFFFFFF"))
                )
            )
        val myMBTtransition = TransitionDrawable(
            arrayOf(
                ColorDrawable(Color.parseColor("#FFFFFFFF")),
                ColorDrawable(Color.parseColor("#FFFF9600"))
                )
        )

        var isOperated = false
        var myOperation: String
        var temp: Double

        binding.butC.setOnClickListener {
            binding.result.text = "0"
            isOperated = false
            myOperation = ""
            temp = 0.0
            binding.butDV.setBackgroundResource(R.drawable.operators_m)
            binding.butDV.setTextColor(Color.parseColor("#FFFFFFFF"))
        }
        binding.but0.setOnClickListener {
            if (binding.result.text != "0") {
                binding.result.text = "${binding.result.text}0"
            }
        }
        binding.but1.setOnClickListener {
            binding.result.text = if (binding.result.text == "0" || isOperated) "1"
            else binding.result.text.toString() + "1"
            isOperated = false
        }
        binding.but2.setOnClickListener {
            binding.result.text = if (binding.result.text == "0" || isOperated) "2"
            else binding.result.text.toString() + "2"
            isOperated = false
        }
        binding.but3.setOnClickListener {
            binding.result.text = if (binding.result.text == "0" || isOperated) "3"
            else binding.result.text.toString() + "3"
            isOperated = false
        }
        binding.but4.setOnClickListener {
            binding.result.text = if (binding.result.text == "0" || isOperated) "4"
            else binding.result.text.toString() + "4"
            isOperated = false
        }
        binding.but5.setOnClickListener {
            binding.result.text = if (binding.result.text == "0" || isOperated) "5"
            else binding.result.text.toString() + "5"
            isOperated = false
        }
        binding.but6.setOnClickListener {
            binding.result.text = if (binding.result.text == "0" || isOperated) "6"
            else binding.result.text.toString() + "6"
            isOperated = false
        }
        binding.but7.setOnClickListener {
            binding.result.text = if (binding.result.text == "0" || isOperated) "7"
            else binding.result.text.toString() + "7"
            isOperated = false
        }
        binding.but8.setOnClickListener {
            binding.result.text = if (binding.result.text == "0" || isOperated) "8"
            else binding.result.text.toString() + "8"
            isOperated = false
        }
        binding.but9.setOnClickListener {
            binding.result.text = if (binding.result.text == "0" || isOperated) "9"
            else binding.result.text.toString() + "9"
            isOperated = false
        }
        binding.butD.setOnClickListener {
            if (!binding.result.text.contains(',')) {
                binding.result.text = "${binding.result.text},"
            }
        }
        binding.butPM.setOnClickListener {
            temp = binding.result.text.toString().replace(',', '.').toDouble()
            binding.result.text = if (temp < 0.0) binding.result.text.drop(1)
            else if (temp == 0.0) binding.result.text
            else "-${binding.result.text}"
        }
        binding.butPR.setOnClickListener {
                binding.result.text = "${binding.result.text}%"
        }
        binding.butDV.setOnClickListener {
//            binding.butDV.requestFocus()
//            binding.butDV.backgroundTintMode = myMBBtransition
            myMBBtransition.startTransition(400)
            binding.butDV.setBackgroundResource(R.drawable.operators_m_a)
            binding.butDV.setTextColor(Color.parseColor("#FFFF9600"))
            isOperated = true
            myOperation = "/"
            temp = binding.result.text.toString().toDouble()
        }
    }
}