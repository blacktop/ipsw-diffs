## com.apple.driver.AppleJPEGDriver

> `com.apple.driver.AppleJPEGDriver`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-8.1.3.0.0
-  __TEXT.__cstring: 0x2a63
-  __TEXT.__os_log: 0x9690
-  __TEXT.__const: 0x39ec
-  __TEXT_EXEC.__text: 0x2b598
+8.1.5.0.0
+  __TEXT.__cstring: 0x2b2e
+  __TEXT.__os_log: 0x9b22
+  __TEXT.__const: 0x3e9c
+  __TEXT_EXEC.__text: 0x2d24c
   __TEXT_EXEC.__auth_stubs: 0x680
-  __DATA.__data: 0x2208
-  __DATA.__common: 0x3d0
+  __DATA.__data: 0x2e58
+  __DATA.__common: 0x3f8
   __DATA.__bss: 0x1
-  __DATA_CONST.__mod_init_func: 0xc0
-  __DATA_CONST.__mod_term_func: 0xc0
-  __DATA_CONST.__const: 0x4b50
-  __DATA_CONST.__kalloc_type: 0xd80
+  __DATA_CONST.__mod_init_func: 0xc8
+  __DATA_CONST.__mod_term_func: 0xc8
+  __DATA_CONST.__const: 0x4df0
+  __DATA_CONST.__kalloc_type: 0xdc0
   __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x98
-  Functions: 1741
+  Functions: 1807
   Symbols:   0
-  CStrings:  520
+  CStrings:  533
 
CStrings:
+ "1211111212221212121111111222112222122222211111"
+ "121121"
+ "AppleJPEGDriver: %s : mHal unexpectedly NULL\n"
+ "AppleJPEGDriver: %s(): Fastsim detected via platform fuses\n"
+ "AppleJPEGDriver: %s: failed to create fuse descriptor at 0x%llx\n"
+ "AppleJPEGDriver: %s: failed to map fuse descriptor at 0x%llx\n"
+ "AppleJPEGDriver: %s: pre-silicon platform (PV_RUNTIME_ENV=0x%x, JPEG_PRESENT=0x%x), fastsim=%d\n"
+ "AppleJPEGDriver: ** %s : dim out of range pixelsX=%u pixelsY=%u decW=%u decH=%u cropW=%u cropH=%u cropOffX=%u cropOffY=%u\n"
+ "AppleJPEGDriver: ** %s : xOffset %u / yOffset %u / pixelsX %u / pixelsY %u out of range\n"
+ "AppleJPEGDriver: jpeg_huffman_set() - Invalid input\n"
+ "StockFunctions"
+ "bool AppleJPEGWrapperControl::getIsFsim() const"
+ "site.StockFunctions"
+ "virtual bool NerineFunctions::detectFastsim()"
+ "virtual bool StockFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)"
- "121111121222121212111111122112222122222211111"
- "12112"
```
