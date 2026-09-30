## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-483.0.28.0.0
-  __TEXT.__text: 0x592d4
+483.0.35.0.1
+  __TEXT.__text: 0x59290
   __TEXT.__auth_stubs: 0xe70
   __TEXT.__objc_methlist: 0x32d4
   __TEXT.__const: 0x27a
   __TEXT.__cstring: 0x80b6
-  __TEXT.__oslogstring: 0x2321
+  __TEXT.__oslogstring: 0x22e1
   __TEXT.__gcc_except_tab: 0x1528
   __TEXT.__dlopen_cstrs: 0x110
   __TEXT.__swift5_typeref: 0xc2

   __TEXT.__unwind_info: 0x1530
   __TEXT.__eh_frame: 0x560
   __TEXT.__objc_classname: 0x3d6
-  __TEXT.__objc_methname: 0x9d3c
+  __TEXT.__objc_methname: 0x9d79
   __TEXT.__objc_methtype: 0x151a
-  __TEXT.__objc_stubs: 0x6f20
+  __TEXT.__objc_stubs: 0x6f60
   __DATA_CONST.__got: 0x430
   __DATA_CONST.__const: 0xe88
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2208
+  __DATA_CONST.__objc_selrefs: 0x2218
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0E57FB65-025F-313D-9AC4-CB35F2515D46
+  UUID: 8EA16FFF-E898-3D48-9303-B945BDCADA65
   Functions: 2051
-  Symbols:   7246
+  Symbols:   7248
   CStrings:  3150
 
Symbols:
+ _objc_msgSend$deviceEncryptionKeyWithContext:
+ _objc_msgSend$deviceSigningKeyWithContext:
Functions:
~ -[PORegistrationManager createOrRepairUserConfigurationWithError:] : 1952 -> 2044
~ -[PORegistrationManager finishRegistrationWithStatus:message:] : 728 -> 764
~ -[POExtensionAgentProcess _keyForKeyType:error:] : 1232 -> 1240
~ sub_238ee2cec -> sub_25b372d74 : 2260 -> 2268
~ sub_238ee36a0 -> sub_25b373730 : 1000 -> 788
CStrings:
+ "deviceEncryptionKeyWithContext:"
+ "deviceSigningKeyWithContext:"
- "Checking group names"
- "Checking profile picture"

```
