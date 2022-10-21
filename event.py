class Event():
    def __init__(self, date, title="None", color="blue"):
        # date is tuple: (day (M, TU, W, TH, F, SA, SU), hour)
        self.date = date
        self.title = title
        self.color = color

    def get_info(self):
        return {
                "date": self.date,
                "title": f"[on {self.color}]{self.title}[/on {self.color}]",
                "color": self.color
                }
