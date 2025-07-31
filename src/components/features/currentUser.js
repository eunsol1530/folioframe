let currentUser = JSON.parse(decrypt(localStorage.getItem("currentUser"))) || null;

export const setCurrentUser = (user) => {
  currentUser = user;
  localStorage.setItem("currentUser", encrypt(JSON.stringify(user)));
};

export const getCurrentUser = () => {
  return currentUser;
};

export const clearCurrentUser = () => {
  currentUser = null;
  localStorage.removeItem("currentUser"); // 로그아웃 시 localStorage에서 제거
};

// Example encryption and decryption functions
function encrypt(data) {
  // Implement encryption logic here
  return btoa(data); // Using base64 for demonstration; replace with strong encryption
}

function decrypt(data) {
  // Implement decryption logic here
  return atob(data); // Using base64 for demonstration; replace with strong decryption
}
