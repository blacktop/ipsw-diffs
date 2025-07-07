## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2759.0.1.1.0
-  __TEXT.__text: 0x39e3bc
-  __TEXT.__auth_stubs: 0x4100
+2764.0.1.0.0
+  __TEXT.__text: 0x3a0c0c
+  __TEXT.__auth_stubs: 0x41d0
   __TEXT.__objc_methlist: 0xd20
-  __TEXT.__const: 0x2eba8
-  __TEXT.__gcc_except_tab: 0x20c2c
-  __TEXT.__cstring: 0x9aa17
+  __TEXT.__const: 0x2ebb8
+  __TEXT.__gcc_except_tab: 0x21068
+  __TEXT.__cstring: 0x9ae1f
   __TEXT.__oslogstring: 0x17
-  __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xd150
+  __TEXT.__ustring: 0x30
+  __TEXT.__unwind_info: 0xd1d8
   __TEXT.__eh_frame: 0x308
   __TEXT.__objc_classname: 0xe0
   __TEXT.__objc_methname: 0x2e13
   __TEXT.__objc_methtype: 0x24c0
   __TEXT.__objc_stubs: 0x2580
-  __DATA_CONST.__got: 0x600
-  __DATA_CONST.__const: 0x4c080
+  __DATA_CONST.__got: 0x5f8
+  __DATA_CONST.__const: 0x4c088
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2098
-  __AUTH_CONST.__const: 0x3c860
-  __AUTH_CONST.__cfstring: 0x35860
+  __AUTH_CONST.__auth_got: 0x2100
+  __AUTH_CONST.__const: 0x3c838
+  __AUTH_CONST.__cfstring: 0x35c40
   __AUTH_CONST.__objc_const: 0x1020
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x30

   __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x2bb0
-  __DATA.__bss: 0x4f40
-  __DATA.__common: 0x1ea0
+  __DATA.__bss: 0x4f30
+  __DATA.__common: 0x1eb0
   __DATA_DIRTY.__data: 0x168
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__common: 0xdf3
-  __DATA_DIRTY.__bss: 0xb38
+  __DATA_DIRTY.__bss: 0xb18
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: FD5799AC-17D6-3AE5-B57B-4A8C01CB61C8
-  Functions: 13114
-  Symbols:   40922
-  CStrings:  24616
+  UUID: 58090C92-BAC7-30E5-A31D-4770DBC16875
+  Functions: 13126
+  Symbols:   40967
+  CStrings:  24684
 
Symbols:
+ GCC_except_table150
+ GCC_except_table152
+ GCC_except_table156
+ _CFAttributedStringGetString
+ _CFStringGetCharacters
+ _CGColorConversionInfoConvertData
+ _CGColorSpaceCreatePattern
+ _CGContextDrawPath
+ _CGContextSetFillColorSpace
+ _CGContextSetFillPattern
+ _CGContextSetStrokeColorSpace
+ _CGContextSetStrokePattern
+ _CGImageCreateWithImageInRect
+ _CGPatternCreate
+ _CGPatternRelease
+ __Z18OFDCreateCGPatternP8OFDColorP7OFDPage
+ __Z39OFDExtractOFDObjectsFromCFArrayWithPagePK9__CFArrayPNSt3__16vectorIP9OFDObjectNS2_9allocatorIS5_EEEEP7OFDPage
+ __ZL22OFDPatternDrawCallbackPvP9CGContext
+ __ZL23OFDCreateObjectWithPagePK14__CFDictionaryP7OFDPage
+ __ZL25OFDPatternReleaseCallbackPv
+ __ZN11OFDDocument12getDrawParamEj
+ __ZN11OFDDocument14applyDrawParamEjP14__CFDictionary
+ __ZN11OFDTemplate27extractObjectsWithDrawParamEPK9__CFArrayj
+ __ZN13IIODictionary33getArrayObjectForPathWithIndexingEPK10__CFString
+ __ZN13OFDPathObject16resolveDrawParamEPK14__CFDictionaryP7OFDPage
+ __ZN13OFDPathObject20applyDrawParamColorsEPK14__CFDictionary
+ __ZN13OFDPathObjectC1EPK14__CFDictionaryP7OFDPage
+ __ZN13OFDPathObjectC2EPK14__CFDictionaryP7OFDPage
+ __ZN14IIOImageSource21getPropertiesInternalEP13IIODictionary
+ __ZN19IIOImageDestination20handleEncodingIntentEP7CGImageP13IIODictionaryS3_
+ __ZN7OFDPage18extractAnnotationsEv
+ __ZN7OFDPage21applyAnnotationOffsetEPK9__CFArray6CGRect
+ __ZNSt3__19to_stringEj
+ ___block_descriptor_tmp.29
+ ___block_descriptor_tmp.44
+ ___block_literal_global.31
+ ___block_literal_global.54
+ _gFunc_CTFontGetAdvancesForGlyphs
+ _gFunc_CTFontGetGlyphsForCharacters
+ _kCGImageDestinationEncodeForScreenshot
+ _kCGImageDestinationEncodingIntent
- GCC_except_table153
- _IIOUpdatePropertiesIfNeeded
- _IIOUpdatePropertiesIfNeeded.cold.1
- _IIOUpdatePropertiesIfNeeded.cold.2
- __ZZL18IIOSolariumEnabledvE4once
- __ZZL18IIOSolariumEnabledvE9isEnabled
- __ZZL20IIOScreencaptureModevE18screenCaptureFlags
- __ZZL20IIOScreencaptureModevE4once
- ____ZL18IIOSolariumEnabledv_block_invoke
- ____ZL20IIOScreencaptureModev_block_invoke
- ___block_descriptor_tmp.16
- ___block_descriptor_tmp.28
- ___block_descriptor_tmp.43
- ___block_literal_global.18
- ___block_literal_global.30
- ___block_literal_global.36
- ___block_literal_global.80
- _kCGColorSpaceDisplayP3_HLG
CStrings:
+ "     colorspace: kCGColorSpaceDisplayP3  (fallback for 8bpc from kKTX_ExtendedRGB)\n"
+ "%g %g %g %g"
+ "%s %s:%d %s orientation(_HEIC_to_JPEG): %d\n"
+ "%s %s:%d %s orientation(_useAppleJPEG_resize): %d\n"
+ "%s %s:%d %s orientation(default): %d\n"
+ "%s %s:%d %s orientation(recode): %d\n"
+ "%s %s:%d %s orientation: %d\n"
+ "%s %s:%d - Orientation: not found\n"
+ "%s %s:%d - Orientation: top:%d  {TIFF}:%d\n"
+ "%s %s:%d CGImageCreateThumbNew: maxPixelSize: %d  applied exifOrientation: %d  - resetting orientation in options to 1\n"
+ "*** ERROR: 'kCGImageSourceTypeIdentifierHint:%s' is not specifing image format -- ignoring...\n"
+ "*** ERROR: CGBitmapContextCreate failed (size: %dx%d   rb: %d  bpc: %d  bmi: %s\n"
+ "*** ERROR: CVPixelBufferCreateWithIOSurface '%c%c%c%c' failed with: %d  (%s)\n"
+ "*** ERROR: CVPixelBufferCreateWithIOSurface failed - NULL-surface\n"
+ "*** ERROR: Invalid dfdOffset / dfdLength  (%d / %d).\n"
+ "*** ERROR: Invalid kvdOffset / kvdLength  (%d / %d).\n"
+ "*** ERROR: Invalid numberOfArrayElements (%d).\n"
+ "*** ERROR: Invalid scgdOffset / scgdLength  (%d / %d).\n"
+ "*** ERROR: Invalid typeSize (%d). typeSize must be 1 for block-compressed or supercompressed formats.\n"
+ "*** ERROR: corrupt Level info - byteOffset: %ld  byteLength: %ld\n"
+ "*** ERROR: failed to read KTX2Header\n"
+ "*** ERROR: failed to read KTX2LevelInfo\n"
+ "*** ERROR: invalid KTX2Header\n"
+ "*** ERROR: ❌ '%s' is using 'kCGImageSourceTypeIdentifierHint:%s' - as a hint for an image file format?\n"
+ "*** Empty component at index %u\n"
+ "*** check font-mapping:   fontName: %s\n"
+ "*** 🔄 ImageIO: write plugin changed from '%c%c%c%c' to '%c%c%c%c' (%s)\n"
+ "/Annotation.xml"
+ "/Annots/Page_"
+ "Appearance"
+ "Array index %ld out of bounds (array size: %ld) for key '%s'\n"
+ "CTFontGetAdvancesForGlyphs"
+ "CTFontGetGlyphsForCharacters"
+ "CellContent"
+ "Content"
+ "Current object is not a dictionary, cannot access key '%s'\n"
+ "Doc_"
+ "DrawParam"
+ "HEIF_HEIF"
+ "HEIF_JPEG"
+ "Hiragino Sans GB W3"
+ "ImageObject"
+ "Invalid array syntax: missing closing bracket in '%s'\n"
+ "I{\xbf~"
+ "JPEG_HEIF"
+ "JPEG_JPEG"
+ "Key '%s' is not an array or doesn't exist\n"
+ "Layer"
+ "Page"
+ "Page.Content.Layer"
+ "Page.Content.Layer.PageBlock"
+ "Page.Content.Layer[%d].ImageObject"
+ "Page.Content.Layer[%d].PathObject"
+ "Page.Content.Layer[%d].TextObject"
+ "PageAnnot.Annot"
+ "PathObject"
+ "PingFang SC"
+ "RAW_HEIF"
+ "RAW_JPEG"
+ "Res.DrawParams.DrawParam"
+ "SimHei"
+ "SimSun"
+ "Subtype"
+ "TextObject"
+ "XStep"
+ "YStep"
+ "getArrayObjectForPathWithIndexing"
+ "getPropertiesInternal"
+ "kCGImageDestinationEncodeForScreenshot"
+ "kCGImageDestinationEncodingIntent"
+ "use"
+ "\xae_o\x8fŖў"
- "     colorspace: kCGColorSpaceExtendedSRGB\n"
- "%s %s:%d - Orientation not found in dictionary\n"
- "%s %s:%d - Orientation tiff: %d\n"
- "%s %s:%d - Orientation top+tiff: %d / %d\n"
- "%s %s:%d - Orientation top: %d\n"
- "%s CGImageCreateThumbNew: maxPixelSize: %d  exifOrientation: %d\n"
- "%s WriteExifData: writing Exif data\n"
- "%s bakeInOrientation: _HEIC_to_JPEG %s\n"
- "%s bakeInOrientation: _useAppleJPEG_resize %s\n"
- "%s bakeInOrientation: default %s\n"
- "%s finalize: bakeInOrientation-%s:  %d\n"
- "%s recode: bakeInOrientation: %d\n"
- "%s recode: not changing orientation : %d\n"
- "%s recode: orientation value from user input:\n"
- "%s recode: writing Exif to destination file:\n"
- "*** ERROR: CVPixelBufferCreateWithIOSurface failed with: %d  (%s)\n"
- "*** ERROR: Invalid typeSize (%d). typeSize must be 1 for block-compressed or supercompressed formats."
- "*** ERROR: XMLDictionaryCreateWithData failed\n"
- "*** ERROR: failed to get properties from incomplete CGImageSource\n"
- "*** ERROR: ❌ unknown hint identifier 'kCGImageSourceTypeIdentifierHint:%s' -- ignoring...\n"
- "*** Note: switching write plugin (auxImage): 'JPEG' --> 'HEIC'  (_transcodingMode: %d)\n"
- "CADebug"
- "IIOReadPlugin::CleanupRecodeProperties:  top: %d  tiff: %d\n"
- "ScreenshotServicesService"
- "Solarium"
- "SwiftUI"
- "com.apple.DiagnosticExtensions.ScreenshotterDiagnosticExtension"
- "com.apple.TapToRadar"
- "com.apple.dt.DTScreenshotService"
- "coreautomationd"
- "getProperties"
- "parseXML"
- "stacktool"

```
