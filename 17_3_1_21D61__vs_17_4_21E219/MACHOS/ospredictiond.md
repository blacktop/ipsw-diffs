## ospredictiond

> `/usr/libexec/ospredictiond`

```diff

-126.0.0.0.0
-  __TEXT.__text: 0x430a8
+131.0.0.0.0
+  __TEXT.__text: 0x43de0
   __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x5e80
-  __TEXT.__objc_methlist: 0x4d60
-  __TEXT.__const: 0x2f8
-  __TEXT.__objc_methname: 0xa0e3
-  __TEXT.__cstring: 0x2ed8
+  __TEXT.__objc_stubs: 0x6000
+  __TEXT.__objc_methlist: 0x4d98
+  __TEXT.__const: 0x300
+  __TEXT.__objc_methname: 0xa2e7
+  __TEXT.__cstring: 0x2f67
   __TEXT.__objc_classname: 0x8c3
-  __TEXT.__oslogstring: 0x3f3a
-  __TEXT.__objc_methtype: 0x12f0
+  __TEXT.__oslogstring: 0x416e
+  __TEXT.__objc_methtype: 0x131b
   __TEXT.__gcc_except_tab: 0x324
-  __TEXT.__unwind_info: 0xc7c
+  __TEXT.__unwind_info: 0xc94
   __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x968
-  __DATA_CONST.__cfstring: 0x3420
+  __DATA_CONST.__const: 0x9a8
+  __DATA_CONST.__cfstring: 0x34a0
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x198
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x498
+  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_intobj: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x9a8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x288
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x93a8
-  __DATA.__objc_selrefs: 0x22e0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x490
-  __DATA.__objc_superrefs: 0x1f0
+  __DATA.__objc_selrefs: 0x2350
   __DATA.__objc_ivar: 0x6f0
   __DATA.__objc_data: 0x16d0
   __DATA.__data: 0x540

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9B3AA6F0-3F2E-3690-B71B-A4555B360387
-  Functions: 1901
-  Symbols:   234
-  CStrings:  3149
+  UUID: BBDB09DA-D159-387A-87E4-AE2FF976E73F
+  Functions: 1904
+  Symbols:   235
+  CStrings:  3186
 
Symbols:
+ _OBJC_CLASS_$_NSMutableString
CStrings:
+ "%02ld: "
+ "%@\n%@\n\n%@\n\n<Oldest lock>\n%@\n<Newest lock>\n%@\nLock count: %lu (need at least %d)\n<Recent Longest Locks>\n%@"
+ "(%ld) %@ is out of time range; returning low confidence prediction"
+ "(%ld) %@ predicts %@"
+ "(%ld) Input query for time %@ is within %f seconds for last query for %@"
+ "(%ld) Logging to Power Log: %@"
+ "(%ld) Model output overridden to %@"
+ "(%ld) Querying model with input date: %@"
+ "(%ld) Restricting entry between %d to %d"
+ "(%ld) Returning Cached output"
+ "(%ld) User has overridden to use time restriction during (%d, %d)"
+ "((endDate >= %@) AND (startDate <= %@))"
+ "*"
+ "@48@0:8q16@24@32@40"
+ "@56@0:8q16@24@32d40@48"
+ "Advancing query date to %.2f seconds from now to accelerate sleep suppression"
+ "Evaluating... Date %@ not worth querying because didn't happen during recent long locks"
+ "Logging sleep suppression query event to PL: %@"
+ "Model queried for sleep suppression: %@"
+ "Reporting sleep suppression query event to CA: %@"
+ "T@\"NSArray\",&,N,V_hourBinsOfLongestLocks"
+ "T@\"NSString\",?,R,C"
+ "Updated hour bins of %ld longest locks ending after %@ & starting before date %@"
+ "_hourBinsOfLongestLocks"
+ "accumulativelyBinKLongestIntervals:endAfter:startBefore:longerThan:fromIntervals:"
+ "appendFormat:"
+ "appendString:"
+ "component:fromDate:"
+ "components:fromDate:toDate:options:"
+ "cpn_%@"
+ "didDateTakePlaceDuringRecentLongLocks:"
+ "hourBinsOfLongestLocks"
+ "longestK:intervalsInArray:"
+ "longestKIntervals:endAfter:startBefore:fromIntervals:"
+ "q24@?0@\"<_OSIIntervalProtocol>\"8@\"<_OSIIntervalProtocol>\"16"
+ "setHourBinsOfLongestLocks:"
+ "sortedArrayUsingComparator:"
+ "string"
+ "subarrayWithRange:"
+ "visualizationFromLongLockHourBinsAtDate:"
- "%@\n%@\n\n%@\n\n<Oldest lock>\n%@\n<Newest lock>\n%@\nLock count: %lu (need at lesat %d)"
- "%@ predicts %@"
- "Advancing query date to %.2f seconds from now to accelerate suppression"
- "Input query for time %@ is within %f seconds for last query for %@"
- "Querying model with input date: %@"
- "Reporting: %@"
- "Returning Cached output"

```
