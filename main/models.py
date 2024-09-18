from django.db import models

class StartupDetails(models.Model):
    startup_name = models.CharField(max_length=255, unique=True)  # unique to ensure no duplicate startup names
    idea_description = models.TextField()
    business_domain = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)

    def __str__(self):
        return self.startup_name


class NonFunctionalRequirements(models.Model):
    startup = models.ForeignKey(StartupDetails, on_delete=models.CASCADE)

    def __str__(self):
        return f"Non-Functional Requirement for {self.startup.startup_name}"


class FunctionalRequirements(models.Model):
    startup = models.ForeignKey(StartupDetails, on_delete=models.CASCADE)
    business_domain = models.CharField(max_length=255)
    application_features = models.JSONField()  # stores array of features
    data_management = models.JSONField()       # stores array of data management requirements

    def __str__(self):
        return f"Functional Requirements for {self.startup.startup_name}"


class Scalability(models.Model):
    startup = models.ForeignKey(StartupDetails, on_delete=models.CASCADE)
    non_functional_req = models.ForeignKey(NonFunctionalRequirements, on_delete=models.CASCADE)
    expected_number_of_users = models.IntegerField()
    expected_number_of_transactions_per_second = models.IntegerField()

    def __str__(self):
        return f"Scalability for {self.startup.startup_name}"


class Deployment(models.Model):
    startup = models.ForeignKey(StartupDetails, on_delete=models.CASCADE)
    non_functional_req = models.ForeignKey(NonFunctionalRequirements, on_delete=models.CASCADE)
    cloud_provider = models.CharField(max_length=255)
    deployment_model = models.CharField(max_length=255)

    def __str__(self):
        return f"Deployment for {self.startup.startup_name}"


class Performance(models.Model):
    startup = models.ForeignKey(StartupDetails, on_delete=models.CASCADE)
    non_functional_req = models.ForeignKey(NonFunctionalRequirements, on_delete=models.CASCADE)
    response_time = models.CharField(max_length=255)
    throughput = models.CharField(max_length=255)

    def __str__(self):
        return f"Performance for {self.startup.startup_name}"


class Security(models.Model):
    startup = models.ForeignKey(StartupDetails, on_delete=models.CASCADE)
    non_functional_req = models.ForeignKey(NonFunctionalRequirements, on_delete=models.CASCADE)
    authentication = models.TextField()
    authorization = models.TextField()

    def __str__(self):
        return f"Security for {self.startup.startup_name}"


class Reliability(models.Model):
    startup = models.ForeignKey(StartupDetails, on_delete=models.CASCADE)
    non_functional_req = models.ForeignKey(NonFunctionalRequirements, on_delete=models.CASCADE)
    uptime = models.CharField(max_length=255)
    backup = models.CharField(max_length=255)
    recovery = models.CharField(max_length=255)

    def __str__(self):
        return f"Reliability for {self.startup.startup_name}"


class Maintainability(models.Model):
    startup = models.ForeignKey(StartupDetails, on_delete=models.CASCADE)
    non_functional_req = models.ForeignKey(NonFunctionalRequirements, on_delete=models.CASCADE)
    code_quality = models.TextField()
    documentation = models.TextField()
    monitoring = models.TextField()

    def __str__(self):
        return f"Maintainability for {self.startup.startup_name}"


class Cost(models.Model):
    startup = models.ForeignKey(StartupDetails, on_delete=models.CASCADE)
    non_functional_req = models.ForeignKey(NonFunctionalRequirements, on_delete=models.CASCADE)
    budget = models.CharField(max_length=255)
    cost_estimation = models.TextField()
    licensing = models.TextField()

    def __str__(self):
        return f"Cost for {self.startup.startup_name}"
