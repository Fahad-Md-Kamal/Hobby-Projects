package models

import (
	"gorm.io/gorm"
)

type Tasks struct{
	gorm.Model
	Name string `json:"name" gorm:"not null"`
	Details string `json:"details" gorm:"not null"`
	IsDone bool `json:"isDone" gorm:"default=false"`
}

func (tsk *Tasks) CreateTask() error{
	if err := DB.Create(tsk).Error; err != nil{
		return err
	}
	return nil
}

func TaskList() ([]Tasks, error){
	var tasks []Tasks
	if err := DB.Find(&tasks).Error; err != nil{
		return nil, err
	}
	return tasks, nil
}

func TaskDetail(id int) (Tasks, error){
	var tasks Tasks
	if err := DB.First(&tasks, id).Error; err != nil{
		return tasks, err
	}
	return tasks, nil
}