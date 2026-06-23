from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from database import SessionLocal, LeaveRequest

app = FastAPI(title="Employee Leave Management")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Leave Management API Running"}


# Apply Leave
@app.post("/apply_leave")
def apply_leave(
    employee_id: str,
    employee_name: str,
    start_date: date,
    end_date: date,
    db: Session = Depends(get_db)
):

    leave_days = (end_date - start_date).days + 1

    leave = LeaveRequest(
        employee_id=employee_id,
        employee_name=employee_name,
        start_date=start_date,
        end_date=end_date,
        leave_days=leave_days,
        status="Pending"
    )

    db.add(leave)
    db.commit()

    return {"message": "Leave Request Submitted"}


# Manager Approval
@app.put("/approve_leave/{leave_id}")
def approve_leave(
    leave_id: int,
    db: Session = Depends(get_db)
):

    leave = db.query(LeaveRequest).filter(
        LeaveRequest.id == leave_id
    ).first()

    if not leave:
        raise HTTPException(
            status_code=404,
            detail="Leave not found"
        )

    leave.status = "Approved"

    db.commit()

    return {"message": "Leave Approved"}


# Manager Reject
@app.put("/reject_leave/{leave_id}")
def reject_leave(
    leave_id: int,
    db: Session = Depends(get_db)
):

    leave = db.query(LeaveRequest).filter(
        LeaveRequest.id == leave_id
    ).first()

    if not leave:
        raise HTTPException(
            status_code=404,
            detail="Leave not found"
        )

    leave.status = "Rejected"

    db.commit()

    return {"message": "Leave Rejected"}


# View All Leave Requests
@app.get("/leave_requests")
def leave_requests(
    db: Session = Depends(get_db)
):

    data = db.query(LeaveRequest).all()

    result = []

    for r in data:
        result.append({
            "Leave ID": r.id,
            "Employee ID": r.employee_id,
            "Employee Name": r.employee_name,
            "Start Date": r.start_date,
            "End Date": r.end_date,
            "Leave Days": r.leave_days,
            "Status": r.status
        })

    return result


# Employee Leave History
@app.get("/leave_history/{employee_id}")
def leave_history(
    employee_id: str,
    db: Session = Depends(get_db)
):

    data = db.query(LeaveRequest).filter(
        LeaveRequest.employee_id == employee_id
    ).all()

    return data


# Employee Details
@app.get("/employee_details")
def employee_details(
    db: Session = Depends(get_db)
):

    data = db.query(LeaveRequest).all()

    employees = []

    seen = set()

    for row in data:

        if row.employee_id not in seen:

            employees.append({
                "Employee ID": row.employee_id,
                "Employee Name": row.employee_name
            })

            seen.add(row.employee_id)

    return employees