## Family

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.coremedia.mediaparserd.formatreader.xpc"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.healthd.server"))
-		(require-not (global-name "com.apple.rti-screencontinuity"))
 		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.assistant.settings"))
 		(require-not (global-name "com.apple.UIKit.KeyboardManagement.hosted"))

 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.geoanalyticsd"))
 		(require-not (global-name "com.apple.translation.text"))
+		(require-not (require-any
+			(global-name "com.apple.remote-text-editing-legacy")
+			(global-name "com.apple.rti-screencontinuity")
+			(global-name "com.apple.sharing.remote-text-editing")
+		))
+		(require-not (require-any
+			(global-name "com.apple.appprotectiond.viewsubjectinfo")
+			(global-name "com.apple.appprotectiond.viewsubjectmonitor")
+		))
 		(require-not (global-name "com.apple.bird.token"))
 		(require-not (global-name "com.apple.ak.auth.xpc"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))

 			(global-name "com.apple.coremedia.sts")
 			(global-name "com.apple.uikit.viewservice.com.apple.family")
 		))
-		(require-not (require-any
-			(global-name "com.apple.remote-text-editing-legacy")
-			(global-name "com.apple.sharing.remote-text-editing")
-		))
 		(require-not (global-name "com.apple.ak.anisette.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc"))
 		(require-not (global-name "com.apple.networkscored"))

 		(require-not (global-name "com.apple.internal.studylogd"))
 		(require-not (global-name "com.apple.intelligenceplatform.Feedback"))
 		(require-not (global-name "com.apple.contactsd.launch-services-proxy"))
-		(require-not (global-name "com.apple.appprotectiond.viewsubjectmonitor"))
 		(require-not (global-name "com.apple.accessibility.heard"))
 		(require-not (global-name "com.apple.synapse.backlink-service"))
 		(require-not (global-name "com.apple.containermanagerd"))

 			(global-name "com.apple.iMessageAppsViewService.warmup-connection")
 			(global-name "com.apple.uikit.viewservice.com.apple.iMessageAppsViewService")
 		))
-		(require-not (global-name "com.apple.appprotectiond.viewsubjectinfo"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.itunescloudd.xpc"))

 		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.passd.library"))
 		(require-not (global-name "com.apple.FSEvents"))
+		(require-not (global-name "com.apple.servicesanalytics.xpc"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))

 				io_registry_entry_get_name
 				io_registry_entry_get_property_bytes
 				io_registry_entry_get_child_iterator
+				io_registry_entry_get_parent_iterator
 				io_service_close
 				io_connect_get_service
 				io_registry_get_root_entry
```
