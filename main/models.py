from django.db import models

# Startup Details Table
class StartupDetails(models.Model):
    STARTUP_STAGE_CHOICES = [
        ('Idea', 'Idea'),
        ('MVP', 'MVP'),
        ('Growth', 'Growth'),
        ('Scaling', 'Scaling')
    ]
    
    FUNDING_STATUS_CHOICES = [
        ('Bootstrapped', 'Bootstrapped'),
        ('Seed', 'Seed'),
        ('Series A', 'Series A'),
        ('Series B', 'Series B'),
        ('Series C', 'Series C')
    ]
    
    startup_name = models.CharField(max_length=100)
    founder_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    startup_stage = models.CharField(max_length=50, choices=STARTUP_STAGE_CHOICES)
    funding_status = models.CharField(max_length=50, choices=FUNDING_STATUS_CHOICES)
    number_of_employees = models.IntegerField()
    
    def __str__(self):
        return self.startup_name

# Functional Requirements Table
class FunctionalRequirements(models.Model):
    BUSINESS_DOMAIN_CHOICES = [
        ('E-commerce', 'E-commerce'),
        ('FinTech', 'FinTech'),
        ('HealthTech', 'HealthTech'),
        ('EdTech', 'EdTech'),
        ('Social Media', 'Social Media')
    ]
    
    APPLICATION_FEATURE_CHOICES = [
        ('User Authentication', 'User Authentication'),
        ('Payment Processing', 'Payment Processing'),
        ('Product Catalog', 'Product Catalog'),
        ('Social Media Integration', 'Social Media Integration'),
        ('Analytics', 'Analytics')
    ]
    
    USER_INTERFACE_CHOICES = [
        ('Home Page', 'Home Page'),
        ('Product Page', 'Product Page'),
        ('Checkout Page', 'Checkout Page'),
        ('Profile Page', 'Profile Page'),
        ('Dashboard', 'Dashboard')
    ]
    
    DATA_MANAGEMENT_CHOICES = [
        ('User Data', 'User Data'),
        ('Transaction Data', 'Transaction Data'),
        ('Product Data', 'Product Data'),
        ('Analytics Data', 'Analytics Data'),
        ('Logs', 'Logs')
    ]
    
    CLOUD_PROVIDER_CHOICES = [
        ('AWS', 'AWS'),
        ('Azure', 'Azure'),
        ('GCP', 'GCP')
    ]
    
    DEPLOYMENT_MODEL_CHOICES = [
        ('Single Region', 'Single Region'),
        ('Multi-Region', 'Multi-Region')
    ]
    
    startup = models.OneToOneField(StartupDetails, on_delete=models.CASCADE, related_name='functional_requirements')
    business_domain = models.CharField(max_length=50, choices=BUSINESS_DOMAIN_CHOICES)
    application_features = models.JSONField()
    user_interface = models.JSONField()
    data_management = models.JSONField()
    expected_number_of_users = models.IntegerField()
    expected_number_of_transactions = models.IntegerField()
    cloud_provider = models.CharField(max_length=50, choices=CLOUD_PROVIDER_CHOICES)
    deployment_model = models.CharField(max_length=50, choices=DEPLOYMENT_MODEL_CHOICES)
    
    def __str__(self):
        return f"Functional Requirements for {self.startup.startup_name}"

# Non-Functional Requirements Table
class NonFunctionalRequirements(models.Model):
    AUTHENTICATION_CHOICES = [
        ('OAuth', 'OAuth'),
        ('JWT', 'JWT'),
        ('Basic Auth', 'Basic Auth')
    ]
    
    AUTHORIZATION_CHOICES = [
        ('Role-Based Access Control', 'Role-Based Access Control'),
        ('Attribute-Based Access Control', 'Attribute-Based Access Control')
    ]
    
    BACKUP_CHOICES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly')
    ]
    
    RECOVERY_CHOICES = [
        ('Automated', 'Automated'),
        ('Manual', 'Manual')
    ]
    
    MONITORING_CHOICES = [
        ('Enabled', 'Enabled'),
        ('Disabled', 'Disabled')
    ]
    
    COST_ESTIMATION_CHOICES = [
        ('Accurate', 'Accurate'),
        ('Approximate', 'Approximate')
    ]
    
    LICENSING_CHOICES = [
        ('Open Source', 'Open Source'),
        ('Commercial', 'Commercial')
    ]
    
    startup = models.OneToOneField(StartupDetails, on_delete=models.CASCADE, related_name='nonfunctional_requirements')
    response_time = models.IntegerField(help_text="Response Time in milliseconds")
    throughput = models.IntegerField(help_text="Throughput in requests per second")
    authentication = models.CharField(max_length=50, choices=AUTHENTICATION_CHOICES)
    authorization = models.CharField(max_length=50, choices=AUTHORIZATION_CHOICES)
    uptime = models.FloatField(help_text="Uptime requirement in percentage")
    backup = models.CharField(max_length=50, choices=BACKUP_CHOICES)
    recovery = models.CharField(max_length=50, choices=RECOVERY_CHOICES)
    monitoring = models.CharField(max_length=50, choices=MONITORING_CHOICES)
    budget = models.FloatField(help_text="Budget per month in USD")
    cost_estimation = models.CharField(max_length=50, choices=COST_ESTIMATION_CHOICES)
    licensing = models.CharField(max_length=50, choices=LICENSING_CHOICES)
    
    def __str__(self):
        return f"Non-Functional Requirements for {self.startup.startup_name}"
