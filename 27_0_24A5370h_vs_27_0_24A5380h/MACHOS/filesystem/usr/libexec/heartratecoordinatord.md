## heartratecoordinatord

> `/usr/libexec/heartratecoordinatord`

```diff

-  __TEXT.__text: 0x25a78
+  __TEXT.__text: 0x26e50
   __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x3d40
+  __TEXT.__objc_stubs: 0x4000
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1944
+  __TEXT.__objc_methlist: 0x1a0c
   __TEXT.__const: 0x369
-  __TEXT.__oslogstring: 0x3a11
-  __TEXT.__cstring: 0x211c
-  __TEXT.__gcc_except_tab: 0x4098
-  __TEXT.__objc_methname: 0x4dda
+  __TEXT.__oslogstring: 0x3a6f
+  __TEXT.__cstring: 0x21b2
+  __TEXT.__gcc_except_tab: 0x4374
+  __TEXT.__objc_methname: 0x51ab
   __TEXT.__objc_classname: 0x38b
-  __TEXT.__objc_methtype: 0x1ba5
-  __TEXT.__unwind_info: 0x1190
-  __DATA_CONST.__const: 0xc18
-  __DATA_CONST.__cfstring: 0x1f80
+  __TEXT.__objc_methtype: 0x1c3e
+  __TEXT.__unwind_info: 0x1248
+  __DATA_CONST.__const: 0xce0
+  __DATA_CONST.__cfstring: 0x2080
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x210
-  __DATA.__objc_const: 0x2b98
-  __DATA.__objc_selrefs: 0x1140
-  __DATA.__objc_ivar: 0x280
+  __DATA_CONST.__got: 0x228
+  __DATA.__objc_const: 0x2c48
+  __DATA.__objc_selrefs: 0x11f8
+  __DATA.__objc_ivar: 0x28c
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x600
   __DATA.__bss: 0xa8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 900
-  Symbols:   206
-  CStrings:  1815
+  Functions: 922
+  Symbols:   209
+  CStrings:  1867
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSSortDescriptor
+ ___NSArray0__struct
CStrings:
+ "@\"NSArray\""
+ "@56@0:8@16@24@32@40@48"
+ "B24@?0@\"HRCHeartRateData\"8@\"NSDictionary\"16"
+ "T@\"HRCHeartRateData\",&,V_mostRecentHighConfidenceHeartRate"
+ "T@\"HRCHeartRateData\",R,N"
+ "T@\"NSArray\",&,V_heartRatesBuffer"
+ "T@\"NSArray\",R,N"
+ "_appendSampleToRollingBuffer:"
+ "_heartRatesBuffer"
+ "_heartRatesWithinWindow"
+ "_recentHighConfidenceHRBuffer"
+ "_reportRecentHighConfidenceHeartRateAnalytics:"
+ "_requestRecentHighConfidenceHeartRates"
+ "age_seconds"
+ "clientDidServeMostRecentHighConfidenceHeartRateWithSourceType:processName:"
+ "clientDidServeRecentHighConfidenceHeartRatesWithCount:sourceType:processName:"
+ "com.apple.hrc.recent_high_confidence_hr.stats"
+ "copy"
+ "dateWithTimeIntervalSinceNow:"
+ "filteredArrayUsingPredicate:"
+ "handleRecentHighConfidenceHeartRates:"
+ "heartRatesBuffer"
+ "initWithDelegate:onQueue:analyticsReporter:"
+ "initWithDelegate:remoteObjectProxy:onQueue:mostRecentHighConfidenceHR:recentHighConfidenceHRBuffer:"
+ "lastObject"
+ "mostRecentHeartRate"
+ "none"
+ "predicateWithBlock:"
+ "process_name"
+ "recent high confidence HRs requested by %{public}@, returning %lu samples, latest: %{public}@"
+ "recentHighConfidenceHeartRates"
+ "recordMostRecentHighConfidenceHeartRateServed:sourceType:processName:"
+ "recordRecentHighConfidenceHeartRatesServed:ageSeconds:sourceType:processName:"
+ "removeObjectAtIndex:"
+ "requestRecentHighConfidenceHeartRates"
+ "request_type"
+ "setHeartRatesBuffer:"
+ "sortDescriptorWithKey:ascending:"
+ "sortedArrayUsingDescriptors:"
+ "source_type"
+ "v24@0:8@\"NSArray\"16"
+ "v32@0:8q16@\"NSString\"24"
+ "v32@0:8q16@24"
+ "v40@0:8d16q24@32"
+ "v40@0:8q16q24@\"NSString\"32"
+ "v40@0:8q16q24@32"
+ "v48@0:8q16d24q32@40"
- "@48@0:8@16@24@32@40"
- "T@\"HRCHeartRateData\",&,N,V_mostRecentHighConfidenceHeartRate"
- "initWithDelegate:remoteObjectProxy:onQueue:mostRecentHighConfidenceHR:"
- "q"

```
