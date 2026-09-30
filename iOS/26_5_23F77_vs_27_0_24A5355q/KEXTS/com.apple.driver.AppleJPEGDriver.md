## com.apple.driver.AppleJPEGDriver

> `com.apple.driver.AppleJPEGDriver`

```diff

-7.7.9.0.0
-  __TEXT.__cstring: 0x29cd sha256:0f0a0acaec3ea22215111fcc21b9ca36a64dac88fc1a69ac47a2751e9b1db8eb
-  __TEXT.__os_log: 0x92e9 sha256:4fa7d52a30abde498467a613bcfb746d14bee0349f2192beb6089c43a535b386
-  __TEXT.__const: 0x391c sha256:3e9b67dfcc441625e112b794db16cfeb92591ebd703878f90af7ea55dd4d19f1
-  __TEXT_EXEC.__text: 0x2a954 sha256:8a4603371f349b9ca16c6cce5fb2b794f0a66be3aecfa27dc78507ed86d83ea9
+8.1.0.0.0
+  __TEXT.__cstring: 0x2a63 sha256:56c68ca882674ecb78ebb210826faa31001c0af275ec15871901f78d4c58d291
+  __TEXT.__os_log: 0x9690 sha256:936e840860e7305333335ab02d56313946787cd384be08c4e7c287c46ef02083
+  __TEXT.__const: 0x39ec sha256:4903dd0768017efb415da247119a1fa337315e6ff13c5ecaf630d73297095a31
+  __TEXT_EXEC.__text: 0x2b1c4 sha256:c8fca2e326af52c36bd8de89afa54e7311aab9b7bd51346e143d7816f2dbb3d0
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2208 sha256:3953f9f749f571347833f94d02b105140e483b9ce5b9771a1ace65e6811497ba
-  __DATA.__common: 0x3a8 sha256:4db2fd521b198ad08a6602141c428d23a3bf232e85fd7de8418439e89d7b3d04
+  __DATA.__data: 0x2208 sha256:b1f1e4266b018c3d0bb98191797eb9ac190f4e7981c938c693eaabf33d2bfa03
+  __DATA.__common: 0x3d0 sha256:116d7399ce18e417bb9d1586091987731f6b78e79edbea12349960da3b9269b2
   __DATA.__bss: 0x1 sha256:6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d
-  __DATA_CONST.__auth_got: 0x340 sha256:45e214943a83daef53e01b9bb6fffe8512a943bbada10eaee1b53163ca2313fa
-  __DATA_CONST.__got: 0x98 sha256:3367b2b168d930ef880b8ce6d6731b9580d2890c6d9e0432f6171ec8192d0b0a
-  __DATA_CONST.__mod_init_func: 0xb8 sha256:aac03a5f42bf2a8b072f568012b0796ffcf7ca1a7379a2f638f566e38f572a32
-  __DATA_CONST.__mod_term_func: 0xb8 sha256:521ada2235ef91c17f6c2edbe758901eb169dbc626058b5d6e1f367c6728f357
-  __DATA_CONST.__const: 0x49c0 sha256:a56ec82d4e4f75d9617e7b565e13799a74655843d42b4912ae8d0b667a26eaa6
-  __DATA_CONST.__kalloc_type: 0xd40 sha256:8a6945c1f3b282d0c3d6773689103bacad4a9e5e93d8e3f6f6e4fdfa96248854
-  UUID: F81EE642-1044-32C3-8E6A-90775AD49663
-  Functions: 1713
+  __DATA_CONST.__mod_init_func: 0xc0 sha256:a15c74996f87ed016e69674ea0763192b39583b4791aa1fb7c8f2fb5316c40e1
+  __DATA_CONST.__mod_term_func: 0xc0 sha256:cc81321f774575a5119c2b1f1fc59ba4d7217e68f82f73c8851a165d32670c88
+  __DATA_CONST.__const: 0x4b50 sha256:6d3c2fdd5af981192f8dbb91c77ef9f7b8001b9dd450ce913df62c5cb0049af2
+  __DATA_CONST.__kalloc_type: 0xd80 sha256:a6002256612a25d5fe5f201c470f5a18e7e74ff6e2b02e8d22e884c9cb69fdb4
+  __DATA_CONST.__auth_got: 0x340 sha256:51330d4f85a4e041c8208b787c5e128488282deae095166d3b3d6c4cac865ee1
+  __DATA_CONST.__got: 0x98 sha256:a533e928bf65bdc10699fadc287d1c4e8f0f720f37dc43512400d4bcd46ab1a5
+  UUID: 912D5564-4888-3203-A159-D59E3B5943AC
+  Functions: 1741
   Symbols:   0
-  CStrings:  512
+  CStrings:  520
 
CStrings:
+ "112221111111112212112222222221222222222222222222222222222222222222222222222222222222222111122222112222222222222222222222222222222222222222222222212222222121112222222222222"
+ "12211111111111112221122222222122222"
+ "AppleJPEGDriver: %s(): Error! enablePsdService(en = %u, ltr = %u, dieId = %u) returned %d\n"
+ "AppleJPEGDriver: * %s mPendingSetup is NULL - ignoring interrupt"
+ "AppleJPEGDriver: ** %s: crop offset out of bounds: offsetX %u * MCUWidth %u = %u > pixelsX %u, offsetY %u * MCUHeight %u = %u > pixelsY %u\n"
+ "AppleJPEGDriver: ** %s: elementCount %u exceeds partialDecodeFakeHeader capacity %zu, rejecting\n"
+ "AppleJPEGDriver: ** %s: newHeaderSize %u exceeds MARKERRAM_MEM_SIZE %u, rejecting\n"
+ "AppleJPEGDriver: ** %s: newHeaderSize %u is not a multiple of 12 bytes, rejecting\n"
+ "AppleJPEGDriver: ** %s: startOfRawBitStream %u >= sourceSurface allocSize %llu, rejecting\n"
+ "AppleJPEGDriver: ** %s[%p] : die-id = %u\n"
+ "NerineFunctions"
+ "die-id"
+ "site.NerineFunctions"
+ "virtual bool NerineFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)"
- "1122211111111122121122222222212222222222222222222222222222222222222222222222222222222221111222221122222222222222212222222121112222222222222"
- "1221111111111111221122222222122222"
- "AppleJPEGDriver: %s(): Error! enablePsdService(en = %u) returned %d\n"
- "AppleJPEGDriver: %s, ERROR: failed to wait request successfully return 0x%x !\n"
- "AppleJPEGDriver: %s: Timeout occurred, cleaning up codec %d\n"
- "AppleJPEGDriver: * %s mPendingSetup is NULL, likely due to timeout cleanup - ignoring interrupt"

```
