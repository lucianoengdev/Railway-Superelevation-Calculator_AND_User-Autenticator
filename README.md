# Railway-Superelevation Calculator and #User-Autenticator

## 📖 About the Project
This project is a robust web application designed for **Transport Engineers** and students. It combines a secure user authentication system with a specialized calculator for **Railway Geometric Design**. 

The main goal is to automate the complex calculations required to determine the correct Superelevation of a railway curve, ensuring the safety and comfort of passengers and cargo.

## ⚙️ Features
* User Authentication: Secure Login, Registration, and Logout system using password hashing.
* Railway Calculator: Determines the required superelevation ($h$) based on four critical engineering criteria:
    1.  Theoretical Criterion: Equilibrium of centrifugal force.
    2.  Safety Criterion (Dynamic): Stability of the vehicle while in motion.
    3.  Safety Criterion (Static): Stability of the vehicle when stopped on the curve.
    4.  Comfort Criterion: Limits the uncompensated lateral acceleration for passengers.
* Responsive Interface: Clean UI built with Bootstrap 5.

## 🛠️ Technologies Used
* Language: Python
* Web Framework: Flask
* Database: SQLite (via SQLAlchemy)
* Security: Flask-Bcrypt (for password hashing), Flask-Login
* Frontend: HTML5, CSS3, Bootstrap 5, Jinja
* Math: Custom engineering algorithms based on standard railway mechanics.

## 🚀 Project Ambition
The ambition of this project is to become a handy, quick-reference tool for railway engineers to validate track parameters instantly. It aims to bridge the gap between theoretical formulas and practical, on-the-fly verification in the field or office.

## 📍 Current Stage
Status: Finished (v1.0)
The application is fully functional. Users can register, log in, perform calculations with real-world variables (Speed, Radius, Gauge, etc.), and view the results immediately.

## 🐛 Known Issues & Future Improvements
While the project is finished, there is always room for evolution:
* Unit Conversion: Currently accepts inputs in standard metric units (meters, km/h). Future updates could include unit conversion (mm, cm).
* Calculation History: We have a database for users, but currently, we do not save the calculation history. This is a planned feature.
* Formula Standards: The calculations are based on specific academic literature (CEFET-MG/AREMA based). Adding a toggle for different international standards (UIC, ABNT) would be a great addition.

---
*Developed by Luciano Faria - Transport Engineer*