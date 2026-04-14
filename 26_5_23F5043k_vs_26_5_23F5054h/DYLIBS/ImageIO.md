## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.5.1.0.0
-  __TEXT.__text: 0x448988
-  __TEXT.__auth_stubs: 0x4240
+2784.5.2.0.0
+  __TEXT.__text: 0x44959c
+  __TEXT.__auth_stubs: 0x4270
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x31578
-  __TEXT.__gcc_except_tab: 0x2653c
-  __TEXT.__cstring: 0x9dfc7
+  __TEXT.__gcc_except_tab: 0x26584
+  __TEXT.__cstring: 0x9e0f3
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xed18
+  __TEXT.__unwind_info: 0xed28
   __TEXT.__eh_frame: 0x3d0
   __TEXT.__objc_classname: 0xe0
-  __TEXT.__objc_methname: 0x2e13
+  __TEXT.__objc_methname: 0x2e5a
   __TEXT.__objc_methtype: 0x24c0
-  __TEXT.__objc_stubs: 0x2580
+  __TEXT.__objc_stubs: 0x25c0
   __DATA_CONST.__got: 0x608
-  __DATA_CONST.__const: 0x4c180
+  __DATA_CONST.__const: 0x4c1a8
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb10
+  __DATA_CONST.__objc_selrefs: 0xb20
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2138
-  __AUTH_CONST.__const: 0x3e178
-  __AUTH_CONST.__cfstring: 0x35d00
+  __DATA_CONST.__objc_arraydata: 0x470
+  __AUTH_CONST.__auth_got: 0x2150
+  __AUTH_CONST.__const: 0x3e198
+  __AUTH_CONST.__cfstring: 0x35e20
   __AUTH_CONST.__objc_const: 0x1020
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0x9c
-  __DATA.__data: 0x2f18
-  __DATA.__bss: 0x4f70
-  __DATA.__common: 0x3618
+  __DATA.__data: 0x2f58
+  __DATA.__bss: 0x4f90
+  __DATA.__common: 0x3928
   __DATA_DIRTY.__data: 0x168
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__common: 0xe03

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: DF35E16F-39A1-364D-9364-3CC77F4AB024
-  Functions: 15465
-  Symbols:   47027
-  CStrings:  24866
+  UUID: E9C0CDC0-BFF2-3841-89E2-7F9BBBE11ADF
+  Functions: 15481
+  Symbols:   47079
+  CStrings:  24891
 
Symbols:
+ _AnalyticsSendEventLazy
+ _IIO_CodesigningID
+ _IIO_HintedTypeIndex
+ _IIO_MatchingPluginIDs
+ _IIO_Number
+ _IIO_ReaderSelection
+ _IIO_RoutedPluginID
+ _UTI_AnalyticsEnum
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.11
+ __Z30IIOAnalyticsLogReaderSelectionPK10__CFStringj
+ __Z30IIOAnalyticsLogReaderSelectionPK10__CFStringj.cold.1
+ __Z30IIOAnalyticsLogReaderSelectionPK10__CFStringj.cold.2
+ __Z30IIOAnalyticsLogReaderSelectionPK10__CFStringj.cold.3
+ __ZL20sReaderSelectionLock
+ __ZL22sReaderSelectionCounts
+ __ZL24_iio_decode_history_lock
+ __ZN13EXRReadPlugin19decodeBlockAppleEXREPvm.cold.4
+ __ZN13EXRReadPlugin19decodeBlockAppleEXREPvm.cold.5
+ __ZN21IIODecodeHistoryScope20markDecodeSuccessfulEv
+ __ZN21IIODecodeHistoryScopeC1Ej7IIOMode
+ __ZN21IIODecodeHistoryScopeC2Ej7IIOMode
+ __ZN21IIODecodeHistoryScopeD1Ev
+ __ZN21IIODecodeHistoryScopeD2Ev
+ __ZNSt3__16chrono12system_clock3nowEv
+ __ZZL27IIOGetCodesigningIdentifiervE8cachedID
+ __ZZL27IIOGetCodesigningIdentifiervE9onceToken
+ ____Z30IIOAnalyticsLogReaderSelectionPK10__CFStringj_block_invoke
+ ____ZL27IIOGetCodesigningIdentifierv_block_invoke
+ ___block_descriptor_64_e8_32o40o48o_e19_"NSDictionary"8?0ls32l8s40l8s48l8
+ ___block_literal_global.392
+ __iio_decoded_image_history
+ __iio_decoded_image_history_oop
+ __iio_history_size
+ _csops
+ _objc_msgSend$initWithBytesNoCopy:length:encoding:freeWhenDone:
+ _objc_msgSend$unsignedIntegerValue
- _ERROR_ImageIO_DataBufferIsNotBigEnough
- __ZN10IIOScanner14validateBufferEPKc
CStrings:
+ "%@|%@"
+ "*** ERROR: Estimated texture data size exceeds available file data\n"
+ "*** too many bytes to allocate\n"
+ "@\"NSDictionary\"8@?0"
+ "IIOAnalytics.mm"
+ "IIOAnalyticsLogReaderSelection"
+ "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/B777E021-BAD9-40BA-8F43-268FDE41D60D/TemporaryDirectory.nQ3YUm/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
+ "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/B777E021-BAD9-40BA-8F43-268FDE41D60D/TemporaryDirectory.nQ3YUm/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
+ "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/B777E021-BAD9-40BA-8F43-268FDE41D60D/TemporaryDirectory.nQ3YUm/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
+ "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/B777E021-BAD9-40BA-8F43-268FDE41D60D/TemporaryDirectory.nQ3YUm/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
+ "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/B777E021-BAD9-40BA-8F43-268FDE41D60D/TemporaryDirectory.nQ3YUm/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
+ "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/B777E021-BAD9-40BA-8F43-268FDE41D60D/TemporaryDirectory.nQ3YUm/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
+ "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/B777E021-BAD9-40BA-8F43-268FDE41D60D/TemporaryDirectory.nQ3YUm/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
+ "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/B777E021-BAD9-40BA-8F43-268FDE41D60D/TemporaryDirectory.nQ3YUm/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
+ "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/B777E021-BAD9-40BA-8F43-268FDE41D60D/TemporaryDirectory.nQ3YUm/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
+ "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/B777E021-BAD9-40BA-8F43-268FDE41D60D/TemporaryDirectory.nQ3YUm/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"
+ "codesigningID"
+ "com.apple.ImageIO.readerSelection"
+ "hintedTypeIndex"
+ "initWithBytesNoCopy:length:encoding:freeWhenDone:"
+ "matchingPluginIDs"
+ "nil != codesignID"
+ "nil != routed"
+ "number"
+ "public.fax"
+ "routedPluginID"
+ "unsignedIntegerValue"
- "Checking ATX buffer"
- "XMP_Enforce failed: ((xmpParent->options & kXMP_PropValueIsStruct) && (! xmpParent->children.empty())) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 613"
- "XMP_Enforce failed: (amountRead == count) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 158"
- "XMP_Enforce failed: (itemIndex < arraySize) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-GetSet.cpp at line 1068"
- "XMP_Enforce failed: (itemIndex <= arraySize) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta2-GetSet.cpp at line 882"
- "XMP_Enforce failed: (length <= this->currLength) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 268"
- "XMP_Enforce failed: (memcmp( buffer, \"\\x47\\x49\\x46\\x38\\x39\\x61\", 6 ) == 0) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPFiles/source/FileHandlers/GIF_Handler.cpp at line 158"
- "XMP_Enforce failed: (newOffset >= 0) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/source/XMPFiles_IO.cpp at line 220"
- "XMP_Enforce failed: (nsFound) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 191"
- "XMP_Enforce failed: (rdfString != 0) in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/XMPMeta-Serialize.cpp at line 1212"
- "XMP_Enforce failed: (valueNode->name == \"rdf:value\") in /Library/Caches/com.apple.xbs/F823B64B-5772-4373-B9F6-465088DF899B/TemporaryDirectory.336sJg/Sources/ImageIO/XMP-Toolkit-SDK/XMPCore/source/ParseRDF.cpp at line 616"

```
