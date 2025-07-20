#!/bin/bash

# Talabat Dashboard Deployment Script
# This script prepares the dashboard for GitHub Pages deployment

echo "🚀 Preparing Talabat Dashboard for deployment..."

# Create necessary directories
mkdir -p data
mkdir -p assets

# Copy the main HTML file as index.html for GitHub Pages
cp improved_talabat_dashboard.html index.html

# Create data directory for future use
mkdir -p data
echo "✅ Created data/ directory for future analytics"

# Create .gitignore if it doesn't exist
if [ ! -f ".gitignore" ]; then
    cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
EOF
    echo "✅ Created .gitignore file"
fi

# Make the Python script executable
chmod +x scripts/update_analytics.py

echo "✅ Deployment preparation complete!"
echo ""
echo "📋 Next steps:"
echo "1. Initialize git repository: git init"
echo "2. Add files: git add ."
echo "3. Commit: git commit -m 'Initial commit'"
echo "4. Create GitHub repository"
echo "5. Push: git push origin main"
echo "6. Enable GitHub Pages in repository settings"
echo ""
echo "🌐 Your dashboard will be available at:"
echo "   https://yourusername.github.io/talabat-dashboard/" 