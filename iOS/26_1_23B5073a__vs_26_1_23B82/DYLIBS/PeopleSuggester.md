## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1924.7.0.0.0
-  __TEXT.__text: 0xed714
+1924.7.1.0.0
+  __TEXT.__text: 0xed570
   __TEXT.__auth_stubs: 0xf90
   __TEXT.__objc_methlist: 0x982c
   __TEXT.__const: 0x8b8
   __TEXT.__gcc_except_tab: 0x2e1c
-  __TEXT.__cstring: 0xa6b4
-  __TEXT.__oslogstring: 0xb8ea
+  __TEXT.__cstring: 0xa996
+  __TEXT.__oslogstring: 0xb8ec
   __TEXT.__dlopen_cstrs: 0x17f0
   __TEXT.__ustring: 0x33e
-  __TEXT.__unwind_info: 0x2aa0
+  __TEXT.__unwind_info: 0x2a98
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x1127
-  __TEXT.__objc_methname: 0x21222
+  __TEXT.__objc_methname: 0x21232
   __TEXT.__objc_methtype: 0x26b6
-  __TEXT.__objc_stubs: 0x12940
-  __DATA_CONST.__got: 0x8d0
-  __DATA_CONST.__const: 0x36e8
+  __TEXT.__objc_stubs: 0x12960
+  __DATA_CONST.__got: 0x8d8
+  __DATA_CONST.__const: 0x36c0
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0xcb8
   __AUTH_CONST.__auth_got: 0x7d8
-  __AUTH_CONST.__const: 0x1a00
-  __AUTH_CONST.__cfstring: 0xb6c0
+  __AUTH_CONST.__const: 0x19e0
+  __AUTH_CONST.__cfstring: 0xb660
   __AUTH_CONST.__objc_const: 0x12b90
-  __AUTH_CONST.__objc_intobj: 0x1158
+  __AUTH_CONST.__objc_intobj: 0x1128
   __AUTH_CONST.__objc_arrayobj: 0x828
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_dictobj: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6BB4BEAE-C7F6-3276-9D20-0856DCB8699F
-  Functions: 4535
-  Symbols:   15853
-  CStrings:  9071
+  UUID: 960CE527-EFBD-3262-9A2D-7D5D4C6550F1
+  Functions: 4534
+  Symbols:   15851
+  CStrings:  9066
 
Symbols:
+ -[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:].cold.1
+ -[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:].cold.2
+ _OBJC_CLASS_$_BMSQLDatabase
+ _objc_msgSend$executeQuery:
+ _objc_msgSend$featureNames
+ _objc_msgSend$next
+ _objc_msgSend$row
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:options:range:
- ___65-[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:]_block_invoke
- ___65-[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:]_block_invoke_2
- ___65-[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:]_block_invoke_3
- ___block_descriptor_40_e8_32s_e22_B16?0"BMStoreEvent"8ls32l8
- _objc_msgSend$Intent
- _objc_msgSend$dictionaryWithObjectsAndKeys:
- _objc_msgSend$intentClass
- _objc_msgSend$interactionDirection
CStrings:
+ "'"
+ "''"
+ "Error getting features for handle %@"
+ "SELECT    intentClass,    bundleId,    groupIdentifier,    COALESCE(%d - MAX(CASE WHEN interactionDirection = 2 THEN absoluteTimestamp END), -1) AS %@,    COALESCE(%d - MAX(CASE WHEN interactionDirection = 3 THEN absoluteTimestamp END), -1) AS %@,    COUNT(CASE WHEN interactionDirection = 2 THEN 1 END) AS %@,    COUNT(CASE WHEN interactionDirection = 3 THEN 1 END) AS %@ FROM    \"App.Intent\" WHERE\n    (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'iMessage;-;%@') OR (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'SMS;-;%@') OR (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'RCS;-;%@') OR (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'any;-;%@') OR (intentClass = 'INStartCallIntent'    AND groupIdentifier = '%@') GROUP BY    groupIdentifier;"
+ "executeQuery:"
+ "next"
+ "query = %@"
+ "row"
+ "stringByReplacingOccurrencesOfString:withString:options:range:"
- "Computing interaction features for handle: %@"
- "INSendMessageIntent"
- "INStartCallIntent"
- "Intent"
- "RCS;-;%@"
- "SMS;-;%@"
- "any;-;%@"
- "dictionaryWithObjectsAndKeys:"
- "iMessage;-;%@"
- "intentClass"
- "interactionDirection"

```
