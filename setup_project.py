import click
from cookiecutter.main import cookiecutter

# Define the path to your cookiecutter template
TEMPLATE_PATH = 'ml-project-template'

@click.command()
@click.option('--project_name', prompt='Project Name', default='ml_project', help='Project Name, used as the project directory name.')
@click.option('--author', prompt='Author name', default='jimmfan', help='The name of the project author.')
@click.option('--email', prompt='Author email', default='jimmfan@github.com', help='The email of the project author.')
@click.option('--python_version', prompt='Python version', default='3.10', help='The Python version to use for the project.')

def create_project(project_name, author, email, python_version):
    # Additional project-specific prompts can be added here

    # Call cookiecutter to create the project using the collected inputs
    cookiecutter(
        TEMPLATE_PATH,
        no_input=True,
        extra_context={
            'project_name': project_name,
            'author': author,
            'email': email,
            'python_version': python_version
            # Add other variables to pass to cookiecutter here
        }
    )

    click.echo(f'Project {project_name} created successfully.')

if __name__ == '__main__':
    create_project()
