## racoon

> `/usr/sbin/racoon`

```diff

-  __TEXT.__text: 0x64844
+  __TEXT.__text: 0x648e0
   __TEXT.__auth_stubs: 0x1230
   __TEXT.__const: 0x710a
-  __TEXT.__cstring: 0x57c9
+  __TEXT.__cstring: 0x57e7
   __TEXT.__oslogstring: 0xc732
   __TEXT.__unwind_info: 0xeb0
   __DATA_CONST.__const: 0x23e0

   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__data: 0x538
-  __DATA.__bss: 0x3300
+  __DATA.__bss: 0x3308
   __DATA.__common: 0x14e0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DirectoryService.framework/Versions/A/DirectoryService

   - /usr/lib/libiconv.2.dylib
   - /usr/lib/libipsec.A.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 2182
+  Functions: 2183
   Symbols:   332
-  CStrings:  2258
+  CStrings:  2259
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
CStrings:
+ "bad length in yy_scan_bytes()"

```
