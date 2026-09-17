## Mail

> `/System/Library/PrivateFrameworks/Mail.framework/Versions/A/Mail`

```diff

-3901.100.1.1.11
-  __TEXT.__text: 0xa00150
-  __TEXT.__objc_methlist: 0x1982c
-  __TEXT.__const: 0x615c9
-  __TEXT.__cstring: 0x31f49
-  __TEXT.__gcc_except_tab: 0x4c3ec
-  __TEXT.__oslogstring: 0x22139
+3901.200.34.0.0
+  __TEXT.__text: 0xa0fd64
+  __TEXT.__objc_methlist: 0x198a4
+  __TEXT.__const: 0x617a9
+  __TEXT.__cstring: 0x31f19
+  __TEXT.__gcc_except_tab: 0x4c3e8
+  __TEXT.__oslogstring: 0x222f9
   __TEXT.__ustring: 0x44
-  __TEXT.__swift5_typeref: 0xe634
-  __TEXT.__constg_swiftt: 0xbc08
-  __TEXT.__swift5_reflstr: 0xe5d0
-  __TEXT.__swift5_fieldmd: 0x13080
+  __TEXT.__swift5_typeref: 0xe744
+  __TEXT.__constg_swiftt: 0xbc64
+  __TEXT.__swift5_reflstr: 0xe760
+  __TEXT.__swift5_fieldmd: 0x131fc
   __TEXT.__swift5_builtin: 0xc44
-  __TEXT.__swift5_assocty: 0x1b58
-  __TEXT.__swift5_proto: 0x222c
-  __TEXT.__swift5_types: 0x1510
-  __TEXT.__swift5_capture: 0x25c7c
-  __TEXT.__swift5_mpenum: 0x760
+  __TEXT.__swift5_assocty: 0x1b70
+  __TEXT.__swift5_proto: 0x2244
+  __TEXT.__swift5_types: 0x1518
+  __TEXT.__swift5_capture: 0x25fd0
+  __TEXT.__swift5_mpenum: 0x768
   __TEXT.__swift5_protos: 0x60
-  __TEXT.__unwind_info: 0x2d750
-  __TEXT.__eh_frame: 0x15a30
+  __TEXT.__unwind_info: 0x2d9b8
+  __TEXT.__eh_frame: 0x15e90
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
+  __DATA_CONST.__objc_selrefs: 0xe090
   __DATA_CONST.__objc_protorefs: 0x1d0
   __DATA_CONST.__objc_superrefs: 0x840
   __DATA_CONST.__objc_arraydata: 0x270
-  __DATA_CONST.__got: 0x3778
-  __AUTH_CONST.__const: 0x89d28
-  __AUTH_CONST.__cfstring: 0x1a6c0
-  __AUTH_CONST.__objc_const: 0x2b308
+  __DATA_CONST.__got: 0x3790
+  __AUTH_CONST.__const: 0x8a5c8
+  __AUTH_CONST.__cfstring: 0x1a660
+  __AUTH_CONST.__objc_const: 0x2b210
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0xd08
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x3468
-  __AUTH.__objc_data: 0x6338
-  __AUTH.__data: 0x9f70
+  __AUTH_CONST.__auth_got: 0x3488
+  __AUTH.__objc_data: 0x6298
+  __AUTH.__data: 0xa130
   __DATA.__objc_ivar: 0x162c
-  __DATA.__data: 0xc6dc
+  __DATA.__data: 0xc724
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0xd7c
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
+  Functions: 42831
+  Symbols:   28646
+  CStrings:  7742
 
Symbols:
+ +[MFMailAccount _accountContainingEmailAddress:matchingAddress:fullUserName:includingInactive:]
+ +[MFMailAccount accountContainingEmailAddress:includingInactive:]
+ +[MFMailAccount accountWithObjectID:]
+ +[MFSMTPAccount log]
+ -[MFEWSConnection setupConnectionErrorForMonitorWithPort:usingSSL:serverTrust:]
+ -[MFEWSDeliveryAccount shouldIncludeBCCInMIMEHeaders]
+ -[MFExchangeAccount shouldIncludeBCCInMIMEHeaders]
+ -[MFExchangeConnection generateInternalAuthenticationError:]
+ -[MFExchangeConnection isAuthenticationError:]
+ -[MFExchangeConnection recoverySuggestionForNSURLError:port:usingSSL:helpAnchor:]
+ -[MFMailAccount isPrimaryAppleAccount]
+ -[MFMailboxTransformer _accountIdentifierForMailbox:accountIdentifiers:]
+ -[MFMailboxTransformer _transformMailbox:parent:accountIdentifiers:legacyMailboxToMailboxMap:objectIDToLegacyMailboxMap:]
+ -[MFSMTPAccount _repairMisconfiguredAppleTokenAccountIfNeeded]
+ GCC_except_table238
+ GCC_except_table253
+ GCC_except_table261
+ GCC_except_table330
+ GCC_except_table345
+ GCC_except_table349
+ GCC_except_table372
+ _ACAccountPropertyAllowsInsecureAuthentication
+ _ACCredentialTypeToken
+ _OBJC_CLASS_$_EDListUnsubscribeDetector
+ _OBJC_CLASS_$_MCImageMetadataResult
+ _OBJC_CLASS_$_MCImageMetadataService
+ __OBJC_$_CLASS_PROP_LIST_MFSMTPAccount
+ ___121-[MFMailboxTransformer _transformMailbox:parent:accountIdentifiers:legacyMailboxToMailboxMap:objectIDToLegacyMailboxMap:]_block_invoke
+ ___20+[MFSMTPAccount log]_block_invoke
+ ___block_descriptor_72_ea8_32s40s48r56r64r_e28_v32?0"MFCriterion"8Q16^B24l
+ ___swift_memcpy6_1
+ _associated conformance 12NIOIMAPCore211ParseBufferV7NewlineOSHAASQ
+ _associated conformance 12NIOIMAPCore213SortCriterionO3KeyOSHAASQ
+ _associated conformance 12NIOIMAPCore213SortCriterionOSHAASQ
+ _associated conformance 4Mail12MailboxRowIDVs27ExpressibleByIntegerLiteralAA0gH4TypesADP_s01_ef7BuiltingH0
+ _objc_msgSend$_accountContainingEmailAddress:matchingAddress:fullUserName:includingInactive:
+ _objc_msgSend$_accountIdentifierForMailbox:accountIdentifiers:
+ _objc_msgSend$_repairMisconfiguredAppleTokenAccountIfNeeded
+ _objc_msgSend$_transformMailbox:parent:accountIdentifiers:legacyMailboxToMailboxMap:objectIDToLegacyMailboxMap:
+ _objc_msgSend$aa_primaryAppleAccount
+ _objc_msgSend$appendHeaderData:recipients:recipientsByHeaderKey:expandGroups:includeComment:includeBCC:
+ _objc_msgSend$credentialType
+ _objc_msgSend$generateInternalAuthenticationError:
+ _objc_msgSend$handleGraphSyncError:
+ _objc_msgSend$handlePOSIXError:
+ _objc_msgSend$handleURLError:
+ _objc_msgSend$imageMetadataFor:
+ _objc_msgSend$initAsEphemeralID:representedObjectID:
+ _objc_msgSend$initWithMetadataResult:name:type:
+ _objc_msgSend$isAuthenticationError:
+ _objc_msgSend$metadataForImageData:webView:error:
+ _objc_msgSend$recordMessagesNeedToBeDonated:indexingType:trigger:
+ _objc_msgSend$recoverySuggestionForNSURLError:port:usingSSL:helpAnchor:
+ _objc_msgSend$remoteMailAccountsEmployedBy
+ _objc_msgSend$representedObjectID
+ _objc_msgSend$setupConnectionErrorForMonitorWithPort:usingSSL:serverTrust:
+ _objc_msgSend$shouldIncludeBCCInMIMEHeaders
+ _symbolic B2
+ _symbolic SDy__________G 16IMAP2Persistence15OpaqueMailboxIDV AA13SearchRequestV15RangesToExcludeV
+ _symbolic SDy__________y_____GG 16IMAP2Persistence15OpaqueMailboxIDV 12NIOIMAPCore228MessageIdentifierSetNonEmptyV AD3UIDV
+ _symbolic Say_____G 12NIOIMAPCore213SortCriterionO
+ _symbolic Say_____G8criteria_SS7charset_____3keySay_____G13returnOptionst 12NIOIMAPCore213SortCriterionO AA9SearchKeyO AA0D12ReturnOptionO
+ _symbolic So21MCImageMetadataResultCSg
+ _symbolic So21MCImageMetadataResultCSgz_Xx
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
+ _symbolic _____Sg 9GraphSync0aB13EventResourceV
+ _symbolic _____Sg 9GraphSync8APIErrorO
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
+ _symbolic xq_xq_Iegnnrr_
- +[MFAddSearchableDataDetectionResultsTable targetVersion]
- +[MFCreateSearchableAttachmentsTablesUpgradeStep targetVersion]
- +[MFMailAccount _accountContainingEmailAddress:matchingAddress:fullUserName:]
- -[MFAddSearchableDataDetectionResultsTable runWithRowIDsNeedingConversationRecalculation:]
- -[MFCreateSearchableAttachmentsTablesUpgradeStep runWithRowIDsNeedingConversationRecalculation:]
- -[MFEWSConnection _setupConnectionErrorForMonitorWithPort:usingSSL:serverTrust:]
- -[MFMailboxTransformer _transformMailbox:parent:legacyMailboxToMailboxMap:objectIDToLegacyMailboxMap:]
- GCC_except_table276
- GCC_except_table321
- GCC_except_table352
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
CStrings:
+ "$hasnoattachment"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECFlagChangeMessageActionResults.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageAction.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageActionResults.h"
+ "Could not decode the event message for a meeting response: %@"
+ "Couldn't parse JMAPACCESS URL"
+ "ErrorInvalidSyncStateData"
+ "GraphSyncErrorCode"
+ "GraphSyncErrorMessage"
+ "Image metadata fetch failed for junk classification"
+ "Invalid JMAPACCESS URL"
+ "Mail/RowID.swift"
+ "No calendar event is associated with the meeting request, cannot send an event response"
+ "Repairing SMTP account [%{public}@]: backfilling missing AuthenticationScheme %{public}@"
+ "Repairing SMTP account [%{public}@]: backfilling missing IdentityEmailAddress"
+ "Repairing SMTP account [%{public}@]: disabling AllowsInsecureAuthentication"
+ "SyncStateNotFound"
+ "The message to delete is already gone, treating the delete as a success"
+ "Type mismatch for calendarEventID: expected GraphSyncEventMessageResource, got %s"
+ "Unexpected error: %@"
+ "criteria charset key returnOptions "
+ "mailbox %s, count %ld, isLast: %{bool}d"
+ "untagged(jmapAccess)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECFlagChangeMessageActionResults.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageAction.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageActionResults.h"
- "Badly formed token."
- "CREATE TABLE IF NOT EXISTS searchable_attachments (attachment_id INTEGER PRIMARY KEY, attachment INTEGER REFERENCES attachments(ROWID) ON DELETE SET NULL, message_id INTEGER, transaction_id INTEGER NOT NULL);"
- "Creating searchable_attachments table"
- "Error creating searchable_data_detection_results table"
- "Response type mismatch for deleteMessage: expected GraphSyncMessageResource, got %s"
- "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Completed SEARCH for boundary IDs, but didn’t get any result from the server."
- "code"
- "mailbox %{sensitive,mask.mailbox}s, count %ld, isLast: %{bool}d"
```
