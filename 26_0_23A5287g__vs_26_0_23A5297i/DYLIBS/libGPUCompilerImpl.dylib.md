## libGPUCompilerImpl.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib`

```diff

-32023.824.0.0.0
-  __TEXT.__text: 0x488a88
-  __TEXT.__auth_stubs: 0x5020
+32023.825.0.0.0
+  __TEXT.__text: 0x488ad8
+  __TEXT.__auth_stubs: 0x50a0
   __TEXT.__init_offsets: 0x4c
   __TEXT.__const: 0x243980
-  __TEXT.__cstring: 0x45c5ed
+  __TEXT.__cstring: 0x45c6ba
   __TEXT.__oslogstring: 0x47
-  __TEXT.__unwind_info: 0x4dd8
+  __TEXT.__unwind_info: 0x4dc8
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0xd7150
-  __AUTH_CONST.__auth_got: 0x2810
+  __AUTH_CONST.__auth_got: 0x2850
   __AUTH_CONST.__const: 0x93a0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libllvm-lmdb.dylib
-  UUID: 979DD32F-7195-3815-B940-B5C6F32D2BDA
-  Functions: 8099
-  Symbols:   3266
-  CStrings:  23174
+  UUID: DA0A3F04-8814-3EC2-9250-B330D1D1A963
+  Functions: 8095
+  Symbols:   3278
+  CStrings:  23182
 
Symbols:
+ _CCECCryptorExportKey
+ _CCECCryptorGeneratePair
+ _CCECCryptorImportKey
+ _CCECCryptorRelease
+ _CCECCryptorSignHash
+ _CCECCryptorVerifyHash
+ _CCECGetKeySize
+ _CCRandomGenerateBytes
+ __ZN10llvm_utils5ECDSA13generateNonceEv
+ __ZN10llvm_utils5ECDSA15generateKeyPairENS0_7KeySizeE
+ __ZN10llvm_utils5ECDSA15verifySignatureEN4llvm8ArrayRefIhEES3_S3_
+ __ZN10llvm_utils5ECDSA17generateSignatureEN4llvm8ArrayRefIhEES3_
CStrings:
+ "26.0.0"
+ "32023.825"
+ "AIR-PACK 32023.825 (metalfe-32023.825)"
+ "cannot export private key"
+ "cannot export public key"
+ "cannot generate key pair"
+ "cannot generate nonce"
+ "cannot import private key"
+ "cannot import public key"
+ "failed to generate signature"
+ "failed to verify signature"
- "19.0.0"
- "32023.824"
- "AIR-PACK 32023.824 (metalfe-32023.824)"

```
