## IntelligencePlatformLibrary

> `/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary`

```diff

-441.45.0.0.0
-  __TEXT.__text: 0x75433c
-  __TEXT.__objc_methlist: 0x2634c
-  __TEXT.__const: 0x5ed20
+441.45.5.0.0
+  __TEXT.__text: 0x75d828
+  __TEXT.__objc_methlist: 0x26594
+  __TEXT.__const: 0x5ed40
   __TEXT.__constg_swiftt: 0xa6d8
   __TEXT.__swift5_typeref: 0xaebc
-  __TEXT.__swift5_fieldmd: 0x18160
+  __TEXT.__swift5_fieldmd: 0x18190
   __TEXT.__swift5_types: 0x1548
-  __TEXT.__swift5_reflstr: 0x16cfa
+  __TEXT.__swift5_reflstr: 0x16d3a
   __TEXT.__swift5_assocty: 0x47c0
   __TEXT.__oslogstring: 0x1f4
   __TEXT.__swift5_capture: 0x3910
   __TEXT.__swift5_proto: 0x69b8
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__cstring: 0x7df81
+  __TEXT.__cstring: 0x7e305
   __TEXT.__swift5_builtin: 0x640
   __TEXT.__swift5_mpenum: 0x608
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__unwind_info: 0x29b00
-  __TEXT.__eh_frame: 0x22fa4
+  __TEXT.__unwind_info: 0x29bf0
+  __TEXT.__eh_frame: 0x23044
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9618
-  __DATA_CONST.__objc_classlist: 0x13b8
+  __DATA_CONST.__const: 0x9688
+  __DATA_CONST.__objc_classlist: 0x13c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x64a0
+  __DATA_CONST.__objc_selrefs: 0x64f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__got: 0x17f8
-  __AUTH_CONST.__const: 0x43050
-  __AUTH_CONST.__cfstring: 0x269c0
-  __AUTH_CONST.__objc_const: 0x40810
+  __DATA_CONST.__got: 0x1808
+  __AUTH_CONST.__const: 0x43060
+  __AUTH_CONST.__cfstring: 0x26c60
+  __AUTH_CONST.__objc_const: 0x40d10
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0xe28
-  __AUTH.__objc_data: 0xb6a8
+  __AUTH.__objc_data: 0xb748
   __AUTH.__data: 0x4098
-  __DATA.__objc_ivar: 0x32e0
+  __DATA.__objc_ivar: 0x332c
   __DATA.__data: 0xb580
   __DATA.__common: 0x6938
   __DATA_DIRTY.__objc_data: 0x1310

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 63793
-  Symbols:   27660
-  CStrings:  11388
+  Functions: 63857
+  Symbols:   27749
+  CStrings:  11414
 
Symbols:
+ +[CCSetLibraryConfigurationRegistry configurationForSet_SiriConversationRecap]
+ +[CCSetLibraryConfigurationRegistry syncPolicyForSet_SiriConversationRecap]
+ +[CCSiriConversationRecapContent contentMessageClass]
+ +[CCSiriConversationRecapContent descriptionForTypeIdentifier:]
+ +[CCSiriConversationRecapContent itemType]
+ +[CCSiriConversationRecapContent metaContentMessageClass]
+ +[CCSiriConversationRecapContent typeIdentifierForDescription:]
+ +[CCSiriConversationRecapMetaContent contentMessageClass]
+ +[CCSiriConversationRecapMetaContent descriptionForTypeIdentifier:]
+ +[CCSiriConversationRecapMetaContent itemType]
+ +[CCSiriConversationRecapMetaContent metaContentMessageClass]
+ +[CCSiriConversationRecapMetaContent typeIdentifierForDescription:]
+ -[CCSiriConversationRecapContent .cxx_destruct]
+ -[CCSiriConversationRecapContent captureIntervalEnd]
+ -[CCSiriConversationRecapContent captureIntervalStart]
+ -[CCSiriConversationRecapContent copyApplyingPatch:deletedFieldTypes:error:]
+ -[CCSiriConversationRecapContent decodeFieldValuesFromData:error:]
+ -[CCSiriConversationRecapContent enumerateFieldsUsingBlock:parentFieldType:]
+ -[CCSiriConversationRecapContent hasIsSaved]
+ -[CCSiriConversationRecapContent inferredLocationTags]
+ -[CCSiriConversationRecapContent initWithData:error:]
+ -[CCSiriConversationRecapContent initWithJSONDictionary:error:]
+ -[CCSiriConversationRecapContent initWithKind:title:summary:transcriptsText:inferredLocationTags:captureIntervalStart:captureIntervalEnd:isSaved:error:]
+ -[CCSiriConversationRecapContent isSaved]
+ -[CCSiriConversationRecapContent jsonDictionary]
+ -[CCSiriConversationRecapContent kind]
+ -[CCSiriConversationRecapContent setHasIsSaved:]
+ -[CCSiriConversationRecapContent summary]
+ -[CCSiriConversationRecapContent title]
+ -[CCSiriConversationRecapContent transcriptsText]
+ -[CCSiriConversationRecapMetaContent .cxx_destruct]
+ -[CCSiriConversationRecapMetaContent cacheContentHash]
+ -[CCSiriConversationRecapMetaContent copyApplyingPatch:deletedFieldTypes:error:]
+ -[CCSiriConversationRecapMetaContent createdDate]
+ -[CCSiriConversationRecapMetaContent decodeFieldValuesFromData:error:]
+ -[CCSiriConversationRecapMetaContent enumerateFieldsUsingBlock:parentFieldType:]
+ -[CCSiriConversationRecapMetaContent hasCacheContentHash]
+ -[CCSiriConversationRecapMetaContent initWithData:error:]
+ -[CCSiriConversationRecapMetaContent initWithJSONDictionary:error:]
+ -[CCSiriConversationRecapMetaContent initWithSourceItemIdentifier:sourceBundleIdentifier:createdDate:modifiedDate:cacheContentHash:error:]
+ -[CCSiriConversationRecapMetaContent jsonDictionary]
+ -[CCSiriConversationRecapMetaContent modifiedDate]
+ -[CCSiriConversationRecapMetaContent setHasCacheContentHash:]
+ -[CCSiriConversationRecapMetaContent sourceBundleIdentifier]
+ -[CCSiriConversationRecapMetaContent sourceItemIdentifier]
+ GCC_except_table7599
+ GCC_except_table8192
+ _OBJC_CLASS_$_CCSiriConversationRecapContent
+ _OBJC_CLASS_$_CCSiriConversationRecapMetaContent
+ _OBJC_IVAR_$_CCSiriConversationRecapContent._hasIsSaved
+ _OBJC_IVAR_$_CCSiriConversationRecapContent._hasRaw_captureIntervalEnd
+ _OBJC_IVAR_$_CCSiriConversationRecapContent._hasRaw_captureIntervalStart
+ _OBJC_IVAR_$_CCSiriConversationRecapContent._inferredLocationTags
+ _OBJC_IVAR_$_CCSiriConversationRecapContent._isSaved
+ _OBJC_IVAR_$_CCSiriConversationRecapContent._kind
+ _OBJC_IVAR_$_CCSiriConversationRecapContent._raw_captureIntervalEnd
+ _OBJC_IVAR_$_CCSiriConversationRecapContent._raw_captureIntervalStart
+ _OBJC_IVAR_$_CCSiriConversationRecapContent._summary
+ _OBJC_IVAR_$_CCSiriConversationRecapContent._title
+ _OBJC_IVAR_$_CCSiriConversationRecapContent._transcriptsText
+ _OBJC_IVAR_$_CCSiriConversationRecapMetaContent._cacheContentHash
+ _OBJC_IVAR_$_CCSiriConversationRecapMetaContent._hasCacheContentHash
+ _OBJC_IVAR_$_CCSiriConversationRecapMetaContent._hasRaw_createdDate
+ _OBJC_IVAR_$_CCSiriConversationRecapMetaContent._hasRaw_modifiedDate
+ _OBJC_IVAR_$_CCSiriConversationRecapMetaContent._raw_createdDate
+ _OBJC_IVAR_$_CCSiriConversationRecapMetaContent._raw_modifiedDate
+ _OBJC_IVAR_$_CCSiriConversationRecapMetaContent._sourceBundleIdentifier
+ _OBJC_IVAR_$_CCSiriConversationRecapMetaContent._sourceItemIdentifier
+ _OBJC_METACLASS_$_CCSiriConversationRecapContent
+ _OBJC_METACLASS_$_CCSiriConversationRecapMetaContent
+ _OUTLINED_FUNCTION_502
+ _OUTLINED_FUNCTION_503
+ _OUTLINED_FUNCTION_641
+ _OUTLINED_FUNCTION_642
+ _OUTLINED_FUNCTION_643
+ _OUTLINED_FUNCTION_644
+ _OUTLINED_FUNCTION_645
+ _OUTLINED_FUNCTION_646
+ _OUTLINED_FUNCTION_814
+ __OBJC_$_CLASS_METHODS_CCSiriConversationRecapContent
+ __OBJC_$_CLASS_METHODS_CCSiriConversationRecapMetaContent
+ __OBJC_$_INSTANCE_METHODS_CCSiriConversationRecapContent
+ __OBJC_$_INSTANCE_METHODS_CCSiriConversationRecapMetaContent
+ __OBJC_$_INSTANCE_VARIABLES_CCSiriConversationRecapContent
+ __OBJC_$_INSTANCE_VARIABLES_CCSiriConversationRecapMetaContent
+ __OBJC_$_PROP_LIST_CCSiriConversationRecapContent
+ __OBJC_$_PROP_LIST_CCSiriConversationRecapMetaContent
+ __OBJC_CLASS_PROTOCOLS_$_CCSiriConversationRecapContent
+ __OBJC_CLASS_PROTOCOLS_$_CCSiriConversationRecapMetaContent
+ __OBJC_CLASS_RO_$_CCSiriConversationRecapContent
+ __OBJC_CLASS_RO_$_CCSiriConversationRecapMetaContent
+ __OBJC_METACLASS_RO_$_CCSiriConversationRecapContent
+ __OBJC_METACLASS_RO_$_CCSiriConversationRecapMetaContent
+ ___swift_memcpy132_8
+ ___swift_memcpy663_8
- GCC_except_table7597
- GCC_except_table8190
- _OUTLINED_FUNCTION_478
- _OUTLINED_FUNCTION_514
- ___swift_memcpy130_8
- ___swift_memcpy661_8
CStrings:
+ "B32A35C0-AAF4-4976-A684-2030A38AD613"
+ "C9D79ADE-C17E-448D-B52D-6EA4D0112194"
+ "E"
+ "Safari.AutoDarkMode"
+ "Siri.ConversationRecap"
+ "SiriConversationRecap"
+ "SiriConversationRecapContent_captureIntervalEnd"
+ "SiriConversationRecapContent_captureIntervalStart"
+ "SiriConversationRecapContent_inferredLocationTags"
+ "SiriConversationRecapContent_isSaved"
+ "SiriConversationRecapContent_kind"
+ "SiriConversationRecapContent_summary"
+ "SiriConversationRecapContent_title"
+ "SiriConversationRecapContent_transcriptsText"
+ "SiriConversationRecapMetaContent_cacheContentHash"
+ "SiriConversationRecapMetaContent_createdDate"
+ "SiriConversationRecapMetaContent_modifiedDate"
+ "SiriConversationRecapMetaContent_sourceBundleIdentifier"
+ "SiriConversationRecapMetaContent_sourceItemIdentifier"
+ "captureIntervalEnd"
+ "captureIntervalStart"
+ "inferredLocationTags"
+ "isSaved"
+ "kvCacheHasDuplicateId"
+ "kvCacheInputMismatch"
+ "transcriptsText"
```
