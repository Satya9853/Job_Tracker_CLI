# purpose -> Tracking and keeping records of jobs

# Structure
# add job name, address, email, title, salary, status, job_type
# view all-jobs
# search "job" by name, title, status
# edit job 
# delete job

import click
import terminaltables
from database import connectDB


# CONSTANTS
HEADERS = ["Company Name", "Address", "Title", "Email", "Jobtype", "Salary", "Status"]


@click.group()
@click.version_option(prog_name="job tracker ClI", version="0.01")
def main():
    """Job tracker CLI - Job tracking and record keeping CLI"""
    pass


#  add job functionality
@main.command()
@click.option("--name", "-n", help="Name of the Company", type=str, prompt="Company Name")
@click.option("--address", "-a", help="address of the Company", type=str, prompt="Company Address")
@click.option("--email", "-e", help="Email of the Company", type=str, prompt="Company Email")
@click.option("--title", "-t", help="Title Of The Job", type=str, prompt="Job Title")
@click.option("--salary", "-s", help="Salary Of The Job", type=float, prompt="Salary")
@click.option("--status", "-st", help="Status Of The Job", prompt="Status", type=click.Choice(["Pending", "Cancelled", "Success"]))
@click.option("--jobtype", "-jt", help="Type Of The Job", type=click.Choice(["Full-Time", "Remote", "Part-Time", "Contract"]), prompt="Job Type")
def add_job(name, address, email, title, salary, status, jobtype):
    """ add job -> name, address, email, title, salary, status, job_type"""

    click.secho("\n\nAdding Job ...", fg="blue", bg="white")
    click.echo("\n\n===========Summary===========")

    job_table_setup = [
        ["Job Info", "Details"],
        ["Company Name", name],
        ["Company Address", address],
        ["Company Email", email],
        ["Job Title", title],
        ["Job Salary", salary],
        ["Status", status],
        ["Job Type", jobtype],
    ]

    connectDB.create_table()
    connectDB.add_data(name, address, email, title, salary, status, jobtype)

    table = terminaltables.AsciiTable(job_table_setup)
    click.secho(table.table, fg="yellow")
    click.secho("Saved Job To Database", fg="green")


# show all job
@main.command()
def show_all_job():
    """Show All Job"""
    result = connectDB.show_all_jobs()
    result = [HEADERS] + result
    table = terminaltables.AsciiTable(result)
    click.secho(f"\n\n{table.table}", fg="yellow")


# view job functionality
@main.command()
@click.option("--title", "-t", prompt=True, help="View Job By Title")
def view_job(title):
    """ view jobs"""
    click.secho(f"\n\n Searching Job with Title -> {title} ...", fg="blue", bg="white")
    result = connectDB.get_job_by(text=title,  field="title")
    if len(result) == 0:
        click.secho(f"\n\nNo Job Was Found With Title -> {title}", fg="yellow")
        return
    result = [HEADERS] + result
    table = terminaltables.AsciiTable(result)
    click.secho(f"\n\n{table.table}", fg="yellow")


# search job functionality
@main.command()
@click.argument("text")
def search_job():
    """ search "job" by name, title, status"""
    click.echo("search job")
    
    
# edit job functionality
@main.command()
def edit_job():
    """edit a job"""
    click.echo("edit job")


# delete job functionality
@main.command()
def delete_job():
    """delete a job"""
    click.echo("delete job")


if __name__ == "__main__":
    main()
    