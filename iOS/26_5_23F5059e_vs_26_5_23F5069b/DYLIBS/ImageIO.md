## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.5.2.0.0
-  __TEXT.__text: 0x44959c
+2784.5.3.0.0
+  __TEXT.__text: 0x4495c0
   __TEXT.__auth_stubs: 0x4270
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x31578

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0BFC1AF4-3A1C-3C6D-8B40-C07AD486BCC0
+  UUID: E7989B0A-0717-3595-BABC-133673DC0BF6
   Functions: 15481
   Symbols:   47079
   CStrings:  24891
Functions:
~ __ZN2nv17DecompressETC_EACEN4nvtt6FormatEjjPvlPf : 804 -> 828
~ __ZN13ETCReadPlugin10initializeEP13IIODictionary : 1736 -> 1748
CStrings:
+ "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
+ "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
+ "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
+ "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
+ "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
+ "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
+ "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
+ "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
+ "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
+ "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/4F53DF72-4656-4C13-A41D-82C8D8379E2F/TemporaryDirectory.nk3xmp/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
- "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/19AE0533-9012-4828-AF8D-A5DB5E73C336/TemporaryDirectory.Oe6wHb/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
- "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/19AE0533-9012-4828-AF8D-A5DB5E73C336/TemporaryDirectory.Oe6wHb/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
- "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/19AE0533-9012-4828-AF8D-A5DB5E73C336/TemporaryDirectory.Oe6wHb/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
- "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/19AE0533-9012-4828-AF8D-A5DB5E73C336/TemporaryDirectory.Oe6wHb/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
- "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/19AE0533-9012-4828-AF8D-A5DB5E73C336/TemporaryDirectory.Oe6wHb/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
- "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/19AE0533-9012-4828-AF8D-A5DB5E73C336/TemporaryDirectory.Oe6wHb/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
- "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/19AE0533-9012-4828-AF8D-A5DB5E73C336/TemporaryDirectory.Oe6wHb/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
- "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/19AE0533-9012-4828-AF8D-A5DB5E73C336/TemporaryDirectory.Oe6wHb/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
- "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/19AE0533-9012-4828-AF8D-A5DB5E73C336/TemporaryDirectory.Oe6wHb/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
- "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/19AE0533-9012-4828-AF8D-A5DB5E73C336/TemporaryDirectory.Oe6wHb/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"

```
