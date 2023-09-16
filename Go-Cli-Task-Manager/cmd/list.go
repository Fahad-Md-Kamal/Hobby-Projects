/*
Copyright © 2023 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"fmt"

	"github.com/alexeyco/simpletable"
	"github.com/fahad-md-kamal/cli-todo/models"
	"github.com/fatih/color"
	"github.com/spf13/cobra"
)

// listCmd represents the list command
var listCmd = &cobra.Command{
	Use:   "list",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {

		tasks, err := models.TaskList()
		if err != nil {
			fmt.Printf("Error: %v\n", err)
			return
		}

		table := simpletable.New()

		table.Header = &simpletable.Header{
			Cells: []*simpletable.Cell{
				{Align: simpletable.AlignCenter, Text: "ID"},
				{Align: simpletable.AlignCenter, Text: "Name"},
				{Align: simpletable.AlignCenter, Text: "Details"},
				{Align: simpletable.AlignCenter, Text: "Is Done"},
			},
		}

		for _, task := range tasks {
            var nameText string
            if task.IsDone {
                nameText = color.GreenString(task.Name) // Change the color of the "Name" column to green
            } else {
                nameText = color.BlueString(task.Name)  // Change the color of the "Name" column to blue
            }

            r := []*simpletable.Cell{
                {Align: simpletable.AlignRight, Text: fmt.Sprintf("%d", task.ID)},
                {Text: nameText},
                {Text: task.Details},
                {Text: fmt.Sprintf("%t", task.IsDone)},
            }

            table.Body.Cells = append(table.Body.Cells, r)
        }
		
		table.SetStyle(simpletable.StyleCompactLite)
		fmt.Println(table.String())
		
	},
}


var itemName string

func init() {
	rootCmd.AddCommand(listCmd)
    listCmd.Flags().StringVarP(&itemName, "item", "i", "", "Name of the item to list")
    listCmd.Flags().StringP("token", "t", "123", "Value of the tok flag")

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// listCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// listCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}
