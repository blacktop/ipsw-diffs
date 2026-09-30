## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.5.3.0.0
-  __TEXT.__text: 0x4495c0
+2784.5.4.0.0
+  __TEXT.__text: 0x44928c
   __TEXT.__auth_stubs: 0x4270
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x31578
   __TEXT.__gcc_except_tab: 0x26584
-  __TEXT.__cstring: 0x9e0f3
+  __TEXT.__cstring: 0x9e0af
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
   __TEXT.__unwind_info: 0xed28

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E7989B0A-0717-3595-BABC-133673DC0BF6
-  Functions: 15481
-  Symbols:   47079
-  CStrings:  24891
+  UUID: 1CF2BE9A-F370-3744-8779-4AA79E616E39
+  Functions: 15479
+  Symbols:   47077
+  CStrings:  24890
 
Symbols:
- __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.11
Functions:
- sub_18642f8c0
~ __Z17ValidateKTXHeaderRK10_KTXHeadery : 1020 -> 404
- __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.11
CStrings:
+ "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
+ "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
+ "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
+ "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
+ "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
+ "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
+ "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
+ "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
+ "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
+ "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/2EED9C48-8A49-494A-B194-4BA23052EAB3/TemporaryDirectory.bPhODS/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
- "*** ERROR: Estimated texture data size exceeds available file data\n"
- "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
- "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
- "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
- "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
- "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
- "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
- "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
- "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
- "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
- "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"

```
