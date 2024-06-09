// appfront/src/api/api.js
import axiosInstance from './index'

const axios = axiosInstance

export const login = (username, passwd) => {  
    return axios.post(`http://127.0.0.1:8000/api/users/login/`, {  
      'username': username,  
      'password': passwd  
    });  
  }

export const normRegister = (username, email, passwd, repass) => {  
return axios.post(`http://127.0.0.1:8000/api/users/register/user`, {  
    "username":username,
    "user_email":email,
    "password":passwd,
    "confirm_password":repass
});  
}

export const DocRegister = (username, email, passwd, repass, id, name, cno) => {  
    return axios.post(`http://127.0.0.1:8000/api/users/register/doctor`, {  
        "username": username, 
        "user_email": email,
        "password": passwd, 
        "confirm_password": repass, 
        "ID_number": id, 
        "real_name": name, 
        "certificate_number": cno
    });  
}

export const getNormList = () => {  
    return axios.get(`http://127.0.0.1:8000/api/shop/user/goods/`);  
}

export const sortList = (elem) => {  
    return axios.get(`http://127.0.0.1:8000/api/shop/user/goods/?ordering=${elem}`);  
}

export const searchList = (elem) => {  
    return axios.get(`http://127.0.0.1:8000/api/shop/user/goods/?search=${elem}`);  
}