from flask import Flask, request, jsonify

app = Flask(__name__)

# Fonction pour calculer les scores SISR et SLAM
def get_scores(text):
    sisr_keywords = [
        'serveur', 'réseau', 'virtualisation', 'sécurité', 'cloud', 'firewall', 'routeur', 'switch', 'dns',
        'maintenance', 'système', 'linux', 'windows server', 'infrastructure', 'vpn', 'backup', 'stockage',
        'datacenter', 'virtual machine', 'active directory', 'supervision', 'monitoring', 'déploiement', 'configuration',
        'administration système', 'cybersécurité', 'pare-feu', 'protocole', 'tcp/ip', 'ftp', 'ssh', 'smtp', 'udp',
        'hyperviseur', 'containers', 'docker', 'kubernetes', 'ip', 'wifi', 'internet des objets', 'networks',
        'cloud computing', 'cisco', 'microsoft', 'routing', 'switching', 'backup', 'ldap', 'vlan', 'nas', 'san',
        'exploitation', 'infrastructure IT', 'automatisation', 'administration réseaux', 'raspberry pi', 'informatique embarquée',
        'monitoring réseau', 'administration cloud', 'docker', 'apache', 'nginx', 'serveur web', 'redhat', 'centos'
    ]

    slam_keywords = [
        'application', 'base de données', 'développement', 'web', 'html', 'css', 'javascript', 'python', 'java', 'php',
        'sql', 'mysql', 'postgresql', 'oracle', 'mongodb', 'api', 'frontend', 'backend', 'framework', 'node.js', 'angular',
        'react', 'vue.js', 'django', 'flask', 'spring', 'laravel', 'express', 'programmation', 'algorithme', 'modélisation',
        'uml', 'rest', 'soap', 'mobile', 'android', 'ios', 'swift', 'kotlin', 'interface utilisateur', 'design',
        'responsive', 'test unitaire', 'debugging', 'optimisation', 'devops', 'intégration continue', 'gestion de projet',
        'logiciel', 'architecture logicielle', 'git', 'github', 'gestionnaire de version', 'cloud computing', 'microservices',
        'react native', 'xcode', 'android studio', 'typescript', 'webpack', 'mongodb', 'postgres', 'api rest', 'graphql',
        'ui/ux', 'testing', 'mockups', 'cypress', 'selenium', 'jenkins', 'docker', 'redux', 'material ui', 'expressjs',
        'angularjs', 'vuejs', 'typescript', 'docker', 'laravel', 'spring boot', 'nosql', 'firebase', 'angular 2+', 'scrum',
        'oop', 'mvc', 'webapi', 'flutter', 'ionic', 'tdd', 'bachelor informatique', 'frontend developer', 'backend developer'
    ]

    def apply_negative_logic(text, keywords, negative_keywords):
        if any(neg in text.lower() for neg in ['je n\'aime pas', 'pas de']):
            for keyword in keywords:
                if keyword in text.lower():
                    if any(neg_kw in text.lower() for neg_kw in negative_keywords):
                        return -1
        return 0

    sisr_score = sum(1 for word in sisr_keywords if word in text.lower())
    slam_score = sum(1 for word in slam_keywords if word in text.lower())

    sisr_score += apply_negative_logic(text, sisr_keywords, ['réseau', 'serveur', 'virtualisation', 'infrastructure', 'vpn', 'cloud', 'firewall', 'tcp/ip'])
    slam_score += apply_negative_logic(text, slam_keywords, ['html', 'css', 'java', 'mobile', 'développement', 'api', 'frontend', 'backend'])

    return sisr_score, slam_score

# Fonction pour classer le texte
def classify_text(text):
    sisr_score, slam_score = get_scores(text)
    if sisr_score > slam_score:
        return "SISR"
    elif slam_score > sisr_score:
        return "SLAM"
    else:
        return "Les deux filières sont possibles"

# Route principale pour tester l'API
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bienvenue sur l'API de classification SISR/SLAM !"})

# Route pour effectuer une classification
@app.route("/classify", methods=["POST"])
def classify():
    try:
        data = request.get_json()
        text = data.get("text", "")
        result = classify_text(text)
        return jsonify({"classification": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
