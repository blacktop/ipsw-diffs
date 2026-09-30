## CommunicationsSetupUI

> `/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI`

```diff

-1543.400.1.0.0
-  __TEXT.__text: 0x870ac
-  __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__objc_methlist: 0x85fc
-  __TEXT.__cstring: 0xb2d7
-  __TEXT.__const: 0x534
-  __TEXT.__gcc_except_tab: 0x499c
-  __TEXT.__oslogstring: 0x5bf2
+1543.500.101.2.2
+  __TEXT.__text: 0x8f760
+  __TEXT.__auth_stubs: 0x1190
+  __TEXT.__objc_methlist: 0x877c
+  __TEXT.__cstring: 0xb5f7
+  __TEXT.__const: 0x664
+  __TEXT.__gcc_except_tab: 0x436c
+  __TEXT.__oslogstring: 0x5b9a
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__ustring: 0x40
-  __TEXT.__swift5_typeref: 0x304
-  __TEXT.__swift5_reflstr: 0x45
-  __TEXT.__swift5_assocty: 0x30
-  __TEXT.__constg_swiftt: 0x154
-  __TEXT.__swift5_fieldmd: 0xd8
-  __TEXT.__swift5_proto: 0x18
-  __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x2790
-  __TEXT.__objc_classname: 0x108f
-  __TEXT.__objc_methname: 0x152cd
-  __TEXT.__objc_methtype: 0x3a8f
-  __TEXT.__objc_stubs: 0x10480
-  __DATA_CONST.__got: 0xb30
+  __TEXT.__swift5_typeref: 0x342
+  __TEXT.__swift5_reflstr: 0x453
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__constg_swiftt: 0x170
+  __TEXT.__swift5_fieldmd: 0x298
+  __TEXT.__swift5_proto: 0x28
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__unwind_info: 0x2a58
+  __TEXT.__objc_classname: 0x1125
+  __TEXT.__objc_methname: 0x15581
+  __TEXT.__objc_methtype: 0x3aa1
+  __TEXT.__objc_stubs: 0x106c0
+  __DATA_CONST.__got: 0xb38
   __DATA_CONST.__const: 0x1200
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5858
+  __DATA_CONST.__objc_selrefs: 0x58f0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x280
+  __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x8e8
-  __AUTH_CONST.__const: 0x960
-  __AUTH_CONST.__cfstring: 0xae60
-  __AUTH_CONST.__objc_const: 0xd0f8
+  __AUTH_CONST.__auth_got: 0x8d8
+  __AUTH_CONST.__const: 0xdb1
+  __AUTH_CONST.__cfstring: 0xad80
+  __AUTH_CONST.__objc_const: 0xd2b8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1e78
+  __AUTH.__objc_data: 0x1e28
   __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0x568
-  __DATA.__data: 0xe68
-  __DATA.__bss: 0x668
+  __DATA.__data: 0xe80
+  __DATA.__bss: 0x870
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7174B57B-F468-3263-A3E5-D674591D7516
-  Functions: 2891
-  Symbols:   10307
-  CStrings:  7355
+  UUID: DC3341A4-4717-338E-A86E-E0AC5938FC13
+  Functions: 2950
+  Symbols:   10391
+  CStrings:  7394
 
Symbols:
+ +[CKSettingsMessagesController _isSMSDevice]
+ +[CKSettingsMessagesController _mmsSubscriptionsListWithSubscriptionInfo:mmsEmailVisible:]
+ +[CKSettingsMessagesController _shouldShowCheckInLocationHistorySettingsForSearchContext:]
+ +[CKSettingsMessagesController _shouldShowMMS]
+ +[CKSettingsMessagesController areTranscriptBackgroundsEnabled]
+ +[CKSettingsMessagesController currentRegionWantsOnlineSafetyLink]
+ +[CKSettingsMessagesController isCheckInAllowedInRegion]
+ +[CKSettingsMessagesController isConversationListFilteringEnabled]
+ +[CKSettingsMessagesController isFilteringUnknownSenders]
+ +[CKSettingsMessagesController onlineSafetyRegionCodesURLMapping]
+ +[CKSettingsMessagesController shouldShowCharacterCount]
+ +[CKSettingsMessagesController shouldShowCheckInLocationHistorySettings]
+ +[CKSettingsMessagesController shouldShowContactPhotoSettings]
+ +[CKSettingsMessagesController shouldShowConversationBackgroundStartWithPhotosVisible]
+ +[CKSettingsMessagesController shouldShowInboxSummarySettings]
+ +[CKSettingsMessagesController shouldShowJunkConversationsInSearch]
+ +[CKSettingsMessagesController shouldShowJunkConversationsRow]
+ +[CKSettingsMessagesController shouldShowJunkFilteringReceipts]
+ +[CKSettingsMessagesController shouldShowMMSEmailAddress]
+ +[CKSettingsMessagesController shouldShowMMSPane]
+ +[CKSettingsMessagesController shouldShowMMSSwitch]
+ +[CKSettingsMessagesController shouldShowMadridAccounts]
+ +[CKSettingsMessagesController shouldShowMadridSwitch]
+ +[CKSettingsMessagesController shouldShowMessagesForBusiness]
+ +[CKSettingsMessagesController shouldShowNicknames]
+ +[CKSettingsMessagesController shouldShowOnlineSafetyLink]
+ +[CKSettingsMessagesController shouldShowRCSBusinessMessaging]
+ +[CKSettingsMessagesController shouldShowRCSPane]
+ +[CKSettingsMessagesController shouldShowRaiseToListenSwitch]
+ +[CKSettingsMessagesController shouldShowSMSRelaySettings]
+ +[CKSettingsMessagesController shouldShowSatelliteDemoModeButtonInSearch]
+ +[CKSettingsMessagesController shouldShowSatelliteDemoModeButton]
+ +[CKSettingsMessagesController shouldShowSatelliteDemoModeButton].cold.1
+ +[CKSettingsMessagesController shouldShowSatelliteDemoModeButton].cold.2
+ +[CKSettingsMessagesController shouldShowSendAsSMS]
+ -[CKLazuliEnablementManager _canSetRCSEncryptionForSubscription:]
+ -[CKLazuliEnablementManager _isRCSEncryptionEnabledForSubscription:]
+ -[CKLazuliEnablementManager _isRCSEncryptionSupportedForSubscription:]
+ -[CKLazuliEnablementManager _setRCSEncryptionEnabledForSubscription:enabled:]
+ -[CKLazuliEnablementManager _setRCSEncryptionEnabledForSubscription:enabled:].cold.1
+ -[CKLazuliEnablementManager _showRCSEncryptionForSubscription:]
+ -[CKLazuliEnablementManager allSubscriptionsWithRCSSupport]
+ -[CKLazuliEnablementManager canSetRCSEncryption]
+ -[CKLazuliEnablementManager isRCSEncryptionEnabledForAnyActiveSubscription]
+ -[CKLazuliEnablementManager setRCSEncryptionEnabled:specifier:]
+ -[CKLazuliEnablementManager showRCSEncryption]
+ -[CKMMSMultipleCTSubscriptionsController viewDidLoad]
+ -[CKRCSController isRCSEncryptionEnabled:]
+ -[CKRCSController setRCSEncryptionEnabled:specifier:]
+ GCC_except_table146
+ GCC_except_table175
+ GCC_except_table178
+ GCC_except_table235
+ GCC_except_table290
+ GCC_except_table40
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table75
+ _OBJC_CLASS_$_PSSwitchTableCell
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ __OBJC_$_PROP_LIST_CKLazuliEnablementProtocol
+ ___67+[CKSettingsMessagesController shouldShowJunkConversationsInSearch]_block_invoke
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.906
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.907
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.926
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_2.928
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_3.930
+ ___69-[CNFRegSettingsController _setupAccountHandlersForDisabledOperation]_block_invoke.895
+ ___Block_byref_object_copy_.892
+ ___Block_byref_object_dispose_.893
+ ___block_literal_global.398
+ ___block_literal_global.550
+ ___block_literal_global.569
+ ___block_literal_global.623
+ __swiftImmortalRefCount
+ _associated conformance 21CommunicationsSetupUI34MessagesSettingsDynamicDestinationOSHAASQ
+ _associated conformance 21CommunicationsSetupUI34MessagesSettingsDynamicDestinationOs12CaseIterableAA8AllCasessADP_Sl
+ _objc_autorelease
+ _objc_msgSend$_canSetRCSEncryptionForSubscription:
+ _objc_msgSend$_isRCSEncryptionEnabledForSubscription:
+ _objc_msgSend$_isRCSEncryptionSupportedForSubscription:
+ _objc_msgSend$_mmsSubscriptionsListWithSubscriptionInfo:mmsEmailVisible:
+ _objc_msgSend$_setRCSEncryptionEnabledForSubscription:enabled:
+ _objc_msgSend$_shouldShowCheckInLocationHistorySettingsForSearchContext:
+ _objc_msgSend$_shouldShowMMS
+ _objc_msgSend$_showRCSEncryptionForSubscription:
+ _objc_msgSend$allSubscriptionsWithRCSSupport
+ _objc_msgSend$areTranscriptBackgroundsEnabled
+ _objc_msgSend$canSetRCSEncryption
+ _objc_msgSend$carrierSupport
+ _objc_msgSend$connectWithCompletion:
+ _objc_msgSend$controlValue
+ _objc_msgSend$encryptionCapabilities
+ _objc_msgSend$isConversationListFilteringEnabled
+ _objc_msgSend$isFilteringUnknownSenders
+ _objc_msgSend$isMessagesTheDefaultTextApp
+ _objc_msgSend$isRCSEncryptionEnabled
+ _objc_msgSend$isRCSEncryptionEnabledForAnyActiveSubscription
+ _objc_msgSend$isRaiseGestureSupported
+ _objc_msgSend$multiplexedConnectionWithLabel:capabilities:context:
+ _objc_msgSend$secondarySystemGroupedBackgroundColor
+ _objc_msgSend$setLazuliEncryption:enabled:withError:
+ _objc_msgSend$setMessageSummarizationUserPreference:
+ _objc_msgSend$setRCSEncryptionEnabled:specifier:
+ _objc_msgSend$sharedController
+ _objc_msgSend$shouldShowConversationBackgroundStartWithPhotosVisible
+ _objc_msgSend$shouldShowJunkConversationsInSearch
+ _objc_msgSend$shouldShowMMSEmailAddress
+ _objc_msgSend$shouldShowMMSPane
+ _objc_msgSend$shouldShowMMSSwitch
+ _objc_msgSend$shouldShowMessagesForBusiness
+ _objc_msgSend$shouldShowRCSBusinessMessaging
+ _objc_msgSend$shouldShowRCSPane
+ _objc_msgSend$shouldShowSatelliteDemoModeButton
+ _objc_msgSend$showRCSEncryption
+ _objc_msgSend$showSwitch
+ _objc_msgSend$startMonitorIfNeededForReason:
+ _objc_msgSend$waitForSetup
+ _symbolic $sSY
+ _symbolic $ss12CaseIterableP
+ _symbolic SS
+ _symbolic Say_____G 21CommunicationsSetupUI34MessagesSettingsDynamicDestinationO
+ _symbolic _____ 21CommunicationsSetupUI34MessagesSettingsDynamicDestinationO
- -[CKSettingsMessagesController _isMessagesTheDefaultMessagingApp]
- -[CKSettingsMessagesController _isMessagesTheDefaultMessagingApp].cold.1
- -[CKSettingsMessagesController _isRaiseGestureSupported]
- -[CKSettingsMessagesController _isRaiseGestureSupported].cold.1
- -[CKSettingsMessagesController _isSMSDevice]
- -[CKSettingsMessagesController _shouldShowSatelliteDemoModeButton]
- -[CKSettingsMessagesController _shouldShowSatelliteDemoModeButton].cold.1
- -[CKSettingsMessagesController _shouldShowSatelliteDemoModeButton].cold.2
- -[CKSettingsMessagesController currentRegionWantsOnlineSafetyLink]
- -[CKSettingsMessagesController filterUnkownSendersSpecifierIdentifiers]
- -[CKSettingsMessagesController isCheckInAllowedInRegion]
- -[CKSettingsMessagesController isTranscriptBackgroundsEnabledViaSyncedSettings]
- -[CKSettingsMessagesController messagesFilteringSpecifierIdentifiers]
- -[CKSettingsMessagesController onlineSafetyRegionCodesURLMapping]
- -[CKSettingsMessagesController sharedWithYouSettingsSpecifierIdentifiers]
- -[CKSettingsMessagesController shouldShowContactPhotoSettings]
- -[CKSettingsMessagesController shouldShowInboxSummarySettings]
- -[CKSettingsMessagesController shouldShowJunkConversationsRow]
- -[CKSettingsMessagesController shouldShowJunkFilteringReceipts]
- -[CKSettingsMessagesController shouldShowNicknames]
- -[CKSettingsMessagesController shouldShowOnlineSafetyLink]
- -[CKSettingsMessagesController shouldShowRaiseToListenSwitch]
- -[CKSettingsMessagesController shouldShowSharedWithYouSettings]
- -[CKSettingsMessagesController spamFilteringSpecifierIdentifiers]
- GCC_except_table165
- GCC_except_table217
- GCC_except_table218
- GCC_except_table219
- GCC_except_table222
- GCC_except_table277
- _OBJC_CLASS_$_CMGestureManager
- _OBJC_CLASS_$_IMLockdownManager
- ___56-[CKSettingsMessagesController _isRaiseGestureSupported]_block_invoke
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.898
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.903
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.922
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_2.924
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_3.926
- ___69-[CNFRegSettingsController _setupAccountHandlersForDisabledOperation]_block_invoke.891
- ___Block_byref_object_copy_.917
- ___Block_byref_object_dispose_.918
- ___block_literal_global.395
- ___block_literal_global.546
- ___block_literal_global.576
- ___block_literal_global.584
- __isRaiseGestureSupported.isRaiseGestureSupported
- __isRaiseGestureSupported.once
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_isMessagesTheDefaultMessagingApp
- _objc_msgSend$_isRaiseGestureSupported
- _objc_msgSend$_shouldShowSatelliteDemoModeButton
- _objc_msgSend$canChangeDefaultAppForCategory:
- _objc_msgSend$defaultApplicationForCategory:error:
- _objc_msgSend$filterUnkownSendersSpecifierIdentifiers
- _objc_msgSend$generativeModelsAvailable
- _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
- _objc_msgSend$isGestureServiceAvailable
- _objc_msgSend$isInternalInstall
- _objc_msgSend$isIntroductionsEnabled
- _objc_msgSend$isProximityMonitoringEnabled
- _objc_msgSend$isReadMMSDefaultFromCBEnabled
- _objc_msgSend$isSendMenuEnabled
- _objc_msgSend$isTranscriptBackgroundsEnabled
- _objc_msgSend$isTranscriptBackgroundsEnabledViaSyncedSettings
- _objc_msgSend$messagesFilteringSpecifierIdentifiers
- _objc_msgSend$setProximityMonitoringEnabled:
- _objc_msgSend$setSummarizationUserPreferenceEnabled:
- _objc_msgSend$sharedWithYouSettingsSpecifierIdentifiers
- _objc_msgSend$shouldShowSharedWithYouSettings
- _objc_msgSend$spamFilteringSpecifierIdentifiers
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "#CHARACTER_COUNT_SWITCH"
+ "#CONTACT_PHOTO_SWITCH"
+ "#CONVERSATION_BACKGROUNDS_ENABLED_SWITCH"
+ "#CONVERSATION_BACKGROUNDS_START_WITH_PHOTOS_VISIBLE"
+ "#FILTER_NEW_SENDERS_SWITCH"
+ "#INBOX_SUMMARY_SWITCH"
+ "#JUNK_FILTERING_RECEIPTS_SWITCH"
+ "#MADRID_ENABLED_SWITCH"
+ "#MENTIONS_NOTIFY_ME_ID"
+ "#MMS_EMAIL_CELL"
+ "#MMS_MESSAGING"
+ "#ONLINE_SAFETY_BUTTON"
+ "#PREVIEW_TRANSCODING_SWITCH"
+ "#RAISE_TO_LISTEN_SWITCH"
+ "#READ_RECEIPTS_SWITCH"
+ "#SEND_AS_SMS_SWITCH"
+ "#SHOW_SUBJECT_FIELD_SWITCH"
+ "#SPAM_FILTERING_SWITCH"
+ "#TRY_DEMO_MODE_BUTTON_ACTION_ID"
+ "/"
+ "/BLOCKLIST_SETTINGS_MAIN_SPECIFIER_IDENTIFIER"
+ "/BUSINESS_CHAT_BUTTON"
+ "/CHECK_IN_LOCATION_HISTORY_ID"
+ "/EXPIRE_AUDIO_MESSAGES"
+ "/IMESSAGE_APPS_BUTTON"
+ "/JUNK_CONVERSATIONS_BUTTON"
+ "/KEEP_MESSAGES_BUTTON"
+ "/MADRID_ACCOUNTS_BUTTON"
+ "/MMS_MESSAGING_CELL"
+ "/NAME_AND_PHOTO_SHARING_BUTTON"
+ "/NOTIFICATIONS_UNKNOWN_SENDERS_BUTTON"
+ "/RCS_MESSAGING_CELL#BusinessRCSMessages"
+ "/RCS_MESSAGING_CELL#RCS"
+ "/SHARED_WITH_YOU_BUTTON"
+ "/SMS_RELAY_DEVICES"
+ "/TEXT_MESSAGE_FILTERING"
+ "@\"NSArray\"16@0:8"
+ "BUSINESS_CHAT_GROUP"
+ "CKRaiseGesture"
+ "Error enabling/disabling RCS encryption: %@"
+ "FACETIME_TITLE"
+ "RCSEncryption"
+ "RCS_ENCRYPTION_BETA"
+ "RCS_ENCRYPTION_BETA_FOOTER"
+ "SMS_MMS_RCS_RELAY"
+ "SMS_MMS_RCS_RELAY_DEVICES_HEADER"
+ "SMS_MMS_RCS_RELAY_DEVICES_LABEL"
+ "SMS_MMS_RCS_RELAY_DEVICES_NAME_AND_TYPE"
+ "SMS_MMS_RCS_RELAY_MIC_DEVICES_FOOTER"
+ "SMS_MMS_RCS_RELAY_MIC_OTHER_DEVICES_FOOTER"
+ "SMS_MMS_RCS_RELAY_ON"
+ "SMS_MMS_RCS_RELAY_PLACEHOLDER"
+ "Set RCS Encryption Enabled: %@"
+ "ShouldShowMMS %d subscriptionsWithMMSSupport.count %d subscriptionsWithRCSSupport.count %d"
+ "T@\"NSArray\",R,N"
+ "TB,R,N,GareTranscriptBackgroundsEnabled"
+ "TB,R,N,GisFilteringUnknownSenders"
+ "_canSetRCSEncryptionForSubscription:"
+ "_isRCSEncryptionEnabledForSubscription:"
+ "_isRCSEncryptionSupportedForSubscription:"
+ "_mmsSubscriptionsListWithSubscriptionInfo:mmsEmailVisible:"
+ "_setRCSEncryptionEnabledForSubscription:enabled:"
+ "_shouldShowCheckInLocationHistorySettingsForSearchContext:"
+ "_shouldShowMMS"
+ "_showRCSEncryptionForSubscription:"
+ "allSubscriptionsWithRCSSupport"
+ "areTranscriptBackgroundsEnabled"
+ "canSetRCSEncryption"
+ "carrierSupport"
+ "com.apple.conference.MessagesSettingsWidgetKitExtension"
+ "connectWithCompletion:"
+ "controlValue"
+ "encryptionCapabilities"
+ "filteringUnknownSenders"
+ "isConversationListFilteringEnabled"
+ "isFilteringUnknownSenders"
+ "isMessagesTheDefaultTextApp"
+ "isRCSEncryptionEnabled"
+ "isRCSEncryptionEnabled:"
+ "isRCSEncryptionEnabledForAnyActiveSubscription"
+ "isRaiseGestureSupported"
+ "multiplexedConnectionWithLabel:capabilities:context:"
+ "setLazuliEncryption:enabled:withError:"
+ "setMessageSummarizationUserPreference:"
+ "setRCSEncryptionEnabled:specifier:"
+ "sharedController"
+ "shouldShowConversationBackgroundStartWithPhotosVisible"
+ "shouldShowJunkConversationsInSearch"
+ "shouldShowMMSEmailAddress"
+ "shouldShowMMSPane"
+ "shouldShowMMSSwitch"
+ "shouldShowMessagesForBusiness"
+ "shouldShowRCSBusinessMessaging"
+ "shouldShowRCSPane"
+ "shouldShowSatelliteDemoModeButton"
+ "shouldShowSatelliteDemoModeButtonInSearch"
+ "showRCSEncryption"
+ "showSwitch"
+ "startMonitorIfNeededForReason:"
+ "transcriptBackgroundsEnabled"
+ "waitForSetup"
- "%@ (%@)"
- "CONVERSATION_BACKGROUNDS_ENABLED_SWITCH"
- "CONVERSATION_BACKGROUNDS_GROUP"
- "Can't change default app so behaving as if Messages is the default"
- "Can't find application record for domain %@, error %@"
- "CoreTelephony"
- "Development"
- "Force.MessageIsDefaultApp"
- "Force.MessageIsNotDefaultApp"
- "IMESSAGE_FILTERING_GROUP"
- "Interstellar"
- "Livability"
- "MADRID_FILTER"
- "MADRID_FILTER_LABEL"
- "MESSAGES_FILTERING_LABEL"
- "MESSAGES_UNKNOWN_SENDERS_GROUP"
- "MessagingAPI"
- "PRIVACY_WARNING_ACTION"
- "PRIVACY_WARNING_APP_NAME_TITLE"
- "PRIVACY_WARNING_CANCEL"
- "SHARED_WITH_YOU_GROUP"
- "SMS_RELAY"
- "SMS_RELAY_DEVICES_HEADER"
- "SMS_RELAY_MIC_DEVICES_FOOTER"
- "SMS_RELAY_MIC_OTHER_DEVICES_FOOTER"
- "SMS_RELAY_MULTIPLE_DEVICES_LABEL"
- "SMS_RELAY_ON"
- "SMS_RELAY_SINGLE_DEVICE_LABEL"
- "SPAM_FILTERING_GROUP_LABEL"
- "ShouldShowMMS %@ subscriptionsWithMMSEnabledCount %@ subscriptionsWithMMSOverrideEnabledCount %@ subscriptionsWithRCSEnabledCount %@"
- "_isMessagesTheDefaultMessagingApp"
- "_isRaiseGestureSupported"
- "_shouldShowSatelliteDemoModeButton"
- "canChangeDefaultAppForCategory:"
- "defaultApplicationForCategory:error:"
- "filterUnkownSendersSpecifierIdentifiers"
- "generativeModelsAvailable"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "isGestureServiceAvailable"
- "isInternalInstall"
- "isIntroductionsEnabled"
- "isProximityMonitoringEnabled"
- "isReadMMSDefaultFromCBEnabled"
- "isSendMenuEnabled"
- "isTranscriptBackgroundsEnabled"
- "isTranscriptBackgroundsEnabledViaSyncedSettings"
- "messagesFilteringSpecifierIdentifiers"
- "setProximityMonitoringEnabled:"
- "setSummarizationUserPreferenceEnabled:"
- "sharedWithYouSettingsSpecifierIdentifiers"
- "shouldShowSharedWithYouSettings"
- "spamFilteringSpecifierIdentifiers"

```
