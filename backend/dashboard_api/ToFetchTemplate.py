from flask import Blueprint, jsonify, request
from DatabaseConnector import db_conn 
from database.TemplateTable import TemplateTbl,Downloads,Likes

ToFetchTemplate = Blueprint('ToFetchTemplate', __name__)

@ToFetchTemplate.route('/to_fetch_template', methods=['GET'])
def To_Fetch_Template():
    try:
        offset = int(request.args.get('load', 0))  
        
        connector = db_conn()
        if not connector:
            return jsonify({"message": "Database connection failed"}), 500
        
        templates = connector.query(TemplateTbl).offset(offset).limit(8).all()

        if not templates:
            return jsonify({"message": "No more templates found"}), 404

        formData = []
        for template in templates:
            downloads_count = connector.query(Downloads).filter_by(template_title_fk=template.template_title).count()
            likes_count = connector.query(Likes).filter_by(template_title_fk=template.template_title).count()

            formData.append({
                "id": template.id,
                "template_title": template.template_title,
                "file_data": template.file_data,
                "stored_at": template.stored_at,
                "downloads_count": downloads_count,
                "likes_count": likes_count,
            })

        return jsonify(formData), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
