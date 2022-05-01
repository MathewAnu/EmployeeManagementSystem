#GET
curl -X GET http://127.0.0.1:8000/employee_management_system/Team

#POST
curl -X POST -d "team_name"="TestTeamName4" http://127.0.0.1:8000/employee_management_system/Team

#PUT
#curl -X PUT -d "team_name"="Yellow" http://127.0.0.1:8000/employee_management_system/Team/"TestTeamName4"

#DELETE
curl -X DELETE http://127.0.0.1:8000/employee_management_system/Team/"Yellow"