## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.5.4.0.0
-  __TEXT.__text: 0x44928c
-  __TEXT.__auth_stubs: 0x4270
-  __TEXT.__objc_methlist: 0xd20
-  __TEXT.__const: 0x31578
-  __TEXT.__gcc_except_tab: 0x26584
+2784.6.1.0.0
+  __TEXT.__text: 0x4493d4
+  __TEXT.__auth_stubs: 0x4280
+  __TEXT.__objc_methlist: 0xd58
+  __TEXT.__const: 0x31588
+  __TEXT.__gcc_except_tab: 0x2657c
   __TEXT.__cstring: 0x9e0af
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xed28
+  __TEXT.__unwind_info: 0xed30
   __TEXT.__eh_frame: 0x3d0
-  __TEXT.__objc_classname: 0xe0
-  __TEXT.__objc_methname: 0x2e5a
-  __TEXT.__objc_methtype: 0x24c0
-  __TEXT.__objc_stubs: 0x25c0
+  __TEXT.__objc_classname: 0xf1
+  __TEXT.__objc_methname: 0x2e87
+  __TEXT.__objc_methtype: 0x24db
+  __TEXT.__objc_stubs: 0x25e0
   __DATA_CONST.__got: 0x608
   __DATA_CONST.__const: 0x4c1a8
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb20
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_selrefs: 0xb28
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x470
-  __AUTH_CONST.__auth_got: 0x2150
+  __AUTH_CONST.__auth_got: 0x2158
   __AUTH_CONST.__const: 0x3e198
   __AUTH_CONST.__cfstring: 0x35e20
-  __AUTH_CONST.__objc_const: 0x1020
+  __AUTH_CONST.__objc_const: 0x10f8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x320
+  __AUTH.__objc_data: 0x370
   __AUTH.__data: 0x1d0
-  __DATA.__objc_ivar: 0x9c
+  __DATA.__objc_ivar: 0xa4
   __DATA.__data: 0x2f58
   __DATA.__bss: 0x4f90
   __DATA.__common: 0x3928

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1CF2BE9A-F370-3744-8779-4AA79E616E39
-  Functions: 15479
-  Symbols:   47077
-  CStrings:  24890
+  UUID: 7EF6DB09-FF01-3F84-8519-691345FEF171
+  Functions: 15484
+  Symbols:   47098
+  CStrings:  24897
 
Symbols:
+ -[IIORepeatedArray count]
+ -[IIORepeatedArray dealloc]
+ -[IIORepeatedArray initWithRepeatedObject:count:]
+ -[IIORepeatedArray objectAtIndex:]
+ _CGImageBlockSetGetColorSpace
+ _IIORepeatedArrayCreate
+ _OBJC_CLASS_$_IIORepeatedArray
+ _OBJC_IVAR_$_IIORepeatedArray._count
+ _OBJC_IVAR_$_IIORepeatedArray._object
+ _OBJC_METACLASS_$_IIORepeatedArray
+ _OBJC_METACLASS_$_NSArray
+ __OBJC_$_INSTANCE_METHODS_IIORepeatedArray
+ __OBJC_$_INSTANCE_VARIABLES_IIORepeatedArray
+ __OBJC_CLASS_RO_$_IIORepeatedArray
+ __OBJC_METACLASS_RO_$_IIORepeatedArray
+ _objc_msgSend$initWithRepeatedObject:count:
CStrings:
+ "@24@0:8Q16"
+ "@32@0:8@16Q24"
+ "IIORepeatedArray"
+ "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/BFCCCF39-B737-406A-8FC7-49A1B1D35BEC/TemporaryDirectory.UcLNuW/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
+ "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/BFCCCF39-B737-406A-8FC7-49A1B1D35BEC/TemporaryDirectory.UcLNuW/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
+ "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/BFCCCF39-B737-406A-8FC7-49A1B1D35BEC/TemporaryDirectory.UcLNuW/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
+ "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/BFCCCF39-B737-406A-8FC7-49A1B1D35BEC/TemporaryDirectory.UcLNuW/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
+ "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/BFCCCF39-B737-406A-8FC7-49A1B1D35BEC/TemporaryDirectory.UcLNuW/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
+ "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/BFCCCF39-B737-406A-8FC7-49A1B1D35BEC/TemporaryDirectory.UcLNuW/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
+ "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/BFCCCF39-B737-406A-8FC7-49A1B1D35BEC/TemporaryDirectory.UcLNuW/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
+ "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/BFCCCF39-B737-406A-8FC7-49A1B1D35BEC/TemporaryDirectory.UcLNuW/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
+ "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/BFCCCF39-B737-406A-8FC7-49A1B1D35BEC/TemporaryDirectory.UcLNuW/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
+ "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/BFCCCF39-B737-406A-8FC7-49A1B1D35BEC/TemporaryDirectory.UcLNuW/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
+ "_count"
+ "_object"
+ "initWithRepeatedObject:count:"
- "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
- "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
- "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
- "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
- "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
- "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
- "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
- "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
- "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
- "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"

```
