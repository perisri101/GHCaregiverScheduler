from flask import Flask, render_template
from models import init_db
from routes import views
from config import Config
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_app():
    try:
        logger.debug("Starting application creation...")
        app = Flask(__name__)
        app.config.from_object(Config)
        
        # Initialize database
        logger.info("Starting database initialization...")
        db_initialized = init_db(app)
        
        if not db_initialized:
            logger.warning("Database initialization failed, but continuing with limited functionality")
        else:
            logger.info("Database initialization successful")
        
        # Register blueprints
        logger.debug("Registering blueprints...")
        app.register_blueprint(views)
        
        # Add error handlers
        @app.errorhandler(500)
        def handle_500(error):
            error_message = str(error)
            logger.error(f"Internal Server Error: {error_message}")
            return render_template('error.html', 
                                error_code=500,
                                error_message=error_message), 500
        
        @app.errorhandler(404)
        def handle_404(error):
            return render_template('error.html',
                                error_code=404,
                                error_message="Page Not Found"), 404
        
        @app.route('/health')
        def health_check():
            return {"status": "healthy", "database_initialized": db_initialized}
        
        logger.debug("Application creation completed successfully")
        return app
    except Exception as e:
        logger.error(f"Error creating application: {str(e)}")
        raise

# Create the application instance
app = create_app()

if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT', 5000))
        logger.info(f"Starting application on port {port}")
        app.run(host='0.0.0.0', port=port, debug=Config.DEBUG)
    except Exception as e:
        logger.error(f"Error running application: {str(e)}")
        raise
