## PosterUIFoundation

> `/System/iOSSupport/System/Library/PrivateFrameworks/PosterUIFoundation.framework/Versions/A/PosterUIFoundation`

```diff

-350.1.0.0.0
-  __TEXT.__text: 0x93660
-  __TEXT.__objc_methlist: 0xab14
-  __TEXT.__const: 0xdc4
-  __TEXT.__oslogstring: 0x3921
-  __TEXT.__cstring: 0x6593
+355.0.0.0.0
+  __TEXT.__text: 0x932b4
+  __TEXT.__objc_methlist: 0xab04
+  __TEXT.__const: 0xdb4
+  __TEXT.__oslogstring: 0x3861
+  __TEXT.__cstring: 0x6583
   __TEXT.__gcc_except_tab: 0x163c
   __TEXT.__dlopen_cstrs: 0x1c0
-  __TEXT.__swift5_typeref: 0x7f2
-  __TEXT.__constg_swiftt: 0x69c
+  __TEXT.__swift5_typeref: 0x80a
+  __TEXT.__constg_swiftt: 0x708
   __TEXT.__swift5_reflstr: 0x113
   __TEXT.__swift5_fieldmd: 0x194
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x2890
+  __TEXT.__unwind_info: 0x2870
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x58b0
+  __DATA_CONST.__objc_selrefs: 0x58a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x18e0
   __DATA_CONST.__got: 0xf48
   __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x7ea0
-  __AUTH_CONST.__objc_const: 0x1e9a8
+  __AUTH_CONST.__cfstring: 0x7ee0
+  __AUTH_CONST.__objc_const: 0x1e998
   __AUTH_CONST.__objc_dictobj: 0xcf8
   __AUTH_CONST.__objc_intobj: 0xdb0
   __AUTH_CONST.__objc_doubleobj: 0x2b0

   __AUTH_CONST.__auth_got: 0x1010
   __AUTH.__objc_data: 0x2320
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0xbe0
+  __DATA.__objc_ivar: 0xbdc
   __DATA.__data: 0x17a8
   __DATA.__bss: 0x8b0
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4131
-  Symbols:   9679
-  CStrings:  1486
+  Functions: 4134
+  Symbols:   9676
+  CStrings:  1484
 
Symbols:
+ -[PUIPosterSnapshotHostConfigurationDescriptor abortsIfBacklightNotFull]
+ -[PUIPosterSnapshotHostConfigurationDescriptor copyWithAbortsIfBacklightNotFull:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor initWithHostWorkQueue:waitUntilReady:inProcessSnapshot:abortsIfBacklightNotFull:]
+ OBJC_IVAR_$_PUIPosterSnapshotHostConfigurationDescriptor._abortsIfBacklightNotFull
+ _get_witness_table 7SwiftUI4ViewRzAaBRd__r__lqd0__AaBHD3_AaBPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQOyx_qd__Qo_HOTm
+ _objc_msgSend$abortsIfBacklightNotFull
+ _symbolic _____yx_qd__Qo_ 7SwiftUI4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO
+ get_witness_table 7SwiftUI4ViewRzAaBRd__r__lqd0__AaBHD3_AaBPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQOyx_qd__Qo_HO
- -[PUIPosterSnapshotHostConfigurationDescriptor initWithHostWorkQueue:waitUntilReady:inProcessSnapshot:]
- -[PUIPosterSnapshotter _lock_retryStartupLater]
- -[PUIPosterSnapshotter consecutiveStartupFailuresForTesting]
- -[PUIPosterSnapshotter setConsecutiveStartupFailuresForTesting:]
- OBJC_IVAR_$_PUIPosterSnapshotter._lock_consecutiveStartupFailures
- OBJC_IVAR_$_PUIPosterSnapshotter._lock_waitingForRetry
- ___47-[PUIPosterSnapshotter _lock_retryStartupLater]_block_invoke
- _exp2
- _kPFErrorDomain
- _objc_msgSend$_lock_retryStartupLater
- _objc_msgSend$domain
CStrings:
+ "(%{public}@) Booted extension process is invalid (no error) — treating as a boot failure"
+ "(%{public}@) couldn't get assertions; invalidating so the request can be retried on a fresh process"
+ "Snapshotter state error: shouldn't call %s while waiting for extension"
+ "_abortsIfBacklightNotFull"
+ "abortsIfBacklightNotFull"
+ "\xb1"
- "(%{public}@) Booted extension process is invalid (no error) — treating as a startup failure"
- "(%{public}@) Exceeded %lu consecutive mid-snapshot interruptions, giving up"
- "(%{public}@) Exceeded %lu consecutive startup failures, giving up"
- "(%{public}@) Retrying startup in %.1f seconds (attempt %lu/%lu)"
- "(%{public}@) couldn't get assertions, deferring snapshot"
- "-[PUIPosterSnapshotter setConsecutiveStartupFailuresForTesting:]"
- "Snapshotter state error: shouldn't call %s while waiting: for retry? %d; for extension? %d"
- "\xc1"
```
