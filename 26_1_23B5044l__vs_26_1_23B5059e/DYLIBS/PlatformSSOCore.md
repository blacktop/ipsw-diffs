## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-483.40.9.0.0
-  __TEXT.__text: 0x8e3e0
+483.40.13.0.0
+  __TEXT.__text: 0x8e474
   __TEXT.__auth_stubs: 0x1ae0
   __TEXT.__objc_methlist: 0x5f10
   __TEXT.__const: 0x1714
-  __TEXT.__cstring: 0xa4f6
+  __TEXT.__cstring: 0xa516
   __TEXT.__oslogstring: 0x19e7
   __TEXT.__gcc_except_tab: 0x7f8
   __TEXT.__dlopen_cstrs: 0xa6

   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0xd80
   __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x7460
+  __AUTH_CONST.__cfstring: 0x7480
   __AUTH_CONST.__objc_const: 0x141b8
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x3400
+  __AUTH.__objc_data: 0x33b0
   __AUTH.__data: 0x180
   __DATA.__objc_ivar: 0x614
   __DATA.__data: 0x1050
   __DATA.__bss: 0xd31
   __DATA.__common: 0x88
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5BD111C1-66A7-3A59-92FB-6F63C801A143
-  Functions: 3602
-  Symbols:   11955
-  CStrings:  5077
+  UUID: B4D9C875-6A61-33D7-8889-0E6BB1DACD32
+  Functions: 3603
+  Symbols:   11959
+  CStrings:  5079
 
Symbols:
+ ___38-[PODeviceConfiguration initWithData:]_block_invoke.180
+ ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.33
+ ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.33.cold.1
+ ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.60
+ ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.60.cold.1
+ ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.50
+ ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.50.cold.1
+ ___block_literal_global.456
- ___38-[PODeviceConfiguration initWithData:]_block_invoke.174
- ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.54
- ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.54.cold.1
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.38
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.38.cold.1
- ___block_literal_global.450
Functions:
+ sub_25da56b18
~ -[PODeviceConfiguration setAccessTokenTerminalIdentity:] : 500 -> 524
+ ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.33
- sub_25db1e5dc
CStrings:
+ "Missing terminal identity key data"

```
