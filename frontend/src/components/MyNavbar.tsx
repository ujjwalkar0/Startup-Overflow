import { 
    Button, 
    Container, 
    Form, 
    FormControl, 
    Nav, 
    Navbar,
    NavDropdown 
} from "react-bootstrap";

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

type Props = {
    children: JSX.Element,
}



const UserMenu = () => {
    return (
        <Nav>
            <Nav.Link href="/posts/add">Add New Post</Nav.Link>
            <Nav.Link href="/questions">Ask</Nav.Link>
            <Nav.Link href="/logout">Logout</Nav.Link>
        </Nav>
    )
}

const Menu = () => {
    return (
        <Nav>
            <Nav.Link href="/register">Register</Nav.Link>
        </Nav>
    )
}

const MyNavbar = ({children}:Props) => {
    const token = localStorage.getItem("token")
    return(
        <div>
            <Navbar bg="dark" variant="dark" expand="lg">
            <Container>
                <Navbar.Brand href="#home">Startup Overflow</Navbar.Brand>
                <Navbar.Toggle />
                <Navbar.Collapse className="justify-content-end">
                    {token==null ? <Menu/> : <UserMenu/> }
                </Navbar.Collapse>
            </Container>
            </Navbar>
            {children}
        </div>
    )
}

export default MyNavbar;