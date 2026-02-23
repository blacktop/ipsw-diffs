## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-1041.19.2.0.0
-  __TEXT.__text: 0xd5698
+1041.24.0.0.0
+  __TEXT.__text: 0xd584c
   __TEXT.__auth_stubs: 0x1730
-  __TEXT.__objc_methlist: 0x12188
+  __TEXT.__objc_methlist: 0x12190
   __TEXT.__const: 0x6e8
-  __TEXT.__cstring: 0x1fe26
-  __TEXT.__oslogstring: 0x480a
-  __TEXT.__gcc_except_tab: 0x1990
+  __TEXT.__cstring: 0x1fe2e
+  __TEXT.__oslogstring: 0x4862
+  __TEXT.__gcc_except_tab: 0x1920
   __TEXT.__dlopen_cstrs: 0xf3
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0x2f40
+  __TEXT.__unwind_info: 0x2f50
   __TEXT.__objc_classname: 0x149e
-  __TEXT.__objc_methname: 0x34689
+  __TEXT.__objc_methname: 0x3466a
   __TEXT.__objc_methtype: 0x3f90
-  __TEXT.__objc_stubs: 0x19e40
+  __TEXT.__objc_stubs: 0x19e20
   __DATA_CONST.__got: 0xaa8
-  __DATA_CONST.__const: 0x2378
+  __DATA_CONST.__const: 0x23c8
   __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa020
+  __DATA_CONST.__objc_selrefs: 0xa018
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x480
   __DATA_CONST.__objc_arraydata: 0xb50
   __AUTH_CONST.__auth_got: 0xbb0
   __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x1ad00
-  __AUTH_CONST.__objc_const: 0x229f0
+  __AUTH_CONST.__cfstring: 0x1ac80
+  __AUTH_CONST.__objc_const: 0x229d0
   __AUTH_CONST.__objc_intobj: 0x19e0
   __AUTH_CONST.__objc_arrayobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x7a8
-  __DATA.__objc_ivar: 0x2268
+  __DATA.__objc_ivar: 0x2264
   __DATA.__data: 0x1c20
   __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x2e68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C7FD2622-55E4-349B-9AAE-3F6DA27FA00C
-  Functions: 6497
-  Symbols:   21220
-  CStrings:  17526
+  UUID: 9EF7C9FB-559B-3472-85C6-1FA4BAA80082
+  Functions: 6501
+  Symbols:   21229
+  CStrings:  17517
 
Symbols:
+ -[WiFiScanStatistics reset]
+ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_9
+ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_9.cold.1
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.373
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.cold.2
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_descriptor_68_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_literal_global.197
- _OBJC_IVAR_$_SiriNWConnection._dateToDisable
- ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.369
- ___block_literal_global.218
- _objc_msgSend$dateFromString:
Functions:
~ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke : 5124 -> 5236
~ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_2 : 1796 -> 888
+ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_9
~ -[SiriNWConnection initWithQueueAndCompletion:reason:callback:] : 268 -> 144
~ -[SiriNWConnection runSiriProbeWithDepth:trafficClass:] : 788 -> 728
~ ___55-[SiriNWConnection runSiriProbeWithDepth:trafficClass:]_block_invoke : 232 -> 268
~ -[SiriNWConnection .cxx_destruct] : 248 -> 236
+ -[WiFiScanStatistics reset]
~ -[WiFiScanStatistics postDailyScanMetricsToCA] : 276 -> 288
~ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.cold.1 : 176 -> 164
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.cold.2
+ ___43-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_9.cold.1
CStrings:
+ "%s: ERROR - result is nil from WFMeasure, aborting link test evaluation"
+ "%s: Failed to create URL for probe depth %ld"
+ "%s: strongSelf is nil in completion block, object was deallocated"
+ "-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_9"
+ "/AppleInternal/Library/BuildRoots/4~CJRgugAKKq0kCjKnNgmx_Gop-soc5PorRhXJ_nA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/Library/Caches/com.apple.xbs/B24B13FD-8261-45BE-9B29-84E488A9F616/TemporaryDirectory.lq08lo/Sources/WiFiPolicy/frameworks/Sources/TrafficEngineering/WFTrafficEngManager.m"
+ "Failed to create URL for Siri probe"
+ "performLinkTestFor: ERROR - result is nil from WFMeasure, aborting link test evaluation"
- "%s: Probing has been disabled from running after %@, it is now %@"
- "%s: Probing ok to run before %@, it is now %@"
- "-[WFMeasure dispatchSiriTest:trafficClass:]_block_invoke_2"
- "/AppleInternal/Library/BuildRoots/4~CIsLugB0o5r6EMNbd3-qJ3HQjkUA2rYwTNuyDaY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/Library/Caches/com.apple.xbs/C53332FF-2975-4DD8-8EE5-3E472D547CC9/TemporaryDirectory.iTB48e/Sources/WiFiPolicy/frameworks/Sources/TrafficEngineering/WFTrafficEngManager.m"
- "2024-01-30"
- "2025-12-30"
- "Past Siri Probe Functional Date"
- "_dateToDisable"
- "com.apple.wifi.policy"
- "dateFromString:"
- "expireddate"
- "yyyy-MM-dd"

```
