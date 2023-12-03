package com.example.my_proj4

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.my_proj4.databinding.ActivityMainBinding
import java.io.File

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding: ActivityMainBinding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.apply {
//            File("./data.txt").writeText("AAA")
        }
    }
}