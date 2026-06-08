## BrailleTranslation

> `/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation`

```diff

-424.15.0.0.0
-  __TEXT.__text: 0x37a94
-  __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x1dcc
-  __TEXT.__const: 0xe18
-  __TEXT.__cstring: 0x836
-  __TEXT.__oslogstring: 0x58c
+455.1.1.0.0
+  __TEXT.__text: 0x31a7c
+  __TEXT.__objc_methlist: 0x1d1c
+  __TEXT.__const: 0xc30
+  __TEXT.__swift5_typeref: 0x22e
+  __TEXT.__constg_swiftt: 0xddc
+  __TEXT.__swift5_reflstr: 0x65f
+  __TEXT.__swift5_fieldmd: 0x434
+  __TEXT.__swift5_types: 0x20
+  __TEXT.__cstring: 0x7d8
+  __TEXT.__oslogstring: 0x552
   __TEXT.__gcc_except_tab: 0xe0
   __TEXT.__ustring: 0xc2
-  __TEXT.__swift5_typeref: 0x2be
-  __TEXT.__constg_swiftt: 0xf18
-  __TEXT.__swift5_reflstr: 0x66f
-  __TEXT.__swift5_fieldmd: 0x4e8
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__swift5_proto: 0x8
-  __TEXT.__unwind_info: 0xbb0
-  __TEXT.__eh_frame: 0xf8
-  __TEXT.__objc_classname: 0x54f
-  __TEXT.__objc_methname: 0x4883
-  __TEXT.__objc_methtype: 0xd1c
-  __TEXT.__objc_stubs: 0x31a0
-  __DATA_CONST.__got: 0x290
-  __DATA_CONST.__const: 0x338
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__unwind_info: 0xa50
+  __TEXT.__eh_frame: 0x40
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x590
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1190
-  __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_selrefs: 0x1168
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x138
-  __AUTH_CONST.__auth_got: 0x6f8
-  __AUTH_CONST.__const: 0x1010
-  __AUTH_CONST.__cfstring: 0x1140
-  __AUTH_CONST.__objc_const: 0x4378
+  __DATA_CONST.__got: 0x268
+  __AUTH_CONST.__const: 0x230
+  __AUTH_CONST.__cfstring: 0x1160
+  __AUTH_CONST.__objc_const: 0x33c8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x14a8
-  __AUTH.__data: 0x800
+  __AUTH_CONST.__auth_got: 0x718
+  __AUTH.__objc_data: 0x1230
+  __AUTH.__data: 0x7a0
   __DATA.__objc_ivar: 0x164
-  __DATA.__data: 0x6f8
-  __DATA.__bss: 0x200
-  __DATA.__common: 0x10
+  __DATA.__data: 0x600
+  __DATA.__bss: 0xe8
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 992E5954-B85D-3AEB-A95A-57A5307D2AC9
-  Functions: 1196
-  Symbols:   2169
-  CStrings:  1249
+  UUID: C34A4996-EBF8-3BD0-AD91-2E3CAAD33A84
+  Functions: 1086
+  Symbols:   2094
+  CStrings:  280
 
Symbols:
+ +[BRLTBrailleChar grade1EnglishLetterForBrailleChar:]
+ +[BRLTSTranslationService sharedTranslatorQueue]
+ +[BRLTTableEnumerator localizedNameForBrailleLanguage:userLocale:]
+ -[BRLTBrailleModel isInputEightDot]
+ -[BRLTBrailleModel resetEditState]
+ -[BRLTBrailleModel setEditGeneration:]
+ -[BRLTBrailleModel setEditableTextLineIndex:]
+ -[BRLTBrailleModel setSelectionExtendsBeyondLine:]
+ -[BRLTBrailleModel setSnapToPrintText:]
+ -[BRLTTranslationService setSyncQueue:]
+ -[BRLTTranslationService syncBrailleForText:parameters:]
+ -[BRLTTranslationService syncQueue]
+ -[BRLTTranslationService syncTextForPrintBraille:parameters:]
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table468
+ GCC_except_table67
+ GCC_except_table88
+ GCC_except_table93
+ _OBJC_IVAR_$_BRLTTranslationService._syncQueue
+ ___39-[BRLTTranslationService _queue_resume]_block_invoke.21
+ ___48+[BRLTSTranslationService sharedTranslatorQueue]_block_invoke
+ ___56-[BRLTTranslationService syncBrailleForText:parameters:]_block_invoke
+ ___56-[BRLTTranslationService syncBrailleForText:parameters:]_block_invoke_2
+ ___61-[BRLTTranslationService syncTextForPrintBraille:parameters:]_block_invoke
+ ___61-[BRLTTranslationService syncTextForPrintBraille:parameters:]_block_invoke_2
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_48_e8_32s40r_e29_v24?0"NSString"8"NSData"16lr40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8
+ ___block_literal_global.283
+ ___block_literal_global.325
+ ___block_literal_global.384
+ ___block_literal_global.462
+ ___block_literal_global.617
+ ___swift_memcpy48_8
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_BrailleTranslation
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_BrailleTranslation
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_BrailleTranslation
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _dispatch_time
+ _grade1EnglishLetterForBrailleChar:.mapping
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$didSetEditGeneration:
+ _objc_msgSend$dot7
+ _objc_msgSend$grade1EnglishLetterForBrailleChar:
+ _objc_msgSend$isInputEightDot
+ _objc_msgSend$resetEditState
+ _objc_msgSend$setEditGeneration:
+ _objc_msgSend$setEditableTextLineIndex:
+ _objc_msgSend$setSelectionExtendsBeyondLine:
+ _objc_msgSend$setSnapToPrintText:
+ _objc_msgSend$sharedTranslatorQueue
+ _objc_msgSend$supportsTranslationMode8Dot
+ _objc_msgSend$syncQueue
+ _objc_retain_x3
+ _objc_retain_x4
+ _sharedTranslatorQueue.onceToken
+ _sharedTranslatorQueue.sharedQueue
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _symbolic Su
- +[BRLTBrailleMusicParser sharedParser]
- +[BRLTBrailleString unicodeToBestEffortBrf:].cold.1
- +[BRLTTableEnumerator defaultTablesArrayForLocale:].cold.1
- +[BRLTTableEnumerator defaultTablesArrayForLocale:].cold.2
- +[BRLTTranslationService connectionsLock].cold.1
- +[BRLTTranslationService connections].cold.1
- +[BRLTTranslationService serviceForIdentifier:input:loopback:].cold.1
- -[BRLTBrailleMusicParser .cxx_destruct]
- -[BRLTBrailleMusicParser initWithUnderlyingObject:]
- -[BRLTBrailleMusicParser translate:]
- -[BRLTBrailleMusicParser underlyingObject]
- -[BRLTSTranslator translator].cold.1
- -[BRLTSTranslator translator].cold.2
- -[BRLTSTranslator translator].cold.3
- -[BRLTSTranslator translator].cold.4
- -[BRLTServiceTranslator initWithTable:].cold.1
- -[BRLTTableEnumerator translatorBundles].cold.1
- -[NSBundle(BRLTBrailleTables) brl_brailleTablesDictionary].cold.1
- GCC_except_table11
- GCC_except_table13
- GCC_except_table3
- GCC_except_table41
- GCC_except_table6
- _BRLTFirstPreferredLocale
- _BRLTLocalizedStringForKey
- _BRLTLog.cold.1
- _BRLTTranslationServiceClientInterface.cold.1
- _BRLTTranslationServiceInterface.cold.1
- _BRLTTranslatorClassIsValid.cold.1
- _OBJC_CLASS_$_BRLTBrailleMusicParser
- _OBJC_CLASS_$_BRLTBrailleMusicParserInternal
- _OBJC_CLASS_$_NSXMLParser
- _OBJC_IVAR_$_BRLTBrailleMusicParser._underlyingObject
- _OBJC_METACLASS_$_BRLTBrailleMusicParser
- _OBJC_METACLASS_$_BRLTBrailleMusicParserInternal
- _OBJC_METACLASS_$__TtCC18BrailleTranslation22BRLTBrailleMusicParserP33_E886CD66E288DBBFC574695449FA98EA20BrailleMusicDelegate
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- __CLASS_METHODS_BRLTBrailleMusicParserInternal
- __CLASS_PROPERTIES_BRLTBrailleMusicParserInternal
- __DATA_BRLTBrailleMusicParserInternal
- __DATA__TtCC18BrailleTranslation22BRLTBrailleMusicParserP33_E886CD66E288DBBFC574695449FA98EA20BrailleMusicDelegate
- __INSTANCE_METHODS_BRLTBrailleMusicParserInternal
- __INSTANCE_METHODS__TtCC18BrailleTranslation22BRLTBrailleMusicParserP33_E886CD66E288DBBFC574695449FA98EA20BrailleMusicDelegate
- __IVARS__TtCC18BrailleTranslation22BRLTBrailleMusicParserP33_E886CD66E288DBBFC574695449FA98EA20BrailleMusicDelegate
- __METACLASS_DATA_BRLTBrailleMusicParserInternal
- __METACLASS_DATA__TtCC18BrailleTranslation22BRLTBrailleMusicParserP33_E886CD66E288DBBFC574695449FA98EA20BrailleMusicDelegate
- __OBJC_$_CLASS_METHODS_BRLTBrailleMusicParser
- __OBJC_$_INSTANCE_METHODS_BRLTBrailleMusicParser
- __OBJC_$_INSTANCE_VARIABLES_BRLTBrailleMusicParser
- __OBJC_$_PROP_LIST_BRLTBrailleMusicParser
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXMLParserDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSXMLParserDelegate
- __OBJC_$_PROTOCOL_REFS_NSXMLParserDelegate
- __OBJC_CLASS_RO_$_BRLTBrailleMusicParser
- __OBJC_LABEL_PROTOCOL_$_NSXMLParserDelegate
- __OBJC_METACLASS_RO_$_BRLTBrailleMusicParser
- __OBJC_PROTOCOL_$_NSXMLParserDelegate
- __PROTOCOLS__TtCC18BrailleTranslation22BRLTBrailleMusicParserP33_E886CD66E288DBBFC574695449FA98EA20BrailleMusicDelegate
- __PROTOCOLS__TtCC18BrailleTranslation22BRLTBrailleMusicParserP33_E886CD66E288DBBFC574695449FA98EA20BrailleMusicDelegate.13
- ___39-[BRLTTranslationService _queue_resume]_block_invoke.19
- ___39-[BRLTTranslationService _queue_resume]_block_invoke.19.cold.1
- ___45-[BRLTTranslationService _queue_serviceProxy]_block_invoke.cold.1
- ___60-[NSBundle(BRLTBrailleTables) brl_supportedTablesForLocale:]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___exp10
- ___swift_memcpy40_8
- ___swift_memcpy49_8
- __swiftEmptyDictionarySingleton
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_BrailleTranslation
- __swift_FORCE_LOAD_$_swiftNaturalLanguage
- __swift_FORCE_LOAD_$_swiftNaturalLanguage_$_BrailleTranslation
- __swift_dead_method_stub
- __unionRangeIgnoringNotFound
- _associated conformance 18BrailleTranslation4NoteVSHAASQ
- _log10
- _objc_msgSend$initWithData:
- _objc_msgSend$parse
- _objc_msgSend$translate:
- _symbolic SS_SSt
- _symbolic SaySay_____GG 18BrailleTranslation4NoteV
- _symbolic Say_____G 18BrailleTranslation4NoteV
- _symbolic SiSg
- _symbolic _____ 18BrailleTranslation22BRLTBrailleMusicParserC
- _symbolic _____ 18BrailleTranslation22BRLTBrailleMusicParserC0aD8Delegate33_E886CD66E288DBBFC574695449FA98EALLC
- _symbolic _____ 18BrailleTranslation4NoteV
- _symbolic _____Sg 18BrailleTranslation4NoteV
- _symbolic _____Sg_ABt 18BrailleTranslation4NoteV
- _symbolic _____yS2SG s18_DictionaryStorageC
- _symbolic _____ySay_____GG s23_ContiguousArrayStorageC 18BrailleTranslation4NoteV
- _symbolic _____ySsG s23_ContiguousArrayStorageC
- _symbolic _____y_____G s23_ContiguousArrayStorageC 18BrailleTranslation4NoteV
- _symbolic _____yypG s23_ContiguousArrayStorageC
- _type_layout_string 18BrailleTranslation4NoteV
CStrings:
+ "%c"
+ "com.apple.BrailleTranslation.Sync"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<BRLTBrailleModelDelegate>\""
- "@\"<BRLTBrailleStateManagerDelegate>\""
- "@\"<BRLTBrailleTranslationDelegateProtocol>\""
- "@\"<BRLTTranslatorProtocol>\""
- "@\"BRLTBrailleBuffer\""
- "@\"BRLTBrailleModelInternal\""
- "@\"BRLTBrailleMusicParserInternal\""
- "@\"BRLTBrailleString\""
- "@\"BRLTEditStringInternal\""
- "@\"BRLTSLoopbackTranslationService\""
- "@\"BRLTSTranslator\""
- "@\"BRLTScriptString\""
- "@\"BRLTTable\""
- "@\"BRLTTextFormattingRanges\""
- "@\"NSArray\""
- "@\"NSBundle\""
- "@\"NSData\"40@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32"
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSRecursiveLock\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"40@0:8@\"NSString\"16Q24^@32"
- "@\"NSString\"44@0:8@\"NSString\"16^@24B32@\"BRLTTextFormattingRanges\"36"
- "@\"NSString\"64@0:8@\"NSString\"16Q24^@32{_NSRange=QQ}40@\"BRLTTextFormattingRanges\"56"
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8C16"
- "@20@0:8S16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16B24B28"
- "@32@0:8@16o^@24"
- "@32@0:8@16q24"
- "@36@0:8@16B24@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24o^@32"
- "@40@0:8@16Q24^@32"
- "@40@0:8@16{_NSRange=QQ}24"
- "@40@0:8q16@24q32"
- "@40@0:8{_NSRange=QQ}16q32"
- "@44@0:8@16^@24B32@36"
- "@64@0:8@16Q24B32B36{_NSRange=QQ}40@56"
- "@64@0:8@16Q24^@32{_NSRange=QQ}40@56"
- "@64@0:8@16{_NSRange=QQ}24{_NSRange=QQ}40Q56"
- "@88@0:8@16{_NSRange=QQ}24{_NSRange=QQ}40q56{_NSRange=QQ}64@80"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B32@0:8{_NSRange=QQ}16"
- "B40@0:8{_NSRange=QQ}16o^Q32"
- "BRLTBrailleBuffer"
- "BRLTBrailleChar"
- "BRLTBrailleModel"
- "BRLTBrailleModelDelegate"
- "BRLTBrailleModelInternal"
- "BRLTBrailleMusicParser"
- "BRLTBrailleMusicParserInternal"
- "BRLTBrailleStateManager"
- "BRLTBrailleString"
- "BRLTBrailleTables"
- "BRLTBrailleUIFormattingOptions"
- "BRLTEditString"
- "BRLTEditStringInternal"
- "BRLTEmojiPrintPreprocessor"
- "BRLTJJapaneseProcessor"
- "BRLTJMecabraWrapper"
- "BRLTLoopbackTranslationService"
- "BRLTPreprocessorHelper"
- "BRLTPrintPreprocessor"
- "BRLTSLoopbackTranslationService"
- "BRLTSTranslationService"
- "BRLTSTranslator"
- "BRLTScriptString"
- "BRLTServiceTranslator"
- "BRLTTable"
- "BRLTTableEnumerator"
- "BRLTTableIdentifier"
- "BRLTTextFormattingRanges"
- "BRLTTokenRange"
- "BRLTTranslationParameters"
- "BRLTTranslationService"
- "BRLTTranslationServiceClientInterface"
- "BRLTTranslationServiceInterface"
- "BRLTTranslator"
- "BRLTTranslatorProtocol"
- "BRLTUnicodePrintPreprocessor"
- "C"
- "C16@0:8"
- "Failed to form a unicode scalar from "
- "NSCoding"
- "NSContiguousBrailleRange"
- "NSCopying"
- "NSFocus"
- "NSObject"
- "NSSecureCoding"
- "NSSelection"
- "NSSuggestion"
- "NSXMLParserDelegate"
- "NSXPCListenerDelegate"
- "Q"
- "Q16@0:8"
- "Q24@0:8Q16"
- "T#,R"
- "T@\"<BRLTBrailleModelDelegate>\",N,&,Vdelegate"
- "T@\"<BRLTTranslatorProtocol>\",R,N,V_translator"
- "T@\"BRLTBrailleBuffer\",R,N"
- "T@\"BRLTBrailleModelInternal\",N,R"
- "T@\"BRLTBrailleModelInternal\",R,V_underlyingObject"
- "T@\"BRLTBrailleMusicParserInternal\",N,R"
- "T@\"BRLTBrailleMusicParserInternal\",R,V_underlyingObject"
- "T@\"BRLTBrailleString\",R,N"
- "T@\"BRLTEditStringInternal\",N,R"
- "T@\"BRLTEditStringInternal\",R,V_underlyingObject"
- "T@\"BRLTSLoopbackTranslationService\",&,N,V_loopbackService"
- "T@\"BRLTSTranslator\",&,N,V_queueTranslator"
- "T@\"BRLTSTranslator\",&,N,V_translator"
- "T@\"BRLTTable\",R,N,V_table"
- "T@\"BRLTTextFormattingRanges\",&,N,V_textFormattingRanges"
- "T@\"BRLTTextFormattingRanges\",R,N,V_textFormattingRanges"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_translatorBundles"
- "T@\"NSBundle\",&,N,V_bundle"
- "T@\"NSBundle\",R,N"
- "T@\"NSBundle\",R,N,V_bundle"
- "T@\"NSMutableArray\",&,N,V_boldRanges"
- "T@\"NSMutableArray\",&,N,V_italicRanges"
- "T@\"NSMutableArray\",&,N,V_tokenRanges"
- "T@\"NSMutableArray\",&,N,V_underlineRanges"
- "T@\"NSMutableDictionary\",&,N,V_languageAgnosticIdentifiersToTables"
- "T@\"NSMutableDictionary\",R"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSSet\",R,N"
- "T@\"NSSet\",R,N,V_supportedLanguageLocales"
- "T@\"NSSet\",R,N,V_supportedLocales"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_translatorBundlePath"
- "T@\"NSString\",N,R"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_language"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_language"
- "T@\"NSString\",R,N,V_serviceIdentifier"
- "T@\"NSString\",R,N,V_string"
- "T@\"NSString\",R,N,V_variant"
- "T@\"NSXPCConnection\",&,N,V_queue_connection"
- "T@\"NSXPCInterface\",R,N"
- "T@\"NSXPCListener\",R,N,V_listener"
- "T@?,C,N,V_invalidationHandler"
- "TB"
- "TB,N"
- "TB,N,GisInvalid,V_invalid"
- "TB,N,R"
- "TB,N,V_editable"
- "TB,N,V_interrupted"
- "TB,N,V_isTerminalOutput"
- "TB,N,V_showAsAlert"
- "TB,N,V_showAsAlertReady"
- "TB,N,V_truncateAtPanBoundary"
- "TB,N,VbackTranslateByCell"
- "TB,N,VbrailleStringDirty"
- "TB,N,VisShowingSecureToken"
- "TB,N,VisSingleKeyQuickNav"
- "TB,N,VisWordDescriptionActive"
- "TB,N,VtechnicalMode"
- "TB,R"
- "TB,R,N"
- "TB,R,N,GisLoopback"
- "TB,R,N,GisPartial,V_partial"
- "TB,R,N,V_useTechnicalTableIfPossible"
- "TC,R"
- "TQ,N,V_cursor"
- "TQ,N,V_inputTranslationMode"
- "TQ,N,V_lineFocus"
- "TQ,N,V_outputTranslationMode"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_mode"
- "Tq,N,V_token"
- "T{_NSRange=QQ},N,R"
- "T{_NSRange=QQ},N,V_range"
- "T{_NSRange=QQ},N,V_suggestionRange"
- "T{_NSRange=QQ},R,N"
- "T{_NSRange=QQ},R,N,V_focus"
- "T{_NSRange=QQ},R,N,V_selection"
- "T{_NSRange=QQ},R,N,V_textPositionsRange"
- "UTF8String"
- "Unichar Range %s -> Char Range %s"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__EmojiLocaleDataWrapper=}"
- "^{__Mecabra=}"
- "^{__MecabraContext=}"
- "_TtC18BrailleTranslation18BRLTBrailleUIModel"
- "_TtC18BrailleTranslation20BRLTCandidateManager"
- "_TtC18BrailleTranslation26BRLTWordDescriptionManager"
- "_TtCC18BrailleTranslation18BRLTBrailleUIModelP33_12303CD49F5ECD691D5972ABD37CA33B6Action"
- "_TtCC18BrailleTranslation22BRLTBrailleMusicParserP33_E886CD66E288DBBFC574695449FA98EA20BrailleMusicDelegate"
- "_activeBrailleEditingRegion"
- "_activeScriptEditingRegion"
- "_addSelectionRange:"
- "_apiLock"
- "_arrayFromData:"
- "_backTranslate:"
- "_backwardEditingAtomForCursorLocation:isBreak:"
- "_backwardEditingAtomForSelection:isBreak:"
- "_bits"
- "_boldRanges"
- "_brailleBackwardEditingRegion"
- "_brailleBuffer"
- "_brailleChars"
- "_brailleDirty"
- "_brailleFocus"
- "_brailleForwardEditingRegion"
- "_brailleMergeEditingRegion"
- "_brailleRangeForTextRange:textPositions:brailleLength:"
- "_brailleSelection"
- "_brailleString"
- "_brailleSuggestion"
- "_brailleTableDictionary"
- "_brl_rangeOfLastDot"
- "_bundle"
- "_candidateRefForSurface"
- "_commonInit"
- "_context"
- "_currentAnalysis"
- "_currentSurface"
- "_cursor"
- "_delegate"
- "_deleteBrailleCharSilently:"
- "_dotUp:"
- "_editable"
- "_focus"
- "_forwardDeleteBrailleCharSilently:"
- "_generateBrailleBuffer:"
- "_generateBrailleBufferForDelete"
- "_generateBrailleBufferForInsert"
- "_inputTranslationMode"
- "_interrupted"
- "_invalid"
- "_invalidationHandler"
- "_isEqualToTable:"
- "_isTerminalOutput"
- "_italicRanges"
- "_kataToHira"
- "_language"
- "_languageAgnosticIdentifiersToTables"
- "_lastScriptStringOutputTime"
- "_lineFocus"
- "_listener"
- "_locale"
- "_locationMapWithLength:forArray:defaultLocation:"
- "_loopbackService"
- "_mecabra"
- "_mode"
- "_outputTranslationMode"
- "_partial"
- "_pendingScriptSelection"
- "_primaryLanguageCode"
- "_queue"
- "_queueTranslator"
- "_queue_connection"
- "_queue_invalidate"
- "_queue_loadBundle"
- "_queue_resume"
- "_queue_serviceProxy"
- "_range"
- "_reachedEnd"
- "_resetForTest"
- "_runningScriptStringHistory"
- "_scriptBackwardEditingRegion"
- "_scriptDirty"
- "_scriptForwardEditingRegion"
- "_scriptMergeEditingRegion"
- "_scriptString"
- "_selection"
- "_selectionIsValidForDelete"
- "_selectionIsValidForInsert"
- "_serviceIdentifier"
- "_setBrailleSelection:newScriptLocation:"
- "_setDot:up:"
- "_setupLocale"
- "_showAsAlert"
- "_showAsAlertReady"
- "_staticBrailleString"
- "_string"
- "_suggestionRange"
- "_supportedLanguageLocales"
- "_supportedLocales"
- "_table"
- "_tableIdentifier"
- "_textFormattingRanges"
- "_textPositionsRange"
- "_textRangeForBrailleRange:textPositions:scriptLength:"
- "_token"
- "_tokenRanges"
- "_translate:"
- "_translate:isTechnical:textFormattingRanges:"
- "_translationDelegate"
- "_translator"
- "_translatorBundlePath"
- "_translatorBundles"
- "_truncateAtPanBoundary"
- "_underlineRanges"
- "_underlyingObject"
- "_useTechnicalTableIfPossible"
- "_variant"
- "activeTable"
- "activeTableSupportsContractedBraille"
- "activeTableSupportsEightDotBraille"
- "activeTableSupportsIPA"
- "activeTableSupportsTechnicalBraille"
- "addBoldRange:"
- "addItalicRange:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addString:selection:focus:token:"
- "addUnderlineRange:"
- "alertBraille"
- "alertScript"
- "allKeys"
- "allocWithZone:"
- "analysisStringList"
- "analyzeString:"
- "anonymousListener"
- "appendBytes:length:"
- "appendData:"
- "appendString:"
- "appending:"
- "array"
- "arrayFromData:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "autorelease"
- "backTranslateByCell"
- "backTranslateLocally"
- "backwardEditingAtom"
- "backwardEditingAtomForScriptString:"
- "bestEffortBrf"
- "bits"
- "boolValue"
- "brailleBuffer"
- "brailleCache"
- "brailleChars"
- "brailleDisplayDeletedCharacter:"
- "brailleDisplayInsertedCharacter:modifiers:"
- "brailleDisplayString"
- "brailleDisplayStringDidChange:brailleSelection:brailleUIOptions:modifiers:"
- "brailleFocus"
- "brailleForText:locations:"
- "brailleForText:parameters:locations:"
- "brailleForText:parameters:withReply:"
- "brailleLocationForScriptLocation:"
- "brailleRangeForScriptRange:"
- "brailleSelection"
- "brailleSelectionDirty"
- "brailleString"
- "brailleStringDirty"
- "brailleSuggestion"
- "brailleUIActive"
- "brailleUIModel"
- "brailleWords"
- "brfTable"
- "brfToUnicode:"
- "brl_brailleTableBundleWithIdentifier:"
- "brl_brailleTablesDictionary"
- "brl_language"
- "brl_languageAgnosticTables"
- "brl_languageAndVariant"
- "brl_serviceIdentifier"
- "brl_supportedLocaleIdentifiersForTableWithIdentifier:"
- "brl_supportedLocales"
- "brl_supportedLocalesForTableWithIdentifier:"
- "brl_supportedTablesForLocale:"
- "brl_tableIdentifier"
- "brl_tableIsLanguageAgnosticWithIdentifier:"
- "brl_variant"
- "bufferBrailleString"
- "bundle"
- "bundleForClass:"
- "bundleIdentifier"
- "bundleWithPath:"
- "bytes"
- "candidateList"
- "candidateManager"
- "charWithBits:"
- "charWithBrf:"
- "charWithUnichar:"
- "charWithUnicode:"
- "characterAtIndex:"
- "characterSetWithCharactersInString:"
- "class"
- "clearAtNextDotPress"
- "clientSetSelection"
- "collatorIdentifier"
- "componentsSeparatedByString:"
- "composition"
- "conformsToProtocol:"
- "connectionForLoopbackService:"
- "connectionForServiceIdentifier:"
- "connections"
- "connectionsLock"
- "containsObject:"
- "contentLock"
- "contentsOfDirectoryAtPath:error:"
- "contiguousBrailleRange"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "currentChord"
- "currentIndex"
- "currentKeySignature"
- "currentLocale"
- "currentMeasure"
- "currentMetronomeMarking"
- "currentNote"
- "currentStaff"
- "currentTimeSignature"
- "cursor"
- "d"
- "dataWithBytes:length:"
- "dataWithCapacity:"
- "dataWithLength:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "defaultManager"
- "defaultTableForLocale:"
- "defaultTablesArrayForLocale:"
- "delegate"
- "deleteBrailleChar"
- "deleteBrailleCharSilently"
- "deleteMergeAtom"
- "deleteMergeAtomForScriptString:"
- "description"
- "descriptionCache"
- "descriptionOfWord:forLanguage:"
- "dictionary"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjects:forKeys:count:"
- "didChangeBrailleString:brailleSelection:brailleUIOptions:"
- "didDeleteBrailleChar:"
- "didDeleteScriptChar"
- "didInsertScriptString:"
- "didReplaceScriptStringRange:withScriptString:cursorLocation:"
- "dinToUnicode:"
- "displayedBraille"
- "displayedRange"
- "displayedRangeAfter"
- "displayedRangeBefore"
- "displayedScript"
- "dot1"
- "dot2"
- "dot3"
- "dot4"
- "dot5"
- "dot6"
- "dot7"
- "dot8"
- "editScript"
- "editable"
- "editingBrailleRange"
- "editingScriptRange"
- "elementStack"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endpoint"
- "enumerateObjectsUsingBlock:"
- "escapedPatternForString:"
- "exportedInterface"
- "externalServiceIdentifier"
- "fileExistsAtPath:"
- "fileURLWithPath:"
- "firstObject"
- "focus"
- "forceTranslate"
- "forwardDeleteBrailleChar"
- "forwardDeleteBrailleCharSilently"
- "forwardEditingAtom"
- "forwardEditingAtomForCursorLocation:"
- "forwardEditingAtomForScriptString:"
- "future"
- "getCurrentCandidateAnalysisString"
- "getCurrentCandidateSurface"
- "handleBrailleDotPress:"
- "handleBrailleSelection:"
- "handleBrailleSelectionUpTo:"
- "handleBrailleSelectionWithNSSelection:"
- "handleBrailleSelectionWithUpTo:"
- "handleDelete"
- "handleDeleteSilently"
- "handleDeleteWithSilently:"
- "handleEscape"
- "handleMoveCursorLeft"
- "handleMoveCursorRight"
- "handleReturn"
- "handleReturnInternally"
- "handleWordDescriptionCommand"
- "hasCaughtUp"
- "hasReceivedMaskedCharacter"
- "hash"
- "history"
- "identifier"
- "init"
- "initWithBits:"
- "initWithBrailleChars:"
- "initWithBrailleString:"
- "initWithBrf:"
- "initWithBundle:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithData:"
- "initWithDelegate:tableIdentifier:"
- "initWithDelegate:translationDelegate:"
- "initWithExternalIdentifier:"
- "initWithIdentifier:"
- "initWithLanguage:mode:partial:useTechnicalTable:textPositionsRange:textFormattingRanges:"
- "initWithListenerEndpoint:"
- "initWithPattern:options:error:"
- "initWithPrimaryLanguageCode:"
- "initWithRange:token:"
- "initWithServiceIdentifier:connection:"
- "initWithServiceIdentifier:connection:loopbackService:"
- "initWithServiceIdentifier:language:variant:"
- "initWithServiceIdentifier:tableIdentifier:"
- "initWithServiceName:"
- "initWithString:"
- "initWithString:NSSelection:NSFocus:token:NSSuggestion:textFormattingRanges:"
- "initWithString:selection:"
- "initWithString:selection:focus:token:"
- "initWithString:selection:focus:token:suggestion:textFormattingRanges:"
- "initWithTable:"
- "initWithTranslatorBundlesPath:"
- "initWithUnderlyingObject:"
- "initWithUnichar:"
- "initWithUnicode:"
- "initWithUnitTesting:"
- "inputTranslationMode"
- "inputTranslator"
- "insertBrailleChar:"
- "insertBrailleChar:modifiers:"
- "insertBrailleChar:modifiers:inputMode:"
- "insertBrailleChar:modifiers:silently:"
- "insertBrailleChar:silently:"
- "insertObject:atIndex:"
- "instancesRespondToSelector:"
- "interfaceVersion"
- "interfaceWithProtocol:"
- "interrupted"
- "invalid"
- "invalidate"
- "invalidationHandler"
- "invertedSet"
- "isActive"
- "isCandidateSelectionActive"
- "isContentDynamic"
- "isCustomBrailleTable"
- "isEqual:"
- "isEqualTable:"
- "isEqualToArray:"
- "isEqualToBrailleChar:"
- "isEqualToBrailleString:"
- "isEqualToScriptString:"
- "isEqualToString:"
- "isInvalid"
- "isKindOfClass:"
- "isLoopback"
- "isMemberOfClass:"
- "isPartial"
- "isProxy"
- "isSelectionForward"
- "isShowingSecureToken"
- "isSingleKeyQuickNav"
- "isTerminalOutput"
- "isValidBRF:"
- "isWordDescriptionActive"
- "isWordDescriptionLike:"
- "languageAgnosticIdentifiersToTables"
- "languageAgnosticTableIdentifiers"
- "languageAgnosticTables"
- "languageAgnosticTablesForIdentifier:inBundle:"
- "languageAgnosticTablesInBundle:"
- "languageCode"
- "lastScriptOutputTime"
- "learnCandidate:"
- "length"
- "lineFocus"
- "lineRangeForRange:"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "loadBrailleBundleForIdentifier:"
- "localeIdentifier"
- "localeWithLocaleIdentifier:"
- "locales"
- "localizedInfoDictionary"
- "localizedLanguage"
- "localizedName"
- "localizedNameForLanguage:"
- "localizedNameForLanguageAgnosticTableIdentifier:"
- "localizedNameForServiceWithIdentifier:"
- "localizedNameWithService"
- "localizedService"
- "localizedStringForKey:value:table:"
- "localizedStringForLanguage:context:"
- "localizedStringWithFormat:"
- "localizedVariant"
- "lock"
- "longVowelExpressedFor:partOfSpeech:"
- "loopback"
- "loopbackService"
- "lowercaseString"
- "matchesInString:options:range:"
- "mecabra"
- "mergeLocationMap:withLocationMap:"
- "mergePreprocessorOutputLocationMap:outputToPreprocessedMap:outputLen:outputToTextMap:"
- "moveToNextCandidate"
- "musicParenthesis"
- "mutableCopy"
- "needsEqualSign"
- "nsUISelection"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithUnsignedInt:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForInfoDictionaryKey:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "outputScriptString"
- "outputTranslationMode"
- "outputTranslator"
- "parse"
- "parser:didEndElement:namespaceURI:qualifiedName:"
- "parser:didEndMappingPrefix:"
- "parser:didStartElement:namespaceURI:qualifiedName:attributes:"
- "parser:didStartMappingPrefix:toURI:"
- "parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:"
- "parser:foundCDATA:"
- "parser:foundCharacters:"
- "parser:foundComment:"
- "parser:foundElementDeclarationWithName:model:"
- "parser:foundExternalEntityDeclarationWithName:publicID:systemID:"
- "parser:foundIgnorableWhitespace:"
- "parser:foundInternalEntityDeclarationWithName:value:"
- "parser:foundNotationDeclarationWithName:publicID:systemID:"
- "parser:foundProcessingInstructionWithTarget:data:"
- "parser:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:"
- "parser:parseErrorOccurred:"
- "parser:resolveExternalEntityName:systemID:"
- "parser:validationErrorOccurred:"
- "parserDidEndDocument:"
- "parserDidStartDocument:"
- "pathExtension"
- "pathForResource:ofType:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preferredLocalizations"
- "preprocessPrintString:withLocationMap:isEightDot:textFormattingRanges:"
- "principalClass"
- "printBrailleForText:language:mode:textPositionsRange:locations:textFormattingRanges:"
- "printBrailleForText:mode:locations:textPositionsRange:textFormattingRanges:"
- "q"
- "q16@0:8"
- "q24@0:8q16"
- "queue"
- "queueTranslator"
- "queue_connection"
- "range"
- "rangeOfCharacterFromSet:"
- "rangeOfCharacterFromSet:options:"
- "rangeOfComposedCharacterSequenceAtIndex:"
- "rangeOfString:"
- "rangeOfString:options:range:"
- "rangeValue"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectsInRange:"
- "replaceKataWithHira:"
- "replaceObjectsInRange:withObjectsFromArray:"
- "replaceScriptStringRange:withScriptString:cursorLocation:"
- "requestSpeech:language:"
- "respondsToSelector:"
- "result"
- "resume"
- "retain"
- "retainCount"
- "script"
- "scriptEditingRange"
- "scriptHistory"
- "scriptLocationForBrailleLocation:"
- "scriptRangeForBrailleRange:"
- "scriptRangeOfBrailleCellRepresentingCharacterAt:"
- "scriptRangeOfBrailleCellRepresentingCharacterAtScriptIndex:"
- "scriptSelectionDidChange:"
- "sectionDoubleBar"
- "sectionHeavyDoubleBar"
- "selectCandidate"
- "selection"
- "selectionAfter"
- "selectionBefore"
- "self"
- "serviceForIdentifier:input:"
- "serviceForIdentifier:input:loopback:"
- "serviceIdentifier"
- "set"
- "setActiveTable:"
- "setAlert:"
- "setBackTranslateByCell:"
- "setBoldRanges:"
- "setBrailleSelection:"
- "setBrailleSelection:needsForwardToScreenReader:newScriptLocation:"
- "setBrailleStringDirty:"
- "setBrailleUIActive:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClearAtNextDotPress:"
- "setCursor:"
- "setDelegate:"
- "setDot1:"
- "setDot2:"
- "setDot3:"
- "setDot4:"
- "setDot5:"
- "setDot6:"
- "setDot7:"
- "setDot8:"
- "setEditable:"
- "setExportedInterface:"
- "setExportedObject:"
- "setHandleReturnInternally:"
- "setInputTableIdentifier:manager:"
- "setInputTranslationMode:"
- "setInterrupted:"
- "setInterruptionHandler:"
- "setInvalid:"
- "setInvalidationHandler:"
- "setIsShowingSecureToken:"
- "setIsSingleKeyQuickNav:"
- "setIsTerminalOutput:"
- "setIsWordDescriptionActive:"
- "setItalicRanges:"
- "setLanguageAgnosticIdentifiersToTables:"
- "setLineFocus:"
- "setLoopbackService:"
- "setObject:forKeyedSubscript:"
- "setOutputTableIdentifier:manager:"
- "setOutputTranslationMode:"
- "setQueue:"
- "setQueueTranslator:"
- "setQueue_connection:"
- "setRange:"
- "setRemoteObjectInterface:"
- "setScript:"
- "setScriptString:"
- "setShowAsAlert:"
- "setShowAsAlertReady:"
- "setSingleKeyQuickNav:"
- "setSuggestionRange:"
- "setTechnicalMode:"
- "setTerminalOutput:"
- "setTextFormattingRanges:"
- "setToken:"
- "setTokenRanges:"
- "setTranslationDelegate:"
- "setTranslator:"
- "setTranslatorBundlePath:"
- "setTruncateAtPanBoundary:"
- "setUIBraille:truncateAtPanBoundary:"
- "setUnderlineRanges:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObject:"
- "set_bundle:"
- "shared"
- "sharedInstance"
- "sharedModel"
- "sharedParser"
- "showAsAlert"
- "showAsAlertReady"
- "showFirstLine"
- "showLastLine"
- "showNextCandidate"
- "showNextLine"
- "showNextWordDescription"
- "showPreviousCandidate"
- "showPreviousLine"
- "showPreviousWordDescription"
- "showingAlert"
- "showingTerminalOutput"
- "spacedYomiOfWordDescription:"
- "stageRange"
- "stagedText"
- "string"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByReplacingCharactersInRange:withString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithCharacters:length:"
- "stringWithFormat:"
- "subarrayWithRange:"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "suggestion"
- "suggestionRange"
- "superclass"
- "supportedLanguageLocales"
- "supportedLocales"
- "supportedLocalesForTable:"
- "supportsSecureCoding"
- "supportsTranslationMode8Dot"
- "supportsTranslationModeContracted"
- "switchedToEditableWithUncommittedBraille"
- "systemTranslatorBundle"
- "table"
- "tableEnumeratorWithSystemBundlePath"
- "tableIdentifier"
- "tablesForLocale:inBundle:"
- "technicalMode"
- "textForBraille:locations:"
- "textForBraille:parameters:locations:"
- "textForBraille:parameters:withReply:"
- "textForPrintBraille:language:mode:locations:"
- "textForPrintBraille:mode:locations:"
- "textFormattingRanges"
- "token"
- "tokenForLocation:"
- "tokenRanges"
- "translate"
- "translate:"
- "translateForced:"
- "translationDelegate"
- "translationResult"
- "translator"
- "translatorBundlePath"
- "translatorBundles"
- "truncateAtPanBoundary"
- "uiAppendNewLine"
- "uiBraille"
- "uiDisplayRange"
- "uiFind:"
- "uiFocusedLineIndex"
- "uiInsertBraille:"
- "uiMoveFocusTo:"
- "uiMoveToNextCharacter"
- "uiMoveToPreviousCharacter"
- "uiPreviousFind:"
- "uiRedo"
- "uiReplaceLastLineWith:"
- "uiSelectAll"
- "uiSelectBoundary"
- "uiSelectCharacter:"
- "uiSelectCharacterWithIsForward:"
- "uiSelectLine:"
- "uiSelectLineWithIsForward:"
- "uiSelectWord:"
- "uiSelectWordWithIsForward:"
- "uiSelection"
- "uiUndo"
- "uncommittedBrailleCharCount"
- "underlyingObject"
- "unicode"
- "unicodeToBestEffortBrf:"
- "unicodeToDin:"
- "unionSet:"
- "unitTesting"
- "unlock"
- "uppercaseString"
- "useTechnicalTableIfPossible"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"BRLTBrailleChar\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"NSXMLParser\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8i16B20"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSXMLParser\"16@\"NSData\"24"
- "v32@0:8@\"NSXMLParser\"16@\"NSError\"24"
- "v32@0:8@\"NSXMLParser\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8{_NSRange=QQ}16"
- "v36@0:8@16@24B32"
- "v40@0:8@\"NSString\"16@\"BRLTTranslationParameters\"24@?<v@?@\"NSString\"@\"NSData\">32"
- "v40@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24Q32"
- "v48@0:8@\"NSString\"16{_NSRange=QQ}24@\"BRLTBrailleUIFormattingOptions\"40"
- "v48@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16^i24q32^@40"
- "v48@0:8@16{_NSRange=QQ}24@40"
- "v48@0:8{_NSRange=QQ}16@\"NSString\"32q40"
- "v48@0:8{_NSRange=QQ}16@32q40"
- "v48@0:8{_NSRange=QQ}16o^B32o^Q40"
- "v56@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSDictionary\"48"
- "v56@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@16@24@32@40@48"
- "v64@0:8@16{_NSRange=QQ}24{_NSRange=QQ}40Q56"
- "valueForEntitlement:"
- "valueWithRange:"
- "variant"
- "whitespaceAndNewlineCharacterSet"
- "wordDescriptionManager"
- "words"
- "zone"
- "{_NSRange=\"location\"Q\"length\"Q}"
- "{_NSRange=QQ}16@0:8"
- "{_NSRange=QQ}24@0:8@16"
- "{_NSRange=QQ}24@0:8Q16"
- "{_NSRange=QQ}24@0:8q16"
- "{_NSRange=QQ}32@0:8Q16^B24"
- "{_NSRange=QQ}32@0:8{_NSRange=QQ}16"
- "{_NSRange=QQ}40@0:8{_NSRange=QQ}16^B32"
- "{_NSRange=QQ}48@0:8{_NSRange=QQ}16@32Q40"
- "{_NSRange=QQ}48@0:8{_NSRange=QQ}16@32q40"

```
