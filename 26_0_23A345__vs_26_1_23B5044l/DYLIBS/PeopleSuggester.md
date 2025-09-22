## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1924.1.2.0.0
-  __TEXT.__text: 0xed2e8
+1924.5.0.0.0
+  __TEXT.__text: 0xed67c
   __TEXT.__auth_stubs: 0xf90
   __TEXT.__objc_methlist: 0x9824
   __TEXT.__const: 0x8b8
   __TEXT.__gcc_except_tab: 0x2e1c
-  __TEXT.__cstring: 0xa984
-  __TEXT.__oslogstring: 0xb8ec
+  __TEXT.__cstring: 0xa6b4
+  __TEXT.__oslogstring: 0xb8ea
   __TEXT.__dlopen_cstrs: 0x17f0
   __TEXT.__ustring: 0x33e
-  __TEXT.__unwind_info: 0x2a80
+  __TEXT.__unwind_info: 0x2aa0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x1127
-  __TEXT.__objc_methname: 0x211a2
+  __TEXT.__objc_methname: 0x211d1
   __TEXT.__objc_methtype: 0x26b6
   __TEXT.__objc_stubs: 0x12920
-  __DATA_CONST.__got: 0x8d8
-  __DATA_CONST.__const: 0x36c0
+  __DATA_CONST.__got: 0x8d0
+  __DATA_CONST.__const: 0x36e8
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x62d0
+  __DATA_CONST.__objc_selrefs: 0x62d8
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0xcb8
   __AUTH_CONST.__auth_got: 0x7d8
-  __AUTH_CONST.__const: 0x19a0
-  __AUTH_CONST.__cfstring: 0xb620
+  __AUTH_CONST.__const: 0x1a00
+  __AUTH_CONST.__cfstring: 0xb6c0
   __AUTH_CONST.__objc_const: 0x12b60
-  __AUTH_CONST.__objc_intobj: 0x1128
+  __AUTH_CONST.__objc_intobj: 0x1158
   __AUTH_CONST.__objc_arrayobj: 0x828
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x7d0
   __DATA.__objc_ivar: 0xd34
   __DATA.__data: 0x3c8
-  __DATA.__bss: 0x5e0
+  __DATA.__bss: 0x600
   __DATA_DIRTY.__objc_data: 0x2760
   __DATA_DIRTY.__bss: 0x8b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8979F04D-6A75-3634-9250-CABEAA02215C
-  Functions: 4528
-  Symbols:   15830
-  CStrings:  9057
+  UUID: CD53CFA5-6AE2-360D-9F00-9546B6623C11
+  Functions: 4534
+  Symbols:   15849
+  CStrings:  9068
 
Symbols:
+ -[AeroMLTracerSpan emitPETEvent].cold.1
+ ___32-[AeroMLTracerSpan emitPETEvent]_block_invoke
+ ___32-[AeroMLTracerSpan emitPETEvent]_block_invoke_2
+ ___32-[AeroMLTracerSpan emitPETEvent]_block_invoke_2.cold.1
+ ___32-[AeroMLTracerSpan emitPETEvent]_block_invoke_3
+ ___65-[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:]_block_invoke
+ ___65-[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:]_block_invoke_2
+ ___65-[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e22_B16?0"BMStoreEvent"8ls32l8
+ _emitPETEvent._pasExprOnceResult
+ _emitPETEvent._pasOnceToken24
+ _kSqlEventFired_block_invoke._pasExprOnceResult
+ _kSqlEventFired_block_invoke._pasOnceToken25
+ _objc_msgSend$Intent
+ _objc_msgSend$dictionaryWithObjectsAndKeys:
+ _objc_msgSend$intentClass
+ _objc_msgSend$interactionDirection
- -[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:].cold.1
- -[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:].cold.2
- _OBJC_CLASS_$_BMSQLDatabase
- _objc_msgSend$executeQuery:
- _objc_msgSend$featureNames
- _objc_msgSend$next
- _objc_msgSend$row
CStrings:
+ "Computing interaction features for handle: %@"
+ "INSendMessageIntent"
+ "INStartCallIntent"
+ "Intent"
+ "RCS;-;%@"
+ "SMS;-;%@"
+ "any;-;%@"
+ "dictionaryWithObjectsAndKeys:"
+ "iMessage;-;%@"
+ "intentClass"
+ "interactionDirection"
- "Error getting features for handle %@"
- "SELECT    intentClass,    bundleId,    groupIdentifier,    COALESCE(%d - MAX(CASE WHEN interactionDirection = 2 THEN absoluteTimestamp END), -1) AS %@,    COALESCE(%d - MAX(CASE WHEN interactionDirection = 3 THEN absoluteTimestamp END), -1) AS %@,    COUNT(CASE WHEN interactionDirection = 2 THEN 1 END) AS %@,    COUNT(CASE WHEN interactionDirection = 3 THEN 1 END) AS %@ FROM    \"App.Intent\" WHERE\n    (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'iMessage;-;%@') OR (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'SMS;-;%@') OR (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'RCS;-;%@') OR (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'any;-;%@') OR (intentClass = 'INStartCallIntent'    AND groupIdentifier = '%@') GROUP BY    groupIdentifier;"
- "executeQuery:"
- "next"
- "query = %@"
- "row"

```
