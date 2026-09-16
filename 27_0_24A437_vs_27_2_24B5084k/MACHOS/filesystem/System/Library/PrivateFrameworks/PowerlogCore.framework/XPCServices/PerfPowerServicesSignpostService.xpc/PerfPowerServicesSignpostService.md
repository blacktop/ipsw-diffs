## PerfPowerServicesSignpostService

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostService.xpc/PerfPowerServicesSignpostService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3486.2.4.0.0
-  __TEXT.__text: 0x69ec
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_stubs: 0x1660
-  __TEXT.__objc_methlist: 0x7e8
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0xa4c
-  __TEXT.__objc_methname: 0x166e
-  __TEXT.__oslogstring: 0x5aa
+3486.40.92.0.0
+  __TEXT.__text: 0x7518
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_stubs: 0x1800
+  __TEXT.__objc_methlist: 0x828
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0xb2d
+  __TEXT.__objc_methname: 0x179c
+  __TEXT.__oslogstring: 0x6aa
   __TEXT.__objc_classname: 0xe9
-  __TEXT.__objc_methtype: 0x2db
-  __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__unwind_info: 0x350
-  __DATA_CONST.__const: 0x898
-  __DATA_CONST.__cfstring: 0xf40
+  __TEXT.__objc_methtype: 0x2f9
+  __TEXT.__gcc_except_tab: 0x198
+  __TEXT.__unwind_info: 0x368
+  __DATA_CONST.__const: 0x8c0
+  __DATA_CONST.__cfstring: 0x1080
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x2a8
-  __DATA_CONST.__got: 0xf0
-  __DATA.__objc_const: 0xa58
-  __DATA.__objc_selrefs: 0x890
-  __DATA.__objc_ivar: 0x58
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x100
+  __DATA.__objc_const: 0xa88
+  __DATA.__objc_selrefs: 0x900
+  __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x1f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection
   - /System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport
   - /System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 266
-  Symbols:   141
-  CStrings:  539
+  Functions: 273
+  Symbols:   145
+  CStrings:  573
 
Symbols:
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_CLASS_$_NSMutableSet
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
+ _os_transaction_create
- _objc_retain_x25
CStrings:
+ "\n"
+ "%@%@%@"
+ "'%@::%@' is not registered for PowerLog telemetry; skipping collection summary"
+ "@\"NSCountedSet\""
+ "Collected signposts across %lu categories for time-series task: '%@'"
+ "CollectionSummary"
+ "Count"
+ "DistinctCategoryCount"
+ "ProcessName"
+ "RunDuration"
+ "Sending collection summary to PowerLog: %{public}@"
+ "SignpostServiceMetrics"
+ "T@\"NSCountedSet\",&,V_categoryCounts"
+ "Top #%lu by collected signpost count: '%@' in '%@' (%lu)"
+ "TotalSignpostCount"
+ "__PPSKVPairs__"
+ "_categoryCounts"
+ "_categoryFromTallyKey:"
+ "_processFromTallyKey:"
+ "_tallyCategory:process:"
+ "allObjects"
+ "categoryCounts"
+ "com.apple.perfpowerservices.signpost.collection-summary"
+ "compare:"
+ "countForObject:"
+ "objectAtIndexedSubscript:"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "rangeOfString:"
+ "set"
+ "setCategoryCounts:"
+ "sortedArrayUsingComparator:"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "v32@0:8@16@24"
```
