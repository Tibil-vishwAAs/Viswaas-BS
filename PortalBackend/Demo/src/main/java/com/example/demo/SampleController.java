package com.example.demo;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.ArrayList;
import java.util.List;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SampleController {

    @GetMapping("/employees")
    public ResponseEntity<List<Employee>> getEmployees() {
        List<Employee> employees = new ArrayList<>();
        employees.add(new Employee(1, "Amith", "Software Engineer"));
        employees.add(new Employee(2, "Taher ", "Java Expert"));
        employees.add(new Employee(3, "Devaraja ", "QA Expert"));


        return ResponseEntity.ok(employees);
    }

    //    @GetMapping("/health")
    //    public ResponseEntity<String> healthCheck() {
    //        return ResponseEntity.ok("OK");
    //    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class Employee {
        private int id;
        private String name;
        private String role;

        public Employee(int id, String name, String role) {
            this.id = id;
            this.name = name;
            this.role = role;
        }

        public int getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public String getRole() {
            return role;
        }
    }
}
