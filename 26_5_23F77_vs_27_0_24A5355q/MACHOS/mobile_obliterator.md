## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

-371.120.3.0.0
-  __TEXT.__text: 0x1a4dc
+395.0.0.0.0
+  __TEXT.__text: 0x1ab40
   __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__objc_stubs: 0x620
-  __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0xa479
+  __TEXT.__objc_stubs: 0x880
+  __TEXT.__objc_methlist: 0x1fc
+  __TEXT.__cstring: 0xa88c
   __TEXT.__const: 0x6e8
-  __TEXT.__objc_methname: 0x4cd
-  __TEXT.__objc_classname: 0xc
-  __TEXT.__objc_methtype: 0x3a
-  __TEXT.__gcc_except_tab: 0x110
-  __TEXT.__unwind_info: 0x3f0
-  __DATA_CONST.__auth_got: 0xa80
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__auth_ptr: 0x8
+  __TEXT.__gcc_except_tab: 0x144
+  __TEXT.__objc_methname: 0x7c6
+  __TEXT.__objc_classname: 0x5b
+  __TEXT.__objc_methtype: 0x159
+  __TEXT.__unwind_info: 0x3f8
   __DATA_CONST.__const: 0x678
-  __DATA_CONST.__cfstring: 0x18a0
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__cfstring: 0x20a0
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0x198
-  __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0x130
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__auth_got: 0xa88
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x400
+  __DATA.__objc_selrefs: 0x2e0
+  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x250
   __DATA.__common: 0x200
-  __DATA.__bss: 0x2a00
+  __DATA.__bss: 0x2a30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EAB20091-6125-3298-B60E-C204AF1C0443
-  Functions: 277
-  Symbols:   385
-  CStrings:  1428
+  UUID: E3A46BA1-124A-37BF-9EFA-A207E53A5A0F
+  Functions: 271
+  Symbols:   394
+  CStrings:  1636
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_NSXPCListener
+ __Block_object_dispose
+ ___assert_rtn
+ ___objc_personality_v0
+ _objc_alloc
+ _objc_release
+ _objc_release_x21
+ _objc_release_x24
+ _objc_release_x26
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
- _MOXPCTransportOpen
- _MOXPCTransportResume
- _MOXPCTransportSendMessageOnConnection
- _MOXPCTransportSetMessageHandler
- _SecTaskCopyValueForEntitlement
- _SecTaskCreateWithAuditToken
- _objc_release_x19
- _xpc_connection_get_audit_token
- _xpc_connection_send_barrier
CStrings:
+ " (sim-fail DATA_VOLUME_UNMOUNT_POST)"
+ " (sim-fail DATA_VOLUME_UNMOUNT_PRE)"
+ " (sim-fail USER_VOLUME_UNMOUNT_POST)"
+ " (sim-fail USER_VOLUME_UNMOUNT_PRE)"
+ "#16@0:8"
+ "%@:%@"
+ "%s: %s: %sdeleting non-fstab volumes"
+ "%s: %s: Completed %d second delay after reply"
+ "%s: %s: Could not unmount the Data volume%s"
+ "%s: %s: Could not unmount the User volume%s"
+ "%s: %s: Failed to obliterate the Data volume and to wipe volume keys"
+ "%s: %s: Failed to unmount the Data volume post obliteration%s"
+ "%s: %s: Failed to unmount the User volume post obliteration%s"
+ "%s: %s: Not a shared iPad, skipping reboot stage"
+ "%s: %s: Server received new XPC connection request"
+ "%s: %s: Simulating obliterate failure at start"
+ "%s: %s: Skipping RAMROD setup"
+ "%s: %s: XPC connection interrupted"
+ "%s: %s: XPC connection invalidated"
+ "%s: %s: XPC listener for service '%s' initialized and resumed"
+ "%s: %s: unmount Data volume %s%s"
+ "%s: %s: unmount Data volume succeeded"
+ "-[MOXPCListener listener:shouldAcceptNewConnection:]"
+ "-[MOXPCListener listener:shouldAcceptNewConnection:]_block_invoke"
+ "-[MOXPCListener listener:shouldAcceptNewConnection:]_block_invoke_2"
+ "-[MOXPCListener startListening]"
+ "-[MOXPCServerEmbedded obliterateWithOptions:reply:]"
+ "40A0DDD2-77F8-4392-B4A3-1E7304206516"
+ "@\"NSString\"16@0:8"
+ "@\"NSXPCListener\""
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
+ "Could not statfs %s: %s"
+ "Exclusion paths validation failed"
+ "IODTNVRAMVariables"
+ "IONameMatch"
+ "IOProviderClass"
+ "IS"
+ "MOXPCListener"
+ "MOXPCProtocol"
+ "MOXPCServerEmbedded"
+ "Missing entitlement: %@"
+ "Missing required entitlement: %@"
+ "NOT"
+ "NSObject"
+ "NSXPCListenerDelegate"
+ "Obliteration already in progress"
+ "ObliterationSanitizeStorage"
+ "Ooops... shouldn't be here - reboot() must have failed - errno %d!"
+ "Q16@0:8"
+ "SystemAudioVolume"
+ "SystemAudioVolumeExtension"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,R"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_init"
+ "_listener"
+ "alt-boot-volume"
+ "autorelease"
+ "boolValue"
+ "boot-args"
+ "boot-breadcrumbs"
+ "boot-command"
+ "boot-volume"
+ "bootdelay"
+ "brickIfNeeded"
+ "chassis-disable-throttle"
+ "chassis-platform-id"
+ "chassis-slot-id"
+ "checkMultiUserMode"
+ "class"
+ "cleanPrebootVolume"
+ "cleanUpdateVolume"
+ "cleanXartVolume"
+ "conformsToProtocol:"
+ "containsObject:"
+ "copy"
+ "currentConnection"
+ "debug-uarts"
+ "debugDescription"
+ "deleteNonFstabVolumes"
+ "description"
+ "dictionaryWithObjects:forKeys:count:"
+ "dramecc"
+ "errorWithDomain:code:userInfo:"
+ "handle_data_volume_obliteration"
+ "handle_message_block_invoke"
+ "hash"
+ "iboot-failure-reason"
+ "iboot1-precommitted"
+ "initWithMachServiceName:"
+ "interfaceWithProtocol:"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "listener:shouldAcceptNewConnection:"
+ "lookupDataVolumeDevice"
+ "mobile_obliterator.m"
+ "mountHWVolume"
+ "mountUserVolume"
+ "obliterateDevice"
+ "obliterateWithOptions:reply:"
+ "options-system"
+ "ota-anomalies"
+ "ota-brain-version"
+ "ota-breadcrumbs"
+ "ota-child-failures"
+ "ota-context"
+ "ota-controllerVersion"
+ "ota-failure-reason"
+ "ota-forced-reset-uptime"
+ "ota-initial-failure-reason"
+ "ota-initial-forced-reset-uptime"
+ "ota-initial-result"
+ "ota-install-tonight"
+ "ota-outcome"
+ "ota-reboot-retry-enabled"
+ "ota-reboot-retry-zone"
+ "ota-result"
+ "ota-retry-enabled"
+ "ota-retry-failure-reason"
+ "ota-retry-result"
+ "ota-snapshot-update"
+ "ota-tolerated-disable"
+ "ota-updateType"
+ "ota-uuid"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "populateUserVolume"
+ "prepareObliterate"
+ "prepareSafeObliterate"
+ "ramrod-kickstart-aces"
+ "ramrod_NVRAM_has_system_namespace: system namespace %s present\n"
+ "rebuildDataVolume"
+ "recovery-boot-mode"
+ "recovery-breadcrumbs"
+ "reformatDataVolume"
+ "reformatUserVolume"
+ "release"
+ "remoteProcessHasBooleanEntitlement:"
+ "removeExcept /(ANE|AOP|AOP2|AVE|GFX|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware))\\.img4/"
+ "removeExcept /(ANE|AOP|AOP2|AVE|GFX|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware|ExclaveOSVolume|ExclaveOSIntegrityCatalog|ExclaveOSTrustCache|cL4))\\.img4/ /Ap,ExclaveOS.dmg/"
+ "removeExcept /dramecc.db/ /memory_errors.db/"
+ "respondsToSelector:"
+ "restore-retry-enabled"
+ "restoreDataVolumeContent"
+ "restored-host-timeout"
+ "resume"
+ "retain"
+ "retainCount"
+ "root-live-fs"
+ "self"
+ "setDelegate:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setupAndMountDataVolume"
+ "setupDataVolumeContent"
+ "setupMultiUserVolumes"
+ "sharedListener"
+ "startListening"
+ "superclass"
+ "target-uuid"
+ "unmapUserVolume"
+ "unmountVolumesPostObliteration"
+ "update-volume"
+ "upgrade-boot-volume"
+ "upgrade-fallback-boot-command"
+ "upgrade-manifest-hash"
+ "upgrade-retry"
+ "v16@0:8"
+ "v16@?0@\"NSError\"8"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@16@?24"
+ "valueForEntitlement:"
+ "zone"
- " (sim-fail DATA_VOLUME_UNMOUNT)"
- " (sim-fail USER_VOLUME_UNMOUNT)"
- "%s: %s: Could not create the security task from the audit token"
- "%s: %s: Could not delete existing non fstab APFS volumes"
- "%s: %s: Could not extract the value for the entitlement"
- "%s: %s: Could not obliterate the Data volume"
- "%s: %s: Could not setup the content for Data volume"
- "%s: %s: Could not statfs %s: %s"
- "%s: %s: Could not unmount the Data volume"
- "%s: %s: Could not unmount the User volume"
- "%s: %s: Could not verify the obliteration client"
- "%s: %s: Failed to not send response to the client"
- "%s: %s: Failed to obliterate the Data volume and to wipe volume keys, failing safe obliteration"
- "%s: %s: Failed to re-set the user volume in RRTS mode"
- "%s: %s: Failed to set up the data and user volumes in multiuser mode"
- "%s: %s: Failed to unmount the Data volume post obliteration"
- "%s: %s: Failed to unmount the User volume post obliteration"
- "%s: %s: Ooops... shouldn't be here - reboot() must have failed - errno %d!"
- "%s: %s: SAFE WIPE Type Obliteration is in progress..."
- "%s: %s: SafeWipe: Could not unmount the Data volume %s (error: %d)%s"
- "%s: %s: SafeWipe: Could not unmount the User volume %s (error: %d)%s"
- "%s: %s: Simulating safeObliterate failure at start"
- "%s: %s: Skipping the Disable of the watchdog timer"
- "%s: %s: Terminating Daemons Complete, safe wipe started ..."
- "%s: %s: Terminating Daemons for safe wipe ..."
- "%s: %s: The client does not have the obliteration entitlement"
- "%s: %s: The entitlement value is not a boolean"
- "%s: %s: There was an error retrieving the entitlement value"
- "%s: %s: Unable to start server"
- "%s: %s: XXXXXXXXXXXXX SKIPPING RAMROD SETUP XXXXXXXXXXXXX "
- "%s: %s: kip obliterating the Data volume, %sdeleting non-fstab volumes"
- "%s: %s: not need to obliterate the Data volume, %sdeleting non-fstab volumes"
- "%s: %s: skip shared-iPad reboot stage"
- "%s: %s: unmount Data volume %s"
- "ObliterationTypeSafeWipe"
- "SafeWipe Done"
- "com.apple.xpc.remote.mobile_obliteration"
- "obliterate"
- "removeExcept /(ANE|GFX|AVE|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware))\\.img4/"
- "removeExcept /(ANE|GFX|AVE|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware|ExclaveOSVolume|ExclaveOSIntegrityCatalog|ExclaveOSTrustCache|cL4))\\.img4/ /Ap,ExclaveOS.dmg/"
- "safeWipe"
- "send_reply_response_cf"
- "v24@?0@\"NSObject<OS_xpc_object>\"8^{__CFDictionary=}16"
- "verify_obliteration_client"

```
