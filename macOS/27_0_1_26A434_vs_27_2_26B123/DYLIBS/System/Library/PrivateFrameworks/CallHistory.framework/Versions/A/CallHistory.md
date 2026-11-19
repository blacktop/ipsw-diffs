## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/Versions/A/CallHistory`

```diff

-153.100.1.1.25
-  __TEXT.__text: 0x1bd020
-  __TEXT.__objc_methlist: 0x39e4
-  __TEXT.__const: 0x1e6b0
-  __TEXT.__cstring: 0x4246
-  __TEXT.__oslogstring: 0x6379
-  __TEXT.__gcc_except_tab: 0x7dc
+156.200.131.1.11
+  __TEXT.__text: 0x1be6a4
+  __TEXT.__objc_methlist: 0x3a84
+  __TEXT.__const: 0x1e840
+  __TEXT.__cstring: 0x42d6
+  __TEXT.__oslogstring: 0x63f9
+  __TEXT.__gcc_except_tab: 0x7e0
   __TEXT.__dlopen_cstrs: 0xe3
-  __TEXT.__constg_swiftt: 0x114cc
-  __TEXT.__swift5_typeref: 0x524b
+  __TEXT.__constg_swiftt: 0x114f0
+  __TEXT.__swift5_typeref: 0x5285
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x700e
-  __TEXT.__swift5_fieldmd: 0x59b4
+  __TEXT.__swift5_reflstr: 0x702e
+  __TEXT.__swift5_fieldmd: 0x59e8
   __TEXT.__swift5_assocty: 0x1be0
-  __TEXT.__swift5_proto: 0xe0c
-  __TEXT.__swift5_types: 0x440
+  __TEXT.__swift5_proto: 0xe20
+  __TEXT.__swift5_types: 0x444
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift_as_entry: 0xdc
   __TEXT.__swift_as_ret: 0xc8
   __TEXT.__swift_as_cont: 0x104
-  __TEXT.__swift5_capture: 0x3e0
+  __TEXT.__swift5_capture: 0x3f0
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x6580
-  __TEXT.__eh_frame: 0x78f8
+  __TEXT.__unwind_info: 0x65e0
+  __TEXT.__eh_frame: 0x7980
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x990
+  __DATA_CONST.__const: 0x9b8
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25a8
+  __DATA_CONST.__objc_selrefs: 0x2608
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__got: 0x9e0
-  __AUTH_CONST.__const: 0x5c48
-  __AUTH_CONST.__cfstring: 0x3740
-  __AUTH_CONST.__objc_const: 0x14af8
+  __DATA_CONST.__got: 0x9f0
+  __AUTH_CONST.__const: 0x5d38
+  __AUTH_CONST.__cfstring: 0x3760
+  __AUTH_CONST.__objc_const: 0x14b38
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x11c0
   __AUTH_CONST.__auth_ptr: 0xf70
-  __AUTH.__objc_data: 0x1b88
-  __AUTH.__data: 0x1228
+  __AUTH.__objc_data: 0x90
+  __AUTH.__data: 0x1128
   __DATA.__objc_ivar: 0x2c0
-  __DATA.__data: 0x3e28
-  __DATA.__bss: 0x1cc20
+  __DATA.__data: 0x3e58
+  __DATA.__bss: 0x1cea0
   __DATA.__common: 0xc0
-  __DATA_DIRTY.__objc_data: 0xf78
-  __DATA_DIRTY.__data: 0x14868
+  __DATA_DIRTY.__objc_data: 0x2a70
+  __DATA_DIRTY.__data: 0x14968
   __DATA_DIRTY.__bss: 0x1d70
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12374
-  Symbols:   5936
-  CStrings:  1075
+  Functions: 12405
+  Symbols:   5974
+  CStrings:  1082
 
Symbols:
+ +[CallHistoryDBHandle createWithDBManager:featureFlags:]
+ -[CHFeatureFlags applicationMigrationEnabled]
+ -[CHManager migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]
+ -[CallDBManager initWithDeviceObserver:dbManager:]
+ -[CallHistoryDBClientHandle initWithDBStoreHandle:]
+ -[CallHistoryDBClientHandle initWithDBStoreHandleFactory:]
+ -[CallHistoryDBClientHandle migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]
+ -[CallHistoryDBHandle initWithDBManager:featureFlags:]
+ -[CallHistoryDBHandle migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]
+ -[SyncManager migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]
+ GCC_except_table16
+ GCC_except_table23
+ GCC_except_table29
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table43
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table67
+ GCC_except_table69
+ GCC_except_table73
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table92
+ _CHAppMigrationErrorDomain
+ _CHStartCallIntentForCall
+ _OBJC_CLASS_$_INCallRecord
+ _OBJC_CLASS_$_NSError
+ __58-[CallHistoryDBClientHandle initWithDBStoreHandleFactory:]_block_invoke
+ ___109-[CHManager migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]_block_invoke
+ ___125-[CallHistoryDBClientHandle migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]_block_invoke
+ ___51-[CallHistoryDBClientHandle initWithDBStoreHandle:]_block_invoke
+ ___58-[CallHistoryDBClientHandle initWithDBStoreHandleFactory:]_block_invoke
+ ___block_descriptor_33_e26_"CallHistoryDBHandle"8?0l
+ ___block_descriptor_40_e8_32s_e26_"CallHistoryDBHandle"8?0l
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56b
+ ___destroy_helper_block_e8_32s40s48s56s
+ _associated conformance 11CallHistory0A9PredicateO012WasEmergencyA10CodingKeys33_8B2543BF41DCC502B9138013411C04C9LLOSHAASQ
+ _associated conformance 11CallHistory0A9PredicateO012WasEmergencyA10CodingKeys33_8B2543BF41DCC502B9138013411C04C9LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 11CallHistory0A9PredicateO012WasEmergencyA10CodingKeys33_8B2543BF41DCC502B9138013411C04C9LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _objc_msgSend$applicationMigrationEnabled
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$initWithCallRecordFilter:callRecordToCallBack:audioRoute:destinationType:contacts:callCapability:
+ _objc_msgSend$initWithDBManager:featureFlags:
+ _objc_msgSend$initWithDBStoreHandleFactory:
+ _objc_msgSend$initWithDeviceObserver:dbManager:
+ _objc_msgSend$initWithIdentifier:dateCreated:callRecordType:callCapability:callDuration:unseen:participants:numberOfCalls:isCallerIdBlocked:
+ _objc_msgSend$migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:
+ _objc_msgSend$setPreferredCallProvider:
+ _objc_msgSend$setTTYType:
+ _symbolic _____ 11CallHistory0A9PredicateO012WasEmergencyA10CodingKeys33_8B2543BF41DCC502B9138013411C04C9LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11CallHistory0D9PredicateO012WasEmergencyD10CodingKeys33_8B2543BF41DCC502B9138013411C04C9LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11CallHistory0D9PredicateO012WasEmergencyD10CodingKeys33_8B2543BF41DCC502B9138013411C04C9LLO
- -[CallHistoryDBHandle initWithDBManager:]
- GCC_except_table15
- GCC_except_table22
- GCC_except_table28
- GCC_except_table32
- GCC_except_table34
- GCC_except_table36
- GCC_except_table38
- GCC_except_table56
- GCC_except_table60
- GCC_except_table62
- GCC_except_table64
- GCC_except_table68
- GCC_except_table7
- GCC_except_table70
- GCC_except_table72
- GCC_except_table87
- __34-[CallHistoryDBClientHandle init:]_block_invoke
- ___block_descriptor_41_e8_32s_e5_v8?0l
CStrings:
+ "%ld calls found with service provider %@"
+ "156.200.131.1.11"
+ "156.200.131.1.11~2"
+ "@\"CallHistoryDBHandle\"8@?0"
+ "CallHistoryApplicationMigration"
+ "Migrating data from extension %@ to %@"
+ "Will not perform migration; feature is disabled"
+ "com.apple.CallHistory.application-migration"
+ "wasEmergencyCall == %d"
- "153.100.1.1.25"
- "153.100.1.1.25~16"
```
