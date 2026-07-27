## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-2784.6.3.0.0
-  __TEXT.__text: 0x28b91c
+2784.6.6.0.0
+  __TEXT.__text: 0x28bc6c
   __TEXT.__auth_stubs: 0x4ab0
   __TEXT.__objc_methlist: 0xd58
-  __TEXT.__const: 0x11a58
-  __TEXT.__gcc_except_tab: 0x1bad4
-  __TEXT.__cstring: 0x6d710
+  __TEXT.__const: 0x11b28
+  __TEXT.__gcc_except_tab: 0x1badc
+  __TEXT.__cstring: 0x6d77a
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xadd0
+  __TEXT.__unwind_info: 0xae10
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0xf1
   __TEXT.__objc_methname: 0x2cd6

   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x470
   __AUTH_CONST.__auth_got: 0x2570
-  __AUTH_CONST.__const: 0x3c528
+  __AUTH_CONST.__const: 0x3c630
   __AUTH_CONST.__cfstring: 0x35d80
   __AUTH_CONST.__objc_const: 0x10f8
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10192
-  Symbols:   20759
-  CStrings:  14783
+  Functions: 10215
+  Symbols:   20791
+  CStrings:  14785
 
Symbols:
+ _ZN13GlobalGIFInfo14readFromStreamEP14__CFReadStream
+ __ZNK3xdr18PixelFormatR8Unorm13bytesPerPixelEv
+ __ZNK3xdr19PixelFormatR16Float13bytesPerPixelEv
+ __ZNK3xdr19PixelFormatR16Unorm13bytesPerPixelEv
+ __ZNK3xdr19PixelFormatR32Float13bytesPerPixelEv
+ __ZNK3xdr19PixelFormatRG8Unorm13bytesPerPixelEv
+ __ZNK3xdr20PixelFormatRG16Unorm13bytesPerPixelEv
+ __ZNK3xdr21PixelFormatBGRA8Unorm13bytesPerPixelEv
+ __ZNK3xdr22PixelFormatRGBA16Float13bytesPerPixelEv
+ __ZNK3xdr22PixelFormatRGBA16Unorm13bytesPerPixelEv
+ __ZNK3xdr22PixelFormatRGBA32Float13bytesPerPixelEv
+ __ZNK3xdr23PixelFormatBGR10A2Unorm13bytesPerPixelEv
+ __ZNKSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info
+ __ZNSt3__110shared_ptrI11IIOColorMapEaSB9fqe210106IS1_NS_14default_deleteIS1_EELi0EEERS2_ONS_10unique_ptrIT_T0_EE
+ __ZNSt3__115allocate_sharedB9fqe210106I11GIFColorMapNS_9allocatorIS1_EEJRP14ColorMapObjectELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEEC2B9fqe210106IJRP14ColorMapObjectES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEED1Ev
+ __ZTINSt3__114default_deleteI11IIOColorMapEE
+ __ZTINSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEEE
+ __ZTINSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEEE
+ __ZTSNSt3__114default_deleteI11IIOColorMapEE
+ __ZTSNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEEE
+ __ZTSNSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceI11GIFColorMapNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_pointerIP11IIOColorMapNS_14default_deleteIS1_EENS_9allocatorIS1_EEEE
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/AutoSharedLock.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/ConfigurableImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/ErrorImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IConfigurable_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IConfigurationManager_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IError_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IUTF8String_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/UTF8StringImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ArrayNodeImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ClientDOMParserWrapperImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ClientDOMSerializerWrapperImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/CompositeNodeImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/CoreObjectFactoryImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/DOMParserImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/DOMSerializerImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IArrayNode_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICompositeNode_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICoreConfigurationManager_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICoreObjectFactory_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMImplementationRegistry_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMParser_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMSerializer_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IMetadata_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INameSpacePrefixMap_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INodeIterator_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INode_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IPathSegment_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IPath_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ISimpleNode_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IStructureNode_I.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/MetadataConverterUtilsImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/MetadataImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/NameSpacePrefixMapImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/NodeImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/PathImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/PathSegmentImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/RDFDOMParserImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/StructureNodeImpl.cpp"
+ "PixelBufferTexture"
+ "PixelBufferTexture: malformed pixel buffer - bytesPerRow %zu < %u * %zu for format %s"
+ "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
+ "XMP_Enforce failed: (amountRead == count) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
+ "XMP_Enforce failed: (itemIndex < arraySize) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
+ "XMP_Enforce failed: (itemIndex <= arraySize) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
+ "XMP_Enforce failed: (length <= this->currLength) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
+ "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
+ "XMP_Enforce failed: (newOffset >= 0) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
+ "XMP_Enforce failed: (nsFound) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
+ "XMP_Enforce failed: (rdfString != 0) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
+ "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pwwlHM/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
+ "☀️ Using subsample factor: %u (%zu px)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/AutoSharedLock.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/ConfigurableImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/ErrorImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IConfigurable_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IConfigurationManager_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IError_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/IUTF8String_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCommon/source/UTF8StringImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ArrayNodeImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ClientDOMParserWrapperImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ClientDOMSerializerWrapperImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/CompositeNodeImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/CoreObjectFactoryImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/DOMParserImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/DOMSerializerImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IArrayNode_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICompositeNode_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICoreConfigurationManager_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ICoreObjectFactory_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMImplementationRegistry_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMParser_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IDOMSerializer_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IMetadata_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INameSpacePrefixMap_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INodeIterator_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/INode_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IPathSegment_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IPath_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ISimpleNode_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/IStructureNode_I.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/MetadataConverterUtilsImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/MetadataImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/NameSpacePrefixMapImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/NodeImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/PathImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/PathSegmentImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/RDFDOMParserImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/StructureNodeImpl.cpp"
- "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
- "XMP_Enforce failed: (amountRead == count) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
- "XMP_Enforce failed: (itemIndex < arraySize) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
- "XMP_Enforce failed: (itemIndex <= arraySize) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
- "XMP_Enforce failed: (length <= this->currLength) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
- "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
- "XMP_Enforce failed: (newOffset >= 0) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
- "XMP_Enforce failed: (nsFound) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
- "XMP_Enforce failed: (rdfString != 0) in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
- "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n51voX/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
- "☀️ Using subsample factor: %u (%u px)"
```
