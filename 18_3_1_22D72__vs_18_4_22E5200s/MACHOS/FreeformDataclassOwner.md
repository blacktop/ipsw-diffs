## FreeformDataclassOwner

> `/System/Library/Accounts/DataclassOwners/FreeformDataclassOwner.bundle/FreeformDataclassOwner`

```diff

-419.80.1.0.3
-  __TEXT.__text: 0x1a044
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_stubs: 0x1ae0
-  __TEXT.__objc_methlist: 0x8c4
-  __TEXT.__const: 0xa3a
-  __TEXT.__cstring: 0x28c8
-  __TEXT.__objc_methname: 0x291a
+419.100.15.0.6
+  __TEXT.__text: 0x1a45c
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_stubs: 0x1b00
+  __TEXT.__objc_methlist: 0xaf4
+  __TEXT.__const: 0xa92
+  __TEXT.__cstring: 0x2928
+  __TEXT.__objc_methname: 0x2988
   __TEXT.__objc_classname: 0x165
   __TEXT.__objc_methtype: 0x406
   __TEXT.__oslogstring: 0x5dd

   __TEXT.__ustring: 0x50
   __TEXT.__constg_swiftt: 0x47c
   __TEXT.__swift5_typeref: 0x196
-  __TEXT.__swift5_reflstr: 0x3e1
-  __TEXT.__swift5_fieldmd: 0x370
+  __TEXT.__swift5_reflstr: 0x401
+  __TEXT.__swift5_fieldmd: 0x37c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0x40
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x9a8
+  __TEXT.__unwind_info: 0x9e0
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x5b0
+  __DATA_CONST.__auth_got: 0x598
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x158
-  __DATA_CONST.__const: 0x1290
-  __DATA_CONST.__cfstring: 0x1ba0
+  __DATA_CONST.__const: 0x1288
+  __DATA_CONST.__cfstring: 0x1c00
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x12f0
-  __DATA.__objc_selrefs: 0xab8
+  __DATA.__objc_const: 0xf28
+  __DATA.__objc_selrefs: 0xbc0
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x508
   __DATA.__data: 0xb88

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 875
-  Symbols:   6890
-  CStrings:  857
+  Functions: 920
+  Symbols:   7164
+  CStrings:  865
 
Symbols:
+ +[CRLAssertionHandler _logBacktraceWithCallStackSymbols:].cold.2
+ +[CRLAssertionHandler logFullBacktrace].cold.2
+ +[CRLAssertionHandler packedBacktraceStringWithReturnAddresses:].cold.1
+ +[CRLAssertionHandler simulateCrashWithMessage:].cold.1
+ +[CRLLogHelper sharedInstance].cold.1
+ +[CRLSystemInfo hwModel].cold.1
+ +[CRLSystemInfo osVersion].cold.1
+ +[CRLUserDefaults defaultDefaults].cold.1
+ +[NSString(CRLAdditions) crl_stringWithItemProviderData:typeIdentifier:error:].cold.3
+ +[NSString(CRLAdditions) crl_stringWithItemProviderData:typeIdentifier:error:].cold.4
+ +[NSString(CRLPersonNameComponents) crl_localizedDisplayNameWithPersonNameComponents:].cold.2
+ -[CRLLogHelper incrementThrottleCountAndCheckThottleMax:].cold.1
+ -[CRLLogHelper incrementThrottleCountAndCheckThottleMax:].cold.2
+ -[NSString(CRLAdditions) crl_appendJSONStringToString:].cold.1
+ -[NSString(CRLAdditions) crl_escapeForIcuRegex].cold.1
+ -[NSString(CRLAdditions) crl_regexForTitleParsingWithLocalizedCopyString:isFirstCopyFormatString:].cold.2
+ -[NSString(CRLAdditions) crl_regexForTitleParsingWithLocalizedCopyString:isFirstCopyFormatString:].cold.3
+ -[NSString(CRLAdditions) crl_stringByEscapingForSpotlightSearch]
+ -[NSString(CRLAdditions) crl_stringByRemovingCharactersInSet:options:].cold.3
+ -[NSString(CRLAdditions) crl_stringByRemovingCharactersInSet:options:].cold.4
+ -[NSString(CRLAdditions) crl_stringByUniquingPathInsideDirectory:withFormat:].cold.3
+ -[NSString(CRLAdditions) crl_stringByUniquingPathInsideDirectory:withFormat:].cold.4
+ -[NSString(CRLAdditions) crl_stringWithNormalizedHyphens].cold.1
+ -[NSString(CRLAdditions) crl_stringWithNormalizedQuotationMarks].cold.1
+ -[NSString(CRLAdditions) crl_stringWithoutAttachmentCharacters].cold.1
+ -[NSString(CRLLogAdditions) crl_initRedactedWithFormat:arguments:].cold.1
+ CRLAdjustSelectionRangeForChangedRange.cold.10
+ CRLAdjustSelectionRangeForChangedRange.cold.11
+ CRLAdjustSelectionRangeForChangedRange.cold.12
+ CRLAdjustSelectionRangeForChangedRange.cold.13
+ CRLAdjustSelectionRangeForChangedRange.cold.14
+ CRLAdjustSelectionRangeForChangedRange.cold.15
+ CRLAdjustSelectionRangeForChangedRange.cold.16
+ CRLAdjustSelectionRangeForChangedRange.cold.9
+ CRLAppBundleIdentifier.cold.1
+ CRLAppGroupIdentifier.cold.1
+ CRLLogGetNameDictionary.cold.1
+ DisabledCategories.cold.1
+ EnabledCategories.cold.1
+ _$s22FreeformDataclassOwner19CRLFeatureFlagGroupC26isBatteriesIncludedEnabledSbvgZTo
+ _$s22FreeformDataclassOwner19CRLFeatureFlagGroupC33isContentLanguageCopyPasteEnabledSbvgZTo
+ _$s22FreeformDataclassOwner38CRLDeviceManagementRestrictionsManagerC06deviceeF23ChangedNotificationNameSo014NSNotificationK0avpZMV
+ _$s22FreeformDataclassOwner38CRLDeviceManagementRestrictionsManagerC6sharedACvpZMV
+ _CRLVersionV3_4
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __47-[NSString(CRLAdditions) crl_escapeForIcuRegex]_block_invoke.119
+ __47-[NSString(CRLAdditions) crl_escapeForIcuRegex]_block_invoke.cold.3
+ __47-[NSString(CRLAdditions) crl_escapeForIcuRegex]_block_invoke.cold.4
+ __66+[CRLAssertionHandler p_performBlockIgnoringAssertions:onlyFatal:]_block_invoke.cold.2
+ __70-[NSString(CRLAdditions) crl_stringByRemovingCharactersInSet:options:]_block_invoke.107
+ __77-[NSString(CRLAdditions) crl_stringByUniquingPathInsideDirectory:withFormat:]_block_invoke.99
+ __78+[NSString(CRLAdditions) crl_stringWithItemProviderData:typeIdentifier:error:]_block_invoke.252
+ __98-[NSString(CRLAdditions) crl_regexForTitleParsingWithLocalizedCopyString:isFirstCopyFormatString:]_block_invoke.200
+ ___sendCategoryAddedNotification_block_invoke.cold.3
+ ___sendCategoryAddedNotification_block_invoke.cold.4
+ __block_literal_global.101
+ __block_literal_global.105
+ __block_literal_global.109
+ __block_literal_global.112
+ __block_literal_global.117
+ __block_literal_global.121
+ __block_literal_global.166
+ __block_literal_global.171
+ __block_literal_global.179
+ __block_literal_global.199
+ __block_literal_global.202
+ __block_literal_global.216
+ __block_literal_global.221
+ __block_literal_global.251
+ __block_literal_global.254
+ __block_literal_global.346
+ __block_literal_global.381
+ _objc_msgSend$decomposedStringWithCanonicalMapping
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _type_layout_string 22FreeformDataclassOwner11SQLiteErrorV
+ _type_layout_string 22FreeformDataclassOwner9SQLiteRowV
+ _type_layout_string So18ACAccountDataclassa
- CRLVersionFromNSString.cold.11
- CRLVersionFromNSString.cold.12
- CRLVersionFromNSString.cold.13
- CRLVersionFromNSString.cold.14
- _$s22FreeformDataclassOwner012CRLDataclassC0C018actionsForEnablingB02on03forB0SayypGSgSo9ACAccountCSg_So0jB0aSgtFToTm
- _$s22FreeformDataclassOwner11SQLiteErrorVwCP
- _$s22FreeformDataclassOwner11SQLiteErrorVwCPTm
- _$s22FreeformDataclassOwner11SQLiteErrorVwca
- _$s22FreeformDataclassOwner11SQLiteErrorVwcp
- _$s22FreeformDataclassOwner11SQLiteErrorVwta
- _$s22FreeformDataclassOwner11SQLiteErrorVwxx
- _$s22FreeformDataclassOwner19CRLFeatureFlagGroupC26isToolPickerItemAPIEnabledSbvgZTo
- _$s22FreeformDataclassOwner38CRLDeviceManagementRestrictionsManagerC25isMathPaperSolvingAllowedSbvpACTKTm
- _$s22FreeformDataclassOwner38CRLDeviceManagementRestrictionsManagerC25isMathPaperSolvingAllowedSbvpACTkTm
- _$sSa12_endMutationyyFyXl_Ts5
- _CRLVersionV3_3
- __47-[NSString(CRLAdditions) crl_escapeForIcuRegex]_block_invoke.98
- __70-[NSString(CRLAdditions) crl_stringByRemovingCharactersInSet:options:]_block_invoke.86
- __77-[NSString(CRLAdditions) crl_stringByUniquingPathInsideDirectory:withFormat:]_block_invoke.78
- __78+[NSString(CRLAdditions) crl_stringWithItemProviderData:typeIdentifier:error:]_block_invoke.243
- __98-[NSString(CRLAdditions) crl_regexForTitleParsingWithLocalizedCopyString:isFirstCopyFormatString:]_block_invoke.188
- __block_literal_global.100
- __block_literal_global.151
- __block_literal_global.156
- __block_literal_global.164
- __block_literal_global.187
- __block_literal_global.190
- __block_literal_global.204
- __block_literal_global.209
- __block_literal_global.242
- __block_literal_global.245
- __block_literal_global.335
- __block_literal_global.370
- __block_literal_global.84
- __block_literal_global.88
- __block_literal_global.91
- __block_literal_global.96
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_FreeformDataclassOwner
- _swift_bridgeObjectRetain
- _swift_isUniquelyReferenced_nonNull_native
CStrings:
+ "*"
+ "BatteriesIncluded"
+ "ContentLanguageCopyPaste"
+ "\\'"
+ "\\*"
+ "crl_stringByEscapingForSpotlightSearch"
+ "decomposedStringWithCanonicalMapping"
+ "isBatteriesIncludedEnabled"
+ "isContentLanguageCopyPasteEnabled"
- "ToolPickerItemAPI"
- "isToolPickerItemAPIEnabled"

```
