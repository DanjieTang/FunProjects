export default function userGreeting(props) {
    if (props.isLoggedIn) {
        return <h2>Welcome {props.userName}</h2>
    }else{
        return <h2>Please login to continue</h2>
    }
    // return
}