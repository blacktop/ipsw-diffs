## icloudwebd

> Group: ⬆️ Updated

```diff

 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.identityservicesd.idquery.embedded.auth"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.intelligenceplatform.EntityResolution"))

 		(require-not (global-name "com.apple.intelligenceplatform.View"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
+		(require-not (global-name "com.apple.mediaanalysisd.embeddingstore"))
+		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Contact"))
 		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
 		(require-not (global-name "com.apple.gpumemd.source"))

 		io_connect_set_notification_port_64
 		io_registry_entry_get_registry_entry_id
 		io_server_version
+		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
 		io_registry_entry_get_property_bin_buf
 		mach_port_request_notification
```
