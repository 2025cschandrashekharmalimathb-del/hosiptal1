# scripts/seed_data.py

import sys
from datetime import datetime, timedelta
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.database import database


# ---------------------------------------------------------
# TIME HELPERS
# ---------------------------------------------------------

NOW = datetime.utcnow()


def days_ago(n: int) -> datetime:
    return NOW - timedelta(days=n)


# =========================================================
# 1. USERS
# =========================================================

USERS = [

    # Hospital Staff
    {
        "id": "user-emp-1",
        "name": "Dr. Priya Sharma",
        "email": "priya.sharma@cityhospital.com",
        "password": "password123",
        "role": "employee",
        "created_at": days_ago(30)
    },

    {
        "id": "user-emp-2",
        "name": "Rahul Kumar",
        "email": "rahul.kumar@cityhospital.com",
        "password": "password123",
        "role": "employee",
        "created_at": days_ago(29)
    },

    {
        "id": "user-emp-3",
        "name": "Ananya Rao",
        "email": "ananya.rao@cityhospital.com",
        "password": "password123",
        "role": "employee",
        "created_at": days_ago(28)
    },

    {
        "id": "user-emp-4",
        "name": "Suresh Patil",
        "email": "suresh.patil@cityhospital.com",
        "password": "password123",
        "role": "employee",
        "created_at": days_ago(27)
    },

    # Team Lead
    {
        "id": "user-lead-1",
        "name": "Meena Reddy",
        "email": "meena.reddy@cityhospital.com",
        "password": "password123",
        "role": "team_lead",
        "created_at": days_ago(60)
    },

    # Support Staff
    {
        "id": "user-support-1",
        "name": "Arjun Nair",
        "email": "arjun.nair@cityhospital.com",
        "password": "password123",
        "role": "support_engineer",
        "created_at": days_ago(50)
    },

    {
        "id": "user-support-2",
        "name": "Divya Iyer",
        "email": "divya.iyer@cityhospital.com",
        "password": "password123",
        "role": "support_engineer",
        "created_at": days_ago(45)
    },

    # Admin
    {
        "id": "user-admin-1",
        "name": "Vikram Rao",
        "email": "vikram.rao@cityhospital.com",
        "password": "password123",
        "role": "admin",
        "created_at": days_ago(90)
    }
]


# =========================================================
# 2. HOSPITAL REQUEST CATEGORIES
# =========================================================

CATEGORIES = [

    {
        "id": "cat-equipment",
        "name": "Equipment Issue",
        "description": "Problems with medical or hospital equipment",
        "created_at": days_ago(90)
    },

    {
        "id": "cat-maintenance",
        "name": "Maintenance",
        "description": "Electrical, plumbing, air conditioning and repair requests",
        "created_at": days_ago(90)
    },

    {
        "id": "cat-it",
        "name": "IT Issue",
        "description": "Hospital computers, network, software and system problems",
        "created_at": days_ago(90)
    },

    {
        "id": "cat-facility",
        "name": "Facility Request",
        "description": "Cleaning, rooms, utilities and hospital facility requests",
        "created_at": days_ago(90)
    }
]


# =========================================================
# 3. HOSPITAL SERVICE REQUEST TICKETS
# =========================================================

TICKETS = [

    # -----------------------------------------------------
    # NEW
    # -----------------------------------------------------

    {
        "id": "ticket-1",
        "title": "Air Conditioner Not Working",
        "description": "The air conditioner in Room 204 is not functioning and the room temperature is increasing.",

        "category_id": "cat-maintenance",

        # NEW FIELDS
        "department": "General Medicine",
        "location": "Room 204",

        "priority": "HIGH",
        "status": "new",

        "created_by": "user-emp-1",
        "assigned_to": None,

        "created_at": days_ago(1),
        "updated_at": days_ago(1)
    },


    # -----------------------------------------------------
    # ASSIGNED
    # -----------------------------------------------------

    {
        "id": "ticket-2",
        "title": "Patient Monitor Display Problem",
        "description": "The patient monitoring system in ICU Bed 5 has a flickering display.",

        "category_id": "cat-equipment",

        # NEW FIELDS
        "department": "Intensive Care Unit",
        "location": "ICU Bed 5",

        "priority": "HIGH",
        "status": "assigned",

        "created_by": "user-emp-2",
        "assigned_to": "user-support-1",

        "created_at": days_ago(3),
        "updated_at": days_ago(2)
    },


    # -----------------------------------------------------
    # IN PROGRESS
    # -----------------------------------------------------

    {
        "id": "ticket-3",
        "title": "Hospital Wi-Fi Not Available",
        "description": "The Wi-Fi connection is unavailable in the second floor nursing station.",

        "category_id": "cat-it",

        # NEW FIELDS
        "department": "Nursing",
        "location": "2nd Floor Nursing Station",

        "priority": "MEDIUM",
        "status": "in_progress",

        "created_by": "user-emp-3",
        "assigned_to": "user-support-2",

        "created_at": days_ago(4),
        "updated_at": days_ago(2)
    },


    # -----------------------------------------------------
    # ON HOLD
    # -----------------------------------------------------

    {
        "id": "ticket-4",
        "title": "Water Leakage in Ward 3",
        "description": "Water is leaking from the ceiling near the wash area in Ward 3.",

        "category_id": "cat-facility",

        # NEW FIELDS
        "department": "General Medicine",
        "location": "Ward 3",

        "priority": "HIGH",
        "status": "on_hold",

        "created_by": "user-emp-4",
        "assigned_to": "user-support-1",

        "created_at": days_ago(5),
        "updated_at": days_ago(3)
    },


    # -----------------------------------------------------
    # RESOLVED
    # -----------------------------------------------------

    {
        "id": "ticket-5",
        "title": "Operation Theatre Light Failure",
        "description": "One of the surgical lights in Operation Theatre 2 was not working.",

        "category_id": "cat-equipment",

        # NEW FIELDS
        "department": "Surgery",
        "location": "Operation Theatre 2",

        "priority": "CRITICAL",
        "status": "resolved",

        "created_by": "user-emp-1",
        "assigned_to": "user-support-2",

        "created_at": days_ago(8),
        "updated_at": days_ago(1)
    },


    # -----------------------------------------------------
    # CLOSED
    # -----------------------------------------------------

    {
        "id": "ticket-6",
        "title": "Nurse Station Computer Issue",
        "description": "The computer at the emergency ward nurse station was restarting unexpectedly.",

        "category_id": "cat-it",

        # NEW FIELDS
        "department": "Emergency",
        "location": "Emergency Ward Nurse Station",

        "priority": "MEDIUM",
        "status": "closed",

        "created_by": "user-emp-2",
        "assigned_to": "user-support-1",

        "created_at": days_ago(10),
        "updated_at": days_ago(1)
    },


    # -----------------------------------------------------
    # NEW
    # -----------------------------------------------------

    {
        "id": "ticket-7",
        "title": "Wheelchair Wheel Damaged",
        "description": "The front wheel of a wheelchair in the outpatient department is damaged.",

        "category_id": "cat-equipment",

        # NEW FIELDS
        "department": "Outpatient Department",
        "location": "OPD Waiting Area",

        "priority": "MEDIUM",
        "status": "new",

        "created_by": "user-emp-3",
        "assigned_to": None,

        "created_at": days_ago(1),
        "updated_at": days_ago(1)
    },


    # -----------------------------------------------------
    # ASSIGNED
    # -----------------------------------------------------

    {
        "id": "ticket-8",
        "title": "Patient Room Cleaning Required",
        "description": "Room 312 requires immediate cleaning and sanitization before the next patient admission.",

        "category_id": "cat-facility",

        # NEW FIELDS
        "department": "General Medicine",
        "location": "Room 312",

        "priority": "HIGH",
        "status": "assigned",

        "created_by": "user-emp-4",
        "assigned_to": "user-support-2",

        "created_at": days_ago(2),
        "updated_at": days_ago(1)
    }
]


# =========================================================
# 4. COMMENTS
# =========================================================

COMMENTS = [

    {
        "id": "comment-1",
        "ticket_id": "ticket-1",
        "author_id": "user-emp-1",
        "content": "The room is becoming uncomfortable for the patient. Please check it as soon as possible.",
        "created_at": days_ago(1)
    },

    {
        "id": "comment-2",
        "ticket_id": "ticket-2",
        "author_id": "user-support-1",
        "content": "We have inspected the patient monitor and are checking the display connection.",
        "created_at": days_ago(2)
    },

    {
        "id": "comment-3",
        "ticket_id": "ticket-3",
        "author_id": "user-support-2",
        "content": "Network equipment is being checked at the second floor nursing station.",
        "created_at": days_ago(2)
    },

    {
        "id": "comment-4",
        "ticket_id": "ticket-4",
        "author_id": "user-support-1",
        "content": "Maintenance team has been informed about the water leakage.",
        "created_at": days_ago(3)
    },

    {
        "id": "comment-5",
        "ticket_id": "ticket-5",
        "author_id": "user-support-2",
        "content": "The surgical light was repaired and tested successfully.",
        "created_at": days_ago(1)
    },

    {
        "id": "comment-6",
        "ticket_id": "ticket-6",
        "author_id": "user-emp-2",
        "content": "The computer is working normally after the repair.",
        "created_at": days_ago(1)
    },

    {
        "id": "comment-7",
        "ticket_id": "ticket-8",
        "author_id": "user-support-2",
        "content": "Cleaning staff has been assigned to Room 312.",
        "created_at": days_ago(1)
    }
]


# =========================================================
# 5. ATTACHMENTS
# =========================================================

ATTACHMENTS = [

    {
        "id": "attachment-1",
        "ticket_id": "ticket-1",
        "uploaded_by": "user-emp-1",
        "filename": "ac_room_204.jpg",
        "url": "https://files.example.com/ac_room_204.jpg",
        "size": 245760,
        "created_at": days_ago(1)
    },

    {
        "id": "attachment-2",
        "ticket_id": "ticket-2",
        "uploaded_by": "user-support-1",
        "filename": "patient_monitor.jpg",
        "url": "https://files.example.com/patient_monitor.jpg",
        "size": 315000,
        "created_at": days_ago(2)
    },

    {
        "id": "attachment-3",
        "ticket_id": "ticket-3",
        "uploaded_by": "user-emp-3",
        "filename": "wifi_issue.png",
        "url": "https://files.example.com/wifi_issue.png",
        "size": 185000,
        "created_at": days_ago(4)
    },

    {
        "id": "attachment-4",
        "ticket_id": "ticket-4",
        "uploaded_by": "user-emp-4",
        "filename": "water_leakage.jpg",
        "url": "https://files.example.com/water_leakage.jpg",
        "size": 420000,
        "created_at": days_ago(5)
    },

    {
        "id": "attachment-5",
        "ticket_id": "ticket-5",
        "uploaded_by": "user-support-2",
        "filename": "ot_light_repair.pdf",
        "url": "https://files.example.com/ot_light_repair.pdf",
        "size": 95000,
        "created_at": days_ago(1)
    },

    {
        "id": "attachment-6",
        "ticket_id": "ticket-7",
        "uploaded_by": "user-emp-3",
        "filename": "wheelchair_damage.jpg",
        "url": "https://files.example.com/wheelchair_damage.jpg",
        "size": 285000,
        "created_at": days_ago(1)
    },

    {
        "id": "attachment-7",
        "ticket_id": "ticket-8",
        "uploaded_by": "user-emp-4",
        "filename": "room_cleaning.jpg",
        "url": "https://files.example.com/room_cleaning.jpg",
        "size": 215000,
        "created_at": days_ago(2)
    }
]


# =========================================================
# 6. AUDIT LOGS
# =========================================================

AUDIT_LOGS = [

    {
        "id": "audit-1",
        "ticket_id": "ticket-1",
        "action": "created",
        "performed_by": "user-emp-1",
        "details": "Hospital maintenance request created with status 'new'.",
        "created_at": days_ago(1)
    },

    {
        "id": "audit-2",
        "ticket_id": "ticket-2",
        "action": "created",
        "performed_by": "user-emp-2",
        "details": "Medical equipment issue created with status 'new'.",
        "created_at": days_ago(3)
    },

    {
        "id": "audit-3",
        "ticket_id": "ticket-2",
        "action": "assigned",
        "performed_by": "user-lead-1",
        "details": "Patient monitor issue assigned to maintenance staff.",
        "created_at": days_ago(2)
    },

    {
        "id": "audit-4",
        "ticket_id": "ticket-3",
        "action": "created",
        "performed_by": "user-emp-3",
        "details": "Hospital IT request created with status 'new'.",
        "created_at": days_ago(4)
    },

    {
        "id": "audit-5",
        "ticket_id": "ticket-3",
        "action": "assigned",
        "performed_by": "user-lead-1",
        "details": "Hospital Wi-Fi issue assigned to IT support staff.",
        "created_at": days_ago(2)
    },

    {
        "id": "audit-6",
        "ticket_id": "ticket-3",
        "action": "status_changed",
        "performed_by": "user-support-2",
        "details": "Status changed from 'assigned' to 'in_progress'.",
        "created_at": days_ago(2)
    },

    {
        "id": "audit-7",
        "ticket_id": "ticket-5",
        "action": "status_changed",
        "performed_by": "user-support-2",
        "details": "Operation theatre light repair completed. Status changed to 'resolved'.",
        "created_at": days_ago(1)
    },

    {
        "id": "audit-8",
        "ticket_id": "ticket-6",
        "action": "status_changed",
        "performed_by": "user-emp-2",
        "details": "Nurse station computer confirmed working. Ticket closed.",
        "created_at": days_ago(1)
    }
]


# =========================================================
# SEED DATABASE
# =========================================================

def seed() -> None:

    collections_and_data = [
        ("users", USERS),
        ("categories", CATEGORIES),
        ("tickets", TICKETS),
        ("comments", COMMENTS),
        ("attachments", ATTACHMENTS),
        ("audit_logs", AUDIT_LOGS),
    ]

    for collection_name, documents in collections_and_data:

        collection = database[collection_name]

        deleted = collection.delete_many({}).deleted_count

        collection.insert_many(documents)

        print(
            f"{collection_name}: "
            f"cleared {deleted} old record(s), "
            f"inserted {len(documents)} new record(s)"
        )


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    seed()

    print("\n===================================")
    print("Hospital seed data inserted successfully!")
    print("===================================")