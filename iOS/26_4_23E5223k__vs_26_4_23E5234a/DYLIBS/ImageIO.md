## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.4.7.0.0
-  __TEXT.__text: 0x4491c8
+2784.4.10.0.0
+  __TEXT.__text: 0x448940
   __TEXT.__auth_stubs: 0x4240
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x31578
-  __TEXT.__gcc_except_tab: 0x26574
-  __TEXT.__cstring: 0x9e02e
+  __TEXT.__gcc_except_tab: 0x26530
+  __TEXT.__cstring: 0x9dfc7
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xed50
+  __TEXT.__unwind_info: 0xed18
   __TEXT.__eh_frame: 0x3d0
   __TEXT.__objc_classname: 0xe0
   __TEXT.__objc_methname: 0x2e13

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: ED388253-24B1-3802-8928-70BFD7823B94
-  Functions: 15477
-  Symbols:   47054
-  CStrings:  24869
+  UUID: 17B4FCC8-B2A2-3A66-90DB-35F0841C366D
+  Functions: 15465
+  Symbols:   47027
+  CStrings:  24866
 
Symbols:
+ __ZN14WebPReadPlugin18decodeAnimatedWebPEP8WebPDataPhm
- _WebPAnimDecoderRestoreCanvas
- _WebPAnimDecoderSkipFrame
- __ZL21releaseGlobalWebPInfoPv
- __ZN14GlobalWebPInfo14setFrameBufferEPhmjjj
- __ZN14GlobalWebPInfo15copyFrameBufferEPPhPmPj
- __ZN14GlobalWebPInfo16clearFrameBufferEv
- __ZN14GlobalWebPInfo19hasValidFrameBufferEj
- __ZN14GlobalWebPInfoD2Ev
- __ZN14WebPReadPlugin24copyDecodedFrameToBufferEPhS0_jjji
- __ZN14WebPReadPlugin27decodeAnimatedWebPOptimizedEP8WebPDataPhm
- __ZNK14GlobalWebPInfo19getCachedFrameIndexEv
CStrings:
+ "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/14462E0D-9CE1-4CD1-9182-3A06FA3C6A20/TemporaryDirectory.w9lpCC/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
+ "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/14462E0D-9CE1-4CD1-9182-3A06FA3C6A20/TemporaryDirectory.w9lpCC/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
+ "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/14462E0D-9CE1-4CD1-9182-3A06FA3C6A20/TemporaryDirectory.w9lpCC/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
+ "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/14462E0D-9CE1-4CD1-9182-3A06FA3C6A20/TemporaryDirectory.w9lpCC/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
+ "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/14462E0D-9CE1-4CD1-9182-3A06FA3C6A20/TemporaryDirectory.w9lpCC/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
+ "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/14462E0D-9CE1-4CD1-9182-3A06FA3C6A20/TemporaryDirectory.w9lpCC/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
+ "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/14462E0D-9CE1-4CD1-9182-3A06FA3C6A20/TemporaryDirectory.w9lpCC/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
+ "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/14462E0D-9CE1-4CD1-9182-3A06FA3C6A20/TemporaryDirectory.w9lpCC/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
+ "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/14462E0D-9CE1-4CD1-9182-3A06FA3C6A20/TemporaryDirectory.w9lpCC/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
+ "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/14462E0D-9CE1-4CD1-9182-3A06FA3C6A20/TemporaryDirectory.w9lpCC/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
+ "decodeAnimatedWebP"
- "*** ERROR: invalid canvas size %dx%d\n"
- "*** ERROR: setFrameBuffer - bailing out\n"
- "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
- "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
- "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
- "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
- "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
- "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
- "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
- "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
- "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
- "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/C7270653-6719-41EE-A14F-CA9F28239C79/TemporaryDirectory.ft0Mjs/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
- "decodeAnimatedWebPOptimized"
- "setFrameBuffer"

```
