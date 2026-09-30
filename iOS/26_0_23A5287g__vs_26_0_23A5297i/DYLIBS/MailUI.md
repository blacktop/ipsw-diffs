## MailUI

> `/System/Library/PrivateFrameworks/MailUI.framework/MailUI`

```diff

-3858.100.10.2.1
-  __TEXT.__text: 0x2620f4
-  __TEXT.__auth_stubs: 0x4c80
-  __TEXT.__objc_methlist: 0x98b4
-  __TEXT.__cstring: 0xe99a
-  __TEXT.__const: 0xb6a4
-  __TEXT.__oslogstring: 0x69f0
-  __TEXT.__gcc_except_tab: 0x125c
+3860.100.5.2.1
+  __TEXT.__text: 0x25fd94
+  __TEXT.__auth_stubs: 0x4cb0
+  __TEXT.__objc_methlist: 0x99a4
+  __TEXT.__cstring: 0xe7ea
+  __TEXT.__const: 0xb704
+  __TEXT.__oslogstring: 0x6a00
+  __TEXT.__gcc_except_tab: 0x12cc
   __TEXT.__dlopen_cstrs: 0xba
-  __TEXT.__ustring: 0x262
-  __TEXT.__swift5_typeref: 0xa92c
-  __TEXT.__constg_swiftt: 0x3650
-  __TEXT.__swift5_builtin: 0x474
-  __TEXT.__swift5_reflstr: 0x31a0
-  __TEXT.__swift5_fieldmd: 0x2db0
-  __TEXT.__swift5_assocty: 0xeb0
-  __TEXT.__swift5_proto: 0x568
-  __TEXT.__swift5_types: 0x408
-  __TEXT.__swift5_capture: 0x36a0
-  __TEXT.__swift_as_entry: 0xf0
+  __TEXT.__ustring: 0x2e2
+  __TEXT.__swift5_typeref: 0xa928
+  __TEXT.__constg_swiftt: 0x3638
+  __TEXT.__swift5_builtin: 0x488
+  __TEXT.__swift5_reflstr: 0x3140
+  __TEXT.__swift5_fieldmd: 0x2cf4
+  __TEXT.__swift5_assocty: 0xec8
+  __TEXT.__swift5_proto: 0x56c
+  __TEXT.__swift5_types: 0x404
+  __TEXT.__swift5_capture: 0x3670
+  __TEXT.__swift_as_entry: 0xfc
   __TEXT.__swift_as_ret: 0xbc
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x54b8
+  __TEXT.__unwind_info: 0x54d0
   __TEXT.__eh_frame: 0x2124
-  __TEXT.__objc_classname: 0x1568
-  __TEXT.__objc_methname: 0x1c9d9
-  __TEXT.__objc_methtype: 0x3fae
-  __TEXT.__objc_stubs: 0xfe80
-  __DATA_CONST.__got: 0x1a38
-  __DATA_CONST.__const: 0x2eb0
-  __DATA_CONST.__objc_classlist: 0x560
+  __TEXT.__objc_classname: 0x159e
+  __TEXT.__objc_methname: 0x1caf8
+  __TEXT.__objc_methtype: 0x3ff9
+  __TEXT.__objc_stubs: 0x10000
+  __DATA_CONST.__got: 0x1a48
+  __DATA_CONST.__const: 0x2fb8
+  __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x62f8
+  __DATA_CONST.__objc_selrefs: 0x6348
   __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0x2a8
+  __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x2650
-  __AUTH_CONST.__const: 0xc9a8
-  __AUTH_CONST.__cfstring: 0x48a0
-  __AUTH_CONST.__objc_const: 0x13938
+  __AUTH_CONST.__auth_got: 0x2668
+  __AUTH_CONST.__const: 0xc8a8
+  __AUTH_CONST.__cfstring: 0x4b20
+  __AUTH_CONST.__objc_const: 0x13c28
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1e80
+  __AUTH.__objc_data: 0x1f20
   __AUTH.__data: 0xbe8
-  __DATA.__objc_ivar: 0x9b8
-  __DATA.__data: 0x4f58
+  __DATA.__objc_ivar: 0x9d4
+  __DATA.__data: 0x4fa8
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x69c0
+  __DATA.__bss: 0x6b40
   __DATA.__common: 0x3f8
-  __DATA_DIRTY.__objc_data: 0x2cf8
-  __DATA_DIRTY.__data: 0x3128
-  __DATA_DIRTY.__bss: 0x4540
-  __DATA_DIRTY.__common: 0x40
+  __DATA_DIRTY.__objc_data: 0x2ce8
+  __DATA_DIRTY.__data: 0x3118
+  __DATA_DIRTY.__bss: 0x4450
+  __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/ColorSync.framework/ColorSync

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 14A4A12F-B5CC-37B7-A912-D5CF4809ADDB
-  Functions: 12058
-  Symbols:   13644
-  CStrings:  7711
+  UUID: 32FBD188-4CE9-3D4A-BAD1-9C37ECC8D3B0
+  Functions: 12100
+  Symbols:   13756
+  CStrings:  7755
 
Symbols:
+ +[MUICategoryMailboxCountHelper log]
+ -[MUICategoryMailboxCount ef_publicDescription]
+ -[MUICategoryMailboxCount fullCount]
+ -[MUICategoryMailboxCount primaryCount]
+ -[MUICategoryMailboxCount setFullCount:]
+ -[MUICategoryMailboxCount setPrimaryCount:]
+ -[MUICategoryMailboxCountHelper .cxx_destruct]
+ -[MUICategoryMailboxCountHelper _fetchCountForPrimaryOnly:completion:]
+ -[MUICategoryMailboxCountHelper initWithMailboxes:messageRepository:]
+ -[MUICategoryMailboxCountHelper mailboxes]
+ -[MUICategoryMailboxCountHelper messageCount]
+ -[MUICategoryMailboxCountHelper messageRepository]
+ -[MUICategoryMailboxCountHelper setMailboxes:]
+ -[MUICategoryMailboxCountHelper setMessageRepository:]
+ -[MUIMessageListOnboardingTipDataSource count]
+ -[MUIMessageListOnboardingTipDataSource helper]
+ -[MUIMessageListOnboardingTipDataSource initWithConfiguration:bucket:countHelper:]
+ -[MUIMessageListOnboardingTipDataSource setCount:]
+ -[MUIMessageListOnboardingTipDataSource setHelper:]
+ -[MUISearchInstantAnswersSuggestion initWithMessage:instantAnswer:messageList:]
+ -[MUISearchInstantAnswersSuggestion messageList]
+ -[MessageListDataSource pendingSectionDataSources]
+ -[MessageListDataSource setPendingSectionDataSources:]
+ -[MessageListSectionDataSource description]
+ GCC_except_table165
+ GCC_except_table172
+ GCC_except_table28
+ GCC_except_table57
+ GCC_except_table73
+ GCC_except_table86
+ _MUILocalizedOnboardingStringAllMailMessage
+ _MUILocalizedOnboardingStringAllMailTitle
+ _MUILocalizedOnboardingStringBadgeSettingsActionTitle
+ _MUILocalizedOnboardingStringBadgeSettingsMessage
+ _MUILocalizedOnboardingStringBadgeSettingsSecondaryActionTitle
+ _MUILocalizedOnboardingStringBadgeSettingsTitle
+ _MUILocalizedOnboardingStringPrimaryActionTitle
+ _MUILocalizedOnboardingStringPrimaryInformation
+ _MUILocalizedOnboardingStringPrimaryMessage
+ _MUILocalizedOnboardingStringPrimarySecondaryActionTitle
+ _MUILocalizedOnboardingStringPrimaryTitle
+ _MUILocalizedOnboardingStringPromotionsMessage
+ _MUILocalizedOnboardingStringPromotionsTitle
+ _MUILocalizedOnboardingStringTransactionsMessage
+ _MUILocalizedOnboardingStringTransactionsTitle
+ _MUILocalizedOnboardingStringUpdatesMessage
+ _MUILocalizedOnboardingStringUpdatesTitle
+ _MUIOnboardingTipFromBucket
+ _OBJC_CLASS_$_MUICategoryMailboxCount
+ _OBJC_CLASS_$_MUICategoryMailboxCountHelper
+ _OBJC_IVAR_$_MUICategoryMailboxCount._fullCount
+ _OBJC_IVAR_$_MUICategoryMailboxCount._primaryCount
+ _OBJC_IVAR_$_MUICategoryMailboxCountHelper._mailboxes
+ _OBJC_IVAR_$_MUICategoryMailboxCountHelper._messageRepository
+ _OBJC_IVAR_$_MUIMessageListOnboardingTipDataSource._count
+ _OBJC_IVAR_$_MUIMessageListOnboardingTipDataSource._helper
+ _OBJC_IVAR_$_MUISearchInstantAnswersSuggestion._messageList
+ _OBJC_IVAR_$_MessageListDataSource._pendingSectionDataSources
+ _OBJC_METACLASS_$_MUICategoryMailboxCount
+ _OBJC_METACLASS_$_MUICategoryMailboxCountHelper
+ __OBJC_$_CLASS_METHODS_MUICategoryMailboxCountHelper
+ __OBJC_$_INSTANCE_METHODS_MUICategoryMailboxCount
+ __OBJC_$_INSTANCE_METHODS_MUICategoryMailboxCountHelper
+ __OBJC_$_INSTANCE_VARIABLES_MUICategoryMailboxCount
+ __OBJC_$_INSTANCE_VARIABLES_MUICategoryMailboxCountHelper
+ __OBJC_$_PROP_LIST_MUICategoryMailboxCount
+ __OBJC_$_PROP_LIST_MUICategoryMailboxCountHelper
+ __OBJC_CLASS_PROTOCOLS_$_MUICategoryMailboxCount
+ __OBJC_CLASS_RO_$_MUICategoryMailboxCount
+ __OBJC_CLASS_RO_$_MUICategoryMailboxCountHelper
+ __OBJC_METACLASS_RO_$_MUICategoryMailboxCount
+ __OBJC_METACLASS_RO_$_MUICategoryMailboxCountHelper
+ ___115-[MessageListSectionDataSource _addedItemIDs:before:existingItemID:toThreadWithItemID:inCollection:isLastObserver:]_block_invoke.152
+ ___115-[MessageListSectionDataSource _addedItemIDs:before:existingItemID:toThreadWithItemID:inCollection:isLastObserver:]_block_invoke_2.153
+ ___117-[MessageListSectionDataSource _deleteItemsWithIDs:fromCollection:animated:useImmediateCompletion:completionHandler:]_block_invoke.158
+ ___117-[MessageListSectionDataSource _deleteItemsWithIDs:fromCollection:animated:useImmediateCompletion:completionHandler:]_block_invoke_2.162
+ ___123-[MessageListSectionDataSource collection:changedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:]_block_invoke.115
+ ___36+[MUICategoryMailboxCountHelper log]_block_invoke
+ ___45-[MUICategoryMailboxCountHelper messageCount]_block_invoke
+ ___45-[MUICategoryMailboxCountHelper messageCount]_block_invoke_2
+ ___45-[MUICategoryMailboxCountHelper messageCount]_block_invoke_3
+ ___51-[MessageListDataSource _performDataSourceUpdates:]_block_invoke_3
+ ___51-[MessageListDataSource _performDataSourceUpdates:]_block_invoke_3.cold.1
+ ___58-[MessageListDataSource applyMessageListDataSourceUpdate:]_block_invoke_7
+ ___62-[MessageListSectionDataSource _maybeReloadForTimedOutItemIDs]_block_invoke.136
+ ___62-[MessageListSectionDataSource collection:movedItemIDs:after:]_block_invoke.111
+ ___63-[MessageListSectionDataSource collection:movedItemIDs:before:]_block_invoke.106
+ ___63-[MessageListSectionDataSource collectionDidFinishInitialLoad:]_block_invoke.123
+ ___63-[MessageListSectionDataSource didFinishRecoveryForCollection:]_block_invoke.118
+ ___70-[MUICategoryMailboxCountHelper _fetchCountForPrimaryOnly:completion:]_block_invoke
+ ___70-[MUICategoryMailboxCountHelper _fetchCountForPrimaryOnly:completion:]_block_invoke.cold.1
+ ___80-[MessageListSectionDataSource collection:replacedExistingItemID:withNewItemID:]_block_invoke.117
+ ___80-[MessageListSectionDataSource collection:replacedExistingItemID:withNewItemID:]_block_invoke.117.cold.1
+ ___83-[MessageListSectionDataSource collection:didFinishInitialLoadForThreadWithItemID:]_block_invoke.122
+ ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.87
+ ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.89
+ ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.89.cold.1
+ ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.90
+ ___93-[MUIMessageListOnboardingTipDataSource beginObservingAnimated:nextUpdateNeedsCleanSnapshot:]_block_invoke_2
+ ___93-[MUIMessageListOnboardingTipDataSource beginObservingAnimated:nextUpdateNeedsCleanSnapshot:]_block_invoke_3
+ ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.167
+ ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.167.cold.1
+ ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.171
+ ___block_descriptor_41_e8_32bs_e30_v24?0"NSNumber"8"NSError"16ls32l8
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40bs_e33_v16?0"MUICategoryMailboxCount"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e8_v16?0q8lr40l8s32l8
+ ___block_descriptor_52_e8_32s40s_e22_v16?0"NSMutableSet"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8r48l8s32l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e41_v24?0"<EMMessageListItem>"8"NSError"16lw72l8s64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72w_e29_v16?0"<EMMessageListItem>"8lw72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.123
+ ___block_literal_global.126
+ ___block_literal_global.241
+ _associated conformance So16MUIOnboardingTipVSH6MailUISQ
+ _block_copy_helper.380
+ _block_copy_helper.66
+ _block_descriptor.382
+ _block_descriptor.68
+ _block_destroy_helper.381
+ _block_destroy_helper.67
+ _dispatch_get_global_queue
+ _dispatch_group_notify
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA6HStackVyACyACyAA5ImageVAA18_AspectRatioLayoutVGAA06_FrameI0VGGALGAA08_PaddingI0VGAQGAA4ViewHPAraTHPAoaTHPAnaTHPyHC_AlA0L8ModifierHPyHCHC_AqaUHPyHCHC_AqaUHPyHCHC.3
+ _objc_msgSend$_fetchCountForPrimaryOnly:completion:
+ _objc_msgSend$configureForBucket:primaryUnreadCount:otherUnreadCount:
+ _objc_msgSend$customizeButton
+ _objc_msgSend$ef_andCompoundPredicateWithSubpredicates:
+ _objc_msgSend$fullCount
+ _objc_msgSend$helper
+ _objc_msgSend$initWithConfiguration:bucket:countHelper:
+ _objc_msgSend$initWithMailboxes:messageRepository:
+ _objc_msgSend$initWithTargetClass:predicate:sortDescriptors:queryOptions:label:
+ _objc_msgSend$messageCount
+ _objc_msgSend$okButton
+ _objc_msgSend$pendingSectionDataSources
+ _objc_msgSend$performCountQuery:completionHandler:
+ _objc_msgSend$primaryCount
+ _objc_msgSend$setCount:
+ _objc_msgSend$setFullCount:
+ _objc_msgSend$setPrimaryCount:
+ _objc_msgSend$turnOffCategoriesButton
+ _symbolic _____ 6MailUI42MessageListOnboardingTipCollectionViewCellC12LayoutValues33_A0B88E46F03250F4D6BAB59C18D42666LLO
+ _symbolic _____ So16MUIOnboardingTipV
+ _symbolic _____yAAyAAy_____yAAyAAy__________G_____GGAFG_____GAJG 7SwiftUI15ModifiedContentV AA6HStackV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameI0V AA08_PaddingI0V
+ _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameH0V
+ _symbolic _____yAAy_____yAAyAAy__________G_____GGAFG_____G 7SwiftUI15ModifiedContentV AA6HStackV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameI0V AA08_PaddingI0V
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV
+ _symbolic _____y_____yAAyAAy__________G_____GGAFG 7SwiftUI15ModifiedContentV AA6HStackV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameI0V
+ _symbolic _____y_____yABy__________G_____GG 7SwiftUI6HStackV AA15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameI0V
- -[MUIMessageListOnboardingTipDataSource initWithConfiguration:bucket:]
- -[MUISearchInstantAnswersSuggestion initWithMessage:instantAnswer:]
- -[MessageListDataSource mailRankingSignalsForMessageListItemsInSection:]
- -[MessageListDataSource mailRankingSignalsForMessageListItemsInSection:].cold.1
- -[MessageListSectionDataSource collection:sendMailRankingSignals:]
- -[MessageListSectionDataSource mailRankingSignalsByGlobalMessageID]
- -[MessageListSectionDataSource setMailRankingSignalsByGlobalMessageID:]
- GCC_except_table162
- GCC_except_table174
- GCC_except_table27
- GCC_except_table44
- GCC_except_table56
- GCC_except_table74
- GCC_except_table87
- _EMUserDefaultDisableCategorizationOnboardingPrimaryV1
- _OBJC_IVAR_$_MessageListSectionDataSource._mailRankingSignalsByGlobalMessageID
- ___115-[MessageListSectionDataSource _addedItemIDs:before:existingItemID:toThreadWithItemID:inCollection:isLastObserver:]_block_invoke.149
- ___115-[MessageListSectionDataSource _addedItemIDs:before:existingItemID:toThreadWithItemID:inCollection:isLastObserver:]_block_invoke_2.150
- ___117-[MessageListSectionDataSource _deleteItemsWithIDs:fromCollection:animated:useImmediateCompletion:completionHandler:]_block_invoke.155
- ___117-[MessageListSectionDataSource _deleteItemsWithIDs:fromCollection:animated:useImmediateCompletion:completionHandler:]_block_invoke_2.159
- ___123-[MessageListSectionDataSource collection:changedItemIDs:itemIDsWithCountChanges:itemIDsWithBrandIndicatorLocationChanges:]_block_invoke.112
- ___62-[MessageListSectionDataSource _maybeReloadForTimedOutItemIDs]_block_invoke.133
- ___62-[MessageListSectionDataSource collection:movedItemIDs:after:]_block_invoke.108
- ___63-[MessageListSectionDataSource collection:movedItemIDs:before:]_block_invoke.103
- ___63-[MessageListSectionDataSource collectionDidFinishInitialLoad:]_block_invoke.120
- ___63-[MessageListSectionDataSource didFinishRecoveryForCollection:]_block_invoke.115
- ___80-[MessageListSectionDataSource collection:replacedExistingItemID:withNewItemID:]_block_invoke.114
- ___80-[MessageListSectionDataSource collection:replacedExistingItemID:withNewItemID:]_block_invoke.114.cold.1
- ___83-[MessageListSectionDataSource collection:didFinishInitialLoadForThreadWithItemID:]_block_invoke.119
- ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.83
- ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.85
- ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.85.cold.1
- ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.86
- ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.164
- ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.164.cold.1
- ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.168
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e41_v24?0"<EMMessageListItem>"8"NSError"16ls72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs_e29_v16?0"<EMMessageListItem>"8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.122
- ___block_literal_global.125
- ___block_literal_global.236
- _associated conformance 6MailUI16BucketTipInfoKeyOSHAASQ
- _block_copy_helper.368
- _block_copy_helper.54
- _block_descriptor.370
- _block_descriptor.56
- _block_destroy_helper.369
- _block_destroy_helper.55
- _get_witness_table 10Foundation19AttributedStringKeyRzlAA15AttributeScopesO5UIKitE0G10AttributesV04FontE0OAaBHPyHC.26
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA6HStackVyACyAA5ImageVAA12_FrameLayoutVGGAIGAA08_PaddingH0VGANGAA4ViewHPAoaQHPAlaQHPAkaQHPyHC_AiA0J8ModifierHPyHCHC_AnaRHPyHCHC_AnaRHPyHCHC.3
- _objc_msgSend$configureForBucket:
- _objc_msgSend$initWithConfiguration:bucket:
- _objc_msgSend$learnMoreButton
- _objc_msgSend$mailRankingSignalsByGlobalMessageID
- _objc_msgSend$setMailRankingSignalsByGlobalMessageID:
- _objc_msgSend$turnOffButton
- _symbolic SDy__________G 6MailUI16BucketTipInfoKeyO AA08CategorydE0V
- _symbolic _____ 6MailUI15CategoryTipInfoV
- _symbolic _____ 6MailUI16BucketTipInfoKeyO
- _symbolic _____ 6MailUI25OnboardingTipLayoutValuesO
- _symbolic _____SgXw 6MailUI42MessageListOnboardingTipCollectionViewCellC
- _symbolic _____SgXwz_Xx 6MailUI42MessageListOnboardingTipCollectionViewCellC
- _symbolic ___________t 6MailUI16BucketTipInfoKeyO AA08CategorydE0V
- _symbolic _____yAAyAAy_____yAAy__________GGADG_____GAHG 7SwiftUI15ModifiedContentV AA6HStackV AA5ImageV AA12_FrameLayoutV AA08_PaddingH0V
- _symbolic _____yAAy_____yAAy__________GGADG_____G 7SwiftUI15ModifiedContentV AA6HStackV AA5ImageV AA12_FrameLayoutV AA08_PaddingH0V
- _symbolic _____y__________G 7SwiftUI15ModifiedContentV AA5ImageV AA12_FrameLayoutV
- _symbolic _____y_____yAAy__________GGADG 7SwiftUI15ModifiedContentV AA6HStackV AA5ImageV AA12_FrameLayoutV
- _symbolic _____y_____y__________GG 7SwiftUI6HStackV AA15ModifiedContentV AA5ImageV AA12_FrameLayoutV
- _type_layout_string 6MailUI15CategoryTipInfoV
CStrings:
+ " in other categories."
+ " unread Messages in Primary and "
+ " unread Messages in Primary."
+ " unread Messages in other categories."
+ "$__lazy_storage_$_cancelButton"
+ "$__lazy_storage_$_customizeButton"
+ "$__lazy_storage_$_okButton"
+ "$__lazy_storage_$_primarySeparator"
+ "$__lazy_storage_$_secondarySeparator"
+ "$__lazy_storage_$_turnOffCategoriesButton"
+ "%p: [%u] Setting data source: %{public}@ for section: %{public}@ (remaining pending sections: %{public}@)"
+ "/AppleInternal/Library/BuildRoots/4~B5UsugDDpEaOGn581OBoYNkuWN7D2bBryPipJVw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/System/Library/PrivateFrameworks/Email.framework/Headers/EMContentRequestOptions.h"
+ "<%@: %p> section: %@, messageList: %p"
+ "@\"MUICategoryMailboxCount\""
+ "@\"MUICategoryMailboxCountHelper\""
+ "Customize"
+ "Failed to get category counts for primaryOnly: %{BOOL}d, error: %{public}@"
+ "MUICategoryMailboxCount"
+ "MUICategoryMailboxCountHelper"
+ "MUICategoryMailboxCountHelper-%d"
+ "MailUI/MUIOnboardingTip.swift"
+ "Only unread messages Categorized as Primary will appear on the Mail icon."
+ "S"
+ "Sa"
+ "T@\"EFLocked\",&,N,V_pendingSectionDataSources"
+ "T@\"MUICategoryMailboxCount\",&,N,V_count"
+ "T@\"MUICategoryMailboxCountHelper\",&,N,V_helper"
+ "T@\"NSArray\",&,N,V_mailboxes"
+ "Title that appears at the top of the box of highlighted messages in the message list"
+ "Tq,N,V_fullCount"
+ "Tq,N,V_primaryCount"
+ "Unread Message Count"
+ "You have "
+ "_count"
+ "_fetchCountForPrimaryOnly:completion:"
+ "_fullCount"
+ "_helper"
+ "_pendingSectionDataSources"
+ "_primaryCount"
+ "configureForBucket:primaryUnreadCount:otherUnreadCount:"
+ "customizeButton"
+ "fullCount"
+ "helper"
+ "initWithConfiguration:bucket:countHelper:"
+ "initWithMailboxes:messageRepository:"
+ "initWithMessage:instantAnswer:messageList:"
+ "messageCount"
+ "okButton"
+ "p:%ld,f:%ld"
+ "pendingSectionDataSources"
+ "performCountQuery:completionHandler:"
+ "primaryCount"
+ "setCount:"
+ "setCustomizeButton:"
+ "setFullCount:"
+ "setHelper:"
+ "setOkButton:"
+ "setPendingSectionDataSources:"
+ "setPrimaryCount:"
+ "setTurnOffCategoriesButton:"
+ "turnOffCategoriesButton"
+ "v16@?0@\"MUICategoryMailboxCount\"8"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v40@0:8q16q24q32"
- "$__lazy_storage_$_buttonSeparatorView"
- "$__lazy_storage_$_learnMoreButton"
- "$__lazy_storage_$_separatorView"
- "$__lazy_storage_$_titleTextAttributesTransformer"
- "$__lazy_storage_$_turnOffButton"
- "/AppleInternal/Library/BuildRoots/4~B4WougDGokSyiQXgkXNae50e1pOovw74bXMc9FE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/System/Library/PrivateFrameworks/Email.framework/Headers/EMContentRequestOptions.h"
- "Button for the user to dismiss the categories on-boarding tip by disabling categories."
- "Button for the user to dismiss the categories on-boarding tip by trying out categories."
- "Cancel out of onboarding tip"
- "Label for onboarding tip"
- "Label with description of the All Mail category"
- "Label with description of the Primary category"
- "Label with description of the Promotions category"
- "Label with description of the Transactions category"
- "Label with description of the Updates category"
- "Label with instructions for the configuration menu. The %@ will be replaced by an image of the menu button."
- "Learn More"
- "Manage Badge Count"
- "Only unread messages categorized as Primary will appear on the Mail icon."
- "See what’s new from businesses and organizations you recognize."
- "Sq"
- "T@\"NSDictionary\",C,N,V_mailRankingSignalsByGlobalMessageID"
- "T@\"UIButton\",N,&,VcancelButton"
- "Title that appears at the top of the box of highlighted messages in the message list. All capitalized in English per spec."
- "[Mail Ranking Signals] Fetching the mail ranking signals count:%lu for message list items"
- "[Mail Ranking Signals] [Committed Search] Received mail ranking signals for (%ld) items"
- "_mailRankingSignalsByGlobalMessageID"
- "attributedStringWithImageWithReplacingKeyword:inLocalizedString:imageName:bucketColor:"
- "bucketTipInfo"
- "button for onboarding tip"
- "collection:sendMailRankingSignals:"
- "configureForBucket:"
- "initWithConfiguration:bucket:"
- "initWithMessage:instantAnswer:"
- "learnMoreButton"
- "mailRankingSignalsByGlobalMessageID"
- "mailRankingSignalsForMessageListItemsInSection:"
- "setLearnMoreButton:"
- "setMailRankingSignalsByGlobalMessageID:"
- "setTurnOffButton:"
- "turnOffButton"

```
