## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`

```diff

-3486.40.98.0.0
-  __TEXT.__text: 0x4e7f0c
-  __TEXT.__objc_methlist: 0x2f7dc
+3486.40.112.0.0
+  __TEXT.__text: 0x4e9554
+  __TEXT.__objc_methlist: 0x2f854
   __TEXT.__const: 0x2cc0
   __TEXT.__swift5_typeref: 0x710
   __TEXT.__constg_swiftt: 0x544

   __TEXT.__swift5_types: 0x54
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__cstring: 0x60a1f
+  __TEXT.__cstring: 0x60bab
   __TEXT.__swift5_capture: 0x73c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift_as_cont: 0xd0
-  __TEXT.__oslogstring: 0x16ad3
+  __TEXT.__oslogstring: 0x16b24
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__gcc_except_tab: 0x2d84
+  __TEXT.__gcc_except_tab: 0x2d90
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0xb408
+  __TEXT.__unwind_info: 0xb410
   __TEXT.__eh_frame: 0x16f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9730
+  __DATA_CONST.__const: 0x9740
   __DATA_CONST.__objc_classlist: 0xa78
   __DATA_CONST.__objc_nlclslist: 0x268
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14e18
+  __DATA_CONST.__objc_selrefs: 0x14e70
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb50
-  __DATA_CONST.__objc_arraydata: 0x16dc0
+  __DATA_CONST.__objc_arraydata: 0x16da0
   __DATA_CONST.__got: 0x1b78
   __AUTH_CONST.__const: 0x2a98
-  __AUTH_CONST.__cfstring: 0x784a0
-  __AUTH_CONST.__objc_const: 0x38bb0
+  __AUTH_CONST.__cfstring: 0x78600
+  __AUTH_CONST.__objc_const: 0x38c70
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x6ea0
-  __AUTH_CONST.__objc_arrayobj: 0x3168
+  __AUTH_CONST.__objc_arrayobj: 0x3180
   __AUTH_CONST.__objc_dictobj: 0x5140
-  __AUTH_CONST.__objc_doubleobj: 0x1310
+  __AUTH_CONST.__objc_doubleobj: 0x1320
   __AUTH_CONST.__auth_got: 0x1960
   __AUTH.__objc_data: 0x2c10
   __AUTH.__data: 0x668
-  __DATA.__objc_ivar: 0x1fa4
+  __DATA.__objc_ivar: 0x1fac
   __DATA.__data: 0x10f8
   __DATA.__common: 0x1f8
-  __DATA_DIRTY.__objc_ivar: 0x1388
+  __DATA_DIRTY.__objc_ivar: 0x1390
   __DATA_DIRTY.__objc_data: 0x3f58
   __DATA_DIRTY.__data: 0x728
-  __DATA_DIRTY.__bss: 0x4790
+  __DATA_DIRTY.__bss: 0x4798
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 19892
-  Symbols:   25896
-  CStrings:  19910
+  Functions: 19904
+  Symbols:   25910
+  CStrings:  19924
 
Symbols:
+ +[PLAppTimeService entryAggregateDefinitionDisplayUsage]
+ +[PLUrsaUtilities diagnosticExtensionIDsForProcess:]
+ -[PLAppTimeService aggregateEntryKeyForDisplayUsage]
+ -[PLAppTimeService setAggregateEntryKeyForDisplayUsage:]
+ -[PLAppTimeService updateScreenOnTimeInDBForBundleId:withTime:withDate:forContext:]
+ -[PLBatteryAgent batteryPackCount]
+ -[PLBatteryAgent setBatteryPackCount:]
+ -[PLSleepWakeAgent kaIDMax]
+ -[PLSleepWakeAgent kaIDMin]
+ -[PLSleepWakeAgent setKaIDMax:]
+ -[PLSleepWakeAgent setKaIDMin:]
+ _OBJC_IVAR_$_PLSleepWakeAgent._kaIDMax
+ _OBJC_IVAR_$_PLSleepWakeAgent._kaIDMin
+ ___52+[PLUrsaUtilities diagnosticExtensionIDsForProcess:]_block_invoke
+ ___83-[PLAppTimeService updateScreenOnTimeInDBForBundleId:withTime:withDate:forContext:]_block_invoke
+ ___block_descriptor_57_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8
+ _kPLAppTimeServiceAggregateNameDisplayID
+ _kPLAppTimeServiceAggregateNameDisplayUsage
- +[PLUrsaUtilities shouldCollectCPLDiagnosticExtensionForProcess:]
- GCC_except_table35
- ___65+[PLUrsaUtilities shouldCollectCPLDiagnosticExtensionForProcess:]_block_invoke
- ___block_descriptor_49_e8_32s40s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8
CStrings:
+ "%@: rail is OFF, timestamp=%u, entry=%d"
+ "%@: reached end of buffer, timestamp=%u, entry=%d"
+ "-[PLAppTimeService updateScreenOnTimeInDBForBundleId:withTime:withDate:forContext:]"
+ "AccumSystemEffectiveTotalLoad"
+ "AccumSystemEffectiveTotalLoadCount"
+ "AccumulatedBatteryPower"
+ "BatteryPowerAccumulatorCount"
+ "DisplayID"
+ "DisplayUsage"
+ "For bundleID '%@' and display ID %@, added foreground %@"
+ "Kernel assertions entry: kaID=%llu, duration=%f, count=%zu"
+ "Log Power Delivery Keys to CA, payload=%@"
+ "PLUrsaUtilities: requesting diagnostic extensions %{public}@ for %{public}@"
+ "SystemEffectiveTotalLoad"
+ "adding timeDifference=%f for bundleID=%@ and displayID=%lu"
+ "com.apple.DiagnosticExtensions.IMDiagnosticExtension"
+ "com.apple.power.powerDeliveryKeys"
+ "imagent"
+ "imdpersistence.imdpersistenceagent"
+ "imdpersistenceagent"
+ "rail = %@, payload = %@"
- "%@: manually increment timestamp %u at entry %d"
- "%@: reached the end of buffer at entry %d"
- "%@: reached the end of buffer at entry %d due to timestamp jump %u"
- ",%@"
- "Kernel assertions entry: paID=%llu, duration=%f, count=%zu"
- "PLUrsaUtilities: requesting CPL diagnostic extension for %{public}@"
- "PMUMetricsStatic: rail = %@, payload = %@"
```
