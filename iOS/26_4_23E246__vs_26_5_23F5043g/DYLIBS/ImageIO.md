## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.4.10.0.0
-  __TEXT.__text: 0x448940
+2784.5.1.0.0
+  __TEXT.__text: 0x448988
   __TEXT.__auth_stubs: 0x4240
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x31578
-  __TEXT.__gcc_except_tab: 0x26530
+  __TEXT.__gcc_except_tab: 0x2653c
   __TEXT.__cstring: 0x9dfc7
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30

   __TEXT.__objc_methtype: 0x24c0
   __TEXT.__objc_stubs: 0x2580
   __DATA_CONST.__got: 0x608
-  __DATA_CONST.__const: 0x4c168
+  __DATA_CONST.__const: 0x4c180
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A7A1EDD0-F349-3E7E-8713-5AAA3995A5FB
+  UUID: DF35E16F-39A1-364D-9364-3CC77F4AB024
   Functions: 15465
   Symbols:   47027
   CStrings:  24866
Functions:
~ __ZN14TIFFReadPlugin10initializeEP13IIODictionary : 2928 -> 2948
~ __ZN11_JPEGWriter12processInputEv : 2280 -> 2332
CStrings:
+ "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
+ "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
+ "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
+ "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
+ "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
+ "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
+ "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
+ "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
+ "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
+ "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
- "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/7FD0E563-0A6D-4FB3-81A0-ADD9AA011008/TemporaryDirectory.ZZWAoU/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
- "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/7FD0E563-0A6D-4FB3-81A0-ADD9AA011008/TemporaryDirectory.ZZWAoU/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
- "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/7FD0E563-0A6D-4FB3-81A0-ADD9AA011008/TemporaryDirectory.ZZWAoU/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
- "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/7FD0E563-0A6D-4FB3-81A0-ADD9AA011008/TemporaryDirectory.ZZWAoU/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
- "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/7FD0E563-0A6D-4FB3-81A0-ADD9AA011008/TemporaryDirectory.ZZWAoU/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
- "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/7FD0E563-0A6D-4FB3-81A0-ADD9AA011008/TemporaryDirectory.ZZWAoU/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
- "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/7FD0E563-0A6D-4FB3-81A0-ADD9AA011008/TemporaryDirectory.ZZWAoU/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
- "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/7FD0E563-0A6D-4FB3-81A0-ADD9AA011008/TemporaryDirectory.ZZWAoU/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
- "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/7FD0E563-0A6D-4FB3-81A0-ADD9AA011008/TemporaryDirectory.ZZWAoU/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
- "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/7FD0E563-0A6D-4FB3-81A0-ADD9AA011008/TemporaryDirectory.ZZWAoU/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"

```
