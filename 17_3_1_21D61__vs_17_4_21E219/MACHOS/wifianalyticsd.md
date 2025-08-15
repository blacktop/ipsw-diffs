## wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

-503.2.0.0.0
-  __TEXT.__text: 0x80cc0
-  __TEXT.__auth_stubs: 0xeb0
-  __TEXT.__objc_stubs: 0x7f40
-  __TEXT.__objc_methlist: 0x2c70
+510.16.0.0.0
+  __TEXT.__text: 0x7f8bc
+  __TEXT.__auth_stubs: 0xe90
+  __TEXT.__objc_stubs: 0x7ee0
+  __TEXT.__objc_methlist: 0x2c28
   __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x2f6c
-  __TEXT.__objc_methname: 0xc6eb
-  __TEXT.__cstring: 0x12586
-  __TEXT.__oslogstring: 0x11842
+  __TEXT.__cstring: 0x124ab
+  __TEXT.__gcc_except_tab: 0x2f38
+  __TEXT.__objc_methname: 0xc5d4
+  __TEXT.__oslogstring: 0x117ad
   __TEXT.__objc_classname: 0x300
   __TEXT.__objc_methtype: 0xff8
   __TEXT.__dlopen_cstrs: 0x17a
-  __TEXT.__unwind_info: 0xcb0
+  __TEXT.__unwind_info: 0xc9c
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x770
-  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__auth_got: 0x760
+  __DATA_CONST.__got: 0x170
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x11b0
-  __DATA_CONST.__cfstring: 0xfaa0
+  __DATA_CONST.__const: 0x11e0
+  __DATA_CONST.__cfstring: 0xfa60
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x228
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x1360
   __DATA_CONST.__objc_dictobj: 0xf28
-  __DATA_CONST.__objc_intobj: 0x3d8
+  __DATA_CONST.__objc_intobj: 0x3c0
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_const: 0x51c8
-  __DATA.__objc_selrefs: 0x2958
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x228
-  __DATA.__objc_superrefs: 0xa8
-  __DATA.__objc_ivar: 0x488
+  __DATA.__objc_const: 0x5178
+  __DATA.__objc_selrefs: 0x2940
+  __DATA.__objc_ivar: 0x484
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x368
+  __DATA.__common: 0x40
   __DATA.__bss: 0x170
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: AEAAEE16-05A4-3954-9FC2-CB8217BB1408
-  Functions: 1176
-  Symbols:   342
-  CStrings:  7691
+  UUID: B2EA96AF-CB13-3BC3-919B-4344CCEC6591
+  Functions: 1175
+  Symbols:   339
+  CStrings:  7678
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
+ _os_log_create
- _WAInitLogging
- _WALogCategoryDefault
- _WALogDiagnosticProfileLogHandle
- _WALogWorkReportHandle
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
CStrings:
+ "!."
+ "\"WiFiAnalytics_executables-510.16\""
+ "%{public}s::%d:%@ Process Immediately: read JSON files"
+ "%{public}s::%d:%@ contains %@"
+ "%{public}s::%d:Reading %@"
+ "%{public}s::%d:Registered group %@(%lu) for token %@"
+ "%{public}s::%d:cachedIOReportSample nil - running and caching IOReportCreateSamples"
+ "%{public}s::%d:initWithCoder _cachedChannelsCountPerIORPopulatable %@"
+ "%{public}s::%d:performPruneBasedOnStoreSizeAndSave"
+ "%{public}s::%d:pid %d proc %@ group %@(%ld) not in submitterMap"
+ "Default"
+ "Feb 16 2024 22:32:40"
+ "T@\"NSString\",?,R,C"
+ "WiFiAnalytics_executables-510.16"
+ "WorkReport"
+ "compare:"
+ "diagnosticstream"
+ "groupTypeToString:"
+ "sortedArrayUsingSelector:"
- "!/"
- "\"WiFiAnalytics_executables-503.2\""
- "%02lx"
- "%{public}s::%d:%s: Null coreAnalyticsDict"
- "%{public}s::%d:Failed to convert %@ field %@ with value %@"
- "%{public}s::%d:Failed to convert to hex %@ field %@ with value %@"
- "%{public}s::%d:Invalid data - %@ field %@ with value %@"
- "%{public}s::%d:Null jsonDict"
- "%{public}s::%d:Set cachedAvailabilityStatusPerIORPopulatable %@ for %@"
- "%{public}s::%d:WiFiAnalyticsMessage: %@ processImmediately=%d"
- "%{public}s::%d:initWithCoder cachedAvailabilityStatusPerIORPopulatable %@"
- "%{public}s::%d:pid %d proc %@ group %ld not in submitterMap"
- "-[WAEngine _processWAMessageForCoreAnalytics:]"
- "-[WAEngine _processWAMessageForJSONDump:]"
- "-[WAEngine _submitWiFiAnalyticsMessage:]"
- "-[WAEngine xpcConnection:submitWiFiAnalyticsMessage:andReply:]_block_invoke"
- ":"
- "Dec 20 2023 18:45:44"
- "T@\"NSMutableDictionary\",&,N,V_cachedAvailabilityStatusPerIORPopulatable"
- "WiFiAnalytics_executables-503.2"
- "_cachedAvailabilityStatusPerIORPopulatable"
- "_processWAMessageForCoreAnalytics"
- "_processWAMessageForCoreAnalytics:"
- "_processWAMessageForJSONDump"
- "_processWAMessageForJSONDump:"
- "_submitWiFiAnalyticsMessage:"
- "cachedAvailabilityStatusPerIORPopulatable"
- "setCachedAvailabilityStatusPerIORPopulatable:"
- "xpcConnection:submitWiFiAnalyticsMessage:andReply:"

```
