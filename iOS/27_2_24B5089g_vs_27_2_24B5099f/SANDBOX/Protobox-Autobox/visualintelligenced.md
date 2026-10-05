## visualintelligenced

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
+		(require-not (global-name "com.apple.polaris.systemgraph"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.naturallanguaged"))

 		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.TextInput.rdt"))
 		(require-not (global-name "com.apple.trustd"))

 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.ClipServices.clipserviced"))
 		(require-not (global-name "com.apple.businessservicesd"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.kvsd"))
+		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.linkd.transcript"))
 		(require-not (global-name "com.apple.feedbackd.centralized-feedback"))
 		(require-not (global-name "com.apple.geod"))

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.DeviceConfigurationAgent.consumer.async"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.siri.activation.service"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
```
