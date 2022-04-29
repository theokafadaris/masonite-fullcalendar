"""CreateEventsTable Migration."""

from masoniteorm.migrations import Migration


class CreateEventsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("events") as table:
            table.increments("id")
            table.string("title")
            table.date("start")
            table.date("end")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("events")
