class Event():
    def __init__(self, date, id, title="None", color="blue"):
        # date is tuple: (day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday), hour)
        self.id = id
        self.date = date
        self.title = title
        self.color = color

    def set_date(self, date):
        self.date = date

    def set_title(self, title):
        self.title = title 

    def set_color(self, color):
        self.color = color 

    def get_info(self):
        return {
                "date": self.date,
                "title": f"[on {self.color}]{self.title}[/on {self.color}]",
                "color": self.color,
                "id": self.id
                }
