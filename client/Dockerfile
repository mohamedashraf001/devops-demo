# --------- Build Stage ----------
FROM node:20 AS build

WORKDIR /app

# نسخ ملفات البروجكت
COPY package*.json ./
RUN npm install

COPY . .

# build للـ Angular app
RUN npm run build -- --configuration production

# --------- Nginx Stage ----------
FROM nginx:alpine

# نسخ الـ build output للـ Nginx
COPY --from=build /app/dist/client/browser /usr/share/nginx/html

# نسخ ملف nginx.conf (ممكن نعدله بعدين)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
