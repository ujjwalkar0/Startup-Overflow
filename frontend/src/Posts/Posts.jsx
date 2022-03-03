import { useEffect, useState } from 'react';
import { Button, Card, Container, Row, Col } from 'react-bootstrap';
import { Navigate } from 'react-router-dom';
import MyNavbar from '../components/MyNavbar';
import Login from '../users/Login';

function Post(props){
  return(
    <div>
      <Card className='card'>
      <Card.Body>
      <Row xs={1} sm={2} md={2} lg={2}>
        <Col className='card-image' style={{ width: '18rem' }}>
          <Card.Img variant="top" src="holder.js/100px180"/>
        </Col>
        <Col>
          <Card.Title>{props.title}</Card.Title>
          <Card.Text>
            {props.desc}
          </Card.Text>
        </Col>
        </Row>
      </Card.Body>
      </Card>
      
      {/* 
        <Card.Body>
        <Card.Img variant="top" src="holder.js/100px180" />
          <Card.Title>{props.title}</Card.Title>
          <Card.Text>
            {props.desc}
          </Card.Text>
          <Button variant="primary">Go somewhere</Button>
        </Card.Body>
      </Card> */}
    </div>
  )
}

function MyPosts(){
  const [posts, setPosts] = useState([])
  const token = localStorage.getItem("token")

  useEffect(() => {
    fetch('http://127.0.0.1:8000/posts/',{
      method:"GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Token ${token}`
      }
  })
  .then(resp => resp.json())
  .then(resp => setPosts(resp))
  .catch(error => console.log(error))
  },[])
  console.log(posts==0)
  // console.log(posts)

  return (
    <Container>
        
          {posts==0 ? <h4>No Post Found</h4> :posts.map(post=><Post key={post.id} title={post.title} desc={post.desc}/>)}
        {/* </Row> */}
    </Container>
  );
}



function Posts() {
  const token = localStorage.getItem("token")
  console.log(token)

  return(
      <div>
        <MyNavbar>
          {localStorage.getItem("token")==null? window.setTimeout(()=>{window.location.reload()}): <MyPosts/>}
        </MyNavbar>
      </div>
  )
}

export default Posts;