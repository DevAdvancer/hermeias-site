from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Product data
products = {
    'mystiko': {
        'title': 'Mystiko',
        'subtitle': 'Secure Messaging Platform',
        'description': 'A next-generation secure messaging platform that puts your privacy first. With end-to-end encryption, self-destructing messages, and zero data collection, Hi ensures your conversations remain truly private.',
        'features': [
            'End-to-end encryption for all messages',
            'Self-destructing messages with customizable timers',
            'Zero data collection policy',
            'Secure file sharing with encryption',
            'Cross-platform support (iOS, Android, Web)',
            'Group messaging with advanced privacy controls',
            'Message recall and editing capabilities',
            'Offline messaging support'
        ],
        'technical_specs': [
            'AES-256 encryption',
            'Perfect forward secrecy',
            'Local message storage only',
            'Open-source cryptography',
            'Regular security audits'
        ]
    },
    'ensights': {
        'title': 'Ensights',
        'subtitle': 'Private LLM Analytics',
        'description': 'A revolutionary localized LLM solution that securely analyzes your company\'s sales data. Transform raw data into actionable insights while keeping your sensitive information completely private and on-premises.',
        'features': [
            'On-premises deployment options',
            'Custom LLM model training',
            'Real-time data analytics',
            'Interactive visualization dashboard',
            'Automated report generation',
            'Data privacy compliance tools',
            'Integration with existing systems',
            'Scalable architecture'
        ],
        'technical_specs': [
            'Containerized deployment',
            'GPU acceleration support',
            'REST API interface',
            'Multiple database connectors',
            'Enterprise-grade security'
        ]
    },
    'demole': {
        'title': 'DemoLe AI',
        'subtitle': 'AI-Powered Legal Assistant',
        'description': 'Democratizing legal assistance through AI trained on comprehensive legal data. Get instant access to legal information, document analysis, and guidance for common legal issues, making justice more accessible to all.',
        'features': [
            'Legal document analysis',
            'Case law research assistance',
            'Document template generation',
            'Legal requirement compliance checking',
            'Multi-jurisdiction support',
            'Plain language explanations',
            'Automated document review',
            'Legal deadline tracking'
        ],
        'technical_specs': [
            'NLP-based document processing',
            'Regular legal database updates',
            'Multi-language support',
            'GDPR compliant',
            'Secure document storage'
        ]
    },
    'info-haus': {
        'title': 'info-haus',
        'subtitle': 'Private Investigation Marketplace',
        'description': 'A secure marketplace connecting clients with verified private investigators. Whether you\'re seeking investigative services or offering your expertise, our platform ensures professional, confidential connections.',
        'features': [
            'Verified investigator profiles',
            'Secure messaging system',
            'Case management tools',
            'Secure file sharing',
            'Payment escrow service',
            'Rating and review system',
            'Compliance monitoring',
            'Confidentiality agreements'
        ],
        'technical_specs': [
            'Identity verification system',
            'Encrypted communications',
            'Secure payment processing',
            'Document watermarking',
            'Audit trail logging'
        ]
    }
}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/products/<product_name>')
def product_page(product_name):
    if product_name in products:
        return render_template('product.html', product=products[product_name])
    return "Product not found", 404

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)
@app.route('/comingsoon')
def targetpage():
    return render_template('comingsoon.html')

if __name__ == '__main__':
    app.run(ssl_context='adhoc', host='0.0.0.0', port=8443)