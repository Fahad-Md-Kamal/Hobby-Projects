/*
Copyright © 2023 NAME HERE <EMAIL ADDRESS>
*/
package main

import (
	"github.com/fahad-md-kamal/cli-todo/cmd"
	"github.com/fahad-md-kamal/cli-todo/models"
)

func main() {
	models.DbConnection()
	models.ApplyMigrations()
	cmd.Execute()
}
