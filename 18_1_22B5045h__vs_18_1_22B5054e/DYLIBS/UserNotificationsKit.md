## UserNotificationsKit

> `/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit`

```diff

-909.2.15.1.0
-  __TEXT.__text: 0x3e294
-  __TEXT.__auth_stubs: 0x1750
-  __TEXT.__objc_methlist: 0x250c
-  __TEXT.__const: 0x1008
-  __TEXT.__cstring: 0x20b8
+909.2.20.1.0
+  __TEXT.__text: 0x4892c
+  __TEXT.__auth_stubs: 0x1930
+  __TEXT.__objc_methlist: 0x25ec
+  __TEXT.__const: 0x13e8
+  __TEXT.__cstring: 0x25e8
   __TEXT.__gcc_except_tab: 0x1b4
-  __TEXT.__oslogstring: 0x1d6c
-  __TEXT.__constg_swiftt: 0x77c
-  __TEXT.__swift5_typeref: 0x234a
-  __TEXT.__swift5_reflstr: 0x42a
-  __TEXT.__swift5_fieldmd: 0x4f0
+  __TEXT.__oslogstring: 0x215c
+  __TEXT.__constg_swiftt: 0x970
+  __TEXT.__swift5_typeref: 0x36bc
+  __TEXT.__swift5_reflstr: 0x568
+  __TEXT.__swift5_fieldmd: 0x6a4
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_assocty: 0x138
-  __TEXT.__swift5_capture: 0x358
-  __TEXT.__swift5_proto: 0x78
-  __TEXT.__swift5_types: 0x64
+  __TEXT.__swift5_assocty: 0x1c8
+  __TEXT.__swift5_capture: 0x3bc
+  __TEXT.__swift5_proto: 0x98
+  __TEXT.__swift5_types: 0x80
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xf80
-  __TEXT.__eh_frame: 0x998
-  __TEXT.__objc_classname: 0x566
-  __TEXT.__objc_methname: 0x88bc
-  __TEXT.__objc_methtype: 0xff9
-  __TEXT.__objc_stubs: 0x4360
-  __DATA_CONST.__got: 0x620
-  __DATA_CONST.__const: 0x450
+  __TEXT.__unwind_info: 0x10c8
+  __TEXT.__eh_frame: 0x620
+  __TEXT.__objc_classname: 0x57e
+  __TEXT.__objc_methname: 0x8abf
+  __TEXT.__objc_methtype: 0x1021
+  __TEXT.__objc_stubs: 0x4420
+  __DATA_CONST.__got: 0x660
+  __DATA_CONST.__const: 0x498
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a40
-  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_selrefs: 0x1ad8
+  __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0xbb8
-  __AUTH_CONST.__auth_ptr: 0x440
-  __AUTH_CONST.__const: 0x1070
-  __AUTH_CONST.__cfstring: 0x17e0
-  __AUTH_CONST.__objc_const: 0x5668
-  __AUTH.__objc_data: 0x330
-  __AUTH.__data: 0x6d0
-  __DATA.__objc_ivar: 0x2cc
-  __DATA.__data: 0xdd8
-  __DATA.__bss: 0xf98
-  __DATA.__common: 0xc0
+  __AUTH_CONST.__auth_got: 0xca8
+  __AUTH_CONST.__auth_ptr: 0x518
+  __AUTH_CONST.__const: 0x1438
+  __AUTH_CONST.__cfstring: 0x1920
+  __AUTH_CONST.__objc_const: 0x5910
+  __AUTH.__objc_data: 0x350
+  __AUTH.__data: 0x760
+  __DATA.__objc_ivar: 0x2dc
+  __DATA.__data: 0x11e8
+  __DATA.__bss: 0x13d8
+  __DATA.__common: 0x140
   __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__bss: 0x18
   __DATA_DIRTY.__common: 0x48

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
+  - /System/Library/Frameworks/Symbols.framework/Symbols
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1547
-  Symbols:   1341
-  CStrings:  1914
+  Functions: 1731
+  Symbols:   1358
+  CStrings:  1998
 
Symbols:
+ OBJC_IVAR_$_NCNotificationRequest._summaryStatus
+ OBJC_IVAR_$_NCNotificationRequest._isPresentedAsBanner
+ _memset
+ _swift_makeBoxUnique
+ OBJC_IVAR_$_NCNotificationRequest._priorityStatus
+ _swift_deallocPartialClassInstance
+ OBJC_IVAR_$_NCNotificationRequest._isRemoved
- _swift_unknownObjectWeakAssign
- _swift_asyncLet_get_throwing
- _swift_asyncLet_begin
- _swift_asyncLet_finish
- _swift_asyncLet_get
- _swift_dynamicCastClass
CStrings:
+ "isRemoved"
+ "v24@0:8@\"NSCoder\"16"
+ "NotificationSummarizationOnboardingViewModel decoding: Cannot get 'topSourcesIndexesNSArray'"
+ "TB,N,V_isPresentedAsBanner"
+ "NotificationSummarizationOnboardingViewModel decoding: Cannot create 'isSummarizationEnabledByIndex' from 'isSummarizationEnabledByIndexNSArray' with count '%!{(MISSING)public}ld'"
+ "objectAtIndexedSubscript:"
+ "isPriority"
+ "_summaryStatusLoggingDescription"
+ "_summaryStatus"
+ "init(view:title:subtitle:primaryAction:secondaryAction:linkAction:backAction:)"
+ "initWithArray:"
+ "NotificationSummarizationOnboardingViewModel decoding: Cannot create 'sources' from 'sourcesNSArray' with count '%!{(MISSING)public}ld'"
+ "summarized"
+ "topSourcesIndexes"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V2_CATEGORY_COMMUNICATION"
+ "boolValue"
+ "ineligible"
+ "initWithInteger:"
+ "primaryButtonPressed"
+ "\n\x1f\x01!A\x11"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V1_CONFIRM_TEXT"
+ "sources"
+ "setPriorityStatus:"
+ "initWithBool:"
+ "NSCoding"
+ "Contradictory frame constraints specified."
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V2_CATEGORY_OTHER"
+ "Tq,N,R"
+ "allowedClassesForExperience:"
+ "integerValue"
+ "TQ,R,N,V_summaryStatus"
+ "NSSecureCoding"
+ "notificationFrequency"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V2_PRIVACY_TEXT"
+ "@24@0:8@\"NSCoder\"16"
+ "_priorityStatus"
+ "TB,R"
+ "_isPresentedAsBanner"
+ "couldn't not icon for %!{(MISSING)public}s"
+ "supportsSecureCoding"
+ "isNotPriority"
+ "setIsPresentedAsBanner:"
+ "setSummaryStatus:"
+ "isSummarizationEnabledByIndex"
+ "sourcesSortMethod"
+ "GreymatterOnboardingWithAppCategorization"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V1_ORDERING_TEXT"
+ "_isRemoved"
+ "summaryStatus"
+ "error"
+ "_priorityStatusLoggingDescription"
+ "primaryAction"
+ "TB,N,R"
+ "@24@0:8^v16"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V1_CANCEL_TEXT"
+ "_selectedCategories"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V2_CATEGORY_NEWS"
+ "secondaryAction"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V1_DETAIL"
+ "primaryButtonPressed()"
+ "checkmark.circle.fill"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V2_TITLE"
+ "SUMMARIZATION_ONBOARDING_INTRO_CONFIRM_TEXT_V1"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V2_CONFIRM_TEXT_NO_SELECTION"
+ "Action not implemented for '%!{(MISSING)public}s'"
+ "should never call loadImage(for:completion) where request.source is nil. use placeholder(...) instead"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V2_CATEGORY_NONE"
+ "SUMMARIZATION_ONBOARDING_INTRO_CONFIRM_TEXT_V2"
+ "alphabetical"
+ "encodeWithCoder:"
+ "inferenceTimedOut"
+ "TQ,R,N,V_priorityStatus"
+ "T@\"UITraitCollection\",N,R"
+ "NotificationSummarizationOnboardingViewModel decoding: Cannot create 'topSourcesIndexes' from 'topSourcesIndexesNSArray' with count '%!{(MISSING)public}ld'"
+ "isPresentedAsBanner"
+ "NotificationSummarizationOnboardingViewModel decoding: Cannot create 'sortMethod' from 'sortMethodRawValue' with value '%!{(MISSING)public}@'"
+ "id: %!@(MISSING); section: %!@(MISSING); thread: %!@(MISSING); category: %!@(MISSING); timestamp: %!@(MISSING); interruption-level: %!@(MISSING); priorityStatus: %!@(MISSING); summaryStatus: %!@(MISSING); relevance-score: %!f(MISSING); filter-criteria: %!@(MISSING); actions: [ %!@(MISSING) ]; destinations: [ %!@(MISSING) ]"
+ "backButtonPressed()"
+ "NotificationSummarizationOnboardingViewModel decoding: Cannot get 'sortMethodRawValue'"
+ "_isSummarizationEnabledByIndex"
+ "priorityStatus"
+ "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_V1_TITLE"
+ "backAction"
+ "linkAction"
+ "setIsRemoved:"
+ "secondaryButtonPressed"
+ "secondaryButtonPressed()"
+ "encodeObject:forKey:"
+ "TB,N,V_isRemoved"
- "_isSourceEnabled"
- "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_ORDERING_TEXT"
- "_topSources"
- "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_TITLE"
- "start animating (allowAnimations)"
- "_sources"
- "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_CONFIRM_TEXT"
- "\n\x1f\x01!!\x11"
- "confirmButtonPressed"
- "cancelButtonPressed"
- "id: %!@(MISSING); section: %!@(MISSING); thread: %!@(MISSING); category: %!@(MISSING); timestamp: %!@(MISSING); interruption-level: %!@(MISSING); relevance-score: %!f(MISSING); filter-criteria: %!@(MISSING); actions: [ %!@(MISSING) ]; destinations: [ %!@(MISSING) ]"
- "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_CANCEL_TEXT"
- "SUMMARIZATION_ONBOARDING_CUSTOMIZATION_DETAIL"
- "setOverrideUserInterfaceStyle:"
- "SUMMARIZATION_ONBOARDING_INTRO_CONFIRM_TEXT"

```
