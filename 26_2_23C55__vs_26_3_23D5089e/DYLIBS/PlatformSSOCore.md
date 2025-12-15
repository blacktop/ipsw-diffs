## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-483.60.4.0.0
-  __TEXT.__text: 0x8ec0c
-  __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_methlist: 0x5f58
-  __TEXT.__const: 0x17a4
-  __TEXT.__cstring: 0xa528
+483.80.3.0.0
+  __TEXT.__text: 0x8f038
+  __TEXT.__auth_stubs: 0x1af0
+  __TEXT.__objc_methlist: 0x5f90
+  __TEXT.__const: 0x17e4
+  __TEXT.__cstring: 0xa558
   __TEXT.__oslogstring: 0x19e7
   __TEXT.__gcc_except_tab: 0x7f8
   __TEXT.__dlopen_cstrs: 0xa6
-  __TEXT.__swift5_typeref: 0x158
-  __TEXT.__constg_swiftt: 0x348
+  __TEXT.__swift5_typeref: 0x15e
+  __TEXT.__constg_swiftt: 0x374
   __TEXT.__swift5_reflstr: 0x146
-  __TEXT.__swift5_fieldmd: 0x118
+  __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x40
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__unwind_info: 0x1ff8
+  __TEXT.__swift5_types: 0x38
+  __TEXT.__unwind_info: 0x2020
   __TEXT.__eh_frame: 0x5b8
   __TEXT.__objc_classname: 0xd3d
   __TEXT.__objc_methname: 0xcad3

   __TEXT.__objc_stubs: 0x7060
   __DATA_CONST.__got: 0x918
   __DATA_CONST.__const: 0x2448
-  __DATA_CONST.__objc_classlist: 0x4b0
+  __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0xd80
+  __AUTH_CONST.__auth_got: 0xd88
   __AUTH_CONST.__const: 0x780
   __AUTH_CONST.__cfstring: 0x7480
-  __AUTH_CONST.__objc_const: 0x14228
+  __AUTH_CONST.__objc_const: 0x14270
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x33b0
-  __AUTH.__data: 0x180
+  __AUTH.__objc_data: 0x3460
+  __AUTH.__data: 0x1a0
   __DATA.__objc_ivar: 0x61c
   __DATA.__data: 0x1050
   __DATA.__bss: 0xd31

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B5FEF2EC-99DA-3CBF-9C24-533A07188C0A
-  Functions: 3612
-  Symbols:   11978
-  CStrings:  5091
+  UUID: 3F7E571F-A33E-31F7-8F85-DCE1DAD82241
+  Functions: 3620
+  Symbols:   11992
+  CStrings:  5092
 
Symbols:
+ -[POAuthenticationContext dealloc]
+ -[PODeviceConfiguration dealloc]
+ -[POUserConfiguration dealloc]
+ GCC_except_table10
+ _CFRetain
+ _OBJC_CLASS_$__TtC15PlatformSSOCore17POSmartCardHelper
+ _OBJC_METACLASS_$__TtC15PlatformSSOCore17POSmartCardHelper
+ __DATA__TtC15PlatformSSOCore17POSmartCardHelper
+ __INSTANCE_METHODS__TtC15PlatformSSOCore17POSmartCardHelper
+ __METACLASS_DATA__TtC15PlatformSSOCore17POSmartCardHelper
+ ___36-[POUserConfiguration initWithData:]_block_invoke.159
+ ___38-[PODeviceConfiguration initWithData:]_block_invoke.186
+ ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.31
+ ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.31.cold.1
+ ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.35
+ ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.35.cold.1
+ ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.62
+ ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.62.cold.1
+ ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.46
+ ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.46.cold.1
+ ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.52
+ ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.52.cold.1
+ ___block_literal_global.474
+ _kTCIDataLength
+ _symbolic _____ 15PlatformSSOCore17POSmartCardHelperC
- ___36-[POUserConfiguration initWithData:]_block_invoke.157
- ___38-[PODeviceConfiguration initWithData:]_block_invoke.184
- ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.29
- ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.29.cold.1
- ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.33
- ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.33.cold.1
- ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.60
- ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.60.cold.1
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.44
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.44.cold.1
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.50
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.50.cold.1
- ___block_literal_global.472
CStrings:
+ "_TtC15PlatformSSOCore17POSmartCardHelper"

```
