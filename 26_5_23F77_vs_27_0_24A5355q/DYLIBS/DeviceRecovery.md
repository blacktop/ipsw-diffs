## DeviceRecovery

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery`

```diff

-107.100.11.0.0
-  __TEXT.__text: 0x1d768
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x5e8
-  __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x2b8
-  __TEXT.__cstring: 0x3eab
-  __TEXT.__oslogstring: 0xe90
-  __TEXT.__unwind_info: 0x5e0
-  __TEXT.__objc_classname: 0xa2
-  __TEXT.__objc_methname: 0x1074
-  __TEXT.__objc_methtype: 0x2d5
-  __TEXT.__objc_stubs: 0xa20
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x4e0
+142.0.0.0.0
+  __TEXT.__text: 0x1fcc0
+  __TEXT.__objc_methlist: 0x700
+  __TEXT.__const: 0x1a0
+  __TEXT.__oslogstring: 0x12d5
+  __TEXT.__cstring: 0x4591
+  __TEXT.__gcc_except_tab: 0x248
+  __TEXT.__unwind_info: 0x6c0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x530
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x488
-  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_selrefs: 0x510
+  __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x308
+  __DATA_CONST.__got: 0xb0
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0xea0
-  __AUTH_CONST.__objc_const: 0x788
+  __AUTH_CONST.__cfstring: 0xfc0
+  __AUTH_CONST.__objc_const: 0x820
   __AUTH_CONST.__objc_intobj: 0x48
-  __DATA.__objc_ivar: 0x5c
-  __DATA.__data: 0xca
+  __AUTH_CONST.__auth_got: 0x360
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x60
+  __DATA.__data: 0x18a
   __DATA.__bss: 0x58
-  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2321D373-B3DC-33BA-8130-4E06DE936989
-  Functions: 837
-  Symbols:   1883
-  CStrings:  842
+  UUID: E8B9099C-8CC7-38F8-9DCE-AFD521326933
+  Functions: 933
+  Symbols:   2096
+  CStrings:  674
 
Symbols:
+ -[DeviceRecoveryController _shutdownWithCompletion:completion:]
+ -[DeviceRecoveryController _shutdownWithCompletion:completion:].cold.1
+ -[DeviceRecoveryController _shutdownWithCompletion:completion:].cold.2
+ -[DeviceRecoveryController _shutdownWithCompletion:completion:].cold.3
+ -[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:]
+ -[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:].cold.1
+ -[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:].cold.2
+ -[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:].cold.3
+ -[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:].cold.4
+ -[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:].cold.5
+ -[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:].cold.6
+ -[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:].cold.7
+ -[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:].cold.8
+ -[DeviceRecoveryController eraseAllContentAndSettingsWithCompletion:]
+ -[DeviceRecoveryController eraseAllContentAndSettingsWithCompletion:].cold.1
+ -[DeviceRecoveryController eraseAllContentAndSettingsWithCompletion:].cold.2
+ -[DeviceRecoveryController eraseAllContentAndSettingsWithCompletion:].cold.3
+ -[DeviceRecoveryController isInternalBuild]
+ -[DeviceRecoveryController rebootToEnvironment:completion:]
+ -[DeviceRecoveryController rebootToNeRDWithCompletion:autoRecovery:allowErase:]
+ -[DeviceRecoveryController setIsInternalBuild:]
+ -[DeviceRecoveryController verifyPasscode:completion:]
+ -[DeviceRecoveryController(Internal) deleteNVRAM:completion:]
+ -[DeviceRecoveryController(Internal) deleteNVRAM:completion:].cold.1
+ -[DeviceRecoveryController(Internal) deleteNVRAM:completion:].cold.2
+ -[DeviceRecoveryController(Internal) deleteNVRAM:completion:].cold.3
+ -[DeviceRecoveryController(Internal) deleteNVRAM:completion:].cold.4
+ -[DeviceRecoveryController(Internal) deleteNVRAM:completion:].cold.5
+ -[DeviceRecoveryController(Internal) getAllNVRAM:]
+ -[DeviceRecoveryController(Internal) getAllNVRAM:].cold.1
+ -[DeviceRecoveryController(Internal) getAllNVRAM:].cold.2
+ -[DeviceRecoveryController(Internal) getAllNVRAM:].cold.3
+ -[DeviceRecoveryController(Internal) getAllNVRAM:].cold.4
+ -[DeviceRecoveryController(Internal) getNVRAMValueForKey:completion:]
+ -[DeviceRecoveryController(Internal) getNVRAMValueForKey:completion:].cold.1
+ -[DeviceRecoveryController(Internal) getNVRAMValueForKey:completion:].cold.2
+ -[DeviceRecoveryController(Internal) getNVRAMValueForKey:completion:].cold.3
+ -[DeviceRecoveryController(Internal) getNVRAMValueForKey:completion:].cold.4
+ -[DeviceRecoveryController(Internal) getNVRAMValueForKey:completion:].cold.5
+ -[DeviceRecoveryController(Internal) listInstalledRoots:]
+ -[DeviceRecoveryController(Internal) listInstalledRoots:].cold.1
+ -[DeviceRecoveryController(Internal) listInstalledRoots:].cold.2
+ -[DeviceRecoveryController(Internal) listInstalledRoots:].cold.3
+ -[DeviceRecoveryController(Internal) listInstalledRoots:].cold.4
+ -[DeviceRecoveryController(Internal) prepareForInternalSettingsChanges:]
+ -[DeviceRecoveryController(Internal) prepareForInternalSettingsChanges:].cold.1
+ -[DeviceRecoveryController(Internal) prepareForInternalSettingsChanges:].cold.2
+ -[DeviceRecoveryController(Internal) prepareForInternalSettingsChanges:].cold.3
+ -[DeviceRecoveryController(Internal) prepareForInternalSettingsChanges:].cold.4
+ -[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:]
+ -[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:].cold.1
+ -[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:].cold.2
+ -[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:].cold.3
+ -[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:].cold.4
+ -[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:].cold.5
+ -[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:].cold.6
+ -[DeviceRecoveryController(Internal) uninstallAllRoots:]
+ -[DeviceRecoveryController(Internal) uninstallAllRoots:].cold.1
+ -[DeviceRecoveryController(Internal) uninstallAllRoots:].cold.2
+ -[DeviceRecoveryController(Internal) uninstallAllRoots:].cold.3
+ -[DeviceRecoveryController(Internal) uninstallAllRoots:].cold.4
+ _ACMGetEnvironmentVariableData
+ _CFRelease
+ _DRAnalyticsEventPerformDiagnosticsMode
+ _DRAnalyticsEventPerformEACS
+ _DRAnalyticsEventPerformNeRD
+ _DRAnalyticsEventPerformRecoveryMode
+ _DRAnalyticsKeyDuration
+ _DREGetNVRAMAll
+ _DREGetNVRAMAll.cold.1
+ _DRENVRAMValueToString
+ _IORegistryEntryCreateCFProperties
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_IVAR_$_DeviceRecoveryController._isInternalBuild
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ __OBJC_$_INSTANCE_METHODS_DeviceRecoveryController(Internal)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DeviceRecoveryServiceInterfaceInternal
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DeviceRecoveryServiceInterfaceInternalNVRAM
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DeviceRecoveryServiceInterfaceInternal
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DeviceRecoveryServiceInterfaceInternalNVRAM
+ __OBJC_$_PROTOCOL_REFS_DeviceRecoveryServiceInterfaceInternal
+ __OBJC_LABEL_PROTOCOL_$_DeviceRecoveryServiceInterfaceInternal
+ __OBJC_LABEL_PROTOCOL_$_DeviceRecoveryServiceInterfaceInternalNVRAM
+ __OBJC_PROTOCOL_$_DeviceRecoveryServiceInterfaceInternal
+ __OBJC_PROTOCOL_$_DeviceRecoveryServiceInterfaceInternalNVRAM
+ __OBJC_PROTOCOL_REFERENCE_$_DeviceRecoveryServiceInterfaceInternal
+ ___32-[DeviceRecoveryController init]_block_invoke.46
+ ___32-[DeviceRecoveryController init]_block_invoke.47
+ ___32-[DeviceRecoveryController init]_block_invoke.47.cold.1
+ ___32-[DeviceRecoveryController init]_block_invoke.52
+ ___32-[DeviceRecoveryController init]_block_invoke.52.cold.1
+ ___32-[DeviceRecoveryController init]_block_invoke.52.cold.2
+ ___32-[DeviceRecoveryController init]_block_invoke.52.cold.3
+ ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.77
+ ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.77.cold.1
+ ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.77.cold.2
+ ___50-[DeviceRecoveryController(Internal) getAllNVRAM:]_block_invoke
+ ___50-[DeviceRecoveryController(Internal) getAllNVRAM:]_block_invoke.21
+ ___50-[DeviceRecoveryController(Internal) getAllNVRAM:]_block_invoke.21.cold.1
+ ___50-[DeviceRecoveryController(Internal) getAllNVRAM:]_block_invoke.cold.1
+ ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.109
+ ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.109.cold.1
+ ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.108
+ ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.108.cold.1
+ ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.106
+ ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.106.cold.1
+ ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.106.cold.2
+ ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.105
+ ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.105.cold.1
+ ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.105.cold.2
+ ___56-[DeviceRecoveryController(Internal) uninstallAllRoots:]_block_invoke
+ ___56-[DeviceRecoveryController(Internal) uninstallAllRoots:]_block_invoke.20
+ ___56-[DeviceRecoveryController(Internal) uninstallAllRoots:]_block_invoke.20.cold.1
+ ___56-[DeviceRecoveryController(Internal) uninstallAllRoots:]_block_invoke.cold.1
+ ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.76
+ ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.76.cold.1
+ ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.76.cold.2
+ ___57-[DeviceRecoveryController(Internal) listInstalledRoots:]_block_invoke
+ ___57-[DeviceRecoveryController(Internal) listInstalledRoots:]_block_invoke.19
+ ___57-[DeviceRecoveryController(Internal) listInstalledRoots:]_block_invoke.19.cold.1
+ ___57-[DeviceRecoveryController(Internal) listInstalledRoots:]_block_invoke.cold.1
+ ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.104
+ ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.104.cold.1
+ ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.104.cold.2
+ ___61-[DeviceRecoveryController(Internal) deleteNVRAM:completion:]_block_invoke
+ ___61-[DeviceRecoveryController(Internal) deleteNVRAM:completion:]_block_invoke.32
+ ___61-[DeviceRecoveryController(Internal) deleteNVRAM:completion:]_block_invoke.32.cold.1
+ ___61-[DeviceRecoveryController(Internal) deleteNVRAM:completion:]_block_invoke.cold.1
+ ___63-[DeviceRecoveryController _shutdownWithCompletion:completion:]_block_invoke
+ ___63-[DeviceRecoveryController _shutdownWithCompletion:completion:]_block_invoke.107
+ ___63-[DeviceRecoveryController _shutdownWithCompletion:completion:]_block_invoke.107.cold.1
+ ___63-[DeviceRecoveryController _shutdownWithCompletion:completion:]_block_invoke.107.cold.2
+ ___63-[DeviceRecoveryController _shutdownWithCompletion:completion:]_block_invoke.cold.1
+ ___65-[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:]_block_invoke.61
+ ___65-[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:]_block_invoke.61.cold.1
+ ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.103
+ ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.103.cold.1
+ ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.103.cold.2
+ ___69-[DeviceRecoveryController eraseAllContentAndSettingsWithCompletion:]_block_invoke
+ ___69-[DeviceRecoveryController eraseAllContentAndSettingsWithCompletion:]_block_invoke.102
+ ___69-[DeviceRecoveryController eraseAllContentAndSettingsWithCompletion:]_block_invoke.102.cold.1
+ ___69-[DeviceRecoveryController eraseAllContentAndSettingsWithCompletion:]_block_invoke.102.cold.2
+ ___69-[DeviceRecoveryController eraseAllContentAndSettingsWithCompletion:]_block_invoke.cold.1
+ ___69-[DeviceRecoveryController(Internal) getNVRAMValueForKey:completion:]_block_invoke
+ ___69-[DeviceRecoveryController(Internal) getNVRAMValueForKey:completion:]_block_invoke.26
+ ___69-[DeviceRecoveryController(Internal) getNVRAMValueForKey:completion:]_block_invoke.26.cold.1
+ ___69-[DeviceRecoveryController(Internal) getNVRAMValueForKey:completion:]_block_invoke.cold.1
+ ___70-[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:]_block_invoke
+ ___70-[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:]_block_invoke.31
+ ___70-[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:]_block_invoke.31.cold.1
+ ___70-[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:]_block_invoke.cold.1
+ ___72-[DeviceRecoveryController(Internal) prepareForInternalSettingsChanges:]_block_invoke
+ ___72-[DeviceRecoveryController(Internal) prepareForInternalSettingsChanges:]_block_invoke.17
+ ___72-[DeviceRecoveryController(Internal) prepareForInternalSettingsChanges:]_block_invoke.17.cold.1
+ ___72-[DeviceRecoveryController(Internal) prepareForInternalSettingsChanges:]_block_invoke.cold.1
+ ___75-[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:]_block_invoke
+ ___75-[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:]_block_invoke.100
+ ___75-[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:]_block_invoke.100.cold.1
+ ___75-[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:]_block_invoke.101
+ ___75-[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:]_block_invoke.101.cold.1
+ ___75-[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:]_block_invoke.101.cold.2
+ ___78-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke.110
+ ___78-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke.110.cold.1
+ ___block_descriptor_56_e8_32s40s48bs_e51_v32?0"NSError"8"NSDictionary"16"NSDictionary"24ls32l8s40l8s48l8
+ ___block_literal_global.50
+ ___block_literal_global.59
+ ___block_literal_global.63
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$_shutdownWithCompletion:completion:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$authenticationHelper:verifyPasscode:completion:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$deleteNVRAM:completion:
+ _objc_msgSend$dictionary
+ _objc_msgSend$eraseAllContentAndSettingsWithCompletion:
+ _objc_msgSend$getAllNVRAM:
+ _objc_msgSend$getNVRAMValueForKey:completion:
+ _objc_msgSend$isInternalBuild
+ _objc_msgSend$listInstalledRoots:
+ _objc_msgSend$prepareForInternalSettingsChanges:
+ _objc_msgSend$setNVRAMValue:forKey:completion:
+ _objc_msgSend$shutdown:completion:
+ _objc_msgSend$string
+ _objc_msgSend$stringValue
+ _objc_msgSend$uninstallAllRoots:
+ _objc_msgSend$validatePasscode:completion:
+ _objc_release_x27
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x8
- -[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]
- -[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:].cold.1
- -[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:].cold.2
- -[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:].cold.3
- -[DeviceRecoveryController rebootToNeRDWithCompletion:]
- -[DeviceRecoveryController userAuthenticated:completion:].cold.1
- -[DeviceRecoveryController userAuthenticated:completion:].cold.2
- -[DeviceRecoveryController userAuthenticated:completion:].cold.3
- -[DeviceRecoveryController userAuthenticated:completion:].cold.4
- -[DeviceRecoveryController userAuthenticated:completion:].cold.5
- -[DeviceRecoveryController userAuthenticated:completion:].cold.6
- -[DeviceRecoveryController userAuthenticated:completion:].cold.7
- -[DeviceRecoveryController userAuthenticated:completion:].cold.8
- GCC_except_table112
- GCC_except_table113
- GCC_except_table114
- GCC_except_table43
- GCC_except_table84
- __OBJC_$_INSTANCE_METHODS_DeviceRecoveryController
- ___32-[DeviceRecoveryController init]_block_invoke.32
- ___32-[DeviceRecoveryController init]_block_invoke.33
- ___32-[DeviceRecoveryController init]_block_invoke.33.cold.1
- ___32-[DeviceRecoveryController init]_block_invoke.38
- ___32-[DeviceRecoveryController init]_block_invoke.38.cold.1
- ___32-[DeviceRecoveryController init]_block_invoke.38.cold.2
- ___32-[DeviceRecoveryController init]_block_invoke.38.cold.3
- ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.63
- ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.63.cold.1
- ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.63.cold.2
- ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.94
- ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.94.cold.1
- ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.93
- ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.93.cold.1
- ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.91
- ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.91.cold.1
- ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.91.cold.2
- ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.90
- ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.90.cold.1
- ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.90.cold.2
- ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.62
- ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.62.cold.1
- ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.62.cold.2
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.86
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.86.cold.1
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.87
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.87.cold.1
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.87.cold.2
- ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.89
- ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.89.cold.1
- ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.89.cold.2
- ___65-[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:]_block_invoke.47
- ___65-[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:]_block_invoke.47.cold.1
- ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.88
- ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.88.cold.1
- ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.88.cold.2
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.92
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.92.cold.1
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.92.cold.2
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.cold.1
- ___78-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke.95
- ___78-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke.95.cold.1
- ___block_literal_global.31
- ___block_literal_global.36
- ___block_literal_global.49
- _objc_msgSend$_shutdownWithCompletion:andReboot:andSetNeRDBoot:
- _objc_msgSend$shutdown:andReboot:andPrepareNeRDBoot:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%02x"
+ "%{public}s: Could not load NVRAM info (%d)"
+ "%{public}s: EACS completed successfully (device should be rebooting)"
+ "%{public}s: EACS failed: %{public}@"
+ "%{public}s: Failed to convert nvram value %{public}@ to string"
+ "%{public}s: Framework: eraseAllContentAndSettingsWithCompletion called"
+ "%{public}s: Reading NVRAM var: %{public}@"
+ "%{public}s: failed to delete nvram %{public}@: %{public}@"
+ "%{public}s: failed to get all nvram: %{public}@"
+ "%{public}s: failed to get nvram value for key %{public}@: %{public}@"
+ "%{public}s: failed to list install roots: %{public}@"
+ "%{public}s: failed to prepare for internal settings changes: %{public}@"
+ "%{public}s: failed to set nvram %{public}@=%{public}@: %{public}@"
+ "%{public}s: failed to uninstall roots: %{public}@"
+ "%{public}s: got all nvram: %{public}@"
+ "%{public}s: got nvram: %{public}@"
+ "%{public}s: passcode authentication failed: %{public}@"
+ "%{public}s: passcode authentication succeeded"
+ "%{public}s: successfully deleted nvram %{public}@"
+ "%{public}s: successfully listed installed roots: %{public}@"
+ "%{public}s: successfully prepared for internal settings changes: %{public}@"
+ "%{public}s: successfully set nvram %{public}@=%{public}@"
+ "%{public}s: successfully uninstalled roots"
+ "((recoveryResultVal == DROverrideRecoveryResultNoOverride) || (recoveryResultVal == DROverrideRecoveryResultForceFailure) || (recoveryResultVal == DROverrideRecoveryResultRequireOSBootPhase) || (recoveryResultVal == DROverrideRecoveryResultRequirePostUserUnlockPhase) || (recoveryResultVal == DROverrideRecoveryResultRequireBothOSPhases))"
+ "-[DeviceRecoveryController _shutdownWithCompletion:completion:]"
+ "-[DeviceRecoveryController _shutdownWithCompletion:completion:]_block_invoke"
+ "-[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:]"
+ "-[DeviceRecoveryController authenticationHelper:verifyPasscode:completion:]_block_invoke"
+ "-[DeviceRecoveryController eraseAllContentAndSettingsWithCompletion:]"
+ "-[DeviceRecoveryController eraseAllContentAndSettingsWithCompletion:]_block_invoke"
+ "-[DeviceRecoveryController(Internal) deleteNVRAM:completion:]"
+ "-[DeviceRecoveryController(Internal) deleteNVRAM:completion:]_block_invoke"
+ "-[DeviceRecoveryController(Internal) getAllNVRAM:]"
+ "-[DeviceRecoveryController(Internal) getAllNVRAM:]_block_invoke"
+ "-[DeviceRecoveryController(Internal) getNVRAMValueForKey:completion:]"
+ "-[DeviceRecoveryController(Internal) getNVRAMValueForKey:completion:]_block_invoke"
+ "-[DeviceRecoveryController(Internal) listInstalledRoots:]"
+ "-[DeviceRecoveryController(Internal) listInstalledRoots:]_block_invoke"
+ "-[DeviceRecoveryController(Internal) prepareForInternalSettingsChanges:]"
+ "-[DeviceRecoveryController(Internal) prepareForInternalSettingsChanges:]_block_invoke"
+ "-[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:]"
+ "-[DeviceRecoveryController(Internal) setNVRAMValue:forKey:completion:]_block_invoke"
+ "-[DeviceRecoveryController(Internal) uninstallAllRoots:]"
+ "-[DeviceRecoveryController(Internal) uninstallAllRoots:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DeviceRecovery/DeviceRecovery_Framework/DeviceRecoveryController+Internal.m"
+ "ACMCredential - ACMCredentialDataPKITokenValidated"
+ "ACMCredential - ACMCredentialDataPKITokenValidated2"
+ "ACMGetEnvironmentVariableData"
+ "DREGetNVRAMAll"
+ "DRENVRAMValueToString"
+ "Duration"
+ "No key"
+ "No value"
+ "Not allowed on non-internal build"
+ "com.apple.DeviceRecovery.performDiagnosticsMode"
+ "com.apple.DeviceRecovery.performEACS"
+ "com.apple.DeviceRecovery.performNeRD"
+ "com.apple.DeviceRecovery.performRecoveryMode"
+ "key != NULL"
+ "self.isInternalBuild"
+ "value != NULL"
- "%{public}s: Deleting NVRAM var: %{public}@"
- "%{public}s: failed to register user authentication: %{public}@"
- "((recoveryResultVal == DROverrideRecoveryResultNoOverride) || (recoveryResultVal == DROverrideBrainLoadResultForceFailure) || (recoveryResultVal == DROverrideRecoveryResultRequireOSBootPhase) || (recoveryResultVal == DROverrideRecoveryResultRequirePostUserUnlockPhase) || (recoveryResultVal == DROverrideRecoveryResultRequireBothOSPhases))"
- "-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]"
- "-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke"
- "-[DeviceRecoveryController userAuthenticated:completion:]"
- "-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8@16"
- "B"
- "B16@0:8"
- "CreateCookieAndCleanup"
- "DREEntryDescription"
- "DREEntryReasonEnum"
- "DREStringFromEntryReason:"
- "DeviceRecoveryController"
- "DeviceRecoveryEnvironmentWorker"
- "DeviceRecoveryOverrideClient"
- "DeviceRecoveryOverrideServiceInterface"
- "DeviceRecoveryServiceInterface"
- "T@\"NSDictionary\",R,N"
- "T@\"NSNumber\",&,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serviceQueue"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_timer"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_entryDescription"
- "T@\"NSString\",&,V_mainOSLanguageCode"
- "T@\"NSString\",R,V_deviceRecoveryEntryReason"
- "T@\"NSXPCConnection\",&,V_serviceConnection"
- "TB,N,V_isInternalBuild"
- "TB,N,V_testModeEnabled"
- "TB,N,V_userApprovedDiagnosticsSubmission"
- "TB,R,V_isRunningInDeviceRecoveryEnvironment"
- "TB,V_dataVolumeMounted"
- "TB,V_isPasscodeSet"
- "TB,V_issuesScanComplete"
- "TB,V_networkAvailable"
- "TB,V_recoveryBrainLoaded"
- "TB,V_recoveryComplete"
- "TB,V_repairableIssuesFound"
- "TB,V_userAuthenticated"
- "Tc,N,V_timerCount"
- "Ti,N"
- "Ti,N,V_entryReason"
- "Ti,V_simplePasscodeType"
- "Ti,V_unlockScreenType"
- "UTF8String"
- "_dataVolumeMounted"
- "_deviceRecoveryEntryReason"
- "_entryDescription"
- "_entryReason"
- "_isInternalBuild"
- "_isPasscodeSet"
- "_isRunningInDeviceRecoveryEnvironment"
- "_issuesScanComplete"
- "_mainOSLanguageCode"
- "_networkAvailable"
- "_recoveryBrainLoaded"
- "_recoveryComplete"
- "_repairableIssuesFound"
- "_serviceConnection"
- "_serviceQueue"
- "_shutdownWithCompletion:andReboot:andSetNeRDBoot:"
- "_simplePasscodeType"
- "_testModeEnabled"
- "_timer"
- "_timerCount"
- "_unlockScreenType"
- "_userApprovedDiagnosticsSubmission"
- "_userAuthenticated"
- "activate"
- "allOverrides"
- "boolValue"
- "brainBundlePath"
- "brainLoadResult"
- "brainType"
- "bytes"
- "c"
- "c16@0:8"
- "dataVolumeMounted"
- "dataWithBytes:length:"
- "defaultManager"
- "description"
- "deviceRecoveryEntryReason"
- "dictionaryWithCapacity:"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjects:forKeys:count:"
- "disableRecoveryAutoBoot:"
- "enableTestMode:"
- "enableTestModeWithCompletion:"
- "errorWithDomain:code:userInfo:"
- "fetchOverride:"
- "fetchOverride:callback:"
- "fetchOverrides:"
- "fetchState:"
- "fileExistsAtPath:"
- "freeSpaceThreshold"
- "getObjectFromInternalCookie:"
- "i16@0:8"
- "initWithData:encoding:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "isEqualToString:"
- "isInternalBuild"
- "isPasscodeSet"
- "isRunningInDeviceRecoveryEnvironment"
- "issuesScanComplete"
- "issuesScanResult"
- "length"
- "loadAccessibilitySettingsToDefaults:"
- "loadAccessibilitySettingsToDefaultsWithCompletion:"
- "loadRecoveryBrain:"
- "loadRecoveryBrainWithCompletion:"
- "mainOSLanguageCode"
- "mutableCopy"
- "networkAvailable"
- "networkAvailableResult"
- "numberWithBool:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "populateDREDescription:"
- "populateDREReason"
- "processAttributes:"
- "reboot:"
- "rebootToNeRDWithCompletion:"
- "rebootWithCompletion:"
- "recoverDevice:"
- "recoverDeviceFromBootedOS:"
- "recoverDeviceWithCompletion:"
- "recoveryBrainLoaded"
- "recoveryComplete"
- "recoveryResult"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllOverrides"
- "removeAllOverrides:"
- "removeOverride:callback:"
- "repairableIssuesFound"
- "reportNetworkAvailability:"
- "reportNetworkAvailabilityWithCompletion:"
- "resetRecovery:"
- "scanForIssues:"
- "scanForIssuesWithCompletion:"
- "serviceConnection"
- "serviceQueue"
- "setBrainBundlePath:"
- "setBrainLoadResult:"
- "setBrainType:"
- "setDataVolumeMounted:"
- "setDiagnosticsSubmissionApproved:completion:"
- "setEntryDescription:"
- "setEntryReason:"
- "setFreeSpaceThreshold:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsInternalBuild:"
- "setIsPasscodeSet:"
- "setIssuesScanComplete:"
- "setIssuesScanResult:"
- "setMainOSLanguageCode:"
- "setNetworkAvailable:"
- "setNetworkAvailableResult:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOverride:value:"
- "setOverride:value:callback:"
- "setRecoveryBrainLoaded:"
- "setRecoveryComplete:"
- "setRecoveryResult:"
- "setRemoteObjectInterface:"
- "setRepairableIssuesFound:"
- "setServiceConnection:"
- "setServiceQueue:"
- "setSimplePasscodeType:"
- "setSystemDataPath:"
- "setTestModeEnabled:"
- "setTimer:"
- "setTimerCount:"
- "setUnlockScreenType:"
- "setUpdateVolumePath:"
- "setUserApprovedDiagnosticsSubmission:"
- "setUserAuthResult:"
- "setUserAuthenticated:"
- "setUserDataPath:"
- "setupPopulateDREDescription"
- "sharedController"
- "sharedWorker"
- "shutdown:andReboot:andPrepareNeRDBoot:"
- "shutdownWithCompletion:"
- "simplePasscodeType"
- "stringByAppendingFormat:"
- "stringWithFormat:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemDataPath"
- "testModeEnabled"
- "timer"
- "timerCount"
- "unlockScreenType"
- "unsignedCharValue"
- "unsignedIntValue"
- "updateVolumePath"
- "userApprovedDiagnosticsSubmission"
- "userAuthResult"
- "userAuthenticated"
- "userAuthenticated:completion:"
- "userDataPath"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8c16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\">16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\">20"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@?16B24B28"
- "v32@0:8@?<v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\">16B24B28"
- "v40@0:8@\"NSString\"16@24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "writeToFile:atomically:"

```
