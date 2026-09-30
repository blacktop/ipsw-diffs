## Sandbox Profiles

### Protobox/Autobox

#### New (1)

##### NFReportingService

```scheme
(version 1)
(disable-callouts)

(allow default)

(allow device-camera)

(deny mach-lookup
	(require-all
		(require-not (global-name "com.apple.diagnosticd"))
		(require-not (global-name "com.apple.logd.events"))
		(require-not (global-name "com.apple.runningboard"))
		(require-not (global-name "com.apple.system.notification_center"))
		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
		(require-not (global-name "com.apple.system.libinfo.muser"))
		(require-not (global-name "com.apple.nehelper"))
		(require-not (global-name "com.apple.dnssd.service"))
		(require-not (global-name "com.apple.usymptomsd"))
		(require-not (global-name "com.apple.trustd"))
		(require-not (global-name "com.apple.analyticsd"))
		(require-not (global-name "com.apple.cfprefsd.daemon"))
		(require-not (global-name "com.apple.logd"))
		(require-not (global-name "com.apple.containermanagerd.system"))
		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
		(require-not (global-name "com.apple.ak.anisette.xpc"))
		(require-not (global-name "com.apple.AppSSO.service-xpc"))
		(require-all
			(system-attribute developer-mode)
			(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
		)
	)
)

(deny system-kas-info)
```

#### Changed (74)

##### AUHostingServiceXPC_arrow

```diff

 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
+			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
```

##### AppleQEMUGuestAgent

```diff

 		(require-not (literal "/bin/sh"))
 		(require-not (literal "/bin/chmod"))
 		(require-not (literal "/bin/zsh"))
+		(require-not (literal "/usr/bin/killall"))
 		(require-any
 			(require-all
-				(require-not (literal "/usr/local/bin/fcq"))
 				(require-not (literal "/usr/local/bin/darwinup"))
+				(require-not (require-any
+					(literal "/usr/local/bin/fcq")
+					(literal "/usr/local/bin/pairtool")
+				))
+				(require-not (literal "/AppleInternal/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9"))
 			)
 			(require-not (system-attribute internal-build))
 		)
```

##### BTLEServer

```diff

 		(require-not (global-name "com.apple.AudioAccessoryServices"))
 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.bluetoothd"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.internal.studylogd"))

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.datamigrator"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
+		(require-not (global-name "com.apple.BTServer.map"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.lsd.advertisingidentifiers"))
```

##### Camera

```diff

 		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.accessibility.AXSpringBoardServer"))
 		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
-		(require-not (xpc-service-name "com.sogou.sogouinput.basekeyboard"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (require-any
+			(xpc-service-name "com.google.keyboard.KeyboardExtension")
+			(xpc-service-name "com.tencent.wetype.keyboard")
+		))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))

 		(require-not (global-name "com.apple.accessibility.heard"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (xpc-service-name "com.sogou.sogouinput.basekeyboard"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (global-name "com.apple.internal.objc_trace"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Topic.readOnly"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (local-name "com.apple.iphone.axserver"))
-		(require-not (xpc-service-name "com.google.keyboard.KeyboardExtension"))
+		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.bytedance.ios.doubaoime.keyboardExtension"))
 		(require-not (global-name "com.apple.CameraOverlayAngel.application-service"))
```

##### CommCenterRootHelper

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "AppleBasebandUserClient")
 	)
 )
 
 (deny iokit-open-service)
+(allow iokit-open-service
+	(require-any
+		(iokit-registry-entry-class "AppleBasebandINT1")
+		(iokit-registry-entry-class "AppleConvergedIPCLedaBBBTIInterface")
+	)
+)
 
 (deny iokit-set-properties)
 
 (deny ipc*)
 
+(deny ipc-posix-shm-read-data)
+(allow ipc-posix-shm-read-data
+	(ipc-posix-name "apple.cfprefs.user.daemonv1")
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)
 
 (deny mach-lookup
 	(require-all
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.sysdiagnose.service.xpc"))
 		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.logd.admin"))
 		(require-not (global-name "com.apple.tailspind"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-all
 			(system-attribute developer-mode)
 			(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))

 		SYS_mprotect
 		SYS_madvise
 		SYS_fcntl
+		SYS_fsync
 		SYS_socket
 		SYS_connect
 		SYS_sigsuspend

 		SYS_writev
 		SYS_fchown
 		SYS_fchmod
+		SYS_rename
 		SYS_sendto
 		SYS_mkdir
 		SYS_rmdir

 		SYS_lseek
 		SYS_ftruncate
 		SYS_sysctl
+		SYS_open_dprotected_np
 		SYS_getattrlist
 		SYS_fgetattrlist
 		SYS_fsetattrlist

 		SYS_pid_shutdown_sockets
 		SYS_memorystatus_control
 		SYS_guarded_close_np
+		SYS_change_fdguard_np
 		SYS_proc_rlimit_control
 		SYS_openat
 		SYS_openat_nocancel

 		SYS_guarded_writev_np
 		SYS_persona
 		SYS_getentropy
+		SYS_necp_open
+		SYS_necp_client_action
+		SYS___nexus_set_opt
+		SYS___channel_open
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload

 		io_iterator_next
 		io_registry_create_iterator
 		io_registry_entry_get_name
+		io_service_close
 		io_service_open_extended
+		io_connect_method
+		io_service_add_interest_notification_64
 		io_server_version
+		io_service_get_matching_service_bin
+		io_service_add_notification_bin_64
 		io_registry_entry_get_properties_bin_buf
+		io_registry_entry_get_property_bin_buf
+		mach_port_get_refs
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user

 		semaphore_create
 		semaphore_destroy
 		task_set_exc_guard_behavior
+		thread_policy
 		vm_remap_external
 		mach_make_memory_entry_64
 		vm_reallocate

 		mach_vm_range_create
 		mach_vm_reallocate
 		mach_memory_entry_ownership
+		mach_voucher_attr_command
 		task_restartable_ranges_register
 		task_restartable_ranges_synchronize)
 )

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_PREALLOCATE

 )
 
 (deny system-necp-client-action)
+(allow system-necp-client-action
+	(necp-client-action
+		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_COPY_AGENT
+		NECP_CLIENT_ACTION_COPY_INTERFACE
+		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_MAP_SYSCTLS
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_UPDATE_CACHE)
+)
```

##### ContactsBackgroundColorService

```diff

 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
+			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 5))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 67))
```

##### CorePrescriptionService

```diff

 		task_get_special_port_from_user
 		task_set_special_port
 		semaphore_create
+		task_set_exc_guard_behavior
 		vm_remap_external
 		vm_reallocate
 		mach_vm_map_external
```

##### CoreRoutineHelperService

```diff

 		(require-not (global-name "com.apple.Maps.mapspushd.geoservices"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
```

##### Family

```diff

 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.figmetriceventtimeline.xpc"))
 		(require-not (global-name "com.apple.intelligenceplatform.EntityResolution"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
+		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))

 		(require-not (require-any
 			(global-name "com.apple.ScreenTimeAgent.settings")
 			(global-name "com.apple.ak.puffin.xpc")
-			(global-name "com.apple.coreidvd.digital-presentment.xpc")
 			(global-name "com.apple.testmanagerd")
 			(global-name "com.apple.uikit.viewservice.com.apple.family")
 		))

 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
-		(require-not (local-name "com.apple.iphone.axserver"))
+		(require-not (global-name "com.apple.coreidvd.digital-presentment.xpc"))
 		(require-not (global-name "com.apple.dmd.policy"))
 		(require-not (global-name "com.apple.TextInput.preferences"))
 		(require-not (global-name "com.apple.passd.in-app-payment"))

 		(require-not (global-name "com.apple.rti-screencontinuity"))
 		(require-not (global-name "com.apple.hangtracermonitor"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.ScreenTimeAgent.ask-for-time"))
 		(require-not (global-name "com.apple.uikit.viewservice.com.apple.datadetectors.DDActionsSe"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.dt.xctestd.target"))

 		(require-not (global-name "com.apple.contactsd.launch-services-proxy"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
-		(require-not (global-name "com.apple.TextInput.rdt"))
+		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.assistant.analytics"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.awdd"))

 		(require-not (global-name "com.apple.generativeexperiences.textcomposition"))
 		(require-not (global-name "com.apple.assistant.cdm"))
 		(require-not (global-name "com.apple.synapse.backlink-service"))
-		(require-not (global-name "com.apple.geoanalyticsd"))
+		(require-not (local-name "com.apple.iphone.axserver"))
 		(require-not (global-name "com.apple.coreduetd.people"))
 		(require-not (require-any
 			(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")

 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.gputools.service"))
-		(require-not (global-name "com.apple.Safari.SafeBrowsing.Service"))
+		(require-not (global-name "com.apple.appstored.xpc"))
 		(require-not (global-name "com.apple.contactsd.support"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		(require-not (global-name "com.apple.DataDeliveryServices.AssetService"))
 		(require-not (global-name "com.apple.webinspector"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
-		(require-not (global-name "com.apple.appstored.xpc"))
+		(require-not (global-name "com.apple.TextInput.rdt"))
 		(require-not (global-name "com.apple.biometrickitd"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.erm.logging"))

 		(require-not (global-name "com.apple.mediaartworkd.xpc"))
 		(require-not (global-name "com.apple.uikit.viewservice.com.apple.mobilesms.compose"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
-		(require-not (global-name "com.apple.stickers.api"))
+		(require-not (global-name "com.apple.geoanalyticsd"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))

 		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.MobileTimer.alarmserver"))
-		(require-not (global-name "com.apple.ScreenTimeAgent.ask-for-time"))
+		(require-not (global-name "com.apple.stickers.api"))
 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))

 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.setup"))
 		(require-not (global-name "com.apple.ak.anisette.xpc"))
+		(require-not (global-name "com.apple.Safari.SafeBrowsing.Service"))
 		(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
 	)
 )
```

##### GNSSLocationService

```diff

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 90 96)
-		(require-not (mac-policy-name "AMFI"))
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
 	)
 )
 (deny system-mac-syscall
 	(require-any
-		(require-not (mac-policy-name "Sandbox"))
-		(require-not (mac-syscall-number 2))
+		(require-not (mac-policy-name "AMFI"))
+		(require-not (mac-syscall-number 90))
 	)
 )
 
```

##### ManifestStorageService

```diff

 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
+			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
```

##### MomentsUIService

```diff

 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
```

##### NFStorageServer

```diff

 		SYS_psynch_rw_upgrade
 		SYS_psynch_mutexwait
 		SYS_psynch_mutexdrop
+		SYS_psynch_cvbroad
+		SYS_psynch_cvsignal
+		SYS_psynch_cvwait
 		SYS_psynch_rw_rdlock
 		SYS_psynch_rw_wrlock
 		SYS_psynch_rw_unlock
 		SYS_psynch_rw_unlock2
+		SYS_psynch_cvclrprepost
 		SYS_issetugid
 		SYS___pthread_kill
 		SYS___pthread_sigmask
```

##### OverlayUI

```diff

 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
-		(require-not (xpc-service-name "com.tencent.wetype.keyboard"))
+		(require-not (require-any
+			(xpc-service-name "com.google.keyboard.KeyboardExtension")
+			(xpc-service-name "com.tencent.wetype.keyboard")
+		))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.UIKit.OverlayUI.services"))
 		(require-not (global-name "com.apple.dt.automationmode.reader"))

 		(require-not (global-name "com.apple.TextInput.rdt"))
 		(require-not (global-name "com.apple.stickers.api"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
-		(require-not (xpc-service-name "com.google.keyboard.KeyboardExtension"))
-		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
+		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
+		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
+		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DragUI.druid.source"))
 		(require-not (global-name "com.apple.DragUI.druid.destination"))
```

##### PersonalizedSensingService

```diff

 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
```

##### Photos

```diff

 
 (deny mach-lookup
 	(require-all
+		(require-not (global-name "com.apple.dmd.emergency-mode"))
+		(require-not (require-any
+			(global-name "com.apple.findmy.findmylocate.friendshipservice")
+			(global-name "com.apple.findmy.findmylocate.settings")
+		))
 		(require-not (global-name "com.apple.sharingd.pairedcontactmanager"))
 		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))

 		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
+			(xpc-service-name "com.bitstrips.imoji.BitmojiKeyboard")
+			(xpc-service-name "com.grammarly.keyboard.extension")
+			(xpc-service-name "com.jimmy54.SuperWubi.Keyboard")
+			(xpc-service-name "com.linecorp.LineEmoji.KeyboardExtension")
+			(xpc-service-name "com.navercorp.smartboard.extension")
+			(xpc-service-name "com.riffsy.RiffsyKeyboard.RiffsyGIFKeyboard")
+			(xpc-service-name "com.superduper.superwhisper-ios.superwhisper-keyboard")
+			(xpc-service-name "com.tackgyulee.dinggul.dinggulkeyboard")
+			(xpc-service-name "com.willowvoice.ios.keyboard")
+			(xpc-service-name "com.wispr.flowapp.flowboard")
 		))
 		(require-not (global-name "com.apple.contacts.donation.agent"))
 		(require-not (global-name "com.apple.imagent.embedded.auth"))

 		(require-not (global-name "com.apple.TapToRadarKit.service"))
 		(require-not (global-name "com.apple.proactive.FaceSuggestions.xpc"))
 		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
-		(require-not (xpc-service-name "com.google.keyboard.KeyboardExtension"))
-		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
-		(require-not (xpc-service-name "com.sogou.sogouinput.basekeyboard"))
 		(require-not (require-any
-			(xpc-service-name "com.grammarly.keyboard.extension")
-			(xpc-service-name "com.jimmy54.SuperWubi.Keyboard")
-			(xpc-service-name "com.linecorp.LineEmoji.KeyboardExtension")
-			(xpc-service-name "com.riffsy.RiffsyKeyboard.RiffsyGIFKeyboard")
-			(xpc-service-name "com.superduper.superwhisper-ios.superwhisper-keyboard")
-			(xpc-service-name "com.tackgyulee.dinggul.dinggulkeyboard")
-			(xpc-service-name "com.willowvoice.ios.keyboard")
-			(xpc-service-name "com.wispr.flowapp.flowboard")
+			(xpc-service-name "com.google.keyboard.KeyboardExtension")
+			(xpc-service-name "com.tencent.wetype.keyboard")
 		))
+		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
+		(require-not (xpc-service-name "com.bytedance.ios.doubaoime.keyboardExtension"))
 		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
-		(require-not (xpc-service-name "com.tencent.wetype.keyboard"))
+		(require-not (xpc-service-name "com.sogou.sogouinput.basekeyboard"))
 		(require-all
 			(system-attribute developer-mode)
 			(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
```

##### STExtractionService.privileged

```diff

 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
 		(require-not (global-name "com.apple.installcoordinationd"))
+		(require-not (xpc-service-name "com.apple.backgroundassets.managed.relay.service"))
 		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
 		(require-not (xpc-service-name "com.apple.backgroundassets.managed.helper.service"))
 		(require-all
```

##### ScreenSharingServer

```diff

 		io_service_add_interest_notification_64
 		io_server_version
 		io_service_get_matching_service_bin
+		io_service_get_matching_services_bin
 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
 		mach_port_request_notification
```

##### SoftwareUpdateUIService

```diff

 		(require-not (global-name "com.apple.TextInput.rdt"))
 		(require-not (local-name "com.apple.iphone.axserver"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
-		(require-not (xpc-service-name "com.google.keyboard.KeyboardExtension"))
 		(require-not (xpc-service-name "com.baidu.inputMethod.keyboard"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.sogou.sogouinput.basekeyboard"))
+		(require-not (require-any
+			(xpc-service-name "com.google.keyboard.KeyboardExtension")
+			(xpc-service-name "com.tencent.wetype.keyboard")
+		))
 		(require-not (xpc-service-name "com.apple.EventTimingProfileService"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
-		(require-not (xpc-service-name "com.tencent.wetype.keyboard"))
 		(require-any
 			(require-all
 				(system-attribute developer-mode)
```

##### SpringBoard

```diff

 		(require-not (global-name "com.apple.FamilyControlsAgent.private"))
 		(require-not (global-name "com.apple.AudioAccessoryServices"))
 		(require-not (global-name "com.apple.UIKit.statusbarserver"))
+		(require-not (global-name "com.apple.translation.text"))
 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.bird"))
 		(require-not (global-name "com.apple.VoiceOverTouch"))

 		io_service_add_notification_bin_64
 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
+		mach_port_destroy
 		mach_port_deallocate
 		mach_port_get_refs
 		mach_port_request_notification
```

##### UserEventAgent

```diff

 		SYS_sem_close
 		SYS_sysctlbyname
 		SYS_chmod_extended
+		SYS_fchmod_extended
 		SYS_gettid
 		SYS_shared_region_check_np
 		SYS_psynch_mutexwait
```

##### XPCAcmeService

```diff

 		host_info
 		host_get_io_master
 		host_get_clock_service
+		host_request_notification
 		host_get_special_port
 		clock_get_time
 		mach_exception_raise
```

##### abm-helper

```diff

 
 (deny ipc*)
 
+(deny ipc-posix-shm-read-data)
+(allow ipc-posix-shm-read-data
+	(ipc-posix-name "apple.cfprefs.user.daemonv1")
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
```

##### adprivacyd

```diff

 		(require-not (global-name "com.apple.ap.promotedcontent.supportinterface"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.amsaccountsd.multiuser"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
```

##### amsaccountsd

```diff

 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
 		(require-not (global-name "com.apple.coreidvd.proofing"))
+		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.xpc.amstreatmentstoreservice"))
 		(require-not (global-name "com.apple.coreidvd.docUpload.xpc"))
+		(require-not (global-name "com.apple.coreidvd.digital-presentment.xpc"))
 		(require-not (global-name "com.apple.passd.in-app-payment"))
 		(require-not (global-name "com.apple.algosd"))
 		(require-not (global-name "com.apple.asd.scoring"))
```

##### amsengagementd

```diff

 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.gamed"))
 		(require-not (global-name "com.apple.nesessionmanager"))
+		(require-not (global-name "com.apple.bird.token"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.SharedWebCredentials"))
 		(require-not (global-name "com.apple.diagd"))
```

##### analyticsagent

```diff

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
```

##### announced

```diff

 
 (deny system-necp-client-action)
 (allow system-necp-client-action
-	(necp-client-action NECP_CLIENT_ACTION_ADD)
+	(necp-client-action
+		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_COPY_AGENT
+		NECP_CLIENT_ACTION_COPY_INTERFACE
+		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT)
 )
```

##### appstored

```diff

 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.pearld"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
+		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (global-name "com.apple.managedappdistributiond.xpc"))
```

##### askpermissiond

```diff

 		F_GETFL
 		F_SETFL
 		F_SETLKW
+		F_RDADVISE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
```

##### atc

```diff

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.carousel.connectionstatusservice"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cmfsyncagent.embedded.auth"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.aggregated"))
```

##### attributionkitd

```diff

 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
+		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
 		MSC_mk_timer_cancel)
 )
```

##### avconferenced

```diff

 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.coremedia.mediaparserd.formatreader.xpc"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.videoconference.audiotranscriptionanalysis"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.coremedia.capturesession"))
 		(require-not (global-name "com.apple.backboardd.virtualframebuffer"))
```

##### backgroundassets.user

```diff

 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.nehelper"))
+		(require-not (global-name "com.apple.nesessionmanager"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.dnssd.service"))

 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.lsd.advertisingidentifiers"))
 		(require-not (global-name "com.apple.containermanagerd"))
```

##### bluetoothd

```diff

 		(require-not (global-name "com.apple.securityd"))
 		(require-not (require-any
 			(global-name "com.apple.BTServer.avrcp")
-			(global-name "com.apple.BTServer.map")
 			(global-name "com.apple.BTServer.pbap")
 			(global-name "com.apple.BlueTool")
 			(global-name "com.apple.bluetoothaudiod")

 		(require-not (global-name "com.apple.nfcd.hwmanager"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
-		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.iohideventsystem"))

 		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
-		(require-not (global-name "com.apple.timed.xpc"))
+		(require-not (global-name "com.apple.BTServer.map"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))

 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.terminusd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
 		(require-all
 			(system-attribute developer-mode)
 			(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
```

##### bookdatastored

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### bootpd

```diff

 		io_registry_entry_get_parent_iterator
 		io_registry_entry_get_path
 		io_registry_entry_get_name_in_plane
+		io_registry_entry_get_location_in_plane
 		io_service_open_extended
 		io_registry_entry_get_registry_entry_id
 		io_server_version
```

##### clipserviced

```diff

 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
+		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
 		MSC_mk_timer_cancel)
 )
```

##### com.apple.MessageSecurity.MSTimestampXPCService

```diff

 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-all
 			(system-attribute developer-mode)
 			(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
```

##### com.apple.PerformanceTrace.PerformanceTraceService

```diff

 		(require-not (global-name "com.apple.coresymbolicationd"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))

 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
 		SYS_stack_snapshot_with_config
+		SYS_persona
 		SYS_getentropy
 		SYS_ulock_wait
 		SYS_ulock_wake

 		mach_vm_range_create
 		mach_vm_reallocate
 		mach_memory_entry_ownership
+		mach_voucher_attr_command
 		task_restartable_ranges_register
 		task_restartable_ranges_synchronize)
 )
```

##### com.apple.dt.DTMLModelRunnerService

```diff

 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
+		(iokit-registry-entry-class "AppleM2ScalerParavirtDriver")
 		(iokit-registry-entry-class "AppleParavirtGPU")
 		(iokit-registry-entry-class "AppleVirtIONeuralEngineDevice")
 		(iokit-registry-entry-class "H11ANEIn")
```

##### coreduetd

```diff

 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.corerecents.recentsd"))
+		(require-not (global-name "com.apple.TapToRadarKit.service"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.biome.access.system"))
```

##### debugserver

```diff

 
 (deny socket-ioctl)
 (allow socket-ioctl
-	(ioctl-command CTLIOCGINFO)
+	(ioctl-command CTLIOCGINFO TIOCGETA)
 )
 
 (deny syscall-unix)
```

##### destinationd

```diff

 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
 		F_DUPFD_CLOEXEC
+		F_BARRIERFSYNC
 		F_OFD_GETLK
 		F_SETCONFINED
 		F_ADDFILESIGS_RETURN
```

##### diagnosticservicesd

```diff

 	(machtrap-number
 		MSC__kernelrpc_mach_vm_allocate_trap
 		MSC__kernelrpc_mach_vm_deallocate_trap
+		MSC_task_dyld_process_info_notify_get
 		MSC__kernelrpc_mach_vm_protect_trap
 		MSC__kernelrpc_mach_vm_map_trap
 		MSC__kernelrpc_mach_port_deallocate_trap
```

##### donotdisturbd

```diff

 		SYS_getattrlist
 		SYS_setattrlist
 		SYS_fgetattrlist
+		SYS_fsetattrlist
 		SYS_getxattr
 		SYS_fgetxattr
 		SYS_listxattr
+		SYS_flistxattr
 		SYS_fsctl
 		SYS_posix_spawn
 		SYS_shm_open
```

##### familycircled

```diff

 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.darwindirectory")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### fontservicesd

```diff

 		SYS_stat
 		SYS_fstat
 		SYS_lstat
+		SYS_pathconf
 		SYS_getrlimit
 		SYS_setrlimit
 		SYS_mmap
```

##### iapauthd

```diff

 		MSC__kernelrpc_mach_vm_map_trap
 		MSC__kernelrpc_mach_port_deallocate_trap
 		MSC__kernelrpc_mach_port_mod_refs_trap
+		MSC__kernelrpc_mach_port_insert_right_trap
 		MSC__kernelrpc_mach_port_construct_trap
 		MSC__kernelrpc_mach_port_destruct_trap
 		MSC_mach_reply_port
```

##### icloudsubscriptionoptimizerd

```diff

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))

 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.UsageTrackingAgent.private"))
+		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.ind.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))

 )
 
 (deny system-necp-client-action)
+(allow system-necp-client-action
+	(necp-client-action NECP_CLIENT_ACTION_ADD)
+)
```

##### inboxupdaterd

```diff

 
 (deny process-exec*
 	(require-all
-		(require-not (literal "/AppleInternal/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9"))
 		(require-not (literal "/usr/local/bin/smcif"))
 		(require-not (literal "/usr/local/bin/apple80211"))
+		(require-not (literal "/AppleInternal/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9"))
 	)
 )
 (deny process-exec*

 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command
+		CTLIOCGINFO
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEXPENSIVE
```

##### itunesstored

```diff

 		SYS_close_nocancel
 		SYS_sendmsg_nocancel
 		SYS_recvfrom_nocancel
+		SYS_msync_nocancel
 		SYS_fcntl_nocancel
 		SYS_select_nocancel
 		SYS_connect_nocancel
```

##### liveactivitiesd

```diff

 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.replicatorservices"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.ProgressReporting"))
```

##### locationd

```diff

 		(require-not (global-name "com.apple.icloud.searchpartyd.ownersession"))
 		(require-not (global-name "com.apple.nearbyd.xpc.nearbyinteraction"))
 		(require-not (global-name "com.apple.carkit.app.service"))
+		(require-not (global-name "com.apple.coreduetd.context"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationmanager"))
```

##### matd

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "AppleHPMUserClient")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "IOUSBDeviceInterfaceUserClient")
 		(iokit-registry-entry-class "RootDomainUserClient")

 (deny iokit-open-service)
 (allow iokit-open-service
 	(require-any
+		(iokit-registry-entry-class "AppleHPMARMI2C")
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "IOMobileFramebuffer")
 		(iokit-registry-entry-class "IOPMrootDomain")

 		io_iterator_next
 		io_registry_entry_from_path
 		io_registry_entry_get_name
+		io_registry_entry_get_child_iterator
+		io_registry_entry_get_parent_iterator
 		io_registry_get_root_entry
 		io_registry_entry_set_properties
 		io_service_open_extended

 		io_registry_entry_get_registry_entry_id
 		io_server_version
 		io_service_get_matching_service_bin
+		io_service_get_matching_services_bin
 		io_service_match_property_table_bin
 		io_service_add_notification_bin_64
+		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
 		mach_port_get_refs
 		mach_port_request_notification
```

##### mc_mobile_tunnel

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### migrationd

```diff

 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.ak.auth.xpc"))
 		(require-not (global-name "com.apple.kvsd"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))

 		(require-not (global-name "com.apple.remindd"))
 		(require-not (global-name "com.apple.itunesstored.xpc"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
+		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.amsprivateidentifiers"))
 		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
+		(require-not (global-name "com.apple.accessibility.mediaaccessibilityd"))
 		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))

 		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```

##### momentsd

```diff

 		(require-not (global-name "com.apple.cloudkit.partlycloudd"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.photoanalysisd"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
```

##### musicd

```diff

 )
 (deny system-mac-syscall
 	(require-any
-		(require-not (mac-policy-name "Sandbox"))
-		(require-not (mac-syscall-number 2))
+		(require-not (mac-policy-name "AMFI"))
+		(require-not (mac-syscall-number 90))
 	)
 )
 
```

##### nanomediaremotelinkagent

```diff

 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.neighborhood-activities"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
```

##### nanoregistryd

```diff

 			(global-name "com.apple.reboard")
 		))
 		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.wifi.manager"))
 		(require-not (global-name "com.apple.rtcreportingd"))
 		(require-not (global-name "com.apple.watchnotificationsui.alertservice"))
 		(require-not (global-name "com.apple.controlcenter.remoteservice"))
```

##### nanosystemsettingsd

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### passd

```diff

 		(require-not (global-name "com.apple.nearbyd.xpc.nearbyinteraction"))
 		(require-not (global-name "com.apple.carkit.app.service"))
 		(require-not (global-name "com.apple.mobile.installd"))
+		(require-not (global-name "com.apple.coreduetd.context"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.financed.service.coredatastore"))
 		(require-not (global-name "com.apple.logd.events"))
```

##### pkreporter

```diff

 	(deny system-mac-syscall
 		(require-all
 			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 2))
 		)
```

##### promotedcontentd

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 	)
 )
 

 	(require-any
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
+		(ipc-posix-name "apple.shm.notification_center")
 	)
 )
 

 			(global-name "com.apple.ap.promotedcontent.metrics")
 			(global-name "com.apple.ap.promotedcontent.pcinterface")
 			(global-name "com.apple.ap.promotedcontent.signing")
+			(global-name "com.apple.metrickit.xpc")
 		))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.trustd"))

 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))

 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.FileCoordination"))
```

##### proximitycontrold

```diff

 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
 		(require-not (global-name "com.apple.ProgressReporting"))
```

##### replicatord

```diff

 		(require-not (global-name "com.apple.userprofiles"))
 		(require-not (global-name "com.apple.StatusKit.local.actor"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
```

##### springboardservicesrelay

```diff

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.containermanagerd"))

 		SYS_guarded_close_np
 		SYS_proc_rlimit_control
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### threadradiod

```diff

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.corefollowup.agent"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.srp-mdns-proxy.proxy"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.audioanalyticsd"))
```

##### uarphidd

```diff

 		SYS_gettid
 		SYS_mkdir_extended
 		SYS_shared_region_check_np
+		SYS_psynch_rw_longrdlock
+		SYS_psynch_rw_yieldwrlock
+		SYS_psynch_rw_downgrade
+		SYS_psynch_rw_upgrade
+		SYS_psynch_mutexwait
+		SYS_psynch_mutexdrop
 		SYS_psynch_rw_rdlock
+		SYS_psynch_rw_wrlock
 		SYS_psynch_rw_unlock
+		SYS_psynch_rw_unlock2
 		SYS_issetugid
 		SYS___pthread_kill
 		SYS___pthread_sigmask
```

##### uarppersonalizationd

```diff

 			(global-name "com.apple.uarppersonalization")
 			(global-name "com.apple.uarppersonalization.btleserver")
 		))
-		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-all
```

##### visioncompaniond

```diff

 		SYS_change_fdguard_np
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```

##### watchdogd

```diff

 	)
 )
 
-(deny process-exec*
-	(require-all
-		(require-not (literal "/usr/bin/tailspin"))
-		(require-not (literal "/usr/sbin/kextstat"))
-		(require-any
-			(require-all
-				(require-not (literal "/usr/local/bin/ddt"))
-				(require-not (literal "/usr/local/bin/darwinup"))
-			)
-			(require-not (system-attribute internal-build))
-		)
+(deny process-exec*)
+(allow process-exec*
+	(require-any
+		(literal "/usr/bin/tailspin")
+		(literal "/usr/sbin/kextstat")
 	)
 )
 
```

##### wcd

```diff

 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.FileCoordination"))
```
