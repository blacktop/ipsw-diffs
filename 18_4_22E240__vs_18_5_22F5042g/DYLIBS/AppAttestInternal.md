## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-108.2.0.0.0
-  __TEXT.__text: 0x650b8
-  __TEXT.__auth_stubs: 0x1580
-  __TEXT.__objc_methlist: 0x63c
+109.3.0.0.0
+  __TEXT.__text: 0x65b38
+  __TEXT.__auth_stubs: 0x15b0
+  __TEXT.__objc_methlist: 0x68c
   __TEXT.__const: 0x2cd0
-  __TEXT.__cstring: 0x56d8
-  __TEXT.__oslogstring: 0x33ba
-  __TEXT.__gcc_except_tab: 0x730
+  __TEXT.__cstring: 0x5798
+  __TEXT.__oslogstring: 0x348a
+  __TEXT.__gcc_except_tab: 0x784
   __TEXT.__swift5_typeref: 0x9de
   __TEXT.__swift5_reflstr: 0xdf3
   __TEXT.__swift5_assocty: 0x1b0

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_capture: 0x23c
-  __TEXT.__unwind_info: 0xe70
+  __TEXT.__unwind_info: 0xe90
   __TEXT.__eh_frame: 0xba0
-  __TEXT.__objc_classname: 0xd0
-  __TEXT.__objc_methname: 0x11ce
-  __TEXT.__objc_methtype: 0x29b
-  __TEXT.__objc_stubs: 0x1280
-  __DATA_CONST.__got: 0x4b0
+  __TEXT.__objc_classname: 0xe2
+  __TEXT.__objc_methname: 0x1236
+  __TEXT.__objc_methtype: 0x2b6
+  __TEXT.__objc_stubs: 0x1320
+  __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__const: 0x308
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x658
+  __DATA_CONST.__objc_selrefs: 0x680
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0xad0
+  __AUTH_CONST.__auth_got: 0xae8
   __AUTH_CONST.__auth_ptr: 0x4b8
-  __AUTH_CONST.__const: 0x2380
-  __AUTH_CONST.__cfstring: 0x19a0
-  __AUTH_CONST.__objc_const: 0x1668
+  __AUTH_CONST.__const: 0x23a0
+  __AUTH_CONST.__cfstring: 0x1a60
+  __AUTH_CONST.__objc_const: 0x1768
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x9f8
+  __AUTH.__objc_data: 0xa48
   __AUTH.__data: 0x920
-  __DATA.__objc_ivar: 0x34
+  __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x728
   __DATA.__bss: 0x40f0
   __DATA.__common: 0x158
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1278
-  Symbols:   757
-  CStrings:  1059
+  Functions: 1290
+  Symbols:   778
+  CStrings:  1083
 
Symbols:
+ _OBJC_CLASS_$_AppAttestCDHash
+ _OBJC_METACLASS_$_AppAttestCDHash
+ _audit_token_to_pid
+ _csops
+ _fetchCdHash
+ _fetchOptInEntitlements
+ _strerror
CStrings:
+ "\x11"
+ "%25s:%-5d Adding CD Hash data to attestation object CBOR."
+ "%25s:%-5d Failed to fetch CD hash. { error=%s }"
+ "%25s:%-5d Fetched opt-in entitlement values. { values=%@ }"
+ "%25s:%-5d No values for opt-in entitlement found."
+ "/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestUtils.m"
+ "@28@0:8@16C24"
+ "AppAttest (%@-109.3) - %@"
+ "AppAttestCDHash"
+ "C"
+ "T@\"NSData\",&,N,V_cdHash"
+ "TC,N,V_type"
+ "_cdHash"
+ "_type"
+ "addCdHash"
+ "cdHash"
+ "com.apple.DeviceCheckTests"
+ "com.apple.developer.devicecheck.app-attest-optin"
+ "initWithHash:andType:"
+ "setCdHash:"
+ "setType:"
+ "v20@0:8C16"
- "AppAttest (%@-108.2) - %@"

```
