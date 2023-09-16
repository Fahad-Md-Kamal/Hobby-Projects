package models

import (
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

var DB *gorm.DB

func DbConnection(){
	var err error
	dsn := "host=localhost user=postgres password=postgres dbname=cobra_db port=5433 sslmode=disable TimeZone=Asia/Dhaka"
	DB, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})

	if err != nil{
		panic(err)
	}
}

func ApplyMigrations(){
	DB.AutoMigrate(&Tasks{})
}