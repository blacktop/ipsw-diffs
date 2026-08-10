## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

 2784.6.6.0.0
-  __TEXT.__text: 0x28bc6c
+  __TEXT.__text: 0x28c2b0
   __TEXT.__auth_stubs: 0x4ab0
   __TEXT.__objc_methlist: 0xd58
   __TEXT.__const: 0x11b28
-  __TEXT.__gcc_except_tab: 0x1badc
-  __TEXT.__cstring: 0x6d77a
+  __TEXT.__gcc_except_tab: 0x1bbb4
+  __TEXT.__cstring: 0x6dc4e
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xae10
+  __TEXT.__unwind_info: 0xae30
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0xf1
   __TEXT.__objc_methname: 0x2cd6

   __AUTH.__objc_data: 0x370
   __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0xa4
-  __DATA.__data: 0x2390
+  __DATA.__data: 0x23e0
   __DATA.__bss: 0x4df8
   __DATA.__common: 0xac0
   __DATA_DIRTY.__data: 0x141

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10215
-  Symbols:   20791
-  CStrings:  14785
+  Functions: 10213
+  Symbols:   20793
+  CStrings:  14805
 
Symbols:
+ __ZN13GlobalGIFInfo14globalColorMapEv
+ __ZZ41CGImageMetadataRegisterNamespaceForPrefixE22alreadyRegistered_lock
CStrings:
+ "*** ERROR: CG fallback rowBytes overflow rounding up: product=%u\n"
+ "*** ERROR: CG fallback rowBytes overflow: dstWidth=%zu * bpp=%u\n"
+ "*** ERROR: Extended XMP marker XMP data is NULL, skipping marker\n"
+ "*** ERROR: IOSurface does not support chroma rowBytes larger than INT32_MAX"
+ "*** ERROR: _TAG::writeToBuffer - out-of-bounds source: offset: %u  tiffStart: %u  size: %u  jpegDataSize: %ld\n"
+ "*** ERROR: copyDateTime - out-of-bounds: offset: %u  tiffStart: %u  count: %u  size: %ld\n"
+ "*** ERROR: dstRowBytes overflow: dstWidth=%zu * (bpp/8)=%u\n"
+ "*** ERROR: iio_convert_XRGB2101010ToRGB16U: MALLOC(%zu) failed\n"
+ "*** ERROR: iio_convert_XRGB2101010ToRGB16U: rowBytes overflow (width=%zu)\n"
+ "*** ERROR: image dimensions exceed UINT32_MAX: %zu x %zu\n"
+ "*** ERROR: preserveGainMapUsingCFDataRef - gain map descriptor (%u x %u, rowBytes %u) inconsistent with %ld-byte source; skipping\n"
+ "*** ERROR: subsampleRGB888 MALLOC failed (src=%p dst=%p, %zu x %u)\n"
+ "*** IOSurface does not support allocSize larger than INT32_MAX\n"
+ "*** IOSurface does not support rowBytes/allocSize larger than INT32_MAX\n"
+ "*** dest buffer size overflow [%u x %u x %zu]\n"
+ "*** invalid row bytes (src=%u dst=%u)\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/AutoSharedLock.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/ConfigurableImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/ErrorImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IConfigurable_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IConfigurationManager_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IError_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IUTF8String_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/UTF8StringImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ArrayNodeImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ClientDOMParserWrapperImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ClientDOMSerializerWrapperImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/CompositeNodeImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/CoreObjectFactoryImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/DOMParserImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/DOMSerializerImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IArrayNode_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICompositeNode_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICoreConfigurationManager_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICoreObjectFactory_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMImplementationRegistry_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMParser_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMSerializer_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IMetadata_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INameSpacePrefixMap_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INodeIterator_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INode_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IPathSegment_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IPath_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ISimpleNode_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IStructureNode_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/MetadataConverterUtilsImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/MetadataImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/NameSpacePrefixMapImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/NodeImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/PathImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/PathSegmentImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/RDFDOMParserImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/StructureNodeImpl.cpp"
+ "IIO_UpdatePlanarSurfaceOptions"
+ "IIO_UpdateSurfaceOptions"
+ "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
+ "XMP_Enforce failed: (amountRead == count) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
+ "XMP_Enforce failed: (itemIndex < arraySize) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
+ "XMP_Enforce failed: (itemIndex <= arraySize) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
+ "XMP_Enforce failed: (length <= this->currLength) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
+ "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
+ "XMP_Enforce failed: (newOffset >= 0) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
+ "XMP_Enforce failed: (nsFound) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
+ "XMP_Enforce failed: (rdfString != 0) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
+ "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bgy0ZM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
+ "copyDateTime"
+ "writeToBuffer"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/AutoSharedLock.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/ConfigurableImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/ErrorImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IConfigurable_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IConfigurationManager_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IError_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IUTF8String_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/UTF8StringImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ArrayNodeImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ClientDOMParserWrapperImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ClientDOMSerializerWrapperImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/CompositeNodeImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/CoreObjectFactoryImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/DOMParserImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/DOMSerializerImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IArrayNode_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICompositeNode_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICoreConfigurationManager_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICoreObjectFactory_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMImplementationRegistry_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMParser_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMSerializer_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IMetadata_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INameSpacePrefixMap_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INodeIterator_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INode_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IPathSegment_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IPath_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ISimpleNode_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IStructureNode_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/MetadataConverterUtilsImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/MetadataImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/NameSpacePrefixMapImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/NodeImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/PathImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/PathSegmentImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/RDFDOMParserImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/StructureNodeImpl.cpp"
- "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
- "XMP_Enforce failed: (amountRead == count) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
- "XMP_Enforce failed: (itemIndex < arraySize) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
- "XMP_Enforce failed: (itemIndex <= arraySize) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
- "XMP_Enforce failed: (length <= this->currLength) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
- "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
- "XMP_Enforce failed: (newOffset >= 0) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
- "XMP_Enforce failed: (nsFound) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
- "XMP_Enforce failed: (rdfString != 0) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
- "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
```
