## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS`

```diff

-3277.0.0.0.1
-  __TEXT.__text: 0x58b04 sha256:23c7a34c5802c40a67efa123d0823c7d6027c5db857a0a568431337aa27eac64
-  __TEXT.__const: 0x85b0 sha256:04b05e2211708270655837e73356d9202751a583cdee1a2d15d73ad0394c599c
-  __TEXT.__cstring: 0xebf2 sha256:1a1eedaea47f8bb0488d6bc054b5eb41db67c69bbe18ed013bd2d8e3e85e8798
-  __TEXT.__oslogstring: 0x17be sha256:52ea6f42e0512cf2aea9b2cfb473c4be4813a1cfff557b44b07a27128f0c4766
-  __TEXT.__gcc_except_tab: 0x1c sha256:0b561ac68d32676139537d83fc37176be98d039c61e56b0e2cd91e73deff1b13
-  __TEXT.__unwind_info: 0xa78 sha256:7985c5465cdf022e03740c05d0dc118405391847143b562d93d9f7fea3e24e97
+3283.0.0.0.0
+  __TEXT.__text: 0x57d14 sha256:da6f74dec9127f6f765de47444b3a4da7a7a7b481d13f9ff473c53f3f0bbae13
+  __TEXT.__const: 0x8580 sha256:de114997c44bfe59b5fba90211737d4b819e34afc6f215d5f192625d79623403
+  __TEXT.__cstring: 0xebe9 sha256:515eab7d11d222ff39ab96db0efd23155d329bb4a2580b9d6d9678eb2561142f
+  __TEXT.__oslogstring: 0x174b sha256:58f1633d669735330a756ab5f7f7766bdf980fa50fcd0c93e085be1c24008815
+  __TEXT.__gcc_except_tab: 0x1c sha256:8c158865ce05466932301cf10ed35743b6a30374aeb9bdbe468e82bb716a6520
+  __TEXT.__unwind_info: 0xa60 sha256:29feaa64fafb51bb4bfc49526db82af62af5c79e1bafceb3ab0cd013320c9109
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x528 sha256:c8f1da1d9be75d91c666b0e9797ac5eeaa34677663a0701ad5d72a2ac207e660
+  __DATA_CONST.__const: 0x528 sha256:70061c0db1b750e1d0f2861041d3b71ab26847ac0f624979c41939c21a69c5b3
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x400 sha256:8bb0ef51f49675997b32d5415ecf8db3341a10868271bb8fbf602a0fca83bca2
-  __AUTH_CONST.__cfstring: 0x14c0 sha256:8037a60653cda55344ec491028a54d995b56e0e66f78ab799bf594642025b868
-  __AUTH_CONST.__weak_auth_got: 0x8 sha256:9800df19a7526da3ce29aa581c23155a68e314c9a5989a93c8c8b922d7812eaa
-  __AUTH_CONST.__auth_got: 0x6f8 sha256:161e5073a0bdc6cd6a4842aae8e537e13998336cc3545fe0572174b8ae0160cd
-  __DATA.__data: 0xc0 sha256:fbcff768330b94c6f1b4b97ca846352272db9a81d5ff1b43ec27fb345652349d
+  __AUTH_CONST.__const: 0x400 sha256:d14cf2934d1afd51fc9a46d3ba946a9061e5470f6abd62868d7ef8f79d31384c
+  __AUTH_CONST.__cfstring: 0x14e0 sha256:0dc2b42d4c4b5e04f6f034345d2c248bd8fd18a5c7dbb738fa2c2bc724d4d321
+  __AUTH_CONST.__weak_auth_got: 0x8 sha256:3077a0b9bc0c21b7d8fa9e15001a8d3ccb290e5871012b29b5e68ff18b7cdcb0
+  __AUTH_CONST.__auth_got: 0x6c0 sha256:7636c9f8da9a82f9a9fcd804a25795a9c900e1c7e19f7442a7b113c8ccd64eb2
+  __DATA.__data: 0x9c sha256:6a0373f092de28a0441d97e3ff3f5f027550f3e9dac921765dc918e3a727b65b
   __DATA.__bss: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
   __DATA.__common: 0x420 sha256:10e2103ee73921931a7828ebdf325d3a3a64c7a90cc1da5c0ca6fe17b1e3dd78
-  __DATA_DIRTY.__data: 0x148 sha256:06da0db316b09bb402b60af496f3240e85c7c3225ee40ba887a4c20714fd9e78
+  __DATA_DIRTY.__data: 0x148 sha256:6037db87c1f1b3a18ab955c2d3a8a859d7c5db20155b6e962232b7506c1eb861
   __DATA_DIRTY.__common: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: 9260BD09-0E74-3C80-8CB7-BB81600A465B
-  Functions: 956
-  Symbols:   1305
-  CStrings:  1638
+  UUID: 8FAC6C27-6491-3218-970F-8BFDC52270F9
+  Functions: 942
+  Symbols:   1280
+  CStrings:  1635
 
Symbols:
+ __block_descriptor_tmp.223
- APFSContainerEFIEmbed.cold.1
- APFSContainerEFIEmbed.cold.2
- APFSContainerEFIGetVersion.cold.1
- APFSContainerEFIGetVersion.cold.2
- _CCRSACryptorCreateFromData
- _CCRSACryptorRelease
- _CCRSACryptorVerify
- _CC_SHA256_Final
- _CC_SHA256_Init
- _CC_SHA256_Update
- _EfiGetAPFSDriverVersion
- _HashFatBinary
- _HashPeImage
- _HashTrbxFatBinary
- _RSA_VerifySignature
- _VerifyFatBinary
- _VerifyPeCoffSignature
- _VerifyPeImage
- _VerifySignature
- _VerifyTrbxFatBinary
- __block_descriptor_tmp.220
- _efi_js_desc
- _efi_js_desc_funcs
- _kEfiSignAppleCertTypeGuid
- _kEfiSignCertTypeRsa2048Sha256Guid
- _malloc
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRuFugDgq-plnSsvKmFGQuzFQvVyj3HRu0HiAIA/Library/Caches/com.apple.xbs/TemporaryDirectory.cg4QzQ/Sources/apfs_framework/nx/obj.c"
+ "3283"
+ "com.apple.apfs.stream.restore.alloc.estimate.override"
- "%s:%d: buffer length (%u) is less than the minimum (%zu)\n"
- "%s:%d: failed to verify the buffer signature, error: %d\n"
- ".text"
- "/AppleInternal/Library/BuildRoots/4~CQBpugBQk53bvDYSDT-DCeNW8ubOi5ps9yaKaeQ/Library/Caches/com.apple.xbs/TemporaryDirectory.KQJQyx/Sources/apfs_framework/nx/obj.c"
- "3277.0.0.0.1"
- "APFSContainerEFIEmbed"
- "APFSContainerEFIGetVersion"

```
