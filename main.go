package main

import (
	"fmt"
	"net/http"
)

func main() {
	//
	http.HandleFunc("/download", func(w http.ResponseWriter, r *http.Request) {
		fileName := "example.txt"

		w.Header().Set("Content-Disposition", fmt.Sprintf("attachment; filename=%s", fileName))
		w.Header().Set("Content-Type", "application/octet-stream")

		fileContent := []byte("File content.")

		w.Write(fileContent)
	})

	fmt.Println("Server http://localhost:8080 on!")
	http.ListenAndServe(":8080", nil)
}

