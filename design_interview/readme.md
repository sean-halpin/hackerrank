# General Design Interview Strategy

Given that an interviewer may start a design interview with "Design Youtube", we should then; 
- Clarify the requirements the system must meet
  - Which part of youtube do they want designed? Upload/Viewing/Comments/Likes?
- Work backwards from the customer/user experience
  - Do they want video discovery/suggestions/search engine?
    - We use this to limit the scope of what we are designing, as designing the whole of youtube in an hour is not feasible. 
- Define Scaling Requirements
  - How many users? hundereds or millions, etc
  - How often do users visit, try to determine what is the transaction rate in the system.
  - Scale of the data, videos per day, retention time
    - Likely we will need every trick in the book for horizontally scaled servers and data storage
  - Some tools may not need this level of scaling and complexity
    - Always prefer the simplest solution, vertical scaling may be enough.
- Define Latency Requirements
  - How fast is fast enough?
    - This informs us of the need for caching & CDN 
      - Caching is not strictly a scaling tool, but used to reduce load on services and data stores
    - Try to express this as SLA language, eg 100ms at 3 9s latency
- Define Availability Req's
  - Is being down a threat to the business or just an invonveniance?
  - If we need high availability, design for redundancy across many regions/racks/data centres.
- Back of the envelope estimations may be required for estimates of the above. 
- Sketch out the design, starting with high level components
  - How do they scale?
  - How are they distributed for availability?
- Identify bottlenecks, maintenance, costs or concerns as you go. 
- Highlight the tradeoffs between choices available
- Interviewer will try to poke holes in the design, be prepared to answer for;
  - What happens if X component fails?
  - What happens if there is a surge of traffic or data?
  - Did you meet scaling & availability requirements? How?
  - Did the system meet all use cases?
  - How would you make it better?
  - How would you simplify?
  - How would you optimize?
  - What is the operational burden?
  - How would you monitor it?

# URL Shortening Service Considerations

