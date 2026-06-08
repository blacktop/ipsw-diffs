## devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

```diff

-107.100.11.0.0
-  __TEXT.__text: 0x1fc94
-  __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_stubs: 0x21c0
-  __TEXT.__objc_methlist: 0xbbc
-  __TEXT.__cstring: 0x6ab5
-  __TEXT.__const: 0x58
-  __TEXT.__objc_methname: 0x23f1
-  __TEXT.__oslogstring: 0x3215
-  __TEXT.__objc_classname: 0x125
-  __TEXT.__objc_methtype: 0x541
-  __TEXT.__gcc_except_tab: 0x6fc
-  __TEXT.__unwind_info: 0x688
-  __DATA_CONST.__auth_got: 0x728
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xc00
-  __DATA_CONST.__cfstring: 0x2360
+142.0.0.0.0
+  __TEXT.__text: 0x22f50
+  __TEXT.__auth_stubs: 0xfb0
+  __TEXT.__objc_stubs: 0x25a0
+  __TEXT.__objc_methlist: 0xcec
+  __TEXT.__cstring: 0x7b10
+  __TEXT.__const: 0x478
+  __TEXT.__objc_methname: 0x2751
+  __TEXT.__oslogstring: 0x3615
+  __TEXT.__objc_classname: 0x16a
+  __TEXT.__objc_methtype: 0x5f4
+  __TEXT.__gcc_except_tab: 0x544
+  __TEXT.__unwind_info: 0x6e0
+  __DATA_CONST.__const: 0xcf0
+  __DATA_CONST.__cfstring: 0x2c60
   __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x13c8
-  __DATA.__objc_selrefs: 0xa68
+  __DATA_CONST.__objc_arraydata: 0x28
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__auth_got: 0x7e8
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA.__objc_const: 0x1420
+  __DATA.__objc_selrefs: 0xb88
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x220
-  __DATA.__bss: 0x1e0
+  __DATA.__data: 0x2e0
+  __DATA.__bss: 0x228
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/Darwinup.framework/Darwinup
   - /System/Library/PrivateFrameworks/DeviceRecoveryBrainSupport.framework/DeviceRecoveryBrainSupport
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaKit.framework/MediaKit
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
+  - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate

   - /System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 10567237-BC23-3C4E-9C91-89E2DB225658
-  Functions: 710
-  Symbols:   297
-  CStrings:  1748
+  UUID: 6BB46DC5-3684-3292-8D7C-DE882C0D605E
+  Functions: 809
+  Symbols:   329
+  CStrings:  1996
 
Symbols:
+ _CFStringCreateWithFormatAndArguments
+ _CFStringGetLength
+ _CFStringGetMaximumSizeForEncoding
+ _IOConnectCallStructMethod
+ _IOServiceClose
+ _IOServiceMatching
+ _IOServiceOpen
+ _MKBVerifyACMPasswordWithContext
+ _Mobile_Obliterate
+ _NSKeyedArchiveRootObjectKey
+ _OBJC_CLASS_$_DURoot
+ _OBJC_CLASS_$_DUSession
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _WiFiDeviceClientCopyCurrentNetwork
+ _WiFiManagerClientCopyInterfaces
+ _WiFiManagerClientCreate
+ _WiFiNetworkCopyPassword
+ _WiFiNetworkGetSSID
+ ___stderrp
+ _fprintf
+ _getenv
+ _kObliterationTypeKey
+ _kObliterationTypeMarkStart
+ _mach_task_self_
+ _malloc_type_posix_memalign
+ _memcpy
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x3
+ _strncpy
- _objc_retain_x27
CStrings:
+ " | "
+ "%02x"
+ "%@/%s"
+ "%f"
+ "%lld"
+ "%s :Failed to create WiFiManagerClient\n"
+ "%s: %s"
+ "%{public}s: ADD_EVENT: Adding CoreAnalytics event to the history queue: %{public}@"
+ "%{public}s: Calling Mobile_Obliterate with kObliterationTypeMarkStart"
+ "%{public}s: Could not load NVRAM info (%d)"
+ "%{public}s: EACS initiated successfully - device will erase and reboot"
+ "%{public}s: EACS triggered - erasing all content and settings"
+ "%{public}s: Event payload data \"%{public}@\" is unsupported type \"%{public}@\". Supported Types: NSString, NSNumber, NSData, NSError"
+ "%{public}s: Failed to convert nvram value %{public}@ to string"
+ "%{public}s: Failed to link %{public}@ to %{public}@, error:%{public}@"
+ "%{public}s: Failed to move %{public}@ to %{public}@, error:%{public}@"
+ "%{public}s: Failed to open darwinup session: %{public}@"
+ "%{public}s: Failed to remove %{public}@, error:%{public}@"
+ "%{public}s: Mobile_Obliterate failed with result: %d"
+ "%{public}s: Mobile_Obliterate succeeded, clearing boot-command NVRAM variable"
+ "%{public}s: Moving %{public}@ to %{public}@"
+ "%{public}s: Reading NVRAM var: %{public}@"
+ "%{public}s: Validating passcode"
+ "%{public}s: Validating passcode with MKBVerifyACMPasswordWithContext"
+ "%{public}s: [TEST MODE] enabled - simulating EACS"
+ "%{public}s: events dict = %{public}@"
+ "%{public}s: no roots, with error: %{public}@"
+ "%{public}s: passcode validation failed - MKBVerifyACMPasswordWithContext returned unexpected error: %d"
+ "%{public}s: passcode validation failed - backoff = %g seconds"
+ "%{public}s: passcode validation failed - invalid passcode. LockStateInfo: %@"
+ "%{public}s: passcode validation failed - keybag not ready. LockStateInfo: %@"
+ "%{public}s: passcode validation succeeded"
+ "%{public}s: processCAEventsFile finished with %{public}@"
+ "%{public}s: reboot:%{BOOL}d bootType:%ld, autoRecovery:%{BOOL}d, allowErase:%{BOOL}d"
+ "%{public}s: removing %{public}@"
+ "%{public}s: user authentication failed - passcode is in backoff = %g seconds"
+ "((recoveryResultVal == DROverrideRecoveryResultNoOverride) || (recoveryResultVal == DROverrideRecoveryResultForceFailure) || (recoveryResultVal == DROverrideRecoveryResultRequireOSBootPhase) || (recoveryResultVal == DROverrideRecoveryResultRequirePostUserUnlockPhase) || (recoveryResultVal == DROverrideRecoveryResultRequireBothOSPhases))"
+ "-[DRAnalytics submitEvent:]_block_invoke"
+ "-[DeviceRecoveryService deleteNVRAM:completion:]"
+ "-[DeviceRecoveryService eraseAllContentAndSettingsWithCompletion:]"
+ "-[DeviceRecoveryService getAllNVRAM:]"
+ "-[DeviceRecoveryService getNVRAMValueForKey:completion:]"
+ "-[DeviceRecoveryService linkPath:toPath:]"
+ "-[DeviceRecoveryService listInstalledRoots:]"
+ "-[DeviceRecoveryService mountUserDataVolumeWithPasscode:]"
+ "-[DeviceRecoveryService prepareForInternalSettingsChanges:]"
+ "-[DeviceRecoveryService processCAEventsFile:]"
+ "-[DeviceRecoveryService setNVRAMValue:forKey:completion:]"
+ "-[DeviceRecoveryService shutdown:completion:]"
+ "-[DeviceRecoveryService startService]_block_invoke"
+ "-[DeviceRecoveryService uninstallAllRoots:]"
+ "-[DeviceRecoveryService validatePasscode:completion:]"
+ "/dev/console"
+ "/private/var/MobileSoftwareUpdate/"
+ "/private/var/MobileSoftwareUpdate/DeviceRecoveryCAEvents.plist"
+ "/private/var/mnt/mobile/Library/Preferences"
+ "/private/var/mnt/preferences"
+ "/private/var/mobile/Library/Preferences"
+ "/private/var/preferences"
+ "1"
+ "23:58:12"
+ "AllowErase"
+ "AutoRecovery"
+ "BootedOSAccessPoint"
+ "BootedOSAccessPointPwd"
+ "BootedOSEncryptedWiFiData"
+ "BootedOSHasConnectivityData"
+ "Can't create recovery OS partition because the main OS partition isn't the last in the partition table (can't resize other partitions).\n"
+ "ConnectivityData.plist"
+ "Controller/NeRD"
+ "Could not allocate matching dict for kIOAESAcceleratorClass\n"
+ "Could not find kIOAESAcceleratorClass\n"
+ "Couldn't find System volume after System creation."
+ "Couldn't find baseband volume after baseband creation."
+ "Couldn't find hardware volume after hardware creation."
+ "Creating System partition failed with error: %d"
+ "Creating baseband partition failed with error: %d"
+ "Creating directory(%@) to save connectivity data\n"
+ "Creating hardware partition failed with error: %d"
+ "DREGetNVRAMAll"
+ "DREGetNVRAMAll() call returned nil"
+ "DREGetNVRAMProperty() call returned nil"
+ "DREIsRunningInDeviceRecoveryEnvironment()"
+ "DRENVRAMValueToString"
+ "DeviceRecoveryServiceInterfaceInternal"
+ "DeviceRecoveryServiceInterfaceInternalNVRAM"
+ "Duration"
+ "Events processing - CA event submission"
+ "Failed to allocate aligned crypto buffer\n\n"
+ "Failed to allocate path string to save Booted OS state\n"
+ "Failed to allocate string to save the path for the state file\n"
+ "Failed to create directory : %@\n"
+ "Failed to encrypt WiFi credentials\n"
+ "Failed to initialize NSKeyedArchiver to store wifi credentials\n"
+ "Failed to initialize dictionary for connectivity data\n"
+ "Failed to mount user data volume - failed to validate passcode: %@"
+ "Failed to remove events file %@, error is %@"
+ "Failed to validate passcode - MKBVerifyACMPasswordWithContext returned %d"
+ "Failed to write connectivity data dictionary to file(%@)\n"
+ "Found an existing recovery OS partition, no need to create again (non critical).\n"
+ "IOAESAccelerator"
+ "Jun  2 2026"
+ "New main OS partition block count is %llu.\n"
+ "New recovery OS partition block count is %llu.\n"
+ "No passcode provided for validation"
+ "OSBuildVersion"
+ "Passcode is not NSData (%s)"
+ "Passcode validation failed - MKBVerifyACMPasswordWithContext returned %d"
+ "Passcode validation only supported in DRE or internal build"
+ "Return %d trying to open kIOAESAcceleratorClass\n"
+ "Unable to allocate return crypto CFData\n"
+ "Unable to get wiFi interface information\n"
+ "[passcodeACMData isKindOfClass:[NSData class]]"
+ "[self clientHasInternalEntitlement:client]"
+ "[self clientHasPasscodeValidationEntitlement:client]"
+ "_EventName"
+ "__OSINSTALL_ENVIRONMENT"
+ "_eventsHistory"
+ "_orig"
+ "_queue_copyEventsWriteable"
+ "_queue_submitEventsFromWritableDictionary:"
+ "allInstalledRootsAndReturnError:"
+ "auto-boot"
+ "build"
+ "checkerboard"
+ "client %@ missing '%@' entitlement required for EACS"
+ "client %@ missing '%@' entitlement required for internal operations"
+ "client %@ missing '%@' entitlement required for passcode validation"
+ "clientHasInternalEntitlement:"
+ "clientHasPasscodeValidationEntitlement:"
+ "closeAndReturnError:"
+ "com.apple.DeviceRecovery.Control.Internal"
+ "com.apple.DeviceRecovery.PasscodeValidation"
+ "com.apple.DeviceRecovery.performDiagnosticsMode"
+ "com.apple.DeviceRecovery.performEACS"
+ "com.apple.DeviceRecovery.performNeRD"
+ "com.apple.DeviceRecovery.performRecoveryMode"
+ "componentsJoinedByString:"
+ "containsObject:"
+ "copyEventsWriteable"
+ "createSymbolicLinkAtPath:withDestinationPath:error:"
+ "darwinup not supported"
+ "dateInstalled"
+ "deleteNVRAM:completion:"
+ "devicerecovery"
+ "encodeObject:forKey:"
+ "encodedData"
+ "eraseAllContentAndSettingsWithCompletion:"
+ "eventsDict != nil"
+ "false"
+ "fileExistsAtPath:isDirectory:"
+ "getAllNVRAM:"
+ "getNVRAMValueForKey:completion:"
+ "initRequiringSecureCoding:"
+ "key != nil"
+ "link path not allowed: %@"
+ "linkPath:toPath:"
+ "listInstalledRoots:"
+ "missing key"
+ "missing value"
+ "mountUserDataVolumeWithPasscode:"
+ "moveItemAtPath:toPath:error:"
+ "name"
+ "nerd-erase-allowed"
+ "no events file: %@"
+ "now"
+ "numberWithInt:"
+ "one-time-boot-command"
+ "only supported in DRE env"
+ "only supported on internal build"
+ "openAndReturnError:"
+ "ota-outcome"
+ "ota-uuid"
+ "partition_probe_media after System creation failed."
+ "partition_probe_media after baseband creation failed."
+ "partition_probe_media after hardware creation failed."
+ "partition_probe_media before System creation failed."
+ "partition_probe_media before baseband creation failed."
+ "partition_probe_media before hardware creation failed."
+ "passcodeACMData != nil"
+ "perform aes => %d\n"
+ "prepareForInternalSettingsChanges:"
+ "processCAEventsFile:"
+ "processing CA events from file is not supported in DRE"
+ "recordBootEvent:"
+ "removeError == nil"
+ "result"
+ "result != nil"
+ "self.isInternalBuild"
+ "self.isRunningInDeviceRecoveryEnvironment || self.isInternalBuild"
+ "setNVRAMValue:forKey:completion:"
+ "setValue:forKey:"
+ "shutdown:completion:"
+ "string"
+ "stringByAppendingString:"
+ "stringValue"
+ "stringValue != nil"
+ "submitEvent:"
+ "submitEventsFromWritableDictionary:"
+ "timeIntervalSinceDate:"
+ "uninstallAllRoots:"
+ "uninstallAllRootsAndReturnError:"
+ "uniqueIdentifier"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\">24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\">32"
+ "v40@0:8{?=BqBB}16"
+ "v48@0:8{?=BqBB}16@?40"
+ "v48@0:8{?=BqBB}16@?<v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\">40"
+ "validatePasscode:completion:"
+ "writeConnectivityData"
+ "writeConnectivityData() call failed: %d"
- " | %@"
- "%{public}s: ADD_EVENT: Adding CoreAnalytics event to the submission queue: %{public}@"
- "%{public}s: Deleting NVRAM var: %{public}@"
- "%{public}s: Event payload data \"%{public}@\" is unsupported type \"%{public}@\". Supported Types: NSString, NSNumber, NSData, NSDate, NSError"
- "%{public}s: LockStateInfo: %@"
- "%{public}s: REMOVE_EVENT: Event %{public}@ does not exist. Nothing to do."
- "%{public}s: REMOVE_EVENT: Event without UUID passed to removeEvent"
- "%{public}s: REMOVE_EVENT: Nil event passed to removeEvent"
- "%{public}s: REMOVE_EVENT: Removed event %{public}@ from queue"
- "%{public}s: SUBMIT_ALL_EVENTS: Sending event %{public}@"
- "%{public}s: SUBMIT_ALL_EVENTS: Will submit %{public}lu total events to CoreAnalytics"
- "%{public}s: reboot:%d nerdBoot:%d"
- "%{public}s: user authentication failed - invalid passcode - backoff = %g seconds"
- "((recoveryResultVal == DROverrideRecoveryResultNoOverride) || (recoveryResultVal == DROverrideBrainLoadResultForceFailure) || (recoveryResultVal == DROverrideRecoveryResultRequireOSBootPhase) || (recoveryResultVal == DROverrideRecoveryResultRequirePostUserUnlockPhase) || (recoveryResultVal == DROverrideRecoveryResultRequireBothOSPhases))"
- "-[DRAnalytics _queue_removeEvent:]"
- "-[DRAnalytics _queue_submitAllEvents]"
- "-[DRAnalytics addEvent:]_block_invoke"
- "-[DeviceRecoveryService shutdown:andReboot:andPrepareNeRDBoot:]"
- "22:11:36"
- "Apr 18 2026"
- "Can't create recovery OS partition becuase the main OS partition isn't the last in the partition table (can't resize other partitions).\n"
- "Failed to mount user data volume - invalid passcode: %@"
- "Found an existing recovery OS partition, no need to create again (non cretical).\n"
- "New recovery OS partiton block count is %llu.\n"
- "T@\"NSDictionary\",R,&,N,V_events"
- "_events"
- "_queue_removeEvent:"
- "_queue_submitAllEvents"
- "addEvent:"
- "allValues"
- "deleteCharactersInRange:"
- "events"
- "shutdown:andReboot:andPrepareNeRDBoot:"
- "submitAllEvents"
- "success && (mountError == nil)"
- "v32@0:8@?16B24B28"
- "v32@0:8@?<v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\">16B24B28"

```
