from datetime import datetime


class App_logger:
    def log(self, file_object, log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime('%H:%M:%s')
        file_object.write(str(self.date) + " /" + str(self.current_time) + "\t\t" + log_message + "\n")