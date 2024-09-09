from odoo import http
from odoo.http import request, Response
import logging
import json

_logger = logging.getLogger(__name__)

class StudentAPIController(http.Controller):

    @http.route('/api/student/create', type='http', auth='public', methods=['POST'], csrf=False)
    def create_student(self, **post):
        """Create a new student record"""
        try:
            # Log the incoming raw data
            raw_data = request.httprequest.data

            # Check if there's data in the request
            if raw_data:
                # Decode the data from bytes to string and load it as JSON
                data = raw_data.decode('utf-8')
                vals = json.loads(data)

                # Create the student record
                res = request.env["sms_module.student"].sudo().create(vals)

                _logger.info(f"Successfully created Student ID: {res.id}")

                # Return success response with the created student ID
                return request.make_json_response({
                    "message": "Student has been created successfully",
                    "student_id": res.id
                }, status=200)
            else:
                _logger.warning("No data provided in the request")
                return request.make_response(
                    json.dumps({'status': 'error', 'message': 'No data provided'}),
                    status=400,
                )
        except Exception as e:
            # Log and handle any unexpected errors
            _logger.error(f"An error occurred while creating a student: {str(e)}")
            return request.make_response(
                json.dumps({'status': 'error', 'message': str(e)}),
                status=500,
            )

    @http.route('/api/student/read/<int:student_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def read_student(self, student_id):
        """Retrieve details of a specific student by ID"""
        try:
            student = request.env['sms_module.student'].sudo().browse(student_id)
            if not student.exists():
                return request.make_response(
                    json.dumps({'status': 'error', 'message': "Student not found"}),
                    status=404,
                )
            return request.make_json_response({
                'status': 'success',
                'data': student.read()[0]
            }, status=200)
        except Exception as e:
            _logger.error(f"Error reading student {student_id}: {str(e)}")
            return request.make_response(
                json.dumps({'status': 'error', 'message': str(e)}),
                status=500,
            )

    @http.route('/api/student/read_all', type='http', auth='public', methods=['GET'], csrf=False)
    def read_all_students(self):
        """Retrieve all student records"""
        try:
            students = request.env['sms_module.student'].sudo().search([])
            return request.make_json_response({
                'status': 'success',
                'data': students.read()
            }, status=200)
        except Exception as e:
            _logger.error(f"Error reading all students: {str(e)}")
            return request.make_response(
                json.dumps({'status': 'error', 'message': str(e)}),
                status=500,
            )

    @http.route('/api/student/update/<int:student_id>', type='http', auth='public', methods=['PUT'], csrf=False)
    def update_student(self, student_id, **post):
        """Update a student record"""
        try:
            # Log the incoming raw data
            raw_data = request.httprequest.data

            # Check if there's data in the request
            if raw_data:
                # Decode the data from bytes to string and load it as JSON
                data = raw_data.decode('utf-8')
                vals = json.loads(data)

                # Extract student ID from the data
                if not student_id:
                    _logger.warning("No student_id provided")
                    return request.make_response(
                        json.dumps({'status': 'error', 'message': 'student_id is required'}),
                        status=400,
                    )

                # Search for the student record
                student = request.env["sms_module.student"].sudo().browse(student_id)
                if not student.exists():
                    _logger.warning(f"Student with ID {student_id} not found")
                    return request.make_response(
                        json.dumps({'status': 'error', 'message': f'Student with ID {student_id} not found'}),
                        status=404,
                    )

                # Update the student record
                student.sudo().write(vals)

                _logger.info(f"Successfully updated Student ID: {student.id}")
                return request.make_json_response({
                    'status': 'success',
                    'student_id': student.id
                }, status=200)
            else:
                _logger.warning("No data provided in the update request")
                return request.make_response(
                    json.dumps({'status': 'error', 'message': 'No data provided'}),
                    status=400,
                )
        except Exception as e:
            # Log and handle any unexpected errors
            _logger.error(f"An error occurred while updating student: {str(e)}")
            return request.make_response(
                json.dumps({'status': 'error', 'message': str(e)}),
                status=500,
            )

    @http.route('/api/student/delete/<int:student_id>', type='http', auth='public', methods=['DELETE'], csrf=False)
    def delete_student(self, student_id):
        """Delete a student record"""
        try:
            student = request.env['sms_module.student'].sudo().browse(student_id)

            # Check if the student exists before deleting
            if not student.exists():
                return request.make_response(json.dumps({
                    'status': 'error',
                    'message': "Student not found"
                }), status=404, headers={'Content-Type': 'application/json'})

            # Save the name before deleting
            student_name = student.name

            # Delete the student record
            student.sudo().unlink()

            _logger.info(f"Deleted Student ID: {student_id}")
            return request.make_response(json.dumps({
                'status': 'success',
                'message': f"Student {student_name} deleted successfully."
            }), status=200, headers={'Content-Type': 'application/json'})

        except Exception as e:
            _logger.error(f"Error deleting student {student_id}: {str(e)}")
            return request.make_response(json.dumps({
                'status': 'error',
                'message': str(e)
            }), status=500, headers={'Content-Type': 'application/json'})
