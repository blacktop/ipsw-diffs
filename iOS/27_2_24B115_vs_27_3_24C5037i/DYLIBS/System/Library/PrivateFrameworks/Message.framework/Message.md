## Message

> `/System/Library/PrivateFrameworks/Message.framework/Message`

```diff

-3901.200.71.2.2
-  __TEXT.__text: 0xae7000
-  __TEXT.__objc_methlist: 0x144c4
-  __TEXT.__const: 0x6b898
-  __TEXT.__gcc_except_tab: 0x370c0
-  __TEXT.__cstring: 0x31576
+3901.300.26.0.0
+  __TEXT.__text: 0xaefadc
+  __TEXT.__objc_methlist: 0x1480c
+  __TEXT.__const: 0x6a7d8
+  __TEXT.__gcc_except_tab: 0x376e0
+  __TEXT.__cstring: 0x30fc6
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__oslogstring: 0x27ec0
+  __TEXT.__oslogstring: 0x280b0
   __TEXT.__ustring: 0x23ca
-  __TEXT.__swift5_typeref: 0x10d2c
-  __TEXT.__swift5_capture: 0x33978
-  __TEXT.__constg_swiftt: 0xda74
-  __TEXT.__swift5_reflstr: 0xf390
-  __TEXT.__swift5_fieldmd: 0x15508
-  __TEXT.__swift5_builtin: 0xd70
+  __TEXT.__swift5_typeref: 0x1101c
+  __TEXT.__swift5_capture: 0x337b0
+  __TEXT.__constg_swiftt: 0xdb58
+  __TEXT.__swift5_reflstr: 0xf4e0
+  __TEXT.__swift5_fieldmd: 0x156e0
+  __TEXT.__swift5_builtin: 0xd48
   __TEXT.__swift5_assocty: 0x1d38
-  __TEXT.__swift5_proto: 0x2a40
-  __TEXT.__swift5_types: 0x1834
-  __TEXT.__swift5_mpenum: 0x7f0
+  __TEXT.__swift5_proto: 0x2a58
+  __TEXT.__swift5_types: 0x1848
+  __TEXT.__swift5_mpenum: 0x7d8
   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x32570
-  __TEXT.__eh_frame: 0x18b48
+  __TEXT.__unwind_info: 0x327b8
+  __TEXT.__eh_frame: 0x18aa8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15470
-  __DATA_CONST.__objc_classlist: 0xb68
+  __DATA_CONST.__const: 0x15440
+  __DATA_CONST.__objc_classlist: 0xb80
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x530
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xb8c0
+  __DATA_CONST.__objc_selrefs: 0xba38
   __DATA_CONST.__objc_protorefs: 0x1b0
-  __DATA_CONST.__objc_superrefs: 0x678
+  __DATA_CONST.__objc_superrefs: 0x690
   __DATA_CONST.__objc_arraydata: 0xeb8
-  __DATA_CONST.__got: 0x2eb0
-  __AUTH_CONST.__const: 0xacda8
-  __AUTH_CONST.__cfstring: 0x18740
-  __AUTH_CONST.__objc_const: 0x23108
+  __DATA_CONST.__got: 0x2ea8
+  __AUTH_CONST.__const: 0xac7a0
+  __AUTH_CONST.__cfstring: 0x18660
+  __AUTH_CONST.__objc_const: 0x23638
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_arrayobj: 0xb10
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x4098
-  __AUTH.__objc_data: 0x5e28
-  __AUTH.__data: 0xb5d0
-  __DATA.__objc_ivar: 0x1388
-  __DATA.__data: 0xe9c8
+  __AUTH_CONST.__auth_got: 0x4070
+  __AUTH.__objc_data: 0x5f18
+  __AUTH.__data: 0xb7b0
+  __DATA.__objc_ivar: 0x13b8
+  __DATA.__data: 0xeb40
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0xec9
+  __DATA.__common: 0xed9
   __DATA_DIRTY.__objc_data: 0x1040
-  __DATA_DIRTY.__bss: 0x310
+  __DATA_DIRTY.__bss: 0x320
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 48722
-  Symbols:   21355
-  CStrings:  8552
+  Functions: 48814
+  Symbols:   21459
+  CStrings:  8563
 
Symbols:
+ +[MFAccountHealer log]
+ -[GmailAccount serverRoleForType:]
+ -[IMAPAccount serverRoleForType:]
+ -[MFAccountAutoFetchController startExpectingOneTimeCodeForAccount:]
+ -[MFAccountAutoFetchController stopExpectingOneTimeCodeForAccount:]
+ -[MFAccountHealer .cxx_destruct]
+ -[MFAccountHealer _alternateAccount]
+ -[MFAccountHealer _fetchServerFromACEDB:forIncomingServer:]
+ -[MFAccountHealer _getMailAccountFromDeliveryAccount:]
+ -[MFAccountHealer _lastTimeConnectToACEDBForAccount:]
+ -[MFAccountHealer _overwriteAccount:withAlternateAccount:]
+ -[MFAccountHealer _renewCredentialsWithError:completionHandler:]
+ -[MFAccountHealer _shouldHealAccount:withNewAccount:]
+ -[MFAccountHealer account]
+ -[MFAccountHealer alternateAccount]
+ -[MFAccountHealer error]
+ -[MFAccountHealer healFromAlternateAccountWithCompletion:]
+ -[MFAccountHealer healSilentlyWithCompletion:]
+ -[MFAccountHealer initWithAccount:networkController:error:]
+ -[MFAccountHealer networkController]
+ -[MFAccountHealer shouldHealFromAlternateAccount]
+ -[MFMailboxHierarchyNode .cxx_destruct]
+ -[MFMailboxHierarchyNode _findNodeForMailbox:removeNode:]
+ -[MFMailboxHierarchyNode addChild:]
+ -[MFMailboxHierarchyNode children]
+ -[MFMailboxHierarchyNode description]
+ -[MFMailboxHierarchyNode displayName]
+ -[MFMailboxHierarchyNode findNodeForMailbox:]
+ -[MFMailboxHierarchyNode initWithMailbox:]
+ -[MFMailboxHierarchyNode level]
+ -[MFMailboxHierarchyNode mailbox]
+ -[MFMailboxHierarchyNode parentMailbox]
+ -[MFMailboxHierarchyNode removeNodeForMailbox:]
+ -[MFMailboxHierarchyNode setDisplayName:]
+ -[MFMailboxHierarchyNode setLevel:]
+ -[MFMailboxHierarchyNode setParentMailbox:]
+ -[MFMailboxHierarchyTree .cxx_destruct]
+ -[MFMailboxHierarchyTree _addChildNode:toParentNode:]
+ -[MFMailboxHierarchyTree _insertMailboxUidsFlattenedFromMailboxNode:intoArray:currentLevel:]
+ -[MFMailboxHierarchyTree addChildMailbox:forMailboxNode:]
+ -[MFMailboxHierarchyTree displayNameForMailbox:]
+ -[MFMailboxHierarchyTree flattenedMailboxTreeRepresentation]
+ -[MFMailboxHierarchyTree initWithRootMailbox:]
+ -[MFMailboxHierarchyTree levelForMailbox:]
+ -[MFMailboxHierarchyTree mailboxHasSubMailboxes:]
+ -[MFMailboxHierarchyTree moveMailbox:toParent:]
+ -[MFMailboxHierarchyTree parentForMailbox:]
+ -[MFMailboxHierarchyTree removeNodeForMailbox:]
+ -[MFMailboxHierarchyTree rootMailboxNode]
+ -[MFMailboxHierarchyTree setDisplayName:forMailbox:]
+ -[MFMailboxUid _mailboxPersistenceForRemoteID]
+ -[MFMailboxUid childWithServerRole:]
+ -[MFMailboxUid descendantWithServerRole:]
+ -[MFMailboxUid level]
+ -[MFMailboxUid remoteID]
+ -[MFMailboxUid serverRole]
+ -[MFMailboxUid setRemoteID:]
+ -[MFSearchableIndexManager_iOS downloadStatistics]
+ -[MFSearchableIndexManager_iOS initWithDatabase:messagePersistence:richLinkPersistence:hookRegistry:accountsProvider:]
+ -[MFSearchableIndexManager_iOS test_tearDown]
+ -[MailAccount _addGenericChildrenToMailboxTree:forNode:hideNotes:]
+ -[MailAccount _addSpecialMailbox:toTree:]
+ -[MailAccount _allMailboxesIncludingLocals:withOutbox:hideInbox:hideNotes:]
+ -[MailAccount _putMailboxesRootedAt:intoArray:hideNotes:]
+ -[MailAccount _treeOfAllMailboxesIncludingLocals:withOutbox:hideInbox:hideNotes:]
+ -[MailAccount addSpecialMailbox:toArray:]
+ -[MailAccount allMailboxUidsSortedWithSpecialsAtTopIncludingLocals:]
+ -[MailAccount emailAddressesIncludingAliases]
+ -[MailAccount treeOfAllGenericMailboxes]
+ -[MailAccount treeOfAllMailboxUidsSortedWithSpecialsAtTopIncludingLocals:client:outbox:]
+ GCC_except_table166
+ GCC_except_table226
+ GCC_except_table238
+ GCC_except_table277
+ GCC_except_table278
+ GCC_except_table321
+ GCC_except_table332
+ GCC_except_table338
+ GCC_except_table350
+ GCC_except_table378
+ GCC_except_table380
+ GCC_except_table400
+ GCC_except_table403
+ GCC_except_table422
+ GCC_except_table450
+ GCC_except_table472
+ GCC_except_table475
+ GCC_except_table481
+ GCC_except_table484
+ GCC_except_table485
+ GCC_except_table486
+ GCC_except_table487
+ GCC_except_table490
+ GCC_except_table491
+ GCC_except_table500
+ GCC_except_table514
+ GCC_except_table519
+ GCC_except_table521
+ GCC_except_table523
+ GCC_except_table524
+ GCC_except_table525
+ GCC_except_table526
+ GCC_except_table551
+ GCC_except_table554
+ GCC_except_table556
+ GCC_except_table557
+ GCC_except_table558
+ GCC_except_table560
+ _EDMailboxRoleFromSpecialUseAttributes
+ _OBJC_CLASS_$_EDAddMailboxRemoteIDUpgradeStep
+ _OBJC_CLASS_$_MFAccountHealer
+ _OBJC_CLASS_$_MFMailboxHierarchyNode
+ _OBJC_CLASS_$_MFMailboxHierarchyTree
+ _OBJC_IVAR_$_MFAccountHealer._account
+ _OBJC_IVAR_$_MFAccountHealer._alternateAccount
+ _OBJC_IVAR_$_MFAccountHealer._error
+ _OBJC_IVAR_$_MFAccountHealer._networkController
+ _OBJC_IVAR_$_MFMailboxHierarchyNode._children
+ _OBJC_IVAR_$_MFMailboxHierarchyNode._displayName
+ _OBJC_IVAR_$_MFMailboxHierarchyNode._level
+ _OBJC_IVAR_$_MFMailboxHierarchyNode._mailbox
+ _OBJC_IVAR_$_MFMailboxHierarchyNode._parentMailbox
+ _OBJC_IVAR_$_MFMailboxHierarchyTree._mailboxStructureHasBeenCached
+ _OBJC_IVAR_$_MFMailboxHierarchyTree._nodesByMailbox
+ _OBJC_IVAR_$_MFMailboxHierarchyTree._rootMailboxNode
+ _OBJC_METACLASS_$_MFAccountHealer
+ _OBJC_METACLASS_$_MFMailboxHierarchyNode
+ _OBJC_METACLASS_$_MFMailboxHierarchyTree
+ __CompareMFMailboxHierarchyNodes
+ __OBJC_$_CLASS_METHODS_MFAccountAutoFetchController(Swift)
+ __OBJC_$_CLASS_METHODS_MFAccountHealer
+ __OBJC_$_CLASS_PROP_LIST_MFAccountHealer
+ __OBJC_$_INSTANCE_METHODS_MFAccountHealer
+ __OBJC_$_INSTANCE_METHODS_MFMailboxHierarchyNode
+ __OBJC_$_INSTANCE_METHODS_MFMailboxHierarchyTree
+ __OBJC_$_INSTANCE_VARIABLES_MFAccountHealer
+ __OBJC_$_INSTANCE_VARIABLES_MFMailboxHierarchyNode
+ __OBJC_$_INSTANCE_VARIABLES_MFMailboxHierarchyTree
+ __OBJC_$_PROP_LIST_MFAccountHealer
+ __OBJC_$_PROP_LIST_MFMailboxHierarchyNode
+ __OBJC_CLASS_PROTOCOLS_$_MFAccountHealer
+ __OBJC_CLASS_RO_$_MFAccountHealer
+ __OBJC_CLASS_RO_$_MFMailboxHierarchyNode
+ __OBJC_CLASS_RO_$_MFMailboxHierarchyTree
+ __OBJC_METACLASS_RO_$_MFAccountHealer
+ __OBJC_METACLASS_RO_$_MFMailboxHierarchyNode
+ __OBJC_METACLASS_RO_$_MFMailboxHierarchyTree
+ ___22+[MFAccountHealer log]_block_invoke
+ ___46-[MFAccountHealer healSilentlyWithCompletion:]_block_invoke
+ ___54-[MFAccountHealer _getMailAccountFromDeliveryAccount:]_block_invoke
+ ___58-[MFAccountHealer healFromAlternateAccountWithCompletion:]_block_invoke
+ ___64-[MFAccountHealer _renewCredentialsWithError:completionHandler:]_block_invoke
+ ___67-[MFAccountAutoFetchController stopExpectingOneTimeCodeForAccount:]_block_invoke
+ ___68-[MFAccountAutoFetchController startExpectingOneTimeCodeForAccount:]_block_invoke
+ ___block_descriptor_32_e25_v16?0"<MFTaskManager>"8l
+ ___block_descriptor_40_ea8_32bs_e20_v24?0Q8"MFError"16ls32l8
+ ___block_descriptor_40_ea8_32s_e42_B48?0{EDMessageRemoteIDAndGlobal=IIqqqq}8ls32l8
+ ___block_descriptor_48_ea8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_49_ea8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_80_ea8_32s40s48s56r64r_e42_B48?0{EDMessageRemoteIDAndGlobal=IIqqqq}8ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_88_ea8_32s40s48s56s64r72r_e42_B48?0{EDMessageRemoteIDAndGlobal=IIqqqq}8ls32l8s40l8s48l8s56l8r64l8r72l8
+ ___swift_exist.box.addr_destructor.14Tm
+ ___swift_memcpy121_8
+ ___swift_memcpy258_8
+ ___swift_memcpy280_8
+ ___swift_memcpy51_8
+ ___swift_memcpy82_8
+ _associated conformance 13IMAP2Behavior5StateV6RemoteV6ServerV17ListStatusSupportO6OptionOSHAASQ
+ _associated conformance 15IMAP2Connection9MechanismO4KindOSHAASQ
+ _associated conformance 15IMAP2Connection9MechanismO4SASLO4KindOSHAASQ
+ _associated conformance 15IMAP2Connection9MechanismO4SASLOSHAASQ
+ _associated conformance 15IMAP2Connection9MechanismOSHAASQ
+ _associated conformance 15IMAP2Connection9MechanismOSLAASQ
+ _get_enum_tag_for_layout_string 13IMAP2Behavior5StateV6RemoteV6ServerVSg
+ _get_enum_tag_for_layout_string 15IMAP2Connection9MechanismO
+ _get_enum_tag_for_layout_string 15IMAP2Connection9MechanismO4SASLO
+ _mailboxHasRole
+ _pthread_main_np
+ _symbolic Say_____G 15IMAP2Connection9MechanismO
+ _symbolic Shy_____G 13IMAP2Behavior5StateV6RemoteV6ServerV17ListStatusSupportO6OptionO
+ _symbolic Shy_____G 15IMAP2Connection9MechanismO
+ _symbolic So46EDSearchableIndexDownloadStatisticsPersistenceCSg
+ _symbolic _____ 13IMAP2Behavior5StateV6RemoteV6ServerV17ListStatusSupportO6OptionO
+ _symbolic _____ 15IMAP2Connection13GetJMAPAccessV
+ _symbolic _____ 15IMAP2Connection9MechanismO
+ _symbolic _____ 15IMAP2Connection9MechanismO4KindO
+ _symbolic _____ 15IMAP2Connection9MechanismO4SASLO
+ _symbolic _____ 15IMAP2Connection9MechanismO4SASLO4KindO
+ _symbolic _____Sg 15IMAP2Connection0B6ActionO
+ _symbolic _____Sg 15IMAP2Connection9MechanismO
+ _symbolic _____Sg 15IMAP2Connection9MechanismO4KindO
+ _symbolic _____Sg 16IMAP2Persistence11SyncRequestV2IDV
+ _symbolic _____Sg 16IMAP2Persistence8ActionIDV
+ _symbolic _____Sg_ABt 15IMAP2Connection9MechanismO
+ _symbolic _____Sg_Say_____G_____t 15IMAP2Connection9MechanismO4KindO 12NIOIMAPCore210CapabilityV 0A8Protocol8ServerIDV
+ _symbolic _____Sg_Say_____Gt 15IMAP2Connection9MechanismO4KindO 12NIOIMAPCore210CapabilityV
+ _symbolic _____Sg______Sgt 15IMAP2Connection14HandshakeReplyO AA20UnauthenticatedStateO6UpdateO
+ _symbolic _____Sgz_Xx 16IMAP2Persistence11SyncRequestV2IDV
+ _symbolic ______AAt 15IMAP2Connection0B6ActionO
+ _symbolic ______AAt 15IMAP2Connection20UnauthenticatedStateO6UpdateO
+ _symbolic ___________Say_____GSgt 15IMAP2Connection9MechanismO4KindO 12NIOIMAPCore212ResponseTextV AF10CapabilityV
+ _symbolic ___________Sg8responset 15IMAP2Connection9MechanismO 12NIOIMAPCore212ResponseTextV
+ _symbolic ___________SgSay_____G_____t 15IMAP2Connection6EnableV AA9MechanismO4KindO 12NIOIMAPCore210CapabilityV 0A8Protocol8ServerIDV
+ _symbolic _____y_____G s11_SetStorageC 13IMAP2Behavior5StateV6RemoteV6ServerV17ListStatusSupportO6OptionO
+ _symbolic _____y_____G s11_SetStorageC 15IMAP2Connection9MechanismO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 15IMAP2Connection9MechanismO
+ _symbolic _____y_____yAAy_____y_____y_____y_____GGG_____SgGGAJG s15LazyMapSequenceV s0a6FilterC0V s18ReversedCollectionV s0aC0V 12NIOIMAPCore220MessageIdentifierSetV AI3UIDV 16IMAP2Persistence0H10ToDownloadV
+ _symbolic _____y_____yAAy_____y_____y_____y_____y_____GGGG_____SgGGALG s15LazyMapSequenceV s0a6FilterC0V s5SliceV s18ReversedCollectionV s0aC0V 12NIOIMAPCore220MessageIdentifierSetV AK3UIDV 16IMAP2Persistence0I10ToDownloadV
+ _symbolic _____y_____y_____y_____GGG s18ReversedCollectionV s12LazySequenceV 12NIOIMAPCore220MessageIdentifierSetV AE3UIDV
+ _symbolic _____y_____y_____y_____y_____GGGG s5SliceV s18ReversedCollectionV s12LazySequenceV 12NIOIMAPCore220MessageIdentifierSetV AG3UIDV
+ _symbolic _____y_____y_____y_____y_____GGG_____SgG s15LazyMapSequenceV s18ReversedCollectionV s0aC0V 12NIOIMAPCore220MessageIdentifierSetV AG3UIDV 16IMAP2Persistence0G10ToDownloadV
+ _symbolic _____y_____y_____y_____y_____y_____GGGGG s16IndexingIteratorV s5SliceV s18ReversedCollectionV s12LazySequenceV 12NIOIMAPCore220MessageIdentifierSetV AI3UIDV
+ _symbolic _____y_____y_____y_____y_____y_____GGGG_____SgG s15LazyMapSequenceV s5SliceV s18ReversedCollectionV s0aC0V 12NIOIMAPCore220MessageIdentifierSetV AI3UIDV 16IMAP2Persistence0H10ToDownloadV
+ _symbolic _____y_____y_____y_____y_____y_____GGGG_____Sg_G s15LazyMapSequenceV8IteratorV s5SliceV s18ReversedCollectionV s0aC0V 12NIOIMAPCore220MessageIdentifierSetV AK3UIDV 16IMAP2Persistence0I10ToDownloadV
+ _symbolic _____y_____y_____y_____y_____y_____GGG_____SgGG s18LazyFilterSequenceV s0a3MapC0V s18ReversedCollectionV s0aC0V 12NIOIMAPCore220MessageIdentifierSetV AI3UIDV 16IMAP2Persistence0H10ToDownloadV
+ _symbolic _____y_____y_____y_____y_____y_____y_____GGGG_____SgGG s18LazyFilterSequenceV s0a3MapC0V s5SliceV s18ReversedCollectionV s0aC0V 12NIOIMAPCore220MessageIdentifierSetV AK3UIDV 16IMAP2Persistence0I10ToDownloadV
+ _symbolic _____y_____y_____y_____y_____y_____y_____GGGG_____SgG_G s18LazyFilterSequenceV8IteratorV s0a3MapC0V s5SliceV s18ReversedCollectionV s0aC0V 12NIOIMAPCore220MessageIdentifierSetV AM3UIDV 16IMAP2Persistence0J10ToDownloadV
+ _symbolic _____y_____y_____y_____y_____y_____y_____y_____GGGG_____SgGGAM_G s15LazyMapSequenceV8IteratorV s0a6FilterC0V AB s5SliceV s18ReversedCollectionV s0aC0V 12NIOIMAPCore220MessageIdentifierSetV AM3UIDV 16IMAP2Persistence0J10ToDownloadV
+ _symbolic y_____c 10Foundation3URLV
+ _type_layout_string 13IMAP2Behavior5StateV6RemoteV6ServerV17ListStatusSupportO
+ _type_layout_string 15IMAP2Connection9MechanismO
+ _type_layout_string 15IMAP2Connection9MechanismO4SASLO
- -[GmailAccount specialUseAttributeForType:]
- -[GmailAccount specialUseAttributesForMailbox:]
- -[IMAPAccount specialUseAttributeForType:]
- -[IMAPAccount specialUseAttributesForMailbox:]
- -[MFAccountAutoFetchController fetchOneTimeCodeForAccount:completion:]
- -[MFMailMessageLibrary _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMax:dateReceivedMin:limit:kind:block:]
- -[MFMailMessageLibrary _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMin:block:]
- -[MFMailMessageLibrary _enumerateMessageRemoteIDAndGlobalUsingBatchesForMailbox:excluding:inLatest:dateReceivedMin:kind:block:]
- -[MFMailboxUid descendantWithExtraAttribute:]
- -[MFSearchableIndexManager_iOS downloadRequestQueue]
- -[MFSearchableIndexManager_iOS initWithDatabase:messagePersistence:richLinkPersistence:hookRegistry:]
- GCC_except_table186
- GCC_except_table187
- GCC_except_table265
- GCC_except_table270
- GCC_except_table279
- GCC_except_table280
- GCC_except_table312
- GCC_except_table327
- GCC_except_table330
- GCC_except_table334
- GCC_except_table336
- GCC_except_table358
- GCC_except_table368
- GCC_except_table369
- GCC_except_table370
- GCC_except_table395
- GCC_except_table414
- GCC_except_table442
- GCC_except_table447
- GCC_except_table452
- GCC_except_table453
- GCC_except_table454
- GCC_except_table456
- GCC_except_table457
- GCC_except_table458
- GCC_except_table459
- GCC_except_table483
- GCC_except_table492
- GCC_except_table493
- GCC_except_table497
- GCC_except_table498
- GCC_except_table499
- GCC_except_table502
- GCC_except_table503
- GCC_except_table516
- GCC_except_table520
- GCC_except_table530
- GCC_except_table531
- GCC_except_table532
- GCC_except_table533
- GCC_except_table534
- GCC_except_table535
- GCC_except_table537
- GCC_except_table562
- GCC_except_table564
- GCC_except_table565
- GCC_except_table566
- GCC_except_table567
- GCC_except_table568
- _EDSearchableIndexTransactionItemsNeedDownloadToReindex
- _EDSearchableIndexTransactionItemsNeedReindex
- _EMFetchTypePush
- _OBJC_CLASS_$_EDSearchableIndexDownloadRequestQueue
- ___127-[MFMailMessageLibrary _enumerateMessageRemoteIDAndGlobalUsingBatchesForMailbox:excluding:inLatest:dateReceivedMin:kind:block:]_block_invoke
- ___137-[MFMailMessageLibrary _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMax:dateReceivedMin:limit:kind:block:]_block_invoke
- ___137-[MFMailMessageLibrary _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMax:dateReceivedMin:limit:kind:block:]_block_invoke_2
- ___137-[MFMailMessageLibrary _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMax:dateReceivedMin:limit:kind:block:]_block_invoke_3
- ___137-[MFMailMessageLibrary _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMax:dateReceivedMin:limit:kind:block:]_block_invoke_4
- ___42-[IMAPAccount specialUseAttributeForType:]_block_invoke
- ___46-[IMAPAccount specialUseAttributesForMailbox:]_block_invoke
- ___70-[MFAccountAutoFetchController fetchOneTimeCodeForAccount:completion:]_block_invoke
- ___block_descriptor_40_ea8_32bs_e25_v16?0"<MFTaskManager>"8ls32l8
- ___block_descriptor_40_ea8_32s_e12_v24?0Q8^B16ls32l8
- ___block_descriptor_40_ea8_32s_e42_B40?0{_MFMessageRemoteIDAndGlobal=IIqqq}8ls32l8
- ___block_descriptor_48_ea8_32r_e42_B40?0{_MFMessageRemoteIDAndGlobal=IIqqq}8lr32l8
- ___block_descriptor_48_ea8_32s40s_e24_v32?0{_NSRange=QQ}8^B24ls32l8s40l8
- ___block_descriptor_80_ea8_32s40s48s56r64r_e42_B40?0{_MFMessageRemoteIDAndGlobal=IIqqq}8ls32l8s40l8s48l8r56l8r64l8
- ___block_descriptor_88_ea8_32s40s48s56s64r72r_e42_B40?0{_MFMessageRemoteIDAndGlobal=IIqqq}8ls32l8s40l8s48l8s56l8r64l8r72l8
- ___block_descriptor_96_ea8_32s40bs_e41_B16?0"EDPersistenceDatabaseConnection"8ls32l8s40l8
- ___swift_exist.box.addr_destructor.10Tm
- ___swift_memcpy114_8
- ___swift_memcpy242_8
- ___swift_memcpy272_8
- ___swift_memcpy43_8
- _associated conformance 13IMAP2Behavior5StateV6RemoteV6ServerV17ListStatusSupportOSHAASQ
- _associated conformance 15IMAP2Connection13MechanismKindO8SASLKindOSHAASQ
- _associated conformance 15IMAP2Connection13MechanismKindOSHAASQ
- _associated conformance 15IMAP2Connection13MechanismKindOSLAASQ
- _get_enum_tag_for_layout_string 13IMAP2Protocol20PushRegistrationInfoVSg
- _get_enum_tag_for_layout_string 15IMAP2Connection0B6ActionO
- _get_enum_tag_for_layout_string 15IMAP2Connection13MechanismKindO
- _get_enum_tag_for_layout_string 15IMAP2Connection13MechanismKindO8SASLKindO
- _get_enum_tag_for_layout_string 15IMAP2Connection20UnauthenticatedStateO6UpdateO
- _specialUseAttributeForType:.map
- _specialUseAttributeForType:.onceToken
- _specialUseAttributesForMailbox:.knownSpecialAttributes
- _specialUseAttributesForMailbox:.onceToken
- _symbolic SaySo20EDPersistedMessageIDCG
- _symbolic Say_____G 15IMAP2Connection13MechanismKindO
- _symbolic Say_____G So37EDSearchableIndexDownloadRequestQueueC11EmailDaemonE0C0V
- _symbolic Shy_____G 15IMAP2Connection13MechanismKindO
- _symbolic Shy_____G s6UInt32V
- _symbolic So37EDSearchableIndexDownloadRequestQueueCSg
- _symbolic _____ 15IMAP2Connection13MechanismKindO
- _symbolic _____ 15IMAP2Connection13MechanismKindO8SASLKindO
- _symbolic _____Iegg_ 7Message24MailboxPersistenceHelperC18FindMessagesResultO
- _symbolic _____Sg 15IMAP2Connection13MechanismKindO
- _symbolic _____Sg_ABt 15IMAP2Connection13MechanismKindO
- _symbolic ______Say_____GSgt 12NIOIMAPCore212ResponseTextV AA10CapabilityV
- _symbolic ______Say_____G_____t 15IMAP2Connection6EnableV 12NIOIMAPCore210CapabilityV 0A8Protocol8ServerIDV
- _symbolic ___________Sg8responset 15IMAP2Connection13MechanismKindO 12NIOIMAPCore212ResponseTextV
- _symbolic _____y_____G s11_SetStorageC 15IMAP2Connection13MechanismKindO
- _symbolic _____y_____G s23_ContiguousArrayStorageC 15IMAP2Connection13MechanismKindO
- _type_layout_string 15IMAP2Connection0B6ActionO
- _type_layout_string 15IMAP2Connection13MechanismKindO
- _type_layout_string 15IMAP2Connection13MechanismKindO8SASLKindO
- _type_layout_string 15IMAP2Connection20UnauthenticatedStateO6UpdateO
CStrings:
+ " response "
+ "#Warning credential renewal failed: %@"
+ "%@, %@"
+ "-[MFSearchableIndexManager_iOS test_tearDown]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECFlagChangeMessageActionResults.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageAction.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageActionResults.h"
+ "<%{public}@> client:%{public}@"
+ "Attempting renewal of credentials for account: %{public}@"
+ "B48@?0{EDMessageRemoteIDAndGlobal=IIqqqq}8"
+ "Credential renewal for account %{public}@  %@"
+ "Current thread is main"
+ "Current thread must be main"
+ "Error adding remote_id column to mailboxes table: %{public}@"
+ "Error for error we use to determind to heal with another account or not: %{public}@, should heal? %@"
+ "Informations we got back from Ace DB: %@, %i, %i"
+ "MFAccountHealer.m"
+ "MFSearchableIndexManager_iOS.m"
+ "RaveBResetAttachmentIndexingCursor"
+ "RaveCBaseline"
+ "Unable to find account that is related to this SMTP server: %@:%i %i"
+ "User allow us to heal their account to: %@:%i %i"
+ "[%.*hhx-%.*X] Setting remote ID for mailbox '%{sensitive,mask.mailbox}s'."
+ "[%.*hhx-%.*X] [OTC] Clearing out previous sync #%u"
+ "[%.*hhx-%.*X] [OTC] Expecting a one-time code (sync #%u)"
+ "[%.*hhx-%.*X] [OTC] No one-time code sync to close."
+ "[%.*hhx-%.*X] [OTC] No primary mailbox to expect a one-time code in."
+ "[%.*hhx-%{public}s] Reporting JMAP access URL."
+ "[%.*hhx-%{public}s] Unexpected gotJMAPAccess"
+ "[%.*hhx] Did send action %s: report JMAP access URL."
+ "[%.*hhx] Ignoring %{public}s sync #%u without mailboxes."
+ "[%.*hhx] One-time code sync %{public}s keeping %ld mailbox(es)"
+ "[%.*hhx] One-time code sync %{public}s keeping mailbox {%.*hx} '%{sensitive,mask.mailbox}s'"
+ "[%.*hhx] Server support: move: %{BOOL}d, Gmail labels: %{BOOL}d, cond-store: %{BOOL}d, message-seq-numbers: %{BOOL}d special-use: %{BOOL}d list-status: %{BOOL}d status-mod-seq: %{BOOL}d mailbox-id: %{BOOL}d"
+ "failed"
+ "gettingJMAPAccess"
+ "oneTimeCode"
+ "unauthenticated(gettingJMAPAccess)"
+ "updateJMAPAccessURL"
+ "v24@?0Q8@\"MFError\"16"
+ "waitingForOneTimeCode"
- " LIMIT %llu"
- " messages.date_received <= %llu"
- " messages.date_received >= %llu"
- "(server_messages.remote_id < %llu OR %llu <= server_messages.remote_id)"
- ",%llu"
- "-[MFMailMessageLibrary _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMax:dateReceivedMin:limit:kind:block:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECFlagChangeMessageActionResults.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageAction.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageActionResults.h"
- "B40@?0{_MFMessageRemoteIDAndGlobal=IIqqq}8"
- "EXISTS (  SELECT global_message_id     FROM message_attachments LEFT OUTER     JOIN searchable_attachments ON message_attachments.rowid = searchable_attachments.attachment_id     WHERE message_attachments.global_message_id = messages.global_message_id       AND searchable_attachments.attachment_id IS NULL       AND message_attachments.attachment IS NOT NULL )"
- "Message/PersistenceAdaptor+LogNewestMessages.swift"
- "SELECT messages.global_message_id, server_messages.remote_id, messages.size, messages.date_received, messages.ROWID FROM (SELECT * FROM messages WHERE mailbox == %llu AND deleted = '0'       ORDER BY date_received DESC LIMIT %llu) AS messages INNER JOIN server_messages ON messages.ROWID = server_messages.message LEFT OUTER JOIN searchable_messages ON messages.searchable_message = searchable_messages.ROWID WHERE %@ ORDER BY messages.date_received DESC"
- "SELECT messages.global_message_id, server_messages.remote_id, messages.size, messages.date_received, messages.ROWID FROM messages INNER JOIN server_messages ON messages.ROWID = server_messages.message LEFT OUTER JOIN searchable_messages ON messages.searchable_message = searchable_messages.ROWID WHERE messages.mailbox == %llu AND %@ ORDER BY messages.date_received DESC"
- "[%.*hhx-%.*X] [%{sensitive,mask.mailbox}s] Download-and-index queue is missing."
- "[%.*hhx-%.*X] [%{sensitive,mask.mailbox}s] Found 0 recent messages within dateLimit. Retrying with broader date limit (oldestDate=%s, excludeCount=%ld)."
- "[%.*hhx-%.*X] [%{sensitive,mask.mailbox}s] Gave up on %ld message(s) larger than the index-download budget (%lld bytes); excluded from future backfill scans."
- "[%.*hhx-%.*X] [%{sensitive,mask.mailbox}s] Retry without dateLimit returned %ld messages (excludeCount=%ld, oldestDate=%s)"
- "[%.*hhx] Ignoring push sync #%u without mailboxes."
- "[%.*hhx] Server support: move: %{BOOL}d, Gmail labels: %{BOOL}d, cond-store: %{BOOL}d, message-seq-numbers: %{BOOL}d special-use: %{BOOL}d list-status: %{BOOL}d status-mod-seq: %{BOOL}d"
- "[%{public}s] Unable to find primary mailbox for fetching one-time-code."
- "_enumerateMessageRemoteIDAndGlobalUsingBatchesForMailbox took %.3g s (%zi iterations)"
- "list-status-highest-mod-seq"
- "messages.deleted = '0'"
- "messages.searchable_message IS NULL"
- "searchable_messages.message_body_indexed = 0"
- "searchable_messages.transaction_id IN (%@, %@)"
- "self"
- "server_messages.remote_id NOT IN (%@)"
- "v24@?0Q8^B16"
```
