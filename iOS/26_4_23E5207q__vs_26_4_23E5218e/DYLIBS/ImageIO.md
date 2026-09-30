## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.4.3.0.0
-  __TEXT.__text: 0x44913c
-  __TEXT.__auth_stubs: 0x4230
+2784.4.6.0.0
+  __TEXT.__text: 0x449048
+  __TEXT.__auth_stubs: 0x4240
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x31578
-  __TEXT.__gcc_except_tab: 0x26590
-  __TEXT.__cstring: 0x9de20
+  __TEXT.__gcc_except_tab: 0x2659c
+  __TEXT.__cstring: 0x9df68
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
   __TEXT.__unwind_info: 0xed50

   __DATA_CONST.__objc_selrefs: 0xb10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2130
+  __AUTH_CONST.__auth_got: 0x2138
   __AUTH_CONST.__const: 0x3e178
-  __AUTH_CONST.__cfstring: 0x35c60
+  __AUTH_CONST.__cfstring: 0x35d00
   __AUTH_CONST.__objc_const: 0x1020
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0BEAE013-40B7-37DE-9EE4-194F2BB1BB14
+  UUID: 0E189857-B504-3716-AB3F-AA55AC8C984A
   Functions: 15478
-  Symbols:   47055
-  CStrings:  24853
+  Symbols:   47056
+  CStrings:  24864
 
Symbols:
+ _CGColorConversionInfoCreateForToneMapping
+ __ZN17IIOColorConverter30createConverterWithColorSpacesEP20vImage_CGImageFormatS1_P12CGColorSpaceS3_ff13CGToneMappingPK14__CFDictionary
+ __ZN17IIOColorConverterC1EP12CGColorSpaceS1_ff13CGToneMappingPK14__CFDictionary
+ __ZN17IIOColorConverterC2EP12CGColorSpaceS1_ff13CGToneMappingPK14__CFDictionary
+ __ZN17IIO_ReaderHandler19copyTypeIdentifiersEb
- __ZN17IIOColorConverter30createConverterWithColorSpacesEP20vImage_CGImageFormatS1_P12CGColorSpaceS3_
- __ZN17IIOColorConverterC1EP12CGColorSpaceS1_
- __ZN17IIOColorConverterC2EP12CGColorSpaceS1_
- __ZN17IIO_ReaderHandler19copyTypeIdentifiersEv
CStrings:
+ "*** ERROR: 'kCGImageSourceTypeIdentifierHint:%s' is not specifing image format\n"
+ "*** ERROR: CGColorConversionInfoConvertData cannot be used for resizing data (%d x%d) -> (%d, %d) - %d - '%s'\n"
+ "*** ERROR: CGColorConversionInfoConvertData failed\n"
+ "*** IIOColorConverter failed (%d)\n"
+ "*** IIOColorConverter failed - %s\n"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/FileFormats/libTIFF/tif_dir.c"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/AutoSharedLock.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/ConfigurableImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/ErrorImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IConfigurable_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IConfigurationManager_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IError_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IUTF8String_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/UTF8StringImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ArrayNodeImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ClientDOMParserWrapperImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ClientDOMSerializerWrapperImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/CompositeNodeImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/CoreObjectFactoryImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/DOMParserImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/DOMSerializerImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IArrayNode_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICompositeNode_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICoreConfigurationManager_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICoreObjectFactory_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMImplementationRegistry_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMParser_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMSerializer_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IMetadata_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INameSpacePrefixMap_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INodeIterator_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INode_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IPathSegment_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IPath_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ISimpleNode_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IStructureNode_I.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/MetadataConverterUtilsImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/MetadataImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/NameSpacePrefixMapImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/NodeImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/PathImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/PathSegmentImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/RDFDOMParserImpl.cpp"
+ "/Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/StructureNodeImpl.cpp"
+ "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
+ "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
+ "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
+ "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
+ "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
+ "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
+ "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
+ "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
+ "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
+ "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/2EA4C34E-C409-4C50-8080-B843220A6387/TemporaryDirectory.1ZWGLo/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
+ "com.apple.HubbleBlastDoorService"
+ "com.apple.ThumbnailsBlastDoorService"
+ "com.apple.WebKit.WebContent.EnhancedSecurity"
+ "com.apple.quicklook.thumbnail.ATXThumbnailExtension"
+ "com.apple.quicklook.thumbnail.NotificationExtension"
- "*** ERROR: 'kCGImageSourceTypeIdentifierHint:%s' is not specifing image format -- ignoring...\n"
- "*** vImageConvert_AnyToAny - %s\n"
- "*** vImageConvert_AnyToAny failed (%d)\n"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/FileFormats/libTIFF/tif_dir.c"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/AutoSharedLock.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/ConfigurableImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/ErrorImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IConfigurable_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IConfigurationManager_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IError_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IUTF8String_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/UTF8StringImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ArrayNodeImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ClientDOMParserWrapperImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ClientDOMSerializerWrapperImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/CompositeNodeImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/CoreObjectFactoryImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/DOMParserImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/DOMSerializerImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IArrayNode_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICompositeNode_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICoreConfigurationManager_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICoreObjectFactory_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMImplementationRegistry_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMParser_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMSerializer_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IMetadata_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INameSpacePrefixMap_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INodeIterator_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INode_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IPathSegment_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IPath_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ISimpleNode_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IStructureNode_I.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/MetadataConverterUtilsImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/MetadataImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/NameSpacePrefixMapImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/NodeImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/PathImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/PathSegmentImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/RDFDOMParserImpl.cpp"
- "/Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/StructureNodeImpl.cpp"
- "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
- "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
- "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
- "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
- "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
- "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
- "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
- "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
- "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
- "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/A390C3C5-55D4-41E9-9093-74630645A600/TemporaryDirectory.fAOhbL/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
- "png_do_quantize returned rowbytes=0"

```
