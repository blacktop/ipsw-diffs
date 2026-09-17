## SecureSessionManagement

> `/System/Library/PrivateFrameworks/SecureSessionManagement.framework/Versions/A/SecureSessionManagement`

```diff

-217.10.0.0.0
-  __TEXT.__text: 0x2f454
-  __TEXT.__const: 0x1068
-  __TEXT.__cstring: 0x21b
-  __TEXT.__swift5_typeref: 0x598
-  __TEXT.__oslogstring: 0x7e2
-  __TEXT.__constg_swiftt: 0x6e4
-  __TEXT.__swift5_reflstr: 0x492
-  __TEXT.__swift5_fieldmd: 0x5e4
+242.0.0.0.0
+  __TEXT.__text: 0x30688
+  __TEXT.__const: 0x1178
+  __TEXT.__cstring: 0x25a
+  __TEXT.__swift5_typeref: 0x5fc
+  __TEXT.__oslogstring: 0xa02
+  __TEXT.__constg_swiftt: 0x7b8
+  __TEXT.__swift5_reflstr: 0x512
+  __TEXT.__swift5_fieldmd: 0x64c
   __TEXT.__swift5_capture: 0x198
-  __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x44
-  __TEXT.__swift_as_entry: 0x8c
-  __TEXT.__swift_as_ret: 0x11c
-  __TEXT.__swift_as_cont: 0x1cc
+  __TEXT.__swift5_proto: 0x60
+  __TEXT.__swift5_types: 0x48
+  __TEXT.__swift_as_entry: 0xa4
+  __TEXT.__swift_as_ret: 0x150
+  __TEXT.__swift_as_cont: 0x21c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_protos: 0x24
+  __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0xb50
-  __TEXT.__eh_frame: 0x23e0
+  __TEXT.__unwind_info: 0xcc8
+  __TEXT.__eh_frame: 0x28f0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x838
-  __AUTH_CONST.__objc_const: 0x530
-  __AUTH_CONST.__auth_got: 0x3f0
+  __AUTH_CONST.__const: 0x8b0
+  __AUTH_CONST.__objc_const: 0x590
+  __AUTH_CONST.__auth_got: 0x3f8
   __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0x790
-  __DATA.__data: 0x330
+  __AUTH.__data: 0x838
+  __DATA.__data: 0x368
   __DATA.__common: 0x50
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 621
-  Symbols:   247
-  CStrings:  45
+  Functions: 685
+  Symbols:   256
+  CStrings:  55
 
Symbols:
+ ___swift_memcpy0_1
+ __swift_closure_destructor.175Tm
+ _swift_dynamicCast
+ _symbolic $s23SecureSessionManagement17KeyRecordOrderingP
+ _symbolic Sb
+ _symbolic _____ 23SecureSessionManagement08FollowerB7ManagerC22CaptureAlreadyInFlightV
+ _symbolic _____SgyYaYbcSg s6UInt64V
+ _symbolic ______p 23SecureSessionManagement17KeyRecordOrderingP
+ _symbolic ______p 23SecureSessionManagement18KeyRecordProvidingP
+ _symbolic ______pSg 23SecureSessionManagement17KeyRecordOrderingP
- __swift_closure_destructor.146Tm
CStrings:
+ "Attempted to remove tag=%llu while in-flight"
+ "Debug tag %llu in use; %s"
+ "Holding rotated-out tag=%llu — capture in flight"
+ "Removed secure session tag=%llu"
+ "commitSecureSessionIndex: failed to advance tag=%llu from=%ld: %@"
+ "nextSecureSessionIndex called on key store that doesn't provide ordering"
+ "nextSecureSessionIndex: a capture is already in flight for tag=%llu"
+ "nextSecureSessionIndex: active tag=%llu has no backing record; clearing stale cache and requesting a new session"
+ "no active session"
+ "overriding active session"
```
