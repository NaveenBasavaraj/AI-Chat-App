# reactchat/Dockerfile (dev)
FROM node:18

WORKDIR /app

# copy only package manifest first (faster caching)
COPY package*.json ./
RUN npm ci

# copy source
COPY . .

# Expose Vite port
EXPOSE 5173

# Make Vite bind to 0.0.0.0 so it is reachable from outside container
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
