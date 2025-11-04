## HealthMenstrualCyclesDaemon

> `/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`

```diff

-6200.2.14.2.5
-  __TEXT.__text: 0x7c0bc
+6200.3.4.0.0
+  __TEXT.__text: 0x7c340
   __TEXT.__auth_stubs: 0x1ff0
   __TEXT.__objc_methlist: 0x33ec
   __TEXT.__const: 0x1890
-  __TEXT.__cstring: 0x4025
-  __TEXT.__oslogstring: 0x63d2
-  __TEXT.__gcc_except_tab: 0xe4c
+  __TEXT.__cstring: 0x4065
+  __TEXT.__oslogstring: 0x6482
+  __TEXT.__gcc_except_tab: 0xe88
   __TEXT.__constg_swiftt: 0x630
   __TEXT.__swift5_typeref: 0xb68
   __TEXT.__swift5_reflstr: 0x74d

   __TEXT.__unwind_info: 0x1680
   __TEXT.__eh_frame: 0xec8
   __TEXT.__objc_classname: 0xbd5
-  __TEXT.__objc_methname: 0x11209
+  __TEXT.__objc_methname: 0x11228
   __TEXT.__objc_methtype: 0x20f9
-  __TEXT.__objc_stubs: 0x95c0
-  __DATA_CONST.__got: 0xc20
+  __TEXT.__objc_stubs: 0x95e0
+  __DATA_CONST.__got: 0xc28
   __DATA_CONST.__const: 0xf28
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c80
+  __DATA_CONST.__objc_selrefs: 0x2c88
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x1010
   __AUTH_CONST.__const: 0xea8
-  __AUTH_CONST.__cfstring: 0x2280
+  __AUTH_CONST.__cfstring: 0x22a0
   __AUTH_CONST.__objc_const: 0x62b8
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7763813D-B6DB-346B-9694-55C696C864CA
-  Functions: 2133
-  Symbols:   5493
-  CStrings:  3311
+  UUID: 3E1A9C57-FDAD-3462-88FD-BAB261CC0256
+  Functions: 2134
+  Symbols:   5497
+  CStrings:  3318
 
Symbols:
+ -[HDMCDaySummaryQueryServer _queue_surfaceDaySummariesWithError:].cold.2
+ _NSLocalizedDescriptionKey
+ _objc_msgSend$errorWithDomain:code:userInfo:
Functions:
~ -[HDMCDaySummaryQueryServer _queue_surfaceDaySummariesWithError:] : 1112 -> 1620
+ -[HDMCDaySummaryQueryServer _queue_surfaceDaySummariesWithError:].cold.2
CStrings:
+ " with error: "
+ "DaySummary Query interrupted during enumeration"
+ "[%{public}@] Query stopped with %@ partial results"
+ "[%{public}@] Query stopping with enumeration error: %{public}@"
+ "[%{public}@] Query suspended, will retry on resume %s%{public}@"
+ "errorWithDomain:code:userInfo:"

```
