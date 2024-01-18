# The Base Image for subsequent instructions.
FROM node:14

# App directory
WORKDIR /app

# Install app dependencies
COPY package*.json ./

# Install tools required for project
RUN npm install

# Copy the entire project 
COPY . .

# Listening Ports 
EXPOSE 3000

# RUN app node.js in /app1
CMD [ "node", "index.js" ] 
