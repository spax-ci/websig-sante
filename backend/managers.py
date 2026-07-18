from django.contrib.auth.models import BaseUserManager


class CustomUerManager(BaseUserManager):
    # Méthode permettant de créer un utilisateur
    def create_user(
        self, 
        # Adresse email pour s'authentifier
        email,
        # Mot de passe  pour s'authentifier
        password = None,
        # Rôle utilisateur
        code_role  = None,
        # Dictionnaire contenant les autres champs du modèle
        **extra_fields
    ):
        # Vérifier que l'adresse e-mail est renseigné
        if not email:
            
            # si le mail n'est pas fourni, lever une exception
            raise ValueError(
                "L'adresse email n'est pas fournie"
            )
        # Normaliser l'adresse email
        email = self.normalize_email(email)
        
        # Créer l'utilisateur
        user = self.model(
            email = email,
            code_role = code_role,
            **extra_fields
        )
        
        # Stocker le mot de passe
        user.set_password(password)
        
        # Enregistrer l'utilisateur dans la base de données
        user.save(using=self._db)
        
    # Créer le supper admin
    def create_superuser(
        self, 
        # Adresse email pour s'authentifier
        email,
        # Mot de passe  pour s'authentifier
        password = None,
        # Rôle utilisateur
        code_role  = None,
        # Dictionnaire contenant les autres champs du modèle
        **extra_fields
    ):
        extra_fields.setdefault(
            "is_staff",
            True
        )
        
        extra_fields.setdefault(
            "is_superuser",
            True
        )
        
        extra_fields.setdefault(
        "is_active",
        True
        )
        
        return self.create_user(
             self, 
            # Adresse email pour s'authentifier
            email,
            # Mot de passe  pour s'authentifier
            password = None,
            # Rôle utilisateur
            code_role  = None,
            # Dictionnaire contenant les autres champs du modèle
            **extra_fields
        )