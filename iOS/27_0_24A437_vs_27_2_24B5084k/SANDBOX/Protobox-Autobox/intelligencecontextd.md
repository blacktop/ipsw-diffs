## intelligencecontextd

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationUserClient")
 		(iokit-registry-entry-class "H11ANEInDirectPathClient")
+		(iokit-registry-entry-class "H1xANELoadBalancerDirectPathClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")

 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.coremedia.capturesession"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.assistant.settings"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))

 		(require-not (global-name "com.apple.intelligenceflow.context"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
+		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.springboard.services"))
+		(require-not (global-name "com.apple.backboard.display.services"))
 		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
+		(require-not (global-name "com.apple.lsd.modifydb"))
 		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))

 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (global-name "com.apple.generativeexperiences.agentMediaStore"))
 		(require-not (global-name "com.apple.breadboardservices"))
+		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.intelligenceflow.toolbox"))
 		(require-not (global-name "com.apple.mediaanalysisd.service.public"))

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_openat_nocancel
 		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat

 		vm_remap_external
 		mach_make_memory_entry_64
 		vm_reallocate
+		mach_vm_read
 		mach_vm_copy
 		mach_vm_map_external
 		mach_vm_remap_external
```
