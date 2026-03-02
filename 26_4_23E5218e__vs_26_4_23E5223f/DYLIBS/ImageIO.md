## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.4.6.0.0
-  __TEXT.__text: 0x449048
+2784.4.7.0.0
+  __TEXT.__text: 0x4491c8
   __TEXT.__auth_stubs: 0x4240
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x31578
-  __TEXT.__gcc_except_tab: 0x2659c
-  __TEXT.__cstring: 0x9df68
+  __TEXT.__gcc_except_tab: 0x26574
+  __TEXT.__cstring: 0x9e02e
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
   __TEXT.__unwind_info: 0xed50

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0E189857-B504-3716-AB3F-AA55AC8C984A
-  Functions: 15478
-  Symbols:   47056
-  CStrings:  24864
+  UUID: ED388253-24B1-3802-8928-70BFD7823B94
+  Functions: 15477
+  Symbols:   47054
+  CStrings:  24869
 
Symbols:
+ ___block_descriptor_tmp.25
+ ___block_descriptor_tmp.46
+ ___block_descriptor_tmp.48
+ ___block_descriptor_tmp.57
+ ___block_literal_global.27
+ ___block_literal_global.50
- __ZN14IIOImageSource14extractOptionsEP13IIODictionary.cold.4
- ___block_descriptor_tmp.49
- ___block_descriptor_tmp.64
- ___block_literal_global.28
- ___block_literal_global.51
Functions:
~ __ZN14IIOImageSource14extractOptionsEP13IIODictionary : 1248 -> 1268
~ __ZN14IIOImageSource14doBindToReaderEv : 1248 -> 1232
~ __ZN17IIO_ReaderHandler17readerForBytesImpEPKhmPK10__CFStringm16IIOHeaderOptions10IIORequestPi : 816 -> 700
~ __ZN19IIOImageDestination33createPixelDataProviderConformingEP7CGImagelbP7CGColor23CGImagePluginWriteModesP13IIODictionary : 3588 -> 3636
~ __ZN14kdu_codestream15get_subsamplingEiR10kdu_coordsb : 376 -> 372
~ __ZN14kdu_codestream16get_registrationEi10kdu_coordsRS0_b : 412 -> 408
~ __TIFFGetStrileOffsetOrByteCountValue : 1348 -> 1384
~ __ZN20IIOImageWriteSession18createTempFileNameEPc : 268 -> 336
~ __ZN14ASTCTextureImp40createDecodedDataFromLZFSECompressedDataEP19IIOImageReadSessionPhmPS2_Pm : 280 -> 300
~ _OUTLINED_FUNCTION_8 : 24 -> 12
~ _OUTLINED_FUNCTION_9 : 12 -> 24
~ _OUTLINED_FUNCTION_13 : 12 -> 20
~ _OUTLINED_FUNCTION_16 : 20 -> 12
~ __cg_TIFFRGBAImageGet : 136 -> 240
~ __cg_TIFFReadRGBAImageOriented : 296 -> 272
~ _gtTileContig : 988 -> 1060
~ _gtStripContig : 788 -> 868
~ _gtTileSeparate : 1432 -> 1476
~ _gtStripSeparate : 1276 -> 1284
- __ZN14IIOImageSource28getPropertiesAtIndexInternalEmP13IIODictionary.cold.2
~ _CGImageCopyFileWithParametersOLD : 1836 -> 1908
CStrings:
+ "*** ERROR: failed to create temp file (err = %d '%s')\n"
+ "*** ERROR: kCGImageSourceDecodeFormatAllowlist does not contain the provided hint '%s'\n"
+ "*** ERROR: kCGImageSourceFailForDataNotMatchingHint=true but hint '%s' not in allowlist\n"
+ "Error in TIFFRGBAImageGet: row offset %d exceeds image height %d"
+ "Error in gtStripContig: column offset %d exceeds image width %d"
+ "Error in gtStripSeparate: column offset %d exceeds image width %d"
+ "Error in gtTileContig: column offset %d exceeds image width %d"
+ "Error in gtTileSeparate: column offset %d exceeds image width %d"
+ "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
+ "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
+ "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
+ "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
+ "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
+ "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
+ "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
+ "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
+ "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
+ "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
- "*** ERROR: invalid options: kCGImageSourceDecodeFormatAllowlist cannot be used when kCGImageSourceFailForDataNotMatchingHint is set to false\n"
- "*** ERROR: kCGImageSourceDecodeFormatAllowlist does not contain the provided hint '%s' - ignoring hint \n"
- "*** NOTE: incorrect hint '%s' with kCGImageSourceFailForDataNotMatchingHint - dropping hint, using allowList\n"
- "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
- "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
- "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
- "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
- "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
- "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
- "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
- "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
- "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
- "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"

```
