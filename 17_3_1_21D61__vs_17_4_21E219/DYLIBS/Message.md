## Message

> `/System/Library/PrivateFrameworks/Message.framework/Message`

```diff

-3774.400.21.0.0
-  __TEXT.__text: 0x9e3c38
-  __TEXT.__auth_stubs: 0x72b0
-  __TEXT.__objc_methlist: 0x117ec
-  __TEXT.__gcc_except_tab: 0x31780
-  __TEXT.__const: 0x42a70
-  __TEXT.__cstring: 0x3c7ab
-  __TEXT.__oslogstring: 0xe276
+3774.500.171.2.2
+  __TEXT.__text: 0x9ec0d8
+  __TEXT.__auth_stubs: 0x7180
+  __TEXT.__objc_methlist: 0x117e4
+  __TEXT.__gcc_except_tab: 0x31800
+  __TEXT.__const: 0x42e10
+  __TEXT.__cstring: 0x3c54b
+  __TEXT.__oslogstring: 0xe32e
   __TEXT.__ustring: 0x22b2
-  __TEXT.__swift5_typeref: 0xe780
-  __TEXT.__constg_swiftt: 0xac9c
-  __TEXT.__swift5_reflstr: 0xc7e6
-  __TEXT.__swift5_fieldmd: 0x10df8
-  __TEXT.__swift5_builtin: 0xcd0
-  __TEXT.__swift5_assocty: 0x2098
-  __TEXT.__swift5_capture: 0x236c4
+  __TEXT.__swift5_typeref: 0xe6b8
+  __TEXT.__constg_swiftt: 0xacb0
+  __TEXT.__swift5_reflstr: 0xc846
+  __TEXT.__swift5_fieldmd: 0x10e60
+  __TEXT.__swift5_builtin: 0xce4
+  __TEXT.__swift5_assocty: 0x2080
+  __TEXT.__swift5_capture: 0x23998
   __TEXT.__swift5_proto: 0x204c
-  __TEXT.__swift5_types: 0x1310
-  __TEXT.__swift5_mpenum: 0xaf4
+  __TEXT.__swift5_types: 0x1318
+  __TEXT.__swift5_mpenum: 0xb10
   __TEXT.__swift5_protos: 0x5c
-  __TEXT.__unwind_info: 0x300d0
-  __TEXT.__eh_frame: 0x21480
+  __TEXT.__unwind_info: 0x2fc40
+  __TEXT.__eh_frame: 0x1e9d8
   __TEXT.__objc_classname: 0x286a
-  __TEXT.__objc_methname: 0x2cf53
+  __TEXT.__objc_methname: 0x2ce1f
   __TEXT.__objc_methtype: 0x6324
-  __TEXT.__objc_stubs: 0x23f00
-  __DATA_CONST.__got: 0x1730
-  __DATA_CONST.__const: 0x14e10
-  __DATA_CONST.__objc_classlist: 0xa98
+  __TEXT.__objc_stubs: 0x23ec0
+  __DATA_CONST.__got: 0x1738
+  __DATA_CONST.__const: 0x14e20
+  __DATA_CONST.__objc_classlist: 0xa90
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x418
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1bcf8
-  __DATA_CONST.__objc_selrefs: 0xae38
+  __DATA_CONST.__objc_const: 0x1bc18
+  __DATA_CONST.__objc_selrefs: 0xadc8
+  __DATA_CONST.__objc_protorefs: 0x110
+  __DATA_CONST.__objc_classrefs: 0x1230
+  __DATA_CONST.__objc_superrefs: 0x690
   __DATA_CONST.__objc_arraydata: 0xee8
   __AUTH_CONST.__cfstring: 0x17f20
-  __AUTH_CONST.__const: 0x866f0
+  __AUTH_CONST.__const: 0x86f90
   __AUTH_CONST.__objc_const: 0x73f8
   __AUTH_CONST.__objc_arrayobj: 0xb58
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x3970
-  __AUTH.__objc_data: 0x4e90
-  __AUTH.__data: 0x6408
-  __DATA.__objc_protorefs: 0x110
-  __DATA.__objc_classrefs: 0x1240
-  __DATA.__objc_superrefs: 0x690
+  __AUTH_CONST.__auth_got: 0x38d8
+  __AUTH.__objc_data: 0x4e40
+  __AUTH.__data: 0x6368
   __DATA.__objc_ivar: 0x1324
-  __DATA.__data: 0x1c9a0
+  __DATA.__data: 0x1eb60
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x32e80
-  __DATA.__common: 0x600
+  __DATA.__bss: 0x32bf0
+  __DATA.__common: 0x5d0
   __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0x440
+  __DATA_DIRTY.__bss: 0x450
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8EEC9E39-CE49-36D3-AB90-A6BD77D4221A
-  Functions: 63998
-  Symbols:   42158
-  CStrings:  19240
+  UUID: EF037060-8F61-3124-9E46-2EB0F2C53C7E
+  Functions: 63718
+  Symbols:   42087
+  CStrings:  19216
 
Symbols:
+ +[MFOutgoingMessageDelivery log]
+ -[MFOutgoingMessageDelivery _deliverSynchronouslyWithCurrentSettings:].cold.1
+ -[MFOutgoingMessageDelivery _deliveryAccountForInitializers].cold.1
+ -[MFOutgoingMessageDelivery deliverSynchronouslyWithCompletion:].cold.1
+ -[MFSMTPDelivery deliverMessageData:toRecipients:].cold.2
+ _OBJC_CLASS_$_EFSQLBitExpression
+ __AddFilterPredicateToInboxThreadScopes
+ __OBJC_$_PROP_LIST_MFActivityCondition.148
+ __PROTOCOLS__TtCCCC7Message25InProgressMessageDownload26AttachmentDecoderAndWriter7DecoderP33_E488F2EBCE7947B89745EE1E7B527BA212DataConsumer.16
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__114default_deleteIA_11DetailEntryEclB8ue170006IS1_EENS3_20_EnableIfConvertibleIT_E4typeEPS6_
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKc8EncodingEENS_22__unordered_map_hasherIS3_S5_20CStringAlnumCaseHash21CStringAlnumCaseEqualLb1EEENS_21__unordered_map_equalIS3_S5_S8_S7_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_performB8ue170006EPNS_11__hash_nodeIS5_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKc8EncodingEENS_22__unordered_map_hasherIS3_S5_20CStringAlnumCaseHash21CStringAlnumCaseEqualLb1EEENS_21__unordered_map_equalIS3_S5_S8_S7_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_prepareB8ue170006EmRS5_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006EPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006ILi0EEEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
+ __ZNSt3__113unordered_mapIPKc8Encoding20CStringAlnumCaseHash21CStringAlnumCaseEqualNS_9allocatorINS_4pairIKS2_S3_EEEEED1B8ue170006Ev
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___141-[MFMailMessageLibrary addMessages:withMailbox:newMessagesByOldMessage:remoteIDs:setFlags:addPOPUIDs:dataSectionsByMessage:generationWindow:]_block_invoke.666
+ ___141-[MFMailMessageLibrary addMessages:withMailbox:newMessagesByOldMessage:remoteIDs:setFlags:addPOPUIDs:dataSectionsByMessage:generationWindow:]_block_invoke.791
+ ___24-[_MFDataCollector done]_block_invoke.2363
+ ___32+[MFOutgoingMessageDelivery log]_block_invoke
+ ___43-[MFActivityCondition conditionsObservable]_block_invoke.75
+ ___43-[MFActivityCondition conditionsObservable]_block_invoke.75.cold.1
+ ___62-[MFMessageContentRequest _processContentLoadingContextEvent:]_block_invoke.103
+ ___62-[MFMessageContentRequest _processContentLoadingContextEvent:]_block_invoke.74
+ ___62-[MFMessageContentRequest _processContentLoadingContextEvent:]_block_invoke.74.cold.1
+ ___62-[MFMessageContentRequest _processContentLoadingContextEvent:]_block_invoke.81
+ ___62-[MFMessageContentRequest _processContentLoadingContextEvent:]_block_invoke_2.107
+ ___62-[MFMessageContentRequest _processContentLoadingContextEvent:]_block_invoke_2.87
+ ___62-[MFMessageContentRequest _processContentLoadingContextEvent:]_block_invoke_3.94
+ ___86-[MFMailMessageLibrary messageWithLibraryID:options:inMailbox:temporarilyUnavailable:]_block_invoke.1172
+ ___88-[MFMessageContentRequest _contentRepresentationForLoadingEvent:existingRepresentation:]_block_invoke.119.cold.1
+ ___88-[MFMessageContentRequest _contentRepresentationForLoadingEvent:existingRepresentation:]_block_invoke.121
+ ___88-[MFMessageContentRequest _contentRepresentationForLoadingEvent:existingRepresentation:]_block_invoke.125
+ ___88-[MFMessageContentRequest _contentRepresentationForLoadingEvent:existingRepresentation:]_block_invoke_2.122
+ ___88-[MFMessageContentRequest _contentRepresentationForLoadingEvent:existingRepresentation:]_block_invoke_2.122.cold.1
+ ___91-[MFMessageContentRequest _requestContentForAttachment:manager:options:managed:completion:]_block_invoke.135
+ ___91-[MFMessageContentRequest _requestContentForAttachment:manager:options:managed:completion:]_block_invoke.143
+ ___91-[MFMessageContentRequest _requestContentForAttachment:manager:options:managed:completion:]_block_invoke_2.136
+ ___91-[MFMessageContentRequest _requestContentForAttachment:manager:options:managed:completion:]_block_invoke_2.136.cold.1
+ ___91-[MFMessageContentRequest _requestContentForAttachment:manager:options:managed:completion:]_block_invoke_2.146
+ ___block_descriptor_56_ea8_32s40s48bs_e50_v24?0"<EMExtendedContentItem>"8"MFAttachment"16ls32l8s40l8s48l8
+ ___block_literal_global.1017
+ ___block_literal_global.1284
+ ___block_literal_global.1321
+ ___block_literal_global.1489
+ ___block_literal_global.1527
+ ___block_literal_global.1533
+ ___block_literal_global.1547
+ ___block_literal_global.253
+ ___block_literal_global.2624
+ ___block_literal_global.2641
+ ___block_literal_global.2694
+ ___block_literal_global.2700
+ ___block_literal_global.349
+ ___block_literal_global.447
+ ___block_literal_global.480
+ ___block_literal_global.589
+ ___block_literal_global.679
+ ___block_literal_global.775
+ ___block_literal_global.78
+ ___block_literal_global.802
+ ___block_literal_global.803
+ ___block_literal_global.821
+ ___block_literal_global.859
+ ___block_literal_global.907
+ ___block_literal_global.915
+ ___block_literal_global.927
+ ___block_literal_global.930
+ ___block_literal_global.933
+ ___block_literal_global.994
+ ___fetchArgumentsForCriterion_block_invoke.478
+ ___swift_memcpy5_2
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_Message
+ __unnamed_array_storage.462
+ __unnamed_array_storage.662
+ __unnamed_array_storage.671
+ __unnamed_array_storage.674
+ __unnamed_array_storage.693
+ __unnamed_array_storage.707
+ __unnamed_array_storage.713
+ __unnamed_array_storage.722
+ __unnamed_array_storage.756
+ __unnamed_array_storage.766
+ __unnamed_array_storage.769
+ __unnamed_array_storage.772
+ __unnamed_array_storage.785
+ __unnamed_array_storage.788
+ __unnamed_array_storage.794
+ __unnamed_array_storage.800
+ __unnamed_array_storage.812
+ __unnamed_array_storage.815
+ __unnamed_array_storage.818
+ __unnamed_array_storage.826
+ __unnamed_array_storage.829
+ __unnamed_array_storage.832
+ __unnamed_array_storage.835
+ __unnamed_array_storage.838
+ __unnamed_array_storage.856
+ __unnamed_array_storage.874
+ __unnamed_array_storage.880
+ __unnamed_array_storage.904
+ __unnamed_array_storage.950
+ _block_copy_helper.190
+ _block_copy_helper.202
+ _block_copy_helper.211
+ _block_copy_helper.26
+ _block_copy_helper.261
+ _block_copy_helper.270
+ _block_copy_helper.276
+ _block_copy_helper.3181
+ _block_copy_helper.320
+ _block_copy_helper.327
+ _block_copy_helper.3553
+ _block_copy_helper.3559
+ _block_copy_helper.373
+ _block_copy_helper.431
+ _block_copy_helper.4892
+ _block_copy_helper.4907
+ _block_copy_helper.4913
+ _block_copy_helper.4917
+ _block_copy_helper.4929
+ _block_copy_helper.5129
+ _block_copy_helper.580
+ _block_copy_helper.6
+ _block_descriptor.192
+ _block_descriptor.204
+ _block_descriptor.213
+ _block_descriptor.263
+ _block_descriptor.272
+ _block_descriptor.278
+ _block_descriptor.28
+ _block_descriptor.3183
+ _block_descriptor.322
+ _block_descriptor.329
+ _block_descriptor.3555
+ _block_descriptor.3561
+ _block_descriptor.375
+ _block_descriptor.433
+ _block_descriptor.4894
+ _block_descriptor.4909
+ _block_descriptor.4915
+ _block_descriptor.4919
+ _block_descriptor.4931
+ _block_descriptor.5131
+ _block_descriptor.582
+ _block_descriptor.8
+ _block_destroy_helper.191
+ _block_destroy_helper.203
+ _block_destroy_helper.212
+ _block_destroy_helper.262
+ _block_destroy_helper.27
+ _block_destroy_helper.271
+ _block_destroy_helper.277
+ _block_destroy_helper.3182
+ _block_destroy_helper.321
+ _block_destroy_helper.328
+ _block_destroy_helper.3554
+ _block_destroy_helper.3560
+ _block_destroy_helper.374
+ _block_destroy_helper.432
+ _block_destroy_helper.4893
+ _block_destroy_helper.4908
+ _block_destroy_helper.4914
+ _block_destroy_helper.4918
+ _block_destroy_helper.4930
+ _block_destroy_helper.5130
+ _block_destroy_helper.581
+ _block_destroy_helper.7
+ _objc_msgSend$encryptionLevelForSender:forAdvertisement:useGCM:encryptSubject:
+ _objc_msgSend$ifNull:second:
+ _objc_msgSend$initWithTable:conflictResolution:
+ _objc_msgSend$mf_stringWithData:encoding:
+ _objc_msgSend$or:with:
+ _objc_msgSend$resultIfAvailable
+ _sec_protocol_options_set_verify_block
+ _swift_unknownObjectRetain_n
+ _symbolic SaySJG
+ _symbolic Say_____G 13IMAP2Behavior14StateWithTasksV13InSyncMailboxV
+ _symbolic Say_____G______t 16IMAP2Persistence11CredentialsO 0A10Connection20UnauthenticatedStateO11TLSMetadataO
+ _symbolic SbIeyBy_
+ _symbolic _____ 13IMAP2Behavior14StateWithTasksV13InSyncMailboxV
+ _symbolic _____ 15IMAP2Connection0B13ConfigurationV22TransportLayerSecurityO
+ _symbolic _____ 15IMAP2Connection20UnauthenticatedStateO11TLSMetadataO
+ _symbolic _____ 15IMAP2Connection29UnauthenticatedStateWithTasksV11tlsDidStart0G06loggeryAA0cD0O11TLSMetadataO_AA0B0C6LoggerVtKF010UnexpectedhI3TLSL_V
+ _symbolic _____ 7Message10makeUnique33_9756C92D0D431C9DA10B9422B1759BA4LL9mailboxes07skipNonC06loggerSDy12NIOIMAPCore211MailboxNameVAA0Q10UpdateTreeACLLV7ElementVGSayAMG_SbAA18PersistenceAdaptorC6LoggerVtKF0q11NamesAreNotC0L_V
+ _symbolic _____ 7Message17MailboxUpdateTree33_9756C92D0D431C9DA10B9422B1759BA4LLV4make7account9namespace13pathSeparator9mimeCache13skipNonUnique6loggerADSo11IMAPAccountC_13IMAP2Protocol9NamespaceVSgSJSg0Y4MIME0S0CSbAA18PersistenceAdaptorC6LoggerVtKFZ017AccountHasNilRootB0L_V
+ _symbolic _____ 7Message17MailboxUpdateTree33_9756C92D0D431C9DA10B9422B1759BA4LLV4make7account9namespace13pathSeparator9mimeCache13skipNonUnique6loggerADSo11IMAPAccountC_13IMAP2Protocol9NamespaceVSgSJSg0Y4MIME0S0CSbAA18PersistenceAdaptorC6LoggerVtKFZ21AccountHasNilChildrenL_V
+ _symbolic _____ 7Message17MailboxUpdateTree33_9756C92D0D431C9DA10B9422B1759BA4LLV7ElementV4make7mailbox7account13pathSeparatorSayAFGSo12MFMailboxUidC_So11IMAPAccountCSJSgtKFZ04PathR9IsUnknownL_V
+ _symbolic _____ 7Message17MailboxUpdateTree33_9756C92D0D431C9DA10B9422B1759BA4LLV7ElementV4make7mailbox7account13pathSeparatorSayAFGSo12MFMailboxUidC_So11IMAPAccountCSJSgtKFZ0B13NameIsUnknownL_V
+ _symbolic _____ 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localL05limitSayAC4MoveVG_AA0k5LocalL0VtSaySo07ECLocalA6ActionCG_SitF06TargetjR0L_V
+ _symbolic _____ 9IMAP2MIME8RFC_2231O34EncodedWithCharacterSetAndLanguageV
+ _symbolic _____Sg 7Network10NWEndpointO
+ _symbolic _____Sg 9IMAP2MIME8RFC_2231O34EncodedWithCharacterSetAndLanguageV
+ _symbolic ___________tSg 13IMAP2Behavior5StateV12LocalMailboxV 0A11Persistence16ConnectionStatusO
+ _symbolic _____yAAy_____yAAyAAyAByAAySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAGG_____SgGGALGSay_____GG s15LazyMapSequenceV s0a6FilterC0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localP05limitSayAG4MoveVG_AE0o5LocalP0VtSaySo07ECLocalE6ActionCG_SitF06TargetnV0L_V AL
+ _symbolic _____yAAy_____yAAySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAGG_____SgG s15LazyMapSequenceV s0a6FilterC0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localP05limitSayAG4MoveVG_AE0o5LocalP0VtSaySo07ECLocalE6ActionCG_SitF06TargetnV0L_V
+ _symbolic _____ySay_____GG s16IndexingIteratorV 7Message17MailboxUpdateTree33_9756C92D0D431C9DA10B9422B1759BA4LLV7ElementV
+ _symbolic _____y_____yAAyAAyAByAAySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAGG_____SgGGALG s15LazyMapSequenceV s0a6FilterC0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localP05limitSayAG4MoveVG_AE0o5LocalP0VtSaySo07ECLocalE6ActionCG_SitF06TargetnV0L_V
+ _symbolic _____y_____yAByAAyABySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAGG_____SgGG s18LazyFilterSequenceV s0a3MapC0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localP05limitSayAG4MoveVG_AE0o5LocalP0VtSaySo07ECLocalE6ActionCG_SitF06TargetnV0L_V
+ _symbolic _____y_____yABy_____yAByAByACyABySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAHG_____SgGGAMGSay_____GGG s15FlattenSequenceV s07LazyMapB0V s0c6FilterB0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localQ05limitSayAI4MoveVG_AG0p5LocalQ0VtSaySo07ECLocalF6ActionCG_SitF06TargetoW0L_V AN
+ _symbolic _____y_____ySay_____GG_____G s15LazyMapSequenceV s0a6FilterC0V 13IMAP2Behavior5StateV12LocalMailboxV AE0G9WithTasksV06InSyncI0V
+ _symbolic _____y_____y_____yACy_____yACyACyADyACySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAIG_____SgGGANGSay_____GGGG s12LazySequenceV s07FlattenB0V s0a3MapB0V s0a6FilterB0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localQ05limitSayAK4MoveVG_AI0p5LocalQ0VtSaySo07ECLocalF6ActionCG_SitF06TargetoW0L_V AP
+ _symbolic _____y_____y_____y_____yADy_____yADyADyAEyADySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAJG_____SgGGAOGSay_____GGGGG s5SliceV s12LazySequenceV s07FlattenC0V s0b3MapC0V s0b6FilterC0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localR05limitSayAM4MoveVG_AK0q5LocalR0VtSaySo07ECLocalG6ActionCG_SitF06TargetpX0L_V AR
- -[MFNetworkController awdNetworkDiagnosticReport]
- _OBJC_CLASS_$_AWDMailNetworkDiagnosticsReport
- _OBJC_CLASS_$_ECMessageBodyHTMLParser
- _OBJC_CLASS_$_ECMessageBodyOriginalTextSubparser
- _OUTLINED_FUNCTION_278
- _OUTLINED_FUNCTION_279
- _OUTLINED_FUNCTION_280
- _OUTLINED_FUNCTION_281
- _OUTLINED_FUNCTION_282
- _OUTLINED_FUNCTION_283
- _OUTLINED_FUNCTION_284
- _OUTLINED_FUNCTION_285
- _OUTLINED_FUNCTION_286
- _OUTLINED_FUNCTION_287
- _OUTLINED_FUNCTION_288
- _OUTLINED_FUNCTION_289
- _OUTLINED_FUNCTION_290
- __DATA__TtCC7Message18PersistenceAdaptor18MailboxNameMapping
- __IVARS__TtCC7Message18PersistenceAdaptor18MailboxNameMapping
- __METACLASS_DATA__TtCC7Message18PersistenceAdaptor18MailboxNameMapping
- __OBJC_$_PROP_LIST_MFActivityCondition.147
- __PROTOCOLS__TtCCCC7Message25InProgressMessageDownload26AttachmentDecoderAndWriter7DecoderP33_E488F2EBCE7947B89745EE1E7B527BA212DataConsumer.17
- __SetThreadScopeFilterPredicate
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__114default_deleteIA_11DetailEntryEclB7v160006IS1_EENS3_20_EnableIfConvertibleIT_E4typeEPS6_
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKc8EncodingEENS_22__unordered_map_hasherIS3_S5_20CStringAlnumCaseHash21CStringAlnumCaseEqualLb1EEENS_21__unordered_map_equalIS3_S5_S8_S7_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_performB7v160006EPNS_11__hash_nodeIS5_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKc8EncodingEENS_22__unordered_map_hasherIS3_S5_20CStringAlnumCaseHash21CStringAlnumCaseEqualLb1EEENS_21__unordered_map_equalIS3_S5_S8_S7_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_prepareB7v160006EmRS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006EPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006IDnEEPKc
- __ZNSt3__113unordered_mapIPKc8Encoding20CStringAlnumCaseHash21CStringAlnumCaseEqualNS_9allocatorINS_4pairIKS2_S3_EEEEED1B7v160006Ev
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___141-[MFMailMessageLibrary addMessages:withMailbox:newMessagesByOldMessage:remoteIDs:setFlags:addPOPUIDs:dataSectionsByMessage:generationWindow:]_block_invoke.665
- ___141-[MFMailMessageLibrary addMessages:withMailbox:newMessagesByOldMessage:remoteIDs:setFlags:addPOPUIDs:dataSectionsByMessage:generationWindow:]_block_invoke.790
- ___24-[_MFDataCollector done]_block_invoke.2362
- ___43-[MFActivityCondition conditionsObservable]_block_invoke.74
- ___43-[MFActivityCondition conditionsObservable]_block_invoke.74.cold.1
- ___62-[MFMessageContentRequest _processContentLoadingContextEvent:]_block_invoke.101
- ___62-[MFMessageContentRequest _processContentLoadingContextEvent:]_block_invoke.77
- ___62-[MFMessageContentRequest _processContentLoadingContextEvent:]_block_invoke_2.105
- ___62-[MFMessageContentRequest _processContentLoadingContextEvent:]_block_invoke_2.83
- ___62-[MFMessageContentRequest _processContentLoadingContextEvent:]_block_invoke_3.90
- ___86-[MFMailMessageLibrary messageWithLibraryID:options:inMailbox:temporarilyUnavailable:]_block_invoke.1171
- ___88-[MFMessageContentRequest _contentRepresentationForLoadingEvent:existingRepresentation:]_block_invoke.117
- ___88-[MFMessageContentRequest _contentRepresentationForLoadingEvent:existingRepresentation:]_block_invoke.117.cold.1
- ___88-[MFMessageContentRequest _contentRepresentationForLoadingEvent:existingRepresentation:]_block_invoke.123
- ___88-[MFMessageContentRequest _contentRepresentationForLoadingEvent:existingRepresentation:]_block_invoke_2.118
- ___88-[MFMessageContentRequest _contentRepresentationForLoadingEvent:existingRepresentation:]_block_invoke_2.120.cold.1
- ___91-[MFMessageContentRequest _requestContentForAttachment:manager:options:managed:completion:]_block_invoke.133
- ___91-[MFMessageContentRequest _requestContentForAttachment:manager:options:managed:completion:]_block_invoke.141
- ___91-[MFMessageContentRequest _requestContentForAttachment:manager:options:managed:completion:]_block_invoke_2.134
- ___91-[MFMessageContentRequest _requestContentForAttachment:manager:options:managed:completion:]_block_invoke_2.134.cold.1
- ___91-[MFMessageContentRequest _requestContentForAttachment:manager:options:managed:completion:]_block_invoke_2.144
- ____SetThreadScopeFilterPredicate_block_invoke
- ___block_descriptor_32_e31_"NSString"16?0"MailAccount"8l
- ___block_literal_global.1016
- ___block_literal_global.1283
- ___block_literal_global.1320
- ___block_literal_global.1487
- ___block_literal_global.1525
- ___block_literal_global.1531
- ___block_literal_global.1545
- ___block_literal_global.2623
- ___block_literal_global.2640
- ___block_literal_global.2693
- ___block_literal_global.2699
- ___block_literal_global.346
- ___block_literal_global.445
- ___block_literal_global.479
- ___block_literal_global.588
- ___block_literal_global.677
- ___block_literal_global.77
- ___block_literal_global.773
- ___block_literal_global.801
- ___block_literal_global.819
- ___block_literal_global.857
- ___block_literal_global.86
- ___block_literal_global.905
- ___block_literal_global.914
- ___block_literal_global.926
- ___block_literal_global.929
- ___block_literal_global.932
- ___block_literal_global.959
- ___block_literal_global.993
- ___fetchArgumentsForCriterion_block_invoke.477
- __dataIndicatorString
- __unnamed_array_storage.460
- __unnamed_array_storage.660
- __unnamed_array_storage.669
- __unnamed_array_storage.672
- __unnamed_array_storage.691
- __unnamed_array_storage.705
- __unnamed_array_storage.711
- __unnamed_array_storage.720
- __unnamed_array_storage.754
- __unnamed_array_storage.764
- __unnamed_array_storage.767
- __unnamed_array_storage.770
- __unnamed_array_storage.783
- __unnamed_array_storage.786
- __unnamed_array_storage.792
- __unnamed_array_storage.798
- __unnamed_array_storage.810
- __unnamed_array_storage.813
- __unnamed_array_storage.816
- __unnamed_array_storage.824
- __unnamed_array_storage.827
- __unnamed_array_storage.830
- __unnamed_array_storage.833
- __unnamed_array_storage.836
- __unnamed_array_storage.854
- __unnamed_array_storage.872
- __unnamed_array_storage.878
- __unnamed_array_storage.902
- __unnamed_array_storage.948
- _block_copy_helper.17
- _block_copy_helper.196
- _block_copy_helper.208
- _block_copy_helper.217
- _block_copy_helper.271
- _block_copy_helper.280
- _block_copy_helper.286
- _block_copy_helper.3205
- _block_copy_helper.331
- _block_copy_helper.340
- _block_copy_helper.3580
- _block_copy_helper.3586
- _block_copy_helper.389
- _block_copy_helper.449
- _block_copy_helper.4932
- _block_copy_helper.4947
- _block_copy_helper.4953
- _block_copy_helper.4957
- _block_copy_helper.4969
- _block_copy_helper.5171
- _block_copy_helper.583
- _block_descriptor.19
- _block_descriptor.198
- _block_descriptor.210
- _block_descriptor.219
- _block_descriptor.273
- _block_descriptor.282
- _block_descriptor.288
- _block_descriptor.3207
- _block_descriptor.333
- _block_descriptor.342
- _block_descriptor.3582
- _block_descriptor.3588
- _block_descriptor.391
- _block_descriptor.451
- _block_descriptor.4934
- _block_descriptor.4949
- _block_descriptor.4955
- _block_descriptor.4959
- _block_descriptor.4971
- _block_descriptor.5173
- _block_descriptor.585
- _block_destroy_helper.18
- _block_destroy_helper.197
- _block_destroy_helper.209
- _block_destroy_helper.218
- _block_destroy_helper.272
- _block_destroy_helper.281
- _block_destroy_helper.287
- _block_destroy_helper.3206
- _block_destroy_helper.332
- _block_destroy_helper.341
- _block_destroy_helper.3581
- _block_destroy_helper.3587
- _block_destroy_helper.390
- _block_destroy_helper.450
- _block_destroy_helper.4933
- _block_destroy_helper.4948
- _block_destroy_helper.4954
- _block_destroy_helper.4958
- _block_destroy_helper.4970
- _block_destroy_helper.5172
- _block_destroy_helper.584
- _objc_msgSend$determineAdvertisedEncryptionTypeFor:
- _objc_msgSend$setCellData:
- _objc_msgSend$setDataIndicator:
- _objc_msgSend$setDnsEnabled:
- _objc_msgSend$setNumActiveCalls:
- _objc_msgSend$setReachabilityFlags:
- _objc_msgSend$setRoamingAllowed:
- _objc_msgSend$setWifiEnabled:
- _objectdestroy.17Tm
- _objectdestroy.3Tm
- _symbolic Say_____G______Sgt 16IMAP2Persistence11CredentialsO 0A10Connection16ProtocolMetadataV3TLSV
- _symbolic Say___________tG 12NIOIMAPCore211MailboxNameV 7Message0B10UpdateTree33_9756C92D0D431C9DA10B9422B1759BA4LLV7ElementV
- _symbolic Sbz_Xx
- _symbolic SiXMT
- _symbolic So30ECMessageBodyStringAccumulator_p
- _symbolic _____ 15IMAP2Connection29UnauthenticatedStateWithTasksV11tlsDidStart0G06loggeryAA16ProtocolMetadataV3TLSVSg_AA0B0C6LoggerVtKF010UnexpectedhiM0L_V
- _symbolic _____ 7Message17MailboxUpdateTree33_9756C92D0D431C9DA10B9422B1759BA4LLV7ElementV4make7mailbox7account11nameMappingSayAFGSo12MFMailboxUidC_So11IMAPAccountCAA18PersistenceAdaptorC0b4NameR0CtKFZ0bX9IsUnknownL_V
- _symbolic _____ 7Message17MailboxUpdateTree33_9756C92D0D431C9DA10B9422B1759BA4LLV7ElementV4make7mailbox7account11nameMappingSayAFGSo12MFMailboxUidC_So11IMAPAccountCAA18PersistenceAdaptorC0b4NameR0CtKFZ22PathSeparatorIsUnknownL_V
- _symbolic _____ 7Message17MailboxUpdateTree33_9756C92D0D431C9DA10B9422B1759BA4LLV7account11nameMapping9namespace9mimeCache6loggerADSo11IMAPAccountC_AA18PersistenceAdaptorC0b4NameO0C13IMAP2Protocol9NamespaceVSg0X4MIME0R0CAM6LoggerVtKcfc017AccountHasNilRootB0L_V
- _symbolic _____ 7Message17MailboxUpdateTree33_9756C92D0D431C9DA10B9422B1759BA4LLV7account11nameMapping9namespace9mimeCache6loggerADSo11IMAPAccountC_AA18PersistenceAdaptorC0b4NameO0C13IMAP2Protocol9NamespaceVSg0X4MIME0R0CAM6LoggerVtKcfc0B17NamesAreNotUniqueL_V
- _symbolic _____ 7Message17MailboxUpdateTree33_9756C92D0D431C9DA10B9422B1759BA4LLV7account11nameMapping9namespace9mimeCache6loggerADSo11IMAPAccountC_AA18PersistenceAdaptorC0b4NameO0C13IMAP2Protocol9NamespaceVSg0X4MIME0R0CAM6LoggerVtKcfc21AccountHasNilChildrenL_V
- _symbolic _____ 7Message18PersistenceAdaptorC18MailboxNameMappingC
- _symbolic _____ 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localL05limit11nameMappingSayAC4MoveVG_AA0k5LocalL0VtSaySo07ECLocalA6ActionCG_SiAA0C7AdaptorC0b4NameP0CtF06TargetjT0L_V
- _symbolic _____ So30ECMessageBodyElementAttributesV
- _symbolic ___________t 12NIOIMAPCore23UIDV 13IMAP2Behavior19MoveAndCopyMessagesV0G0V11MessageInfoV
- _symbolic ___________t 12NIOIMAPCore23UIDV 16IMAP2Persistence32OpaquePersistedMessageIdentifierV
- _symbolic ___________t 16IMAP2Persistence15OpaqueMailboxIDV AA0D10OfInterestV
- _symbolic _____yAAy_____yAAyAAyAByAAySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAGG_____SgGGALGSay_____GG s15LazyMapSequenceV s0a6FilterC0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localP05limit11nameMappingSayAG4MoveVG_AE0o5LocalP0VtSaySo07ECLocalE6ActionCG_SiAE0G7AdaptorC0f4NameT0CtF06TargetnX0L_V AM
- _symbolic _____yAAy_____yAAySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAGG_____SgG s15LazyMapSequenceV s0a6FilterC0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localP05limit11nameMappingSayAG4MoveVG_AE0o5LocalP0VtSaySo07ECLocalE6ActionCG_SiAE0G7AdaptorC0f4NameT0CtF06TargetnX0L_V
- _symbolic _____ySaySi______SgtGSiG s15LazyMapSequenceV 12NIOIMAPCore211MailboxNameV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 12NIOIMAPCore213AppendCommandO
- _symbolic _____y_____G s23_ContiguousArrayStorageC 16IMAP2Persistence15OpaqueMailboxIDV
- _symbolic _____y_____SaySSGG 10Foundation15ListFormatStyleV AA06StringD0V
- _symbolic _____y_____SaySSG_G 10Foundation15ListFormatStyleV0B4TypeO AA06StringD0V
- _symbolic _____y_____SaySSG_G 10Foundation15ListFormatStyleV5WidthO AA06StringD0V
- _symbolic _____y___________tG s23_ContiguousArrayStorageC 12NIOIMAPCore23UIDV 13IMAP2Behavior19MoveAndCopyMessagesV0J0V11MessageInfoV
- _symbolic _____y___________tG s23_ContiguousArrayStorageC 12NIOIMAPCore23UIDV 16IMAP2Persistence32OpaquePersistedMessageIdentifierV
- _symbolic _____y___________tG s23_ContiguousArrayStorageC 16IMAP2Persistence15OpaqueMailboxIDV AC0G10OfInterestV
- _symbolic _____y_____yAAyAAyAByAAySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAGG_____SgGGALG s15LazyMapSequenceV s0a6FilterC0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localP05limit11nameMappingSayAG4MoveVG_AE0o5LocalP0VtSaySo07ECLocalE6ActionCG_SiAE0G7AdaptorC0f4NameT0CtF06TargetnX0L_V
- _symbolic _____y_____yAByAAyABySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAGG_____SgGG s18LazyFilterSequenceV s0a3MapC0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localP05limit11nameMappingSayAG4MoveVG_AE0o5LocalP0VtSaySo07ECLocalE6ActionCG_SiAE0G7AdaptorC0f4NameT0CtF06TargetnX0L_V
- _symbolic _____y_____yABy_____yAByAByACyABySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAHG_____SgGGAMGSay_____GGG s15FlattenSequenceV s07LazyMapB0V s0c6FilterB0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localQ05limit11nameMappingSayAI4MoveVG_AG0p5LocalQ0VtSaySo07ECLocalF6ActionCG_SiAG0H7AdaptorC0g4NameU0CtF06TargetoY0L_V AO
- _symbolic _____y_____y_____yACy_____yACyACyADyACySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAIG_____SgGGANGSay_____GGGG s12LazySequenceV s07FlattenB0V s0a3MapB0V s0a6FilterB0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localQ05limit11nameMappingSayAK4MoveVG_AI0p5LocalQ0VtSaySo07ECLocalF6ActionCG_SiAI0H7AdaptorC0g4NameU0CtF06TargetoY0L_V AQ
- _symbolic _____y_____y_____y_____yADy_____yADyADyAEyADySaySo20ECLocalMessageActionCGSo010ECTransferbC0CSgGGAJG_____SgGGAOGSay_____GGGGG s5SliceV s12LazySequenceV s07FlattenC0V s0b3MapC0V s0b6FilterC0V 7Message24MailboxPersistenceHelperC44findMovedOrCopiedMessagesAndCompletedActions05localR05limit11nameMappingSayAM4MoveVG_AK0q5LocalR0VtSaySo07ECLocalG6ActionCG_SiAK0I7AdaptorC0h4NameV0CtF06TargetpZ0L_V AS
- _symbolic _____y_____y_____y_____ySay_____G_____SgGGAG_GG s12_IteratorBoxC s15LazyMapSequenceV0A0V s0c6FilterE0V AD 13IMAP2Behavior11TaskHistoryV7RunningO 0G8Protocol12ConnectionIDV
CStrings:
+ "\x01\x02\x03\x04\x05\x06\a\b\t\n\v\f\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x1b\x1c\x17\x18\x19\x1a\x1d\x1e\x1f !\"#$%"
+ "Can't construct Array with count < 0"
+ "DawnCAddUnreadCountIndex"
+ "EncryptedMail"
+ "Failed to deliver message due to error %{public}@"
+ "Failed to find a valid delivery object"
+ "Failed to find an account to deliver message"
+ "Failed to find valid connection for SMTP delivery"
+ "Negative value is not representable"
+ "Swift/FloatingPointTypes.swift"
+ "T@\"NSArray\",?,R,C"
+ "T@\"NSString\",?,R,C"
+ "[%.*hhx-%.*X] Mailbox ID %s is not unique."
+ "[%.*hhx-%.*X] Mailbox name '%{sensitive,mask.mailbox}s' is not unique (%s %s)."
+ "[%.*hhx-%.*X] Mailboxes are not unique. Retrying"
+ "[%.*hhx-%{public}s] Did request opportunistic STARTTLS"
+ "[%.*hhx-%{public}s] Opportunistic STARTTLS completed: %hu / %hu"
+ "[%.*hhx] Persistence passed %ld copies of mailbox with ID %s \"%{sensitive,mask.mailbox}s\" - \"%{sensitive,mask.mailbox}s\"."
+ "[%.*hhx] Persistence passed %ld copies of mailbox with name \"%{sensitive,mask.mailbox}s\" %s - %s."
+ "[%.*hhx] Persistence passed list of %ld mailboxes with duplicate names/IDs."
+ "com.apple.email.PersistenceAdaptor.account"
+ "com.apple.imap.insecure-cert-verify"
+ "encryptionLevelForSender:forAdvertisement:useGCM:encryptSubject:"
+ "ifNull:second:"
+ "initWithTable:conflictResolution:"
+ "mf_stringWithData:encoding:"
+ "or:with:"
+ "resultIfAvailable"
+ "transportLayerSecurity"
+ "v24@?0@\"<EMExtendedContentItem>\"8@\"MFAttachment\"16"
+ "v32@?0@\"<OS_sec_protocol_metadata>\"8@\"<OS_sec_trust>\"16@?<v@?B>24"
- "@\"NSString\"16@?0@\"MailAccount\"8"
- "Attachment: "
- "Attachments: "
- "Can't unsafeBitCast between types of different sizes"
- "Division by zero in remainder operation"
- "Division results in an overflow in remainder operation"
- "Format string for when there’s a single file in a message.  Parameter is the filename."
- "Format string for when there’s more than one file in a message.  Parameter is the joined filenames."
- "MULTI_FILE"
- "Message/LocalizedString.swift"
- "SINGLE_FILE"
- "StaticString should have Unicode scalar representation"
- "StaticString should have pointer representation"
- "String index is out of bounds"
- "Swift/Builtin.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "T@\"AWDMailNetworkDiagnosticsReport\",R,N"
- "T@\"NSArray\",R,C"
- "UnsafeBufferPointer has a nil start and nonzero count"
- "UnsafeMutableBufferPointer has a nil start and nonzero count"
- "UnsafeMutableRawBufferPointer with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "UnsafeRawBufferPointer with negative count"
- "[%.*hhx-%.*X] [%{sensitive,mask.mailbox}s] Setting %ld character summary for message UID %u."
- "[%.*hhx-%{public}s] Not using TLS."
- "[%.*hhx] Persistence passed %ld copies of mailbox %s."
- "[%.*hhx] Persistence passed list of %ld mailboxes with duplicate names."
- "_TtCC7Message18PersistenceAdaptor18MailboxNameMapping"
- "accumulatedString"
- "addSubparser:"
- "appendCustomEntityWithTag:stringRepresentation:"
- "appendInnerTextWithConsumableNode:"
- "awdNetworkDiagnosticReport"
- "determineAdvertisedEncryptionTypeFor:"
- "initWithHTML:"
- "nameMapping"
- "newElements.underestimatedCount was an overestimate"
- "newStringAccumulatorWithOptions:lengthLimit:"
- "parse"
- "pathSeparator"
- "plainTextFromHTML:limit:"
- "setCellData:"
- "setDataIndicator:"
- "setDnsEnabled:"
- "setFoundTextBlock:"
- "setFoundWhitespaceBlock:"
- "setNumActiveCalls:"
- "setReachabilityFlags:"
- "setRoamingAllowed:"
- "setWifiEnabled:"
- "tlsOptions"
- "v16@?0@\"<ECMessageBodyElement>\"8"
- "v32@?0@\"<ECMessageBodyElement>\"8Q16^B24"
- "valueForAttributes:"

```
