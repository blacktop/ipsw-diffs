## logd_reporter

> `/usr/libexec/logd_reporter`

```diff

-1612.80.7.0.0
-  __TEXT.__text: 0x3ab8
+1643.100.44.0.0
+  __TEXT.__text: 0x3ae0
   __TEXT.__auth_stubs: 0x300
   __TEXT.__objc_stubs: 0xb00
   __TEXT.__objc_methlist: 0x100
-  __TEXT.__const: 0xa0
-  __TEXT.__objc_methname: 0x91c
-  __TEXT.__oslogstring: 0x526
+  __TEXT.__const: 0xa8
+  __TEXT.__objc_methname: 0x94a
+  __TEXT.__oslogstring: 0x566
   __TEXT.__cstring: 0x46c
   __TEXT.__objc_classname: 0x21
   __TEXT.__objc_methtype: 0xc2
   __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x160
   __DATA_CONST.__cfstring: 0x600
   __DATA_CONST.__objc_classlist: 0x10

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/Versions/A/LoggingSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 676BE067-CBB5-3C2F-8691-2C4CB89394A1
+  UUID: F13BAD7E-3980-3C9D-8BD4-4FD4E18B199C
   Functions: 41
   Symbols:   76
-  CStrings:  279
+  CStrings:  280
 
Functions:
~ sub_10000232c -> sub_10000141c : 752 -> 748
~ sub_100002d30 -> sub_100001e1c : 948 -> 944
~ sub_100003644 -> sub_10000272c : 5172 -> 5212
~ sub_100004ff0 -> sub_100004100 : 748 -> 760
~ sub_1000054e4 -> sub_100004600 : 624 -> 620
CStrings:
+ "No events found in aggregation interval. Not generating report."
+ "aggregationForLogReporterWithStartDate:endDate:predicate:withOptions:catalogCacheSize:dataCacheSize:errorOut:"
- "aggregationForStartDate:endDate:predicate:withOptions:errorOut:"

```
