# Django API Enpoint for GP Instructions
- This project provides a RESTful API endpoint that lists GP instructions.

## Features
- List, retrieve and create GP instructions
- Optional filtering by instruction type, date range (start_date, end_date), patient name, and GP name.
- A nested JSON output that includes date, patient name, instruction type, GP name and GP surgery name.
- An admin interface to manage GP instructions.
- Swagger documentation for the API using drf-spectacular.


## Prerequisites
- Python 3.6 or higher
- Django 3.2 or higher
- Django REST Framework
- Django Filter
- drf-spectacular for API documentation
- Django Admin for managing GP instructions



## Setup Instructions


1. Create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```
pip install django djangorestframework django-filter drf-spectacular

```

3. Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```
4. Run tests:

```
python manage.py test core/tests/api_tests.py

``` 


4. Start the server:

```
python manage.py runserver

```
5. Access the API endpoint to see the list of GP instructions in JSON format:

```
http://localhost:8000/api/instructions/

```
**Example Output**

- This is an example of an instruction

```
[
    {
        "instruction_id": 2,
        "date": "2025-07-01",
        "patient": {
            "id": 2,
            "full_name": "Rex Kamp"
        },
        "instruction_type": {
            "id": 2,
            "name": "POA"
        },
        "gp": {
            "id": 2,
            "name": "Laura",
            "surgery": {
                "id": 2,
                "name": "Medicare"
            }
        }
    }        
]

```
### Query Parameters

- You can filter the results using the following query parameters:

- instruction_type: Filter by instruction type e.g; AMRA, SARS, POA, VACCINE

    For example;

    ```
    http://localhost:8000/api/instructions/?instruction_type=AMRA

    ```
- date range(start_date, end_date): Use the format YYYY-MM-DD.

    For example;
  
    ```
    http://localhost:8000/api/instructions/?start_date=2025-06-10&end_date=2025-07-01

    ```
- patient_name: Filter by patient's full name.

    For example;

    ```
    http://localhost:8000/api/instructions/?patient_name=John Doe 
  
    ```

- gp_name: Filter by GP name.

    For example;
    
    ``` 
    http://localhost:8000/api/instructions/?gp_name=Alex

    ```

- You can also combine the query parameters to refine your search.

    - For example;    

    ```
    http://localhost:8000/api/instructions/?instruction_type=SARS&start_date=2025-06-01&end_date=2025-06-30&patient_name=John Doe&gp_name=Smith

    ```

6. On a new terminal, activate the virtual environment and create a superuser to access the admin interface. 

```
python manage.py createsuperuser 

```
- The admin interface allows you to manage GP instructions, including adding, editing, and deleting records.

Access the admin interface at:

```
http://localhost:8000/admin/

```

## API Documentation

The API documentation is generated using drf-spectacular and is available at:

```
http://localhost:8000/api/docs/

```

## Design Decisions

- I used a DRF ViewSet to encapsulate logic for listing and retrieving instructions. It makes it easy to extend the endpoint and also allows automatic routing.

- I used a nested serializer for the GP model. A GP belongs to a surgery, therefore the surgery should be nested in the gp field. This makes the JSON output look more structured and readable.

- I used django-filters to implement filtering because it allows flexibility of query parameters such as instruction_type and date range.

- I used the Django's built-in admin to create, update and delete instructions because it provides an interface for quick data management.

- I added unit tests to check whether the endpoint returns the correct data. This ensures accuracy.

## Areas of improvement
- Pagination - This would be useful for large datasets. It improves scalability by limited the amount of data returned in each response.

- More complex query logic - Allow filtering patients' full name instead of their first name only. It improves usability and accuracy.

- Authentication/ Role based access - This ensures that the instructions are only accessed by authorized personnel.

- Error handling - Provide more detailed responses incase a user tries to use and invalid filter.

- Custom validation - Add validation for the date range logic, e.g; the start date should be before the end date.
