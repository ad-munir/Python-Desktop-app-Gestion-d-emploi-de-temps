import sqlite3

conn = sqlite3.connect('myDataBase.db')
cursor = conn.cursor()
# Create tables for all four classes
def create_tables():

    # Utilisateur (User) table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Utilisateur (
            id INTEGER PRIMARY KEY,
            nom TEXT,
            prenom TEXT,
            role TEXT,
            email TEXT
        )
    ''')

    # Cours (Course) table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cours (
            id INTEGER PRIMARY KEY,
            nom_cours TEXT,
            description TEXT
        )
    ''')

    # EmploiDuTemps (Schedule) table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS EmploiDuTemps (
            id INTEGER PRIMARY KEY,
            jour_semaine TEXT,
            heure_debut TEXT,
            heure_fin TEXT,
            cours_id INTEGER,
            utilisateur_id INTEGER,
            salle_id INTEGER,
            FOREIGN KEY (cours_id) REFERENCES Cours(id),
            FOREIGN KEY (utilisateur_id) REFERENCES Utilisateur(id),
            FOREIGN KEY (salle_id) REFERENCES Salle(id)
        )
    ''')

    # Salle (Room) table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Salle (
            id INTEGER PRIMARY KEY,
            nom_salle TEXT,
            capacite INTEGER
        )
    ''')

    conn.commit()

# CRUD functions for Utilisateur (User)
def create_utilisateur(id,nom, prenom, role, email):

    cursor.execute('INSERT INTO Utilisateur (id,nom, prenom, role, email) VALUES (?, ?, ?, ? ,?)', (id , nom, prenom, role, email))
    conn.commit()

def get_all_utilisateurs():

    cursor.execute('SELECT * FROM Utilisateur')
    utilisateurs = cursor.fetchall()
    return utilisateurs

def update_utilisateur_email(utilisateur_id, new_email):
 
    cursor.execute('UPDATE Utilisateur SET email = ? WHERE id = ?', (new_email, utilisateur_id))
    conn.commit()

def delete_utilisateur(utilisateur_id):
    cursor.execute('DELETE FROM Utilisateur WHERE id = ?', (utilisateur_id,))
    conn.commit()

# CRUD functions for Cours (Course)
def create_cours(nom_cours, description):
    cursor.execute('INSERT INTO Cours (nom_cours, description) VALUES (?, ?)', (nom_cours, description))
    conn.commit()

def get_all_cours():
 
    cursor.execute('SELECT * FROM Cours')
    cours = cursor.fetchall()
    return cours

def update_cours_description(cours_id, new_description):
    
    cursor.execute('UPDATE Cours SET description = ? WHERE id = ?', (new_description, cours_id))
    conn.commit()

def delete_cours(cours_id):

    cursor.execute('DELETE FROM Cours WHERE id = ?', (cours_id,))
    conn.commit()
   

# CRUD functions for EmploiDuTemps (Schedule)
def create_emploi_du_temps(jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id):
   
    cursor.execute('INSERT INTO EmploiDuTemps (jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id) VALUES (?, ?, ?, ?, ?, ?)', (jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id))
    conn.commit()

def get_all_emplois_du_temps():
  
    cursor.execute('SELECT * FROM EmploiDuTemps')
    emplois_du_temps = cursor.fetchall()
    return emplois_du_temps

def update_emploi_du_temps(emploi_du_temps_id, jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id):

    cursor.execute('UPDATE EmploiDuTemps SET jour_semaine = ?, heure_debut = ?, heure_fin = ?, cours_id = ?, utilisateur_id = ?, salle_id = ? WHERE id = ?', (jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id, emploi_du_temps_id))
    conn.commit()

def delete_emploi_du_temps(emploi_du_temps_id):

    cursor.execute('DELETE FROM EmploiDuTemps WHERE id = ?', (emploi_du_temps_id,))
    conn.commit()

# CRUD functions for Salle (Room)
def create_salle(nom_salle, capacite):
  
    cursor.execute('INSERT INTO Salle (nom_salle, capacite) VALUES (?, ?)', (nom_salle, capacite))
    conn.commit()

def get_all_salles():
  
    cursor.execute('SELECT * FROM Salle')
    salles = cursor.fetchall()
    return salles

def update_salle_capacite(salle_id, new_capacite):
    cursor = conn.cursor()
    cursor.execute('UPDATE Salle SET capacite = ? WHERE id = ?', (new_capacite, salle_id))
    conn.commit()

def delete_salle(salle_id):

    cursor.execute('DELETE FROM Salle WHERE id = ?', (salle_id,))
    conn.commit()


    # Create tables if they don't exist
# create_tables()
# create_utilisateur(4,"omar","chaara", "etudiant", "omarchaara@gmail.com")
# create_cours('POO', 'cours de programmation orienté objet en Java')
# print(get_all_cours())

# create_salle("S16", 50)
# create_salle("S17", 40)
# print(get_all_salles())