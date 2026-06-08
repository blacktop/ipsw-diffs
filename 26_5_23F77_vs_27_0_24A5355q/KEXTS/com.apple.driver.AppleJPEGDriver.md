## com.apple.driver.AppleJPEGDriver

> `com.apple.driver.AppleJPEGDriver`

```diff

-7.7.9.0.0
-  __TEXT.__cstring: 0x29cd
-  __TEXT.__os_log: 0x92e9
-  __TEXT.__const: 0x391c
-  __TEXT_EXEC.__text: 0x2a954
+8.1.0.0.0
+  __TEXT.__cstring: 0x2a63
+  __TEXT.__os_log: 0x9690
+  __TEXT.__const: 0x39ec
+  __TEXT_EXEC.__text: 0x2b1c4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2208
-  __DATA.__common: 0x3a8
+  __DATA.__common: 0x3d0
   __DATA.__bss: 0x1
+  __DATA_CONST.__mod_init_func: 0xc0
+  __DATA_CONST.__mod_term_func: 0xc0
+  __DATA_CONST.__const: 0x4b50
+  __DATA_CONST.__kalloc_type: 0xd80
   __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__mod_init_func: 0xb8
-  __DATA_CONST.__mod_term_func: 0xb8
-  __DATA_CONST.__const: 0x49c0
-  __DATA_CONST.__kalloc_type: 0xd40
-  UUID: F81EE642-1044-32C3-8E6A-90775AD49663
-  Functions: 1713
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
