import Register from './users/Register'
import Login from './users/Login'
import { Route, Routes } from 'react-router-dom';
import {CookiesProvider} from 'react-cookie';
import Posts from './Posts/Posts';
import Hashtag from './Hashtag/Hashtag';
import 'bootstrap/dist/css/bootstrap.min.css';
import Logout from './users/Logout';
import AddPost from './Posts/AddPosts';
import Tags from './Hashtag/Tags';


function App() {
  return (
    <CookiesProvider>
      <Routes>
        <Route path="/posts" element={<Posts/>} />
        <Route path="/register" element={<Register/>} />
        <Route path="/" element={<Login/>} />
        <Route path="/logout" element={<Logout/>} />
        {/* <Route path="/tags" element={<Tags/>} /> */}
        <Route path="/hashtag" element={<Hashtag/>} />
        <Route path="/posts/add" element={<AddPost/>} />
      </Routes>
    </CookiesProvider>
  );
}

export default App;
