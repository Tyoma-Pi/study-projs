package com.example.my_proj3

import android.content.res.ColorStateList
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.graphics.drawable.Drawable
import android.graphics.drawable.TransitionDrawable
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.method.ScrollingMovementMethod
import com.example.my_proj3.databinding.ActivityMainBinding
import kotlin.math.abs
import kotlin.math.max
import kotlin.math.roundToInt

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding: ActivityMainBinding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        var num1 = 0.0
        var num2 = 0.0
        var numFract1 = 0
        var numFract2 = 0
        var numFractF = 0
        var forDigits = false
        var forEquation = false
        var error = false
        var myOperation = ""

        binding.apply {
            fun defTSize()
            {
                if (result.text.toString().length > 17)
                    result.setTextSize(22F)
                else if (result.text.toString().length > 14)
                    result.setTextSize(30F)
                else if (result.text.toString().length > 11)
                    result.setTextSize(36F)
                else
                    result.setTextSize(45F)
            }

            butC.setOnClickListener {
                result.text = "0"
                num1 = 0.0
                num2 = 0.0
                numFract1 = 0
                forDigits = false
                forEquation = false
                error = false
                myOperation = ""
                butDV.setBackgroundResource(R.drawable.operators_m)
                butDV.setTextColor(Color.parseColor("#FFFFFFFF"))
                butML.setBackgroundResource(R.drawable.operators_m)
                butML.setTextColor(Color.parseColor("#FFFFFFFF"))
                butMN.setBackgroundResource(R.drawable.operators_m)
                butMN.setTextColor(Color.parseColor("#FFFFFFFF"))
                butPL.setBackgroundResource(R.drawable.operators_m)
                butPL.setTextColor(Color.parseColor("#FFFFFFFF"))
                result.setTextSize(45F)
            }

            but0.setOnClickListener {
                if (forDigits)
                {
                    result.text = "0"
                }
                else if (result.text.contains("Error"))
                {
                    result.text = "Error"
                }
                else if (result.text != "0") {
                    result.text = "${result.text}0"
                }
                forDigits = false
                defTSize()
            }
            but1.setOnClickListener {
                result.text = if (result.text == "0" || forDigits) "1"
                else if (result.text.contains("Error")) "Error"
                else result.text.toString() + "1"
                forDigits = false
                defTSize()
            }
            but2.setOnClickListener {
                result.text = if (result.text == "0" || forDigits) "2"
                else if (result.text.contains("Error")) "Error"
                else result.text.toString() + "2"
                forDigits = false
                defTSize()
            }
            but3.setOnClickListener {
                result.text = if (result.text == "0" || forDigits) "3"
                else if (result.text.contains("Error")) "Error"
                else result.text.toString() + "3"
                forDigits = false
                defTSize()
            }
            but4.setOnClickListener {
                result.text = if (result.text == "0" || forDigits) "4"
                else if (result.text.contains("Error")) "Error"
                else result.text.toString() + "4"
                forDigits = false
                defTSize()
            }
            but5.setOnClickListener {
                result.text = if (result.text == "0" || forDigits) "5"
                else if (result.text.contains("Error")) "Error"
                else result.text.toString() + "5"
                forDigits = false
                defTSize()
            }
            but6.setOnClickListener {
                result.text = if (result.text == "0" || forDigits) "6"
                else if (result.text.contains("Error")) "Error"
                else result.text.toString() + "6"
                forDigits = false
                defTSize()
            }
            but7.setOnClickListener {
                result.text = if (result.text == "0" || forDigits) "7"
                else if (result.text.contains("Error")) "Error"
                else result.text.toString() + "7"
                forDigits = false
                defTSize()
            }
            but8.setOnClickListener {
                result.text = if (result.text == "0" || forDigits) "8"
                else if (result.text.contains("Error")) "Error"
                else result.text.toString() + "8"
                forDigits = false
                defTSize()
            }
            but9.setOnClickListener {
                result.text = if (result.text == "0" || forDigits) "9"
                else if (result.text.contains("Error")) "Error"
                else result.text.toString() + "9"
                forDigits = false
                defTSize()
            }
            butD.setOnClickListener {
                if (result.text.contains("Error"))
                {
                    result.text = "Error"
                }
                else if (!result.text.contains(','))
                {
                    result.text = "${result.text},"
                }
                defTSize()
            }

            butPM.setOnClickListener {
                if (!error)
                    if (!forEquation)
                    {
                        num1 = result.text.toString().replace(',', '.').toDouble()
                    }
                    else
                    {
                        num2 = result.text.toString().replace(',', '.').toDouble()
                    }
                result.text = if (result.text == "Error") "Error"
                else if(result.text.toString().replace(',', '.').toDouble() < 0.0) result.text.drop(1)
                else if (result.text.toString().replace(',', '.').toDouble() == 0.0) result.text
                else "-${result.text}"
                defTSize()
            }
            butPR.setOnClickListener {
                result.text = if (result.text == "Error") "Error"
                else if (result.text in listOf("0", "0,", "0,0") ||
                    result.text.contains(Regex("^0,0+$"))) "0"
                else (result.text.toString().replace(',', '.').toDouble() / 100)
                    .toString().replace('.', ',')
                defTSize()
            }

            butDV.setOnClickListener {
//                butDV.requestFocus()
//                butDV.backgroundTintMode = myMBBtransition
//                myMBBtransition.startTransition(400)
                if (forEquation && myOperation == "/")
                {
                    numFract1 = if (result.text == "0" || num1 == 0.0 && result.text == "Error" || error) 0
                    else 0
                    result.text = if (result.text == "0" || num1 == 0.0 && result.text == "Error" || error) "Error"
                    else String.format("%.${numFract1}f", num1 / num1)
                }
                if (result.text != "Error")
                {
                    num1 = result.text.toString().replace(',', '.').toDouble()
                    if (!forEquation)
                        numFract1 = if (result.text.contains(",")) {
                            if (result.text.startsWith("-")) result.text.drop(3).length
                            else result.text.drop(2).length
                        } else 0
                }
                else
                    error = true
                forDigits = true
                forEquation = true
                myOperation = "/"
                butDV.setBackgroundResource(R.drawable.operators_m_a)
                butDV.setTextColor(Color.parseColor("#FFFF9600"))
                butML.setBackgroundResource(R.drawable.operators_m)
                butML.setTextColor(Color.parseColor("#FFFFFFFF"))
                butMN.setBackgroundResource(R.drawable.operators_m)
                butMN.setTextColor(Color.parseColor("#FFFFFFFF"))
                butPL.setBackgroundResource(R.drawable.operators_m)
                butPL.setTextColor(Color.parseColor("#FFFFFFFF"))
                defTSize()
            }
            butML.setOnClickListener {
                if (forEquation && myOperation == "*")
                {
                    numFract1 = if (result.text == "0" || num1 == 0.0 && result.text == "Error" || error) 0
                    else numFract1 * 2
                    result.text = if (result.text == "Error" || error) "Error"
                    else String.format("%.${numFract1}f", num1 * num1).replace('.', ',')
                }
                if (result.text != "Error")
                {
                    num1 = result.text.toString().replace(',', '.').toDouble()
                    if (!forEquation)
                        numFract1 = if (result.text.contains(",")) {
                            if (result.text.startsWith("-")) result.text.drop(3).length
                            else result.text.drop(2).length
                        } else 0
                }
                else
                    error = true
                forDigits = true
                forEquation = true
                myOperation = "*"
                butDV.setBackgroundResource(R.drawable.operators_m)
                butDV.setTextColor(Color.parseColor("#FFFFFFFF"))
                butML.setBackgroundResource(R.drawable.operators_m_a)
                butML.setTextColor(Color.parseColor("#FFFF9600"))
                butMN.setBackgroundResource(R.drawable.operators_m)
                butMN.setTextColor(Color.parseColor("#FFFFFFFF"))
                butPL.setBackgroundResource(R.drawable.operators_m)
                butPL.setTextColor(Color.parseColor("#FFFFFFFF"))
                defTSize()
            }
            butMN.setOnClickListener {
                if (forEquation && myOperation == "-")
                {
                    numFract1 = 0
                    result.text = if (result.text == "Error" || error) "Error"
                    else String.format("%.${numFract1}f", num1 - num1)
                }
                if (result.text != "Error")
                {
                    num1 = result.text.toString().replace(',', '.').toDouble()
                    if (!forEquation)
                        numFract1 = if (result.text.contains(",")) {
                            if (result.text.startsWith("-")) result.text.drop(3).length
                            else result.text.drop(2).length
                        } else 0
                }
                else
                    error = true
                forDigits = true
                forEquation = true
                myOperation = "-"
                butDV.setBackgroundResource(R.drawable.operators_m)
                butDV.setTextColor(Color.parseColor("#FFFFFFFF"))
                butML.setBackgroundResource(R.drawable.operators_m)
                butML.setTextColor(Color.parseColor("#FFFFFFFF"))
                butMN.setBackgroundResource(R.drawable.operators_m_a)
                butMN.setTextColor(Color.parseColor("#FFFF9600"))
                butPL.setBackgroundResource(R.drawable.operators_m)
                butPL.setTextColor(Color.parseColor("#FFFFFFFF"))
                defTSize()
            }
            butPL.setOnClickListener {
                if (forEquation && myOperation == "+")
                {
                    result.text = if (result.text == "Error" || error) "Error"
                    else String.format("%.${numFract1}f", num1 + num1).replace('.', ',')
                }
                if (result.text != "Error")
                {
                    num1 = result.text.toString().replace(',', '.').toDouble()
                    if (!forEquation)
                        numFract1 = if (result.text.contains(",")) {
                            if (result.text.startsWith("-")) result.text.drop(3).length
                            else result.text.drop(2).length
                        } else 0
                }
                else
                    error = true
                forDigits = true
                forEquation = true
                myOperation = "+"
                butDV.setBackgroundResource(R.drawable.operators_m)
                butDV.setTextColor(Color.parseColor("#FFFFFFFF"))
                butML.setBackgroundResource(R.drawable.operators_m)
                butML.setTextColor(Color.parseColor("#FFFFFFFF"))
                butMN.setBackgroundResource(R.drawable.operators_m)
                butMN.setTextColor(Color.parseColor("#FFFFFFFF"))
                butPL.setBackgroundResource(R.drawable.operators_m_a)
                butPL.setTextColor(Color.parseColor("#FFFF9600"))
                defTSize()
            }

            butEQ.setOnClickListener {
                forDigits = false
                if (forEquation && !error)
                {
                    num2 = result.text.toString().replace(',', '.').toDouble()
                    numFract2 = if (result.text.contains(",")) {
                        if (result.text.startsWith("-")) result.text.drop(3).length
                        else result.text.drop(2).length
                    } else 0
                }
                forEquation = false
                if (error || myOperation == "/" && num2 == 0.0)
                {
                    result.text = "Error"
                    error = true
                }
                else if (myOperation == "/" && num1 == 0.0)
                    result.text = "0"
                else
                {
                    numFractF = when (myOperation){
                        "/" -> abs(numFract1 - numFract2)
                        "*" -> numFract1 + numFract2
                        else -> max(numFract1, numFract2)
                    }
                    result.text = when (myOperation) {
                        "/" -> String.format("%.${numFractF}f", num1 / num2)
                        "*" -> String.format("%.${numFractF}f", num1 * num2)
                        "-" -> String.format("%.${numFractF}f", num1 - num2)
                        "+" -> String.format("%.${numFractF}f", num1 + num2)
                        else -> if (result.text.matches("^0,(0+)?$".toRegex())) "0"
                            else result.text.toString()
                    }.replace('.', ',').replace(",0", "")
                    num1 = result.text.toString().replace(',', '.').toDouble()
                }
                butDV.setBackgroundResource(R.drawable.operators_m)
                butDV.setTextColor(Color.parseColor("#FFFFFFFF"))
                butML.setBackgroundResource(R.drawable.operators_m)
                butML.setTextColor(Color.parseColor("#FFFFFFFF"))
                butMN.setBackgroundResource(R.drawable.operators_m)
                butMN.setTextColor(Color.parseColor("#FFFFFFFF"))
                butPL.setBackgroundResource(R.drawable.operators_m)
                butPL.setTextColor(Color.parseColor("#FFFFFFFF"))
//                testOut.text = result.text.toString().length.toString()
                defTSize()
            }
        }
    }
}