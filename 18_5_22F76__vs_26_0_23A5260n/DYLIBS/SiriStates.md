## SiriStates

> `/System/Library/PrivateFrameworks/SiriStates.framework/SiriStates`

```diff

-3400.3.1.0.0
-  __TEXT.__text: 0x1ef10
-  __TEXT.__auth_stubs: 0xbf0
+3500.2.1.0.0
+  __TEXT.__text: 0x1e9ac
+  __TEXT.__auth_stubs: 0xc00
   __TEXT.__objc_methlist: 0xcc4
   __TEXT.__const: 0xdb2
   __TEXT.__cstring: 0xbef

   __TEXT.__swift5_types: 0x54
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0xa78
-  __TEXT.__eh_frame: 0x3b8
+  __TEXT.__unwind_info: 0xa80
+  __TEXT.__eh_frame: 0x2e0
   __TEXT.__objc_classname: 0x286
   __TEXT.__objc_methname: 0x827
   __TEXT.__objc_methtype: 0x3e1
   __TEXT.__objc_stubs: 0x3c0
-  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_selrefs: 0x2b0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x600
-  __AUTH_CONST.__const: 0x688
+  __AUTH_CONST.__auth_got: 0x608
+  __AUTH_CONST.__const: 0x778
   __AUTH_CONST.__objc_const: 0x1c00
   __AUTH.__objc_data: 0x1010
   __AUTH.__data: 0x6d0

   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: DA64572A-B85C-34C4-B947-FFA8EF693E91
-  Functions: 1105
-  Symbols:   3327
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 017B85F0-04DA-3FD3-B77A-B5C94EB62879
+  Functions: 1108
+  Symbols:   3340
   CStrings:  352
 
Symbols:
+ _$s10SiriStates11SharedStateC5namedyACSgSSFZTf4nd_n
+ _$s10SiriStates14CallStateProxyC4fromACs7Decoder_p_tKcfcTm
+ _$s10SiriStates5StateC5namedyACSgSSFZTf4nd_n
+ _$s10SiriStates9CallStateC5namedyACSgSSFZTf4nd_n
+ _$sSa6append10contentsOfyqd__n_t7ElementQyd__RszSTRd__lFs5UInt8V_SayAFGTgq5
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss11_StringGutsV23_allocateForDeconstructyXl5owner_SVSi6lengthtyFTv_r
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_SiriStates
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_SiriStates
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_SiriStates
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SiriStates
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SiriStates
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SiriStates
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_SiriStates
+ _objc_release_x28
+ _objc_retain_x23
+ _swift_coroFrameAlloc
- _$s2os21OSAllocatedUnfairLockVAAytRszlE04withD9Uncheckedyqd__qd__yKXEKlF
- _$sSTsE5first5where7ElementQzSgSbADKXE_tKFShy10SiriStates9CallStateCG_Tg504$s10d7States9fG25C5namedyACSgSSFZSbACXEfU_SSTf1cn_nTf4ng_nTm
- _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_SiriStates
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_SiriStates
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_SiriStates
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_SiriStates
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_SiriStates
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_SiriStates
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_SiriStates
- _objc_retain_x21
- _swift_bridgeObjectRelease_n

```
