## IOMFB_FDR_Loader

> `/usr/bin/IOMFB_FDR_Loader`

```diff

-396.9.0.0.0
-  __TEXT.__text: 0x26004
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__gcc_except_tab: 0x160
+396.11.0.0.0
+  __TEXT.__text: 0x261ac
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__gcc_except_tab: 0x1a0
   __TEXT.__const: 0x1a00
-  __TEXT.__cstring: 0x4c8c
-  __TEXT.__unwind_info: 0x460
-  __DATA_CONST.__auth_got: 0x328
+  __TEXT.__cstring: 0x4cf2
+  __TEXT.__unwind_info: 0x478
+  __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x1870

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 346
-  Symbols:   130
-  CStrings:  674
+  Functions: 348
+  Symbols:   133
+  CStrings:  677
 
Symbols:
+ _AMFDRSealingManifestCopyMultiInstanceForClass
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
CStrings:
+ "AMFDR alternative failed to load!"
+ "AMFDR multi instance not found!"
+ "No matching FDR data, using default"

```
