## CoreUI

> `/System/Library/PrivateFrameworks/CoreUI.framework/Versions/A/CoreUI`

```diff

-1010.0.0.0.0
-  __TEXT.__text: 0x125234
+1011.2.0.0.0
+  __TEXT.__text: 0x125530
   __TEXT.__delay_stubs: 0x140
   __TEXT.__delay_helper: 0xa4
   __TEXT.__objc_methlist: 0xb618
   __TEXT.__const: 0xa858
   __TEXT.__gcc_except_tab: 0x308c
-  __TEXT.__cstring: 0x2be18
+  __TEXT.__cstring: 0x2c072
   __TEXT.__oslogstring: 0x250
   __TEXT.__swift5_typeref: 0x3b0
   __TEXT.__swift5_capture: 0x168

   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x5c
-  __TEXT.__unwind_info: 0x5c68
+  __TEXT.__unwind_info: 0x5c70
   __TEXT.__eh_frame: 0x120
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x520
   __DATA_CONST.__objc_arraydata: 0x17f0
   __DATA_CONST.__got: 0xc88
-  __AUTH_CONST.__const: 0x5098
-  __AUTH_CONST.__cfstring: 0x15040
+  __AUTH_CONST.__const: 0x50b8
+  __AUTH_CONST.__cfstring: 0x15080
   __AUTH_CONST.__objc_const: 0x11248
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x1578

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6743
-  Symbols:   14055
-  CStrings:  6215
+  Functions: 6745
+  Symbols:   14058
+  CStrings:  6224
 
Symbols:
+ _____preferredLocalization_block_invoke
+ __preferredLocalization.__preferredLocalizationCache
+ __preferredLocalization.__preferredLocalizationOnce
Functions:
~ __ReadFreeList : 464 -> 412
~ -[CUICatalog _setPreferredLocalization:] : 392 -> 588
~ -[_CUIThemePixelRendition newImageFromCSIDataSlice:ofBitmap:usingColorspace:] : 1780 -> 1832
~ -[_CSIRenditionBlockData expandCSIBitmapData:fromSlice:makeReadOnly:] : 1708 -> 1716
~ _CUIUncompressDeepmap2ImageData : 1048 -> 1056
~ _pk_decompressData : 248 -> 448
~ ___decompressRLE32 : 288 -> 352
~ -[CUIVectorGlyphLayerDrawAttachmentStore computeCapacity:numAttachments:withScanner:usingAttachmentDelimiter:fieldDelimiter:digits:] : 388 -> 392
~ -[CUIVectorGlyphLayerDrawAttachmentStore initFromSVGString:attachmentData:] : 1316 -> 1304
~ ___decompressRLE8 : 292 -> 344
~ ___decompressRLE16 : 288 -> 344
~ -[_CUIThemePixelRendition _initWithCSIHeader:version:] : 3092 -> 3180
~ _OUTLINED_FUNCTION_1 : 24 -> 32
+ _____preferredLocalization_block_invoke
+ __getDeviceTraits.cold.1
CStrings:
+ "%@:%@"
+ "CoreUI: CSI bitmap data starts past the end of the rendition data"
+ "CoreUI: CSI image index %u (offset %u) is outside the rendition data: '%@'"
+ "CoreUI: Invalid chunk rows of %lu in image of height %lu (rows already decoded: %lu)"
+ "CoreUI: raw image slice needs %zu bytes at offset %zu but only %zu bytes of bitmap data are available (rowbytes %zu)"
+ "com.apple.coreui-preferred-localization-cache"
+ "decompressData: %zu byte block too small to hold the row index for rows %d..%d\n"
+ "decompressData: invalid region %d,%d %dx%d\n"
+ "decompressData: row %d offset %u lies outside the %zu byte block\n"
+ "decompressData: truncated scanline %d in the %zu byte block\n"
- "_ReadFreeList: tring to read count of freelist table."
```
