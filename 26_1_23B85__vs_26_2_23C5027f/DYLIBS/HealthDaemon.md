## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6200.2.14.2.5
-  __TEXT.__text: 0x79276c
+6200.3.4.0.0
+  __TEXT.__text: 0x792b08
   __TEXT.__auth_stubs: 0x4820
-  __TEXT.__objc_methlist: 0x43b2c
-  __TEXT.__const: 0x1df7c
+  __TEXT.__objc_methlist: 0x43b44
+  __TEXT.__const: 0x1df6c
   __TEXT.__dlopen_cstrs: 0x15b
   __TEXT.__cstring: 0x7d130
   __TEXT.__constg_swiftt: 0x14dc

   __TEXT.__swift5_proto: 0x100
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x5c4
-  __TEXT.__oslogstring: 0x41dab
+  __TEXT.__oslogstring: 0x41df2
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x60
   __TEXT.__gcc_except_tab: 0x383b4
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1cd30
+  __TEXT.__unwind_info: 0x1cd38
   __TEXT.__eh_frame: 0x2310
   __TEXT.__objc_classname: 0xc5c3
-  __TEXT.__objc_methname: 0x8ecac
+  __TEXT.__objc_methname: 0x8ed05
   __TEXT.__objc_methtype: 0x16b61
-  __TEXT.__objc_stubs: 0x50580
+  __TEXT.__objc_stubs: 0x505c0
   __DATA_CONST.__got: 0x5668
   __DATA_CONST.__const: 0x1d2a0
   __DATA_CONST.__objc_classlist: 0x29d8
   __DATA_CONST.__objc_catlist: 0x4c0
   __DATA_CONST.__objc_protolist: 0x9b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19ef8
+  __DATA_CONST.__objc_selrefs: 0x19f08
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x1d88
   __DATA_CONST.__objc_arraydata: 0x84a0
   __AUTH_CONST.__auth_got: 0x2428
   __AUTH_CONST.__const: 0x10018
   __AUTH_CONST.__cfstring: 0x3d5e0
-  __AUTH_CONST.__objc_const: 0x7d968
+  __AUTH_CONST.__objc_const: 0x7d9a8
   __AUTH_CONST.__objc_arrayobj: 0x1ed8
   __AUTH_CONST.__objc_intobj: 0x3e58
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0xd120
   __AUTH.__data: 0x760
-  __DATA.__objc_ivar: 0x43b4
+  __DATA.__objc_ivar: 0x43b8
   __DATA.__data: 0x81c8
   __DATA.__common: 0x64
   __DATA.__bss: 0x18c0
-  __DATA_DIRTY.__objc_ivar: 0xe84
+  __DATA_DIRTY.__objc_ivar: 0xe88
   __DATA_DIRTY.__objc_data: 0xe2e0
   __DATA_DIRTY.__data: 0x210
   __DATA_DIRTY.__bss: 0x3d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BCEE73CC-0DC4-318F-B330-F2F2C4970DE6
-  Functions: 34766
-  Symbols:   103908
-  CStrings:  44274
+  UUID: C0B89F1F-85BA-3692-9953-F80C92A776BA
+  Functions: 34769
+  Symbols:   103917
+  CStrings:  44278
 
Symbols:
+ -[HDMirroredWorkoutSessionServer cancelDisconnectTimerIfNeeded]
+ -[HDMirroredWorkoutSessionServer disconnectFromRemoteTimerFired]
+ _OBJC_IVAR_$_HDMirroredWorkoutAnalyticsCollector._lock
+ ___67-[HDMirroredWorkoutSessionServer didDisconnectFromRemoteWithError:]_block_invoke_3
+ _objc_msgSend$cancelDisconnectTimerIfNeeded
+ _objc_msgSend$disconnectFromRemoteTimerFired
CStrings:
+ "[mirroring] %{public}@: Client disconnect timer fired. Tearing down..."
+ "_disconnectionTimeoutSource"
+ "cancelDisconnectTimerIfNeeded"
+ "disconnectFromRemoteTimerFired"

```
