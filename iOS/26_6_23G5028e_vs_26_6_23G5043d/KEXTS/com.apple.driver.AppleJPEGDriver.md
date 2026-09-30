## com.apple.driver.AppleJPEGDriver

> `com.apple.driver.AppleJPEGDriver`

```diff

-7.7.9.0.0
-  __TEXT.__cstring: 0x29cd sha256:0f0a0acaec3ea22215111fcc21b9ca36a64dac88fc1a69ac47a2751e9b1db8eb
-  __TEXT.__os_log: 0x92e9 sha256:4fa7d52a30abde498467a613bcfb746d14bee0349f2192beb6089c43a535b386
-  __TEXT.__const: 0x391c sha256:3e9b67dfcc441625e112b794db16cfeb92591ebd703878f90af7ea55dd4d19f1
-  __TEXT_EXEC.__text: 0x2a954 sha256:3de12e9cfff86707e8629a9e329b13840672a7988a43842a0acb90aadbab6563
+8.1.3.0.0
+  __TEXT.__cstring: 0x297e sha256:22fc33f49679152b0f9161bbb86b88fdee6db0e24f8697aabca1fc9b793edeaf
+  __TEXT.__os_log: 0x9407 sha256:5b132618167be9c74c6956160c8e2fd1a0f1baf84de778cc6919c2509cf8e918
+  __TEXT.__const: 0x351c sha256:d1a6cbcc0202a36212f6e8393abad63f6296d1a288794685a60a86f0d230d1ec
+  __TEXT_EXEC.__text: 0x2a200 sha256:2253e8158b333243d2e4b0d413ae9023b531e37f6f21111296a90f1a798f7378
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2208 sha256:2d572c354c989c32c5d3380c21cd0fdd34cc1a157bd7c15bd98fff6f5927c075
-  __DATA.__common: 0x3a8 sha256:4db2fd521b198ad08a6602141c428d23a3bf232e85fd7de8418439e89d7b3d04
+  __DATA.__data: 0x2208 sha256:b2da4c1fc3ba4f97930053efccadb8079b0113c725af551aa00bc26fa336192f
+  __DATA.__common: 0x380 sha256:d54f02b97ed5bc2a642756268b41d4b8f7a077e73224e1580d22436834a14db5
   __DATA.__bss: 0x1 sha256:6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d
-  __DATA_CONST.__auth_got: 0x340 sha256:311d02f17a5577d2c3de252f204fc5c80e66998b3a4b0d5d96b034f659cfb41f
-  __DATA_CONST.__got: 0x98 sha256:1149baf2e83e2bfe235d0438677883e86b1633823aa4b2c13650c08bb7d35da6
-  __DATA_CONST.__mod_init_func: 0xb8 sha256:bcc46e3f04a608c752ef5b0d15dabde7620994fb5e16c56e61f82ed8ec2b6fa1
-  __DATA_CONST.__mod_term_func: 0xb8 sha256:e88b66b6744eb9f0bbd953d7e6189f97e045742bf6e2755affc94dad5ee98038
-  __DATA_CONST.__const: 0x49c0 sha256:766014b43b1cc5c31cb884ba70697dbc84092bd7e0d5b438c0802bf8730e429a
-  __DATA_CONST.__kalloc_type: 0xd40 sha256:abd6dfe51f059c83dd1561b772278549c23a69b21cd3616c0604fdde86912f3b
-  UUID: F81EE642-1044-32C3-8E6A-90775AD49663
-  Functions: 1713
+  __DATA_CONST.__auth_got: 0x340 sha256:5d70c7790a0b1e7023277855fdd031a8ed209d9999308d2902410be4a8176730
+  __DATA_CONST.__got: 0x98 sha256:7af57392e9ce13d47ddf0f96e22763e35bb2ee380fe5074526fd8e092b476b56
+  __DATA_CONST.__mod_init_func: 0xb0 sha256:601adca6da930de1a9e31ee1cd2d66d6ccca79f8aa7f33abb7700868959c0581
+  __DATA_CONST.__mod_term_func: 0xb0 sha256:39cd63d10f098de048d5be8ea368e0d18526885fda9a31c12e2223604bd9bcbc
+  __DATA_CONST.__const: 0x4830 sha256:9f6f43edc4fcb81742a3b796a8e201add65a4471e730b63e8b8dce837af1041c
+  __DATA_CONST.__kalloc_type: 0xd00 sha256:49d72c1a7c57fc83535d7b6fd281012c16c3a2e4fbca78a68d8cc5a34f38f14f
+  UUID: C38966E9-1E53-3940-8A71-EE197C74D223
+  Functions: 1680
   Symbols:   0
-  CStrings:  512
+  CStrings:  514
 
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
+ "die-id"
- "1122211111111122121122222222212222222222222222222222222222222222222222222222222222222221111222221122222222222222212222222121112222222222222"
- "1221111111111111221122222222122222"
- "AppleJPEGDriver: %s(): Error! enablePsdService(en = %u) returned %d\n"
- "AppleJPEGDriver: %s, ERROR: failed to wait request successfully return 0x%x !\n"
- "AppleJPEGDriver: %s: Timeout occurred, cleaning up codec %d\n"
- "AppleJPEGDriver: * %s mPendingSetup is NULL, likely due to timeout cleanup - ignoring interrupt"
- "DandelionFunctions"
- "site.DandelionFunctions"
- "virtual bool DandelionFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)"

```
