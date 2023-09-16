/*
Copyright © 2023 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"fmt"

	"github.com/fahad-md-kamal/cli-todo/models"
	"github.com/spf13/cobra"
)

// type TaskCreate struct{
// 	Name string `json:"name"`
// 	Details string `json:"details"`
// 	IsDone bool `json:"isDone"`
// }

// addCmd represents the add command
var addCmd = &cobra.Command{
	Use:   "add",
	Short: "A brief description of your command",
	Long: `Add a new task with various details.
	For example:

	To add a new Task:
	$ your-app-name add --name "FahadMdKamal" --details "Task Details" --isDone true --owner "Jhon"
	`,
	Run: func(cmd *cobra.Command, args []string) {
		var task models.Tasks
		task.Name, _ = cmd.Flags().GetString("name")
		task.Details, _ = cmd.Flags().GetString("details")
		task.IsDone, _ = cmd.Flags().GetBool("isDone")

		if task.Name != "" {
			task.CreateTask()
			fmt.Printf("Task Added:\nName: %s\nDetails: %s\nIsDone: %v\n",
				task.Name, task.Details, task.IsDone)
		} else {
			fmt.Println("Please provide a valid task name using the --name flag.")
		}
	},
}

func init() {
	rootCmd.AddCommand(addCmd)
	addCmd.PersistentFlags().StringP("name", "n", "", "Item Name")
	addCmd.PersistentFlags().StringP("details", "d", "", "Item detail")
	addCmd.PersistentFlags().BoolP("isDone", "i", false, "Is Done")
}
