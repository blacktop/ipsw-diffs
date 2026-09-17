## PerfPowerServicesSignpostService

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/Versions/A/XPCServices/PerfPowerServicesSignpostService.xpc/Contents/MacOS/PerfPowerServicesSignpostService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3486.1.2.0.0
-  __TEXT.__text: 0x6f88
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_stubs: 0x1640
-  __TEXT.__objc_methlist: 0x7e8
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x9ba
-  __TEXT.__objc_methname: 0x1658
-  __TEXT.__oslogstring: 0x565
+3486.40.92.0.0
+  __TEXT.__text: 0x7b94
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_stubs: 0x17e0
+  __TEXT.__objc_methlist: 0x828
+  __TEXT.__const: 0xd8
+  __TEXT.__cstring: 0xa9b
+  __TEXT.__objc_methname: 0x1786
+  __TEXT.__oslogstring: 0x665
   __TEXT.__objc_classname: 0xe9
-  __TEXT.__objc_methtype: 0x2db
-  __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__unwind_info: 0x368
-  __DATA_CONST.__const: 0x8d0
-  __DATA_CONST.__cfstring: 0xe80
+  __TEXT.__objc_methtype: 0x2f9
+  __TEXT.__gcc_except_tab: 0x198
+  __TEXT.__unwind_info: 0x378
+  __DATA_CONST.__const: 0x900
+  __DATA_CONST.__cfstring: 0xfc0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x1e0
-  __DATA_CONST.__got: 0xd8
-  __DATA.__objc_const: 0xa58
-  __DATA.__objc_selrefs: 0x888
-  __DATA.__objc_ivar: 0x58
+  __DATA_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0xe0
+  __DATA.__objc_const: 0xa88
+  __DATA.__objc_selrefs: 0x8f8
+  __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x1e8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/Versions/A/DiagnosticExtensions
+  - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/SignpostCollection.framework/Versions/A/SignpostCollection
   - /System/Library/PrivateFrameworks/SignpostSupport.framework/Versions/A/SignpostSupport
   - /System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/Versions/A/WorkflowResponsiveness

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 273
-  Symbols:   113
-  CStrings:  530
+  Functions: 280
+  Symbols:   117
+  CStrings:  564
 
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
+ _os_transaction_create
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
