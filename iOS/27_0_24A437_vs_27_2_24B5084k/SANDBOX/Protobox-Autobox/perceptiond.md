## perceptiond

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.userprofiles"))
 		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
+		(require-not (global-name "com.apple.dockaccessoryd"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (require-any
 			(global-name "com.apple.audio.isolated.client.service")
```
