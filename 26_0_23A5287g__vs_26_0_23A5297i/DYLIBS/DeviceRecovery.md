## DeviceRecovery

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery`

```diff

-85.0.0.0.9
-  __TEXT.__text: 0x1e50c
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x4b8
-  __TEXT.__const: 0x180
-  __TEXT.__gcc_except_tab: 0x2f4
-  __TEXT.__cstring: 0x3960
-  __TEXT.__oslogstring: 0xab4
-  __TEXT.__unwind_info: 0x570
-  __TEXT.__objc_classname: 0xaa
-  __TEXT.__objc_methname: 0xc81
-  __TEXT.__objc_methtype: 0x259
-  __TEXT.__objc_stubs: 0x780
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x4b8
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x18
+88.0.0.0.4
+  __TEXT.__text: 0x1eb94
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_methlist: 0x588
+  __TEXT.__const: 0x188
+  __TEXT.__gcc_except_tab: 0x2d4
+  __TEXT.__cstring: 0x39f6
+  __TEXT.__oslogstring: 0xc6a
+  __TEXT.__unwind_info: 0x580
+  __TEXT.__objc_classname: 0xa2
+  __TEXT.__objc_methname: 0xefe
+  __TEXT.__objc_methtype: 0x28a
+  __TEXT.__objc_stubs: 0x940
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x4a8
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x380
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x2c8
-  __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0xde0
-  __AUTH_CONST.__objc_const: 0x588
+  __DATA_CONST.__objc_selrefs: 0x438
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x18
+  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__const: 0x160
+  __AUTH_CONST.__cfstring: 0xe40
+  __AUTH_CONST.__objc_const: 0x718
   __AUTH_CONST.__objc_intobj: 0x48
-  __DATA.__objc_ivar: 0x3c
-  __DATA.__data: 0x12a
-  __DATA.__bss: 0x40
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x54
+  __DATA.__data: 0xca
+  __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C2F2CF9B-5A52-30B1-B2C3-BF75B7076279
-  Functions: 701
-  Symbols:   1518
-  CStrings:  753
+  UUID: 606AA69B-8302-3886-AB31-2C8A306CE7FA
+  Functions: 720
+  Symbols:   1599
+  CStrings:  805
 
Symbols:
+ +[DeviceRecoveryEnvironmentWorker sharedWorker]
+ +[DeviceRecoveryEnvironmentWorker sharedWorker].cold.1
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
+ GCC_except_table34
+ GCC_except_table43
+ GCC_except_table44
+ _DREIsRunningInDeviceRecoveryEnvironment.cold.1
+ _DREIsRunningInDeviceRecoveryEnvironment.cold.2
+ _DREIsRunningInDeviceRecoveryEnvironment.cold.3
+ _OBJC_CLASS_$_DeviceRecoveryEnvironmentWorker
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_IVAR_$_DeviceRecoveryEnvironmentWorker._entryDescription
+ _OBJC_IVAR_$_DeviceRecoveryEnvironmentWorker._entryReason
+ _OBJC_IVAR_$_DeviceRecoveryEnvironmentWorker._isInternalBuild
+ _OBJC_IVAR_$_DeviceRecoveryEnvironmentWorker._serviceQueue
+ _OBJC_IVAR_$_DeviceRecoveryEnvironmentWorker._timer
+ _OBJC_IVAR_$_DeviceRecoveryEnvironmentWorker._timerCount
+ _OBJC_METACLASS_$_DeviceRecoveryEnvironmentWorker
+ __OBJC_$_CLASS_METHODS_DeviceRecoveryEnvironmentWorker
+ __OBJC_$_INSTANCE_METHODS_DeviceRecoveryEnvironmentWorker
+ __OBJC_$_INSTANCE_VARIABLES_DeviceRecoveryEnvironmentWorker
+ __OBJC_$_PROP_LIST_DeviceRecoveryEnvironmentWorker
+ __OBJC_CLASS_RO_$_DeviceRecoveryEnvironmentWorker
+ __OBJC_METACLASS_RO_$_DeviceRecoveryEnvironmentWorker
+ ___39-[DeviceRecoveryEnvironmentWorker init]_block_invoke
+ ___47+[DeviceRecoveryEnvironmentWorker sharedWorker]_block_invoke
+ ___53-[DeviceRecoveryEnvironmentWorker DREEntryReasonEnum]_block_invoke
+ ___54-[DeviceRecoveryEnvironmentWorker DREEntryDescription]_block_invoke
+ ___57-[DeviceRecoveryEnvironmentWorker CreateCookieAndCleanup]_block_invoke
+ ___62-[DeviceRecoveryEnvironmentWorker setupPopulateDREDescription]_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ __dispatch_source_type_timer
+ _dispatch_activate
+ _dispatch_async
+ _dispatch_get_global_queue
+ _dispatch_queue_attr_make_initially_inactive
+ _dispatch_queue_create_with_target$V2
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_sync
+ _objc_msgSend$DREEntryDescription
+ _objc_msgSend$DREEntryReasonEnum
+ _objc_msgSend$DREStringFromEntryReason:
+ _objc_msgSend$bytes
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$length
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$populateDREDescription:
+ _objc_msgSend$populateDREReason
+ _objc_msgSend$setupPopulateDREDescription
+ _objc_msgSend$sharedWorker
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$writeToFile:atomically:
+ _os_variant_allows_internal_security_policies
+ _sharedWorker.onceToken
+ _sharedWorker.worker
- -[DeviceRecoveryOverrideClient environmentEntryDescription]
- -[DeviceRecoveryOverrideClient environmentEntryReason]
- -[DeviceRecoveryOverrideClient setEnvironmentEntryDescription:]
- -[DeviceRecoveryOverrideClient setEnvironmentEntryReason:]
- GCC_except_table38
- GCC_except_table4
- GCC_except_table47
- GCC_except_table48
- GCC_except_table5
- _DREEntryReason
- _DREIsRunningInDeviceRecoveryEnvironemnt
- _DREIsRunningInDeviceRecoveryEnvironemnt.cold.1
- _DREIsRunningInDeviceRecoveryEnvironemnt.cold.2
- _DREIsRunningInDeviceRecoveryEnvironemnt.cold.3
- _DROverrideDescription.cold.13
- _DROverrideDescription.cold.14
- _DROverrideNameEnvEntryDesc
- _DROverrideNameEnvEntryReason
- _DRValidateOverride.cold.16
- _DRValidateOverride.cold.17
- _GetServiceConnection
- _GetServiceConnection.cold.1
- _GetServiceConnection.cold.2
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_DeviceRecoveryEnvironmentServiceInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_DeviceRecoveryEnvironmentServiceInterface
- __OBJC_LABEL_PROTOCOL_$_DeviceRecoveryEnvironmentServiceInterface
- __OBJC_PROTOCOL_$_DeviceRecoveryEnvironmentServiceInterface
- __OBJC_PROTOCOL_REFERENCE_$_DeviceRecoveryEnvironmentServiceInterface
- ___DREEntryDescription_block_invoke
- ___DREEntryDescription_block_invoke.3
- ___DREEntryDescription_block_invoke.cold.1
- ___DREEntryReasonEnum_block_invoke
- ___DREEntryReasonEnum_block_invoke.7
- ___DREEntryReasonEnum_block_invoke.cold.1
- ___block_descriptor_40_e8_32r_e18_v16?0"NSString"8lr32l8
- ___block_descriptor_40_e8_32r_e8_v12?0i8lr32l8
- ___block_literal_global.6
- _objc_msgSend$fetchDREEntryDescription:
- _objc_msgSend$fetchDREEntryReason:
CStrings:
+ " | PanicMedic: %@"
+ "%{public}s: %{public}@ var is not a numeric / data object: %{public}s"
+ "%{public}s: Entry description: %{public}@"
+ "%{public}s: Entry reason: %d"
+ "%{public}s: Found PanicMedic cookie file but did not find a '%{public}@' entry"
+ "%{public}s: Found internal DeviceRecovery cookie file but did not find a '%{public}@' entry"
+ "%{public}s: No entry reason: %{public}@"
+ "%{public}s: Unable to find an entry description"
+ "%{public}s: Unknown entry reason: %u - Defaulting to: %u (%{public}@)"
+ "%{public}s: entry reason DT entry less than 4 bytes: %{public}@ (%ld bytes)"
+ "(dtRecoveryReasonData != nil) && (err == nil)"
+ "-[DeviceRecoveryEnvironmentWorker populateDREDescription:]"
+ "-[DeviceRecoveryEnvironmentWorker populateDREReason]"
+ "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryEnvironmentWorker.m"
+ "/var/db/com.apple.DeviceRecovery.entryInfo"
+ "/var/db/com.apple.DumpPanic.panicLogPathBreadcrumb"
+ "/var/run/com.apple.DumpPanic.finishedThisBoot"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@20@0:8i16"
+ "CreateCookieAndCleanup"
+ "DREEntryDescription"
+ "DREEntryReasonEnum"
+ "DREIsRunningInDeviceRecoveryEnvironment"
+ "DREStringFromEntryReason:"
+ "DeviceRecoveryEnvironmentWorker"
+ "IODeviceTree:/chosen"
+ "PanicReason"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serviceQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_timer"
+ "T@\"NSString\",&,N,V_entryDescription"
+ "TB,N,V_isInternalBuild"
+ "Tc,N,V_timerCount"
+ "Ti,N,V_entryReason"
+ "[dtRecoveryReasonData isKindOfClass:[NSData class]]"
+ "_entryDescription"
+ "_entryReason"
+ "_isInternalBuild"
+ "_serviceQueue"
+ "_timer"
+ "_timerCount"
+ "boot-command"
+ "bytes"
+ "c"
+ "c16@0:8"
+ "com.apple.DeviceRecovery.DREnvironmentServiceQueue"
+ "defaultManager"
+ "device-recovery-boot-reason"
+ "dictionaryWithContentsOfFile:"
+ "dictionaryWithObjects:forKeys:count:"
+ "dtRecoveryReasonData.length >= 4"
+ "entryDescription"
+ "entryReason"
+ "fileExistsAtPath:"
+ "isInternalBuild"
+ "length"
+ "nvramDesc || panicMedicDesc"
+ "objectForKey:"
+ "populateDREDescription:"
+ "populateDREReason"
+ "recovery-reason"
+ "serviceQueue"
+ "setEntryDescription:"
+ "setEntryReason:"
+ "setIsInternalBuild:"
+ "setServiceQueue:"
+ "setTimer:"
+ "setTimerCount:"
+ "setupPopulateDREDescription"
+ "sharedWorker"
+ "stringByAppendingFormat:"
+ "timer"
+ "timerCount"
+ "v20@0:8c16"
+ "writeToFile:atomically:"
- "%{public}s: Could not create an NSXPCInterface for: %{public}@"
- "%{public}s: DREEntryReason error: %{public}@"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryEnvironment.m"
- "DREEntryDescription_block_invoke"
- "DREEntryReasonEnum_block_invoke"
- "DREIsRunningInDeviceRecoveryEnvironemnt"
- "Device Recovery Entry Description: %@"
- "Device Recovery Entry Reason: %@"
- "DeviceRecoveryEnvironmentServiceInterface"
- "EntryReason override has an invalid value: %d (must be between 0 and %d)"
- "EntryReason override is not an NSNumber (%s)"
- "GetServiceConnection"
- "com.apple.DeviceRecoveryEnvironmentService"
- "connection != nil"
- "entryReason < RECOVERY_REASON_SIZE"
- "environmentEntryDescription"
- "environmentEntryReason"
- "fetchDREEntryDescription:"
- "fetchDREEntryReason:"
- "overrideEnvEntryDesc"
- "overrideEnvEntryReason"
- "setEnvironmentEntryDescription:"
- "setEnvironmentEntryReason:"
- "v12@?0i8"
- "v16@?0@\"NSString\"8"
- "v24@0:8@?<v@?@\"NSString\">16"
- "v24@0:8@?<v@?i>16"

```
