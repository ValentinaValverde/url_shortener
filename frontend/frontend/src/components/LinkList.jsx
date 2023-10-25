import { useState, useEffect } from "react"


export const LinkList = () => {
    const [linkList, setLinkList] = useState([])

    useEffect(() => {
        const url = "http://localhost:8000/urls/"
        const getList = async () => {
            const data = await fetch(url, {
                method: 'GET',
                headers: {
                    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MTc5NjI1LCJpYXQiOjE2OTgxNzc4MjUsImp0aSI6IjI2MmIxOTEyZjQyNDQ4NWQ4M2U4MDU0MTJiOTQ2MTdjIiwidXNlcl9pZCI6MX0.qMOHThr_cNh7nxUT2zPgyu_5KPPjr8-3h-ml1iiGVBU'
                }
            })
            const linkData = await data.json()
            
            console.log("DATA: ", data)
            setLinkList(linkData) 
        }
        getList();
    }, []);
    
    console.log("LINK LIST: ", linkList)

    return (
        <>
            <ul>
                {linkList.map((link, index) => {
                    return (
                        <li key={index}>
                            {link.title}
                        </li>
                    );
                })}
            </ul>
        </>
    );
};