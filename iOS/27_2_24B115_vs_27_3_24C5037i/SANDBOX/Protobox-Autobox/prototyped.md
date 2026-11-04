## prototyped

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")
+		(iokit-registry-entry-class "RootDomainUserClient")
 	)
 )
 

 		(require-not (global-name "com.apple.TextInput.emoji"))
 		(require-not (global-name "com.apple.handwritingd.pksettings"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.hangtracerd"))

 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.TextInput.rdt"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.bird.token"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
 		(require-not (global-name "com.apple.inputanalyticsd"))

 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
+		(require-not (global-name "com.apple.dt.automationmode.reader"))
 		(require-not (global-name "com.apple.DragUI.druid.destination"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.pasteboard.pasted"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
+		(require-not (global-name "com.apple.dt.xctestd.target"))
 		(require-not (global-name "com.apple.springboard.backgroundappservices"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.campo"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.figmetriceventtimeline.xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))

 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.assistant.dictation"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
+		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.pearld"))
 		(require-not (global-name "com.apple.DragUI.druid.source"))
 		(require-not (global-name "com.apple.lsd.advertisingidentifiers"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))

 		(require-not (global-name "com.apple.audio.hapticd"))
 		(require-not (global-name "com.apple.uikit.viewservice.com.apple.datadetectors.DDActionsSe"))
 		(require-not (global-name "com.apple.gpumemd.source"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.videotarget.xpc"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))

 (allow socket-ioctl
 	(ioctl-command
 		SIOCGIFAFLAG_IN6
+		SIOCGIFAGENTDATA
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEFLAGS

 		SYS_necp_open
 		SYS_necp_client_action
 		SYS___channel_open
+		SYS___channel_get_info
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload

 			io_service_get_matching_services_bin
 			io_service_add_notification_bin_64
 			io_registry_entry_get_property_bin_buf
+			mach_port_get_refs
 			mach_port_request_notification
 			mach_port_extract_right
 			mach_port_set_attributes

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
 			(require-not (mac-syscall-number 7))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 2))
 		)
```
