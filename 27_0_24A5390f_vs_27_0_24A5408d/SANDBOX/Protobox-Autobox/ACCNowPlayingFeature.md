## ACCNowPlayingFeature

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.MediaPlayer.MPRadioControllerServer"))
 		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.itunescloudd.tcchelper"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
-		(require-not (global-name "com.apple.MediaPlayer.MPRadioControllerServer"))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-any
 			(process-attribute is-autoboxed)
 			(require-all
```
