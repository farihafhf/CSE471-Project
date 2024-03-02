class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'due_date', 'priority']
