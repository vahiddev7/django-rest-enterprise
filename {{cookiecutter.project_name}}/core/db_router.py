# --- db_router.py ---
class DatabaseRouter:
    """
    Routes models between multiple databases.
    Users & Auth → default
    Analytics → analytics
    """
    
    app_label_to_db = {
        'users': 'default',
        'authentication': 'default',
        'analytics': 'analytics',
    }

    def db_for_read(self, model, **hints):
        return self.app_label_to_db.get(model._meta.app_label, 'default')

    def db_for_write(self, model, **hints):
        return self.app_label_to_db.get(model._meta.app_label, 'default')

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == self.app_label_to_db.get(app_label, db)