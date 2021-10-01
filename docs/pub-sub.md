# GCP Pub/Sub

- Can handle duplicate messages
- Messaging order is not guaranteed

![](pub-sub.png)

We can have many different orders, dropping into message queue.

![](pub-sub-buffer.png)

## Fan Out Messages

Orders are fanned out to inventory and payment.

![](pub-sub-fan.png)