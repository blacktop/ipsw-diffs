## UsageTracking

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking`

```diff

-391.0.0.0.0
-  __TEXT.__text: 0x298cc
+392.1.0.0.0
+  __TEXT.__text: 0x297b8
   __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_methlist: 0x1618
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x75c
-  __TEXT.__cstring: 0x126b
-  __TEXT.__oslogstring: 0x11cb
+  __TEXT.__cstring: 0x1296
+  __TEXT.__oslogstring: 0x1226
   __TEXT.__unwind_info: 0x6e0
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0x29f

   __TEXT.__objc_methtype: 0xfb0
   __TEXT.__objc_stubs: 0x4240
   __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0xe80
+  __DATA_CONST.__const: 0xea8
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B19A8AD9-1AA3-3BD6-8B28-B0EB27D5BAC3
-  Functions: 591
-  Symbols:   2396
-  CStrings:  1326
+  UUID: 065A91A4-4016-3846-A868-2AABA95EAE1F
+  Functions: 593
+  Symbols:   2403
+  CStrings:  1328
 
Symbols:
+ _OUTLINED_FUNCTION_4
+ ___47-[USUsageAccumulator _stopAllUsageWithEndDate:]_block_invoke.19
+ ___47-[USUsageAccumulator _stopAllUsageWithEndDate:]_block_invoke.cold.1
+ ___55-[USUsageAccumulator _aggregateStartDatesUsingEndDate:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40s_e42_v32?0"USTrustIdentifier"8"NSDate"16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e42_v32?0"USTrustIdentifier"8"NSDate"16^B24ls32l8s40l8s48l8
- ___47-[USUsageAccumulator _stopAllUsageWithEndDate:]_block_invoke.18
- ___block_descriptor_56_e8_32s40s48s_e43_v32?0"USTrustIdentifier"8"NSArray"16^B24ls32l8s40l8s48l8
Functions:
~ -[USApplicationUsageMonitor updateAppDataInContextStore] : 1136 -> 1028
~ -[USApplicationUsageMonitor updateInUseApplications:activeApplications:] : 1456 -> 1620
~ -[USUsageAccumulator _accumulateApplication:timestamp:starting:isUsageTrusted:] : 552 -> 612
~ ___47-[USUsageAccumulator _stopAllUsageWithEndDate:]_block_invoke : 480 -> 188
~ ___55-[USUsageAccumulator _aggregateStartDatesUsingEndDate:]_block_invoke : 492 -> 200
+ _OUTLINED_FUNCTION_4
+ ___55-[USUsageAccumulator _aggregateStartDatesUsingEndDate:]_block_invoke.cold.1
CStrings:
+ "Ignoring start event for %{public}@ at %{public}@ because it already started at %{public}@"
+ "v32@?0@\"USTrustIdentifier\"8@\"NSDate\"16^B24"

```
