## WritingTools

> `/System/Library/PrivateFrameworks/WritingTools.framework/WritingTools`

```diff

-96.5.2.0.0
-  __TEXT.__text: 0x2260
-  __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_methlist: 0x5bc
-  __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x287
-  __TEXT.__constg_swiftt: 0x58
-  __TEXT.__swift5_typeref: 0x6
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x55
-  __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0xed
-  __TEXT.__objc_methname: 0xa81
-  __TEXT.__objc_methtype: 0x310
-  __TEXT.__objc_stubs: 0x5a0
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0xd8
-  __DATA_CONST.__objc_classlist: 0x38
+129.1.103.0.0
+  __TEXT.__text: 0xa380
+  __TEXT.__objc_methlist: 0x85c
+  __TEXT.__const: 0x3ea
+  __TEXT.__cstring: 0x5f7
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__oslogstring: 0x1d5
+  __TEXT.__swift5_typeref: 0x105
+  __TEXT.__constg_swiftt: 0xcc
+  __TEXT.__swift5_reflstr: 0x17a
+  __TEXT.__swift5_fieldmd: 0x150
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_proto: 0x24
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__swift5_capture: 0x6c
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0xc
+  __TEXT.__swift_as_cont: 0x20
+  __TEXT.__unwind_info: 0x380
+  __TEXT.__eh_frame: 0x418
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x240
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d8
-  __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x198
-  __AUTH_CONST.__const: 0x30
-  __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0xb50
-  __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__data: 0x240
-  __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__common: 0x18
+  __DATA_CONST.__objc_selrefs: 0x4c8
+  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__got: 0x1d8
+  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__cfstring: 0x580
+  __AUTH_CONST.__objc_const: 0x12b0
+  __AUTH_CONST.__auth_got: 0x528
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x70
+  __DATA.__data: 0x2a8
+  __DATA.__bss: 0x430
+  __DATA_DIRTY.__objc_data: 0x300
+  __DATA_DIRTY.__data: 0x138
+  __DATA_DIRTY.__common: 0x68
+  __DATA_DIRTY.__bss: 0x80
+  - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7DE0EBDC-D833-3FE1-AB55-B89F3F8FC37E
-  Functions: 85
-  Symbols:   405
-  CStrings:  234
+  UUID: F6A4593F-BC13-33DC-8B25-27C35BFDF73C
+  Functions: 268
+  Symbols:   780
+  CStrings:  116
 
Symbols:
+ +[WTFollowUpEntry entryWithSessionUUID:followUps:]
+ +[WTFollowUpEntry supportsSecureCoding]
+ +[WTFollowUpStore sharedStore]
+ -[WTAlwaysOnProofreadingPopoverAnchor .cxx_destruct]
+ -[WTAlwaysOnProofreadingPopoverAnchor initWithRect:sourceView:]
+ -[WTAlwaysOnProofreadingPopoverAnchor rect]
+ -[WTAlwaysOnProofreadingPopoverAnchor sourceView]
+ -[WTFollowUpEntry .cxx_destruct]
+ -[WTFollowUpEntry copyWithZone:]
+ -[WTFollowUpEntry creationDate]
+ -[WTFollowUpEntry encodeWithCoder:]
+ -[WTFollowUpEntry followUps]
+ -[WTFollowUpEntry initWithCoder:]
+ -[WTFollowUpEntry initWithSessionUUID:followUps:]
+ -[WTFollowUpEntry sessionUUID]
+ -[WTFollowUpStore .cxx_destruct]
+ -[WTFollowUpStore _init]
+ -[WTFollowUpStore _readEntriesFromDiskWithError:]
+ -[WTFollowUpStore _readEntriesFromDiskWithError:].cold.1
+ -[WTFollowUpStore _readEntriesFromDiskWithError:].cold.2
+ -[WTFollowUpStore _writeEntries:error:]
+ -[WTFollowUpStore _writeEntries:error:].cold.1
+ -[WTFollowUpStore _writeEntries:error:].cold.2
+ -[WTFollowUpStore _writeEntries:error:].cold.3
+ -[WTFollowUpStore _writeEntries:error:].cold.4
+ -[WTFollowUpStore _writeEntries:error:].cold.5
+ -[WTFollowUpStore allEntriesWithError:]
+ -[WTFollowUpStore allEntriesWithOptions:error:]
+ -[WTFollowUpStore entryForSessionUUID:error:]
+ -[WTFollowUpStore init]
+ -[WTFollowUpStore queue]
+ -[WTFollowUpStore setQueue:]
+ -[WTFollowUpStore(Internal) removeAllEntriesWithError:]
+ -[WTFollowUpStore(Internal) removeEntryForSessionUUID:error:]
+ -[WTFollowUpStore(Internal) writeEntry:error:]
+ -[WTSession proofreadingSessionType]
+ -[WTSession setProofreadingSessionType:]
+ -[WTTextSuggestion asCodableTextSuggestion]
+ -[WTTextSuggestion initWithOriginalRange:replacement:suggestionCategory:suggestionDescription:suggestionType:originalString:]
+ -[WTTextSuggestion originalString]
+ -[WTTextSuggestion setOriginalString:]
+ -[WTTextSuggestion setSuggestionType:]
+ -[WTTextSuggestion suggestionType]
+ GCC_except_table17
+ GCC_except_table20
+ GCC_except_table23
+ GCC_except_table8
+ _NSHomeDirectory
+ _NSLocalizedDescriptionKey
+ _NSStringFromWTTextSuggestionState
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_WTAlwaysOnProofreadingPopoverAnchor
+ _OBJC_CLASS_$_WTCodableTextSuggestion
+ _OBJC_CLASS_$_WTFollowUpEntry
+ _OBJC_CLASS_$_WTFollowUpQueryOptions
+ _OBJC_CLASS_$_WTFollowUpStore
+ _OBJC_IVAR_$_WTAlwaysOnProofreadingPopoverAnchor._rect
+ _OBJC_IVAR_$_WTAlwaysOnProofreadingPopoverAnchor._sourceView
+ _OBJC_IVAR_$_WTFollowUpEntry._creationDate
+ _OBJC_IVAR_$_WTFollowUpEntry._followUps
+ _OBJC_IVAR_$_WTFollowUpEntry._sessionUUID
+ _OBJC_IVAR_$_WTFollowUpStore._queue
+ _OBJC_IVAR_$_WTSession._proofreadingSessionType
+ _OBJC_IVAR_$_WTTextSuggestion._originalString
+ _OBJC_IVAR_$_WTTextSuggestion._suggestionType
+ _OBJC_METACLASS_$_WTAlwaysOnProofreadingPopoverAnchor
+ _OBJC_METACLASS_$_WTCodableTextSuggestion
+ _OBJC_METACLASS_$_WTFollowUpEntry
+ _OBJC_METACLASS_$_WTFollowUpQueryOptions
+ _OBJC_METACLASS_$_WTFollowUpStore
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _WTFollowUpStoreErrorDomain
+ _WTFollowUpStoreLog
+ _WTFollowUpStoreLog.cold.1
+ _WTFollowUpStoreLog.log
+ _WTFollowUpStoreLog.onceToken
+ _WTFollowUpStorePath
+ _WTFollowUpStorePath.cold.1
+ _WTFollowUpStorePath.onceToken
+ _WTFollowUpStorePath.path
+ __Block_object_dispose
+ __DATA_WTCodableTextSuggestion
+ __INSTANCE_METHODS_WTCodableTextSuggestion
+ __IVARS_WTCodableTextSuggestion
+ __IVARS__TtC12WritingTools12Availability
+ __METACLASS_DATA_WTCodableTextSuggestion
+ __NSConcreteGlobalBlock
+ __OBJC_$_CLASS_METHODS_WTAvailability(availability)
+ __OBJC_$_CLASS_METHODS_WTFollowUpEntry
+ __OBJC_$_CLASS_METHODS_WTFollowUpStore
+ __OBJC_$_CLASS_PROP_LIST_WTFollowUpEntry
+ __OBJC_$_CLASS_PROP_LIST_WTFollowUpStore
+ __OBJC_$_INSTANCE_METHODS_WTAlwaysOnProofreadingPopoverAnchor
+ __OBJC_$_INSTANCE_METHODS_WTFollowUpEntry
+ __OBJC_$_INSTANCE_METHODS_WTFollowUpStore(Internal)
+ __OBJC_$_INSTANCE_VARIABLES_WTAlwaysOnProofreadingPopoverAnchor
+ __OBJC_$_INSTANCE_VARIABLES_WTFollowUpEntry
+ __OBJC_$_INSTANCE_VARIABLES_WTFollowUpStore
+ __OBJC_$_PROP_LIST_WTAlwaysOnProofreadingPopoverAnchor
+ __OBJC_$_PROP_LIST_WTFollowUpEntry
+ __OBJC_$_PROP_LIST_WTFollowUpStore
+ __OBJC_CLASS_PROTOCOLS_$_WTFollowUpEntry
+ __OBJC_CLASS_RO_$_WTAlwaysOnProofreadingPopoverAnchor
+ __OBJC_CLASS_RO_$_WTFollowUpEntry
+ __OBJC_CLASS_RO_$_WTFollowUpQueryOptions
+ __OBJC_CLASS_RO_$_WTFollowUpStore
+ __OBJC_METACLASS_RO_$_WTAlwaysOnProofreadingPopoverAnchor
+ __OBJC_METACLASS_RO_$_WTFollowUpEntry
+ __OBJC_METACLASS_RO_$_WTFollowUpQueryOptions
+ __OBJC_METACLASS_RO_$_WTFollowUpStore
+ __PROPERTIES_WTCodableTextSuggestion
+ __Unwind_Resume
+ ___30+[WTFollowUpStore sharedStore]_block_invoke
+ ___46-[WTFollowUpStore(Internal) writeEntry:error:]_block_invoke
+ ___46-[WTFollowUpStore(Internal) writeEntry:error:]_block_invoke_2
+ ___47-[WTFollowUpStore allEntriesWithOptions:error:]_block_invoke
+ ___55-[WTFollowUpStore(Internal) removeAllEntriesWithError:]_block_invoke
+ ___61-[WTFollowUpStore(Internal) removeEntryForSessionUUID:error:]_block_invoke
+ ___61-[WTFollowUpStore(Internal) removeEntryForSessionUUID:error:]_block_invoke_2
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___NSArray0__struct
+ ___NSDictionary0__struct
+ ___WTFollowUpStoreLog_block_invoke
+ ___WTFollowUpStorePath_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e32_B32?0"WTFollowUpEntry"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e42_B24?0"WTFollowUpEntry"8"NSDictionary"16ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8r48l8s40l8r56l8
+ ___block_literal_global
+ ___block_literal_global.71
+ ___error
+ ___objc_personality_v0
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.11
+ ___swift_closure_destructor.15
+ ___swift_closure_destructor.6
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_1
+ __os_log_error_impl
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_WritingTools
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 12WritingTools12AvailabilityC7Combine16ObservableObjectAA0F19WillChangePublisherAdEP_AD0I0
+ _associated conformance 12WritingTools21CodableTextSuggestionC10CodingKeys33_61D9E43404D7CBC474513A90A7E42F43LLOSHAASQ
+ _associated conformance 12WritingTools21CodableTextSuggestionC10CodingKeys33_61D9E43404D7CBC474513A90A7E42F43LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 12WritingTools21CodableTextSuggestionC10CodingKeys33_61D9E43404D7CBC474513A90A7E42F43LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _bzero
+ _dispatch_once
+ _dispatch_queue_create
+ _dispatch_sync
+ _getpwnam
+ _getpwuid
+ _getuid
+ _objc_allocWithZone
+ _objc_autorelease
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$_init
+ _objc_msgSend$_readEntriesFromDiskWithError:
+ _objc_msgSend$_writeEntries:error:
+ _objc_msgSend$addObject:
+ _objc_msgSend$allEntriesWithError:
+ _objc_msgSend$allEntriesWithOptions:error:
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$creationDate
+ _objc_msgSend$dataWithContentsOfFile:options:error:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$date
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$followUps
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$initWithOriginalRange:replacement:suggestionCategory:suggestionDescription:suggestionType:originalString:
+ _objc_msgSend$initWithSessionUUID:followUps:
+ _objc_msgSend$initWithUUID:originalRange:replacement:suggestionCategory:suggestionDescription:state:suggestionType:originalString:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$originalString
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$proofreadingSessionType
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$queue
+ _objc_msgSend$sessionUUID
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setState:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$sharedStore
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$suggestionType
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_msgSend$writeToFile:options:error:
+ _objc_release_x1
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_setProperty_nonatomic_copy
+ _os_log_create
+ _rename
+ _sharedStore.onceToken
+ _sharedStore.sharedStore
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCast
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_setDeallocating
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _swift_willThrowTypedImpl
+ _symbolic $s7Combine16ObservableObjectP
+ _symbolic $sSY
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic Sb
+ _symbolic SbSg
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic Si
+ _symbolic So8NSObjectC
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 12WritingTools21CodableTextSuggestionC
+ _symbolic _____ 12WritingTools21CodableTextSuggestionC10CodingKeys33_61D9E43404D7CBC474513A90A7E42F43LLO
+ _symbolic _____ 16GenerativeModels0aB12AvailabilityV
+ _symbolic _____ 7Combine25ObservableObjectPublisherC
+ _symbolic _____Sg 16GenerativeModels0aB12AvailabilityV0C0O
+ _symbolic _____SgXw 12WritingTools12AvailabilityC
+ _symbolic _____SgXwz_Xx 12WritingTools12AvailabilityC
+ _symbolic ______p s5ErrorP
+ _symbolic _____y_____G s11_SetStorageC 16GenerativeModels0cD12AvailabilityV0E0O15UnavailableInfoV0F6ReasonO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12WritingTools21CodableTextSuggestionC10CodingKeys33_61D9E43404D7CBC474513A90A7E42F43LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12WritingTools21CodableTextSuggestionC10CodingKeys33_61D9E43404D7CBC474513A90A7E42F43LLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 16GenerativeModels0dE12AvailabilityV0F0O15UnavailableInfoV0G6ReasonO
+ _symbolic ytIeAgHr_
- __OBJC_$_CLASS_METHODS_WTAvailability(isAvailable)
CStrings:
+ ".tmp"
+ "Accepted"
+ "B24@?0@\"WTFollowUpEntry\"8@\"NSDictionary\"16"
+ "B32@?0@\"WTFollowUpEntry\"8Q16^B24"
+ "Failed to archive follow-up entries."
+ "Failed to archive follow-up entries: %{public}@"
+ "Failed to create store directory %{public}@: %{public}@"
+ "Failed to read follow-up store from %{public}@"
+ "Failed to rename follow-up store (errno %d)."
+ "Failed to unarchive follow-up store: %{public}@"
+ "Failed to write follow-up store temp file."
+ "Failed to write temp file %{public}@: %{public}@"
+ "Invalid"
+ "Library/Application Support"
+ "Pending"
+ "Rejected"
+ "Reviewing"
+ "Tentative"
+ "The follow-up store data is corrupt."
+ "Tmp file has been renamed to %s"
+ "Unknown (%ld)"
+ "WTFollowUpEntryCodingKeyCreationDate"
+ "WTFollowUpEntryCodingKeyFollowUps"
+ "WTFollowUpEntryCodingKeyUUID"
+ "WTFollowUpStore"
+ "WTFollowUpStoreErrorDomain"
+ "WTSessionCodingKeyOriginalString"
+ "WTSessionCodingKeyProofreadingType"
+ "WTSessionCodingKeySuggestionType"
+ "WritingTools.CodableTextSuggestion"
+ "com.apple.WritingTools.followUpStore.queue"
+ "follow_up_store.plist"
+ "init()"
+ "isEnhancedSiriAvailable value changed: %{bool}d"
+ "mobile"
+ "originalRangeLength"
+ "originalRangeLocation"
+ "originalString"
+ "rename() failed (errno=%d) for path %{public}@"
+ "suggestionType"
+ "v8@?0"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<WTTextViewDelegate_Proposed_v1>\""
- "@\"NSAttributedString\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"TIInputContextHistory\""
- "@\"WTSmartReplyConfiguration\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"<BSXPCDecoding>\"16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSObject<OS_xpc_object>\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16{_NSRange=QQ}24"
- "@40@0:8{_NSRange=QQ}16@32"
- "@48@0:8{_NSRange=QQ}16@32@40"
- "@56@0:8{_NSRange=QQ}16@32@40@48"
- "@64@0:8{_NSRange=QQ}16@32@40@48@56"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BSXPCCoding"
- "BSXPCSecureCoding"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<WTTextViewDelegate_Proposed_v1>\",W,N,V_textViewDelegate"
- "T@\"NSAttributedString\",&,V_attributedString"
- "T@\"NSAttributedString\",R,N,V_attributedText"
- "T@\"NSString\",&,N,V_baseResponse"
- "T@\"NSString\",&,N,V_entryPoint"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_replacement"
- "T@\"NSString\",R,N,V_suggestionCategory"
- "T@\"NSString\",R,N,V_suggestionDescription"
- "T@\"NSString\",R,N,V_suggestionShortDescription"
- "T@\"NSUUID\",R,N,V_uuid"
- "T@\"TIInputContextHistory\",R,N,V_inputContextHistory"
- "T@\"WTSmartReplyConfiguration\",&,N,V_smartReplyConfig"
- "TB,N,R"
- "TB,R"
- "TQ,R"
- "Tq,N,V_state"
- "Tq,R,N,V_type"
- "Tq,V_compositionSessionType"
- "T{_NSRange=QQ},N,V_range"
- "T{_NSRange=QQ},R,N,V_originalRange"
- "UTF8String"
- "UUID"
- "Vv16@0:8"
- "WTAvailability"
- "WTBSCompatibleAttributedString"
- "WTContext"
- "WTSession"
- "WTSmartReplyConfiguration"
- "WTTextSuggestion"
- "^{_NSZone=}16@0:8"
- "_TtC12WritingTools12Availability"
- "_attributedString"
- "_attributedText"
- "_baseResponse"
- "_compositionSessionType"
- "_entryPoint"
- "_inputContextHistory"
- "_originalRange"
- "_range"
- "_replacement"
- "_smartReplyConfig"
- "_state"
- "_suggestionCategory"
- "_suggestionDescription"
- "_suggestionShortDescription"
- "_textViewDelegate"
- "_type"
- "_uuid"
- "addAttributes:range:"
- "allocWithZone:"
- "allowedClasses"
- "attributedString"
- "attributedText"
- "autorelease"
- "baseResponse"
- "class"
- "compositionSessionType"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "debugDescription"
- "decodeInt64ForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "description"
- "encodeInt64:forKey:"
- "encodeObject:forKey:"
- "encodeWithBSXPCCoder:"
- "encodeWithCoder:"
- "encodeWithGeneralCoder:"
- "encodeWithXPCDictionary:"
- "entryPoint"
- "enumerateAttributesInRange:options:usingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "fallbackXPCEncodableClass"
- "hash"
- "init"
- "initWithAttributedText:range:"
- "initWithBSXPCCoder:"
- "initWithCoder:"
- "initWithGeneralCoder:"
- "initWithInputContextHistory:"
- "initWithOriginalRange:replacement:"
- "initWithOriginalRange:replacement:suggestionCategory:suggestionDescription:"
- "initWithOriginalRange:replacement:suggestionCategory:suggestionShortDescription:suggestionDescription:"
- "initWithOriginalRange:replacement:suggestionDescription:"
- "initWithString:"
- "initWithType:textViewDelegate:"
- "initWithXPCDictionary:"
- "inputContextHistory"
- "isAvailable"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isWritingToolsAllowed"
- "length"
- "originalRange"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q"
- "q16@0:8"
- "range"
- "rangeValue"
- "release"
- "requestedTool"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setAttributedString:"
- "setAttributedText:"
- "setBaseResponse:"
- "setCompositionSessionType:"
- "setEntryPoint:"
- "setObject:forKeyedSubscript:"
- "setRange:"
- "setSmartReplyConfig:"
- "setState:"
- "setTextViewDelegate:"
- "setWithObjects:"
- "sharedConnection"
- "smartReplyConfig"
- "string"
- "suggestionShortDescription"
- "superclass"
- "supportsBSXPCSecureCoding"
- "supportsSecureCoding"
- "textViewDelegate"
- "type"
- "v16@0:8"
- "v24@0:8@\"<BSXPCEncoding>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSObject<OS_xpc_object>\"16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v32@0:8{_NSRange=QQ}16"
- "valueWithRange:"
- "zone"
- "{_NSRange=\"location\"Q\"length\"Q}"
- "{_NSRange=QQ}16@0:8"

```
