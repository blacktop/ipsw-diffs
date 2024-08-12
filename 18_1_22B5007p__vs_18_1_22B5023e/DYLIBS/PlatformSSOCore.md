## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-417.0.13.0.0
-  __TEXT.__text: 0x997b8
-  __TEXT.__auth_stubs: 0x1c20
-  __TEXT.__objc_methlist: 0x5704
+417.0.15.0.0
+  __TEXT.__text: 0x99ec0
+  __TEXT.__auth_stubs: 0x1c30
+  __TEXT.__objc_methlist: 0x572c
   __TEXT.__const: 0x14a4
-  __TEXT.__cstring: 0xb684
+  __TEXT.__cstring: 0xb674
   __TEXT.__oslogstring: 0x18df
   __TEXT.__gcc_except_tab: 0x68c
   __TEXT.__dlopen_cstrs: 0xa6
-  __TEXT.__swift5_typeref: 0x1a8
+  __TEXT.__swift5_typeref: 0x1a0
   __TEXT.__constg_swiftt: 0x348
   __TEXT.__swift5_reflstr: 0x146
   __TEXT.__swift5_fieldmd: 0x118

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x2078
-  __TEXT.__eh_frame: 0x648
+  __TEXT.__unwind_info: 0x2088
+  __TEXT.__eh_frame: 0x690
   __TEXT.__objc_classname: 0xd48
-  __TEXT.__objc_methname: 0xb74d
-  __TEXT.__objc_methtype: 0x26e9
-  __TEXT.__objc_stubs: 0x6a40
+  __TEXT.__objc_methname: 0xb81a
+  __TEXT.__objc_methtype: 0x28c3
+  __TEXT.__objc_stubs: 0x6a80
   __DATA_CONST.__got: 0x940
-  __DATA_CONST.__const: 0x2400
+  __DATA_CONST.__const: 0x2440
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2750
+  __DATA_CONST.__objc_selrefs: 0x2768
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0xe20
-  __AUTH_CONST.__auth_ptr: 0x1a0
+  __AUTH_CONST.__auth_got: 0xe28
+  __AUTH_CONST.__auth_ptr: 0x198
   __AUTH_CONST.__const: 0x7f0
-  __AUTH_CONST.__cfstring: 0x70c0
-  __AUTH_CONST.__objc_const: 0x14690
+  __AUTH_CONST.__cfstring: 0x70e0
+  __AUTH_CONST.__objc_const: 0x146d0
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3427
-  Symbols:   4521
-  CStrings:  4159
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 3432
+  Symbols:   4537
+  CStrings:  4170
 
Symbols:
+ _CFErrorGetCode
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "@\"NSData\"40@0:8@\"NSData\"16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^@32"
+ "@\"NSString\"48@0:8@\"POMutableJWT\"16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^{__SecCertificate=}32^@40"
+ "@48@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^{__SecCertificate=}32^@40"
+ "@56@0:8@16@24^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32^{__SecCertificate=}40^@48"
+ "Failed to create key data"
+ "Failed to sign embedded SmartCard assertion."
+ "Key error creating signature"
+ "createEncryptionKeyForAlgorithm:"
+ "encodeAndSignJWT:algorithm:key:certificate:error:"
+ "encodeAndSignJWT:key:certificate:error:"
+ "encodeAndSignJWT:signingAlgorithm:key:certificate:error:"
+ "signData:usingKey:error:"
- "Failed to sign embedded SmartCardassertion."

```
