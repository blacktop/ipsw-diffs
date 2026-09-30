## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-199.0.0.0.0
-  __TEXT.__text: 0x1fcf8
+203.0.0.0.0
+  __TEXT.__text: 0x1fea8
   __TEXT.__auth_stubs: 0x1320
   __TEXT.__init_offsets: 0x8
-  __TEXT.__oslogstring: 0x2921
+  __TEXT.__oslogstring: 0x29d1
   __TEXT.__const: 0x12c8
   __TEXT.__cstring: 0x1b94
   __TEXT.__gcc_except_tab: 0x8c0

   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_reflstr: 0x24
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__unwind_info: 0x948
+  __TEXT.__unwind_info: 0x950
   __TEXT.__eh_frame: 0x1d0
   __DATA_CONST.__auth_got: 0x998
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x1390
+  __DATA_CONST.__const: 0x1370
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x150

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8E27AD5F-77F1-355A-9305-7F121EBE1EE9
-  Functions: 642
-  Symbols:   3503
-  CStrings:  458
+  UUID: ACC9DA23-4E42-39B6-B181-4089D678D0E2
+  Functions: 644
+  Symbols:   3505
+  CStrings:  463
 
Symbols:
+ _Z20log_neural_processesP15jetsam_snapshot.cold.1
+ _Z20log_neural_processesP15jetsam_snapshot.cold.2
+ _Z33rearm_exc_resource_implementationi.cold.1
+ __Z20log_neural_processesP15jetsam_snapshot
+ __Z26rearm_exc_resource_for_pidi
+ __Z27rearm_exc_resource_all_pidsv
+ __Z33rearm_exc_resource_implementationi
- _Z18rearm_exc_resourcev.cold.1
- _Z22log_top_neural_processP15jetsam_snapshot.cold.1
- _Z22log_top_neural_processP15jetsam_snapshot.cold.2
- __Z18rearm_exc_resourcev
- __Z22log_top_neural_processP15jetsam_snapshot
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_MemoryMaintenance_Swift
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_MemoryMaintenance_Swift
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_MemoryMaintenance_Swift
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_MemoryMaintenance_Swift
CStrings:
+ "ANE memory usage dropped below threshold after modelmanagerd kill, final memory usage %lld bytes"
+ "Detected process %s with %lld pages of neural memory"
+ "Getting post-assertion neural memory usgae"
+ "Getting pre-assertion neural memory usgae"
+ "OS update has occurred, resetting stored OS version"
+ "Re-arming for pid %d"
+ "pid"
- "ANE memory usage dropped below threshold after modelmanagerd kill"
- "OS update has occured, resetting stored OS version"

```
