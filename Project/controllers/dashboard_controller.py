from services import dashboard_service


def dashboard_controller():
    data = dashboard_service.get_dashboard_summary()

    return {
        "status": "success",
        "data": data
    }


def department_dashboard_controller():
    data = dashboard_service.get_department_summary()

    return {
        "status": "success",
        "data": data
    }


def task_dashboard_controller():
    data = dashboard_service.get_task_status_summary()

    return {
        "status": "success",
        "data": data
    }