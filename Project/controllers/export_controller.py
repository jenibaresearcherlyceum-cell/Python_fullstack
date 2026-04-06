from flask import Response, request
from services import export_service


def export_employees_controller():
    department = request.args.get("department")
    search = request.args.get("search")

    csv_data = export_service.export_employees_csv(department, search)

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=employees.csv"
        }
    )


def export_tasks_controller():
    search = request.args.get("search")

    csv_data = export_service.export_tasks_csv(search)

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=tasks.csv"
        }
    )