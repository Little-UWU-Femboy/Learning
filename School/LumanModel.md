```mermaid
erDiagram
    USER ||--o{ USER_SKILL : "possesses"
    USER ||--o{ HELP_REQUEST : "initiates"
    ROLE ||--o{ USER : "assigns_permissions_to"
    SKILL ||--o{ USER_SKILL : "categorizes"
    RESOURCE_CENTER ||--o{ INVENTORY : "stores"
    RESOURCE_CENTER ||--o{ USER : "staffed_by"
    RESOURCE_ITEM ||--o{ INVENTORY : "quantifies"
    RESOURCE_ITEM ||--o{ HELP_REQUEST : "fulfills"

    USER {
        int id PK
        string full_name
        string email
        string phone_number
        int role_id FK
        datetime created_at
    }

    ROLE {
        int id PK
        string title "Admin, Employee, Survivor, Volunteer"
    }

    SKILL {
        int id PK
        string skill_name "Medical, Search & Rescue, Logistics"
        string description
    }

    USER_SKILL {
        int user_id FK
        int skill_id FK
        string certification_level
        boolean background_checked
    }

    RESOURCE_CENTER {
        int id PK
        string center_name
        string address
        float latitude
        float longitude
        int contact_person_id FK
    }

    RESOURCE_ITEM {
        int id PK
        string item_name "Water, First Aid Kit, MRE"
        string unit_of_measure "Liters, Units, Kilograms"
    }

    INVENTORY {
        int id PK
        int center_id FK
        int item_id FK
        int quantity
        datetime last_updated
    }

    HELP_REQUEST {
        int id PK
        int survivor_id FK
        int requested_item_id FK
        float latitude
        float longitude
        string urgency_level "Low, Medium, High, Critical"
        string status "Pending, Dispatched, Fulfilled"
        datetime timestamp
    }
```

Remove HELP_REQUEST table. Only RESOURCE_CENTER should be able to make request for help. 

RESOURCE_CENTER should also track currentl number of surivors

Try to make the invitory items more dynamic. Like if bottle of water, should be a way to count the amount of 16oz, 32oz, 1 oz, etc.






$$
CPU_\text{time} = (\text{Clock Cycles} * time)\\
\text{OR}\\
CPU_\text{time} = \text{Clock Cycles} * \frac{1}{\text{rate}}
$$
