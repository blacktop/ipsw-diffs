## UserNotificationsKit

> `/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit`

```diff

-909.2.20.1.0
-  __TEXT.__text: 0x4892c
-  __TEXT.__auth_stubs: 0x1930
+909.2.26.2.0
+  __TEXT.__text: 0x50dec
+  __TEXT.__auth_stubs: 0x1a40
   __TEXT.__objc_methlist: 0x25ec
-  __TEXT.__const: 0x13e8
-  __TEXT.__cstring: 0x25e8
+  __TEXT.__const: 0x1618
+  __TEXT.__cstring: 0x2ce8
   __TEXT.__gcc_except_tab: 0x1b4
-  __TEXT.__oslogstring: 0x215c
-  __TEXT.__constg_swiftt: 0x970
-  __TEXT.__swift5_typeref: 0x36bc
-  __TEXT.__swift5_reflstr: 0x568
-  __TEXT.__swift5_fieldmd: 0x6a4
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_assocty: 0x1c8
-  __TEXT.__swift5_capture: 0x3bc
-  __TEXT.__swift5_proto: 0x98
-  __TEXT.__swift5_types: 0x80
+  __TEXT.__oslogstring: 0x23cc
+  __TEXT.__constg_swiftt: 0x9a8
+  __TEXT.__swift5_typeref: 0x38cc
+  __TEXT.__swift5_reflstr: 0x60f
+  __TEXT.__swift5_fieldmd: 0x6d8
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_assocty: 0x228
+  __TEXT.__swift5_capture: 0x538
+  __TEXT.__swift5_proto: 0xb8
+  __TEXT.__swift5_types: 0x84
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x10c8
-  __TEXT.__eh_frame: 0x620
+  __TEXT.__unwind_info: 0x1270
+  __TEXT.__eh_frame: 0x7b0
   __TEXT.__objc_classname: 0x57e
-  __TEXT.__objc_methname: 0x8abf
+  __TEXT.__objc_methname: 0x8bc7
   __TEXT.__objc_methtype: 0x1021
   __TEXT.__objc_stubs: 0x4420
-  __DATA_CONST.__got: 0x660
+  __DATA_CONST.__got: 0x708
   __DATA_CONST.__const: 0x498
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ad8
+  __DATA_CONST.__objc_selrefs: 0x1b28
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0xca8
-  __AUTH_CONST.__auth_ptr: 0x518
-  __AUTH_CONST.__const: 0x1438
+  __AUTH_CONST.__auth_got: 0xd30
+  __AUTH_CONST.__auth_ptr: 0x5b8
+  __AUTH_CONST.__const: 0x18a8
   __AUTH_CONST.__cfstring: 0x1920
-  __AUTH_CONST.__objc_const: 0x5910
-  __AUTH.__objc_data: 0x350
-  __AUTH.__data: 0x760
+  __AUTH_CONST.__objc_const: 0x5930
+  __AUTH.__objc_data: 0x358
+  __AUTH.__data: 0x780
   __DATA.__objc_ivar: 0x2dc
-  __DATA.__data: 0x11e8
-  __DATA.__bss: 0x13d8
+  __DATA.__data: 0x12a8
+  __DATA.__bss: 0x17e0
   __DATA.__common: 0x140
   __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__bss: 0x18

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/PrivateFrameworks/Categories.framework/Categories
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1731
-  Symbols:   1358
-  CStrings:  1998
+  Functions: 1867
+  Symbols:   1385
+  CStrings:  2065
 
Symbols:
+ _AnalyticsSendEvent
+ _CTCategoryIdentifierCreativity
+ _CTCategoryIdentifierEducation
+ _CTCategoryIdentifierEntertainment
+ _CTCategoryIdentifierGames
+ _CTCategoryIdentifierHealthAndFitness
+ _CTCategoryIdentifierOther
+ _CTCategoryIdentifierProductivity
+ _CTCategoryIdentifierReadingAndReference
+ _CTCategoryIdentifierShoppingAndFood
+ _CTCategoryIdentifierSocialNetworking
+ _CTCategoryIdentifierSystemBlockable
+ _CTCategoryIdentifierSystemHidden
+ _CTCategoryIdentifierSystemUnblockable
+ _CTCategoryIdentifierTravel
+ _CTCategoryIdentifierUtilities
+ _OBJC_CLASS_$_CTCategory
+ _OBJC_CLASS_$_NSDictionary
+ __swift_stdlib_bridgeErrorToNSError
+ _dispatch_semaphore_create
+ _swift_dynamicCastClass
+ _swift_errorRetain
+ _swift_initStackObject
CStrings:
+ "',reasonToShow='"
+ "<false,neverShown>"
+ "Failed to look up Screen Time Category for bundleId: %!{(MISSING)public}s error: %!@(MISSING)"
+ "Failed to look up iTunes Category for bundleId: %!{(MISSING)public}s error: %!@(MISSING)"
+ "No selection persisted."
+ "NotificationSummarizationOnboardingViewModel decoding: Cannot create 'categorizedSources' from 'categorizedSourcesNSDictionary'"
+ "NotificationSummarizationOnboardingViewModel decoding: Cannot create 'category' from 'categoryInt'"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V2_CONFIRM_TEXT_DISABLED_ALL_APPS"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V2_CONFIRM_TEXT_ENABLED_ALL_APPS"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V2_CONFIRM_TEXT_ENABLED_SOME_APPS"
+ "Should show onboarding experience, '%!{(MISSING)public}s', in '%!{(MISSING)public}s'? %!{(MISSING)bool,public}d. [Force=%!{(MISSING)bool}d OR GreymatterEnabled=%!{(MISSING)bool,public}d && OnboardingEnabled=%!{(MISSING)bool,public}d && (ReasonToReshowOnboarding=%!{(MISSING)public}s) || FreshOnboardingPresentation=%!{(MISSING)bool,public}d)"
+ "Showed Legacy App List UI in "
+ "Unknown Screen Time category: %!{(MISSING)public}s for bundleId: %!{(MISSING)public}s"
+ "Unknown iTunesCategory: %!{(MISSING)public}s for bundleId: %!{(MISSING)public}s"
+ "__swift_setObject:forKeyedSubscript:"
+ "applicationIdentifier"
+ "categorizedSources"
+ "categoryForBundleID:withCompletionHandler:"
+ "com.apple.AppStore"
+ "com.apple.Bridge"
+ "com.apple.DocumentsApp"
+ "com.apple.Fitness"
+ "com.apple.Health"
+ "com.apple.Magnifier"
+ "com.apple.MobileAddressBook"
+ "com.apple.MobileSMS"
+ "com.apple.MobileStore"
+ "com.apple.NotificationSummarizationOnboardingOutcome"
+ "com.apple.Passbook"
+ "com.apple.Preferences"
+ "com.apple.Translate"
+ "com.apple.VoiceMemos"
+ "com.apple.calculator"
+ "com.apple.camera"
+ "com.apple.compass"
+ "com.apple.facetime"
+ "com.apple.findmy"
+ "com.apple.iBooks"
+ "com.apple.measure"
+ "com.apple.mobilecal"
+ "com.apple.mobilemail"
+ "com.apple.mobilenotes"
+ "com.apple.mobilephone"
+ "com.apple.mobilesafari"
+ "com.apple.mobileslideshow"
+ "com.apple.mobiletimer"
+ "com.apple.podcasts"
+ "com.apple.reminders"
+ "com.apple.shortcuts"
+ "com.apple.stocks"
+ "com.apple.weather"
+ "com.google.Dynamite"
+ "com.google.Gmail"
+ "com.microsoft.Office.Outlook"
+ "com.microsoft.skype.teams"
+ "com.tinyspeck.chatlyio"
+ "com.yahoo.Aerogram"
+ "com.yahoo.finance"
+ "communicationAndSocial"
+ "could not load icon for %!{(MISSING)public}s"
+ "genreIdentifier"
+ "iTunesMetadata"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithUnsignedInteger:"
+ "majorBuildLetterString"
+ "majorBuildNumber"
+ "minorBuildNumber"
+ "net.whatsapp.WhatsAppSMB"
+ "newsAndEntertainment"
+ "v24@?0@\"CTCategory\"8@\"NSError\"16"
- "<true,neverShown>"
- "Should show onboarding experience, '%!{(MISSING)public}s', in '%!{(MISSING)public}s'? %!{(MISSING)bool,public}d. [Force=%!{(MISSING)bool}d OR GreymatterEnabled=%!{(MISSING)bool,public}d && OnboardingEnabled=%!{(MISSING)bool,public}d && OnboardingNotCompleted=%!{(MISSING)public}s)"
- "couldn't not icon for %!{(MISSING)public}s"

```
