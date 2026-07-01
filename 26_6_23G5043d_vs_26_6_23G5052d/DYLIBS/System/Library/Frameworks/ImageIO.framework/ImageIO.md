## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-  __TEXT.__text: 0x4497b8
+  __TEXT.__text: 0x44979c
   __TEXT.__auth_stubs: 0x4280
   __TEXT.__objc_methlist: 0xd58
   __TEXT.__const: 0x31588

   __TEXT.__cstring: 0x9e0ec
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xed40
+  __TEXT.__unwind_info: 0xed38
   __TEXT.__eh_frame: 0x3d0
   __TEXT.__objc_classname: 0xf1
   __TEXT.__objc_methname: 0x2e87

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15484
-  Symbols:   47099
+  Functions: 15483
+  Symbols:   47097
   CStrings:  24898
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
- __ZN12BCReadPlugin16decodeDXTCtoRGBXEP19IIOImageReadSessionP13vImage_Buffer16CGImageAlphaInfob.cold.1
Functions:
~ __ZN12BCReadPlugin16decodeDXTCtoRGBXEP19IIOImageReadSessionP13vImage_Buffer16CGImageAlphaInfob : 1148 -> 1164
+ __ZN10IIO_Reader12xpcInitImageEP17_xpc_connection_sPvS2_.cold.1
- __ZN10IIO_Reader12xpcInitImageEP17_xpc_connection_sPvS2_.cold.1
- _TIFFHashSetRemove.cold.1
CStrings:
+ "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/217BC4F1-2C9D-47DD-9B23-824E1B33BBF1/TemporaryDirectory.gwo8we/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
+ "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/217BC4F1-2C9D-47DD-9B23-824E1B33BBF1/TemporaryDirectory.gwo8we/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
+ "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/217BC4F1-2C9D-47DD-9B23-824E1B33BBF1/TemporaryDirectory.gwo8we/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
+ "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/217BC4F1-2C9D-47DD-9B23-824E1B33BBF1/TemporaryDirectory.gwo8we/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
+ "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/217BC4F1-2C9D-47DD-9B23-824E1B33BBF1/TemporaryDirectory.gwo8we/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
+ "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/217BC4F1-2C9D-47DD-9B23-824E1B33BBF1/TemporaryDirectory.gwo8we/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
+ "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/217BC4F1-2C9D-47DD-9B23-824E1B33BBF1/TemporaryDirectory.gwo8we/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
+ "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/217BC4F1-2C9D-47DD-9B23-824E1B33BBF1/TemporaryDirectory.gwo8we/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
+ "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/217BC4F1-2C9D-47DD-9B23-824E1B33BBF1/TemporaryDirectory.gwo8we/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
+ "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/217BC4F1-2C9D-47DD-9B23-824E1B33BBF1/TemporaryDirectory.gwo8we/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
- "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/0BE22CAA-5300-423B-8BC2-DAC5770D921A/TemporaryDirectory.ujyEHm/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
- "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/0BE22CAA-5300-423B-8BC2-DAC5770D921A/TemporaryDirectory.ujyEHm/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
- "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/0BE22CAA-5300-423B-8BC2-DAC5770D921A/TemporaryDirectory.ujyEHm/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
- "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/0BE22CAA-5300-423B-8BC2-DAC5770D921A/TemporaryDirectory.ujyEHm/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
- "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/0BE22CAA-5300-423B-8BC2-DAC5770D921A/TemporaryDirectory.ujyEHm/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
- "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/0BE22CAA-5300-423B-8BC2-DAC5770D921A/TemporaryDirectory.ujyEHm/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
- "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/0BE22CAA-5300-423B-8BC2-DAC5770D921A/TemporaryDirectory.ujyEHm/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
- "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/0BE22CAA-5300-423B-8BC2-DAC5770D921A/TemporaryDirectory.ujyEHm/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
- "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/0BE22CAA-5300-423B-8BC2-DAC5770D921A/TemporaryDirectory.ujyEHm/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
- "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/0BE22CAA-5300-423B-8BC2-DAC5770D921A/TemporaryDirectory.ujyEHm/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"

```
