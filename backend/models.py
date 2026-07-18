from django.contrib.gis.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Role Utilisateur
class RoleUtilisateur(models.Model):
    code_role = models.AutoField(primary_key=True, editable=False)
    libelle_role = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'role_utilisateur'
        managed = False
        verbose_name = 'rôle utilisateur'
        
    def __str__(self):
        return self.libelle_role
    
# Utilisateur
class Utilisateur(AbstractUser):
    num_utilisateur = models.AutoField(primary_key=True, editable=False)
    code_role = models.ForeignKey(
        RoleUtilisateur, on_delete=models.DO_NOTHING,
        db_column="code_role", null=True, blank=True
        )
    
    photo = models.TextField(null=True, blank=True)
        
    telephone_utilisateur = models.CharField(max_length=20, unique=True)
    
    email = models.EmailField(max_length=100, unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    
    class Meta:
        db_table = 'utilisateur'
        managed = False
        verbose_name = 'Utilisateur'
        
    def __str__(self):
        return self.email
    
        
       