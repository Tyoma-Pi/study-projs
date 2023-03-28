package com.example.my_proj

import android.os.Bundle
import android.view.KeyEvent
import android.view.View
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val myText: TextView = findViewById(R.id.myText)
        val editText: TextView = findViewById(R.id.myEditText)
        val myButton: View = findViewById(R.id.myButton)

        fun showVal() {
            val str: String = editText.text.toString()
            myText.text = str
        }

        myButton.setOnClickListener {
            showVal()
        }

        editText.setOnKeyListener(View.OnKeyListener { v, keyCode, event ->
            if (keyCode == KeyEvent.KEYCODE_ENTER && event.action == KeyEvent.ACTION_DOWN) {
                showVal()
                return@OnKeyListener true
            }
            false
        })
    }
}