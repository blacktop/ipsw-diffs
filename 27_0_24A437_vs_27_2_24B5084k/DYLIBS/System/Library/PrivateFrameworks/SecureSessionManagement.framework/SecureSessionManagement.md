## SecureSessionManagement

> `/System/Library/PrivateFrameworks/SecureSessionManagement.framework/SecureSessionManagement`

```diff

-217.11.0.0.0
-  __TEXT.__text: 0x336f8
-  __TEXT.__const: 0x12c8
-  __TEXT.__cstring: 0x2bb
-  __TEXT.__constg_swiftt: 0x7ec
-  __TEXT.__swift5_typeref: 0x6b4
+242.1.0.0.0
+  __TEXT.__text: 0x34a4c
+  __TEXT.__const: 0x13c8
+  __TEXT.__cstring: 0x2fb
+  __TEXT.__constg_swiftt: 0x8c0
+  __TEXT.__swift5_typeref: 0x718
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x4d0
-  __TEXT.__swift5_fieldmd: 0x6c0
-  __TEXT.__swift5_types: 0x60
-  __TEXT.__oslogstring: 0x876
+  __TEXT.__swift5_reflstr: 0x550
+  __TEXT.__swift5_fieldmd: 0x728
+  __TEXT.__swift5_types: 0x64
+  __TEXT.__oslogstring: 0xa96
   __TEXT.__swift5_capture: 0x1ec
-  __TEXT.__swift5_proto: 0x6c
-  __TEXT.__swift_as_entry: 0xa4
-  __TEXT.__swift_as_ret: 0x134
-  __TEXT.__swift_as_cont: 0x1ec
+  __TEXT.__swift5_proto: 0x70
+  __TEXT.__swift_as_entry: 0xbc
+  __TEXT.__swift_as_ret: 0x168
+  __TEXT.__swift_as_cont: 0x23c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_protos: 0x24
+  __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0xc90
-  __TEXT.__eh_frame: 0x26e8
+  __TEXT.__unwind_info: 0xe08
+  __TEXT.__eh_frame: 0x2bf8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xc30
-  __AUTH_CONST.__objc_const: 0x620
-  __AUTH_CONST.__auth_got: 0x690
+  __AUTH_CONST.__const: 0xca8
+  __AUTH_CONST.__objc_const: 0x680
+  __AUTH_CONST.__auth_got: 0x698
   __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0x850
-  __DATA.__data: 0x3d8
+  __AUTH.__data: 0x8f8
+  __DATA.__data: 0x410
   __DATA.__common: 0x78
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 706
-  Symbols:   327
-  CStrings:  51
+  Functions: 767
+  Symbols:   335
+  CStrings:  61
 
Symbols:
+ ___swift_closure_destructor.175Tm
+ _swift_dynamicCast
+ _symbolic $s23SecureSessionManagement17KeyRecordOrderingP
+ _symbolic Sb
+ _symbolic _____ 23SecureSessionManagement08FollowerB7ManagerC22CaptureAlreadyInFlightV
+ _symbolic _____SgyYaYbcSg s6UInt64V
+ _symbolic ______p 23SecureSessionManagement17KeyRecordOrderingP
+ _symbolic ______p 23SecureSessionManagement18KeyRecordProvidingP
+ _symbolic ______pSg 23SecureSessionManagement17KeyRecordOrderingP
- ___swift_closure_destructor.146Tm
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
