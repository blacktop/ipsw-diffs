## IMDMessageServicesAgent

> Group: ⬆️ Updated

```diff

 )
 
 (deny iokit-open-service)
+(allow iokit-open-service
+	(iokit-registry-entry-class "AppleKeyStore")
+)
 
 (deny iokit-set-properties)
 

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.donotdisturb.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.imdpersistence.IMDPersistenceAgent"))
 		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.donotdisturb.service.non-launching"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
```
