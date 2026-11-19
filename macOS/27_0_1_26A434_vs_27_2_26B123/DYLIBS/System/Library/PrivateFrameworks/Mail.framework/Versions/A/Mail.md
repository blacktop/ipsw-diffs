## Mail

> `/System/Library/PrivateFrameworks/Mail.framework/Versions/A/Mail`

```diff

-3901.100.1.1.12
-  __TEXT.__text: 0xa19270
-  __TEXT.__objc_methlist: 0x1982c
-  __TEXT.__gcc_except_tab: 0x4c3ec
-  __TEXT.__const: 0x615c9
-  __TEXT.__cstring: 0x31f39
-  __TEXT.__oslogstring: 0x22139
+3901.200.71.1.16
+  __TEXT.__text: 0xa30e98
+  __TEXT.__objc_methlist: 0x199b4
+  __TEXT.__const: 0x61b99
+  __TEXT.__cstring: 0x329b9
+  __TEXT.__gcc_except_tab: 0x4c800
+  __TEXT.__oslogstring: 0x223c9
   __TEXT.__ustring: 0x44
-  __TEXT.__swift5_typeref: 0xe634
-  __TEXT.__constg_swiftt: 0xbc08
-  __TEXT.__swift5_reflstr: 0xe5d0
-  __TEXT.__swift5_fieldmd: 0x13080
+  __TEXT.__swift5_typeref: 0xe7f4
+  __TEXT.__constg_swiftt: 0xbce8
+  __TEXT.__swift5_reflstr: 0xe820
+  __TEXT.__swift5_fieldmd: 0x13304
   __TEXT.__swift5_builtin: 0xc44
-  __TEXT.__swift5_assocty: 0x1b58
-  __TEXT.__swift5_proto: 0x222c
-  __TEXT.__swift5_types: 0x1510
-  __TEXT.__swift5_capture: 0x25c7c
-  __TEXT.__swift5_mpenum: 0x760
+  __TEXT.__swift5_assocty: 0x1bb8
+  __TEXT.__swift5_proto: 0x2270
+  __TEXT.__swift5_types: 0x1524
+  __TEXT.__swift5_capture: 0x26080
+  __TEXT.__swift5_mpenum: 0x768
   __TEXT.__swift5_protos: 0x60
-  __TEXT.__unwind_info: 0x1e5e0
-  __TEXT.__eh_frame: 0x15a28
+  __TEXT.__unwind_info: 0x1e8e8
+  __TEXT.__eh_frame: 0x16094
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11890
-  __DATA_CONST.__objc_classlist: 0xdb8
+  __DATA_CONST.__const: 0x118a0
+  __DATA_CONST.__objc_classlist: 0xda8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x5a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xe008
+  __DATA_CONST.__objc_selrefs: 0xe108
   __DATA_CONST.__objc_protorefs: 0x1d0
   __DATA_CONST.__objc_superrefs: 0x840
   __DATA_CONST.__objc_arraydata: 0x270
-  __DATA_CONST.__got: 0x3778
-  __AUTH_CONST.__const: 0x89d28
-  __AUTH_CONST.__cfstring: 0x1a6c0
-  __AUTH_CONST.__objc_const: 0x2b308
+  __DATA_CONST.__got: 0x37a0
+  __AUTH_CONST.__const: 0x8aa28
+  __AUTH_CONST.__cfstring: 0x1a7c0
+  __AUTH_CONST.__objc_const: 0x2b2b8
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0xd08
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x3468
-  __AUTH_CONST.__auth_ptr: 0xb720
-  __AUTH.__objc_data: 0x6338
-  __AUTH.__data: 0x9f70
+  __AUTH_CONST.__auth_got: 0x34d8
+  __AUTH_CONST.__auth_ptr: 0xb7f0
+  __AUTH.__objc_data: 0x6298
+  __AUTH.__data: 0xa130
   __DATA.__objc_ivar: 0x162c
-  __DATA.__data: 0xc6ec
+  __DATA.__data: 0xc83c
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x437a8
-  __DATA.__common: 0xd7c
+  __DATA.__bss: 0x44028
+  __DATA.__common: 0xdbc
   __DATA_DIRTY.__objc_data: 0x25d0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x868
+  __DATA_DIRTY.__bss: 0x878
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 42585
-  Symbols:   28615
-  CStrings:  7730
+  Functions: 42951
+  Symbols:   28705
+  CStrings:  7788
 
Symbols:
+ +[MFEWSConnection sendSavesToSentItems]
+ +[MFExchangeConnection sendSavesToSentItems]
+ +[MFMailAccount _accountContainingEmailAddress:matchingAddress:fullUserName:includingInactive:]
+ +[MFMailAccount accountContainingEmailAddress:includingInactive:]
+ +[MFMailAccount accountWithObjectID:]
+ +[MFSMTPAccount log]
+ -[MFAccount displayNameWithoutPII]
+ -[MFEWSConnection setupConnectionErrorForMonitorWithPort:usingSSL:serverTrust:]
+ -[MFEWSDeliveryAccount shouldIncludeBCCInMIMEHeaders]
+ -[MFExchangeAccount _graphIDFromEWSID:]
+ -[MFExchangeAccount _migrateFolderId:toGraphFolderId:forMailbox:]
+ -[MFExchangeAccount connectionClass]
+ -[MFExchangeAccount migrateFolderIDForMailbox:]
+ -[MFExchangeAccount migrateMessageIDsForMailbox:]
+ -[MFExchangeAccount migrateRootFolderID]
+ -[MFExchangeAccount shouldAppendSentMessageAfterSending]
+ -[MFExchangeAccount shouldIncludeBCCInMIMEHeaders]
+ -[MFExchangeConnection generateInternalAuthenticationError:]
+ -[MFExchangeConnection isAuthenticationError:]
+ -[MFExchangeConnection recoverySuggestionForNSURLError:port:usingSSL:helpAnchor:]
+ -[MFIMAPAccount initialSyncCompletedForMailbox:]
+ -[MFLibrary associatedEventIDsForMessageID:]
+ -[MFLibrary migrateEWSFolderId:toGraphFolderId:]
+ -[MFLibrary remoteIDsForMailbox:batchSize:lastRowID:]
+ -[MFLibrary setAssociatedEventID:forRowID:]
+ -[MFLibrary setRemoteID:forRowID:]
+ -[MFMailAccount isPrimaryAppleAccount]
+ -[MFMailboxTransformer _accountIdentifierForMailbox:accountIdentifiers:]
+ -[MFMailboxTransformer _transformMailbox:parent:accountIdentifiers:legacyMailboxToMailboxMap:objectIDToLegacyMailboxMap:]
+ -[MFMessageChangeManager_macOS hasCompletedInitialSyncForMailboxURL:]
+ -[MFRemoteStoreAccount shouldAppendSentMessageAfterSending]
+ -[MFSMTPAccount _repairMisconfiguredAppleTokenAccountIfNeeded]
+ GCC_except_table228
+ GCC_except_table238
+ GCC_except_table253
+ GCC_except_table261
+ GCC_except_table330
+ GCC_except_table345
+ GCC_except_table348
+ GCC_except_table349
+ GCC_except_table353
+ GCC_except_table356
+ GCC_except_table360
+ GCC_except_table364
+ GCC_except_table365
+ GCC_except_table372
+ GCC_except_table381
+ GCC_except_table382
+ GCC_except_table390
+ GCC_except_table391
+ GCC_except_table392
+ GCC_except_table400
+ GCC_except_table403
+ GCC_except_table404
+ GCC_except_table405
+ GCC_except_table408
+ GCC_except_table412
+ GCC_except_table413
+ GCC_except_table440
+ GCC_except_table445
+ GCC_except_table453
+ GCC_except_table454
+ GCC_except_table456
+ GCC_except_table457
+ GCC_except_table458
+ GCC_except_table459
+ GCC_except_table460
+ GCC_except_table461
+ GCC_except_table462
+ GCC_except_table473
+ GCC_except_table474
+ GCC_except_table475
+ GCC_except_table495
+ GCC_except_table503
+ GCC_except_table509
+ GCC_except_table511
+ GCC_except_table512
+ GCC_except_table514
+ _ACAccountPropertyAllowsInsecureAuthentication
+ _ACCredentialTypeToken
+ _OBJC_CLASS_$_EDListUnsubscribeDetector
+ _OBJC_CLASS_$_MCImageMetadataResult
+ _OBJC_CLASS_$_MCImageMetadataService
+ __CLASS_METHODS_MFGraphSyncConnection
+ __CLASS_PROPERTIES_MFGraphSyncConnection
+ __OBJC_$_CLASS_METHODS_MFEWSConnection
+ __OBJC_$_CLASS_PROP_LIST_MFSMTPAccount
+ ___121-[MFMailboxTransformer _transformMailbox:parent:accountIdentifiers:legacyMailboxToMailboxMap:objectIDToLegacyMailboxMap:]_block_invoke
+ ___20+[MFSMTPAccount log]_block_invoke
+ ___34-[MFLibrary setRemoteID:forRowID:]_block_invoke
+ ___43-[MFLibrary setAssociatedEventID:forRowID:]_block_invoke
+ ___44-[MFLibrary associatedEventIDsForMessageID:]_block_invoke
+ ___48-[MFLibrary migrateEWSFolderId:toGraphFolderId:]_block_invoke
+ ___53-[MFLibrary remoteIDsForMailbox:batchSize:lastRowID:]_block_invoke
+ ___block_descriptor_64_ea8_32s40r_e41_B16?0"EDPersistenceDatabaseConnection"8l
+ ___block_descriptor_72_ea8_32s40s48r56r64r_e28_v32?0"MFCriterion"8Q16^B24l
+ ___swift_memcpy6_1
+ _associated conformance 12NIOIMAPCore211ParseBufferV7NewlineOSHAASQ
+ _associated conformance 12NIOIMAPCore213SortCriterionO3KeyOSHAASQ
+ _associated conformance 12NIOIMAPCore213SortCriterionOSHAASQ
+ _associated conformance 15IMAP2Connection6EnableVSHAASQ
+ _associated conformance 4Mail12MailboxRowIDVs27ExpressibleByIntegerLiteralAA0gH4TypesADP_s01_ef7BuiltingH0
+ _associated conformance So17MFExchangeMessageC4MailE0B6Status33_51905892CF2471EB373F9E70C1539825LLOSHACSQ
+ _associated conformance So17MFExchangeMessageC4MailE12FollowupIcon33_51905892CF2471EB373F9E70C1539825LLOSHACSQ
+ _associated conformance So17MFExchangeMessageC4MailE16LastVerbExecuted33_51905892CF2471EB373F9E70C1539825LLOSHACSQ
+ _objc_msgSend$_accountContainingEmailAddress:matchingAddress:fullUserName:includingInactive:
+ _objc_msgSend$_accountIdentifierForMailbox:accountIdentifiers:
+ _objc_msgSend$_graphIDFromEWSID:
+ _objc_msgSend$_migrateFolderId:toGraphFolderId:forMailbox:
+ _objc_msgSend$_repairMisconfiguredAppleTokenAccountIfNeeded
+ _objc_msgSend$_transformMailbox:parent:accountIdentifiers:legacyMailboxToMailboxMap:objectIDToLegacyMailboxMap:
+ _objc_msgSend$aa_primaryAppleAccount
+ _objc_msgSend$appendHeaderData:recipients:recipientsByHeaderKey:expandGroups:includeComment:includeBCC:
+ _objc_msgSend$associatedEventIDsForMessageID:
+ _objc_msgSend$connectionClass
+ _objc_msgSend$credentialType
+ _objc_msgSend$generateInternalAuthenticationError:
+ _objc_msgSend$handleGraphSyncError:
+ _objc_msgSend$handlePOSIXError:
+ _objc_msgSend$handleURLError:
+ _objc_msgSend$imageMetadataFor:
+ _objc_msgSend$initAsEphemeralID:representedObjectID:
+ _objc_msgSend$initWithMetadataResult:name:type:
+ _objc_msgSend$initialSyncCompletedForMailbox:
+ _objc_msgSend$isAuthenticationError:
+ _objc_msgSend$isGraphSyncAuthError:
+ _objc_msgSend$metadataForImageData:webView:error:
+ _objc_msgSend$migrateEWSFolderId:toGraphFolderId:
+ _objc_msgSend$recordMessagesNeedToBeDonated:indexingType:trigger:
+ _objc_msgSend$recoverySuggestionForNSURLError:port:usingSSL:helpAnchor:
+ _objc_msgSend$remoteIDsForMailbox:batchSize:lastRowID:
+ _objc_msgSend$remoteMailAccountsEmployedBy
+ _objc_msgSend$representedObjectID
+ _objc_msgSend$sendSavesToSentItems
+ _objc_msgSend$setAssociatedEventID:forRowID:
+ _objc_msgSend$setRemoteID:forRowID:
+ _objc_msgSend$setupConnectionErrorForMonitorWithPort:usingSSL:serverTrust:
+ _objc_msgSend$shouldAppendSentMessageAfterSending
+ _objc_msgSend$shouldIncludeBCCInMIMEHeaders
+ _symbolic B2
+ _symbolic SDySS_____G 9GraphSync0aB41SingleValueLegacyExtendedPropertyResourceV
+ _symbolic SDy__________G 16IMAP2Persistence15OpaqueMailboxIDV AA13SearchRequestV15RangesToExcludeV
+ _symbolic SDy__________y_____GG 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore228MessageIdentifierSetNonEmptyV AD3UIDV
+ _symbolic SS______t 9GraphSync0aB41SingleValueLegacyExtendedPropertyResourceV
+ _symbolic Say_____G 12NIOIMAPCore213SortCriterionO
+ _symbolic Say_____G 9GraphSync0aB41SingleValueLegacyExtendedPropertyResourceV
+ _symbolic Say_____G8criteria_SS7charset_____3keySay_____G13returnOptionst 12NIOIMAPCore213SortCriterionO AA9SearchKeyO AA0D12ReturnOptionO
+ _symbolic So17MFExchangeMessageC
+ _symbolic So21MCImageMetadataResultCSg
+ _symbolic So21MCImageMetadataResultCSgz_Xx
+ _symbolic _____ 12NIOIMAPCore211ParseBufferV7NewlineO
+ _symbolic _____ 12NIOIMAPCore213SortCriterionO
+ _symbolic _____ 12NIOIMAPCore213SortCriterionO3KeyO
+ _symbolic _____ 12NIOIMAPCore214ResponseParserV0B10AndNewlineV
+ _symbolic _____ 13IMAP2Behavior20MessageDownloadStateV
+ _symbolic _____ 9GraphSync0aB15MessageResourceV
+ _symbolic _____ So17MFExchangeMessageC4MailE0B6Status33_51905892CF2471EB373F9E70C1539825LLO
+ _symbolic _____ So17MFExchangeMessageC4MailE12FollowupIcon33_51905892CF2471EB373F9E70C1539825LLO
+ _symbolic _____ So17MFExchangeMessageC4MailE16LastVerbExecuted33_51905892CF2471EB373F9E70C1539825LLO
+ _symbolic _____3key______y_____G5valuet 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore228MessageIdentifierSetNonEmptyV AD3UIDV
+ _symbolic _____7mailbox_Say_____GSb6isLastt 16IMAP2Persistence15OpaqueMailboxIDV AA0C26PersistedMessageIdentifierV
+ _symbolic _____7mailbox______7messaget 16IMAP2Persistence15OpaqueMailboxIDV AA0C26PersistedMessageIdentifierV
+ _symbolic _____7mailbox______Sg5valuet 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore225ModificationSequenceValueV
+ _symbolic _____Sg 10Foundation13URLComponentsV
+ _symbolic _____Sg 12NIOIMAPCore211ParseBufferV7NewlineO
+ _symbolic _____Sg 13IMAP2Behavior23DetermineMessageBatchesV9CommandIDO
+ _symbolic _____Sg 9GraphSync0aB13EventResourceV
+ _symbolic _____Sg 9GraphSync0aB41SingleValueLegacyExtendedPropertyResourceV
+ _symbolic _____Sg 9GraphSync8APIErrorO
+ _symbolic _____Sg_ABt 13IMAP2Behavior23DetermineMessageBatchesV9CommandIDO
+ _symbolic ______AAt 13IMAP2Behavior23DetermineMessageBatchesV9CommandIDO
+ _symbolic ______SDy__________y_____GGt 16IMAP2Persistence13SearchRequestV2IDV AA013OpaqueMailboxE0V 12NIOIMAPCore220MessageIdentifierSetV AH3UIDV
+ _symbolic ______Say_____G_____t 15IMAP2Connection6EnableV 12NIOIMAPCore210CapabilityV 0A8Protocol8ServerIDV
+ _symbolic _____________________pIeglnrzo_ 12NIOIMAPCore211ParseBufferV AA12StackTrackerV AA13SortCriterionO s5ErrorP
+ _symbolic _____________________pIeglnrzo_ 12NIOIMAPCore211ParseBufferV AA12StackTrackerV AA13SortCriterionO3KeyO s5ErrorP
+ _symbolic _____________________pIeglydzo_ 12NIOIMAPCore211ParseBufferV AA12StackTrackerV AA13SortCriterionO s5ErrorP
+ _symbolic ___________t 16IMAP2Persistence15OpaqueMailboxIDV AA13SearchRequestV15RangesToExcludeV
+ _symbolic ___________t 16IMAP2Persistence15OpaqueMailboxIDV s6UInt32V
+ _symbolic ___________y_____Gt 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore228MessageIdentifierSetNonEmptyV AD3UIDV
+ _symbolic _____ySSSay___________tGG s18_DictionaryStorageC 16IMAP2Persistence15OpaqueMailboxIDV s6UInt32V
+ _symbolic _____ySay_____GG s16IndexingIteratorV 9GraphSync0cD41SingleValueLegacyExtendedPropertyResourceV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12NIOIMAPCore213SortCriterionO
+ _symbolic _____y____________G 13IMAP2Behavior24TaskHistoryWithCustomIDsV0F5IDMapV7CommandV AA23DetermineMessageBatchesV0I2IDO AI06ActionM0O
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC 16IMAP2Persistence15OpaqueMailboxIDV s6UInt32V
+ _symbolic _____y___________y_____GtG s23_ContiguousArrayStorageC 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore220MessageIdentifierSetV AF3UIDV
+ _symbolic _____y__________y_____GG s18_DictionaryStorageC 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore220MessageIdentifierSetV AF3UIDV
+ _symbolic _____y__________z______tKcG s23_ContiguousArrayStorageC 12NIOIMAPCore213SortCriterionO AC11ParseBufferV AC12StackTrackerV
+ _symbolic _____y_____y_____GG s23_ContiguousArrayStorageC 12NIOIMAPCore228MessageIdentifierSetNonEmptyV AC14SequenceNumberV
+ _symbolic xq_xq_Iegnnrr_
+ _type_layout_string So26MFExchangeFolderPropertiesV
- +[MFAddSearchableDataDetectionResultsTable targetVersion]
- +[MFCreateSearchableAttachmentsTablesUpgradeStep targetVersion]
- +[MFMailAccount _accountContainingEmailAddress:matchingAddress:fullUserName:]
- -[MFAddSearchableDataDetectionResultsTable runWithRowIDsNeedingConversationRecalculation:]
- -[MFCreateSearchableAttachmentsTablesUpgradeStep runWithRowIDsNeedingConversationRecalculation:]
- -[MFEWSConnection _setupConnectionErrorForMonitorWithPort:usingSSL:serverTrust:]
- -[MFIMAPAccount _initialSyncCompletedForMailbox:]
- -[MFMailboxTransformer _transformMailbox:parent:legacyMailboxToMailboxMap:objectIDToLegacyMailboxMap:]
- GCC_except_table206
- GCC_except_table247
- GCC_except_table257
- GCC_except_table282
- GCC_except_table351
- GCC_except_table352
- GCC_except_table358
- GCC_except_table359
- GCC_except_table362
- GCC_except_table366
- GCC_except_table370
- GCC_except_table384
- GCC_except_table387
- GCC_except_table388
- GCC_except_table395
- GCC_except_table396
- GCC_except_table397
- GCC_except_table398
- GCC_except_table406
- GCC_except_table414
- GCC_except_table415
- GCC_except_table416
- GCC_except_table417
- GCC_except_table418
- GCC_except_table419
- GCC_except_table450
- GCC_except_table463
- GCC_except_table464
- GCC_except_table465
- GCC_except_table485
- GCC_except_table493
- GCC_except_table499
- GCC_except_table501
- GCC_except_table502
- GCC_except_table504
- _OBJC_CLASS_$_EDAddSearchableDataDetectionResultsTableUpgradeStep
- _OBJC_CLASS_$_EMListUnsubscribeDetector
- _OBJC_CLASS_$_MFAddSearchableDataDetectionResultsTable
- _OBJC_CLASS_$_MFCreateSearchableAttachmentsTablesUpgradeStep
- _OBJC_CLASS_$_NSImage
- _OBJC_METACLASS_$_MFAddSearchableDataDetectionResultsTable
- _OBJC_METACLASS_$_MFCreateSearchableAttachmentsTablesUpgradeStep
- __OBJC_$_CLASS_METHODS_MFAddSearchableDataDetectionResultsTable
- __OBJC_$_CLASS_METHODS_MFCreateSearchableAttachmentsTablesUpgradeStep
- __OBJC_$_INSTANCE_METHODS_MFAddSearchableDataDetectionResultsTable
- __OBJC_$_INSTANCE_METHODS_MFCreateSearchableAttachmentsTablesUpgradeStep
- __OBJC_CLASS_RO_$_MFAddSearchableDataDetectionResultsTable
- __OBJC_CLASS_RO_$_MFCreateSearchableAttachmentsTablesUpgradeStep
- __OBJC_METACLASS_RO_$_MFAddSearchableDataDetectionResultsTable
- __OBJC_METACLASS_RO_$_MFCreateSearchableAttachmentsTablesUpgradeStep
- ___102-[MFMailboxTransformer _transformMailbox:parent:legacyMailboxToMailboxMap:objectIDToLegacyMailboxMap:]_block_invoke
- ___block_descriptor_64_ea8_32s40s48r56r_e28_v32?0"MFCriterion"8Q16^B24l
- _associated conformance 12IMAP2Helpers15MillisecondDateVSHAASQ
- _associated conformance 12NIOIMAPCore211MailboxDataO10SearchSortVSHAASQ
- _associated conformance 12NIOIMAPCore225FetchModificationResponseVSHAASQ
- _objc_msgSend$_accountContainingEmailAddress:matchingAddress:fullUserName:
- _objc_msgSend$_initialSyncCompletedForMailbox:
- _objc_msgSend$_setupConnectionErrorForMonitorWithPort:usingSSL:serverTrust:
- _objc_msgSend$_transformMailbox:parent:legacyMailboxToMailboxMap:objectIDToLegacyMailboxMap:
- _objc_msgSend$appendHeaderData:recipients:recipientsByHeaderKey:expandGroups:includeComment:
- _objc_msgSend$initWithImage:name:type:
- _objc_msgSend$initWithRepresentedObjectID:
- _objc_msgSend$recordMessagesNeedToBeDonated:indexingType:
- _symbolic SDy__________G 12NIOIMAPCore211MailboxNameV 16IMAP2Persistence13SearchRequestV15RangesToExcludeV
- _symbolic SDy__________y_____GG 12NIOIMAPCore211MailboxNameV AA28MessageIdentifierSetNonEmptyV AA3UIDV
- _symbolic Say_____G 11EmailDaemon17SearchableMessageV0A7AddressV
- _symbolic Sb16includesFirstUID_t
- _symbolic Spy_____SgG 9IMAP2MIME8BoundaryV
- _symbolic _____ 12IMAP2Helpers15MillisecondDateV
- _symbolic _____ 12NIOIMAPCore211MailboxDataO10SearchSortV
- _symbolic _____ 12NIOIMAPCore225FetchModificationResponseV
- _symbolic _____3key______y_____G5valuet 12NIOIMAPCore211MailboxNameV AA20MessageIdentifierSetV AA3UIDV
- _symbolic _____3key______y_____G5valuet 12NIOIMAPCore211MailboxNameV AA28MessageIdentifierSetNonEmptyV AA3UIDV
- _symbolic _____7mailbox_Say_____GSb6isLastt 12NIOIMAPCore211MailboxNameV 16IMAP2Persistence32OpaquePersistedMessageIdentifierV
- _symbolic _____7mailbox_Si5limitt 12NIOIMAPCore211MailboxNameV
- _symbolic _____7mailbox______Sg5valuet 12NIOIMAPCore211MailboxNameV AA25ModificationSequenceValueV
- _symbolic _____Sg 11EmailDaemon17SearchableMessageV8PriorityO
- _symbolic _____Sg_ABt s6MirrorV12DisplayStyleO
- _symbolic ______SDy__________y_____GGt 16IMAP2Persistence13SearchRequestV2IDV 12NIOIMAPCore211MailboxNameV AF20MessageIdentifierSetV AF3UIDV
- _symbolic ___________t 12NIOIMAPCore211MailboxNameV 16IMAP2Persistence13SearchRequestV15RangesToExcludeV
- _symbolic ___________t 12NIOIMAPCore211MailboxNameV s6UInt32V
- _symbolic ___________t 13IMAP2Behavior23DetermineMessageBatchesV9CommandIDO AC9TaskStateO
- _symbolic ___________y_____Gt 12NIOIMAPCore211MailboxNameV AA20MessageIdentifierSetV AA3UIDV
- _symbolic ___________y_____Gt 12NIOIMAPCore211MailboxNameV AA28MessageIdentifierSetNonEmptyV AA3UIDV
- _symbolic _____ySSSay___________tGG s18_DictionaryStorageC 12NIOIMAPCore211MailboxNameV s6UInt32V
- _symbolic _____ySSSg5label_yp5valuetG s13AnyCollectionV
- _symbolic _____y___________tG s23_ContiguousArrayStorageC 12NIOIMAPCore211MailboxNameV s6UInt32V
- _symbolic _____y___________y_____GtG s23_ContiguousArrayStorageC 12NIOIMAPCore211MailboxNameV AC20MessageIdentifierSetV AC3UIDV
- _type_layout_string 12IMAP2Helpers15MillisecondDateV
- _type_layout_string 12NIOIMAPCore211MailboxDataO10SearchSortV
- _type_layout_string 12NIOIMAPCore225FetchModificationResponseV
- _type_layout_string So19MFMailboxAttributesV
CStrings:
+ "#microsoft.graph.eventMessage"
+ "#microsoft.graph.eventMessageRequest"
+ "#microsoft.graph.eventMessageResponse"
+ "#microsoft.graph.message"
+ "#microsoft.graph.post"
+ "$hasnoattachment"
+ "+[MFExchangeConnection sendSavesToSentItems]"
+ "-[MFLibrary associatedEventIDsForMessageID:]"
+ "-[MFLibrary migrateEWSFolderId:toGraphFolderId:]"
+ "-[MFLibrary remoteIDsForMailbox:batchSize:lastRowID:]"
+ "-[MFLibrary setAssociatedEventID:forRowID:]"
+ "-[MFLibrary setRemoteID:forRowID:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECFlagChangeMessageActionResults.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageAction.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageActionResults.h"
+ "Boolean {A7B529B5-4B75-47A7-A24F-20743D6C55CD} Name MessageJunkFlag"
+ "Boolean {A7B529B5-4B75-47A7-A24F-20743D6C55CD} Name MessageJunkRecordedFlag"
+ "Boolean {A7B529B5-4B75-47A7-A24F-20743D6C55CD} Name MessageNotJunkFlag"
+ "Boolean {A7B529B5-4B75-47A7-A24F-20743D6C55CD} Name MessageRedirectedFlag"
+ "Could not decode the event message for a meeting response: %@"
+ "Couldn't parse JMAPACCESS URL"
+ "ErrorInvalidSyncStateData"
+ "GraphSyncErrorCode"
+ "GraphSyncErrorMessage"
+ "GraphSyncMessageResource contains unexpected @odata.type %s"
+ "Image metadata fetch failed for junk classification"
+ "Integer 0x1081"
+ "Integer 0x1095"
+ "Integer 0xE17"
+ "Invalid JMAPACCESS URL"
+ "Long 0xE08"
+ "Mail/RowID.swift"
+ "No calendar event is associated with the meeting request, cannot send an event response"
+ "Reached the maximum MIME part parsing depth: %{public}ld"
+ "Repairing SMTP account [%{public}@]: backfilling missing AuthenticationScheme %{public}@"
+ "Repairing SMTP account [%{public}@]: backfilling missing IdentityEmailAddress"
+ "Repairing SMTP account [%{public}@]: disabling AllowsInsecureAuthentication"
+ "SELECT ROWID, associated_id_string FROM events WHERE message_id = ?"
+ "SELECT ROWID, remote_id FROM messages WHERE ROWID > ? AND mailbox = (SELECT ROWID FROM mailboxes WHERE url = ?) AND deleted = 0 AND remote_id NOTNULL ORDER BY ROWID LIMIT ?"
+ "SyncStateNotFound"
+ "The message to delete is already gone, treating the delete as a success"
+ "Type mismatch for calendarEventID: expected GraphSyncEventMessageResource, got %s"
+ "UPDATE events SET associated_id_string = ? WHERE ROWID = ?"
+ "UPDATE ews_folders SET folder_id = ?, sync_state = NULL WHERE folder_id = ?"
+ "UPDATE messages SET remote_id = ? WHERE ROWID = ?"
+ "Unexpected error: %@"
+ "Unexpected meeting message type %s"
+ "[%.*hhx-%{public}s] Did enable capabilities: %{public}s"
+ "[%.*hhx-%{public}s] Received post-auth capabilities from server: %{public}s"
+ "criteria charset key returnOptions "
+ "enablingCapabilities"
+ "enumerating event IDs for message"
+ "enumerating remote IDs for mailbox"
+ "flag"
+ "hasAttachments"
+ "importance"
+ "internetMessageHeaders"
+ "internetMessageId"
+ "isDraft"
+ "isRead"
+ "mailbox %s, count %ld, isLast: %{bool}d"
+ "microsoft.graph.eventMessage/meetingMessageType"
+ "migrating EWS folder ID to Graph"
+ "receivedDateTime"
+ "replyTo"
+ "sentDateTime"
+ "singleValueExtendedProperties($filter=id eq 'Long 0x0E08' or id eq 'Integer 0x0E17' or id eq 'Integer 0x1095' or id eq 'Integer 0x1081' or id eq 'Boolean {A7B529B5-4B75-47A7-A24F-20743D6C55CD} Name MessageJunkFlag' or id eq 'Boolean {A7B529B5-4B75-47A7-A24F-20743D6C55CD} Name MessageNotJunkFlag' or id eq 'Boolean {A7B529B5-4B75-47A7-A24F-20743D6C55CD} Name MessageJunkRecordedFlag' or id eq 'Boolean {A7B529B5-4B75-47A7-A24F-20743D6C55CD} Name MessageRedirectedFlag')"
+ "singleValueExtendedProperties($filter=id eq 'Long 0x0E08' or id eq 'String 0x1039' or id eq 'Integer 0x0E17' or id eq 'Integer 0x1095' or id eq 'Integer 0x1081' or id eq 'Boolean {A7B529B5-4B75-47A7-A24F-20743D6C55CD} Name MessageJunkFlag' or id eq 'Boolean {A7B529B5-4B75-47A7-A24F-20743D6C55CD} Name MessageNotJunkFlag' or id eq 'Boolean {A7B529B5-4B75-47A7-A24F-20743D6C55CD} Name MessageJunkRecordedFlag' or id eq 'Boolean {A7B529B5-4B75-47A7-A24F-20743D6C55CD} Name MessageRedirectedFlag')"
+ "unauthenticated(enablingCapabilities)"
+ "untagged(jmapAccess)"
+ "updating associated_id_string for event"
+ "updating remote ID for message"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECFlagChangeMessageActionResults.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageAction.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageActionResults.h"
- "Badly formed token."
- "CREATE TABLE IF NOT EXISTS searchable_attachments (attachment_id INTEGER PRIMARY KEY, attachment INTEGER REFERENCES attachments(ROWID) ON DELETE SET NULL, message_id INTEGER, transaction_id INTEGER NOT NULL);"
- "Creating searchable_attachments table"
- "Error creating searchable_data_detection_results table"
- "Response type mismatch for deleteMessage: expected GraphSyncMessageResource, got %s"
- "[%.*hhx-%{public}s] Did enable UIDONLY"
- "[%.*hhx-%{public}s] Received capabilities from server"
- "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Completed SEARCH for boundary IDs, but didn’t get any result from the server."
- "code"
- "mailbox %{sensitive,mask.mailbox}s, count %ld, isLast: %{bool}d"
- "unauthenticated(enablingUIDOnly)"
```
