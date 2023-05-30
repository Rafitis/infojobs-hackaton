import { useState, useEffect } from 'react';
import { Card, Subtitle, Metric, Text, Divider, Icon } from "@tremor/react";
import { JobSumary } from './JobSumary';
import { LinkIcon } from '@heroicons/react/solid';

export function JobsOffers() {
    const [offers, setOffers] = useState([]);

    const fetchOffers = async () => {
        const res = await fetch(
            'http://localhost:8000/infojobs/data/')

        const { items } = await res.json()

        const listOfOffers = items.map(item => {
            const { id, title, province, experienceMin, link } = item

            return {
                id,
                title,
                province: province.value,
                experienceMin: experienceMin.value,
                link,
            }
        })
        setOffers(listOfOffers)
    }

    useEffect(() => {
        fetchOffers()
    }, [])

    return (
        <div className="flex flex-wrap gap-2">
            {offers.map(item => (
                <Card className="max-w-lg mx-auto" key={item.id}>
                    <Text>Oferta
                        <Icon
                            className='cursor-pointer'
                            size="md"
                            icon={LinkIcon}
                            onClick={() => window.open(item.link)} />
                    </Text>
                    <Metric>{item.title}</Metric>
                    <Divider />
                    <Subtitle>Summary</Subtitle>
                    <JobSumary
                        job_id={item.id} />
                </Card>
            ))}
        </div>
    )
}