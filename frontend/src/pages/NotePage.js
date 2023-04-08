import React, {useState, useEffect} from 'react'
import { Link, useParams } from 'react-router-dom'
import { ReactComponent as Icon} from "../assets/arrow-left.svg"
//import { withRouter } from 'react-router-dom';
//import { useHistory } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

const NotePage = () => {

    const { id } = useParams();
    let [note, setNote] = useState(null)
    const history = useNavigate();
    
    useEffect(() => {
        getNote()
    }, [id])

    let getNote = async () => {
        if (id === 'new') return 

        let response = await fetch(`/api/${id}`)
        let data = await response.json()
        setNote(data)
    }

    let createNote = async () => {
        fetch('/api/create/', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })
    }
    
    let updateNote = async () => {
        fetch(`/api/${id}/update/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })
    }
    

    let handleSubmit = () => {
        console.log('NOTE:', note)
        if (id !== 'new' && note.body == '') {
            deleteNote()
        } else if (id !== 'new') {
            updateNote()
        } else if (id === 'new' && note.body !== null) {
            createNote()
        }
        history('/')
    }

    let deleteNote = async () => {
        fetch(`/api/${id}/delete/`, {
            method: 'DELETE',
            'headers': {
                'Content-Type': 'application/json'
            }
        })
        history('/')
    }

    let handleChange = (value) => {
        setNote(note => ({ ...note, 'body': value }))
        console.log('Handle Change:', note)
    }

    return (
        <div className="note">
            <div className='note-header'>
                <h3>
                    <Icon onClick={handleSubmit}/>
                </h3>
                {id !== 'new' ? (
                    <button onClick={deleteNote}>Delete</button>
                ) : (
                    <button onClick={handleSubmit}>Done</button>
                )}
            </div>
            <textarea onChange={(e) => { handleChange(e.target.value) }} value={note?.text}></textarea>
        </div>
    )
}

export default NotePage
