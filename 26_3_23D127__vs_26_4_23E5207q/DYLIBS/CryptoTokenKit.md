## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`

```diff

-805.80.2.0.0
-  __TEXT.__text: 0x4742c
-  __TEXT.__auth_stubs: 0xd80
+805.100.40.0.0
+  __TEXT.__text: 0x487c8
+  __TEXT.__auth_stubs: 0xd00
   __TEXT.__delay_helper: 0x1f0
-  __TEXT.__objc_methlist: 0x454c
-  __TEXT.__gcc_except_tab: 0x1670
-  __TEXT.__const: 0x298
-  __TEXT.__cstring: 0x2bd8
+  __TEXT.__objc_methlist: 0x4604
+  __TEXT.__gcc_except_tab: 0x15fc
+  __TEXT.__const: 0x2a0
+  __TEXT.__cstring: 0x2ce6
   __TEXT.__oslogstring: 0x3487
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__swift5_typeref: 0x2a
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x16f8
+  __TEXT.__unwind_info: 0x1788
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0xc19
-  __TEXT.__objc_methname: 0x8b7e
-  __TEXT.__objc_methtype: 0x21aa
-  __TEXT.__objc_stubs: 0x6820
-  __DATA_CONST.__got: 0x5e0
+  __TEXT.__objc_methname: 0x8d28
+  __TEXT.__objc_methtype: 0x220b
+  __TEXT.__objc_stubs: 0x6980
+  __DATA_CONST.__got: 0x5e8
   __DATA_CONST.__const: 0x16e0
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2100
+  __DATA_CONST.__objc_selrefs: 0x2160
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__auth_got: 0x690
   __AUTH_CONST.__const: 0xb18
-  __AUTH_CONST.__cfstring: 0x2560
+  __AUTH_CONST.__cfstring: 0x2580
   __AUTH_CONST.__objc_const: 0x8618
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: DD2A6944-D880-3084-B11F-9FDCBB05D8B0
-  Functions: 1960
-  Symbols:   6953
-  CStrings:  3070
+  UUID: CCA237B8-F5CA-35CE-B0A0-58C31B134673
+  Functions: 2017
+  Symbols:   7148
+  CStrings:  3090
 
Symbols:
+ +[TKBERTLVRecord isEndOfContentMarkerAtSource:]
+ +[TKBERTLVRecord parseChildTLVRecordFromSource:nestingLevel:]
+ +[TKBERTLVRecord parseFromDataSource:nestingLevel:]
+ +[TKBERTLVRecord parseIndefiniteLengthValueFromDataSource:nestingLevel:]
+ +[TKBERTLVRecord parseLongFormValueFromDataSource:lengthByte:]
+ +[TKBERTLVRecord parseShortFormValueFromDataSource:length:]
+ +[TKBERTLVRecord parseTagFromDataSource:tag:]
+ +[TKBERTLVRecord parseValueFromDataSource:]
+ +[TKBERTLVRecord parseValueFromDataSource:nestingLevel:]
+ +[TKBERTLVRecord validateIndefiniteLengthBounds:]
+ +[TKCompactTLVRecord parseFromDataSource:nestingLevel:]
+ +[TKSimpleTLVRecord parseFromDataSource:]
+ +[TKSimpleTLVRecord parseFromDataSource:nestingLevel:]
+ +[TKTLVRecord parseFromDataSource:nestingLevel:]
+ +[TKTLVRecord sequenceOfRecordsFromData:nestingLevel:]
+ -[TKDataSource fetchByte:]
+ GCC_except_table38
+ _NSRangeException
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_65
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$isEndOfContentMarkerAtSource:
+ _objc_msgSend$parseChildTLVRecordFromSource:nestingLevel:
+ _objc_msgSend$parseFromDataSource:nestingLevel:
+ _objc_msgSend$parseIndefiniteLengthValueFromDataSource:nestingLevel:
+ _objc_msgSend$parseLongFormValueFromDataSource:lengthByte:
+ _objc_msgSend$parseShortFormValueFromDataSource:length:
+ _objc_msgSend$parseTagFromDataSource:tag:
+ _objc_msgSend$parseValueFromDataSource:nestingLevel:
+ _objc_msgSend$sequenceOfRecordsFromData:nestingLevel:
+ _objc_msgSend$validateIndefiniteLengthBounds:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "+[TKTLVRecord parseFromDataSource:nestingLevel:]"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "Attempt to read beyond data bounds"
+ "B24@0:8*16"
+ "B32@0:8@16Q24"
+ "B32@0:8@16^Q24"
+ "fetchByte:"
+ "isEndOfContentMarkerAtSource:"
+ "parseChildTLVRecordFromSource:nestingLevel:"
+ "parseFromDataSource:nestingLevel:"
+ "parseIndefiniteLengthValueFromDataSource:nestingLevel:"
+ "parseLongFormValueFromDataSource:lengthByte:"
+ "parseShortFormValueFromDataSource:length:"
+ "parseTagFromDataSource:tag:"
+ "parseValueFromDataSource:"
+ "parseValueFromDataSource:nestingLevel:"
+ "sequenceOfRecordsFromData:nestingLevel:"
+ "validateIndefiniteLengthBounds:"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"

```
