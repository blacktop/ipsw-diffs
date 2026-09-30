## MusicUI

> `/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI`

```diff

-4024.100.124.0.0
-  __TEXT.__text: 0xcbb908
-  __TEXT.__auth_stubs: 0x9b40
-  __TEXT.__objc_methlist: 0xf48
-  __TEXT.__const: 0x45364
+4024.200.3.0.0
+  __TEXT.__text: 0xce4d78
+  __TEXT.__auth_stubs: 0x9e40
+  __TEXT.__objc_methlist: 0xfc0
+  __TEXT.__const: 0x457b4
   __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__cstring: 0x13b36
+  __TEXT.__cstring: 0x14966
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__constg_swiftt: 0x17c14
-  __TEXT.__swift5_typeref: 0x587cc
+  __TEXT.__constg_swiftt: 0x17e74
+  __TEXT.__swift5_typeref: 0x5d93c
   __TEXT.__swift5_builtin: 0x3e8
-  __TEXT.__swift5_reflstr: 0x152cb
-  __TEXT.__swift5_fieldmd: 0x14cb4
-  __TEXT.__swift5_assocty: 0x5e98
-  __TEXT.__swift5_proto: 0x30f4
-  __TEXT.__swift5_types: 0x17a8
-  __TEXT.__swift5_capture: 0x6a6c
-  __TEXT.__swift5_protos: 0x180
+  __TEXT.__swift5_reflstr: 0x1589b
+  __TEXT.__swift5_fieldmd: 0x14fe4
+  __TEXT.__swift5_assocty: 0x5fc8
+  __TEXT.__swift5_proto: 0x30d0
+  __TEXT.__swift5_types: 0x17b4
+  __TEXT.__swift5_capture: 0x6ac4
+  __TEXT.__swift5_protos: 0x17c
   __TEXT.__swift5_mpenum: 0x148
   __TEXT.__oslogstring: 0x85
-  __TEXT.__unwind_info: 0x1a100
-  __TEXT.__eh_frame: 0x1f950
+  __TEXT.__unwind_info: 0x1a720
+  __TEXT.__eh_frame: 0x1ffa8
   __TEXT.__objc_classname: 0x488
-  __TEXT.__objc_methname: 0x598b
+  __TEXT.__objc_methname: 0x5c52
   __TEXT.__objc_methtype: 0x1eda
   __TEXT.__objc_stubs: 0x140
-  __DATA_CONST.__got: 0x2b10
-  __DATA_CONST.__const: 0x3b0
-  __DATA_CONST.__objc_classlist: 0x508
-  __DATA_CONST.__objc_catlist: 0x20
+  __DATA_CONST.__got: 0x2c08
+  __DATA_CONST.__const: 0x3f0
+  __DATA_CONST.__objc_classlist: 0x500
+  __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1740
+  __DATA_CONST.__objc_selrefs: 0x1820
   __DATA_CONST.__objc_protorefs: 0x1d8
-  __AUTH_CONST.__auth_got: 0x4db0
-  __AUTH_CONST.__auth_ptr: 0x8228
-  __AUTH_CONST.__const: 0x2acb8
+  __AUTH_CONST.__auth_got: 0x4f30
+  __AUTH_CONST.__auth_ptr: 0x88d0
+  __AUTH_CONST.__const: 0x2b358
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x13660
-  __AUTH.__objc_data: 0x4120
-  __AUTH.__data: 0x17e30
-  __DATA.__data: 0x1f1c8
-  __DATA.__bss: 0x5c930
-  __DATA.__common: 0x7e0
-  __DATA_DIRTY.__data: 0x90
+  __AUTH_CONST.__objc_const: 0x138a8
+  __AUTH.__objc_data: 0x21a0
+  __AUTH.__data: 0x9570
+  __DATA.__data: 0x151f0
+  __DATA.__bss: 0x42760
+  __DATA.__common: 0x4e0
+  __DATA_DIRTY.__objc_data: 0x2148
+  __DATA_DIRTY.__data: 0x199f8
+  __DATA_DIRTY.__bss: 0x19d80
+  __DATA_DIRTY.__common: 0x398
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices

   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/PhotosUI.framework/PhotosUI
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/WebKit.framework/WebKit

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 39194
-  Symbols:   9578
-  CStrings:  3499
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 39851
+  Symbols:   9942
+  CStrings:  3621
 
Symbols:
+ _MPCloudControllerEnableCloudLibraryOptionMergeWithCloudLibrary
+ _MPCloudControllerEnableCloudLibraryOptionStartInitialImport
+ _MPRestrictionsMonitorAllowsMusicSubscriptionDidChangeNotification
+ _OBJC_CLASS_$_AMSCarrierLinkResult
+ _OBJC_CLASS_$_AMSUIOnboardingFeature
+ _OBJC_CLASS_$_AMSUIPurchaseTask
+ _OBJC_CLASS_$_CCSIconElementRequest
+ _OBJC_CLASS_$_ICLightweightMusicSubscriptionStatusRequest
+ _OBJC_CLASS_$_MPRestrictionsMonitor
+ _SecItemAdd
+ _SecItemCopyMatching
+ _UIAccessibilityAnnouncementNotification
+ _UIAccessibilityPostNotification
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _kSecAttrAccount
+ _kSecAttrServer
+ _kSecClass
+ _kSecClassInternetPassword
+ _kSecMatchLimit
+ _kSecMatchLimitOne
+ _kSecReturnAttributes
+ _kSecReturnData
+ _kSecValueData
+ _swift_task_isCancelled
+ _swift_weakCopyAssign
+ _swift_weakCopyInit
+ _swift_weakTakeAssign
+ _swift_weakTakeInit
- _OBJC_CLASS_$_AMSPurchaseTask
- _swift_initStaticObject
CStrings:
+ " Unified Messages waiting for enablement result."
+ " awaiting disclaimer acknowledgement..."
+ " is not yet defined."
+ " is the same as the selected tabID."
+ " subscription already exists. Skip re-subscribing."
+ ": Could not get UserDefaults suite "
+ "Active user identity changed."
+ "AgeVerificationState changed "
+ "App not bootstrapped yet.  Falling back to results state"
+ "Attempt to purchase a subscription while another purchase attempt is in flight."
+ "Begin observing active user identity changes."
+ "Begin observing subscription status."
+ "Carrier Link failure: "
+ "Carrier Link nil"
+ "Carrier Link success: "
+ "Deferring request with URL "
+ "DialogTask Failed In Music"
+ "Disclaimer acknowledged, fetching "
+ "Dropping lightweight response, active account changed."
+ "Dropping lightweight response, privacy acknowledgement is no longer required."
+ "Enter New Credentials"
+ "GridItemButton"
+ "Home"
+ "MetricsFieldsContext"
+ "MusicUI.PageHostingController"
+ "MusicUI.PresentingViewController"
+ "MusicUI.SubscriptionPurchaseViewModel"
+ "MusicUI/PageNavigation.swift"
+ "MusicUI/SubscriptionPurchaseView.swift"
+ "NoticeManager not present in object graph "
+ "OpenInAppleClassical"
+ "Optional<LegibilityWeight>"
+ "Performing authenticate task..."
+ "Presenting alert dialog task..."
+ "Presenting engagement..."
+ "Privacy disclaimer acknowledgement changed."
+ "Privacy disclaimer acknowledgement required? "
+ "Result failure: "
+ "Result success: "
+ "SocialProfileContextMenuModel"
+ "Stop observing active user identity changes."
+ "Stop observing subscription status."
+ "Subscription Purchase Succeeded."
+ "Subscription Purchase failed with error "
+ "TabChangePublisher"
+ "To favorite music, Sync Library needs to be turned on. Changes to your library will then sync on devices using this Apple Account."
+ "Turn On Sync Library"
+ "Turn on Sync Library to Favorite Music"
+ "Updated user pending followers: '"
+ "Updating from lightweight response."
+ "Use Saved Credentials"
+ "_TtC7MusicUI29SocialProfileContextMenuModel"
+ "_TtC7MusicUI29SubscriptionPurchaseViewModel"
+ "_TtC7MusicUI40SubscriptionContentRestrictionController"
+ "_TtC7MusicUIP33_472952789AFE0556D5F511BA5300504524PresentingViewController"
+ "_TtCV7MusicUI14ChartsPageView19ChartsPagePresenter"
+ "_ageVerificationState"
+ "_chartsPage"
+ "_impressionsTracker"
+ "_isSubscriptionContentRestricted"
+ "_monitor"
+ "_newTitle"
+ "_paymentSheet"
+ "_performBlockAfterCATransactionCommits:"
+ "_restrictionsMonitor"
+ "_stateObservation"
+ "_systemImageNamed:"
+ "_trailingAccessoryButton"
+ "activeUserIdentityDidChangeObserver"
+ "allowMusicSubscriptionDidChange"
+ "allowsMusicSubscription"
+ "appForegrounding"
+ "carrierBundlingStatus"
+ "carrierBundlingStatusType"
+ "catalogPresenter"
+ "chartsPage"
+ "chartsPage"
+ "com.apple.MusicUI.subscriptionContentRestrictionDidChange"
+ "containerBundleIdentifier"
+ "disablePlaybackIndicator"
+ "eligible"
+ "eligibleOffers"
+ "enableCloudLibraryWithOptions:completionHandler:"
+ "enablementTask"
+ "endObservingSubscriptionStatusWithToken:"
+ "findFriendInvite"
+ "handleIconElementRequest:completionHandler:"
+ "hasLightweightProfile"
+ "hideFromProfile"
+ "host"
+ "idle"
+ "init(coder:rootView:)"
+ "init(rootView:)"
+ "initWithImage:titleText:descriptionText:"
+ "initWithIntent:moduleIdentifier:containerBundleIdentifier:moduleSize:"
+ "initWithRequestContext:"
+ "initWithTitleText:features:primaryButtonText:privacyLinkController:"
+ "initialNavigationItem"
+ "isInitialTabSelection"
+ "isPartOfBundle"
+ "isSubscriptionContentRestricted"
+ "isSubscriptionContentRestricted"
+ "isUMCachePolicyEnabled"
+ "launch/umLibraryObservationDelay"
+ "lightweightSubscriptionStatus"
+ "listViewReorderAfter"
+ "listViewReorderBefore"
+ "metricsContext"
+ "mobileiPodDefaults"
+ "musicFriendsProfileFollow"
+ "needsManualVerification"
+ "newTitle"
+ "newTitle"
+ "noPlaylistsFound"
+ "notEligible"
+ "observeUserDefaultsChanges()"
+ "onPresentPaymentSheet"
+ "performAppLaunchRequestIfNeeded"
+ "performRequestWithResponseHandler:"
+ "protectionSpace"
+ "protectionSpaceHost"
+ "publicSocialProfileID"
+ "purchaseFailed"
+ "purchasedSucceeded"
+ "purchasing"
+ "requestIconElementState:completionHandler:"
+ "search-page-list-query"
+ "setChartsPage:"
+ "setIsSubscriptionContentRestricted:"
+ "setModalTransitionStyle:"
+ "setNewTitle:"
+ "setOpaque:"
+ "setUserRequestedSubscriptionHidden:"
+ "setup(objectGraph:)"
+ "sharedRestrictionsMonitor"
+ "square.grid.2x2.fill"
+ "subscriptionContentRestrictionController"
+ "subscriptionContentRestrictionDidChange"
+ "system"
+ "trackContextualAction"
+ "unlinked"
+ "userProfilePendingFollowers"
+ "v16@?0@\"NSError\"8"
+ "v24@?0@\"AMSPurchaseResult\"8@\"NSError\"16"
+ "v24@?0@\"ICLightweightMusicSubscriptionStatusResponse\"8@\"NSError\"16"
+ "v24@?0Q8@\"NSError\"16"
+ "viewDidAppear:"
+ "welcomeFeatureOneDescription"
+ "welcomeFeatureOneTitle"
+ "welcomeFeatureTwoDescription"
+ "welcomeFeatureTwoTitle"
+ "willPerformAction is fired for tabTD "
+ "willPerformAction will not be fired as the tabID "
+ "willPerformAction will not be fired as this is the initial tab selection of "
+ "💬 Attempt to enable Music Recognition."
+ "💬 Failed to enable Music Recognition containerBundleIdentifier "
+ "💬 GDPR has changed - isPrivacyAcknowledgementRequired: "
+ "💬 Missing the containerBundleIdentifier"
+ "💬 Popover should disappear: "
+ "💬 Prewarming popovers: "
+ "💬 Sheet presentation disabled, skipped presenting sheet"
+ "💬 Succeeded to enable Music Recognition for containerBundleIdentifier "
+ "💬 Tab changed, popover should disappear: "
+ "💬 isMusicRecognitionEnabled: "
+ "💬 ┃ Checking for UM enablement in JS..."
+ "💬 ┃ Setting lastNLSQueryDate "
+ "💬 ┃ Unified Messages enabled?: "
+ "💬 ┃ lastNLSQueryDate UserDefaults: "
+ "💬 ┃ ⛔ GDPR has not been accepted; prevent setup and observing for messages."
+ "💬 ┃ 🟢 GDPR was accepted, proceed with checking for enablement."
+ "💬 ┃┃ isSocialOnboardingAllowed? "
+ "💬 ┃┃ mliState UserDefaults: "
+ "💬 ┃┃ mliState changing from "
+ "💬 ┃┃ ⛔ Automation has disabled Unified Messages"
+ "💬 ┃┃ ⛔ GDPR has not been accepted; disallow UM."
+ "💬 ┃┏ Starting "
+ "💬 ┏ Checking GDPR acknowledgement..."
+ "💬 ┗ ⛔ Skipping setup since Unified messages is disabled"
+ "💬 ┗┗ Ending "
+ "💬 ╭ Attempting to make request for: "
+ "💬 ╰ No UM found for "
+ "💬 ╰ No messageRequest for placement: "
+ "💬 ╰ No response for placements "
+ "💬 ╰ Received request for "
+ "💬 ❌ Could not check isMusicRecognitionEnabled for containerBundleIdentifier "
+ "💬 ❌ Error in getting a pending result"
+ "💬 ❌ Failed to check if Unified Messages is enabled, disabling feature: "
+ "💬 ❌ GDPR acceptance required before retrieving mliState."
- " Could not check isCachePolicyEnabled, so setting to false"
- " ObjectGraph never loaded in Unified Messages, exiting"
- " isCachePolicyEnabledFromJS = true"
- "Attempt to enable Music Recognition."
- "Empty Response without error"
- "Error dispatching intent with error: "
- "Error saving genre bubbles because no bubbles were found for page: '"
- "Failed to enable Music Recognition: "
- "ListenNow"
- "MusicUI.OnboardingViewController"
- "MusicUI.SubscriptionPurchaseActionImplementation"
- "MusicUI/OnboardingViewController.swift"
- "Open Finance Error: "
- "Result response: "
- "Sheet presentation disabled, skipped presenting sheet"
- "SubscriptionPurchase"
- "Succeeded to enable Music Recognition: "
- "Unable to increase offset because no visual descriptor was found"
- "_TtC7MusicUI16OnboardingBubble"
- "_TtC7MusicUI23OnboardingPagePresenter"
- "_TtC7MusicUI26PresentationViewController"
- "_TtC7MusicUI35OnboardingResetActionImplementation"
- "_TtC7MusicUI40OnboardingSaveTastesActionImplementation"
- "_TtC7MusicUI45OnboardingShowMoreArtistsActionImplementation"
- "browse / grouping"
- "getEnabledStateOfModuleWithIdentifier:completionHandler:"
- "imageNamed:"
- "initWithHeaderImage:titleText:descriptionText:primaryButtonText:privacyLinkController:"
- "isMusicRecognitionEnabled: "
- "label"
- "onApplyVisualDescriptor"
- "onPresentationReady"
- "onUpdatePhaseChange"
- "onboardingPresenter"
- "onboardingResetAction"
- "onboardingSaveTastesAction"
- "onboardingShowMoreArtistsAction"
- "preference"
- "purchase result error: "
- "purchase result: "
- "radio / grouping"
- "requestEnableModuleWithIdentifier:completionHandler:"
- "search / search_landing"
- "secondaryButtonAction"
- "secondaryButtonTitle"
- "subscription purchase"
- "v16@?0Q8"
- "videos / grouping"
- "visualDescriptor"
- "💬 Attempting to make request for: "
- "💬 Error in getting a pending result"
- "💬 Failed to check if Unified Messages is enabled, disabling feature: "
- "💬 GDPR acceptance required before retrieving mliState."
- "💬 GDPR has not been accepted; disallow UM."
- "💬 GDPR has not been accepted; prevent setup and observing for messages."
- "💬 GDPR was accepted, proceed with checking for enablement."
- "💬 No UM found for "
- "💬 No messageRequest for placement: "
- "💬 No response for placements "
- "💬 ObjectGraph never loaded in Unified Messages, exiting"
- "💬 Received request for "
- "💬 Setting lastNLSQueryDate "
- "💬 Unified Messages enabled?: "
- "💬 isSocialOnboardingAllowed? "
- "💬 lastNLSQueryDate UserDefaults: "
- "💬 mliState UserDefaults: "
- "💬 mliState changing from "

```
