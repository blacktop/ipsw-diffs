## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore`

```diff

-191.13.0.0.0
-  __TEXT.__text: 0x144c34
-  __TEXT.__auth_stubs: 0x2c60
-  __TEXT.__objc_methlist: 0xb660
-  __TEXT.__const: 0x36a4
-  __TEXT.__cstring: 0xc511
-  __TEXT.__oslogstring: 0xa3f6
-  __TEXT.__gcc_except_tab: 0x1cbc
+208.2.0.0.0
+  __TEXT.__text: 0x14b108
+  __TEXT.__auth_stubs: 0x2bf0
+  __TEXT.__objc_methlist: 0xb4ac
+  __TEXT.__const: 0x3754
+  __TEXT.__cstring: 0x9c48
+  __TEXT.__oslogstring: 0xa836
+  __TEXT.__gcc_except_tab: 0x1b04
   __TEXT.__ustring: 0xe6
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__constg_swiftt: 0x1cf0
-  __TEXT.__swift5_typeref: 0x3d60
+  __TEXT.__constg_swiftt: 0x1ce8
+  __TEXT.__swift5_typeref: 0x3b96
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0xac2
-  __TEXT.__swift5_fieldmd: 0xcfc
-  __TEXT.__swift5_assocty: 0x2a0
-  __TEXT.__swift5_proto: 0x158
+  __TEXT.__swift5_reflstr: 0xb5b
+  __TEXT.__swift5_fieldmd: 0xd3c
+  __TEXT.__swift5_assocty: 0x270
+  __TEXT.__swift5_proto: 0x15c
   __TEXT.__swift5_types: 0x13c
-  __TEXT.__swift5_capture: 0xd08
+  __TEXT.__swift5_capture: 0xd1c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4b20
-  __TEXT.__eh_frame: 0x1580
-  __TEXT.__objc_classname: 0x11e2
-  __TEXT.__objc_methname: 0x1d1d8
-  __TEXT.__objc_methtype: 0x3dc8
-  __TEXT.__objc_stubs: 0x14dc0
-  __DATA_CONST.__got: 0x11b0
-  __DATA_CONST.__const: 0x4018
-  __DATA_CONST.__objc_classlist: 0x540
+  __TEXT.__unwind_info: 0x5040
+  __TEXT.__eh_frame: 0x13e0
+  __TEXT.__objc_classname: 0x1a9c
+  __TEXT.__objc_methname: 0x1e64d
+  __TEXT.__objc_methtype: 0x45fb
+  __TEXT.__objc_stubs: 0x16900
+  __DATA_CONST.__got: 0x1178
+  __DATA_CONST.__const: 0x4138
+  __DATA_CONST.__objc_classlist: 0x520
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7598
+  __DATA_CONST.__objc_selrefs: 0x7590
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x288
+  __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x4d0
-  __AUTH_CONST.__auth_got: 0x1640
-  __AUTH_CONST.__const: 0x47b8
-  __AUTH_CONST.__cfstring: 0x9080
-  __AUTH_CONST.__objc_const: 0x1d648
+  __AUTH_CONST.__auth_got: 0x1608
+  __AUTH_CONST.__const: 0x4780
+  __AUTH_CONST.__cfstring: 0x9020
+  __AUTH_CONST.__objc_const: 0x1cf78
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x498
-  __AUTH.__objc_data: 0x4ec8
-  __AUTH.__data: 0xd70
-  __DATA.__objc_ivar: 0x704
-  __DATA.__data: 0x2cb0
+  __AUTH.__objc_data: 0x4e48
+  __AUTH.__data: 0xda0
+  __DATA.__objc_ivar: 0x6f0
+  __DATA.__data: 0x2ca0
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x3038
+  __DATA.__bss: 0x30b8
   __DATA.__common: 0x158
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6D098208-3CA0-3F1D-98C3-63652EA79A4C
-  Functions: 7345
-  Symbols:   15726
-  CStrings:  9424
+  UUID: 45744032-71ED-3B00-9272-C614F9CE65C5
+  Functions: 7444
+  Symbols:   16033
+  CStrings:  9277
 
Symbols:
+ +[FBKAttachmentViewingControllerSelector _finalizeController:attachment:deleteHandler:]
+ +[FBKAttachmentViewingControllerSelector controllerForAttachment:deleteHandler:]
+ +[FBKAttachmentViewingControllerSelector controllerForItem:deleteHandler:]
+ +[FBKAttachmentViewingControllerSelector controllerForItem:deleteHandler:].cold.1
+ +[FBKAttachmentViewingControllerSelector controllerForUrl:]
+ +[FBKAttachmentViewingControllerSelector controllerForUrl:deleteHandler:]
+ +[FBKLaunchAction actionWithPathAndQueryParams:]
+ +[FBKNotificationManager shared]
+ +[FBKNotificationManager shared].cold.1
+ -[FBKAttachmentViewerViewController initWithURL:]
+ -[FBKDECollector _updateAttachmentsWithRequirements:alreadyCollectedGroups:alreadyStartedCollections:deferredCollections:].cold.1
+ -[FBKData recordConsentResponseForConsent:response:completionWithError:]
+ -[FBKDeviceDisplayCell initWithStyle:reuseIdentifier:]
+ -[FBKDeviceDisplayCell setupConstraints]
+ -[FBKDeviceDisplayCell setupViews]
+ -[FBKLaunchAction initWithFeedbackAssistantWebURL:]
+ -[FBKLaunchAction initWithFeedbackAssistantWebURL:].cold.1
+ -[FBKLaunchAction initWithFeedbackAssistantWebURL:].cold.2
+ -[FBKLaunchAction itemTypeToShow]
+ -[FBKLaunchAction setItemTypeToShow:]
+ -[FBKNotificationManager .cxx_destruct]
+ -[FBKNotificationManager APNSToken]
+ -[FBKNotificationManager deregisterTokenWithSeedPortal:completion:]
+ -[FBKNotificationManager deregisterTokenWithSeedPortal:completion:].cold.1
+ -[FBKNotificationManager deregisterTokenWithSeedPortal:completion:].cold.2
+ -[FBKNotificationManager registerTokenWithSeedPortal:]
+ -[FBKNotificationManager registerTokenWithSeedPortal:].cold.1
+ -[FBKNotificationManager registerTokenWithSeedPortal:].cold.2
+ -[FBKNotificationManager requestPermission]
+ -[FBKNotificationManager setAPNSToken:]
+ -[FBKNotificationManager setToken:]
+ -[FBKNotificationManager setToken:].cold.1
+ -[FBKNotificationManager setToken:].cold.2
+ -[FBKSeedPortalAPI APNSTokenURL]
+ -[FBKSeedPortalAPI deregisterAPNSWithRequestDictionary:success:error:]
+ -[FBKTeam didInitialContentItemFetch]
+ -[FBKTeam setDidInitialContentItemFetch:]
+ -[NSURLComponents(QueryDictionary) fbkQueryDictionaryForName:]
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachment:fromIndexPath:deleteHandler:]
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachment:fromIndexPath:deleteHandler:].cold.1
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachment:fromIndexPath:deleteHandler:].cold.2
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachmentWithImagePush:fromIndexPath:deleteHandler:]
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachmentWithImagePush:fromIndexPath:deleteHandler:].cold.1
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table114
+ GCC_except_table117
+ GCC_except_table121
+ GCC_except_table125
+ GCC_except_table132
+ GCC_except_table141
+ GCC_except_table143
+ GCC_except_table147
+ GCC_except_table153
+ GCC_except_table158
+ GCC_except_table164
+ GCC_except_table170
+ GCC_except_table174
+ GCC_except_table176
+ GCC_except_table182
+ GCC_except_table184
+ GCC_except_table186
+ GCC_except_table198
+ GCC_except_table208
+ GCC_except_table219
+ GCC_except_table223
+ GCC_except_table229
+ GCC_except_table236
+ GCC_except_table243
+ GCC_except_table249
+ GCC_except_table283
+ GCC_except_table285
+ GCC_except_table289
+ GCC_except_table290
+ GCC_except_table341
+ GCC_except_table391
+ GCC_except_table399
+ GCC_except_table400
+ GCC_except_table409
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table65
+ GCC_except_table76
+ GCC_except_table78
+ GCC_except_table81
+ GCC_except_table97
+ GCC_except_table98
+ _FBKWebURLAnnouncementItem
+ _FBKWebURLDraftItem
+ _FBKWebURLFeedbackItem
+ _FBKWebURLFormResponseItem
+ _FBKWebURLFragmentFollowupPrefix
+ _FBKWebURLHost
+ _FBKWebURLNewDraft
+ _FBKWebURLNewFormResponse
+ _FBKWebURLNewsItem
+ _FBKWebURLParameterAnswers
+ _FBKWebURLParameterFormIdentifier
+ _FBKWebURLSurveyFeedbackItem
+ _FBKWebURLSurveyItem
+ _FBKWebURLWelcome
+ _OBJC_CLASS_$_FBKNotificationManager
+ _OBJC_CLASS_$_UNUserNotificationCenter
+ _OBJC_CLASS_$__TtC12FeedbackCore27FBKEmbeddedAttachmentViewer
+ _OBJC_IVAR_$_FBKLaunchAction._itemTypeToShow
+ _OBJC_IVAR_$_FBKNotificationManager._APNSToken
+ _OBJC_IVAR_$_FBKTeam._didInitialContentItemFetch
+ _OBJC_METACLASS_$_FBKNotificationManager
+ _OBJC_METACLASS_$__TtC12FeedbackCore27FBKEmbeddedAttachmentViewer
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ __DATA__TtC12FeedbackCore27FBKEmbeddedAttachmentViewer
+ __INSTANCE_METHODS__TtC12FeedbackCore27FBKEmbeddedAttachmentViewer
+ __IVARS__TtC12FeedbackCore27FBKEmbeddedAttachmentViewer
+ __METACLASS_DATA__TtC12FeedbackCore27FBKEmbeddedAttachmentViewer
+ __OBJC_$_CATEGORY_NSString_$_FBKInstalledAppAdditions
+ __OBJC_$_CATEGORY_NSURLComponents_$_QueryDictionary
+ __OBJC_$_CLASS_METHODS_FBKNotificationManager
+ __OBJC_$_CLASS_METHODS_NSString(FBKInstalledAppAdditions|FBKFile|FBKUtils|Truncation|FeedbackCore)
+ __OBJC_$_INSTANCE_METHODS_FBKLoginManager(FeedbackCore)
+ __OBJC_$_INSTANCE_METHODS_FBKNotificationManager
+ __OBJC_$_INSTANCE_METHODS_NSString(FBKInstalledAppAdditions|FBKFile|FBKUtils|Truncation|FeedbackCore)
+ __OBJC_$_INSTANCE_METHODS_NSURLComponents(QueryDictionary|FeedbackCore)
+ __OBJC_$_INSTANCE_VARIABLES_FBKNotificationManager
+ __OBJC_$_INSTANCE_VARIABLES_FBKTeam
+ __OBJC_$_PROP_LIST_FBKNotificationManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBKAddAttachmentsControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBKBugFormPickerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBKAddAttachmentsControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBKBugFormPickerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBKAddAttachmentsControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBKBugFormPickerDelegate
+ __OBJC_$_PROTOCOL_REFS_FBKAddAttachmentsControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_FBKBugFormPickerDelegate
+ __OBJC_CLASS_RO_$_FBKNotificationManager
+ __OBJC_LABEL_PROTOCOL_$_FBKAddAttachmentsControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_FBKBugFormPickerDelegate
+ __OBJC_METACLASS_RO_$_FBKNotificationManager
+ __OBJC_PROTOCOL_$_FBKAddAttachmentsControllerDelegate
+ __OBJC_PROTOCOL_$_FBKBugFormPickerDelegate
+ __PROPERTIES__TtC12FeedbackCore27FBKEmbeddedAttachmentViewer
+ __PROTOCOLS__TtC12FeedbackCore21FBKAddAttachmentsCell.7
+ ___25-[FBKLoginManager logOut]_block_invoke_5
+ ___32+[FBKNotificationManager shared]_block_invoke
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.251
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.251.cold.1
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.258
+ ___39-[FBKData saveFormResponse:completion:]_block_invoke.244
+ ___39-[FBKData saveFormResponse:completion:]_block_invoke.246
+ ___39-[FBKData saveFormResponse:completion:]_block_invoke_2.245
+ ___39-[FBKData saveFormResponse:completion:]_block_invoke_2.245.cold.1
+ ___42-[FBKBugFormTableViewController legalText]_block_invoke.293
+ ___42-[FBKData deleteUploadForTask:completion:]_block_invoke.264.cold.1
+ ___42-[FBKData deleteUploadForTask:completion:]_block_invoke.265
+ ___43-[FBKData markAnnouncementRead:completion:]_block_invoke.299
+ ___43-[FBKNotificationManager requestPermission]_block_invoke
+ ___43-[FBKNotificationManager requestPermission]_block_invoke.42
+ ___43-[FBKNotificationManager requestPermission]_block_invoke.cold.1
+ ___44-[FBKData formResponseStubForID:completion:]_block_invoke.247
+ ___44-[FBKData refreshUnreadCountWithCompletion:]_block_invoke.195
+ ___47-[FBKData getAllContentForFeedback:completion:]_block_invoke.260
+ ___51-[FBKData deleteDraftsFromContentItems:completion:]_block_invoke.228
+ ___51-[FBKData deleteDraftsFromContentItems:completion:]_block_invoke.228.cold.1
+ ___52-[FBKData refreshFormResponseOnlyWithID:completion:]_block_invoke.208
+ ___52-[FBKData refreshFormResponseOnlyWithID:completion:]_block_invoke.210
+ ___52-[FBKData refreshFormResponseOnlyWithID:completion:]_block_invoke_2.209
+ ___52-[FBKData refreshFormResponseOnlyWithID:completion:]_block_invoke_2.209.cold.1
+ ___53-[FBKData fetchFeedbackStatusForFeedback:completion:]_block_invoke.253
+ ___54-[FBKData _refreshContentItemsForTeam:withCompletion:]_block_invoke_3
+ ___54-[FBKData recordConsentResponseForConsent:completion:]_block_invoke.309
+ ___54-[FBKNotificationManager registerTokenWithSeedPortal:]_block_invoke
+ ___54-[FBKNotificationManager registerTokenWithSeedPortal:]_block_invoke.33
+ ___54-[FBKNotificationManager registerTokenWithSeedPortal:]_block_invoke.33.cold.1
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.75.cold.1
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.75.cold.2
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.75.cold.3
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.76
+ ___57-[FBKData refreshAnnouncementFromContentItem:completion:]_block_invoke.297
+ ___57-[FBKLoginManager loginWithAppleConnectToken:completion:]_block_invoke.92
+ ___57-[FBKSeedPortalAPI didLogInWithLoginUserInfo:completion:]_block_invoke.22
+ ___58-[FBKLoginManager autoLoginUsingSystemAccount:completion:]_block_invoke.71
+ ___59-[FBKData createFeedbackFollowupOfType:forItem:completion:]_block_invoke.288
+ ___59-[FBKData createFeedbackFollowupOfType:forItem:completion:]_block_invoke.291
+ ___59-[FBKData createFeedbackFollowupOfType:forItem:completion:]_block_invoke_2.290
+ ___59-[FBKData createFeedbackFollowupOfType:forItem:completion:]_block_invoke_2.290.cold.1
+ ___59-[FBKData refreshSurveyFromContentItem:forTeam:completion:]_block_invoke.255
+ ___60-[FBKData _didGetFeedback:error:withContentItem:completion:]_block_invoke.258
+ ___60-[FBKData deleteDraftFromContentItem:shouldSave:completion:]_block_invoke.224
+ ___60-[FBKData deleteDraftFromContentItem:shouldSave:completion:]_block_invoke.226.cold.1
+ ___60-[FBKData deleteDraftFromContentItem:shouldSave:completion:]_block_invoke.227
+ ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke.211
+ ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke.213
+ ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke.213.cold.1
+ ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke.217
+ ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke.219
+ ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke.223
+ ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke_2.212
+ ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke_2.212.cold.1
+ ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke_2.218
+ ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke_2.221
+ ___60-[FBKLoginManager loginWithEphemeralDeviceToken:completion:]_block_invoke.66
+ ___60-[FBKLoginManager loginWithEphemeralDeviceToken:completion:]_block_invoke_2.67
+ ___61-[FBKData getFeedbackFollowupForFeedback:atIndex:completion:]_block_invoke.263
+ ___61-[FBKData getFeedbackFollowupForFeedback:atIndex:completion:]_block_invoke.263.cold.1
+ ___61-[FBKData refreshFormResponseStubFromContentItem:completion:]_block_invoke.250
+ ___61-[FBKData refreshFormResponseStubFromContentItem:completion:]_block_invoke.250.cold.1
+ ___61-[FBKData refreshFormResponseStubFromContentItem:completion:]_block_invoke.250.cold.2
+ ___61-[FBKSeedPortalAPI getFormResponseStubWithID:withCompletion:]_block_invoke.242
+ ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.201
+ ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.201.cold.1
+ ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke.237
+ ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke_2.238
+ ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke_2.238.cold.1
+ ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke_2.238.cold.2
+ ___65-[FBKData deleteUnsolicitedFollowup:withFeedbackItem:completion:]_block_invoke.295
+ ___65-[FBKData deleteUnsolicitedFollowup:withFeedbackItem:completion:]_block_invoke_2.296
+ ___67-[FBKData beginSubmissionForFormResponse:withCollector:completion:]_block_invoke.345
+ ___67-[FBKData beginSubmissionForFormResponse:withCollector:completion:]_block_invoke_2.346
+ ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke.353
+ ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke.357
+ ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke_2.354
+ ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke_2.358
+ ___67-[FBKLoginManager loginAsAnonymousUserWithLaunchAction:completion:]_block_invoke.68
+ ___67-[FBKLoginManager loginAsAnonymousUserWithLaunchAction:completion:]_block_invoke_2.69
+ ___67-[FBKNotificationManager deregisterTokenWithSeedPortal:completion:]_block_invoke
+ ___67-[FBKNotificationManager deregisterTokenWithSeedPortal:completion:]_block_invoke.37
+ ___67-[FBKNotificationManager deregisterTokenWithSeedPortal:completion:]_block_invoke.37.cold.1
+ ___67-[FBKSeedPortalAPI fetchAnnouncementForContentItem:withCompletion:]_block_invoke.254
+ ___68-[FBKData beginFileSubmissionForFilerForm:withCollector:completion:]_block_invoke.351
+ ___68-[FBKData beginFileSubmissionForFilerForm:withCollector:completion:]_block_invoke.351.cold.1
+ ___68-[FBKSeedPortalAPI getFileDownloadURLForFilePromiseUUID:completion:]_block_invoke.272
+ ___69-[FBKBugFormTableViewController checkDeviceConnectivity:andContinue:]_block_invoke.219
+ ___69-[FBKBugFormTableViewController checkDeviceConnectivity:andContinue:]_block_invoke.223
+ ___69-[FBKBugFormTableViewController checkDeviceConnectivity:andContinue:]_block_invoke.227
+ ___71-[FBKLoginManager _loginWithUsername:authenticationResults:completion:]_block_invoke.91
+ ___72-[FBKData recordConsentResponseForConsent:response:completionWithError:]_block_invoke
+ ___72-[FBKData recordConsentResponseForConsent:response:completionWithError:]_block_invoke.306
+ ___72-[FBKData recordConsentResponseForConsent:response:completionWithError:]_block_invoke_2
+ ___72-[FBKData recordConsentResponseForConsent:response:completionWithError:]_block_invoke_2.307
+ ___72-[FBKData recordConsentResponseForConsent:response:completionWithError:]_block_invoke_3
+ ___72-[FBKData recordConsentResponseForConsent:response:completionWithError:]_block_invoke_3.308
+ ___72-[FBKData recordConsentResponseForConsent:response:completionWithError:]_block_invoke_4
+ ___72-[FBKData recordConsentResponseForConsent:response:completionWithError:]_block_invoke_5
+ ___72-[FBKData recordConsentResponseForConsent:response:completionWithError:]_block_invoke_6
+ ___72-[FBKData recordConsentResponseForConsent:response:completionWithError:]_block_invoke_7
+ ___72-[FBKData recordConsentResponseForConsent:response:completionWithError:]_block_invoke_7.cold.1
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.173
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.173.cold.1
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.173.cold.2
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.173.cold.3
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.176
+ ___74-[FBKData respondToFollowup:withResponses:collector:optingOut:completion:]_block_invoke.293
+ ___74-[FBKLoginManager _completeAuthenticationWith:credentialToken:completion:]_block_invoke.81
+ ___74-[FBKLoginManager _completeAuthenticationWith:credentialToken:completion:]_block_invoke_2.82
+ ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.189
+ ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.189.cold.1
+ ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.190
+ ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.190.cold.1
+ ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.198
+ ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.202
+ ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.310
+ ___79-[FBKSeedPortalAPI createFormResponseForBugForm:inTeam:appToken:success:error:]_block_invoke.225
+ ___84-[FBKData refreshBugFormWithID:fromStub:forTeam:requestPlugIns:appToken:completion:]_block_invoke.200
+ ___84-[FBKData refreshBugFormWithID:fromStub:forTeam:requestPlugIns:appToken:completion:]_block_invoke.202.cold.1
+ ___84-[FBKData refreshBugFormWithID:fromStub:forTeam:requestPlugIns:appToken:completion:]_block_invoke.203
+ ___87-[FBKData beginSubmissionForFollowup:withResponses:didOptOut:withCollector:completion:]_block_invoke.360
+ ___87-[FBKSeedPortalAPI fetchBugFormWithID:forTeamID:requestPlugIns:appToken:success:error:]_block_invoke.214
+ ___89-[FBKLoginManager autoLoginWithUserID:userName:deviceToken:usesSystemAccount:completion:]_block_invoke.89
+ ___89-[FBKLoginManager autoLoginWithUserID:userName:deviceToken:usesSystemAccount:completion:]_block_invoke_2.90
+ ___91-[FBKData _newFormResponseForBugFormID:formStub:inTeam:requestPlugIns:appToken:completion:]_block_invoke.204
+ ___91-[FBKData _newFormResponseForBugFormID:formStub:inTeam:requestPlugIns:appToken:completion:]_block_invoke.206
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32s_e21_v24?0"FBKTeam"8^B16ls32l8
+ ___block_descriptor_48_e8_32s40s_e57_v16?0"_TtC12FeedbackCore27FBKEmbeddedAttachmentViewer"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e27_v24?0"NSSet"8"NSError"16lw48l8s40l8s32l8
+ ___block_literal_global.137
+ ___block_literal_global.209
+ ___block_literal_global.213
+ ___block_literal_global.240
+ ___block_literal_global.247
+ ___block_literal_global.289
+ ___block_literal_global.291
+ ___block_literal_global.295
+ ___block_literal_global.314
+ ___block_literal_global.349
+ ___block_literal_global.36
+ ___block_literal_global.373
+ ___block_literal_global.41
+ ___block_literal_global.62
+ ___block_literal_global.646
+ ___block_literal_global.90
+ _associated conformance 12FeedbackCore19AuthenticationErrorOSHAASQ
+ _block_copy_helper.132
+ _block_copy_helper.51
+ _block_copy_helper.64
+ _block_copy_helper.72
+ _block_copy_helper.78
+ _block_copy_helper.90
+ _block_descriptor.134
+ _block_descriptor.53
+ _block_descriptor.66
+ _block_descriptor.74
+ _block_descriptor.80
+ _block_descriptor.92
+ _block_destroy_helper.133
+ _block_destroy_helper.52
+ _block_destroy_helper.65
+ _block_destroy_helper.73
+ _block_destroy_helper.79
+ _block_destroy_helper.91
+ _flat unique So24FBKBugFormPickerDelegate_p
+ _flat unique So35FBKAddAttachmentsControllerDelegate_p
+ _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOQr.1
+ _get_underlying_witness 7SwiftUI4ViewPAAEAcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOqd0__AaBHC.2
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA6HStackVyAA9TupleViewVyACyAA6SpacerVAA12_FrameLayoutVG_ACy12FeedbackCore014AttachmentIconG0VAA08_PaddingJ0VGACyACyAA6VStackVyAGyAA012_ConditionalD0VyAA4TextVAXG_ACyACyAxA30_EnvironmentKeyWritingModifierVySiSgGGA_yAX14TruncationModeOGGSgA7_tGGAQGAQGAiCyAM0m9AccessoryG0VAQGtGGAA013AccessibilitymV0VGAA0G0HPA16_AAA20_HPyHC_A18_AA0gV0HPyHCHC.5
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA6HStackVyAA9TupleViewVyACyACyAA0G0PAAE10fontWeightyQrAA4FontV0I0VSgFQOyACyACyACyAA5ImageVAA24_ForegroundStyleModifierVyAA5ColorVGGAA18_AspectRatioLayoutVGAA06_FrameR0VG_Qo_AA08_PaddingR0VGAA013_TraitWritingN0VyAA010TransitionU3KeyVGGSg_ACyACyACyAA6VStackVyAGyAA4TextV_ACyAA09_VariadicG0O4TreeVy_AA01_R4RootVy12FeedbackCore013EvenWidthGridR0VGAA7ForEachVySaySo17FBKQuestionChoiceCGA30_ACyAiAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOyAiAE06toggleM0yQrqd__AA06ToggleM0Rd__lFQOyAA6ToggleVyACyA16_AA05_FlexsR0VGG_AA012ButtonToggleM0VQo__A30_Qo_A4_GGGA4_GtGGA4_GA39_GA0_GtGGA39_GAaHHPA56_AaHHPyHC_A39_AA0gN0HPyHCHC.61
+ _keypath_get.17Tm
+ _legalText.onceToken.292
+ _objc_msgSend$APNSToken
+ _objc_msgSend$APNSTokenURL
+ _objc_msgSend$URLForDirectory:inDomain:appropriateForURL:create:error:
+ _objc_msgSend$__swift_objectForKeyedSubscript:
+ _objc_msgSend$__swift_setObject:forKeyedSubscript:
+ _objc_msgSend$_annotationUntypedButAccessibleInSwift
+ _objc_msgSend$_finalizeController:attachment:deleteHandler:
+ _objc_msgSend$actionWithURL:
+ _objc_msgSend$adamID
+ _objc_msgSend$addAttachmentWithItemProvider:
+ _objc_msgSend$addAttributes:range:
+ _objc_msgSend$addConstraint:
+ _objc_msgSend$addFileFrom:byMoving:
+ _objc_msgSend$addFileFromURL:byMoving:
+ _objc_msgSend$addTarget:action:forControlEvents:
+ _objc_msgSend$addTeamsObject:
+ _objc_msgSend$addedCurrentDeviceNeedsMatcherPredicateEvaluation
+ _objc_msgSend$addedRows
+ _objc_msgSend$addedSections
+ _objc_msgSend$additionalDeviceCandidates
+ _objc_msgSend$additionalDevicePlatforms
+ _objc_msgSend$additionalMatchers
+ _objc_msgSend$additionalSysdiagnoseMatcherWithPlatform:
+ _objc_msgSend$allAttachments
+ _objc_msgSend$appWithAppProxy:
+ _objc_msgSend$assignFeedback:inTeamID:toParticipantID:success:error:
+ _objc_msgSend$assignURLForTeamID:participantID:
+ _objc_msgSend$attachmentCollections
+ _objc_msgSend$attachmentIndex:
+ _objc_msgSend$attachmentManager
+ _objc_msgSend$attachmentManager:didAddAttachment:atIndex:
+ _objc_msgSend$attachmentManager:didFinishAttaching:error:
+ _objc_msgSend$attachmentManager:didRemoveAttachment:atIndex:
+ _objc_msgSend$attachmentManager:didStartAttaching:
+ _objc_msgSend$attachmentManager:didStartBugSessionsForDevice:success:
+ _objc_msgSend$attachmentManager:didUpdateAttachment:atIndex:
+ _objc_msgSend$attachmentsAlert:needsDeviceDiagnosticsController:
+ _objc_msgSend$attachmentsAlertDidSelectOption:
+ _objc_msgSend$attachmentsBeingAttached
+ _objc_msgSend$attachmentsForDevice:
+ _objc_msgSend$boundingRectWithSize:options:attributes:context:
+ _objc_msgSend$bugFormPicker:didSelectBugFormStub:
+ _objc_msgSend$bugFormPickerDidCancel:
+ _objc_msgSend$bundleURL
+ _objc_msgSend$cachedDiffableIdentifiersTable
+ _objc_msgSend$canBeDeleted
+ _objc_msgSend$canDemoteFeedback
+ _objc_msgSend$canLoadObjectsOfClass:
+ _objc_msgSend$canPromoteFeedback
+ _objc_msgSend$canReassignFeedback
+ _objc_msgSend$cancelCollection:
+ _objc_msgSend$centerYAnchor
+ _objc_msgSend$choiceForValue:
+ _objc_msgSend$collectorIdentifier
+ _objc_msgSend$collectsSameDiagnosticsAsOtherMatcher:
+ _objc_msgSend$combine
+ _objc_msgSend$commitWithForm:withCompletion:
+ _objc_msgSend$configurationWithActions:
+ _objc_msgSend$constraintEqualToConstant:
+ _objc_msgSend$contextualActionWithStyle:title:handler:
+ _objc_msgSend$controllerForAttachment:deleteHandler:
+ _objc_msgSend$controllerForItem:deleteHandler:
+ _objc_msgSend$controllerForUrl:
+ _objc_msgSend$controllerForUrl:deleteHandler:
+ _objc_msgSend$copyItem:toDestinationDir:zipped:
+ _objc_msgSend$currentNotificationCenter
+ _objc_msgSend$currentTraitCollection
+ _objc_msgSend$dataForURL:success:error:
+ _objc_msgSend$deConsentTextsForGatheringAttachments
+ _objc_msgSend$demoteFeedback:fromTeamID:success:error:
+ _objc_msgSend$demoteURLForTeamID:
+ _objc_msgSend$deregisterAPNSWithRequestDictionary:success:error:
+ _objc_msgSend$deregisterTokenWithSeedPortal:completion:
+ _objc_msgSend$descriptionString
+ _objc_msgSend$deviceDataForSubmissionWithSession:filerFormID:
+ _objc_msgSend$deviceDiagnosticsCombineObject
+ _objc_msgSend$deviceDiagnosticsController:didAddAttachment:toDevice:
+ _objc_msgSend$deviceDiagnosticsController:didAddDevices:
+ _objc_msgSend$deviceDiagnosticsController:didFailToAttach:toDevice:error:
+ _objc_msgSend$deviceDiagnosticsController:didFailToConnectToDevice:
+ _objc_msgSend$deviceDiagnosticsController:didRemoveAttachment:fromDevice:
+ _objc_msgSend$deviceDiagnosticsController:didRemoveDevice:
+ _objc_msgSend$deviceDiagnosticsController:didUpdateAttachment:onDevice:
+ _objc_msgSend$deviceDiagnosticsController:needsSelectionFromDevices:completion:
+ _objc_msgSend$deviceHasAnyAttachmentsWithDevice:
+ _objc_msgSend$deviceIdToAttachments
+ _objc_msgSend$didFetch
+ _objc_msgSend$dragItem
+ _objc_msgSend$enumerateApplicationsOfType:block:
+ _objc_msgSend$envelopedObjectFrom:
+ _objc_msgSend$fbkPresetAttachment:fromIndexPath:deleteHandler:
+ _objc_msgSend$fbkQueryDictionaryForName:
+ _objc_msgSend$fontDescriptor
+ _objc_msgSend$fontDescriptorByAddingAttributes:
+ _objc_msgSend$fontDescriptorWithSymbolicTraits:
+ _objc_msgSend$fontWithDescriptor:size:
+ _objc_msgSend$formDescription
+ _objc_msgSend$fragment
+ _objc_msgSend$gatherFilesForExtension:answers:
+ _objc_msgSend$getFilesFromFileProviderBeforeTheyDisappearWithCoordinator:
+ _objc_msgSend$getParticipantsForTeamID:success:error:
+ _objc_msgSend$getRed:green:blue:alpha:
+ _objc_msgSend$handleDataResponseFor:data:success:errorHandler:
+ _objc_msgSend$hasAnyAttachmentCollectedOrCollecting
+ _objc_msgSend$hasAnyDevices
+ _objc_msgSend$hasItemsConformingToTypeIdentifiers:
+ _objc_msgSend$hasUnmetRequirements
+ _objc_msgSend$iconName
+ _objc_msgSend$icons
+ _objc_msgSend$ignoredMatchers
+ _objc_msgSend$imageNamed:inBundle:
+ _objc_msgSend$imageWithRenderingMode:
+ _objc_msgSend$init
+ _objc_msgSend$initDevice:matcherPredicates:
+ _objc_msgSend$initForOpeningContentTypes:asCopy:
+ _objc_msgSend$initForTextStyle:
+ _objc_msgSend$initWithAttachmentManager:device:
+ _objc_msgSend$initWithCategory:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithDeviceChoices:allowsMultipleSelection:completion:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithDropOperation:
+ _objc_msgSend$initWithDropOperation:intent:
+ _objc_msgSend$initWithEmbeddedViewController:deleteAction:
+ _objc_msgSend$initWithFeedbackAssistantWebURL:
+ _objc_msgSend$initWithFrame:textContainer:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithMatcherPredicates:pendingFileUrls:pendingExtensions:form:targetDevice:shouldGetSessionStatus:shouldCheckDeferredLogs:attachmentDescriptors:autoGathersDiagnosticExtensions:
+ _objc_msgSend$initWithNavigationBarClass:toolbarClass:
+ _objc_msgSend$initWithNibName:bundle:
+ _objc_msgSend$initWithRed:green:blue:alpha:
+ _objc_msgSend$initWithSection:object:
+ _objc_msgSend$initWithType:object:
+ _objc_msgSend$initWithView:respond:close:download:delete:assign:demote:
+ _objc_msgSend$isAlreadyCollectingThisMatcher:ignoreAdditional:
+ _objc_msgSend$isAppStoreVendable
+ _objc_msgSend$isAttachmentParent:
+ _objc_msgSend$isNetworkError:
+ _objc_msgSend$isOn
+ _objc_msgSend$isReadyForDropSessionFromController:tableView:dropSessionDidUpdate:withDestinationIndexPath:
+ _objc_msgSend$itemProvider
+ _objc_msgSend$items
+ _objc_msgSend$labelFontSize
+ _objc_msgSend$linkWithBundleIdentifier:
+ _objc_msgSend$localizedCustomerConsentText
+ _objc_msgSend$menu
+ _objc_msgSend$modalConfigurations
+ _objc_msgSend$moveFileFrom:
+ _objc_msgSend$participants
+ _objc_msgSend$participantsURLForTeamID:
+ _objc_msgSend$pattern
+ _objc_msgSend$pendingRequirements
+ _objc_msgSend$postLaunchAttachLocalFiles:allRequirements:
+ _objc_msgSend$prefetchedChoices
+ _objc_msgSend$presentingViewController
+ _objc_msgSend$previousSnapshot
+ _objc_msgSend$promisedFileName
+ _objc_msgSend$promoteFeedback:toTeamID:success:error:
+ _objc_msgSend$promoteURLForTeamID:
+ _objc_msgSend$questionGroupIdToQuestions
+ _objc_msgSend$recordConsentResponseForConsent:response:completionWithError:
+ _objc_msgSend$registerAPNSWithRequestDictionary:success:error:
+ _objc_msgSend$registerForRemoteNotifications
+ _objc_msgSend$registerTokenWithSeedPortal:
+ _objc_msgSend$removeDevice:
+ _objc_msgSend$removeFromParentViewController
+ _objc_msgSend$removeTeamsObject:
+ _objc_msgSend$removedDevices
+ _objc_msgSend$removedRows
+ _objc_msgSend$removedSections
+ _objc_msgSend$replaceEmptyAttachmentsWithAdditionalMatchersWithAdditional:
+ _objc_msgSend$replacePreviousAdditionalMatchersWithRequiredMatchersIfNeededWithRequired:
+ _objc_msgSend$requestAuthorizationWithOptions:completionHandler:
+ _objc_msgSend$requirements
+ _objc_msgSend$requiresRemote
+ _objc_msgSend$setAPNSToken:
+ _objc_msgSend$setAddedCurrentDeviceNeedsMatcherPredicateEvaluation:
+ _objc_msgSend$setAllowedUnits:
+ _objc_msgSend$setAllowsMultipleSelection:
+ _objc_msgSend$setApp:
+ _objc_msgSend$setAttachmentCollections:
+ _objc_msgSend$setAttributedText:
+ _objc_msgSend$setCanSelect:
+ _objc_msgSend$setContentCompressionResistancePriority:forAxis:
+ _objc_msgSend$setContentEdgeInsets:
+ _objc_msgSend$setContentHorizontalAlignment:
+ _objc_msgSend$setDataDetectorTypes:
+ _objc_msgSend$setDate:
+ _objc_msgSend$setDatePickerMode:
+ _objc_msgSend$setDeferredAttachmentCollections:
+ _objc_msgSend$setDeviceDiagnosticsCombineObject:
+ _objc_msgSend$setDeviceIcon:
+ _objc_msgSend$setDidFetch:
+ _objc_msgSend$setDidInitialContentItemFetch:
+ _objc_msgSend$setDraftDevices:
+ _objc_msgSend$setFilesBeingAttachedCount:
+ _objc_msgSend$setGivenSectionIdentifier:
+ _objc_msgSend$setHidesBackButton:
+ _objc_msgSend$setIgnoredMatchers:
+ _objc_msgSend$setImage:forState:
+ _objc_msgSend$setImageEdgeInsets:
+ _objc_msgSend$setIsRefreshingTeams:
+ _objc_msgSend$setMaximumUnitCount:
+ _objc_msgSend$setMaximumValue:
+ _objc_msgSend$setMinimumValue:
+ _objc_msgSend$setNameLabel:
+ _objc_msgSend$setNeedsUpdateConfiguration
+ _objc_msgSend$setOn:
+ _objc_msgSend$setOnTintColor:
+ _objc_msgSend$setPendingRequirements:
+ _objc_msgSend$setPrefetchedChoices:
+ _objc_msgSend$setPreviousMatcherPredicates:
+ _objc_msgSend$setRemovedDevices:
+ _objc_msgSend$setScrollEnabled:
+ _objc_msgSend$setSeparatorInset:
+ _objc_msgSend$setShowsMenuAsPrimaryAction:
+ _objc_msgSend$setTextContainerInset:
+ _objc_msgSend$setTitle:forState:
+ _objc_msgSend$setTitleColor:forState:
+ _objc_msgSend$setTitleEdgeInsets:
+ _objc_msgSend$setTypeLabel:
+ _objc_msgSend$setUnitsStyle:
+ _objc_msgSend$setValue:animated:
+ _objc_msgSend$set_annotationUntypedButAccessibleInSwift:
+ _objc_msgSend$setupConstraints
+ _objc_msgSend$setupViews
+ _objc_msgSend$shared
+ _objc_msgSend$snapshotWithSize:scale:options:
+ _objc_msgSend$sortDescriptors
+ _objc_msgSend$sp2
+ _objc_msgSend$storyboardWithName:bundle:
+ _objc_msgSend$stringByReplacingCharactersInRange:withString:
+ _objc_msgSend$systemFontOfSize:weight:
+ _objc_msgSend$targetDevice
+ _objc_msgSend$teamPicker:didSelectTeam:
+ _objc_msgSend$teamPickerDidCancel:
+ _objc_msgSend$teamsURL
+ _objc_msgSend$titleLabel
+ _objc_msgSend$trailingSwipeActionConfigurationWithAttachment:orDevice:fromViewController:
+ _objc_msgSend$updateMatcherPredicatesWithUpdatedMatchers:allRequiredMatchers:formPlatform:
+ _objc_msgSend$updateRequirements:
+ _objc_msgSend$updateTeamsWithCompletion:
+ _objc_msgSend$userInterfaceStyle
+ _objc_msgSend$verticalSizeClass
+ _objc_msgSend$widthAnchor
+ _objc_msgSend$wrapFeedbackIDs:
+ _objectdestroy.37Tm
+ _shared.onceToken
+ _shared.sharedInstance
+ _swift_willThrowTypedImpl
+ _symbolic SaySo18NSLayoutConstraintCG
+ _symbolic SaySo7NSErrorCG
+ _symbolic So6UIViewC
+ _symbolic So8UIButtonC
+ _symbolic _____ 12FeedbackCore19AuthenticationErrorO
+ _symbolic _____ 12FeedbackCore27FBKEmbeddedAttachmentViewerC
+ _symbolic _____IeyBy_ 12FeedbackCore27FBKEmbeddedAttachmentViewerC
+ _symbolic ______pSgXw So24FBKBugFormPickerDelegateP
+ _symbolic ______pSgXw So35FBKAddAttachmentsControllerDelegateP
+ _symbolic _____yAAyAAy__________G_____y_____GG_____G 7SwiftUI15ModifiedContentV AA5ImageV AA12_FrameLayoutV AA24_ForegroundStyleModifierV AA5ColorV AA08_PaddingG0V
+ _symbolic _____y______G 7Combine9PublishedV9PublisherV So18FBKAttachmentStateV
+ _symbolic y_____cSg 12FeedbackCore27FBKEmbeddedAttachmentViewerC
+ _type_layout_string So16NSURLResourceKeya
- +[FBKAttachmentViewingControllerSelector _setControllerTitle:attachment:]
- +[FBKAttachmentViewingControllerSelector _setControllerTitle:dedItem:]
- +[FBKAttachmentViewingControllerSelector _setControllerTitle:url:]
- +[FBKAttachmentViewingControllerSelector controllerForAttachment:useRedesign:deleteHandler:]
- +[FBKAttachmentViewingControllerSelector controllerForItem:useRedesign:deleteHandler:]
- +[FBKAttachmentViewingControllerSelector controllerForItem:useRedesign:deleteHandler:].cold.1
- +[FBKAttachmentViewingControllerSelector controllerForUrl:useFallback:useRedesign:deleteHandler:]
- +[FBKAttachmentViewingControllerSelector controllerForUrl:useRedesign:deleteHandler:]
- +[FBKAttachmentViewingControllerSelector fallbackToOpaqueViewer]
- +[FBKIssueDefinition entityName]
- +[FBKIssueType entityName]
- +[FBKSecureUnarchiveFromDataTransformer allowedTopLevelClasses]
- +[FBKSecureUnarchiveFromDataTransformer initialize]
- -[FBKAttachmentViewerViewController _didTapDeleteButton]
- -[FBKAttachmentViewerViewController initWithURL:deleteHandler:]
- -[FBKAttachmentViewerViewController interactionEnabled]
- -[FBKAttachmentViewerViewController setInteractionEnabled:]
- -[FBKBugFormFileBrowserTableViewController .cxx_destruct]
- -[FBKBugFormFileBrowserTableViewController directoryList]
- -[FBKBugFormFileBrowserTableViewController documentInteractionControllerDidEndPreview:]
- -[FBKBugFormFileBrowserTableViewController documentInteractionControllerRectForPreview:]
- -[FBKBugFormFileBrowserTableViewController documentInteractionControllerViewControllerForPreview:]
- -[FBKBugFormFileBrowserTableViewController documentInteractionControllerViewForPreview:]
- -[FBKBugFormFileBrowserTableViewController group]
- -[FBKBugFormFileBrowserTableViewController initWithGroup:]
- -[FBKBugFormFileBrowserTableViewController initWithUrl:]
- -[FBKBugFormFileBrowserTableViewController numberOfSectionsInTableView:]
- -[FBKBugFormFileBrowserTableViewController setDirectoryList:]
- -[FBKBugFormFileBrowserTableViewController setGroup:]
- -[FBKBugFormFileBrowserTableViewController setUrl:]
- -[FBKBugFormFileBrowserTableViewController tableView:cellForRowAtIndexPath:]
- -[FBKBugFormFileBrowserTableViewController tableView:didSelectRowAtIndexPath:]
- -[FBKBugFormFileBrowserTableViewController tableView:didSelectRowAtIndexPath:].cold.1
- -[FBKBugFormFileBrowserTableViewController tableView:didSelectRowAtIndexPath:].cold.2
- -[FBKBugFormFileBrowserTableViewController tableView:didSelectRowAtIndexPath:].cold.3
- -[FBKBugFormFileBrowserTableViewController tableView:numberOfRowsInSection:]
- -[FBKBugFormFileBrowserTableViewController url]
- -[FBKBugFormFileBrowserTableViewController viewDidLoad]
- -[FBKBugFormTableViewController _useAttachmentCellRedesign]
- -[FBKBugFormTableViewController adjustAttachmentLabelSpacing:]
- -[FBKDeviceDisplayCell awakeFromNib]
- -[FBKDeviceDisplayCell didTapConnectionButton:]
- -[FBKDeviceDisplayCell setConnected:]
- -[FBKFollowupTableCell .cxx_destruct]
- -[FBKFollowupTableCell promptLabel]
- -[FBKFollowupTableCell responseLabel]
- -[FBKFollowupTableCell setPromptLabel:]
- -[FBKFollowupTableCell setResponseLabel:]
- -[FBKImagePickerController shouldAutorotate]
- -[FBKImagePickerController supportedInterfaceOrientations]
- -[FBKInstalledApp isIWorkApp]
- -[FBKInstalledApp isIWorkApp].cold.1
- -[FBKIssueDefinition setPropertiesFromJSONObject:]
- -[FBKIssueType setPropertiesFromJSONObject:]
- -[FBKSeedPortalAPI createResponseURLForBugFormID:appToken:]
- -[FBKSeedPortalAPI deregisterAPNSWithDeviceToken:success:error:]
- -[FBKSeedPortalAPI registerAPNSTokenURL]
- -[FBKSeedPortalAPI unregisterAPNSTokenURL]
- -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachment:fromIndexPath:]
- -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachment:fromIndexPath:useRedesign:deleteHandler:]
- -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachment:fromIndexPath:useRedesign:deleteHandler:].cold.1
- -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachment:fromIndexPath:useRedesign:deleteHandler:].cold.2
- -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachmentWithImagePush:fromIndexPath:useRedesign:deleteHandler:]
- -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachmentWithImagePush:fromIndexPath:useRedesign:deleteHandler:].cold.1
- GCC_except_table104
- GCC_except_table105
- GCC_except_table112
- GCC_except_table115
- GCC_except_table116
- GCC_except_table119
- GCC_except_table130
- GCC_except_table140
- GCC_except_table142
- GCC_except_table144
- GCC_except_table149
- GCC_except_table152
- GCC_except_table157
- GCC_except_table161
- GCC_except_table168
- GCC_except_table172
- GCC_except_table175
- GCC_except_table180
- GCC_except_table183
- GCC_except_table187
- GCC_except_table197
- GCC_except_table207
- GCC_except_table218
- GCC_except_table222
- GCC_except_table227
- GCC_except_table234
- GCC_except_table242
- GCC_except_table246
- GCC_except_table280
- GCC_except_table282
- GCC_except_table286
- GCC_except_table287
- GCC_except_table344
- GCC_except_table388
- GCC_except_table393
- GCC_except_table397
- GCC_except_table406
- GCC_except_table54
- GCC_except_table55
- GCC_except_table60
- GCC_except_table68
- GCC_except_table69
- GCC_except_table74
- GCC_except_table79
- GCC_except_table80
- GCC_except_table94
- _FBKPushItemIDKey
- _FBKPushItemTypeAnnouncement
- _FBKPushItemTypeFollowup
- _FBKPushItemTypeKey
- _FBKPushItemTypeSurvey
- _FBKPushNotificationsEnabled
- _FBKPushParticipantIDKey
- _FBKSecureUnarchiveFromDataTransformerName
- _OBJC_CLASS_$_FBKBugFormFileBrowserTableViewController
- _OBJC_CLASS_$_FBKFollowupTableCell
- _OBJC_CLASS_$_FBKImagePickerController
- _OBJC_CLASS_$_FBKIssueDefinition
- _OBJC_CLASS_$_FBKIssueType
- _OBJC_CLASS_$_FBKSecureUnarchiveFromDataTransformer
- _OBJC_CLASS_$_NSSecureUnarchiveFromDataTransformer
- _OBJC_CLASS_$_UIImagePickerController
- _OBJC_IVAR_$_FBKAttachmentViewerViewController._deleteButton
- _OBJC_IVAR_$_FBKAttachmentViewerViewController._deleteHandler
- _OBJC_IVAR_$_FBKAttachmentViewerViewController._interactionEnabled
- _OBJC_IVAR_$_FBKBugFormFileBrowserTableViewController._directoryList
- _OBJC_IVAR_$_FBKBugFormFileBrowserTableViewController._group
- _OBJC_IVAR_$_FBKBugFormFileBrowserTableViewController._url
- _OBJC_IVAR_$_FBKFollowupTableCell._promptLabel
- _OBJC_IVAR_$_FBKFollowupTableCell._responseLabel
- _OBJC_METACLASS_$_FBKBugFormFileBrowserTableViewController
- _OBJC_METACLASS_$_FBKFollowupTableCell
- _OBJC_METACLASS_$_FBKImagePickerController
- _OBJC_METACLASS_$_FBKIssueDefinition
- _OBJC_METACLASS_$_FBKIssueType
- _OBJC_METACLASS_$_FBKSecureUnarchiveFromDataTransformer
- _OBJC_METACLASS_$_NSSecureUnarchiveFromDataTransformer
- _OBJC_METACLASS_$_UIImagePickerController
- __CATEGORY_INSTANCE_METHODS_NSURLComponents_$_FeedbackCore
- __CATEGORY_NSURLComponents_$_FeedbackCore
- __CATEGORY_PROPERTIES_NSURLComponents_$_FeedbackCore
- __FBKAnswerIsBlank
- __OBJC_$_CATEGORY_NSString_$_FBKFile
- __OBJC_$_CLASS_METHODS_FBKIssueDefinition
- __OBJC_$_CLASS_METHODS_FBKIssueType
- __OBJC_$_CLASS_METHODS_FBKSecureUnarchiveFromDataTransformer
- __OBJC_$_CLASS_METHODS_NSString(FBKFile|FBKInstalledAppAdditions|Truncation|FBKUtils|FeedbackCore)
- __OBJC_$_INSTANCE_METHODS_FBKBugFormFileBrowserTableViewController
- __OBJC_$_INSTANCE_METHODS_FBKFollowupTableCell
- __OBJC_$_INSTANCE_METHODS_FBKImagePickerController
- __OBJC_$_INSTANCE_METHODS_FBKIssueDefinition
- __OBJC_$_INSTANCE_METHODS_FBKIssueType
- __OBJC_$_INSTANCE_METHODS_FBKLoginManager
- __OBJC_$_INSTANCE_METHODS_NSString(FBKFile|FBKInstalledAppAdditions|Truncation|FBKUtils|FeedbackCore)
- __OBJC_$_INSTANCE_VARIABLES_FBKBugFormFileBrowserTableViewController
- __OBJC_$_INSTANCE_VARIABLES_FBKFollowupTableCell
- __OBJC_$_PROP_LIST_FBKAttachmentViewerViewController
- __OBJC_$_PROP_LIST_FBKBugFormFileBrowserTableViewController
- __OBJC_$_PROP_LIST_FBKFollowupTableCell
- __OBJC_$_PROP_LIST_FBKIssueDefinition
- __OBJC_$_PROP_LIST_FBKIssueType
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__TtP12FeedbackCore24FBKBugFormPickerDelegate_
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__TtP12FeedbackCore35FBKAddAttachmentsControllerDelegate_
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP12FeedbackCore24FBKBugFormPickerDelegate_
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP12FeedbackCore35FBKAddAttachmentsControllerDelegate_
- __OBJC_$_PROTOCOL_METHOD_TYPES__TtP12FeedbackCore24FBKBugFormPickerDelegate_
- __OBJC_$_PROTOCOL_METHOD_TYPES__TtP12FeedbackCore35FBKAddAttachmentsControllerDelegate_
- __OBJC_CLASS_PROTOCOLS_$_FBKBugFormFileBrowserTableViewController
- __OBJC_CLASS_RO_$_FBKBugFormFileBrowserTableViewController
- __OBJC_CLASS_RO_$_FBKFollowupTableCell
- __OBJC_CLASS_RO_$_FBKImagePickerController
- __OBJC_CLASS_RO_$_FBKIssueDefinition
- __OBJC_CLASS_RO_$_FBKIssueType
- __OBJC_CLASS_RO_$_FBKSecureUnarchiveFromDataTransformer
- __OBJC_LABEL_PROTOCOL_$__TtP12FeedbackCore24FBKBugFormPickerDelegate_
- __OBJC_LABEL_PROTOCOL_$__TtP12FeedbackCore35FBKAddAttachmentsControllerDelegate_
- __OBJC_METACLASS_RO_$_FBKBugFormFileBrowserTableViewController
- __OBJC_METACLASS_RO_$_FBKFollowupTableCell
- __OBJC_METACLASS_RO_$_FBKImagePickerController
- __OBJC_METACLASS_RO_$_FBKIssueDefinition
- __OBJC_METACLASS_RO_$_FBKIssueType
- __OBJC_METACLASS_RO_$_FBKSecureUnarchiveFromDataTransformer
- __OBJC_PROTOCOL_$__TtP12FeedbackCore24FBKBugFormPickerDelegate_
- __OBJC_PROTOCOL_$__TtP12FeedbackCore35FBKAddAttachmentsControllerDelegate_
- __PROTOCOLS__TtC12FeedbackCore21FBKAddAttachmentsCell.5
- __PROTOCOL_INSTANCE_METHODS_OPT__TtP12FeedbackCore24FBKBugFormPickerDelegate_
- __PROTOCOL_INSTANCE_METHODS_OPT__TtP12FeedbackCore35FBKAddAttachmentsControllerDelegate_
- __PROTOCOL_INSTANCE_METHODS__TtP12FeedbackCore24FBKBugFormPickerDelegate_
- __PROTOCOL_INSTANCE_METHODS__TtP12FeedbackCore35FBKAddAttachmentsControllerDelegate_
- __PROTOCOL_METHOD_TYPES__TtP12FeedbackCore24FBKBugFormPickerDelegate_
- __PROTOCOL_METHOD_TYPES__TtP12FeedbackCore35FBKAddAttachmentsControllerDelegate_
- __PROTOCOL__TtP12FeedbackCore24FBKBugFormPickerDelegate_
- __PROTOCOL__TtP12FeedbackCore35FBKAddAttachmentsControllerDelegate_
- ___29-[FBKInstalledApp isIWorkApp]_block_invoke
- ___39-[FBKBugFormTableViewController submit]_block_invoke.253
- ___39-[FBKBugFormTableViewController submit]_block_invoke.253.cold.1
- ___39-[FBKBugFormTableViewController submit]_block_invoke.262
- ___39-[FBKData saveFormResponse:completion:]_block_invoke.243
- ___39-[FBKData saveFormResponse:completion:]_block_invoke.245
- ___39-[FBKData saveFormResponse:completion:]_block_invoke_2.244
- ___39-[FBKData saveFormResponse:completion:]_block_invoke_2.244.cold.1
- ___42-[FBKBugFormTableViewController legalText]_block_invoke.295
- ___42-[FBKData deleteUploadForTask:completion:]_block_invoke.263
- ___42-[FBKData deleteUploadForTask:completion:]_block_invoke.263.cold.1
- ___43-[FBKData markAnnouncementRead:completion:]_block_invoke.298
- ___44-[FBKData formResponseStubForID:completion:]_block_invoke.246
- ___44-[FBKData refreshUnreadCountWithCompletion:]_block_invoke.194
- ___47-[FBKData getAllContentForFeedback:completion:]_block_invoke.259
- ___48-[FBKAttachmentViewerViewController viewDidLoad]_block_invoke
- ___48-[FBKBugFormTableViewController _separatorInset]_block_invoke
- ___51+[FBKSecureUnarchiveFromDataTransformer initialize]_block_invoke
- ___51-[FBKData deleteDraftsFromContentItems:completion:]_block_invoke.227
- ___51-[FBKData deleteDraftsFromContentItems:completion:]_block_invoke.227.cold.1
- ___52-[FBKData refreshFormResponseOnlyWithID:completion:]_block_invoke.207
- ___52-[FBKData refreshFormResponseOnlyWithID:completion:]_block_invoke.209
- ___52-[FBKData refreshFormResponseOnlyWithID:completion:]_block_invoke_2.208
- ___52-[FBKData refreshFormResponseOnlyWithID:completion:]_block_invoke_2.208.cold.1
- ___53-[FBKData fetchFeedbackStatusForFeedback:completion:]_block_invoke.252
- ___54-[FBKData recordConsentResponseForConsent:completion:]_block_invoke.308
- ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.73
- ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.73.cold.1
- ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.73.cold.2
- ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.74.cold.3
- ___57-[FBKData refreshAnnouncementFromContentItem:completion:]_block_invoke.296
- ___57-[FBKLoginManager loginWithAppleConnectToken:completion:]_block_invoke.91
- ___57-[FBKSeedPortalAPI didLogInWithLoginUserInfo:completion:]_block_invoke.21
- ___58-[FBKLoginManager autoLoginUsingSystemAccount:completion:]_block_invoke.70
- ___59-[FBKData createFeedbackFollowupOfType:forItem:completion:]_block_invoke.284
- ___59-[FBKData createFeedbackFollowupOfType:forItem:completion:]_block_invoke.290
- ___59-[FBKData createFeedbackFollowupOfType:forItem:completion:]_block_invoke_2.289
- ___59-[FBKData createFeedbackFollowupOfType:forItem:completion:]_block_invoke_2.289.cold.1
- ___59-[FBKData refreshSurveyFromContentItem:forTeam:completion:]_block_invoke.254
- ___60-[FBKData _didGetFeedback:error:withContentItem:completion:]_block_invoke.257
- ___60-[FBKData deleteDraftFromContentItem:shouldSave:completion:]_block_invoke.223
- ___60-[FBKData deleteDraftFromContentItem:shouldSave:completion:]_block_invoke.225
- ___60-[FBKData deleteDraftFromContentItem:shouldSave:completion:]_block_invoke.225.cold.1
- ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke.210
- ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke.212
- ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke.212.cold.1
- ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke.216
- ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke.218
- ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke.222
- ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke_2.211
- ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke_2.211.cold.1
- ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke_2.217
- ___60-[FBKData refreshFormResponseWithID:contentItem:completion:]_block_invoke_2.220
- ___60-[FBKLoginManager loginWithEphemeralDeviceToken:completion:]_block_invoke.65
- ___60-[FBKLoginManager loginWithEphemeralDeviceToken:completion:]_block_invoke_2.66
- ___61-[FBKData getFeedbackFollowupForFeedback:atIndex:completion:]_block_invoke.262
- ___61-[FBKData getFeedbackFollowupForFeedback:atIndex:completion:]_block_invoke.262.cold.1
- ___61-[FBKData refreshFormResponseStubFromContentItem:completion:]_block_invoke.249
- ___61-[FBKData refreshFormResponseStubFromContentItem:completion:]_block_invoke.249.cold.1
- ___61-[FBKData refreshFormResponseStubFromContentItem:completion:]_block_invoke.249.cold.2
- ___61-[FBKSeedPortalAPI getFormResponseStubWithID:withCompletion:]_block_invoke.241
- ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.203
- ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.203.cold.1
- ___63+[FBKSecureUnarchiveFromDataTransformer allowedTopLevelClasses]_block_invoke
- ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke.239
- ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke_2.240
- ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke_2.240.cold.1
- ___63-[FBKBugFormTableViewController checkMissingFiles:andContinue:]_block_invoke_2.240.cold.2
- ___63-[FBKData recordConsentResponseForConsent:response:completion:]_block_invoke.305
- ___63-[FBKData recordConsentResponseForConsent:response:completion:]_block_invoke_2
- ___63-[FBKData recordConsentResponseForConsent:response:completion:]_block_invoke_2.306
- ___63-[FBKData recordConsentResponseForConsent:response:completion:]_block_invoke_3
- ___63-[FBKData recordConsentResponseForConsent:response:completion:]_block_invoke_3.307
- ___63-[FBKData recordConsentResponseForConsent:response:completion:]_block_invoke_4
- ___63-[FBKData recordConsentResponseForConsent:response:completion:]_block_invoke_5
- ___63-[FBKData recordConsentResponseForConsent:response:completion:]_block_invoke_6
- ___63-[FBKData recordConsentResponseForConsent:response:completion:]_block_invoke_7
- ___63-[FBKData recordConsentResponseForConsent:response:completion:]_block_invoke_7.cold.1
- ___65-[FBKData deleteUnsolicitedFollowup:withFeedbackItem:completion:]_block_invoke.294
- ___65-[FBKData deleteUnsolicitedFollowup:withFeedbackItem:completion:]_block_invoke_2.295
- ___67-[FBKData beginSubmissionForFormResponse:withCollector:completion:]_block_invoke.344
- ___67-[FBKData beginSubmissionForFormResponse:withCollector:completion:]_block_invoke_2.345
- ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke.351
- ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke.356
- ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke_2.353
- ___67-[FBKData markFormResponseComplete:withFiles:collector:completion:]_block_invoke_2.357
- ___67-[FBKLoginManager loginAsAnonymousUserWithLaunchAction:completion:]_block_invoke.67
- ___67-[FBKLoginManager loginAsAnonymousUserWithLaunchAction:completion:]_block_invoke_2.68
- ___67-[FBKSeedPortalAPI fetchAnnouncementForContentItem:withCompletion:]_block_invoke.253
- ___68-[FBKData beginFileSubmissionForFilerForm:withCollector:completion:]_block_invoke.350
- ___68-[FBKData beginFileSubmissionForFilerForm:withCollector:completion:]_block_invoke.350.cold.1
- ___68-[FBKSeedPortalAPI getFileDownloadURLForFilePromiseUUID:completion:]_block_invoke.271
- ___69-[FBKBugFormTableViewController checkDeviceConnectivity:andContinue:]_block_invoke.221
- ___69-[FBKBugFormTableViewController checkDeviceConnectivity:andContinue:]_block_invoke.225
- ___69-[FBKBugFormTableViewController checkDeviceConnectivity:andContinue:]_block_invoke.229
- ___71-[FBKLoginManager _loginWithUsername:authenticationResults:completion:]_block_invoke.90
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.175
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.175.cold.1
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.175.cold.2
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.175.cold.3
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.178
- ___74-[FBKData respondToFollowup:withResponses:collector:optingOut:completion:]_block_invoke.292
- ___74-[FBKLoginManager _completeAuthenticationWith:credentialToken:completion:]_block_invoke.80
- ___74-[FBKLoginManager _completeAuthenticationWith:credentialToken:completion:]_block_invoke_2.81
- ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.191
- ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.191.cold.1
- ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.192
- ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.192.cold.1
- ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.200
- ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.204
- ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.314
- ___79-[FBKSeedPortalAPI createFormResponseForBugForm:inTeam:appToken:success:error:]_block_invoke.224
- ___84-[FBKData refreshBugFormWithID:fromStub:forTeam:requestPlugIns:appToken:completion:]_block_invoke.198
- ___84-[FBKData refreshBugFormWithID:fromStub:forTeam:requestPlugIns:appToken:completion:]_block_invoke.201
- ___84-[FBKData refreshBugFormWithID:fromStub:forTeam:requestPlugIns:appToken:completion:]_block_invoke.201.cold.1
- ___87-[FBKData beginSubmissionForFollowup:withResponses:didOptOut:withCollector:completion:]_block_invoke.358
- ___87-[FBKSeedPortalAPI fetchBugFormWithID:forTeamID:requestPlugIns:appToken:success:error:]_block_invoke.216
- ___89-[FBKLoginManager autoLoginWithUserID:userName:deviceToken:usesSystemAccount:completion:]_block_invoke.88
- ___89-[FBKLoginManager autoLoginWithUserID:userName:deviceToken:usesSystemAccount:completion:]_block_invoke_2.89
- ___91-[FBKData _newFormResponseForBugFormID:formStub:inTeam:requestPlugIns:appToken:completion:]_block_invoke.203
- ___91-[FBKData _newFormResponseForBugFormID:formStub:inTeam:requestPlugIns:appToken:completion:]_block_invoke.205
- ___block_descriptor_48_e8_32bs40w_e27_v24?0"NSSet"8"NSError"16lw40l8s32l8
- ___block_descriptor_48_e8_32s40s_e43_v16?0"FBKAttachmentViewerViewController"8ls32l8s40l8
- ___block_literal_global.136
- ___block_literal_global.167
- ___block_literal_global.212
- ___block_literal_global.261
- ___block_literal_global.268
- ___block_literal_global.293
- ___block_literal_global.297
- ___block_literal_global.310
- ___block_literal_global.316
- ___block_literal_global.348
- ___block_literal_global.372
- ___block_literal_global.644
- ___block_literal_global.82
- ___block_literal_global.92
- ___block_literal_global.94
- __separatorInset.inset
- __separatorInset.onceToken
- _allowedTopLevelClasses.classes
- _allowedTopLevelClasses.onceToken
- _associated conformance 12FeedbackCore16CapsuleFillStyle33_CC3864F153E422CCA8CBAEF59B1A78A1LLV7SwiftUI05ShapeE0AA8ResolvedAeFP_AeF
- _associated conformance 12FeedbackCore27AttachmentsBadgeOverlayViewV7SwiftUI0F0AA4BodyAdEP_AdE
- _block_copy_helper.101
- _block_copy_helper.107
- _block_copy_helper.113
- _block_copy_helper.119
- _block_copy_helper.38
- _block_copy_helper.44
- _block_copy_helper.50
- _block_copy_helper.56
- _block_copy_helper.71
- _block_copy_helper.77
- _block_copy_helper.83
- _block_copy_helper.89
- _block_copy_helper.95
- _block_descriptor.103
- _block_descriptor.109
- _block_descriptor.115
- _block_descriptor.121
- _block_descriptor.40
- _block_descriptor.46
- _block_descriptor.52
- _block_descriptor.58
- _block_descriptor.73
- _block_descriptor.79
- _block_descriptor.85
- _block_descriptor.91
- _block_descriptor.97
- _block_destroy_helper.102
- _block_destroy_helper.108
- _block_destroy_helper.114
- _block_destroy_helper.120
- _block_destroy_helper.39
- _block_destroy_helper.45
- _block_destroy_helper.51
- _block_destroy_helper.57
- _block_destroy_helper.72
- _block_destroy_helper.78
- _block_destroy_helper.84
- _block_destroy_helper.90
- _block_destroy_helper.96
- _flat unique 12FeedbackCore24FBKBugFormPickerDelegate_p
- _flat unique 12FeedbackCore35FBKAddAttachmentsControllerDelegate_p
- _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOQr.2
- _get_underlying_witness 7SwiftUI4ViewPAAEAcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOqd0__AaBHC.3
- _get_witness_table 7SwiftUI15ModifiedContentVyAA6HStackVyAA9TupleViewVyACyAA6SpacerVAA12_FrameLayoutVG_ACy12FeedbackCore014AttachmentIconG0VAA08_PaddingJ0VGACyACyAA6VStackVyAGyAA012_ConditionalD0VyAA4TextVAXG_ACyACyAxA30_EnvironmentKeyWritingModifierVySiSgGGA_yAX14TruncationModeOGGSgA7_tGGAQGAQGAiCyAM0m9AccessoryG0VAQGtGGAA013AccessibilitymV0VGAA0G0HPA16_AAA20_HPyHC_A18_AA0gV0HPyHCHC.31
- _get_witness_table 7SwiftUI15ModifiedContentVyAA6HStackVyAA9TupleViewVyACyACyAA0G0PAAE10fontWeightyQrAA4FontV0I0VSgFQOyACyACyACyAA5ImageVAA24_ForegroundStyleModifierVyAA5ColorVGGAA18_AspectRatioLayoutVGAA06_FrameR0VG_Qo_AA08_PaddingR0VGAA013_TraitWritingN0VyAA010TransitionU3KeyVGGSg_ACyACyACyAA6VStackVyAGyAA4TextV_ACyAA09_VariadicG0O4TreeVy_AA01_R4RootVy12FeedbackCore013EvenWidthGridR0VGAA7ForEachVySaySo17FBKQuestionChoiceCGA30_ACyAiAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOyAiAE06toggleM0yQrqd__AA06ToggleM0Rd__lFQOyAA6ToggleVyACyA16_AA05_FlexsR0VGG_AA012ButtonToggleM0VQo__A30_Qo_A4_GGGA4_GtGGA4_GA39_GA0_GtGGA39_GAaHHPA56_AaHHPyHC_A39_AA0gN0HPyHCHC.62
- _get_witness_table 7SwiftUI15ModifiedContentVyAA6ZStackVyAA9TupleViewVyACyAA06_ShapeG0VyAA7CapsuleV12FeedbackCore0I9FillStyle33_CC3864F153E422CCA8CBAEF59B1A78A1LLVGAA12_FrameLayoutVG_AA012_ConditionalD0VyAA4TextVAWGtGGAA14_OpacityEffectVGAA0G0HPAzAA2_HPyHC_A0_AA0G8ModifierHPyHCHC.5
- _get_witness_table 7SwiftUI5ColorVAA10ShapeStyleHPyHC.6
- _initialize.onceToken
- _isIWorkApp._iWorkApps
- _isIWorkApp.onceToken
- _legalText.onceToken.294
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_didTapDeleteButton
- _objc_msgSend$_setControllerTitle:attachment:
- _objc_msgSend$_setControllerTitle:dedItem:
- _objc_msgSend$_setControllerTitle:url:
- _objc_msgSend$_useAttachmentCellRedesign
- _objc_msgSend$adjustAttachmentLabelSpacing:
- _objc_msgSend$controllerForAttachment:useRedesign:deleteHandler:
- _objc_msgSend$controllerForItem:useRedesign:deleteHandler:
- _objc_msgSend$controllerForUrl:useFallback:useRedesign:deleteHandler:
- _objc_msgSend$controllerForUrl:useRedesign:deleteHandler:
- _objc_msgSend$createResponseURLForBugFormID:appToken:
- _objc_msgSend$createResponseURLForBugFormID:teamID:
- _objc_msgSend$fallbackToOpaqueViewer
- _objc_msgSend$fbkPresetAttachment:fromIndexPath:
- _objc_msgSend$fbkPresetAttachment:fromIndexPath:useRedesign:deleteHandler:
- _objc_msgSend$initWithGroup:
- _objc_msgSend$initWithURL:deleteHandler:
- _objc_msgSend$isDirectory:
- _objc_msgSend$registerAPNSTokenURL
- _objc_msgSend$setAttachment:
- _objc_msgSend$setDisplayName:
- _objc_msgSend$setIssueAreaID:
- _objc_msgSend$setIssueTypeID:
- _objc_msgSend$setShowsIcon:
- _objc_msgSend$setValueTransformer:forName:
- _objc_msgSend$unregisterAPNSTokenURL
- _objc_msgSend$updateFilesBeingCopiedCountCancellable
- _objc_msgSend$updateSuperviewToAttachmentLabelSpacing:
- _objc_msgSend$updateSuperviewToSeparatorSpacing:
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objectdestroy.36Tm
- _symbolic $s12FeedbackCore24FBKBugFormPickerDelegateP
- _symbolic $s12FeedbackCore35FBKAddAttachmentsControllerDelegateP
- _symbolic $s7SwiftUI10ShapeStyleP
- _symbolic _____ 12FeedbackCore16CapsuleFillStyle33_CC3864F153E422CCA8CBAEF59B1A78A1LLV
- _symbolic _____ 12FeedbackCore27AttachmentsBadgeOverlayViewV
- _symbolic _____ 7SwiftUI5ColorV
- _symbolic ______pSgXw 12FeedbackCore24FBKBugFormPickerDelegateP
- _symbolic ______pSgXw 12FeedbackCore35FBKAddAttachmentsControllerDelegateP
- _symbolic _____y__________G 7SwiftUI10_ShapeViewV AA7CapsuleV 12FeedbackCore0E9FillStyle33_CC3864F153E422CCA8CBAEF59B1A78A1LLV
- _symbolic _____y___________y_____y_____y__________G_____G______y_____ALGtGG 7SwiftUI13_VariadicViewO4TreeV AA13_ZStackLayoutV AA05TupleD0V AA15ModifiedContentV AA06_ShapeD0V AA7CapsuleV 12FeedbackCore0L9FillStyle33_CC3864F153E422CCA8CBAEF59B1A78A1LLV AA06_FrameG0V AA012_ConditionalJ0V AA4TextV
- _symbolic _____y_____y__________G_____G 7SwiftUI15ModifiedContentV AA10_ShapeViewV AA7CapsuleV 12FeedbackCore0G9FillStyle33_CC3864F153E422CCA8CBAEF59B1A78A1LLV AA12_FrameLayoutV
- _symbolic _____y_____y__________G_____G______y_____AIGt 7SwiftUI15ModifiedContentV AA10_ShapeViewV AA7CapsuleV 12FeedbackCore0G9FillStyle33_CC3864F153E422CCA8CBAEF59B1A78A1LLV AA12_FrameLayoutV AA012_ConditionalD0V AA4TextV
- _symbolic _____y_____y___________y_____y______y_____G_____ySaySo17FBKQuestionChoiceCGAkDy_____y_____y_____yADyAC_____GG______Qo__AKQo______GGGATGtGG 7SwiftUI6VStackV AA9TupleViewV AA4TextV AA15ModifiedContentV AA09_VariadicE0O4TreeV AA11_LayoutRootV 12FeedbackCore013EvenWidthGridK0V AA7ForEachV AA0E0PAAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AvAE11toggleStyleyQrqd__AA06ToggleX0Rd__lFQO AA0Y0V AA010_FlexFrameK0V AA06ButtonyX0V AA08_PaddingK0V
- _symbolic _____y_____y_____yAAy_____y__________G_____G______y_____AKGtGG_____G 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA06_ShapeG0V AA7CapsuleV 12FeedbackCore0I9FillStyle33_CC3864F153E422CCA8CBAEF59B1A78A1LLV AA12_FrameLayoutV AA012_ConditionalD0V AA4TextV AA14_OpacityEffectV
- _symbolic _____y_____y_____y_____y__________G_____G______y_____AKGtGG 7SwiftUI6ZStackV AA9TupleViewV AA15ModifiedContentV AA06_ShapeE0V AA7CapsuleV 12FeedbackCore0I9FillStyle33_CC3864F153E422CCA8CBAEF59B1A78A1LLV AA12_FrameLayoutV AA012_ConditionalG0V AA4TextV
- _type_layout_string 12FeedbackCore27AttachmentsBadgeOverlayViewV
- _type_layout_string So21NSAttributedStringKeya
CStrings:
+ "%02.2hhX"
+ "APNS token successfully deregistered with API"
+ "APNS token successfully registered with API. Token: %@"
+ "APNSToken"
+ "APNSTokenURL"
+ "Attempted to deregister APNS token without token. This happens if token is not set with -setToken:"
+ "Attempted to register APNS token without token."
+ "Attempting to set token to nil value"
+ "B48@0:8@\"FBKAddAttachmentsController\"16@\"UITableView\"24@\"<UIDropSession>\"32@\"NSIndexPath\"40"
+ "Cannot display file [%{public}@], will fallback to opaque controller"
+ "Error occurred deregistering APNS token with API"
+ "Error occurred registering APNS token with API"
+ "Error requesting permission for remote notifications (potentially due to notifications being disabled for FBA): %{public}@"
+ "FBKAddAttachmentsControllerDelegate"
+ "FBKBugFormPickerDelegate"
+ "FBKLaunchAction %@, action %@, customBehavior: %@"
+ "FBKNotificationManager"
+ "FeedbackCore.FBKEmbeddedAttachmentViewer"
+ "FeedbackCore/FBKEmbeddedAttachmentViewer.swift"
+ "No ID for item shown. Opening app."
+ "No controller to display for file [%{public}@], using opaqueVC"
+ "Not web url"
+ "Parsed web URL [%{public}@] as LaunchAction [%{public}@] with ID [%lld] FFU [%lld]"
+ "Permission for remote notifications granted."
+ "Permission for remote notifications not granted."
+ "QueryDictionary"
+ "Recursion depth limit reached while checking for network error. Possible circular error reference. Error: %@"
+ "Setting APNS token: %@"
+ "Skipping APNS token deregistration - no token available. This is expected if not running in Feedback Assistant app."
+ "Skipping APNS token registration - no token available. This is expected if not running in Feedback Assistant app."
+ "T@\"<FBKBugFormPickerDelegate>\",N,W,VpickerDelegate"
+ "T@\"NSString\",&,N,V_APNSToken"
+ "T@\"UIImageView\",&,N,V_deviceIcon"
+ "TB,N,V_didInitialContentItemFetch"
+ "TB,N,VinteractionEnabled"
+ "TQ,N,V_itemTypeToShow"
+ "Unsupported query item included %@: %@"
+ "Using App Token to start FormResponse with POST body parameters"
+ "["
+ "]"
+ "_APNSToken"
+ "_TtC12FeedbackCore27FBKEmbeddedAttachmentViewer"
+ "_didInitialContentItemFetch"
+ "_finalizeController:attachment:deleteHandler:"
+ "_itemTypeToShow"
+ "actionWithPathAndQueryParams:"
+ "apns_token"
+ "buttonTapped"
+ "centerYAnchor"
+ "constraintEqualToConstant:"
+ "containerView"
+ "controllerForAttachment:deleteHandler:"
+ "controllerForItem:deleteHandler:"
+ "controllerForUrl:"
+ "controllerForUrl:deleteHandler:"
+ "currentNotificationCenter"
+ "deleteAction"
+ "deregisterAPNSWithRequestDictionary:success:error:"
+ "deregisterTokenWithSeedPortal:completion:"
+ "didInitialContentItemFetch"
+ "embeddedViewController"
+ "fbkPresetAttachment:fromIndexPath:deleteHandler:"
+ "fbkPresetAttachmentWithImagePush:fromIndexPath:deleteHandler:"
+ "fbkQueryDictionaryForName:"
+ "feedbackassistant.apple.com"
+ "followup-"
+ "form-response"
+ "fragment"
+ "https://%@%@"
+ "initWithEmbeddedViewController:deleteAction:"
+ "initWithFeedbackAssistantWebURL:"
+ "isNetworkError:"
+ "itemTypeToShow"
+ "macOS"
+ "new-form-response"
+ "news"
+ "notifications"
+ "push_subscription"
+ "recordConsentResponseForConsent:response:completionWithError:"
+ "registerForRemoteNotifications"
+ "registerTokenWithSeedPortal:"
+ "requestAuthorizationWithOptions:completionHandler:"
+ "requestPermission"
+ "requirements updated, no extension found for sysdiagnose requirement [%{public}@]"
+ "setAPNSToken:"
+ "setDidInitialContentItemFetch:"
+ "setItemTypeToShow:"
+ "setToken:"
+ "setupConstraints"
+ "setupViews"
+ "shared"
+ "stringByReplacingCharactersInRange:withString:"
+ "survey-feedback"
+ "team_id"
+ "v16@?0@\"_TtC12FeedbackCore27FBKEmbeddedAttachmentViewer\"8"
+ "v24@0:8@\"FBKAddAttachmentsController\"16"
+ "v24@0:8@\"FBKBugFormPickerController\"16"
+ "v24@?0@\"FBKTeam\"8^B16"
+ "v32@0:8@\"FBKAddAttachmentsController\"16@?<v@?@\"FBKDeviceDiagnosticsController\">24"
+ "v32@0:8@\"FBKBugFormPickerController\"16@\"FBKBugFormStub\"24"
+ "visionOS"
+ "welcome"
- "@40@0:8@16B24B28@?32"
- "A"
- "Cannot display file [%{public}@], will fallback to opaque controller %d"
- "DEFileCell"
- "FBKBugFormFileBrowserTableViewController"
- "FBKFollowupTableCell"
- "FBKImagePickerController"
- "FBKIssueDefinition"
- "FBKIssueType"
- "FBKLaunchAction %@, customBehavior: %@"
- "FBKPushNotificationsEnabled"
- "FBKSecureUnarchiveFromDataTransformer"
- "IssueDefinition"
- "IssueType"
- "T@\"<_TtP12FeedbackCore24FBKBugFormPickerDelegate_>\",N,W,VpickerDelegate"
- "T@\"UIImageView\",W,N,V_deviceIcon"
- "T@\"UILabel\",W,N,V_promptLabel"
- "T@\"UILabel\",W,N,V_responseLabel"
- "TB,N,V_interactionEnabled"
- "Updated attachment with annotation: %s"
- "Using App Token to start FormResponse in: [%@]"
- "_TtP12FeedbackCore24FBKBugFormPickerDelegate_"
- "_TtP12FeedbackCore35FBKAddAttachmentsControllerDelegate_"
- "_deleteButton"
- "_deleteHandler"
- "_didTapDeleteButton"
- "_interactionEnabled"
- "_promptLabel"
- "_responseLabel"
- "_setControllerTitle:attachment:"
- "_setControllerTitle:dedItem:"
- "_setControllerTitle:url:"
- "_useAttachmentCellRedesign"
- "adjustAttachmentLabelSpacing:"
- "allowedTopLevelClasses"
- "cannot display item"
- "com.apple.Keynote"
- "com.apple.Numbers"
- "com.apple.Pages"
- "com.apple.iWork"
- "controllerForAttachment:useRedesign:deleteHandler:"
- "controllerForItem:useRedesign:deleteHandler:"
- "controllerForUrl:useFallback:useRedesign:deleteHandler:"
- "controllerForUrl:useRedesign:deleteHandler:"
- "createResponseURLForBugFormID:appToken:"
- "createResponseURLForBugFormID:teamID:"
- "currentDeviceBugSession"
- "deregisterAPNSWithDeviceToken:success:error:"
- "didTapConnectionButton:"
- "display_name"
- "fallbackToOpaqueViewer"
- "fbkPresetAttachment:fromIndexPath:"
- "fbkPresetAttachment:fromIndexPath:useRedesign:deleteHandler:"
- "fbkPresetAttachmentWithImagePush:fromIndexPath:useRedesign:deleteHandler:"
- "initWithGroup:"
- "initWithURL:deleteHandler:"
- "isIWorkApp"
- "issueAreaID"
- "issueTypeID"
- "issue_file_matchers"
- "issue_type_id"
- "notify/register"
- "notify/unregister"
- "promptLabel"
- "radar_keyword_id"
- "registerAPNSTokenURL"
- "responseLabel"
- "setConnected:"
- "setDisplayName:"
- "setIssueAreaID:"
- "setIssueTypeID:"
- "setPromptLabel:"
- "setResponseLabel:"
- "setValueTransformer:forName:"
- "shouldAutorotate"
- "supportedInterfaceOrientations"
- "tapped no connection icon"
- "unregisterAPNSTokenURL"
- "updateFilesBeingCopiedCountCancellable"
- "v16@?0@\"FBKAttachmentViewerViewController\"8"
- "will display FBK file controller from file browser"
- "will display document on detail view controller from file browser"

```
