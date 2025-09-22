## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`

```diff

-2964.2.4.0.0
-  __TEXT.__text: 0x521a88
+2964.40.20.502.2
+  __TEXT.__text: 0x522a7c
   __TEXT.__auth_stubs: 0x2da0
-  __TEXT.__objc_methlist: 0x30624
-  __TEXT.__const: 0x1ef8
+  __TEXT.__objc_methlist: 0x3062c
+  __TEXT.__const: 0x1f08
   __TEXT.__swift5_typeref: 0x4ce
   __TEXT.__constg_swiftt: 0x364
   __TEXT.__swift5_reflstr: 0x2be
   __TEXT.__swift5_fieldmd: 0x51c
-  __TEXT.__cstring: 0x853d8
+  __TEXT.__cstring: 0x85571
   __TEXT.__swift5_proto: 0x108
   __TEXT.__swift5_types: 0x34
-  __TEXT.__oslogstring: 0x126ca
+  __TEXT.__oslogstring: 0x12761
   __TEXT.__swift5_capture: 0x4f4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x58
-  __TEXT.__gcc_except_tab: 0x2d50
+  __TEXT.__gcc_except_tab: 0x2d5c
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x8200
+  __TEXT.__unwind_info: 0x8208
   __TEXT.__eh_frame: 0x10f0
   __TEXT.__objc_classname: 0x2872
-  __TEXT.__objc_methname: 0x670f1
+  __TEXT.__objc_methname: 0x6711c
   __TEXT.__objc_methtype: 0x8354
-  __TEXT.__objc_stubs: 0x358a0
+  __TEXT.__objc_stubs: 0x358c0
   __DATA_CONST.__got: 0x1b00
-  __DATA_CONST.__const: 0xa810
+  __DATA_CONST.__const: 0xa7e8
   __DATA_CONST.__objc_classlist: 0xa70
   __DATA_CONST.__objc_nlclslist: 0x258
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14fc8
+  __DATA_CONST.__objc_selrefs: 0x14fd0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb60
-  __DATA_CONST.__objc_arraydata: 0x15f60
+  __DATA_CONST.__objc_arraydata: 0x15f70
   __AUTH_CONST.__auth_got: 0x16e8
-  __AUTH_CONST.__const: 0x2418
-  __AUTH_CONST.__cfstring: 0x75660
+  __AUTH_CONST.__const: 0x2438
+  __AUTH_CONST.__cfstring: 0x75700
   __AUTH_CONST.__objc_const: 0x3ac80
   __AUTH_CONST.__objc_intobj: 0x7608
   __AUTH_CONST.__objc_arrayobj: 0x2d18
-  __AUTH_CONST.__objc_dictobj: 0x4e70
+  __AUTH_CONST.__objc_dictobj: 0x4e98
   __AUTH_CONST.__objc_doubleobj: 0x1430
   __AUTH.__objc_data: 0x2ca8
   __AUTH.__data: 0x760

   __DATA_DIRTY.__objc_ivar: 0x1720
   __DATA_DIRTY.__objc_data: 0x3d38
   __DATA_DIRTY.__data: 0x2a0
-  __DATA_DIRTY.__bss: 0x56f8
+  __DATA_DIRTY.__bss: 0x5700
   __DATA_DIRTY.__common: 0x98
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 42414077-238D-37AE-929A-3D3D3945794D
-  Functions: 20469
-  Symbols:   55222
-  CStrings:  53006
+  UUID: 3E599BA2-1885-3874-A137-9CF7E063D571
+  Functions: 20471
+  Symbols:   55227
+  CStrings:  53038
 
Symbols:
+ -[PLEnergyIssuesService buildVersionChanged]
+ -[PLEnergyIssuesService logPowerExceptionTelemetry:withNotified:withRequestUUID:]
+ GCC_except_table56
+ GCC_except_table59
+ GCC_except_table68
+ GCC_except_table72
+ ___42-[PLEnergyIssuesService addUrsaResponders]_block_invoke.277
+ ___44-[PLEnergyIssuesService buildVersionChanged]_block_invoke
+ ___81-[PLEnergyIssuesService logPowerExceptionTelemetry:withNotified:withRequestUUID:]_block_invoke
+ ___81-[PLEnergyIssuesService logPowerExceptionTelemetry:withNotified:withRequestUUID:]_block_invoke_2
+ ___block_literal_global.238
+ ___block_literal_global.493
+ ___block_literal_global.556
+ _objc_msgSend$buildVersionChanged
+ _objc_msgSend$logPowerExceptionTelemetry:withNotified:withRequestUUID:
+ _objc_msgSend$reportTelemetryEvent:payload:flag:completionHandler:
- -[PLEnergyIssuesService handlePowerExceptionNotification:]
- GCC_except_table24
- GCC_except_table33
- GCC_except_table57
- ___42-[PLEnergyIssuesService addUrsaResponders]_block_invoke.265
- ___58-[PLEnergyIssuesService handlePowerExceptionNotification:]_block_invoke
- ___58-[PLEnergyIssuesService handlePowerExceptionNotification:]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e47_v32?0"NSError"8"NSString"16"NSDictionary"24ls32l8s40l8
- ___block_literal_global.460
- ___block_literal_global.523
- _objc_msgSend$handlePowerExceptionNotification:
- _objc_msgSend$reportTTR:completionHandler:
CStrings:
+ "%.0f"
+ "Checking for update. Current build = %@, last build = %@."
+ "Invalid last build type: %@"
+ "Invalid payload for log-power-exception event"
+ "buildVersionChanged"
+ "failed to log power exception event <%@>: %@"
+ "istkHWBetweenMed"
+ "istkHighPingIntervals"
+ "istkHighPings"
+ "istkLowAfterMedIntervals"
+ "istkLowNoDIPingIntervals"
+ "istkLowNoDIPings"
+ "istkLowNoSUIPingIntervals"
+ "istkLowNoSUIPings"
+ "istkLowPingIntervals"
+ "istkLowPings"
+ "istkMedPingIntervals"
+ "istkMedPings"
+ "kPLBatteryUrsaLastBuildKey"
+ "lastISHighPingHr"
+ "lastISLowNoDIPingHr"
+ "lastISLowNoSUIPingHr"
+ "lastISLowPingHr"
+ "lastISMedHW"
+ "lastISMedPingHr"
+ "loadBuild"
+ "log-power-exception"
+ "logPowerExceptionTelemetry:withNotified:withRequestUUID:"
+ "logged power exception event <%@>"
- "failed to count ttr for %@ <%@>: %@"
- "handlePowerExceptionNotification:"
- "ttr counted for %@ <%@>"

```
