# Day 12 – Data Integrity & Safe Deletion
-----------------------------------------

## 1.What is Data Integrity?
    Data integrity means:
       -->Data should remain correct, consistent, and reliable throughout the system.
       -->If one record depends on another record, their relationship must stay valid.

    Example:
        *A task is assigned to Employee ID 101.
        *If Employee 101 is deleted, the task should not remain without a valid employee.
        *If it remains, it creates inconsistency.

## 2.What is Data Consistency?
    Data consistency means:
       -->All related data must be logically correct and synchronized.
       -->If parent data changes, child data must also be handled properly.

    Example:
        *Employee → Parent
        *Task → Child
        *Deleting parent without handling child creates problems.

## 3.Orphan Records:
    An orphan record is:
        -->A child record that exists without its parent record.

    Example:
        -->Task has emp_id = 101
        -->But Employee 101 does not exist
        -->This creates system errors and unreliable data.
        -->Real databases prevent orphan records using constraints.

## 4.Hard Delete vs Soft Delete:
    ### Hard Delete:
        -->Hard delete permanently removes a record.
    
    Example:
        *employees.remove(employee)

    Advantages:
        -->Removes unused data completely

    Disadvantages:
        -->Data cannot be recovered
        -->May create orphan records
        -->Risk of accidental data loss

    ### Soft Delete:
        -->Soft delete does not remove the record.
        -->Instead, it marks the record as inactive.

    Example:
        *employee["is_active"] = False


    Advantages:
        -->Data can be restored
        -->Safer approach
        -->No data loss
        -->Better for auditing
        -->Most real-world systems use soft delete.

## 5.Safe Deletion Concept:
    Before deleting a record:
        ✔ Check if related data exists
        ✔ Prevent deletion if dependency exists
        ✔ Or handle related data properly

    -->This is called defensive programming.

## 6.Referential Integrity:
    Referential integrity ensures:
        -->Relationships between tables remain valid.
    In databases:
        -->Foreign keys enforce this rule
        -->Parent cannot be deleted if child exists Or child gets deleted automatically (cascade delete)

    Example in database:
        *ON DELETE RESTRICT
        *ON DELETE CASCADE

## 7.Defensive Programming:

    Defensive programming means:
        -->Writing code that prevents errors before they happen.-->Instead of assuming everything is correct:
        -->Validate before deleting
        -->Check dependencies
        -->Handle errors safely

## 8.Why Safe Deletion is Important:
    Without safe deletion:
        -->Data becomes inconsistent
        -->Reports become wrong
        -->System crashes may occur
        -->Business data may be corrupted
        -->With safe deletion:
        -->System becomes stable
        -->Data remains trustworthy
        -->Professional software standards are followed

### Implementations:
    1. Safe Delete (Block if tasks exist)
    2. Soft Delete (Mark inactive)
    3. Cascade Delete Simulation