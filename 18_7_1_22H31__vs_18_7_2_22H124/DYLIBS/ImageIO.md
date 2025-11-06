## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2661.7.1.0.0
-  __TEXT.__text: 0x465958
-  __TEXT.__auth_stubs: 0x4120
+2661.8.1.0.0
+  __TEXT.__text: 0x4691bc
+  __TEXT.__auth_stubs: 0x41d0
   __TEXT.__objc_methlist: 0xb58
-  __TEXT.__const: 0xb8a08
-  __TEXT.__gcc_except_tab: 0x1fabc
-  __TEXT.__cstring: 0x7c524
+  __TEXT.__const: 0xb8a28
+  __TEXT.__gcc_except_tab: 0x1ff34
+  __TEXT.__cstring: 0x7d1bc
   __TEXT.__oslogstring: 0x17
-  __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xd838
+  __TEXT.__ustring: 0x30
+  __TEXT.__unwind_info: 0xd928
   __TEXT.__eh_frame: 0x510
   __TEXT.__objc_classname: 0xce
   __TEXT.__objc_methname: 0x2a12

   __DATA_CONST.__objc_selrefs: 0xa48
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x20a8
-  __AUTH_CONST.__const: 0x3cde0
-  __AUTH_CONST.__cfstring: 0xda80
+  __AUTH_CONST.__auth_got: 0x2100
+  __AUTH_CONST.__const: 0x3cdf8
+  __AUTH_CONST.__cfstring: 0xde80
   __AUTH_CONST.__objc_const: 0xe50
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x10

   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x2cf0
   __DATA.__bss: 0x12820
-  __DATA.__common: 0x7ec4
+  __DATA.__common: 0x7ed4
   __DATA_DIRTY.__data: 0x170
   __DATA_DIRTY.__crash_info: 0x40
   __DATA_DIRTY.__common: 0xd33

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 285A114E-F7C2-3622-BDFC-8FFF60795707
-  Functions: 13889
-  Symbols:   36727
-  CStrings:  14500
+  UUID: 11142113-492E-33C7-A562-8C6790E944A9
+  Functions: 13917
+  Symbols:   36813
+  CStrings:  14613
 
Symbols:
+ _CFAttributedStringGetString
+ _CFStringGetCharacters
+ _CGColorSpaceCreatePattern
+ _CGContextDrawPath
+ _CGContextSetFillColorSpace
+ _CGContextSetFillPattern
+ _CGContextSetStrokeColorSpace
+ _CGContextSetStrokePattern
+ _CGPatternCreate
+ _CGPatternRelease
+ __Z17GetKtx2FormatInfoP11ktxTexture2RP14Ktx2FormatInfo
+ __Z17ValidateKTXHeaderRK10_KTXHeadery
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.1
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.10
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.2
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.3
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.4
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.5
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.6
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.7
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.8
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.9
+ __Z18OFDCreateCGPatternP8OFDColorP7OFDPage
+ __Z19GetKtx2VKFormatInfo8VkFormatRP14Ktx2FormatInfo
+ __Z39OFDExtractOFDObjectsFromCFArrayWithPagePK9__CFArrayPNSt3__16vectorIP9OFDObjectNS2_9allocatorIS5_EEEEP7OFDPage
+ __ZL22OFDPatternDrawCallbackPvP9CGContext
+ __ZL23OFDCreateObjectWithPagePK14__CFDictionaryP7OFDPage
+ __ZL25OFDPatternReleaseCallbackPv
+ __ZN11OFDDocument12getDrawParamEj
+ __ZN11OFDDocument14applyDrawParamEjP14__CFDictionary
+ __ZN11OFDTemplate27extractObjectsWithDrawParamEPK9__CFArrayj
+ __ZN11OFDTemplate8parseXMLEPK8__CFData.cold.1
+ __ZN13IIODictionary33getArrayObjectForPathWithIndexingEPK10__CFString
+ __ZN13OFDPathObject16resolveDrawParamEPK14__CFDictionaryP7OFDPage
+ __ZN13OFDPathObject20applyDrawParamColorsEPK14__CFDictionary
+ __ZN13OFDPathObjectC1EPK14__CFDictionaryP7OFDPage
+ __ZN13OFDPathObjectC2EPK14__CFDictionaryP7OFDPage
+ __ZN15IIO_Reader_KTX214validateHeaderERK11_KTX2Headerj
+ __ZN15IIO_Reader_KTX214validateHeaderERK11_KTX2Headerj.cold.1
+ __ZN7OFDPage18extractAnnotationsEv
+ __ZN7OFDPage21applyAnnotationOffsetEPK9__CFArray6CGRect
+ __ZNKSt3__16vectorIZN15IIO_Reader_KTX214validateHeaderERK11_KTX2HeaderjE7SectionNS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt3__19to_stringEj
+ __ZZN12IIOXPCClient12replyIsValidEPvE9validChar
+ ___block_descriptor_tmp.52
+ ___block_descriptor_tmp.93
+ ___block_literal_global.54
+ _gFunc_CTFontGetAdvancesForGlyphs
+ _gFunc_CTFontGetGlyphsForCharacters
- __Z17GetKtx2FormatInfo8VkFormatRP14Ktx2FormatInfo
- __Z17ValidateKTXHeaderP10_KTXHeadery
- __ZN10siz_params8finalizeEb.cold.1
- __ZN13JP2ReadPlugin11validateJP2EP10IIOScanner.cold.1
- __ZN13JP2ReadPlugin11validateJP2EP10IIOScanner.cold.2
- __ZN13JP2ReadPlugin11validateJP2EP10IIOScanner.cold.3
- __ZN13JP2ReadPlugin11validateJP2EP10IIOScanner.cold.4
- ___block_descriptor_tmp.92
- ___block_literal_global.36
CStrings:
+ "%g %g %g %g"
+ "*** ERROR: BASIS_LZ supercompression requires SGD (Supercompression Global Data)"
+ "*** ERROR: Cubemaps cannot have depth\n"
+ "*** ERROR: DFD extends beyond file size\n"
+ "*** ERROR: DFD offset and length must both be 0 or both be non-zero\n"
+ "*** ERROR: DFD offset overlaps with header\n"
+ "*** ERROR: GetKtx2VKFormatInfo: Unknown vkFormat %d\n"
+ "*** ERROR: KTX2 3D textures cannot have layers (%d)\n"
+ "*** ERROR: KTX2 numberOfFaces (%d) must be 1 or 6 (cubemap)\n"
+ "*** ERROR: KTX2 numberOfFaces must be greater than 0\n"
+ "*** ERROR: KTX2 numberOfMipmapLevels must be greater than 0\n"
+ "*** ERROR: KTX2 pixelHeight must be greater than 0\n"
+ "*** ERROR: KTX2 pixelWidth must be greater than 0\n"
+ "*** ERROR: KV extends beyond file size\n"
+ "*** ERROR: KVD extends beyond file size\n"
+ "*** ERROR: KVD length is non-zero but offset is 0"
+ "*** ERROR: KVD offset overlaps with header\n"
+ "*** ERROR: No texture data present in file"
+ "*** ERROR: SGD extends beyond file size\n"
+ "*** ERROR: SGD length is non-zero but offset is 0"
+ "*** ERROR: SGD offset overlaps with header\n"
+ "*** ERROR: SGD present but supercompression scheme is NONE"
+ "*** ERROR: bad 'COD ycb/ycb' (%d+%d)>12\n"
+ "*** ERROR: duplicate FTYP File Type Box (count: %u)\n"
+ "*** ERROR: duplicate JP Signature Box (count: %u)\n"
+ "*** ERROR: duplicate JP2C Continuous Codestream Box (count: %u)\n"
+ "*** ERROR: duplicate JP2H Header Box (count: %u)\n"
+ "*** ERROR: failed to get _structure from XMLDictionaryCreateWithData\n"
+ "*** ERROR: format is 0 but no DFD present\n"
+ "*** ERROR: glFormat must be non-zero for uncompressed textures\n"
+ "*** ERROR: glInternalFormat must be non-zero\n"
+ "*** ERROR: glInternalFormat must be non-zero for compressed textures\n"
+ "*** ERROR: glType must be non-zero for uncompressed textures\n"
+ "*** ERROR: glTypeSize (%d) must be 1 for compressed textures\n"
+ "*** ERROR: glTypeSize must be non-zero for uncompressed textures\n"
+ "*** ERROR: invalid KTX2 identifier\n"
+ "*** ERROR: invalid xcb - failing 'COD xcb' check:  2 <= %d <= 10\n"
+ "*** ERROR: invalid ycb - failing 'COD ycb' check:  2 <= %d <= 10\n"
+ "*** ERROR: marker '%c%c%c%c' length (%llu) at offset (%llu [0x%llX]) larger than fileSize(%llu)\n"
+ "*** ERROR: missing or invalid ContinuousCodestreamBox count (%u)\n"
+ "*** ERROR: missing or invalid FileTypeBox count (%u)\n"
+ "*** ERROR: missing or invalid JP2HeaderBox count (%u)\n"
+ "*** ERROR: missing or invalid SignatureBox count (%u)\n"
+ "*** ERROR: numberOfFaces (%d) must be 1 or 6 (cubemap)\n"
+ "*** ERROR: numberOfMipmapLevels (%d) exceeds maximum possible mipmap levels (%d)\n"
+ "*** ERROR: numberOfMipmapLevels must be at least 1"
+ "*** ERROR: pixelWidth must be greater than 0\n"
+ "*** ERROR: sections overlap ['%c%c%c%c' [%llu,%llu) - '%c%c%c%c' [%llu,%llu)\n"
+ "*** ERROR: too many boxes (%u)\n"
+ "*** ERROR: unknown supercompressionScheme (%d)\n"
+ "*** Empty component at index %u\n"
+ "*** NOTE: Cubemap faces should be square"
+ "*** NOTE: Key-value data size not aligned to 4 bytes"
+ "*** check font-mapping:   fontName: %s\n"
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
+ "GetKtx2VKFormatInfo"
+ "Hiragino Sans GB W3"
+ "ImageObject"
+ "Invalid array syntax: missing closing bracket in '%s'\n"
+ "I{\xbf~"
+ "KTXWritePlugin::WriteProc"
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
+ "Res.DrawParams.DrawParam"
+ "SimHei"
+ "SimSun"
+ "Subtype"
+ "TextObject"
+ "ValidateKTXHeader"
+ "XStep"
+ "YStep"
+ "getArrayObjectForPathWithIndexing"
+ "validateHeader"
+ "\xae_o\x8fŖў"
- "*** ERROR: XMLDictionaryCreateWithData failed\n"
- "*** ERROR: bad 'COD CodeBlockWidth' (%d)\n"
- "*** ERROR: marker '%c%c%c%c' length (%d) at offset (%d [0x%04X]) larger than fileSize(%d)\n"
- "*** ERROR: no ContinousCodestreamBox\n"
- "*** ERROR: no FileTypeBox\n"
- "*** ERROR: no JP2HeaderBox\n"
- "*** ERROR: no SignatureBox\n"
- "*** invalid KTX2 file: bytesOfKeyValueData: %d (fileSize: %d)\n"
- "abcdefghijklmnopqrstuvwxyz0123456789_"
- "have_dims && have_size"

```
