## eventkitsyncd

> `/usr/libexec/eventkitsyncd`

```diff

-402.0.0.0.0
-  __TEXT.__text: 0x691b8
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_stubs: 0xb5c0
-  __TEXT.__objc_methlist: 0x6594
-  __TEXT.__cstring: 0x4d53
-  __TEXT.__objc_methname: 0xe1b8
-  __TEXT.__objc_classname: 0x7e0
+403.0.0.0.0
+  __TEXT.__text: 0x69bc0
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_stubs: 0xb740
+  __TEXT.__objc_methlist: 0x665c
+  __TEXT.__cstring: 0x4df1
+  __TEXT.__objc_methname: 0xe3e9
+  __TEXT.__objc_classname: 0x806
   __TEXT.__objc_methtype: 0x2102
   __TEXT.__const: 0x278
-  __TEXT.__oslogstring: 0xa07a
-  __TEXT.__gcc_except_tab: 0x92c
-  __TEXT.__unwind_info: 0x1450
-  __DATA_CONST.__auth_got: 0x688
+  __TEXT.__oslogstring: 0xa199
+  __TEXT.__gcc_except_tab: 0x8bc
+  __TEXT.__unwind_info: 0x1478
+  __DATA_CONST.__auth_got: 0x690
   __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x1548
-  __DATA_CONST.__cfstring: 0x3d60
-  __DATA_CONST.__objc_classlist: 0x2a8
+  __DATA_CONST.__const: 0x1570
+  __DATA_CONST.__cfstring: 0x3e40
+  __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x228
+  __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0xef58
-  __DATA.__objc_selrefs: 0x3780
-  __DATA.__objc_ivar: 0x8bc
-  __DATA.__objc_data: 0x1a90
+  __DATA.__objc_const: 0xf168
+  __DATA.__objc_selrefs: 0x37f0
+  __DATA.__objc_ivar: 0x8cc
+  __DATA.__objc_data: 0x1b30
   __DATA.__data: 0x6c0
   __DATA.__bss: 0x168
   __DATA.__common: 0x1c

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2571
-  Symbols:   338
-  CStrings:  4346
+  Functions: 2593
+  Symbols:   339
+  CStrings:  4385
 
Symbols:
+ _AnalyticsSendEventLazy
CStrings:
+ "== Started EventKitSync-403"
+ "@\"NSDictionary\"8@?0"
+ "Detected drift, watchOnly = %!l(MISSING)d, phoneOnly = %!l(MISSING)d"
+ "Detected duplication, sources = %!l(MISSING)d, calendars = %!l(MISSING)d"
+ "Failed to serialize report data: %!@(MISSING)"
+ "Failed to write data to disk: %!@(MISSING), path = %!@(MISSING)"
+ "NEKDriftResults"
+ "NEKDuplicationResults"
+ "No drift detected on these devices"
+ "No duplication detected on these devices"
+ "T@\"NSArray\",&,N,V_duplicatedCalendars"
+ "T@\"NSArray\",&,N,V_duplicatedSources"
+ "Tq,N,V_occurrencesOnlyOnPhone"
+ "Tq,N,V_occurrencesOnlyOnWatch"
+ "Wrote analytics report to %!@(MISSING)"
+ "_duplicatedCalendars"
+ "_duplicatedSources"
+ "_occurrencesOnlyOnPhone"
+ "_occurrencesOnlyOnWatch"
+ "_reportDriftResultsToAnalytics:"
+ "_reportDuplicationResultsToAnalytics:"
+ "asDictionary"
+ "com.apple.calaccessd"
+ "com.apple.eventkitsync.driftmetrics"
+ "com.apple.eventkitsync.duplicationmetrics"
+ "duplicatedCalendars"
+ "duplicatedSources"
+ "hasDuplicates"
+ "icaluuid"
+ "initWithDuplicatedSources:duplicatedCalendars:"
+ "occurrencesOnlyOnPhone"
+ "occurrencesOnlyOnWatch"
+ "onlyOnPhone"
+ "onlyOnWatch"
+ "setDuplicatedCalendars:"
+ "setDuplicatedSources:"
+ "setOccurrencesOnlyOnPhone:"
+ "setOccurrencesOnlyOnWatch:"
+ "total"
+ "totalDrift"
- "== Started EventKitSync-402"

```
