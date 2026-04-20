#!/bin/bash
# Q2 Prototype Local Server Startup Script

echo "🚀 Starting Q2 Prototype Server..."
echo ""

# Navigate to the prototype directory
cd "$(dirname "$0")"

# Kill any existing servers on port 8080
lsof -ti:8080 | xargs kill -9 2>/dev/null

# Start the server
echo "✓ Starting server on http://localhost:8080"
echo ""
echo "Your prototype is now available at:"
echo "   http://localhost:8080/q2-prototype.html"
echo ""
echo "Press Ctrl+C to stop the server"
echo "----------------------------------------"
echo ""

python3 -m http.server 8080
