from django.db import models

# Create your models here.
status_choices = [
    'to-do',  # for a project that is yet to be started, no team lead, no team
    'in-progress', # for a project that has a team lead and a team, assigned tasks, and is in progress
    'done' # for a project that has been completed and approved by the project owner
    'review', # for a project that has been completed and is awaiting approval by the project owner
    'archived' # for a project that was never completed and is no longer being worked on
]


class User(models.Model):
    """_summary_

    Args:
        models (_type_): User model that has the following attributes:
        first_name (_type_): First name of the user
        last_name (_type_): Last name of the user
        user_name (_type_): User name of the user which will be used for login purposes. Must be unique. 
        email (_type_): Email of the user which will be used for login purposes. Must be unique.
        password (_type_): Password of the user which will be used for login purposes.
        created_at (_type_): Date and time the user was created.
        
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    
    
    
class Project(models.Model):
    """
    

    Args:
        models (_type_): Project model that has the following attributes:
        name (_type_): Name of the project
        description (_type_): Description of the project
        created_at (_type_): Date and time the project was created.
        updated_at (_type_): Date and time the project was last updated.
        due_date (_type_): Date and time the project is due.
        project_owner (_type_): User who owns the project.
        status (_type_): Status of the project. Can be one of the following: to-do, in-progress, done, review, archived.
        team_lead (_type_): User who is the team lead of the project.
        team (_type_): User who is on the team of the project.
        tasks (_type_): Tasks that are assigned to the project.
        
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_owner')
    status = models.CharField(max_length=100, default='to-do')


    

class Task(models.Model):
    """_summary_

    Args:
        models (_type_): Task model that has the following attributes:
        name (_type_): Name of the task
        description (_type_): Description of the task
        created_at (_type_): Date and time the task was created.
        due_date (_type_): Date and time the task is due.
        project_id (_type_): Project that the task is assigned to.
        task_owner (_type_): User who is the task owner.
        estimated_time (_type_): Estimated time to complete the task.
        actual_time (_type_): Actual time to complete the task.
        status (_type_): Status of the task. Can be one of the following: to-do, in-progress, done, review, archived.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='task_owner')
    estimated_time = models.IntegerField()
    actual_time = models.IntegerField()  
    status = models.CharField(max_length=100, default='to-do')
    
class Team(models.Model):
    """
    

    Args:
        models (_type_): Team model that has the following attributes:
        name (_type_): Name of the team
        description (text): Description of the team
        created_at (datetime): Date and time the team was created.
        team_lead (User model): User who is the team lead of the team.
        members (list of users): Users who are on the team.
        project (project_id): Project that the team is assigned to.       
        
    """
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    team_lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_lead')
    members = models.ManyToManyField('User')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')