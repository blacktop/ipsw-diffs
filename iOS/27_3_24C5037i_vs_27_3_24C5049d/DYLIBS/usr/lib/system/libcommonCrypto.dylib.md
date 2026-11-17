## libcommonCrypto.dylib

> `/usr/lib/system/libcommonCrypto.dylib`

```diff

-600041.40.3.0.0
-  __TEXT.__text: 0xb2fc
+600041.60.3.0.0
+  __TEXT.__text: 0xb3b4
   __TEXT.__cstring: 0x2fc
   __TEXT.__const: 0x24c
   __TEXT.__oslogstring: 0x19
-  __TEXT.__unwind_info: 0x558
+  __TEXT.__unwind_info: 0x560
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x740
   __DATA_CONST.__got: 0x0

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  Functions: 357
+  Functions: 358
   Symbols:   699
   CStrings:  52
 
Functions:
~ _CCCryptorUpdate : 816 -> 824
~ _CCECCryptorImportKey : 384 -> 372
~ _CCECCryptorExportKey : 256 -> 276
~ _CCECCryptorSignHash : 128 -> 140
~ _CCECCryptorComputeSharedSecret : 120 -> 140
~ _CCECCryptorTwinDiversifyKey : 272 -> 288
~ _CCECCryptorH2C : 192 -> 200
~ _CCECCryptorBlind : 108 -> 116
~ _CCECCryptorUnblind : 108 -> 116
~ _CCRSACryptorDecrypt : 208 -> 220
~ _CCRSACryptorSign : 216 -> 228
~ _CCECCryptorGetPublicKeyFromPrivateKey : 132 -> 148
+ _CCECCryptorImportKey.cold.1
```
