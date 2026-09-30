## com.apple.podcasts.appremoval

> `/System/Library/AppRemovalServices/com.apple.podcasts.appremoval.xpc/com.apple.podcasts.appremoval`

```diff

-4024.400.4.0.0
-  __TEXT.__text: 0x5dec
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x1560
-  __TEXT.__objc_methlist: 0x7bc
-  __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x379
-  __TEXT.__objc_methname: 0x2282
+4024.500.57.0.0
+  __TEXT.__text: 0x5284
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_stubs: 0x1300
+  __TEXT.__objc_methlist: 0x9cc
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x2a9
+  __TEXT.__objc_methname: 0x1ec0
   __TEXT.__oslogstring: 0x33c
-  __TEXT.__objc_classname: 0x1bb
-  __TEXT.__objc_methtype: 0x76c
-  __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__ustring: 0x20
+  __TEXT.__objc_classname: 0x188
+  __TEXT.__objc_methtype: 0x6c2
+  __TEXT.__gcc_except_tab: 0x1b4
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x220
-  __DATA_CONST.__auth_got: 0x2f8
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x3d0
-  __DATA_CONST.__cfstring: 0x440
-  __DATA_CONST.__objc_classlist: 0x48
+  __TEXT.__ustring: 0x20
+  __TEXT.__unwind_info: 0x1e0
+  __DATA_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__const: 0x300
+  __DATA_CONST.__cfstring: 0x3c0
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x1ee8
-  __DATA.__objc_selrefs: 0x7c0
-  __DATA.__objc_ivar: 0x84
-  __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x360
-  __DATA.__bss: 0x50
+  __DATA.__objc_const: 0x1760
+  __DATA.__objc_selrefs: 0x7b0
+  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_data: 0x280
+  __DATA.__data: 0x300
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait
   - /System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation
-  - /System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 193
-  Symbols:   182
-  CStrings:  524
+  Functions: 166
+  Symbols:   162
+  CStrings:  469
 
Symbols:
+ _com_apple_podcasts_appremovalVersionNumber
+ _com_apple_podcasts_appremovalVersionString
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFNotificationCenterPostNotification
- _CFPreferencesCopyAppValue
- _CFPreferencesSetAppValue
- _NSStringFromClass
- _OBJC_CLASS_$_INPlayMediaIntent
- _OBJC_CLASS_$_MTIntentDonationUtil
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSUserDefaults
- _OBJC_CLASS_$_PUIObjCArtworkProvider
- _OBJC_CLASS_$_UIImage
- _OBJC_METACLASS_$_MTIntentDonationUtil
- _SiriPodcastsErrorDomain
- _UIImageJPEGRepresentation
- _dispatch_after
- _dispatch_queue_attr_make_with_autorelease_frequency
- _dispatch_queue_attr_make_with_qos_class
- _dispatch_time
- _kMTIntentsArtworkSize
- _kMTShowSiriSuggestionsKey
- _objc_release_x1
CStrings:
+ "promptAccountAuthenticationWithDebugReason:forced:"
+ "v28@0:8@\"NSString\"16B24"
+ "v28@0:8@16B24"
- "\x05"
- "#"
- "@\"<MTPlaybackIdentifierComposing>\""
- "@\"MTDefaultsChangeNotifier\""
- "@\"NSMutableDictionary\""
- "AppCanShowSiriSuggestionsBlacklist"
- "B24@0:8@\"NSString\"16"
- "MTIntentDonationUtil"
- "MTIntentDonationUtil.donation_queue"
- "MTSiriIntentDonationService"
- "SiriPodcastsErrorDomain"
- "T#,&,N,V_interactionClass"
- "T@\"<MTPlaybackIdentifierComposing>\",&,N,V_identifierComposer"
- "T@\"MTDefaultsChangeNotifier\",&,N,V_defaultsObserver"
- "T@\"NSMutableDictionary\",&,N,V_cachedScores"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_donationQueue"
- "_applePodcastsFoundationSettingsUserDefaults"
- "_cachedScores"
- "_defaultsObserver"
- "_donationQueue"
- "_identifierComposer"
- "_interactionClass"
- "artworkPathForShow:size:completionHandler:"
- "boolForKey:"
- "boolValue"
- "cachedScores"
- "canContinueIntentWithUserActivityType:"
- "com.apple.suggestions"
- "com.apple.suggestions.settingsChanged"
- "dataWithContentsOfURL:"
- "defaultPodcastArtwork"
- "defaultPodcastArtworkData"
- "defaultsObserver"
- "donateEpisodeUuid:stationUuid:isPlaybackFromSiri:completion:"
- "donationQueue"
- "identifierComposer"
- "interactionClass"
- "mutableCopy"
- "prepareImageDataForPodcastUuid:completion:"
- "removeAllDonations"
- "removeDonationForEpisodeUuid:"
- "removeDonationForPodcastUuid:"
- "removeDonationsForEpisodeUuids:"
- "removeDonationsForPodcastUuids:"
- "removeObject:"
- "setCachedScores:"
- "setDefaultsObserver:"
- "setDonationQueue:"
- "setIdentifierComposer:"
- "setInteractionClass:"
- "setWithArray:"
- "shared"
- "v24@0:8#16"
- "v24@0:8@\"NSArray\"16"
- "v24@?0@\"NSURL\"8@\"NSError\"16"
- "v32@?0@\"NSString\"8@16@24"
- "v44@0:8@\"NSString\"16@\"NSString\"24B32@?<v@?B>36"
- "v44@0:8@16@24B32@?36"

```
