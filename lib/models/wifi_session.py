class WifiSession:
    def __init__(self, session_id, user_id, duration_minutes, status):
        self.id =session_id
        self.user_id = user_id
        self.duration_minutes = duration_minutes
        self.status =status