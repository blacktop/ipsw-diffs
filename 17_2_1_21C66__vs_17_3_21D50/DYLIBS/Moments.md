## Moments

> `/System/Library/PrivateFrameworks/Moments.framework/Moments`

```diff

-127.0.51.0.0
-  __TEXT.__text: 0x3f008
+127.0.55.0.0
+  __TEXT.__text: 0x3f3f8
   __TEXT.__auth_stubs: 0x660
   __TEXT.__objc_methlist: 0x4a90
   __TEXT.__cstring: 0x897b
-  __TEXT.__oslogstring: 0x33d6
+  __TEXT.__oslogstring: 0x3602
   __TEXT.__const: 0x238
   __TEXT.__gcc_except_tab: 0x1d8
-  __TEXT.__unwind_info: 0xe10
+  __TEXT.__unwind_info: 0xe14
   __TEXT.__objc_classname: 0x6c6
   __TEXT.__objc_methname: 0xae0b
   __TEXT.__objc_methtype: 0x1536

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1805
-  Symbols:   6511
-  CStrings:  3849
+  Functions: 1806
+  Symbols:   6513
+  CStrings:  3855
 
Symbols:
+ +[MOEventBundleMetaDataUtility setMetaDataForTime:startDate:endDate:metaData:].cold.1
CStrings:
+ "build meta, time zone, %@, endDate, %@, localDate, %@"
+ "setMetaDataForTime, startDate, %@, endDate, %@, the timestamps are inverted after snapping."
+ "setMetaDataForTime, startDate, %@, endDate, %@, the timestamps are inverted after time zone shifting."
+ "setMetaDataForTime, startDate, %@, endDate, %@, the timestamps are inverted at the end"
+ "typeOfDayTagFromStartDate, startDate, %@, endDate, %@, timeZone, %@, the timestamps are inverted after time zone shifting."
+ "typeOfDayTagFromStartDate, startDate, %@, endDate, %@, timeZone, %@, the timestamps are inverted."

```
