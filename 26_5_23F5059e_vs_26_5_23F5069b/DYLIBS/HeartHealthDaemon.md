## HeartHealthDaemon

> `/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon`

```diff

-6200.6.7.0.0
-  __TEXT.__text: 0x6d0e4
-  __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_methlist: 0x5054
+6200.6.8.2.1
+  __TEXT.__text: 0x6d290
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_methlist: 0x5064
   __TEXT.__const: 0x34a
   __TEXT.__gcc_except_tab: 0xd84
   __TEXT.__cstring: 0x55c2
-  __TEXT.__oslogstring: 0xc26b
+  __TEXT.__oslogstring: 0xc2e0
   __TEXT.__ustring: 0x86
   __TEXT.__swift5_typeref: 0x47
   __TEXT.__swift5_capture: 0x20

   __TEXT.__unwind_info: 0x17b0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x1bf3
-  __TEXT.__objc_methname: 0x12878
+  __TEXT.__objc_methname: 0x128b9
   __TEXT.__objc_methtype: 0x3a63
-  __TEXT.__objc_stubs: 0xb400
+  __TEXT.__objc_stubs: 0xb420
   __DATA_CONST.__got: 0xec8
   __DATA_CONST.__const: 0x1980
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3580
+  __DATA_CONST.__objc_selrefs: 0x3588
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x510
-  __AUTH_CONST.__auth_got: 0x850
+  __AUTH_CONST.__auth_got: 0x858
   __AUTH_CONST.__const: 0x5f0
   __AUTH_CONST.__cfstring: 0x4620
   __AUTH_CONST.__objc_const: 0x9b38

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0981E7DF-DDD4-3BEC-AE4C-AD52678C5D6E
-  Functions: 2104
-  Symbols:   8336
-  CStrings:  4597
+  UUID: F9CA5DBA-D329-3F14-B582-14A0C498258D
+  Functions: 2105
+  Symbols:   8340
+  CStrings:  4599
 
Symbols:
+ -[HDHRHypertensionNotificationsAnalysisScheduler _recalculateNextAnalysisWindowStartDateIfInFuture:referenceDate:]
+ _fmod
+ _objc_msgSend$_recalculateNextAnalysisWindowStartDateIfInFuture:referenceDate:
Functions:
+ -[HDHRHypertensionNotificationsAnalysisScheduler _recalculateNextAnalysisWindowStartDateIfInFuture:referenceDate:]
~ -[HDHRHypertensionNotificationsAnalysisScheduler _queue_performAnalysisIfNeededWithDatabaseTransactionContext:completion:] : 1744 -> 1796
CStrings:
+ "[%{public}@] Last analysis date(%@) is in the future, discarding it and recalculating new analysis window start date"
+ "_recalculateNextAnalysisWindowStartDateIfInFuture:referenceDate:"

```
