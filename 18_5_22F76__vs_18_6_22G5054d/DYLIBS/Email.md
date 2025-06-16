## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3826.600.51.2.1
-  __TEXT.__text: 0xcfa3c
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0xd2fc
-  __TEXT.__gcc_except_tab: 0x1cbb8
-  __TEXT.__const: 0x36a
-  __TEXT.__cstring: 0xa139
-  __TEXT.__oslogstring: 0x6243
+3826.700.51.0.0
+  __TEXT.__text: 0xdd718
+  __TEXT.__auth_stubs: 0x14f0
+  __TEXT.__objc_methlist: 0xd3d4
+  __TEXT.__gcc_except_tab: 0x1d32c
+  __TEXT.__const: 0x11c8
+  __TEXT.__cstring: 0xb31c
+  __TEXT.__oslogstring: 0x62b3
   __TEXT.__ustring: 0x154
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__swift5_typeref: 0x71
-  __TEXT.__swift5_reflstr: 0x59
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__constg_swiftt: 0xf0
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_fieldmd: 0x40
-  __TEXT.__swift5_capture: 0x24
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x8090
-  __TEXT.__objc_classname: 0x1c2d
-  __TEXT.__objc_methname: 0x1bcd4
-  __TEXT.__objc_methtype: 0x4d6f
-  __TEXT.__objc_stubs: 0x122c0
-  __DATA_CONST.__got: 0xbc0
-  __DATA_CONST.__const: 0x4918
-  __DATA_CONST.__objc_classlist: 0x598
+  __TEXT.__constg_swiftt: 0x3e0
+  __TEXT.__swift5_typeref: 0x37d
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_reflstr: 0x294
+  __TEXT.__swift5_fieldmd: 0x3e0
+  __TEXT.__swift5_assocty: 0xf0
+  __TEXT.__swift5_proto: 0xe0
+  __TEXT.__swift5_types: 0x58
+  __TEXT.__swift5_capture: 0x38
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__unwind_info: 0x83d8
+  __TEXT.__eh_frame: 0x1f8
+  __TEXT.__objc_classname: 0x1c40
+  __TEXT.__objc_methname: 0x1be26
+  __TEXT.__objc_methtype: 0x4dc7
+  __TEXT.__objc_stubs: 0x12320
+  __DATA_CONST.__got: 0xc68
+  __DATA_CONST.__const: 0x48f8
+  __DATA_CONST.__objc_classlist: 0x5a8
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x350
+  __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f08
-  __DATA_CONST.__objc_protorefs: 0x108
+  __DATA_CONST.__objc_selrefs: 0x5f50
+  __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__auth_got: 0x7b8
-  __AUTH_CONST.__const: 0x13b0
-  __AUTH_CONST.__cfstring: 0x9320
-  __AUTH_CONST.__objc_const: 0x174a0
+  __AUTH_CONST.__auth_got: 0xa88
+  __AUTH_CONST.__const: 0x1a80
+  __AUTH_CONST.__cfstring: 0x9360
+  __AUTH_CONST.__objc_const: 0x17640
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x370
-  __AUTH.__data: 0x8
+  __AUTH.__objc_data: 0x4b0
+  __AUTH.__data: 0x210
   __DATA.__objc_ivar: 0xc80
-  __DATA.__data: 0x27f8
-  __DATA.__bss: 0x3a0
+  __DATA.__data: 0x2ba8
+  __DATA.__bss: 0x1df0
   __DATA_DIRTY.__objc_data: 0x3590
-  __DATA_DIRTY.__data: 0x60
-  __DATA_DIRTY.__bss: 0x6a0
+  __DATA_DIRTY.__data: 0xb0
+  __DATA_DIRTY.__bss: 0x640
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: FC263CA1-1A56-3B2D-9750-FC16A57B52F1
-  Functions: 4711
-  Symbols:   18593
-  CStrings:  8365
+  UUID: 8EF4CF6E-E0AA-346D-B516-086902E6BFF4
+  Functions: 5072
+  Symbols:   18765
+  CStrings:  8447
 
Symbols:
+ +[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:]
+ -[EMMessageList collection:changedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:]
+ -[EMSectionedMessageList collection:changedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:]
+ -[_EMMessageRepositoryQueryObserver remoteCancelable]
+ -[_EMMessageRepositoryQueryObserver setRemoteCancelable:]
+ GCC_except_table208
+ GCC_except_table209
+ GCC_except_table215
+ GCC_except_table219
+ GCC_except_table220
+ GCC_except_table225
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table235
+ GCC_except_table250
+ GCC_except_table251
+ GCC_except_table264
+ GCC_except_table267
+ GCC_except_table268
+ GCC_except_table274
+ _EMUserDefaultPreferBIMIOverBrandedMail
+ _NSLocalizedDescriptionKey
+ _NSLocalizedFailureReasonErrorKey
+ _OBJC_CLASS_$_EMActivityStateObserver
+ _OBJC_CLASS_$_EMIMAPSyncError
+ _OBJC_METACLASS_$_EMActivityStateObserver
+ _OBJC_METACLASS_$_EMIMAPSyncError
+ _OBJC_METACLASS_$_NSError
+ _SecCopyErrorMessageString
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS_EMIMAPSyncError
+ __CLASS_PROPERTIES_EMIMAPSyncError
+ __DATA_EMActivityStateObserver
+ __DATA_EMIMAPSyncError
+ __INSTANCE_METHODS_EMActivityStateObserver
+ __INSTANCE_METHODS_EMIMAPSyncError
+ __IVARS_EMActivityStateObserver
+ __IVARS_EMIMAPSyncError
+ __METACLASS_DATA_EMActivityStateObserver
+ __METACLASS_DATA_EMIMAPSyncError
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EMActivityObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EMActivityObserver
+ __OBJC_$_PROTOCOL_REFS_EMActivityObserver
+ __OBJC_LABEL_PROTOCOL_$_EMActivityObserver
+ __OBJC_PROTOCOL_$_EMActivityObserver
+ __PROPERTIES_EMIMAPSyncError
+ __PROTOCOLS_EMActivityStateObserver
+ __PROTOCOLS_EMActivityStateObserver.22
+ ___108-[EMMessageList collection:changedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:]_block_invoke
+ ___116-[EMInMemoryThreadCollection initWithQuery:mailboxTypeResolver:dataSource:delgate:scheduler:logClient:limitedCache:]_block_invoke.17
+ ___117-[EMSectionedMessageList collection:changedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:]_block_invoke
+ ___154+[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:]_block_invoke
+ ___154+[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:]_block_invoke_2
+ ___154+[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:]_block_invoke_3
+ ___154+[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:]_block_invoke_4
+ ___93-[EMInMemoryThreadCollection _nts_objectIDDidChangeForMessage:oldObjectID:oldConversationID:]_block_invoke.75
+ ___99+[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:extraInfo:]_block_invoke_3
+ ___block_descriptor_64_ea8_32s40s48r56r_e38_v16?0"<EMCollectionChangeObserver>"8lr48l8r56l8s32l8s40l8
+ ___block_descriptor_96_ea8_32s40s48s56s64s72s_e38_v16?0"<EMCollectionChangeObserver>"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.367
+ ___block_literal_global.52
+ ___block_literal_global.59
+ ___block_literal_global.71
+ ___block_literal_global.83
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_memcpy16_8
+ ___swift_memcpy1_1
+ ___swift_memcpy33_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_boxed_opaque_existential_1
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ _associated conformance 5Email21ActivityStateObserverC0bC0V4KindOSHAASQ
+ _associated conformance 5Email21ActivityStateObserverC0bC0V7RunningOSHAASQ
+ _associated conformance So15EMIMAPSyncErrorC5EmailE10UnderlyingV10CodingKeys33_AD84E3936752491525D28BF4D8222A8ALLOSHACSQ
+ _associated conformance So15EMIMAPSyncErrorC5EmailE10UnderlyingV10CodingKeys33_AD84E3936752491525D28BF4D8222A8ALLOs0E3KeyACs23CustomStringConvertible
+ _associated conformance So15EMIMAPSyncErrorC5EmailE10UnderlyingV10CodingKeys33_AD84E3936752491525D28BF4D8222A8ALLOs0E3KeyACs28CustomDebugStringConvertible
+ _associated conformance So15EMIMAPSyncErrorC5EmailE10UnderlyingV4KindOSHACSQ
+ _associated conformance So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO10CodingKeysOSHACSQ
+ _associated conformance So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO10CodingKeysOs0F3KeyACs23CustomStringConvertible
+ _associated conformance So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO10CodingKeysOs0F3KeyACs28CustomDebugStringConvertible
+ _associated conformance So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO4Kind33_AD84E3936752491525D28BF4D8222A8ALLOSHACSQ
+ _associated conformance So19NSKeyValueChangeKeyaSHSCSQ
+ _associated conformance So19NSKeyValueChangeKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So19NSKeyValueChangeKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _associated conformance So21EMActivityUserInfoKeyaSHSCSQ
+ _associated conformance So21EMActivityUserInfoKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So21EMActivityUserInfoKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _associated conformance So21NSProgressUserInfoKeyaSHSCSQ
+ _associated conformance So21NSProgressUserInfoKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So21NSProgressUserInfoKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _flat unique So12EFCancelable_p
+ _get_enum_tag_for_layout_string 5Email21ActivityStateObserverC0C0O
+ _get_enum_tag_for_layout_string So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO
+ _get_type_metadata 15Synchronization5MutexVy5Email21ActivityStateObserverC0E0OG.24
+ _objc_msgSend$collection:changedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:
+ _objc_msgSend$collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:
+ _objc_msgSend$remoteCancelable
+ _objc_msgSend$setOrInsertObject:forKey:atIndex:
+ _objc_msgSend$setRemoteCancelable:
+ _swift_allocBox
+ _swift_allocError
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassFromObject
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_runtimeSupportsNoncopyableTypes
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unexpectedError
+ _swift_unknownObjectRelease
+ _swift_unknownObjectWeakAssign
+ _swift_willThrow
+ _symbolic $s5Email29ActivityStateObserverDelegateP
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic SSSg4code_AA4textt
+ _symbolic SS_ypt
+ _symbolic Say_____G 5Email21ActivityStateObserverC08ObservedB0V
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic So10EMActivityC
+ _symbolic So10NSProgressCSg
+ _symbolic So15EMIMAPSyncErrorC
+ _symbolic So17EMMailboxObjectIDC
+ _symbolic So24OS_dispatch_queue_serialC
+ _symbolic So7NSErrorCSg
+ _symbolic So8NSStringC
+ _symbolic _____ 5Email21ActivityStateObserverC
+ _symbolic _____ 5Email21ActivityStateObserverC08ObservedB0V
+ _symbolic _____ 5Email21ActivityStateObserverC0C0O
+ _symbolic _____ 5Email21ActivityStateObserverC0C0O10RegisteredV
+ _symbolic _____ 5Email21ActivityStateObserverC0bC0V
+ _symbolic _____ 5Email21ActivityStateObserverC0bC0V4KindO
+ _symbolic _____ 5Email21ActivityStateObserverC0bC0V7RunningO
+ _symbolic _____ 5Email21ActivityStateObserverC6UpdateV
+ _symbolic _____ 6Darwin14POSIXErrorCodeO
+ _symbolic _____ So14EMActivityTypeV
+ _symbolic _____ So15EMIMAPSyncErrorC5EmailE10UnderlyingV
+ _symbolic _____ So15EMIMAPSyncErrorC5EmailE10UnderlyingV10CodingKeys33_AD84E3936752491525D28BF4D8222A8ALLO
+ _symbolic _____ So15EMIMAPSyncErrorC5EmailE10UnderlyingV4KindO
+ _symbolic _____ So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO
+ _symbolic _____ So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO10CodingKeysO
+ _symbolic _____ So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO14UnableToDecode33_AD84E3936752491525D28BF4D8222A8ALLV
+ _symbolic _____ So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO4Kind33_AD84E3936752491525D28BF4D8222A8ALLO
+ _symbolic _____ So19NSKeyValueChangeKeya
+ _symbolic _____ So20EMActivityFetchStateV
+ _symbolic _____ So21EMActivityUserInfoKeya
+ _symbolic _____ So21NSProgressUserInfoKeya
+ _symbolic _____ s5Int32V
+ _symbolic _____ s5UInt8V
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg 5Email21ActivityStateObserverC0bC0V
+ _symbolic _____Sg 5Email21ActivityStateObserverC6UpdateV
+ _symbolic _____Sg So15EMIMAPSyncErrorC5EmailE10UnderlyingV
+ _symbolic _____Sg So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO
+ _symbolic _____Sg So20EMActivityFetchStateV
+ _symbolic _____Sg_ABt 10Foundation4DateV
+ _symbolic ______p So12EFCancelableP
+ _symbolic ______pSg 5Email29ActivityStateObserverDelegateP
+ _symbolic ______pSgXw 5Email29ActivityStateObserverDelegateP
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____y_____G 15Synchronization5MutexVAARi_zrlE 5Email21ActivityStateObserverC0E0O
+ _symbolic _____y_____G s22KeyedDecodingContainerV So15EMIMAPSyncErrorC5EmailE10UnderlyingV10CodingKeys33_AD84E3936752491525D28BF4D8222A8ALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So15EMIMAPSyncErrorC5EmailE10UnderlyingV10CodingKeys33_AD84E3936752491525D28BF4D8222A8ALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO10CodingKeysO
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _symbolic x
+ _symbolic ypSg
+ _type_layout_string 5Email21ActivityStateObserverC08ObservedB0V
+ _type_layout_string 5Email21ActivityStateObserverC0C0O
+ _type_layout_string 5Email21ActivityStateObserverC0C0O10RegisteredV
+ _type_layout_string So15EMIMAPSyncErrorC5EmailE10UnderlyingV7DetailsO
+ _type_layout_string So19NSKeyValueChangeKeya
- +[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:]
- -[EMMessageList collection:changedItemIDs:itemIDsWithCountChanges:]
- -[EMSectionedMessageList collection:changedItemIDs:itemIDsWithCountChanges:]
- GCC_except_table206
- GCC_except_table207
- GCC_except_table211
- GCC_except_table216
- GCC_except_table217
- GCC_except_table221
- GCC_except_table228
- GCC_except_table229
- GCC_except_table233
- GCC_except_table234
- GCC_except_table237
- GCC_except_table262
- GCC_except_table265
- GCC_except_table266
- GCC_except_table272
- ___113+[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:]_block_invoke
- ___113+[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:]_block_invoke_2
- ___113+[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:]_block_invoke_3
- ___113+[EMMessageListChangeObserverHelper collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:]_block_invoke_4
- ___116-[EMInMemoryThreadCollection initWithQuery:mailboxTypeResolver:dataSource:delgate:scheduler:logClient:limitedCache:]_block_invoke.16
- ___63-[EMInMemoryThreadCollection messageListItemForObjectID:error:]_block_invoke_2
- ___67-[EMMessageList collection:changedItemIDs:itemIDsWithCountChanges:]_block_invoke
- ___76-[EMSectionedMessageList collection:changedItemIDs:itemIDsWithCountChanges:]_block_invoke
- ___93-[EMInMemoryThreadCollection _nts_objectIDDidChangeForMessage:oldObjectID:oldConversationID:]_block_invoke.73
- ___block_descriptor_40_ea8_32s_e36_"EMThreadObjectID"16?0"NSNumber"8ls32l8
- ___block_descriptor_56_ea8_32s40s48r_e38_v16?0"<EMCollectionChangeObserver>"8lr48l8s32l8s40l8
- ___block_descriptor_88_ea8_32s40s48s56s64s_e38_v16?0"<EMCollectionChangeObserver>"8ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.31
- ___block_literal_global.364
- ___block_literal_global.50
- ___block_literal_global.57
- ___block_literal_global.67
- ___block_literal_global.81
- _objc_msgSend$collection:changedItemIDs:itemIDsWithCountChanges:
- _objc_msgSend$collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:
CStrings:
+ "!b"
+ "0x%lx Activity 0x%lx did change"
+ "0x%lx Did start activity 0x%lx"
+ "0x%lx Starting."
+ "@\"EFMutableOrderedDictionary\""
+ "A server error occurred."
+ "A server error occurred. Will try to connect again at %1$@."
+ "Authenticating with the server failed. Please check the settings for this account."
+ "Authenticating with the server failed. Please check the settings for this account. Will try to connect again at %1$@."
+ "EMActivityObserver"
+ "EMActivityStateObserver"
+ "EMIMAPSyncError"
+ "Email.ActivityStateObserver"
+ "Email/EMActivityStateObserver.swift"
+ "Email/EMIMAPSyncError.swift"
+ "Fatal error"
+ "Need to call tearDown() before instance gets deallocated."
+ "Network error (DNS %1$@)."
+ "Network error (POSIX %1$@)."
+ "Notifying observer of %lu changed itemIDs (%lu with count changes, %lu with brand indicator changes): <%@: %p>\n%@"
+ "PreferBIMIOverBrandedMail"
+ "Server code “%1$@”"
+ "Server code “%1$@”, server message “%2$@”."
+ "Server message “%1$@”."
+ "T@\"<EFCancelable>\",&,V_remoteCancelable"
+ "T@\"NSDictionary\",N,R"
+ "TB,N,R"
+ "The server can not be reached."
+ "The server can not be reached. Will try to connect again at %1$@."
+ "The server is temporarily unavailable."
+ "The server is temporarily unavailable. Will try to connect again at %1$@."
+ "The server sent an unexpected response that could not be parsed."
+ "The server sent an unexpected response that could not be parsed. Will try to connect again at %1$@."
+ "There was an issue with the network."
+ "There was an issue with the network. Will try to connect again at %1$@."
+ "This is a (technical) description of an error that the mail server reported to us."
+ "This is a (technical) description of an underlying network error we hit while communicating with the mail server."
+ "This is a (technical) description of an underlying network error we hit while communicating with the mail server. The quoted text is an error description, the 2nd value is an error code."
+ "This is a (technical) description of an underlying network error we hit while communicating with the mail server. The value is an error code."
+ "This is an error message that gets displayed when the mail server is rejecting the credentials (e.g. username and/or password) that the user has entered for this account."
+ "This is an error message that gets displayed when the mail server is rejecting the credentials (e.g. username and/or password) that the user has entered for this account. We will automatically try again at the specified time (e.g. 06:12:34)."
+ "This is an error message that gets displayed when the mail server is temporarily unavailable, e.g. when it is too busy, or down for service."
+ "This is an error message that gets displayed when the mail server is temporarily unavailable, e.g. when it is too busy, or down for service. We will automatically try again at the specified time (e.g. 06:12:34)."
+ "This is an error message that gets displayed when the mail server sends something to us that we can’t make any sense of, and thus fail to sync."
+ "This is an error message that gets displayed when the mail server sends something to us that we can’t make any sense of, and thus fail to sync. We will automatically try again at the specified time (e.g. 06:12:34)."
+ "This is an error message that gets displayed when the network connection to the mail server drops."
+ "This is an error message that gets displayed when the network connection to the mail server drops. We will automatically try again at the specified time (e.g. 06:12:34)."
+ "This is an error message that gets displayed when there’s an error on the mail server that caused us to stop syncing."
+ "This is an error message that gets displayed when there’s an error on the mail server that caused us to stop syncing. We will automatically try again at the specified time (e.g. 06:12:34)."
+ "This is an error message that gets displayed when we’re unable to connect to the mail server."
+ "This is an error message that gets displayed when we’re unable to connect to the mail server. We will automatically try again at the specified time (e.g. 06:12:34)."
+ "Trying to start ActivityStateObserver after it was torn down."
+ "Trying to start ActivityStateObserver while it is already running."
+ "Unable to create a secure connection to the server (%1$@)."
+ "Unable to create a secure connection to the server (”%1$@” %2$@)."
+ "_underlying"
+ "brandIndicatorLocation: %@"
+ "bundleForClass:"
+ "collection:changedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:"
+ "collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:"
+ "com.apple.email.imap.sync"
+ "connectionEstablished"
+ "currentLocale"
+ "downloadingMessages"
+ "initWithDomain:code:userInfo:"
+ "initWithInt:"
+ "k"
+ "nc"
+ "queue"
+ "remoteCancelable"
+ "removeObserver:forKeyPath:context:"
+ "sc"
+ "setLocalizedDateFormatFromTemplate:"
+ "setOrInsertObject:forKey:atIndex:"
+ "setRemoteCancelable:"
+ "v32@0:8@\"EMActivityRegistry\"16@\"EMActivity\"24"
+ "v48@0:8@\"<EMCollection>\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40"
- "!r"
- "@\"EMThreadObjectID\"16@?0@\"NSNumber\"8"
- "Notifying observer of %lu changed itemIDs (%lu with count changes): <%@: %p>\n%@"
- "collection:changedItemIDs:itemIDsWithCountChanges:"
- "collection:notifyChangeObserversAboutChangedItemIDs:itemIDsWithCountChanges:"
- "v40@0:8@\"<EMCollection>\"16@\"NSArray\"24@\"NSArray\"32"

```
