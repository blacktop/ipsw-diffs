## Sandbox Profiles

### Collection

#### Changed (2)

##### blastdoor-airlock

```diff

 		(extension "com.apple.app-sandbox.read")
 	)
 )
-(allow file-read*
-	(require-all
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
-		(extension "com.apple.app-sandbox.read")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.MobileSMS")
-		(extension "com.apple.app-sandbox.read")
-	)
-)
 (allow file-read*
 	(require-all
 		(subpath "${HOME}/Library/SMS")

 )
 (allow file-read*
 	(require-all
-		(require-any
-			(subpath "${HOME}/Library/Photos/Libraries/Syndication.photoslibrary/scopes/syndication/originals")
-			(subpath "${HOME}/Media/PhotoData/UBF/scopes/syndication/originals")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
-		)
+		(subpath "/private/var/tmp/com.apple.TelephonyUtilities/SharePlayActivityImages")
 		(extension "com.apple.app-sandbox.read")
 	)
 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var/tmp/com.apple.imtransferagent")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
+		(extension "com.apple.app-sandbox.read")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.MobileSMS")
 		(extension "com.apple.app-sandbox.read")
 	)
 )

 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var/tmp/com.apple.TelephonyUtilities/SharePlayActivityImages")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
+			(subpath "/private/var/tmp/com.apple.imtransferagent")
+		)
 		(extension "com.apple.app-sandbox.read")
 	)
 )

 		(extension "com.apple.app-sandbox.read")
 	)
 )
+(allow file-read*
+	(require-all
+		(require-any
+			(subpath "${HOME}/Library/Photos/Libraries/Syndication.photoslibrary/scopes/syndication/originals")
+			(subpath "${HOME}/Media/PhotoData/UBF/scopes/syndication/originals")
+		)
+		(extension "com.apple.app-sandbox.read")
+	)
+)
 (allow file-read*
 	(require-all
 		(system-attribute internal-build)

 				(require-any
 					(subpath "${HOME}/Library/Photos/Libraries/Syndication.photoslibrary/scopes/syndication/originals")
 					(subpath "${HOME}/Media/PhotoData/UBF/scopes/syndication/originals")
-					(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
 				)
 				(extension "com.apple.app-sandbox.read")
 			)

 				)
 				(extension "com.apple.app-sandbox.read")
 			)
+			(require-all
+				(require-any
+					(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
+					(subpath "/private/var/tmp/com.apple.imtransferagent")
+				)
+				(extension "com.apple.app-sandbox.read")
+			)
 			(require-all
 				(require-not (literal "/private/var"))
 				(require-not (require-any

 				(extension "com.apple.app-sandbox.read")
 			)
 			(require-all
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
+				(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
 				(extension "com.apple.app-sandbox.read")
 			)
 			(require-all

 				(subpath "/private/var/tmp/com.apple.TelephonyUtilities/SharePlayActivityImages")
 				(extension "com.apple.app-sandbox.read")
 			)
-			(require-all
-				(subpath "/private/var/tmp/com.apple.imtransferagent")
-				(extension "com.apple.app-sandbox.read")
-			)
 			(require-all
 				(subpath "/private/var/tmp/com.apple.messages")
 				(extension "com.apple.app-sandbox.read")
```

##### blastdoor-messages

```diff

 
 (allow file-read*
 	(require-all
-		(subpath "${HOME}/Library/SMS")
+		(require-any
+			(subpath "${HOME}/Library/Photos/Libraries/Syndication.photoslibrary/scopes/syndication/originals")
+			(subpath "${HOME}/Media/PhotoData/UBF/scopes/syndication/originals")
+		)
 		(extension "com.apple.app-sandbox.read")
 	)
 )

 )
 (allow file-read*
 	(require-all
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
-		(extension "com.apple.app-sandbox.read")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+		(subpath "${HOME}/Library/SMS")
 		(extension "com.apple.app-sandbox.read")
 	)
 )

 		(extension "com.apple.app-sandbox.read")
 	)
 )
-(allow file-read*
-	(require-all
-		(subpath "/private/var/tmp/com.apple.imtransferagent")
-		(extension "com.apple.app-sandbox.read")
-	)
-)
 (allow file-read*
 	(require-all
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.businessservicesd/temp")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.CallKit.CallDirectory/LiveCallerID")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.facetimemessagestored/IncomingVideoVoiceMail")
-			(subpath "/private/var/tmp/com.apple.CallKit.CallDirectory/LiveCallerID")
+			(literal "${PROCESS_TEMP_DIR}/com.apple.facetimemessagestored/IncomingVideoVoiceMail")
+			(subpath "${HOME}/Library/Caches/com.apple.businessservicesd/temp${PROCESS_TEMP_DIR}/com.apple.CallKit.CallDirectory/LiveCallerID")
 			(subpath "/private/var/tmp/com.apple.facetimemessagestored/IncomingVideoVoiceMail")
 		)
 		(extension "com.apple.app-sandbox.read")
 	)
 )
+(allow file-read*
+	(require-all
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
+		(extension "com.apple.app-sandbox.read")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+		(extension "com.apple.app-sandbox.read")
+	)
+)
 (allow file-read*
 	(require-all
 		(require-any
-			(subpath "${HOME}/Library/Photos/Libraries/Syndication.photoslibrary/scopes/syndication/originals")
-			(subpath "${HOME}/Media/PhotoData/UBF/scopes/syndication/originals")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
+			(subpath "/private/var/tmp/com.apple.imtransferagent")
 		)
 		(extension "com.apple.app-sandbox.read")
 	)
```

### Protobox/Autobox

#### Changed (20)

##### AccessibilityUIServer

```diff

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.usernotifications.remotenotificationservice"))
 		(require-not (global-name "com.apple.UIKit.statusbarserver"))
+		(require-not (global-name "com.apple.translation.text"))
 		(require-not (global-name "com.apple.VoiceOverTouch"))
 		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.contactsd"))

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.usernotifications.remotenotificationservice"))
 		(require-not (global-name "com.apple.UIKit.statusbarserver"))
+		(require-not (global-name "com.apple.translation.text"))
 		(require-not (global-name "com.apple.VoiceOverTouch"))
 		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.contactsd"))
```

##### BTLEServer

```diff

 		(require-not (global-name "com.apple.corespeech.corespeechd.activation.xpc"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.FSEvents"))

 		(require-not (global-name "com.apple.corespeech.corespeechd.activation.xpc"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.FSEvents"))
```

##### BluetoothUIService

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### CDPProximityPairingService

```diff

 		SYS_readv
 		SYS_writev
 		SYS_sendto
+		SYS_mkdir
 		SYS_pread
 		SYS_pwrite
 		SYS_statfs

 		SYS_lstat_extended
 		SYS_fstat_extended
 		SYS_gettid
+		SYS_mkdir_extended
 		SYS_shared_region_check_np
 		SYS_psynch_rw_longrdlock
 		SYS_psynch_rw_yieldwrlock

 		SYS_openat
 		SYS_fstatat
 		SYS_fstatat64
+		SYS_mkdirat
 		SYS_bsdthread_ctl
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
```

##### CMFSyncAgent

```diff

 		io_service_get_matching_service_bin
 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
+		mach_port_deallocate
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user

 		semaphore_destroy
 		task_set_exc_guard_behavior
 		thread_terminate
+		thread_suspend
 		vm_map_external
 		vm_remap_external
 		vm_reallocate
```

##### Family

```diff

 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
+		(require-not (global-name "com.apple.passd.payment"))
 		(require-not (global-name "com.apple.hangtelemetryd"))
 		(require-not (global-name "com.apple.passd.library"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
```

##### FindMyDeviceSharedConfigurationXPCService

```diff

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.trustd"))

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.trustd"))
```

##### NFReportingService

```diff

 	(with no-report)
 	(require-all
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.ak.anisette.xpc"))
```

##### Photos

```diff

 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (require-any
 			(xpc-service-name "com.bitstrips.imoji.BitmojiKeyboard")
+			(xpc-service-name "com.evoafuture.bettertalk.keyboard")
 			(xpc-service-name "com.grammarly.keyboard.extension")
+			(xpc-service-name "com.hamropatro.HamroKeyboard.HamroKey")
+			(xpc-service-name "com.jeethukthomas.ezhuthaani.manglish")
 			(xpc-service-name "com.jimmy54.SuperWubi.Keyboard")
 			(xpc-service-name "com.linecorp.LineEmoji.KeyboardExtension")
 			(xpc-service-name "com.navercorp.smartboard.extension")

 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (require-any
 			(xpc-service-name "com.bitstrips.imoji.BitmojiKeyboard")
+			(xpc-service-name "com.evoafuture.bettertalk.keyboard")
 			(xpc-service-name "com.grammarly.keyboard.extension")
+			(xpc-service-name "com.hamropatro.HamroKeyboard.HamroKey")
+			(xpc-service-name "com.jeethukthomas.ezhuthaani.manglish")
 			(xpc-service-name "com.jimmy54.SuperWubi.Keyboard")
 			(xpc-service-name "com.linecorp.LineEmoji.KeyboardExtension")
 			(xpc-service-name "com.navercorp.smartboard.extension")
```

##### akd

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 	)
 )
 

 
 (deny ipc*)
 
+(deny ipc-posix-shm-read-data)
+(allow ipc-posix-shm-read-data
+	(require-any
+		(ipc-posix-name "apple.cfprefs.system.daemonv1")
+		(ipc-posix-name "apple.cfprefs.user.daemonv1")
+	)
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)

 	(with no-report)
 	(require-all
 		(require-not (global-name "com.apple.security.kcsharing"))
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))

 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.coreidvd.proofing"))

 		(require-not (global-name "com.apple.SharedWebCredentials"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.eligibilityd"))
+		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.appstorecomponentsd.xpc"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.ak.auth.xpc"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (require-any

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.security.octagon"))

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.devicecheckd"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (xpc-service-name "com.apple.AppleVirtualPlatform.IdentityService"))

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.security.kcsharing"))
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))

 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.coreidvd.proofing"))

 		(require-not (global-name "com.apple.SharedWebCredentials"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.eligibilityd"))
+		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.appstorecomponentsd.xpc"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.ak.auth.xpc"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (require-any

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.security.octagon"))

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.devicecheckd"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (xpc-service-name "com.apple.AppleVirtualPlatform.IdentityService"))
```

##### assistivetouchd

```diff

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.accessibility.voices"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.translation.text"))
 		(require-not (global-name "com.apple.VoiceOverTouch"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.breadboardservices"))

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.accessibility.voices"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.translation.text"))
 		(require-not (global-name "com.apple.VoiceOverTouch"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.breadboardservices"))
```

##### dtfetchsymbolsd

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### fileproviderd

```diff

 (deny system-fsctl)
 (allow system-fsctl
 	(fsctl-command
+		APFSIOC_DIR_STATS_OP
 		APFSIOC_GET_DIR_STATS_EXT
 		APFSIOC_GET_PURGEABLE_FILE_FLAGS
 		APFSIOC_GET_SPEC_TELEM
```

##### fitcored

```diff

 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.SharingServices"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.debug.telemetry"))

 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.SharingServices"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.debug.telemetry"))
```

##### icloudwebd

```diff

 		MSC_pid_for_task
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
+		MSC_swtch_pri
 		MSC_syscall_thread_switch
 		MSC_host_create_mach_voucher_trap
 		MSC__kernelrpc_mach_port_type_trap
```

##### migrationd

```diff

 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.voicememod.xpc"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.posterboardservices.services"))
 		(require-not (global-name "com.apple.wifip2pd"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))

 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.voicememod.xpc"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.posterboardservices.services"))
 		(require-not (global-name "com.apple.wifip2pd"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
```

##### nanomediaremotelinkagent

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 
```

##### nfcd

```diff

 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
```

##### threadradiod

```diff

 		mach_exception_raise_state
 		mach_exception_raise_state_identity
 		io_iterator_next
+		io_registry_create_iterator
 		io_registry_entry_from_path
 		io_service_close
 		io_service_get_state
```

##### tipsd

```diff

 
 (deny ipc*)
 
+(deny ipc-posix-shm-read-data)
+(allow ipc-posix-shm-read-data
+	(require-any
+		(ipc-posix-name "apple.cfprefs.system.daemonv1")
+		(ipc-posix-name "apple.cfprefs.user.daemonv1")
+	)
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.passd.account"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.tipsd"))
 		(require-not (global-name "com.apple.tipsd.assistant"))

 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
 		(require-not (global-name "com.apple.contactsd.support"))

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.passd.account"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.tipsd"))
 		(require-not (global-name "com.apple.tipsd.assistant"))

 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
 		(require-not (global-name "com.apple.contactsd.support"))

 		SYS_mprotect
 		SYS_madvise
 		SYS_mincore
+		SYS_dup2
 		SYS_fcntl
 		SYS_select
 		SYS_fsync
```

### Platform Profile

#### Changed (1)

##### platform

```diff

 								(require-not (require-any
 									(subpath "/private/var/CipherMLAssets")
 									(subpath "/private/var/DarwinDataCenterSupportImage")
-									(subpath "/private/var/MLModels/LLM")
+									(subpath "/private/var/MLModels")
 									(subpath "/private/var/PCCApps")
 									(subpath "/private/var/PrivateCloudSupport")
 									(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 								(require-not (require-any
 									(subpath "/private/var/CipherMLAssets")
 									(subpath "/private/var/DarwinDataCenterSupportImage")
-									(subpath "/private/var/MLModels/LLM")
+									(subpath "/private/var/MLModels")
 									(subpath "/private/var/PCCApps")
 									(subpath "/private/var/PrivateCloudSupport")
 									(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 								(require-not (require-any
 									(subpath "/private/var/CipherMLAssets")
 									(subpath "/private/var/DarwinDataCenterSupportImage")
-									(subpath "/private/var/MLModels/LLM")
+									(subpath "/private/var/MLModels")
 									(subpath "/private/var/PCCApps")
 									(subpath "/private/var/PrivateCloudSupport")
 									(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 						(require-not (require-any
 							(subpath "/private/var/CipherMLAssets")
 							(subpath "/private/var/DarwinDataCenterSupportImage")
-							(subpath "/private/var/MLModels/LLM")
+							(subpath "/private/var/MLModels")
 							(subpath "/private/var/PCCApps")
 							(subpath "/private/var/PrivateCloudSupport")
 							(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 										(require-not (require-any
 											(subpath "/private/var/CipherMLAssets")
 											(subpath "/private/var/DarwinDataCenterSupportImage")
-											(subpath "/private/var/MLModels/LLM")
+											(subpath "/private/var/MLModels")
 											(subpath "/private/var/PCCApps")
 											(subpath "/private/var/PrivateCloudSupport")
 											(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 										(require-not (require-any
 											(subpath "/private/var/CipherMLAssets")
 											(subpath "/private/var/DarwinDataCenterSupportImage")
-											(subpath "/private/var/MLModels/LLM")
+											(subpath "/private/var/MLModels")
 											(subpath "/private/var/PCCApps")
 											(subpath "/private/var/PrivateCloudSupport")
 											(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 								(require-not (require-any
 									(subpath "/private/var/CipherMLAssets")
 									(subpath "/private/var/DarwinDataCenterSupportImage")
-									(subpath "/private/var/MLModels/LLM")
+									(subpath "/private/var/MLModels")
 									(subpath "/private/var/PCCApps")
 									(subpath "/private/var/PrivateCloudSupport")
 									(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 								(require-not (require-any
 									(subpath "/private/var/CipherMLAssets")
 									(subpath "/private/var/DarwinDataCenterSupportImage")
-									(subpath "/private/var/MLModels/LLM")
+									(subpath "/private/var/MLModels")
 									(subpath "/private/var/PCCApps")
 									(subpath "/private/var/PrivateCloudSupport")
 									(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 								(require-not (require-any
 									(subpath "/private/var/CipherMLAssets")
 									(subpath "/private/var/DarwinDataCenterSupportImage")
-									(subpath "/private/var/MLModels/LLM")
+									(subpath "/private/var/MLModels")
 									(subpath "/private/var/PCCApps")
 									(subpath "/private/var/PrivateCloudSupport")
 									(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 						(require-not (require-any
 							(subpath "/private/var/CipherMLAssets")
 							(subpath "/private/var/DarwinDataCenterSupportImage")
-							(subpath "/private/var/MLModels/LLM")
+							(subpath "/private/var/MLModels")
 							(subpath "/private/var/PCCApps")
 							(subpath "/private/var/PrivateCloudSupport")
 							(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 										(require-not (require-any
 											(subpath "/private/var/CipherMLAssets")
 											(subpath "/private/var/DarwinDataCenterSupportImage")
-											(subpath "/private/var/MLModels/LLM")
+											(subpath "/private/var/MLModels")
 											(subpath "/private/var/PCCApps")
 											(subpath "/private/var/PrivateCloudSupport")
 											(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 										(require-not (require-any
 											(subpath "/private/var/CipherMLAssets")
 											(subpath "/private/var/DarwinDataCenterSupportImage")
-											(subpath "/private/var/MLModels/LLM")
+											(subpath "/private/var/MLModels")
 											(subpath "/private/var/PCCApps")
 											(subpath "/private/var/PrivateCloudSupport")
 											(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 		(require-not (require-any
 			(subpath "/private/var/CipherMLAssets")
 			(subpath "/private/var/DarwinDataCenterSupportImage")
-			(subpath "/private/var/MLModels/LLM")
+			(subpath "/private/var/MLModels")
 			(subpath "/private/var/PCCApps")
 			(subpath "/private/var/PrivateCloudSupportInternalAdditions")
 		))

 					(require-not (require-any
 						(subpath "/private/var/CipherMLAssets")
 						(subpath "/private/var/DarwinDataCenterSupportImage")
-						(subpath "/private/var/MLModels/LLM")
+						(subpath "/private/var/MLModels")
 						(subpath "/private/var/PCCApps")
 						(subpath "/private/var/PrivateCloudSupport")
 						(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 					(require-not (require-any
 						(subpath "/private/var/CipherMLAssets")
 						(subpath "/private/var/DarwinDataCenterSupportImage")
-						(subpath "/private/var/MLModels/LLM")
+						(subpath "/private/var/MLModels")
 						(subpath "/private/var/PCCApps")
 						(subpath "/private/var/PrivateCloudSupport")
 						(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 		(require-not (require-any
 			(subpath "/private/var/CipherMLAssets")
 			(subpath "/private/var/DarwinDataCenterSupportImage")
-			(subpath "/private/var/MLModels/LLM")
+			(subpath "/private/var/MLModels")
 			(subpath "/private/var/PCCApps")
 			(subpath "/private/var/PrivateCloudSupport")
 			(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 		(require-not (require-any
 			(subpath "/private/var/CipherMLAssets")
 			(subpath "/private/var/DarwinDataCenterSupportImage")
-			(subpath "/private/var/MLModels/LLM")
+			(subpath "/private/var/MLModels")
 			(subpath "/private/var/PCCApps")
 			(subpath "/private/var/PrivateCloudSupport")
 			(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 					(require-not (require-any
 						(subpath "/private/var/CipherMLAssets")
 						(subpath "/private/var/DarwinDataCenterSupportImage")
-						(subpath "/private/var/MLModels/LLM")
+						(subpath "/private/var/MLModels")
 						(subpath "/private/var/PCCApps")
 						(subpath "/private/var/PrivateCloudSupport")
 						(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 					(require-not (require-any
 						(subpath "/private/var/CipherMLAssets")
 						(subpath "/private/var/DarwinDataCenterSupportImage")
-						(subpath "/private/var/MLModels/LLM")
+						(subpath "/private/var/MLModels")
 						(subpath "/private/var/PCCApps")
 						(subpath "/private/var/PrivateCloudSupport")
 						(subpath "/private/var/PrivateCloudSupportInternalAdditions")

 	(_g2 "")
 	(require-any
 		(subpath "/private/var/CipherMLAssets")
-		(subpath "/private/var/MLModels/LLM")
+		(subpath "/private/var/MLModels")
 	)
 ))
 (define (_g4 _)

 	(_g2 "")
 	(require-any
 		(subpath "/private/var/CipherMLAssets")
-		(subpath "/private/var/MLModels/LLM")
+		(subpath "/private/var/MLModels")
 	)
 ))
 (define (_g4 _)
```
