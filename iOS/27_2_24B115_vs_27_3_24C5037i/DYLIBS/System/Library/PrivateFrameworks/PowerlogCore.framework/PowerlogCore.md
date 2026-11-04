## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-3486.42.1.0.0
-  __TEXT.__text: 0xe5fc0
-  __TEXT.__objc_methlist: 0x9828
-  __TEXT.__const: 0x1c38
-  __TEXT.__cstring: 0x43a4b
-  __TEXT.__oslogstring: 0x8caf
+3486.60.36.0.0
+  __TEXT.__text: 0xe671c
+  __TEXT.__objc_methlist: 0x9848
+  __TEXT.__const: 0x1c88
+  __TEXT.__cstring: 0x43b9d
+  __TEXT.__oslogstring: 0x8d92
   __TEXT.__gcc_except_tab: 0x2a58
-  __TEXT.__unwind_info: 0x44b8
+  __TEXT.__unwind_info: 0x44d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2640
+  __DATA_CONST.__const: 0x2668
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x59f0
+  __DATA_CONST.__objc_selrefs: 0x5a00
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0x46108
+  __DATA_CONST.__objc_arraydata: 0x46248
   __DATA_CONST.__got: 0x7e8
   __AUTH_CONST.__const: 0x2540
-  __AUTH_CONST.__cfstring: 0x6d3a0
+  __AUTH_CONST.__cfstring: 0x6d640
   __AUTH_CONST.__objc_const: 0xaa30
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x4cc8
   __AUTH_CONST.__objc_doubleobj: 0x14d0
   __AUTH_CONST.__objc_arrayobj: 0x1230
-  __AUTH_CONST.__objc_dictobj: 0xfde8
+  __AUTH_CONST.__objc_dictobj: 0xfe60
   __AUTH_CONST.__auth_got: 0xdc0
   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x7d0

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4969
-  Symbols:   7276
-  CStrings:  15319
+  Functions: 4977
+  Symbols:   7284
+  CStrings:  15344
 
Symbols:
+ -[PLCoreOperator enumerateOperatorsWithBlock:]
+ -[PLCoreOperator teardownOperatorDependancies]
+ -[PLOperator teardownOperatorDependancies]
+ -[PLSubmissionFilePLL trialsTaskingTrimCutoffForEndDate:]
+ GCC_except_table103
+ GCC_except_table44
+ GCC_except_table64
+ ___46-[PLCoreOperator teardownOperatorDependancies]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e20_v16?0"PLOperator"8ls32l8s40l8
- -[PLCoreOperator initOperatorDependanciesWithBlock:]
CStrings:
+ "ChunkDurationMins"
+ "Chunks"
+ "CumulativeDayMins"
+ "Failed to convert trials tasking trim window to monotonic time"
+ "FedCapabilityData"
+ "FedExtSrcCapProductID"
+ "FedExtSrcCapVendorID"
+ "FedMaxCurrent"
+ "FedMaxPower"
+ "FedMaxVoltage"
+ "FedWPDebugData"
+ "FedWPPolicyData"
+ "IntervalStartDate"
+ "J510"
+ "J511"
+ "LiveRewindEnabled"
+ "MindPalace"
+ "MindPalaceEnabled"
+ "ProcessingBudgetHrs"
+ "Stop Powerlog Services"
+ "TotalConversationMinutes"
+ "TotalConversationOnBatteryMinutes"
+ "WasRetry"
+ "teardownOperatorDependancies: nil workQueue for %@, skipping"
+ "teardownOperatorDependancies: timed out waiting for %lu operator(s): %{public}@"
```
