## DeviceRecoveryBrainSupport

> `/System/Library/PrivateFrameworks/DeviceRecoveryBrainSupport.framework/DeviceRecoveryBrainSupport`

```diff

-85.0.0.0.9
-  __TEXT.__text: 0x19590
-  __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x9ec
+88.0.0.0.4
+  __TEXT.__text: 0x1d01c
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0xd04
   __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x49c
-  __TEXT.__cstring: 0x361f
-  __TEXT.__oslogstring: 0x2786
-  __TEXT.__unwind_info: 0x448
+  __TEXT.__oslogstring: 0x2a9b
+  __TEXT.__cstring: 0x3c48
+  __TEXT.__gcc_except_tab: 0x5bc
+  __TEXT.__unwind_info: 0x538
   __TEXT.__eh_frame: 0xa0
-  __TEXT.__objc_classname: 0x12d
-  __TEXT.__objc_methname: 0x1a27
-  __TEXT.__objc_methtype: 0x38f
-  __TEXT.__objc_stubs: 0x17a0
-  __DATA_CONST.__got: 0x160
-  __DATA_CONST.__const: 0x880
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__objc_classname: 0x16b
+  __TEXT.__objc_methname: 0x203f
+  __TEXT.__objc_methtype: 0x482
+  __TEXT.__objc_stubs: 0x1b40
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x8e8
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x850
+  __DATA_CONST.__objc_selrefs: 0xa40
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x578
-  __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x21c0
-  __AUTH_CONST.__objc_const: 0xa20
+  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__cfstring: 0x22c0
+  __AUTH_CONST.__objc_const: 0xdb8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x48
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x23c
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4BB4828B-C131-395C-A203-4113600C7E3C
-  Functions: 409
-  Symbols:   1101
-  CStrings:  1295
+  UUID: 353BB71C-8656-3C19-8018-DD5E8F62F6C8
+  Functions: 520
+  Symbols:   1311
+  CStrings:  1448
 
Symbols:
+ +[DeviceRecoveryEnvironmentWorker sharedWorker]
+ +[DeviceRecoveryEnvironmentWorker sharedWorker].cold.1
+ -[DeviceRecoveryBrain ERMContentsPresent]
+ -[DeviceRecoveryBrain ERMContentsPresent].cold.1
+ -[DeviceRecoveryBrain ERMContentsPresent].cold.2
+ -[DeviceRecoveryBrain filesInDirectory:withPrefix:extension:excludeSymlinks:]
+ -[DeviceRecoveryBrain filesInDirectory:withPrefix:extension:excludeSymlinks:].cold.1
+ -[DeviceRecoveryBrain filesInDirectory:withPrefix:extension:excludeSymlinks:].cold.2
+ -[DeviceRecoveryBrain filesInDirectory:withPrefix:extension:excludeSymlinks:].cold.3
+ -[DeviceRecoveryBrain initExternalBrain:]
+ -[DeviceRecoveryBrain initExternalBrain:].cold.1
+ -[DeviceRecoveryBrain isExternalBrain]
+ -[DeviceRecoveryBrain recoverTestFiles]
+ -[DeviceRecoveryBrain recoverTestFiles].cold.1
+ -[DeviceRecoveryBrain recoverTestFiles].cold.2
+ -[DeviceRecoveryBrain removeERMContents]
+ -[DeviceRecoveryBrain removeERMContents].cold.1
+ -[DeviceRecoveryBrain removeERMContents].cold.2
+ -[DeviceRecoveryBrain scanForERMContents]
+ -[DeviceRecoveryBrain scanForTestFiles]
+ -[DeviceRecoveryBrain scanForTestFiles].cold.1
+ -[DeviceRecoveryBrain scanForTestFiles].cold.2
+ -[DeviceRecoveryEnvironmentWorker .cxx_destruct]
+ -[DeviceRecoveryEnvironmentWorker CreateCookieAndCleanup]
+ -[DeviceRecoveryEnvironmentWorker DREEntryDescription]
+ -[DeviceRecoveryEnvironmentWorker DREEntryReasonEnum]
+ -[DeviceRecoveryEnvironmentWorker DREStringFromEntryReason:]
+ -[DeviceRecoveryEnvironmentWorker entryDescription]
+ -[DeviceRecoveryEnvironmentWorker entryReason]
+ -[DeviceRecoveryEnvironmentWorker init]
+ -[DeviceRecoveryEnvironmentWorker isInternalBuild]
+ -[DeviceRecoveryEnvironmentWorker populateDREDescription:]
+ -[DeviceRecoveryEnvironmentWorker populateDREDescription:].cold.1
+ -[DeviceRecoveryEnvironmentWorker populateDREDescription:].cold.2
+ -[DeviceRecoveryEnvironmentWorker populateDREDescription:].cold.3
+ -[DeviceRecoveryEnvironmentWorker populateDREReason]
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.1
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.2
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.3
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.4
+ -[DeviceRecoveryEnvironmentWorker serviceQueue]
+ -[DeviceRecoveryEnvironmentWorker setEntryDescription:]
+ -[DeviceRecoveryEnvironmentWorker setEntryReason:]
+ -[DeviceRecoveryEnvironmentWorker setIsInternalBuild:]
+ -[DeviceRecoveryEnvironmentWorker setServiceQueue:]
+ -[DeviceRecoveryEnvironmentWorker setTimer:]
+ -[DeviceRecoveryEnvironmentWorker setTimerCount:]
+ -[DeviceRecoveryEnvironmentWorker setupPopulateDREDescription]
+ -[DeviceRecoveryEnvironmentWorker timerCount]
+ -[DeviceRecoveryEnvironmentWorker timer]
+ -[DeviceRecoveryOverrideClient .cxx_destruct]
+ -[DeviceRecoveryOverrideClient allOverrides]
+ -[DeviceRecoveryOverrideClient allOverrides].cold.1
+ -[DeviceRecoveryOverrideClient allOverrides].cold.2
+ -[DeviceRecoveryOverrideClient brainBundlePath]
+ -[DeviceRecoveryOverrideClient brainLoadResult]
+ -[DeviceRecoveryOverrideClient brainType]
+ -[DeviceRecoveryOverrideClient fetchOverride:]
+ -[DeviceRecoveryOverrideClient fetchOverride:].cold.1
+ -[DeviceRecoveryOverrideClient fetchOverride:].cold.2
+ -[DeviceRecoveryOverrideClient freeSpaceThreshold]
+ -[DeviceRecoveryOverrideClient init]
+ -[DeviceRecoveryOverrideClient init].cold.1
+ -[DeviceRecoveryOverrideClient init].cold.2
+ -[DeviceRecoveryOverrideClient issuesScanResult]
+ -[DeviceRecoveryOverrideClient networkAvailableResult]
+ -[DeviceRecoveryOverrideClient recoveryResult]
+ -[DeviceRecoveryOverrideClient removeAllOverrides]
+ -[DeviceRecoveryOverrideClient removeAllOverrides].cold.1
+ -[DeviceRecoveryOverrideClient removeAllOverrides].cold.2
+ -[DeviceRecoveryOverrideClient serviceConnection]
+ -[DeviceRecoveryOverrideClient setBrainBundlePath:]
+ -[DeviceRecoveryOverrideClient setBrainLoadResult:]
+ -[DeviceRecoveryOverrideClient setBrainType:]
+ -[DeviceRecoveryOverrideClient setFreeSpaceThreshold:]
+ -[DeviceRecoveryOverrideClient setIssuesScanResult:]
+ -[DeviceRecoveryOverrideClient setNetworkAvailableResult:]
+ -[DeviceRecoveryOverrideClient setOverride:value:]
+ -[DeviceRecoveryOverrideClient setOverride:value:].cold.1
+ -[DeviceRecoveryOverrideClient setOverride:value:].cold.2
+ -[DeviceRecoveryOverrideClient setOverride:value:].cold.3
+ -[DeviceRecoveryOverrideClient setOverride:value:].cold.4
+ -[DeviceRecoveryOverrideClient setOverride:value:].cold.5
+ -[DeviceRecoveryOverrideClient setOverride:value:].cold.6
+ -[DeviceRecoveryOverrideClient setRecoveryResult:]
+ -[DeviceRecoveryOverrideClient setServiceConnection:]
+ -[DeviceRecoveryOverrideClient setSystemDataPath:]
+ -[DeviceRecoveryOverrideClient setUpdateVolumePath:]
+ -[DeviceRecoveryOverrideClient setUserAuthResult:]
+ -[DeviceRecoveryOverrideClient setUserDataPath:]
+ -[DeviceRecoveryOverrideClient systemDataPath]
+ -[DeviceRecoveryOverrideClient updateVolumePath]
+ -[DeviceRecoveryOverrideClient userAuthResult]
+ -[DeviceRecoveryOverrideClient userDataPath]
+ DRECopyIORegAsStringWithError.cold.1
+ DRECopyIORegAsStringWithError.cold.2
+ DRECopyIORegEntryWithError.cold.1
+ DREGetNVRAMVar.cold.1
+ DREIsRunningInDeviceRecoveryEnvironment.cold.1
+ DREIsRunningInDeviceRecoveryEnvironment.cold.2
+ DREIsRunningInDeviceRecoveryEnvironment.cold.3
+ DRENVRAMService.sharedNVRAM
+ GCC_except_table0
+ GCC_except_table28
+ GCC_except_table3
+ GCC_except_table34
+ GCC_except_table43
+ GCC_except_table44
+ GCC_except_table8
+ OBJC_IVAR_$_DeviceRecoveryBrain._isExternalBrain
+ OBJC_IVAR_$_DeviceRecoveryEnvironmentWorker._entryDescription
+ OBJC_IVAR_$_DeviceRecoveryEnvironmentWorker._entryReason
+ OBJC_IVAR_$_DeviceRecoveryEnvironmentWorker._isInternalBuild
+ OBJC_IVAR_$_DeviceRecoveryEnvironmentWorker._serviceQueue
+ OBJC_IVAR_$_DeviceRecoveryEnvironmentWorker._timer
+ OBJC_IVAR_$_DeviceRecoveryEnvironmentWorker._timerCount
+ OBJC_IVAR_$_DeviceRecoveryOverrideClient._serviceConnection
+ _DRECopyIORegAsString
+ _DRECopyIORegAsStringWithError
+ _DRECopyIORegEntryWithError
+ _DREDeleteNVRAMProperty
+ _DREGetNVRAMVar
+ _DRENVRAMService
+ _DRESetNVRAMProperty
+ _IORegistryEntryFromPath
+ _IORegistryEntrySetCFProperty
+ _OBJC_CLASS_$_DeviceRecoveryEnvironmentWorker
+ _OBJC_CLASS_$_DeviceRecoveryOverrideClient
+ _OBJC_CLASS_$_NSData
+ _OBJC_METACLASS_$_DeviceRecoveryEnvironmentWorker
+ _OBJC_METACLASS_$_DeviceRecoveryOverrideClient
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ __36-[DeviceRecoveryOverrideClient init]_block_invoke.19
+ __37-[DeviceRecoveryBrain recoverDevice:]_block_invoke.192
+ __37-[DeviceRecoveryBrain scanForIssues:]_block_invoke.160
+ __40-[DeviceRecoveryBrain reclaimFreeSpace:]_block_invoke.164
+ __44-[DeviceRecoveryOverrideClient allOverrides]_block_invoke.34
+ __44-[DeviceRecoveryOverrideClient allOverrides]_block_invoke.cold.1
+ __46-[DeviceRecoveryOverrideClient fetchOverride:]_block_invoke.24
+ __46-[DeviceRecoveryOverrideClient fetchOverride:]_block_invoke.cold.1
+ __50-[DeviceRecoveryOverrideClient removeAllOverrides]_block_invoke.38
+ __50-[DeviceRecoveryOverrideClient removeAllOverrides]_block_invoke.cold.1
+ __50-[DeviceRecoveryOverrideClient setOverride:value:]_block_invoke.28
+ __50-[DeviceRecoveryOverrideClient setOverride:value:]_block_invoke.30
+ __50-[DeviceRecoveryOverrideClient setOverride:value:]_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS_DeviceRecoveryEnvironmentWorker
+ __OBJC_$_INSTANCE_METHODS_DeviceRecoveryEnvironmentWorker
+ __OBJC_$_INSTANCE_METHODS_DeviceRecoveryOverrideClient
+ __OBJC_$_INSTANCE_VARIABLES_DeviceRecoveryEnvironmentWorker
+ __OBJC_$_INSTANCE_VARIABLES_DeviceRecoveryOverrideClient
+ __OBJC_$_PROP_LIST_DeviceRecoveryEnvironmentWorker
+ __OBJC_$_PROP_LIST_DeviceRecoveryOverrideClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DeviceRecoveryOverrideServiceInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DeviceRecoveryOverrideServiceInterface
+ __OBJC_CLASS_RO_$_DeviceRecoveryEnvironmentWorker
+ __OBJC_CLASS_RO_$_DeviceRecoveryOverrideClient
+ __OBJC_LABEL_PROTOCOL_$_DeviceRecoveryOverrideServiceInterface
+ __OBJC_METACLASS_RO_$_DeviceRecoveryEnvironmentWorker
+ __OBJC_METACLASS_RO_$_DeviceRecoveryOverrideClient
+ __OBJC_PROTOCOL_$_DeviceRecoveryOverrideServiceInterface
+ __OBJC_PROTOCOL_REFERENCE_$_DeviceRecoveryOverrideServiceInterface
+ ___36-[DeviceRecoveryOverrideClient init]_block_invoke
+ ___39-[DeviceRecoveryEnvironmentWorker init]_block_invoke
+ ___44-[DeviceRecoveryOverrideClient allOverrides]_block_invoke
+ ___46-[DeviceRecoveryOverrideClient fetchOverride:]_block_invoke
+ ___47+[DeviceRecoveryEnvironmentWorker sharedWorker]_block_invoke
+ ___50-[DeviceRecoveryOverrideClient removeAllOverrides]_block_invoke
+ ___50-[DeviceRecoveryOverrideClient setOverride:value:]_block_invoke
+ ___53-[DeviceRecoveryEnvironmentWorker DREEntryReasonEnum]_block_invoke
+ ___54-[DeviceRecoveryEnvironmentWorker DREEntryDescription]_block_invoke
+ ___57-[DeviceRecoveryEnvironmentWorker CreateCookieAndCleanup]_block_invoke
+ ___62-[DeviceRecoveryEnvironmentWorker setupPopulateDREDescription]_block_invoke
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_e8_32r_e22_v16?0"NSDictionary"8lr32l8
+ ___block_descriptor_40_e8_32r_e8_v16?08lr32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ __block_literal_global.22
+ __block_literal_global.27
+ __block_literal_global.33
+ __block_literal_global.37
+ __block_literal_global.40
+ __dispatch_source_type_timer
+ _dispatch_activate
+ _dispatch_get_global_queue
+ _dispatch_queue_attr_make_initially_inactive
+ _dispatch_queue_create_with_target$V2
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_sync
+ _kIOMainPortDefault
+ _objc_copyWeak
+ _objc_getProperty
+ _objc_initWeak
+ _objc_msgSend$DREEntryDescription
+ _objc_msgSend$DREEntryReasonEnum
+ _objc_msgSend$DREStringFromEntryReason:
+ _objc_msgSend$ERMContentsPresent
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$bytes
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$fetchOverride:
+ _objc_msgSend$fetchOverride:callback:
+ _objc_msgSend$fetchOverrides:
+ _objc_msgSend$filesInDirectory:withPrefix:extension:excludeSymlinks:
+ _objc_msgSend$initExternalBrain:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$isExternalBrain
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$populateDREDescription:
+ _objc_msgSend$populateDREReason
+ _objc_msgSend$recoverTestFiles
+ _objc_msgSend$removeAllOverrides:
+ _objc_msgSend$removeERMContents
+ _objc_msgSend$removeOverride:callback:
+ _objc_msgSend$scanForERMContents
+ _objc_msgSend$scanForTestFiles
+ _objc_msgSend$serviceConnection
+ _objc_msgSend$setOverride:value:
+ _objc_msgSend$setOverride:value:callback:
+ _objc_msgSend$setServiceConnection:
+ _objc_msgSend$setupPopulateDREDescription
+ _objc_msgSend$sharedWorker
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_retain_x28
+ _objc_setProperty_atomic
+ sharedWorker.onceToken
+ sharedWorker.worker
- -[DeviceRecoveryBrain init].cold.1
- -[DeviceRecoveryBrain reclaimFreeSpace:].cold.3
- -[DeviceRecoveryBrain recoverDevice:].cold.4
- -[DeviceRecoveryBrain recoverDevice:].cold.5
- -[DeviceRecoveryBrain recoverDevice:].cold.6
- -[DeviceRecoveryBrain recoverDevice:].cold.7
- -[DeviceRecoveryBrain recoverDevice:].cold.8
- -[DeviceRecoveryBrain recoverDevice:].cold.9
- -[DeviceRecoveryBrain scanForIssues:].cold.2
- -[DeviceRecoveryBrain scanForIssues:].cold.3
- DREIsRunningInDeviceRecoveryEnvironemnt.cold.1
- DREIsRunningInDeviceRecoveryEnvironemnt.cold.2
- DREIsRunningInDeviceRecoveryEnvironemnt.cold.3
- DROverrideDescription.cold.13
- DROverrideDescription.cold.14
- DRValidateOverride.cold.16
- DRValidateOverride.cold.17
- GCC_except_table14
- GCC_except_table22
- GCC_except_table5
- GetServiceConnection.cold.1
- GetServiceConnection.cold.2
- _DREEntryReason
- _DREIsRunningInDeviceRecoveryEnvironemnt
- _DROverrideNameEnvEntryDesc
- _DROverrideNameEnvEntryReason
- _ERMContentsPresent.cold.1
- _ERMContentsPresent.cold.2
- _GetServiceConnection
- __37-[DeviceRecoveryBrain recoverDevice:]_block_invoke.190
- __37-[DeviceRecoveryBrain scanForIssues:]_block_invoke.118
- __40-[DeviceRecoveryBrain reclaimFreeSpace:]_block_invoke.125
- __DREEntryDescription_block_invoke.3
- __DREEntryDescription_block_invoke.cold.1
- __DREEntryReasonEnum_block_invoke.7
- __DREEntryReasonEnum_block_invoke.cold.1
- __ERMContentsPresent
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_DeviceRecoveryEnvironmentServiceInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_DeviceRecoveryEnvironmentServiceInterface
- __OBJC_LABEL_PROTOCOL_$_DeviceRecoveryEnvironmentServiceInterface
- __OBJC_PROTOCOL_$_DeviceRecoveryEnvironmentServiceInterface
- __OBJC_PROTOCOL_REFERENCE_$_DeviceRecoveryEnvironmentServiceInterface
- ___DREEntryDescription_block_invoke
- ___DREEntryReasonEnum_block_invoke
- ___block_descriptor_40_e8_32r_e18_v16?0"NSString"8lr32l8
- ___block_descriptor_40_e8_32r_e8_v12?0i8lr32l8
- __block_literal_global.6
- _objc_msgSend$fetchDREEntryDescription:
- _objc_msgSend$fetchDREEntryReason:
CStrings:
+ " | PanicMedic: %@"
+ "%{public}s: %{public}@ var is not a numeric / data object: %{public}s"
+ "%{public}s: Deleting NVRAM var: %{public}@"
+ "%{public}s: Device Recovery Override Service connection interrupted"
+ "%{public}s: Device Recovery Override Service connection invalidated"
+ "%{public}s: Entry description: %{public}@"
+ "%{public}s: Entry reason: %d"
+ "%{public}s: Error removing override: %{public}@"
+ "%{public}s: Error setting override: %{public}@ -> %{public}@"
+ "%{public}s: Error talking to DeviceRecoveryOverrideService: %{public}@"
+ "%{public}s: Found PanicMedic cookie file but did not find a '%{public}@' entry"
+ "%{public}s: Found internal DeviceRecovery cookie file but did not find a '%{public}@' entry"
+ "%{public}s: No entry reason: %{public}@"
+ "%{public}s: Setting NVRAM var: %{public}@ = %{public}@"
+ "%{public}s: Unable to find an entry description"
+ "%{public}s: Unknown entry reason: %u - Defaulting to: %u (%{public}@)"
+ "%{public}s: entry reason DT entry less than 4 bytes: %{public}@ (%ld bytes)"
+ "%{public}s: error getting contents of directory '%{public}@' - %{public}@"
+ "%{public}s: ioreg property: '%{public}s' = %{public}@"
+ "(dtRecoveryReasonData != nil) && (err == nil)"
+ "-[DeviceRecoveryBrain ERMContentsPresent]"
+ "-[DeviceRecoveryBrain filesInDirectory:withPrefix:extension:excludeSymlinks:]"
+ "-[DeviceRecoveryBrain initExternalBrain:]"
+ "-[DeviceRecoveryBrain recoverTestFiles]"
+ "-[DeviceRecoveryBrain removeERMContents]"
+ "-[DeviceRecoveryBrain scanForERMContents]"
+ "-[DeviceRecoveryBrain scanForTestFiles]"
+ "-[DeviceRecoveryEnvironmentWorker populateDREDescription:]"
+ "-[DeviceRecoveryEnvironmentWorker populateDREReason]"
+ "-[DeviceRecoveryOverrideClient allOverrides]"
+ "-[DeviceRecoveryOverrideClient allOverrides]_block_invoke"
+ "-[DeviceRecoveryOverrideClient fetchOverride:]"
+ "-[DeviceRecoveryOverrideClient fetchOverride:]_block_invoke"
+ "-[DeviceRecoveryOverrideClient init]"
+ "-[DeviceRecoveryOverrideClient init]_block_invoke"
+ "-[DeviceRecoveryOverrideClient removeAllOverrides]"
+ "-[DeviceRecoveryOverrideClient removeAllOverrides]_block_invoke"
+ "-[DeviceRecoveryOverrideClient setOverride:value:]"
+ "-[DeviceRecoveryOverrideClient setOverride:value:]_block_invoke"
+ ".TestDeviceRecovery-modify"
+ ".plist"
+ "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryEnvironmentWorker.m"
+ "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryHelpers.m"
+ "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/DeviceRecovery_Framework/DeviceRecoveryOverrideClient.m"
+ "/private/var/mnt/erm"
+ "/var/db/com.apple.DeviceRecovery.entryInfo"
+ "/var/db/com.apple.DumpPanic.panicLogPathBreadcrumb"
+ "/var/run/com.apple.DumpPanic.finishedThisBoot"
+ "@\"NSObject<OS_dispatch_source>\""
+ "@20@0:8B16"
+ "@44@0:8@16@24@32B40"
+ "CreateCookieAndCleanup"
+ "DRECopyIORegAsStringWithError"
+ "DRECopyIORegEntryWithError"
+ "DREEntryDescription"
+ "DREEntryReasonEnum"
+ "DREGetNVRAMVar"
+ "DREIsRunningInDeviceRecoveryEnvironment"
+ "DRESetNVRAMProperty"
+ "DREStringFromEntryReason:"
+ "DeviceRecoveryEnvironmentWorker"
+ "DeviceRecoveryOverrideClient"
+ "DeviceRecoveryOverrideServiceInterface"
+ "ERMContentsPresent"
+ "IODeviceTree:/chosen"
+ "IODeviceTree:/options"
+ "IONVRAM-DELETE-PROPERTY"
+ "PanicReason"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSNumber\",&,N"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serviceQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_timer"
+ "T@\"NSString\",&,N"
+ "T@\"NSString\",&,N,V_entryDescription"
+ "T@\"NSXPCConnection\",&,V_serviceConnection"
+ "TB,R,N,V_isExternalBrain"
+ "Tc,N,V_timerCount"
+ "Ti,N"
+ "Ti,N,V_entryReason"
+ "[dtRecoveryReasonData isKindOfClass:[NSData class]]"
+ "_entryDescription"
+ "_entryReason"
+ "_isExternalBrain"
+ "_serviceConnection"
+ "_serviceQueue"
+ "_timer"
+ "_timerCount"
+ "addObjectsFromArray:"
+ "allOverrides"
+ "arrayWithObject:"
+ "boot-command"
+ "brainBundlePath"
+ "brainLoadResult"
+ "brainType"
+ "bytes"
+ "c"
+ "c16@0:8"
+ "com.apple.DeviceRecovery.DREnvironmentServiceQueue"
+ "com.apple.DeviceRecoveryOverrideService"
+ "contentsOfDirectoryAtPath:error:"
+ "device-recovery-boot-reason"
+ "directory != nil"
+ "dtRecoveryReasonData.length >= 4"
+ "entryDescription"
+ "entryReason"
+ "fetchOverride:"
+ "fetchOverride:callback:"
+ "fetchOverrides:"
+ "filesInDirectory:withPrefix:extension:excludeSymlinks:"
+ "foundIssues != nil"
+ "initExternalBrain:"
+ "initWithData:encoding:"
+ "isExternalBrain"
+ "issuesScanResult"
+ "networkAvailableResult"
+ "node != IO_OBJECT_NULL"
+ "numberWithUnsignedChar:"
+ "nvramDesc || panicMedicDesc"
+ "nvramService != IO_OBJECT_NULL"
+ "overrideService != nil"
+ "populateDREDescription:"
+ "populateDREReason"
+ "recoverTestFiles"
+ "recovery-reason"
+ "recoveryResult"
+ "removeAllOverrides"
+ "removeAllOverrides:"
+ "removeERMContents"
+ "removeOverride:callback:"
+ "scanForERMContents"
+ "scanForTestFiles"
+ "self.serviceConnection != nil"
+ "serviceConnection"
+ "serviceQueue"
+ "setBrainBundlePath:"
+ "setBrainLoadResult:"
+ "setBrainType:"
+ "setEntryDescription:"
+ "setEntryReason:"
+ "setIssuesScanResult:"
+ "setNetworkAvailableResult:"
+ "setOverride:value:"
+ "setOverride:value:callback:"
+ "setRecoveryResult:"
+ "setServiceConnection:"
+ "setServiceQueue:"
+ "setSystemDataPath:"
+ "setTimer:"
+ "setTimerCount:"
+ "setUpdateVolumePath:"
+ "setUserAuthResult:"
+ "setUserDataPath:"
+ "setupPopulateDREDescription"
+ "sharedWorker"
+ "stringByAppendingFormat:"
+ "systemDataPath"
+ "timer"
+ "timerCount"
+ "unable to coerce io-reg property to a string"
+ "unable to fetch io-reg entry for %s"
+ "unable to fetch property for key: %@"
+ "updateVolumePath"
+ "userAuthResult"
+ "userDataPath"
+ "v16@?0@\"NSDictionary\"8"
+ "v16@?0@8"
+ "v20@0:8c16"
+ "v24@0:8@?<v@?@\"NSDictionary\">16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@>24"
+ "v32@0:8@16@24"
+ "v40@0:8@\"NSString\"16@24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "value != nil"
- "%{public}s: Could not create an NSXPCInterface for: %{public}@"
- "%{public}s: DREEntryReason error: %{public}@"
- "%{public}s: Found test recovery file to modify: %{public}@"
- "%{public}s: Scanning for test recovery file to modify: %{public}@"
- "%{public}s: Scanning for test recovery file to remove: %{public}@"
- "-[DeviceRecoveryBrain init]"
- ".TestDeviceRecovery-modify.plist"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryEnvironment.m"
- "/private/var/erm"
- "DREEntryDescription_block_invoke"
- "DREEntryReasonEnum_block_invoke"
- "DREIsRunningInDeviceRecoveryEnvironemnt"
- "Device Recovery Entry Description: %@"
- "Device Recovery Entry Reason: %@"
- "DeviceRecoveryEnvironmentServiceInterface"
- "EntryReason override has an invalid value: %d (must be between 0 and %d)"
- "EntryReason override is not an NSNumber (%s)"
- "GetServiceConnection"
- "ReclaimFreeSpace not supported in non recovery environment"
- "_ERMContentsPresent"
- "com.apple.DeviceRecoveryEnvironmentService"
- "connection != nil"
- "entryReason < RECOVERY_REASON_SIZE"
- "fetchDREEntryDescription:"
- "fetchDREEntryReason:"
- "overrideEnvEntryDesc"
- "overrideEnvEntryReason"
- "v12@?0i8"
- "v16@?0@\"NSString\"8"
- "v24@0:8@?<v@?@\"NSString\">16"
- "v24@0:8@?<v@?i>16"

```
