## fitnessintelligenced

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.fairplayd.versioned"))
-		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
+		(require-not (global-name "com.apple.itunescloud.music-subscription-status-service"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.fitnessintelligenced"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.nanoprefsync"))
-		(require-not (global-name "com.apple.mediaremoted.xpc"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
+		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
+		(require-not (global-name "com.apple.geod"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.audioanalyticsd"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
+		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
-		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
-		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.itunescloud.music-subscription-status-service"))
+		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.sirittsd"))
-		(require-not (global-name "com.apple.xpc.amsengagementd"))
-		(require-not (global-name "com.apple.geod"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (global-name "com.apple.audioanalyticsd"))
-		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
-		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.FitnessIntelligenceGLPService")
 			(xpc-service-name "com.apple.FitnessSnapshotService")
```
