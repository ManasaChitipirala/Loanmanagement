class PropertyUtil:
    @staticmethod
    def get_property_string():
        server_name = "DESKTOP-BG1K7HN\SQLEXPRESS05"
        database_name = "LoanManagement"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )
        return conn_str
