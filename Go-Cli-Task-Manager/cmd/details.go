/*
Copyright © 2023 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"fmt"

	"github.com/fahad-md-kamal/cli-todo/models"
	"github.com/spf13/cobra"
)

// detailsCmd represents the details command
var detailsCmd = &cobra.Command{
	Use:   "details",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("details called")
		id, err := cmd.Flags().GetInt("tid")
		if err != nil{
			fmt.Println("Missing Task Id")
		}
		task, err := models.TaskDetail(id)
		if err != nil{
			fmt.Println("No Taks found with the given id")
		}
		result := fmt.Sprintf("Id: %d \nName: %s \nDetails: %s \nIsDone: %t\n", task.ID, task.Name, task.Details, task.IsDone)
		print(result)
	},
}

func init() {
	rootCmd.AddCommand(detailsCmd)
	detailsCmd.PersistentFlags().IntP("tid", "t", 0, "Task ID")
}
