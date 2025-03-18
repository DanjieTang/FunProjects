function ConditionalDisplay(props){
    if (props.isStudent){
        return <h1>We're in</h1>
    }else{
        return <h1>We're out</h1>
    }
}

export default ConditionalDisplay