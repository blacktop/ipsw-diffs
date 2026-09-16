## Message

> `/System/Library/PrivateFrameworks/Message.framework/Message`

### Sections with Same Size but Changed Content

- `__TEXT.__ustring`

```diff

-3901.100.1.2.14
-  __TEXT.__text: 0xadd5d8
-  __TEXT.__objc_methlist: 0x1444c
-  __TEXT.__gcc_except_tab: 0x36a70
-  __TEXT.__const: 0x6b608
-  __TEXT.__cstring: 0x31366
-  __TEXT.__oslogstring: 0x27c80
-  __TEXT.__ustring: 0x23ca
+3901.200.34.0.0
+  __TEXT.__text: 0xae6a84
+  __TEXT.__objc_methlist: 0x144ac
+  __TEXT.__const: 0x6b7e8
+  __TEXT.__gcc_except_tab: 0x3701c
+  __TEXT.__cstring: 0x314c6
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__swift5_typeref: 0x10c02
-  __TEXT.__swift5_capture: 0x3377c
-  __TEXT.__constg_swiftt: 0xda18
+  __TEXT.__oslogstring: 0x27eb0
+  __TEXT.__ustring: 0x23ca
+  __TEXT.__swift5_typeref: 0x10d0c
+  __TEXT.__swift5_capture: 0x33968
+  __TEXT.__constg_swiftt: 0xda74
+  __TEXT.__swift5_reflstr: 0xf370
+  __TEXT.__swift5_fieldmd: 0x15508
   __TEXT.__swift5_builtin: 0xd70
-  __TEXT.__swift5_reflstr: 0xf240
-  __TEXT.__swift5_fieldmd: 0x153a4
-  __TEXT.__swift5_assocty: 0x1d20
-  __TEXT.__swift5_proto: 0x2a20
-  __TEXT.__swift5_types: 0x182c
-  __TEXT.__swift5_mpenum: 0x7e8
+  __TEXT.__swift5_assocty: 0x1d38
+  __TEXT.__swift5_proto: 0x2a38
+  __TEXT.__swift5_types: 0x1834
+  __TEXT.__swift5_mpenum: 0x7f0
   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x321a0
-  __TEXT.__eh_frame: 0x18624
+  __TEXT.__unwind_info: 0x32488
+  __TEXT.__eh_frame: 0x1895c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15448
+  __DATA_CONST.__const: 0x154c8
   __DATA_CONST.__objc_classlist: 0xb68
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x540
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xb858
+  __DATA_CONST.__objc_selrefs: 0xb8c0
   __DATA_CONST.__objc_protorefs: 0x1b8
   __DATA_CONST.__objc_superrefs: 0x678
   __DATA_CONST.__objc_arraydata: 0xeb8
-  __DATA_CONST.__got: 0x2e90
-  __AUTH_CONST.__const: 0xac760
-  __AUTH_CONST.__cfstring: 0x18660
-  __AUTH_CONST.__objc_const: 0x230d0
+  __DATA_CONST.__got: 0x2eb0
+  __AUTH_CONST.__const: 0xaccb8
+  __AUTH_CONST.__cfstring: 0x18700
+  __AUTH_CONST.__objc_const: 0x23118
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__objc_arrayobj: 0xb10
   __AUTH_CONST.__objc_intobj: 0x9a8
+  __AUTH_CONST.__objc_arrayobj: 0xb10
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x40f8
+  __AUTH_CONST.__auth_got: 0x4090
   __AUTH.__objc_data: 0x6418
-  __AUTH.__data: 0xb3f8
+  __AUTH.__data: 0xb5c8
   __DATA.__objc_ivar: 0x1388
-  __DATA.__data: 0xe918
+  __DATA.__data: 0xe948
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0xea9
+  __DATA.__common: 0xec9
   __DATA_DIRTY.__objc_data: 0xa50
   __DATA_DIRTY.__bss: 0x310
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/Synapse.framework/Synapse
-  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libParallelCompression.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 48496
-  Symbols:   26245
-  CStrings:  8525
+  Functions: 48698
+  Symbols:   26293
+  CStrings:  8545
 
Symbols:
+ +[MailAccount accountWithObjectID:]
+ +[MailAccount flushAllMessageStoreBodyDataCaches]
+ +[MailAccount flushAllMessageStoreCaches]
+ -[MFMailDelivery _fixHMERecipientsWithHeaders:]
+ -[MFMailboxUidTransformer _accountIdentifierForMailboxUid:accountIdentifiers:]
+ -[MFMailboxUidTransformer _transformMailboxUid:parent:accountIdentifiers:uidToMailboxMap:objectIDToUidMap:]
+ -[MFWeakObjectCache allObjects]
+ -[MailAccount flushAllMessageStoreBodyDataCaches]
+ -[MailAccount flushAllMessageStoreCaches]
+ -[MailAccount isPrimaryAppleAccount]
+ -[NSError(MessageContentView) mf_markupString]
+ GCC_except_table239
+ GCC_except_table273
+ GCC_except_table287
+ GCC_except_table288
+ GCC_except_table344
+ GCC_except_table356
+ GCC_except_table360
+ GCC_except_table374
+ GCC_except_table377
+ GCC_except_table413
+ GCC_except_table453
+ GCC_except_table458
+ GCC_except_table459
+ GCC_except_table480
+ GCC_except_table483
+ GCC_except_table488
+ GCC_except_table489
+ GCC_except_table498
+ GCC_except_table499
+ GCC_except_table503
+ GCC_except_table504
+ GCC_except_table508
+ GCC_except_table512
+ GCC_except_table516
+ GCC_except_table522
+ GCC_except_table534
+ GCC_except_table537
+ GCC_except_table559
+ GCC_except_table567
+ GCC_except_table568
+ _ECMessageHeaderKeyResentFrom
+ _EDSearchableIndexTransactionItemsNeedDownloadToReindex
+ _MFErrorPageMarkupFormat
+ _MFHTMLDataMayContainRichLinkContainer
+ _MFHTMLDataMayContainRichLinkContainer.marker
+ _MFHTMLDataMayContainRichLinkContainer.onceToken
+ _MFMIMEErrorDomain
+ _OBJC_CLASS_$_EDAccountDeletionDiagnostics
+ _OBJC_CLASS_$_EDListUnsubscribeDetector
+ _OBJC_CLASS_$_NSMapTable
+ _OUTLINED_FUNCTION_15
+ __OBJC_$_CATEGORY_MFMimePart_$_SMIMESupport
+ __OBJC_$_CATEGORY_NSString_$_IMAPNameEncoding
+ __OBJC_$_CLASS_METHODS_NSString(IMAPNameEncoding|FormatFlowedSupportInternal|FormatFlowedSupport|MimeEnrichedReader|NSStringUtils|MFDirectoryPathUtils|MFSharedResourcesDirectoryPathUtils)
+ __OBJC_$_INSTANCE_METHODS_MFMessageCriterion(DASearch|MFLibrarySearchableIndexAdditions|LibraryAdditions|PrivateLibraryAdditions|UnreadCountCriterion)
+ __OBJC_$_INSTANCE_METHODS_MFMimePart(SMIMESupport|SMIMEDecoding|SMIMEEncoding|FormatFlowedSupportInternal)
+ __OBJC_$_INSTANCE_METHODS_NSError(MFAccount|MessageAdditions|MessageContentView)
+ __OBJC_$_INSTANCE_METHODS_NSString(IMAPNameEncoding|FormatFlowedSupportInternal|FormatFlowedSupport|MimeEnrichedReader|NSStringUtils|MFDirectoryPathUtils|MFSharedResourcesDirectoryPathUtils)
+ __OBJC_$_PROP_LIST_MFMimePart_$_SMIMESupport
+ __OBJC_CLASS_PROTOCOLS_$_MFMessageCriterion(DASearch|MFLibrarySearchableIndexAdditions|LibraryAdditions|PrivateLibraryAdditions|UnreadCountCriterion)
+ ___107-[MFMailboxUidTransformer _transformMailboxUid:parent:accountIdentifiers:uidToMailboxMap:objectIDToUidMap:]_block_invoke
+ ___47-[MFMailDelivery _fixHMERecipientsWithHeaders:]_block_invoke
+ ___47-[MFMailDelivery _fixHMERecipientsWithHeaders:]_block_invoke_2
+ ___47-[MFMailDelivery _fixHMERecipientsWithHeaders:]_block_invoke_3
+ ___MFHTMLDataMayContainRichLinkContainer_block_invoke
+ ___block_descriptor_48_ea8_32s40r_e15_"NSString"8?0lr40l8s32l8
+ ___block_descriptor_64_ea8_32s40bs48r56r_e26_"NSArray"16?0"NSArray"8ls32l8r48l8s40l8r56l8
+ ___block_descriptor_80_ea8_32s40s48bs56r64r72r_e25_v32?0"NSString"8Q16^B24ls32l8r56l8s48l8r64l8r72l8s40l8
+ ___swift_memcpy6_1
+ _associated conformance 12NIOIMAPCore211ParseBufferV7NewlineOSHAASQ
+ _associated conformance 12NIOIMAPCore213SortCriterionO3KeyOSHAASQ
+ _associated conformance 12NIOIMAPCore213SortCriterionOSHAASQ
+ _associated conformance 7Message12MailboxRowIDVs27ExpressibleByIntegerLiteralAA0gH4TypesADP_s01_ef7BuiltingH0
+ _messageForFragment
+ _objc_msgSend$_fixHMERecipientsWithHeaders:
+ _objc_msgSend$accountObjectID
+ _objc_msgSend$accountWithObjectID:
+ _objc_msgSend$copyFirstHeaderForKey:
+ _objc_msgSend$copyFirstNonDecodedHeaderForKey:
+ _objc_msgSend$ef_containsData:
+ _objc_msgSend$ef_match
+ _objc_msgSend$ef_prefix:
+ _objc_msgSend$flushAllCaches
+ _objc_msgSend$flushAllMessageStoreBodyDataCaches
+ _objc_msgSend$flushAllMessageStoreCaches
+ _objc_msgSend$initAsEphemeralID:representedObjectID:
+ _objc_msgSend$localizedStringWithFormat:
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
+ _objc_msgSend$mf_isSMIMEError
+ _objc_msgSend$mf_stringByEscapingHTMLCodes
+ _objc_msgSend$notifyOfAccountRemovedFromIndex:
+ _objc_msgSend$representedObjectID
+ _objc_msgSend$resolvedPolicyForIMAPHost:
+ _objc_msgSend$searchableMessageForBaseMessage:htmlContent:hasCompleteData:isEncrypted:includeEncryptedBody:
+ _swift_release_x11
+ _symbolic SDy__________G 16IMAP2Persistence15OpaqueMailboxIDV AA13SearchRequestV15RangesToExcludeV
+ _symbolic SDy__________y_____GG 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore228MessageIdentifierSetNonEmptyV AD3UIDV
+ _symbolic Say_____G 12NIOIMAPCore213SortCriterionO
+ _symbolic Say_____G8criteria_SS7charset_____3keySay_____G13returnOptionst 12NIOIMAPCore213SortCriterionO AA9SearchKeyO AA0D12ReturnOptionO
+ _symbolic So16MFLibraryMessageCSo7MFErrorCSgIeggo_
+ _symbolic So31EDSearchableIndexDownloadPolicyCSg
+ _symbolic So7MFErrorCSgz_Xx
+ _symbolic _____ 12NIOIMAPCore211ParseBufferV7NewlineO
+ _symbolic _____ 12NIOIMAPCore213SortCriterionO
+ _symbolic _____ 12NIOIMAPCore213SortCriterionO3KeyO
+ _symbolic _____ 12NIOIMAPCore214ResponseParserV0B10AndNewlineV
+ _symbolic _____ 13IMAP2Behavior20MessageDownloadStateV
+ _symbolic _____3key______y_____G5valuet 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore228MessageIdentifierSetNonEmptyV AD3UIDV
+ _symbolic _____7mailbox_Say_____GSb6isLastt 16IMAP2Persistence15OpaqueMailboxIDV AA0C26PersistedMessageIdentifierV
+ _symbolic _____7mailbox______Sg5valuet 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore225ModificationSequenceValueV
+ _symbolic _____Sg 10Foundation13URLComponentsV
+ _symbolic _____Sg 12NIOIMAPCore211ParseBufferV7NewlineO
+ _symbolic _____Sg 13IMAP2Behavior23DetermineMessageBatchesV9CommandIDO
+ _symbolic _____Sg_ABt 13IMAP2Behavior23DetermineMessageBatchesV9CommandIDO
+ _symbolic ______AAt 13IMAP2Behavior23DetermineMessageBatchesV9CommandIDO
+ _symbolic ______SDy__________y_____GGt 16IMAP2Persistence13SearchRequestV2IDV AA013OpaqueMailboxE0V 12NIOIMAPCore220MessageIdentifierSetV AH3UIDV
+ _symbolic _____________________pIeglnrzo_ 12NIOIMAPCore211ParseBufferV AA12StackTrackerV AA13SortCriterionO s5ErrorP
+ _symbolic _____________________pIeglnrzo_ 12NIOIMAPCore211ParseBufferV AA12StackTrackerV AA13SortCriterionO3KeyO s5ErrorP
+ _symbolic _____________________pIeglydzo_ 12NIOIMAPCore211ParseBufferV AA12StackTrackerV AA13SortCriterionO s5ErrorP
+ _symbolic ___________t 16IMAP2Persistence15OpaqueMailboxIDV AA13SearchRequestV15RangesToExcludeV
+ _symbolic ___________t 16IMAP2Persistence15OpaqueMailboxIDV s6UInt32V
+ _symbolic ___________y_____Gt 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore228MessageIdentifierSetNonEmptyV AD3UIDV
+ _symbolic _____ySSSay___________tGG s18_DictionaryStorageC 16IMAP2Persistence15OpaqueMailboxIDV s6UInt32V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12NIOIMAPCore213SortCriterionO
+ _symbolic _____y____________G 13IMAP2Behavior24TaskHistoryWithCustomIDsV0F5IDMapV7CommandV AA23DetermineMessageBatchesV0I2IDO AI06ActionM0O
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC 16IMAP2Persistence15OpaqueMailboxIDV s6UInt32V
+ _symbolic _____y___________y_____GtG s23_ContiguousArrayStorageC 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore220MessageIdentifierSetV AF3UIDV
+ _symbolic _____y__________y_____GG s18_DictionaryStorageC 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore220MessageIdentifierSetV AF3UIDV
+ _symbolic _____y__________z______tKcG s23_ContiguousArrayStorageC 12NIOIMAPCore213SortCriterionO AC11ParseBufferV AC12StackTrackerV
+ _symbolic _____y_____y_____GG s23_ContiguousArrayStorageC 12NIOIMAPCore228MessageIdentifierSetNonEmptyV AC14SequenceNumberV
- -[MFMailboxUidTransformer _transformMailboxUid:parent:uidToMailboxMap:objectIDToUidMap:]
- -[MFSearchableIndex_iOS _indexMessage:includeBody:indexingType:]
- GCC_except_table166
- GCC_except_table226
- GCC_except_table335
- GCC_except_table338
- GCC_except_table366
- GCC_except_table450
- GCC_except_table455
- GCC_except_table478
- GCC_except_table481
- GCC_except_table486
- GCC_except_table487
- GCC_except_table490
- GCC_except_table491
- GCC_except_table500
- GCC_except_table501
- GCC_except_table506
- GCC_except_table510
- GCC_except_table514
- GCC_except_table518
- GCC_except_table525
- GCC_except_table528
- GCC_except_table557
- GCC_except_table560
- GCC_except_table563
- _DeliveryAccountsKey
- _MFNSStringFromColumnInStatement
- _MFReadLoggingDefaults
- _MFSecureMIMECompositionSpecificationSenderCapabilities
- _OBJC_CLASS_$_EMListUnsubscribeDetector
- _OBJC_CLASS_$_TRIClient
- __OBJC_$_CATEGORY_MFMimePart_$_FormatFlowedSupportInternal
- __OBJC_$_CATEGORY_NSString_$_FormatFlowedSupportInternal
- __OBJC_$_CLASS_METHODS_NSString(FormatFlowedSupportInternal|FormatFlowedSupport|IMAPNameEncoding|MimeEnrichedReader|NSStringUtils|MFDirectoryPathUtils|MFSharedResourcesDirectoryPathUtils)
- __OBJC_$_INSTANCE_METHODS_MFMessageCriterion(LibraryAdditions|PrivateLibraryAdditions|MFLibrarySearchableIndexAdditions|UnreadCountCriterion|DASearch)
- __OBJC_$_INSTANCE_METHODS_MFMimePart(FormatFlowedSupportInternal|SMIMESupport|SMIMEDecoding|SMIMEEncoding)
- __OBJC_$_INSTANCE_METHODS_NSError(MFAccount|MessageAdditions)
- __OBJC_$_INSTANCE_METHODS_NSString(FormatFlowedSupportInternal|FormatFlowedSupport|IMAPNameEncoding|MimeEnrichedReader|NSStringUtils|MFDirectoryPathUtils|MFSharedResourcesDirectoryPathUtils)
- __OBJC_CLASS_PROTOCOLS_$_MFMessageCriterion(LibraryAdditions|PrivateLibraryAdditions|MFLibrarySearchableIndexAdditions|UnreadCountCriterion|DASearch)
- ___88-[MFMailboxUidTransformer _transformMailboxUid:parent:uidToMailboxMap:objectIDToUidMap:]_block_invoke
- _associated conformance 12IMAP2Helpers15MillisecondDateVSHAASQ
- _associated conformance 12NIOIMAPCore211MailboxDataO10SearchSortVSHAASQ
- _associated conformance 12NIOIMAPCore225FetchModificationResponseVSHAASQ
- _objc_msgSend$_indexMessage:includeBody:indexingType:
- _objc_msgSend$booleanValue
- _objc_msgSend$client
- _objc_msgSend$csAccountTypeString
- _objc_msgSend$defaultPolicy
- _objc_msgSend$initWithRepresentedObjectID:
- _objc_msgSend$isPartOfExistingThread
- _objc_msgSend$levelForFactor:withNamespaceName:
- _objc_msgSend$searchableMessageAttachmentsForBaseMessage:includeEncryptedBody:
- _objc_msgSend$searchableMessageUpdateForBaseMessage:
- _symbolic SDy__________G 12NIOIMAPCore211MailboxNameV 16IMAP2Persistence13SearchRequestV15RangesToExcludeV
- _symbolic SDy__________y_____GG 12NIOIMAPCore211MailboxNameV AA28MessageIdentifierSetNonEmptyV AA3UIDV
- _symbolic Say_____G 11EmailDaemon17SearchableMessageV0A7AddressV
- _symbolic SayypG
- _symbolic Sb16includesFirstUID_t
- _symbolic So31EDSearchableIndexDownloadPolicyC
- _symbolic _____ 12IMAP2Helpers15MillisecondDateV
- _symbolic _____ 12NIOIMAPCore211MailboxDataO10SearchSortV
- _symbolic _____ 12NIOIMAPCore225FetchModificationResponseV
- _symbolic _____3key______y_____G5valuet 12NIOIMAPCore211MailboxNameV AA20MessageIdentifierSetV AA3UIDV
- _symbolic _____3key______y_____G5valuet 12NIOIMAPCore211MailboxNameV AA28MessageIdentifierSetNonEmptyV AA3UIDV
- _symbolic _____7mailbox_Say_____GSb6isLastt 12NIOIMAPCore211MailboxNameV 16IMAP2Persistence32OpaquePersistedMessageIdentifierV
- _symbolic _____7mailbox_Si5limitt 12NIOIMAPCore211MailboxNameV
- _symbolic _____7mailbox______Sg5valuet 12NIOIMAPCore211MailboxNameV AA25ModificationSequenceValueV
- _symbolic _____Sg 11EmailDaemon17SearchableMessageV8PriorityO
- _symbolic _____Sg 11EmailDaemon28SearchableMessageAttachmentsV
- _symbolic ______SDy__________y_____GGt 16IMAP2Persistence13SearchRequestV2IDV 12NIOIMAPCore211MailboxNameV AF20MessageIdentifierSetV AF3UIDV
- _symbolic ___________t 12NIOIMAPCore211MailboxNameV 16IMAP2Persistence13SearchRequestV15RangesToExcludeV
- _symbolic ___________t 12NIOIMAPCore211MailboxNameV s6UInt32V
- _symbolic ___________t 13IMAP2Behavior23DetermineMessageBatchesV9CommandIDO AC9TaskStateO
- _symbolic ___________y_____Gt 12NIOIMAPCore211MailboxNameV AA20MessageIdentifierSetV AA3UIDV
- _symbolic ___________y_____Gt 12NIOIMAPCore211MailboxNameV AA28MessageIdentifierSetNonEmptyV AA3UIDV
- _symbolic _____ySSSay___________tGG s18_DictionaryStorageC 12NIOIMAPCore211MailboxNameV s6UInt32V
- _symbolic _____y___________tG s23_ContiguousArrayStorageC 12NIOIMAPCore211MailboxNameV s6UInt32V
- _symbolic _____y___________y_____GtG s23_ContiguousArrayStorageC 12NIOIMAPCore211MailboxNameV AC20MessageIdentifierSetV AC3UIDV
- _type_layout_string 12IMAP2Helpers15MillisecondDateV
- _type_layout_string 12NIOIMAPCore211MailboxDataO10SearchSortV
- _type_layout_string 12NIOIMAPCore225FetchModificationResponseV
- _type_layout_string So13EMFetchOptionV
CStrings:
+ "$hasnoattachment"
+ "(messages.searchable_message IS NULL OR   searchable_messages.message_body_indexed = 0 OR   searchable_messages.transaction_id IN (%@, %@))"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECFlagChangeMessageActionResults.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageAction.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageActionResults.h"
+ "<html dir=auto><body><i><font color=#888>%@</font></i></body></html>"
+ "@\"NSArray\"16@?0@\"NSArray\"8"
+ "@\"NSString\"8@?0"
+ "Account %{public}@ is not enabled for data class Mail"
+ "Account became inactive: %{public}@"
+ "Almost leaked real address in HME reply"
+ "Backfill stopped after downloading %ld messages: the server is unavailable."
+ "Couldn't parse JMAPACCESS URL"
+ "Failed to download body during backfill: %{public}s"
+ "Failed to find a message for error: %{public}@"
+ "Found real recipient address (%{public}@) in HME reply, but was unable to find HME address to replace it with"
+ "Found real recipient address (%{public}@) in HME reply, replacing with %{public}@"
+ "Invalid JMAPACCESS URL"
+ "Leaked real address in HME reply"
+ "MESSAGE_CAUSED_PROBLEM"
+ "MESSAGE_UNAVAILABLE"
+ "Message/RowID.swift"
+ "Skipping remote content parsing (no enabled parsing options apply): %{public}@"
+ "_invalidateAndDeleteAccountData called for account %{public}@ deleteAccountData=%{BOOL}d"
+ "apple-rich-link"
+ "com.apple.email.library.writeMessageData"
+ "criteria charset key returnOptions "
+ "deleteAccount called for account %{public}@"
+ "invalidateAccount called for account %{public}@"
+ "mailbox %s, count %ld, isLast: %{bool}d"
+ "rebuildActiveMailboxesClauseWithActiveAccounts called with %d active accounts, %d inactive accounts"
+ "removeSearchableItemsForAccount called for account %@, domain identifier = %@"
+ "removing searchable items for inactive account %{public}@"
+ "server reported it is unavailable for task %@."
+ "untagged(jmapAccess)"
- "(messages.searchable_message IS NULL OR   searchable_messages.message_body_indexed = 0 OR   searchable_messages.transaction_id = %ld)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECFlagChangeMessageActionResults.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageAction.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageActionResults.h"
- "DeliveryAccounts"
- "MAIL_INDEXING"
- "Message/MFMessageFeature.swift"
- "SenderCapabilities"
- "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Completed SEARCH for boundary IDs, but didn’t get any result from the server."
- "[IMAPFetchMoreMessages] Enabled based an SearchIndexerInsideMaild A/B Experiment"
- "[IMAPInitialSyncByDate] Enabled based an SearchIndexerInsideMaild A/B Experiment"
- "[IndexOnlyForOlderBodies] Enabled based an SearchIndexerInsideMaild A/B Experiment"
- "emailsToExclude"
- "mailbox %{sensitive,mask.mailbox}s, count %ld, isLast: %{bool}d"
- "searchIndexerInsideMaild"
```
