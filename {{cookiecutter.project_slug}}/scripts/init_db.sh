# --- init_db.sh ---
#!/bin/bash
echo "Initializing databases..."
psql -U $DB_DEFAULT_USER -c "CREATE DATABASE IF NOT EXISTS $DB_DEFAULT_NAME;"
psql -U $DB_ANALYTICS_USER -c "CREATE DATABASE IF NOT EXISTS $DB_ANALYTICS_NAME;"