## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2644.0.0.0.0
-  __TEXT.__text: 0x3fb6e8
+2646.0.0.0.0
+  __TEXT.__text: 0x3fb9d8
   __TEXT.__auth_stubs: 0x3fd0
   __TEXT.__objc_methlist: 0x938
-  __TEXT.__const: 0x314b8
-  __TEXT.__gcc_except_tab: 0x1f178
-  __TEXT.__cstring: 0x79ace
+  __TEXT.__const: 0x31478
+  __TEXT.__gcc_except_tab: 0x1f1d0
+  __TEXT.__cstring: 0x79c43
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xd200
+  __TEXT.__unwind_info: 0xd210
   __TEXT.__eh_frame: 0x390
   __TEXT.__objc_classname: 0xce
   __TEXT.__objc_methname: 0x29f2

   __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x2bb8
-  __DATA.__bss: 0x5340
+  __DATA.__bss: 0x5360
   __DATA.__common: 0x1f00
   __DATA_DIRTY.__data: 0x170
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__common: 0xd03
-  __DATA_DIRTY.__bss: 0x6c8
+  __DATA_DIRTY.__common: 0xd0b
+  __DATA_DIRTY.__bss: 0x698
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13097
-  Symbols:   15472
-  CStrings:  12533
+  Functions: 13101
+  Symbols:   15476
+  CStrings:  12535
 
CStrings:
+ "⭕️ ERROR: '%!s(MISSING)' is trying to save an opaque image (%!d(MISSING)x%!d(MISSING)) with '%!s(MISSING)'. This would unnecessarily increase the file size and will double (!!!) the required memory when decoding the image --> ignoring alpha.\n "
+ "*** ERROR: CopyMetadataFromCFData cannot handle input data ([%!l(MISSING)d bytes] %!X(MISSING) %!X(MISSING) %!X(MISSING) %!X(MISSING) %!X(MISSING) %!X(MISSING) %!X(MISSING) %!X(MISSING)... '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING))'\n"
+ "❌  failed to load 'CMPhotoImageHasOpaqueAlphaFromPixelData' "
+ "CMPhotoImageHasOpaqueAlphaFromPixelData"
- "Unknown decode target: %!s(MISSING)\n"
- "⭕️ ImageIO: saving HEIF (%!d(MISSING)x%!d(MISSING)) with '%!s(MISSING)'\n"

```
