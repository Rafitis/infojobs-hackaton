import { useState, useEffect } from 'react';
import { Text, Icon } from "@tremor/react";
import { PlayIcon, PauseIcon } from "@heroicons/react/solid";

const AudioContext = window.AudioContext || window.webkitAudioContext
const context = new AudioContext()
const playSound = context.createBufferSource()

export function JobSumary({ job_id }) {
    const [sumary, setSumary] = useState("")
    const [loading, setLoading] = useState(false)

    const api_key = import.meta.env.VITE_ELEVENLABS_API_KEY
    const [playing, setPlaying] = useState(false)


    const handleStop = () => {
        playSound.stop(context.currentTime)
        setPlaying(false)

    }

    const handlePlay = async (sumary) => {

        const voice_id = 'jwFrUxxY6tVy1pMGyASd'

        let audio
        if (!playing) {
            setPlaying(true)
            await fetch(
                `https://api.elevenlabs.io/v1/text-to-speech/${voice_id}`,
                {
                    method: 'POST',
                    headers: {
                        "Accept": "audio/mpeg",
                        "Content-Type": "application/json",
                        "xi-api-key": api_key
                    },
                    body: JSON.stringify({
                        'text': `${sumary}`,
                        'model_id': 'eleven_multilingual_v1',
                        'voice_settings': {
                            'stability': 0.9,
                            'similarity_boost': 0.9
                        }
                    })
                }
            ).then(data => data.arrayBuffer())
                .then(arrayBuffer => context.decodeAudioData(arrayBuffer))
                .then(decodedAudio => {
                    audio = decodedAudio
                })

        }

        playSound.buffer = audio
        playSound.connect(context.destination)
        playSound.start(context.currentTime)

        playSound.onended = () => {
            setPlaying(false)
        }

    }

    const callSumarizer = async (offer) => {
        const sumaryResponse = await fetch(`http://localhost:8000/openai/summary/?job_offer=${JSON.stringify(offer)}`, {
            method: 'POST',
        })
        const offerSumary = await sumaryResponse.json()

        return offerSumary
    }

    const getOfferData = async (id) => {
        setLoading(true)

        const res = await fetch(`http://localhost:8000/infojobs/data/offer/${id}/`)

        const offer = await res.json()

        const offerSumary = await callSumarizer(offer)

        setSumary(offerSumary)
        setLoading(false)
    }

    useEffect(() => {
        getOfferData(job_id)
    }, [])

    return (
        <>
            <Icon
                className='cursor-pointer'
                size="xl"
                icon={playing ? PauseIcon : PlayIcon}
                onClick={() => playing ? handleStop() : handlePlay(sumary)} />
            <Text className="mt-2">{loading ? 'Loading...' : sumary}</Text>
        </>
    )
}   