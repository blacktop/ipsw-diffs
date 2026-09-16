## CoreUI

> `/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`

```diff

-1010.0.0.0.0
-  __TEXT.__text: 0xe31ac
+1011.2.0.0.0
+  __TEXT.__text: 0xe34ac
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xa4
   __TEXT.__objc_methlist: 0xa420
   __TEXT.__const: 0x64d8
   __TEXT.__gcc_except_tab: 0x2c7c
-  __TEXT.__cstring: 0x25d27
+  __TEXT.__cstring: 0x25f71
   __TEXT.__oslogstring: 0x200
   __TEXT.__constg_swiftt: 0x2fc
   __TEXT.__swift5_typeref: 0x38e

   __TEXT.__swift5_capture: 0x168
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_assocty: 0x58
-  __TEXT.__unwind_info: 0x50d0
+  __TEXT.__unwind_info: 0x50d8
   __TEXT.__eh_frame: 0x120
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0xbe0
   __DATA_CONST.__got: 0xa48
-  __AUTH_CONST.__const: 0x3660
-  __AUTH_CONST.__cfstring: 0x12540
+  __AUTH_CONST.__const: 0x3680
+  __AUTH_CONST.__cfstring: 0x12580
   __AUTH_CONST.__objc_const: 0xf298
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x300

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5828
-  Symbols:   11117
-  CStrings:  5504
+  Functions: 5830
+  Symbols:   11120
+  CStrings:  5513
 
Symbols:
+ _____preferredLocalization_block_invoke
+ ___preferredLocalization.__preferredLocalizationCache
+ ___preferredLocalization.__preferredLocalizationOnce
Functions:
~ __ReadFreeList : 472 -> 420
~ _OUTLINED_FUNCTION_1 : 24 -> 32
~ -[CUICatalog _setPreferredLocalization:] : 388 -> 588
~ -[_CUIThemePixelRendition _initWithCSIHeader:version:] : 3084 -> 3160
~ -[_CUIThemePixelRendition newImageFromCSIDataSlice:ofBitmap:usingColorspace:] : 1776 -> 1828
~ -[_CSIRenditionBlockData expandCSIBitmapData:fromSlice:makeReadOnly:] : 1708 -> 1716
~ _CUIUncompressDeepmap2ImageData : 1032 -> 1040
~ -[CUIVectorGlyphLayerDrawAttachmentStore initFromSVGString:attachmentData:] : 1316 -> 1308
~ -[CUIVectorGlyphLayerDrawAttachmentStore computeCapacity:numAttachments:withScanner:usingAttachmentDelimiter:fieldDelimiter:digits:] : 388 -> 392
~ _pk_decompressData : 248 -> 456
~ ___decompressRLE8 : 292 -> 344
~ ___decompressRLE16 : 288 -> 344
~ ___decompressRLE32 : 288 -> 352
+ _____preferredLocalization_block_invoke
+ -[CUICatalog _vibrantColorMatrixBrightnessSaturationForColor:saturation:brightness:].cold.1
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
