


---


Following a [recommandation step by step guide](https://www.designgurus.io/blog/step-by-step-guide)

> Steps are Requirements, scale, interfaces, data, architecture, dive deep and bottlenecks

> Focus on 
>
> Scalability (growth traffic and data), reliability and fault tolerance (vs hardware or network failures), performance (lateny, balance loads), trade-off 

1. Requirements clarification
2. Scale estimation (metrics)
3. Interfaces definition (like system's core API, contracts between component)
4. Model data (identify entities, relationships)
5. High-Level Archi (db, servers, cache, user)
6. Dive deep in 
7. Bottlenecks identification

----


Some thematic dealing with distribution system performance :

1. vertical scaling 
2. preprocessing (cron, etc.)
3. backups (single point of failure)
4. horizontal scaling

Micro service Architecture

Distributed System (partitioning )

Load balancer

Decoupling

Logging

Extensible

---

Horizontal Scaling : 

pros : resilient (vs SPO), scales well,
cons : load balancer requirement, network calls, data consistency challenges 

Vertical Scaling

pros : inter process communication, consistent
cons : Single point of failure, hardware limit 
