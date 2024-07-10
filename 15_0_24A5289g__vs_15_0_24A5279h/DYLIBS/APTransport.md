## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/Versions/A/APTransport`

```diff

-800.65.1.0.0
-  __TEXT.__text: 0x6bbc0
-  __TEXT.__auth_stubs: 0x2ab0
+800.61.1.0.0
+  __TEXT.__text: 0x6b4b8
+  __TEXT.__auth_stubs: 0x2a30
   __TEXT.__objc_methlist: 0x83c
-  __TEXT.__cstring: 0x1df92
-  __TEXT.__const: 0x250
+  __TEXT.__cstring: 0x1de39
+  __TEXT.__const: 0x248
   __TEXT.__gcc_except_tab: 0x2b4
-  __TEXT.__unwind_info: 0x10b8
+  __TEXT.__unwind_info: 0x10b0
   __TEXT.__objc_classname: 0x90
-  __TEXT.__objc_methname: 0x23f8
+  __TEXT.__objc_methname: 0x23df
   __TEXT.__objc_methtype: 0x618
-  __TEXT.__objc_stubs: 0x2420
-  __DATA_CONST.__got: 0x320
+  __TEXT.__objc_stubs: 0x2400
+  __DATA_CONST.__got: 0x318
   __DATA_CONST.__const: 0x1570
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x990
+  __DATA_CONST.__objc_selrefs: 0x988
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1568
-  __AUTH_CONST.__const: 0x2b10
-  __AUTH_CONST.__cfstring: 0x4a40
+  __AUTH_CONST.__auth_got: 0x1528
+  __AUTH_CONST.__const: 0x2ae0
+  __AUTH_CONST.__cfstring: 0x4920
   __AUTH_CONST.__objc_const: 0x11d0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1442
-  Symbols:   3330
-  CStrings:  3023
+  Functions: 1438
+  Symbols:   3315
+  CStrings:  3008
 
Symbols:
+ ___block_descriptor_92_e8_32r40r_e15_v24?0r^v8r^v16l
+ ___browser_sendPerDeviceRTCMetrics_block_invoke
+ _browser_sendPerDeviceRTCMetrics
- _CFArraySortValues
- _CFNumberCompare
- _CFStringReplace
- _CUGestaltDeviceClassToString
- _FigCFArrayAppendInt64
- _FigCFArrayGetInt64AtIndex
- _FigCFDictionaryApplyBlock
- _FigCFDictionarySetInt64
- _GestaltProductTypeStringToDeviceClass
- ___block_descriptor_48_e8_32r_e15_v24?0r^v8r^v16l
- ___block_descriptor_72_e8_32r40r_e15_v24?0r^v8r^v16l
- ___browser_batchAndSendDiscoveredDeviceRTCMetrics_block_invoke
- __browser_batchAndSendDiscoveredDeviceRTCMetrics_block_invoke.309
- __browser_batchAndSendDiscoveredDeviceRTCMetrics_block_invoke.324
- _browser_batchAndSendDiscoveredDeviceRTCMetrics
- _browser_createCFStringReplacingSuffix
- _browser_ensureAndGetMutableArrayFromCFDictionary
- _objc_msgSend$stringByAppendingString:
CStrings:
+ "800.61.1"
+ "OSStatus browser_sendPerDeviceRTCMetrics(APBrowserRef)"
+ "OSStatus browser_sendPerDeviceRTCMetrics(APBrowserRef)_block_invoke"
+ "[%!{(MISSING)ptr}] Preparing to send per device RTC metrics for %!l(MISSING)d devices"
+ "[%!{(MISSING)ptr}] Sent RTC metrics for device: %!@(MISSING) %!@(MISSING)"
+ "[%!{(MISSING)ptr}] Sent per device RTC metrics for %!l(MISSING)d devices"
+ "browser_sendPerDeviceRTCMetrics"
+ "browser_sendPerDeviceRTCMetrics_block_invoke"
+ "discoveredDeviceAirPlayVersion"
+ "discoveredDeviceModel"
- "3rdParty"
- "800.65.1"
- "AirPort"
- "Bucket1"
- "Bucket2"
- "Bucket3"
- "Bucket4"
- "Bucket5"
- "MedianMs"
- "Ms"
- "OSStatus browser_batchAndSendDiscoveredDeviceRTCMetrics(APBrowserRef)"
- "OSStatus browser_batchAndSendDiscoveredDeviceRTCMetrics(APBrowserRef)_block_invoke"
- "P95Ms"
- "[%!{(MISSING)ptr}] Preparing to send discovered device RTC metrics for %!l(MISSING)d devices"
- "[%!{(MISSING)ptr}] RTC field | %!@(MISSING) : %!@(MISSING)"
- "[%!{(MISSING)ptr}] Sent discovered device RTC metrics"
- "browser_addRTCMetricValueForDeviceType"
- "browser_addStatisticsToRTCPayload"
- "browser_addStatisticsToRTCPayload_Median"
- "browser_addStatisticsToRTCPayload_P95"
- "browser_batchAndSendDiscoveredDeviceRTCMetrics"
- "browser_batchAndSendDiscoveredDeviceRTCMetrics_block_invoke"
- "browser_createCFStringReplacingSuffix"
- "browser_ensureAndGetMutableArrayFromCFDictionary"
- "browser_incrementRTCMetricDurationBucket"

```
