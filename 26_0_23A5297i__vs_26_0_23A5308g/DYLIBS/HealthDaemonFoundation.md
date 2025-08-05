## HealthDaemonFoundation

> `/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation`

```diff

-6100.0.0.0.0
-  __TEXT.__text: 0x4d8c0
+6105.0.0.0.0
+  __TEXT.__text: 0x4d944
   __TEXT.__auth_stubs: 0x1760
   __TEXT.__objc_methlist: 0x339c
   __TEXT.__const: 0xf02
-  __TEXT.__cstring: 0x4407
+  __TEXT.__cstring: 0x4547
   __TEXT.__oslogstring: 0x2709
-  __TEXT.__gcc_except_tab: 0x2cec
+  __TEXT.__gcc_except_tab: 0x2d00
   __TEXT.__swift5_typeref: 0x352
   __TEXT.__swift5_capture: 0x2c8
   __TEXT.__constg_swiftt: 0x264

   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1d40
+  __TEXT.__unwind_info: 0x1d48
   __TEXT.__eh_frame: 0x450
   __TEXT.__objc_classname: 0x74b
   __TEXT.__objc_methname: 0x7a93
   __TEXT.__objc_methtype: 0x1287
   __TEXT.__objc_stubs: 0x4580
   __DATA_CONST.__got: 0x500
-  __DATA_CONST.__const: 0xe90
+  __DATA_CONST.__const: 0xe68
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 379A1875-4849-3077-B043-9C2D1FAC8859
+  UUID: 076C745F-C6EC-3045-93E4-A5A4A3603AFF
   Functions: 2085
-  Symbols:   5825
-  CStrings:  2926
+  Symbols:   5824
+  CStrings:  2937
 
Symbols:
+ ___63-[HDXPCPeriodicActivity _performCurrentActivityWithCompletion:]_block_invoke.304
+ ___64-[HDSQLiteDatabase performTransactionWithType:error:usingBlock:]_block_invoke.373
+ ___block_literal_global.300
+ ___block_literal_global.306
+ ___block_literal_global.390
+ ___block_literal_global.434
+ ___block_literal_global.518
+ ___block_literal_global.654
+ ___hd_xpc_dispatch_event_block_invoke.319
- ___63-[HDXPCPeriodicActivity _performCurrentActivityWithCompletion:]_block_invoke.301
- ___64-[HDSQLiteDatabase performTransactionWithType:error:usingBlock:]_block_invoke.370
- ___block_descriptor_48_ea8_32s40bs_e13_B24?0^v8^16ls32l8s40l8
- ___block_literal_global.297
- ___block_literal_global.303
- ___block_literal_global.387
- ___block_literal_global.431
- ___block_literal_global.515
- ___block_literal_global.648
- ___hd_xpc_dispatch_event_block_invoke.316
Functions:
~ -[HDXPCProcess hasRequiredEntitlement:error:] : 120 -> 176
~ -[HDSQLiteEntity getValuesForProperties:database:error:handler:] : 1196 -> 1240
~ ___64-[HDSQLiteEntity getValuesForProperties:database:error:handler:]_block_invoke_2 : 72 -> 104
CStrings:
+ "@\"<HDBackgroundTaskCondition>\""
+ "@\"BGNonRepeatingSystemTaskRequest\""
+ "@\"BGSystemTask\""
+ "@\"BGSystemTaskScheduler\""
+ "@\"OS_dispatch_queue\""
+ "@\"OS_os_log\""
+ "@\"_TtC22HealthDaemonFoundation33HDUserNotificationImageDefinition\""
+ "Process %@ (%@) missing required entitlement %@"
- "Missing %@ entitlement."

```
