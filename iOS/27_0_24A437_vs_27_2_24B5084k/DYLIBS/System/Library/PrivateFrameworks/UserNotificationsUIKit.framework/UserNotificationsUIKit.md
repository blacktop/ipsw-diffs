## UserNotificationsUIKit

> `/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit`

```diff

-1077.0.1.0.0
-  __TEXT.__text: 0x1b2250
-  __TEXT.__objc_methlist: 0x1acdc
+1077.2.3.0.0
+  __TEXT.__text: 0x1b3534
+  __TEXT.__objc_methlist: 0x1ae1c
   __TEXT.__const: 0x43e4
-  __TEXT.__gcc_except_tab: 0x2d38
-  __TEXT.__cstring: 0x9fed
-  __TEXT.__oslogstring: 0x10239
+  __TEXT.__gcc_except_tab: 0x2bf8
+  __TEXT.__cstring: 0xa02d
+  __TEXT.__oslogstring: 0x10359
   __TEXT.__ustring: 0x22
   __TEXT.__constg_swiftt: 0x1bdc
   __TEXT.__swift5_typeref: 0x3ce2

   __TEXT.__swift5_proto: 0x17c
   __TEXT.__swift5_types: 0x128
   __TEXT.__swift5_mpenum: 0x5c
-  __TEXT.__swift5_capture: 0xc44
+  __TEXT.__swift5_capture: 0xd84
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_cont: 0x4c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x8d68
+  __TEXT.__unwind_info: 0x8d70
   __TEXT.__eh_frame: 0xcb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x41d0
-  __DATA_CONST.__objc_classlist: 0x7f8
-  __DATA_CONST.__objc_catlist: 0xb0
-  __DATA_CONST.__objc_protolist: 0x608
+  __DATA_CONST.__const: 0x41a8
+  __DATA_CONST.__objc_classlist: 0x800
+  __DATA_CONST.__objc_catlist: 0xb8
+  __DATA_CONST.__objc_protolist: 0x5f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcbb8
+  __DATA_CONST.__objc_selrefs: 0xcc60
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x568
+  __DATA_CONST.__objc_superrefs: 0x570
   __DATA_CONST.__objc_arraydata: 0x158
-  __DATA_CONST.__got: 0x1860
-  __AUTH_CONST.__const: 0x4e28
-  __AUTH_CONST.__cfstring: 0x7f20
-  __AUTH_CONST.__objc_const: 0x269d8
+  __DATA_CONST.__got: 0x1858
+  __AUTH_CONST.__const: 0x50f8
+  __AUTH_CONST.__cfstring: 0x7f40
+  __AUTH_CONST.__objc_const: 0x26bb8
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x1530
-  __AUTH.__objc_data: 0x2490
+  __AUTH_CONST.__auth_got: 0x1558
+  __AUTH.__objc_data: 0x24e0
   __AUTH.__data: 0x3d8
-  __DATA.__objc_ivar: 0x1798
-  __DATA.__data: 0x51b0
+  __DATA.__objc_ivar: 0x17c0
+  __DATA.__data: 0x5100
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x3a10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10922
-  Symbols:   19871
-  CStrings:  2169
+  Functions: 10983
+  Symbols:   19934
+  CStrings:  2174
 
Symbols:
+ -[NCActionMenuButton .cxx_destruct]
+ -[NCActionMenuButton _contextMenuInteraction:shouldPresentWithCompletion:]
+ -[NCActionMenuButton contextMenuInteraction:configurationForMenuAtLocation:]
+ -[NCActionMenuButton contextMenuInteraction:willDisplayMenuForConfiguration:animator:]
+ -[NCActionMenuButton contextMenuInteraction:willEndForConfiguration:animator:]
+ -[NCActionMenuButton menuDescriptor]
+ -[NCActionMenuButton setMenuDescriptor:]
+ -[NCActionMenuDescriptor .cxx_destruct]
+ -[NCActionMenuDescriptor contextMenuConfiguration]
+ -[NCActionMenuDescriptor contextMenuInteraction:shouldPresentWithCompletion:]
+ -[NCActionMenuDescriptor contextMenuInteraction:willDisplayMenuForConfiguration:]
+ -[NCActionMenuDescriptor contextMenuInteraction:willEndForConfiguration:]
+ -[NCActionMenuDescriptor initWithContextMenuConfiguration:shouldPresentBlock:willDisplayMenuInteractionBlock:willEndMenuInteractionBlock:]
+ -[NCActionMenuDescriptor setShouldPresentBlock:]
+ -[NCActionMenuDescriptor setWillDisplayInteractionBlock:]
+ -[NCActionMenuDescriptor setWillEndInteractionBlock:]
+ -[NCActionMenuDescriptor shouldPresentBlock]
+ -[NCActionMenuDescriptor willDisplayInteractionBlock]
+ -[NCActionMenuDescriptor willEndInteractionBlock]
+ -[NCNotificationAppSectionList appSectionListHeaderViewOptionsMenuDescriptor:]
+ -[NCNotificationGroupList _configurePromotedLeadingNotificationRequest:]
+ -[NCNotificationGroupList _shouldPresentOptionsMenuForRequest:completion:]
+ -[NCNotificationGroupList cellPendingMenuDisplay]
+ -[NCNotificationGroupList setCellPendingMenuDisplay:]
+ -[NCNotificationListTouchEaterManager installTouchGestureRecognizerForView:]
+ -[NCNotificationOptionsMenuBuilder .cxx_destruct]
+ -[NCNotificationOptionsMenuBuilder _addToContactsAction]
+ -[NCNotificationOptionsMenuBuilder _canAddToContacts]
+ -[NCNotificationOptionsMenuBuilder _clearSectionAction]
+ -[NCNotificationOptionsMenuBuilder _criticalOffAction]
+ -[NCNotificationOptionsMenuBuilder _criticalOnAction]
+ -[NCNotificationOptionsMenuBuilder _customSettingsActionForSectionSettings:]
+ -[NCNotificationOptionsMenuBuilder _deliverImmediatelyAcion]
+ -[NCNotificationOptionsMenuBuilder _didApplicationBreakthroughMode:]
+ -[NCNotificationOptionsMenuBuilder _didBreakthroughMode:]
+ -[NCNotificationOptionsMenuBuilder _didContactBreakthroughMode:]
+ -[NCNotificationOptionsMenuBuilder _isApplicationAllowedForMode:]
+ -[NCNotificationOptionsMenuBuilder _isCommunicationThread]
+ -[NCNotificationOptionsMenuBuilder _isContactAllowedForMode:]
+ -[NCNotificationOptionsMenuBuilder _muteForOneHourAction]
+ -[NCNotificationOptionsMenuBuilder _muteForTodayAction]
+ -[NCNotificationOptionsMenuBuilder _offActionForApplicationForMode:]
+ -[NCNotificationOptionsMenuBuilder _offActionForContactForMode:]
+ -[NCNotificationOptionsMenuBuilder _offActionWithSectionDisplayName:]
+ -[NCNotificationOptionsMenuBuilder _onActionWithSectionDisplayName:]
+ -[NCNotificationOptionsMenuBuilder _priorityFeedbackFileRadarWithFeedbackManager:]
+ -[NCNotificationOptionsMenuBuilder _priorityFeedbackNegativeWithFeedbackManager:]
+ -[NCNotificationOptionsMenuBuilder _priorityFeedbackPositiveWithFeedbackManager:]
+ -[NCNotificationOptionsMenuBuilder _sectionIdentifier]
+ -[NCNotificationOptionsMenuBuilder _sendToDigestAction]
+ -[NCNotificationOptionsMenuBuilder _sender]
+ -[NCNotificationOptionsMenuBuilder _settingsActionForSectionSettings:]
+ -[NCNotificationOptionsMenuBuilder _stopPrioritizingActionForRequest:displayName:]
+ -[NCNotificationOptionsMenuBuilder _stopSummarizingActionForRequest:displayName:]
+ -[NCNotificationOptionsMenuBuilder _summaryFeedbackNegativeWithFeedbackManager:]
+ -[NCNotificationOptionsMenuBuilder _summaryFeedbackPositiveWithFeedbackManager:]
+ -[NCNotificationOptionsMenuBuilder _summaryFeedbackReportConcernWithFeedbackManager:]
+ -[NCNotificationOptionsMenuBuilder _threadIdentifierOrNil]
+ -[NCNotificationOptionsMenuBuilder _threadName]
+ -[NCNotificationOptionsMenuBuilder _timeSensitiveOffAction]
+ -[NCNotificationOptionsMenuBuilder _timeSensitiveOnAction]
+ -[NCNotificationOptionsMenuBuilder _unmuteActionForMuteAssertionLevel:]
+ -[NCNotificationOptionsMenuBuilder areOptionsForSection]
+ -[NCNotificationOptionsMenuBuilder initWithNotificationRequest:settingsDelegate:optionsForSection:]
+ -[NCNotificationOptionsMenuBuilder menuConfiguration]
+ -[NCNotificationOptionsMenuBuilder request]
+ -[NCNotificationOptionsMenuBuilder setOptionsForSection:]
+ -[NCNotificationOptionsMenuBuilder setRequest:]
+ -[NCNotificationOptionsMenuBuilder setSettingsDelegate:]
+ -[NCNotificationOptionsMenuBuilder settingsDelegate]
+ -[NCNotificationRootList _scheduleVisibleContentExtentUpdateIfNeeded]
+ -[NCNotificationRootList countIndicatorBottomInset]
+ -[NCNotificationRootList hasAbandonedVisibleContentExtentUpdates]
+ -[NCNotificationRootList hasScheduledVisibleContentExtentUpdate]
+ -[NCNotificationRootList setCountIndicatorBottomInset:]
+ -[NCNotificationRootList setHasAbandonedVisibleContentExtentUpdates:]
+ -[NCNotificationRootList setHasScheduledVisibleContentExtentUpdate:]
+ -[NCNotificationRootList setVisibleContentExtentRepostWindowStart:]
+ -[NCNotificationRootList setVisibleContentExtentRepostsInWindow:]
+ -[NCNotificationRootList visibleContentExtentRepostWindowStart]
+ -[NCNotificationRootList visibleContentExtentRepostsInWindow]
+ -[NCNotificationStructuredListViewController _setupTouchEaterManagerIfNeeded]
+ -[NCNotificationStructuredListViewController isRequestingAuthenticationForOptionsMenu]
+ -[NCNotificationStructuredListViewController lastPresentedOptionsMenuInteraction]
+ -[NCNotificationStructuredListViewController notificationListComponent:optionsMenuConfigurationForNotificationRequest:optionsForSection:]
+ -[NCNotificationStructuredListViewController notificationListComponent:shouldPresentOptionsMenuForNotificationRequest:completion:]
+ -[NCNotificationStructuredListViewController notificationListComponent:willDismissOptionsMenuInteraction:forNotificationRequest:optionsForSection:listCell:]
+ -[NCNotificationStructuredListViewController notificationListComponent:willDisplayOptionsMenuInteraction:forNotificationRequest:optionsForSection:listCell:]
+ -[NCNotificationStructuredListViewController setLastPresentedOptionsMenuInteraction:]
+ -[NCNotificationStructuredListViewController setRequestingAuthenticationForOptionsMenu:]
+ -[NCPlatterActionButton _contextMenuInteraction:shouldPresentWithCompletion:]
+ -[NCPlatterActionButton contextMenuInteraction:configurationForMenuAtLocation:]
+ -[NCPlatterActionButton contextMenuInteraction:willDisplayMenuForConfiguration:animator:]
+ -[NCPlatterActionButton contextMenuInteraction:willEndForConfiguration:animator:]
+ -[NCPlatterActionButton menuDescriptor]
+ -[NCPlatterActionButton setMenuDescriptor:]
+ -[NCSwipeInteraction _layoutActionButtonsForVisibleWidth:]
+ -[NCSwipeInteraction forceLayoutActionButtons]
+ -[UIAction(UserNotificationsUIKit) _nc_menuDescriptor]
+ -[UIAction(UserNotificationsUIKit) _nc_setMenuDescriptor:]
+ GCC_except_table111
+ GCC_except_table152
+ GCC_except_table154
+ GCC_except_table159
+ GCC_except_table166
+ GCC_except_table188
+ GCC_except_table190
+ GCC_except_table205
+ GCC_except_table210
+ GCC_except_table302
+ GCC_except_table37
+ GCC_except_table53
+ _BSRectRoundForScale
+ _NCPlatterActionButtonsAlwaysMorphMenus.alwaysMorphMenus
+ _NCPlatterActionButtonsAlwaysMorphMenus.onceToken
+ _OBJC_CLASS_$_NCActionMenuButton
+ _OBJC_CLASS_$_NCActionMenuDescriptor
+ _OBJC_CLASS_$_NCNotificationOptionsMenuBuilder
+ _OBJC_IVAR_$_NCActionMenuButton._menuDescriptor
+ _OBJC_IVAR_$_NCActionMenuDescriptor._contextMenuConfiguration
+ _OBJC_IVAR_$_NCActionMenuDescriptor._shouldPresentBlock
+ _OBJC_IVAR_$_NCActionMenuDescriptor._willDisplayInteractionBlock
+ _OBJC_IVAR_$_NCActionMenuDescriptor._willEndInteractionBlock
+ _OBJC_IVAR_$_NCNotificationGroupList._cellPendingMenuDisplay
+ _OBJC_IVAR_$_NCNotificationOptionsMenuBuilder._optionsForSection
+ _OBJC_IVAR_$_NCNotificationOptionsMenuBuilder._request
+ _OBJC_IVAR_$_NCNotificationOptionsMenuBuilder._settingsDelegate
+ _OBJC_IVAR_$_NCNotificationRootList._countIndicatorBottomInset
+ _OBJC_IVAR_$_NCNotificationRootList._hasAbandonedVisibleContentExtentUpdates
+ _OBJC_IVAR_$_NCNotificationRootList._hasScheduledVisibleContentExtentUpdate
+ _OBJC_IVAR_$_NCNotificationRootList._visibleContentExtentRepostWindowStart
+ _OBJC_IVAR_$_NCNotificationRootList._visibleContentExtentRepostsInWindow
+ _OBJC_IVAR_$_NCNotificationStructuredListViewController._lastPresentedOptionsMenuInteraction
+ _OBJC_IVAR_$_NCNotificationStructuredListViewController._requestingAuthenticationForOptionsMenu
+ _OBJC_IVAR_$_NCPlatterActionButton._menuDescriptor
+ _OBJC_METACLASS_$_NCActionMenuButton
+ _OBJC_METACLASS_$_NCActionMenuDescriptor
+ _OBJC_METACLASS_$_NCNotificationOptionsMenuBuilder
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UIAction_$_UserNotificationsUIKit
+ __OBJC_$_CATEGORY_UIAction_$_UserNotificationsUIKit
+ __OBJC_$_INSTANCE_METHODS_NCActionMenuButton
+ __OBJC_$_INSTANCE_METHODS_NCActionMenuDescriptor
+ __OBJC_$_INSTANCE_METHODS_NCNotificationOptionsMenuBuilder
+ __OBJC_$_INSTANCE_VARIABLES_NCActionMenuButton
+ __OBJC_$_INSTANCE_VARIABLES_NCActionMenuDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_NCNotificationOptionsMenuBuilder
+ __OBJC_$_PROP_LIST_NCActionMenuButton
+ __OBJC_$_PROP_LIST_NCActionMenuDescriptor
+ __OBJC_$_PROP_LIST_NCNotificationOptionsMenuBuilder
+ __OBJC_$_PROP_LIST_UIAction_$_UserNotificationsUIKit
+ __OBJC_CLASS_RO_$_NCActionMenuButton
+ __OBJC_CLASS_RO_$_NCActionMenuDescriptor
+ __OBJC_CLASS_RO_$_NCNotificationOptionsMenuBuilder
+ __OBJC_METACLASS_RO_$_NCActionMenuButton
+ __OBJC_METACLASS_RO_$_NCActionMenuDescriptor
+ __OBJC_METACLASS_RO_$_NCNotificationOptionsMenuBuilder
+ ___130-[NCNotificationStructuredListViewController notificationListComponent:shouldPresentOptionsMenuForNotificationRequest:completion:]_block_invoke
+ ___52-[NCNotificationGroupList _optionsActionForRequest:]_block_invoke_2
+ ___52-[NCNotificationGroupList _optionsActionForRequest:]_block_invoke_3
+ ___52-[NCNotificationGroupList _optionsActionForRequest:]_block_invoke_4
+ ___53-[NCNotificationOptionsMenuBuilder _criticalOnAction]_block_invoke
+ ___53-[NCNotificationOptionsMenuBuilder menuConfiguration]_block_invoke
+ ___54-[NCNotificationOptionsMenuBuilder _criticalOffAction]_block_invoke
+ ___55-[NCNotificationOptionsMenuBuilder _clearSectionAction]_block_invoke
+ ___55-[NCNotificationOptionsMenuBuilder _muteForTodayAction]_block_invoke
+ ___55-[NCNotificationOptionsMenuBuilder _sendToDigestAction]_block_invoke
+ ___56-[NCNotificationOptionsMenuBuilder _addToContactsAction]_block_invoke
+ ___57-[NCNotificationOptionsMenuBuilder _muteForOneHourAction]_block_invoke
+ ___58-[NCNotificationOptionsMenuBuilder _timeSensitiveOnAction]_block_invoke
+ ___59-[NCNotificationOptionsMenuBuilder _timeSensitiveOffAction]_block_invoke
+ ___60-[NCNotificationOptionsMenuBuilder _deliverImmediatelyAcion]_block_invoke
+ ___64-[NCNotificationOptionsMenuBuilder _offActionForContactForMode:]_block_invoke
+ ___68-[NCNotificationOptionsMenuBuilder _offActionForApplicationForMode:]_block_invoke
+ ___68-[NCNotificationOptionsMenuBuilder _onActionWithSectionDisplayName:]_block_invoke
+ ___69-[NCNotificationOptionsMenuBuilder _offActionWithSectionDisplayName:]_block_invoke
+ ___69-[NCNotificationRootList _scheduleVisibleContentExtentUpdateIfNeeded]_block_invoke
+ ___70-[NCNotificationOptionsMenuBuilder _settingsActionForSectionSettings:]_block_invoke
+ ___70-[NCNotificationOptionsMenuBuilder _settingsActionForSectionSettings:]_block_invoke_2
+ ___71-[NCNotificationOptionsMenuBuilder _unmuteActionForMuteAssertionLevel:]_block_invoke
+ ___74-[NCNotificationGroupList _shouldPresentOptionsMenuForRequest:completion:]_block_invoke
+ ___74-[NCNotificationGroupList _shouldPresentOptionsMenuForRequest:completion:]_block_invoke_2
+ ___76-[NCNotificationOptionsMenuBuilder _customSettingsActionForSectionSettings:]_block_invoke
+ ___76-[NCNotificationOptionsMenuBuilder _customSettingsActionForSectionSettings:]_block_invoke_2
+ ___78-[NCNotificationAppSectionList appSectionListHeaderViewOptionsMenuDescriptor:]_block_invoke
+ ___78-[NCNotificationAppSectionList appSectionListHeaderViewOptionsMenuDescriptor:]_block_invoke_2
+ ___78-[NCNotificationAppSectionList appSectionListHeaderViewOptionsMenuDescriptor:]_block_invoke_3
+ ___80-[NCNotificationOptionsMenuBuilder _summaryFeedbackNegativeWithFeedbackManager:]_block_invoke
+ ___80-[NCNotificationOptionsMenuBuilder _summaryFeedbackPositiveWithFeedbackManager:]_block_invoke
+ ___81-[NCNotificationOptionsMenuBuilder _priorityFeedbackNegativeWithFeedbackManager:]_block_invoke
+ ___81-[NCNotificationOptionsMenuBuilder _priorityFeedbackPositiveWithFeedbackManager:]_block_invoke
+ ___81-[NCNotificationOptionsMenuBuilder _stopSummarizingActionForRequest:displayName:]_block_invoke
+ ___82-[NCNotificationOptionsMenuBuilder _priorityFeedbackFileRadarWithFeedbackManager:]_block_invoke
+ ___82-[NCNotificationOptionsMenuBuilder _stopPrioritizingActionForRequest:displayName:]_block_invoke
+ ___85-[NCNotificationOptionsMenuBuilder _summaryFeedbackReportConcernWithFeedbackManager:]_block_invoke
+ ___block_descriptor_32_e18_v16?0"UIAction"8l
+ ___block_descriptor_48_e8_32bs40w_e8_v12?0B8ls32l8w40l8
+ ___block_descriptor_48_e8_32s40w_e44_v24?0"UIContextMenuInteraction"8?<v?B>16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e65_v24?0"UIContextMenuInteraction"8"UIContextMenuConfiguration"16lw40l8s32l8
+ ___block_descriptor_49_e8_32s40r_e45_v16?0"NCNotificationStructuredSectionList"8lr40l8s32l8
+ ___block_descriptor_49_e8_32s40r_e49_v24?0"NCNotificationStructuredSectionList"8^B16lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e8_v12?0B8lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e38_v32?0"NCNotificationRequest"8Q16^B24ls32l8s40l8s48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e40_v32?0"NCNotificationGroupList"8Q16^B24ls32l8s40l8s48l8r64l8s56l8
+ ___swift_closure_destructor.118Tm
+ ___swift_closure_destructor.171Tm
+ _objc_msgSend$_configurePromotedLeadingNotificationRequest:
+ _objc_msgSend$_layoutActionButtonsForVisibleWidth:
+ _objc_msgSend$_nc_menuDescriptor
+ _objc_msgSend$_nc_setMenuDescriptor:
+ _objc_msgSend$_scheduleVisibleContentExtentUpdateIfNeeded
+ _objc_msgSend$_setupTouchEaterManagerIfNeeded
+ _objc_msgSend$_shouldPresentOptionsMenuForRequest:completion:
+ _objc_msgSend$appSectionListHeaderViewOptionsMenuDescriptor:
+ _objc_msgSend$contextMenuConfiguration
+ _objc_msgSend$contextMenuInteraction:shouldPresentWithCompletion:
+ _objc_msgSend$contextMenuInteraction:willDisplayMenuForConfiguration:
+ _objc_msgSend$contextMenuInteraction:willEndForConfiguration:
+ _objc_msgSend$countIndicatorBottomInset
+ _objc_msgSend$forceLayoutActionButtons
+ _objc_msgSend$hasAbandonedVisibleContentExtentUpdates
+ _objc_msgSend$hasScheduledVisibleContentExtentUpdate
+ _objc_msgSend$initWithContextMenuConfiguration:shouldPresentBlock:willDisplayMenuInteractionBlock:willEndMenuInteractionBlock:
+ _objc_msgSend$initWithNotificationRequest:settingsDelegate:optionsForSection:
+ _objc_msgSend$installTouchGestureRecognizerForView:
+ _objc_msgSend$lastPresentedOptionsMenuInteraction
+ _objc_msgSend$menuConfiguration
+ _objc_msgSend$notificationListComponent:optionsMenuConfigurationForNotificationRequest:optionsForSection:
+ _objc_msgSend$notificationListComponent:shouldPresentOptionsMenuForNotificationRequest:completion:
+ _objc_msgSend$notificationListComponent:willDismissOptionsMenuInteraction:forNotificationRequest:optionsForSection:listCell:
+ _objc_msgSend$notificationListComponent:willDisplayOptionsMenuInteraction:forNotificationRequest:optionsForSection:listCell:
+ _objc_msgSend$setContextMenuInteractionEnabled:
+ _objc_msgSend$setHasAbandonedVisibleContentExtentUpdates:
+ _objc_msgSend$setHasScheduledVisibleContentExtentUpdate:
+ _objc_msgSend$setMenuDescriptor:
+ _objc_msgSend$setShowsMenuFromSource:
+ _objc_msgSend$setVisibleContentExtentRepostWindowStart:
+ _objc_msgSend$setVisibleContentExtentRepostsInWindow:
+ _objc_msgSend$visibleContentExtentRepostWindowStart
+ _objc_msgSend$visibleContentExtentRepostsInWindow
- -[NCNotificationAppSectionList appSectionListHeaderView:didRequestPresentingOptionsMenuFromView:]
- -[NCNotificationAppSectionListHeaderOptionsButton visiblePathForPreview]
- -[NCNotificationAppSectionListHeaderView didTapOptionsButton:]
- -[NCNotificationGroupList _executeOptionsActionForRequest:action:]
- -[NCNotificationListTouchEaterManager initForView:]
- -[NCNotificationOptionsMenu .cxx_destruct]
- -[NCNotificationOptionsMenu _addToContactsAction]
- -[NCNotificationOptionsMenu _canAddToContacts]
- -[NCNotificationOptionsMenu _clearSectionAction]
- -[NCNotificationOptionsMenu _contextMenuInteraction:styleForMenuWithConfiguration:]
- -[NCNotificationOptionsMenu _criticalOffAction]
- -[NCNotificationOptionsMenu _criticalOnAction]
- -[NCNotificationOptionsMenu _customSettingsActionForSectionSettings:]
- -[NCNotificationOptionsMenu _deliverImmediatelyAcion]
- -[NCNotificationOptionsMenu _didApplicationBreakthroughMode:]
- -[NCNotificationOptionsMenu _didBreakthroughMode:]
- -[NCNotificationOptionsMenu _didContactBreakthroughMode:]
- -[NCNotificationOptionsMenu _isApplicationAllowedForMode:]
- -[NCNotificationOptionsMenu _isCommunicationThread]
- -[NCNotificationOptionsMenu _isContactAllowedForMode:]
- -[NCNotificationOptionsMenu _muteForOneHourAction]
- -[NCNotificationOptionsMenu _muteForTodayAction]
- -[NCNotificationOptionsMenu _offActionForApplicationForMode:]
- -[NCNotificationOptionsMenu _offActionForContactForMode:]
- -[NCNotificationOptionsMenu _offActionWithSectionDisplayName:]
- -[NCNotificationOptionsMenu _onActionWithSectionDisplayName:]
- -[NCNotificationOptionsMenu _priorityFeedbackFileRadarWithFeedbackManager:]
- -[NCNotificationOptionsMenu _priorityFeedbackNegativeWithFeedbackManager:]
- -[NCNotificationOptionsMenu _priorityFeedbackPositiveWithFeedbackManager:]
- -[NCNotificationOptionsMenu _sectionIdentifier]
- -[NCNotificationOptionsMenu _sendToDigestAction]
- -[NCNotificationOptionsMenu _sender]
- -[NCNotificationOptionsMenu _settingsActionForSectionSettings:]
- -[NCNotificationOptionsMenu _stopPrioritizingActionForRequest:displayName:]
- -[NCNotificationOptionsMenu _stopSummarizingActionForRequest:displayName:]
- -[NCNotificationOptionsMenu _summaryFeedbackNegativeWithFeedbackManager:]
- -[NCNotificationOptionsMenu _summaryFeedbackPositiveWithFeedbackManager:]
- -[NCNotificationOptionsMenu _summaryFeedbackReportConcernWithFeedbackManager:]
- -[NCNotificationOptionsMenu _threadIdentifierOrNil]
- -[NCNotificationOptionsMenu _threadName]
- -[NCNotificationOptionsMenu _timeSensitiveOffAction]
- -[NCNotificationOptionsMenu _timeSensitiveOnAction]
- -[NCNotificationOptionsMenu _unmuteActionForMuteAssertionLevel:]
- -[NCNotificationOptionsMenu areOptionsForSection]
- -[NCNotificationOptionsMenu contextMenuInteraction:configurationForMenuAtLocation:]
- -[NCNotificationOptionsMenu contextMenuInteraction:willEndForConfiguration:animator:]
- -[NCNotificationOptionsMenu dismissMenu]
- -[NCNotificationOptionsMenu initWithNotificationRequest:presentingView:settingsDelegate:optionsForSection:shouldMenuOverlapSource:]
- -[NCNotificationOptionsMenu menu]
- -[NCNotificationOptionsMenu presentMenu]
- -[NCNotificationOptionsMenu presentingView]
- -[NCNotificationOptionsMenu request]
- -[NCNotificationOptionsMenu setMenu:]
- -[NCNotificationOptionsMenu setOptionsForSection:]
- -[NCNotificationOptionsMenu setPresentingView:]
- -[NCNotificationOptionsMenu setRequest:]
- -[NCNotificationOptionsMenu setSettingsDelegate:]
- -[NCNotificationOptionsMenu setShouldMenuOverlapSource:]
- -[NCNotificationOptionsMenu settingsDelegate]
- -[NCNotificationOptionsMenu shouldMenuOverlapSource]
- -[NCNotificationStructuredListViewController _presentOptionsMenuForNotificationRequest:withPresentingView:optionsForSection:shouldMenuOverlapSource:]
- -[NCNotificationStructuredListViewController notificationListComponent:requestsPresentingOptionsMenuForNotificationRequest:presentingViewProvider:optionsForSection:completion:]
- -[NCNotificationStructuredListViewController notificationOptionsMenuWillDismiss:]
- -[NCNotificationStructuredListViewController optionsMenu]
- -[NCNotificationStructuredListViewController setOptionsMenu:]
- GCC_except_table151
- GCC_except_table153
- GCC_except_table155
- GCC_except_table160
- GCC_except_table162
- GCC_except_table186
- GCC_except_table187
- GCC_except_table204
- GCC_except_table209
- GCC_except_table301
- GCC_except_table38
- GCC_except_table40
- GCC_except_table50
- GCC_except_table58
- GCC_except_table77
- _OBJC_CLASS_$_NCNotificationAppSectionListHeaderOptionsButton
- _OBJC_CLASS_$_NCNotificationOptionsMenu
- _OBJC_CLASS_$_UIContextMenuInteraction
- _OBJC_CLASS_$__UIContextMenuStyle
- _OBJC_IVAR_$_NCNotificationOptionsMenu._menu
- _OBJC_IVAR_$_NCNotificationOptionsMenu._optionsForSection
- _OBJC_IVAR_$_NCNotificationOptionsMenu._presentingView
- _OBJC_IVAR_$_NCNotificationOptionsMenu._request
- _OBJC_IVAR_$_NCNotificationOptionsMenu._settingsDelegate
- _OBJC_IVAR_$_NCNotificationOptionsMenu._shouldMenuOverlapSource
- _OBJC_IVAR_$_NCNotificationStructuredListViewController._optionsMenu
- _OBJC_METACLASS_$_NCNotificationAppSectionListHeaderOptionsButton
- _OBJC_METACLASS_$_NCNotificationOptionsMenu
- __MergedGlobals
- __OBJC_$_INSTANCE_METHODS_NCNotificationAppSectionListHeaderOptionsButton
- __OBJC_$_INSTANCE_METHODS_NCNotificationOptionsMenu
- __OBJC_$_INSTANCE_VARIABLES_NCNotificationOptionsMenu
- __OBJC_$_PROP_LIST_NCNotificationAppSectionListHeaderOptionsButton
- __OBJC_$_PROP_LIST_NCNotificationOptionsMenu
- __OBJC_$_PROP_LIST_PLContextMenuPresenter
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PLContextMenuPresenter
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIContextMenuInteractionDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIContextMenuInteractionDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_PLContextMenuPresenter
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIContextMenuInteractionDelegate
- __OBJC_$_PROTOCOL_REFS_PLContextMenuPresenter
- __OBJC_$_PROTOCOL_REFS_UIContextMenuInteractionDelegate
- __OBJC_CLASS_PROTOCOLS_$_NCNotificationAppSectionListHeaderOptionsButton
- __OBJC_CLASS_PROTOCOLS_$_NCNotificationOptionsMenu
- __OBJC_CLASS_RO_$_NCNotificationAppSectionListHeaderOptionsButton
- __OBJC_CLASS_RO_$_NCNotificationOptionsMenu
- __OBJC_LABEL_PROTOCOL_$_PLContextMenuPresenter
- __OBJC_LABEL_PROTOCOL_$_UIContextMenuInteractionDelegate
- __OBJC_METACLASS_RO_$_NCNotificationAppSectionListHeaderOptionsButton
- __OBJC_METACLASS_RO_$_NCNotificationOptionsMenu
- __OBJC_PROTOCOL_$_PLContextMenuPresenter
- __OBJC_PROTOCOL_$_UIContextMenuInteractionDelegate
- ___176-[NCNotificationStructuredListViewController notificationListComponent:requestsPresentingOptionsMenuForNotificationRequest:presentingViewProvider:optionsForSection:completion:]_block_invoke
- ___176-[NCNotificationStructuredListViewController notificationListComponent:requestsPresentingOptionsMenuForNotificationRequest:presentingViewProvider:optionsForSection:completion:]_block_invoke_2
- ___46-[NCNotificationOptionsMenu _criticalOnAction]_block_invoke
- ___47-[NCNotificationOptionsMenu _criticalOffAction]_block_invoke
- ___48-[NCNotificationOptionsMenu _clearSectionAction]_block_invoke
- ___48-[NCNotificationOptionsMenu _muteForTodayAction]_block_invoke
- ___48-[NCNotificationOptionsMenu _sendToDigestAction]_block_invoke
- ___49-[NCNotificationOptionsMenu _addToContactsAction]_block_invoke
- ___50-[NCNotificationOptionsMenu _muteForOneHourAction]_block_invoke
- ___51-[NCNotificationOptionsMenu _timeSensitiveOnAction]_block_invoke
- ___52-[NCNotificationOptionsMenu _timeSensitiveOffAction]_block_invoke
- ___53-[NCNotificationOptionsMenu _deliverImmediatelyAcion]_block_invoke
- ___57-[NCNotificationOptionsMenu _offActionForContactForMode:]_block_invoke
- ___59-[NCNotificationRootList notificationListDidLayoutSubviews]_block_invoke_3
- ___61-[NCNotificationOptionsMenu _offActionForApplicationForMode:]_block_invoke
- ___61-[NCNotificationOptionsMenu _onActionWithSectionDisplayName:]_block_invoke
- ___62-[NCNotificationOptionsMenu _offActionWithSectionDisplayName:]_block_invoke
- ___63-[NCNotificationOptionsMenu _settingsActionForSectionSettings:]_block_invoke
- ___63-[NCNotificationOptionsMenu _settingsActionForSectionSettings:]_block_invoke_2
- ___64-[NCNotificationOptionsMenu _unmuteActionForMuteAssertionLevel:]_block_invoke
- ___66-[NCNotificationGroupList _executeOptionsActionForRequest:action:]_block_invoke
- ___66-[NCNotificationGroupList _executeOptionsActionForRequest:action:]_block_invoke_2
- ___69-[NCNotificationOptionsMenu _customSettingsActionForSectionSettings:]_block_invoke
- ___69-[NCNotificationOptionsMenu _customSettingsActionForSectionSettings:]_block_invoke_2
- ___73-[NCNotificationOptionsMenu _summaryFeedbackNegativeWithFeedbackManager:]_block_invoke
- ___73-[NCNotificationOptionsMenu _summaryFeedbackPositiveWithFeedbackManager:]_block_invoke
- ___74-[NCNotificationOptionsMenu _priorityFeedbackNegativeWithFeedbackManager:]_block_invoke
- ___74-[NCNotificationOptionsMenu _priorityFeedbackPositiveWithFeedbackManager:]_block_invoke
- ___74-[NCNotificationOptionsMenu _stopSummarizingActionForRequest:displayName:]_block_invoke
- ___75-[NCNotificationOptionsMenu _priorityFeedbackFileRadarWithFeedbackManager:]_block_invoke
- ___75-[NCNotificationOptionsMenu _stopPrioritizingActionForRequest:displayName:]_block_invoke
- ___78-[NCNotificationOptionsMenu _summaryFeedbackReportConcernWithFeedbackManager:]_block_invoke
- ___83-[NCNotificationOptionsMenu contextMenuInteraction:configurationForMenuAtLocation:]_block_invoke
- ___83-[NCNotificationOptionsMenu contextMenuInteraction:configurationForMenuAtLocation:]_block_invoke_2
- ___97-[NCNotificationAppSectionList appSectionListHeaderView:didRequestPresentingOptionsMenuFromView:]_block_invoke
- ___block_descriptor_32_e23_"UIViewController"8?0l
- ___block_descriptor_40_e8_32s_e49_v16?0?<v?"NCNotificationListCell""UIView"B>8ls32l8
- ___block_descriptor_41_e8_32s_e45_v16?0"NCNotificationStructuredSectionList"8ls32l8
- ___block_descriptor_41_e8_32s_e49_v24?0"NCNotificationStructuredSectionList"8^B16ls32l8
- ___block_descriptor_48_e8_32s40w_e49_v16?0?<v?"NCNotificationListCell""UIView"B>8lw40l8s32l8
- ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_49_e8_32s40s_e46_v28?0"NCNotificationListCell"8"UIView"16B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48w_e18_v16?0"UIAction"8lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56s_e40_v32?0"NCNotificationGroupList"8Q16^B24ls32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48bs56bs64w_e8_v12?0B8lw64l8s32l8s48l8s40l8s56l8
- ___swift_closure_destructor.112Tm
- ___swift_closure_destructor.164Tm
- _objc_msgSend$_executeOptionsActionForRequest:action:
- _objc_msgSend$_presentMenuAtLocation:
- _objc_msgSend$_presentOptionsMenuForNotificationRequest:withPresentingView:optionsForSection:shouldMenuOverlapSource:
- _objc_msgSend$actionButtonsBackgroundConfiguration
- _objc_msgSend$appSectionListHeaderView:didRequestPresentingOptionsMenuFromView:
- _objc_msgSend$defaultStyle
- _objc_msgSend$initForView:
- _objc_msgSend$initWithNotificationRequest:presentingView:settingsDelegate:optionsForSection:shouldMenuOverlapSource:
- _objc_msgSend$notificationListComponent:requestsPresentingOptionsMenuForNotificationRequest:presentingViewProvider:optionsForSection:completion:
- _objc_msgSend$notificationOptionsMenuWillDismiss:
- _objc_msgSend$optionsMenu
- _objc_msgSend$presentMenu
- _objc_msgSend$setPreferredLayout:
- _objc_msgSend$setShouldMenuOverlapSourcePreview:
CStrings:
+ "%{public}@ aggregatedVisibleContentExtent %{public}@ -> %{public}@"
+ "%{public}@ asked if should present options menu for notification request %{public}@ for section %{public}@"
+ "%{public}@ skipping content update for section %{public}@, filtering state is unchanged"
+ "%{public}@ visible content extent did not settle: %lu reposts within %.2fs. Latching off at extent %{public}@"
+ "%{public}@ will present options menu for notification request %{public}@ for section %{public}@ [optionsForSection=%{BOOL}d]"
+ "UIAction.UserNotificationsUIKit.menuDescriptor"
+ "lockscreenPriorityNotifications"
+ "v24@?0@\"UIContextMenuInteraction\"8@\"UIContextMenuConfiguration\"16"
+ "v24@?0@\"UIContextMenuInteraction\"8@?<v@?B>16"
+ "\xf0!"
- "%{public}@ requests presenting options menu for notification request %{public}@ for section %{public}@ [optionsForSection=%{BOOL}d]"
- "@\"UIViewController\"8@?0"
- "Notification list detaching from window — beginning re-parent container resize"
- "v16@?0@?<v@?@\"NCNotificationListCell\"@\"UIView\"B>8"
- "v28@?0@\"NCNotificationListCell\"8@\"UIView\"16B24"
```
