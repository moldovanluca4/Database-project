# Database course - Campus Information Center (CIC)

This repository contains a comprehensive database-driven web application designed to manage and visualize a complex university ecosystem. The project emphasizes clean database design, utilizing ISA hierarchies and normalized relational schemas to handle various campus entities like buildings, events, and academic departments.

## Project Overview

The Campus Information Center (CIC) provides a centralized platform for managing university resources, including academic events, facilities, and campus personnel. This project demonstrates a full-stack approach to solving real-world data management challenges, featuring a robust backend architecture and a responsive web interface.

## Technical Stack

- Backend: Python (Flask)

- Database: Relational Database (SQL)

- Frontend: HTML, CSS, Jinja2 Templates

## Key Features

- Advanced Data Modeling: Implements complex ISA hierarchies using a table-per-subclass approach.

- Event Management: Specialized event types (e.g., Exams, Ceremonies, Tournaments) have dedicated tables with foreign keys referencing a central Event table. This allows for consistent date/time management and a   clean, extensible schema.

- Campus Resources: Efficiently tracks buildings, lecture halls, and research facilities.

- Academic Mapping: Handles complex relationships between physical locations and academic departments/majors.

  ## Project Structure

- /The flask app: Core web application logic, routing, and UI templates.

- /Database scheme: Entity-Relationship diagrams and detailed schema documentation.

- /Data: SQL scripts for schema creation and mock data insertion.

- /Assignments: Progression of project milestones, including web log evaluations and security implementations.

  
