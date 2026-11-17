## nesessionmanager

> Group: ⬆️ Updated

```diff

 )
 
 (deny iokit-open-service)
+(allow iokit-open-service
+	(iokit-registry-entry-class "IOUserEthernetResource")
+)
 
 (deny iokit-set-properties)
 
```
