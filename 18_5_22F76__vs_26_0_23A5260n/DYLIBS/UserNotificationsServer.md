## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-579.6.4.0.0
-  __TEXT.__text: 0x3a92c
+616.0.1.0.0
+  __TEXT.__text: 0x3812c
   __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_methlist: 0x22d4
-  __TEXT.__const: 0x284
-  __TEXT.__oslogstring: 0x638a
-  __TEXT.__cstring: 0x2077
-  __TEXT.__gcc_except_tab: 0x860
-  __TEXT.__swift5_typeref: 0x382
+  __TEXT.__objc_methlist: 0x223c
+  __TEXT.__const: 0x2b4
+  __TEXT.__oslogstring: 0x625a
+  __TEXT.__cstring: 0x14a7
+  __TEXT.__gcc_except_tab: 0x868
+  __TEXT.__swift5_typeref: 0x38e
   __TEXT.__swift5_fieldmd: 0x9c
   __TEXT.__constg_swiftt: 0x1f0
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_capture: 0x114
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0xd78
+  __TEXT.__unwind_info: 0xd88
   __TEXT.__eh_frame: 0x220
-  __TEXT.__objc_classname: 0x708
-  __TEXT.__objc_methname: 0xbdb2
+  __TEXT.__objc_classname: 0x700
+  __TEXT.__objc_methname: 0xb0bc
   __TEXT.__objc_methtype: 0x19cf
-  __TEXT.__objc_stubs: 0xa1c0
-  __DATA_CONST.__got: 0x910
-  __DATA_CONST.__const: 0x1170
+  __TEXT.__objc_stubs: 0x91c0
+  __DATA_CONST.__got: 0x898
+  __DATA_CONST.__const: 0x1110
   __DATA_CONST.__objc_classlist: 0xe8
-  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d68
+  __DATA_CONST.__objc_selrefs: 0x2980
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x888
-  __AUTH_CONST.__const: 0x5a8
-  __AUTH_CONST.__cfstring: 0x18a0
-  __AUTH_CONST.__objc_const: 0x59e0
+  __AUTH_CONST.__const: 0x5b0
+  __AUTH_CONST.__cfstring: 0xb20
+  __AUTH_CONST.__objc_const: 0x5988
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xd8
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x208
-  __DATA.__data: 0xc90
-  __DATA.__bss: 0x1a
+  __DATA.__data: 0xc50
+  __DATA.__bss: 0xa
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x758
-  __DATA_DIRTY.__data: 0x410
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__data: 0x420
+  __DATA_DIRTY.__bss: 0x60
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore
-  - /System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit
   - /System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices
   - /System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings
   - /System/Library/PrivateFrameworks/UserNotificationsTranslation.framework/UserNotificationsTranslation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D6FCD1C1-1540-3812-9802-09AC19C5A8C0
-  Functions: 1043
-  Symbols:   4363
-  CStrings:  2606
+  UUID: 583543EC-8683-3202-AC9B-699F0D74FC7D
+  Functions: 1032
+  Symbols:   4159
+  CStrings:  2262
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_UNCOneTimeCodeManager
+ _OBJC_CLASS_$_UNSNotificationCommunicationContextService
+ __PROPERTIES_UNSSummaryServiceAdapter
+ ___76-[UNSUserNotificationServer _buildForegroundAction:queue:completionHandler:]_block_invoke.77
+ ___76-[UNSUserNotificationServer _buildForegroundAction:queue:completionHandler:]_block_invoke.79
+ ___76-[UNSUserNotificationServer _buildForegroundAction:queue:completionHandler:]_block_invoke_2.81
+ ___78-[UNSUserNotificationServer performAction:forNotification:inApp:withUserText:]_block_invoke.84
+ ___78-[UNSUserNotificationServer performAction:forNotification:inApp:withUserText:]_block_invoke.84.cold.1
+ ___78-[UNSUserNotificationServer performAction:forNotification:inApp:withUserText:]_block_invoke.85
+ ___block_literal_global.107
+ ___block_literal_global.339
+ ___block_literal_global.68
+ ___block_literal_global.72
+ ___block_literal_global.74
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_UserNotificationsServer
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_UserNotificationsServer
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_UserNotificationsServer
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_UserNotificationsServer
+ _objc_msgSend$_removeStoreForBundleIdentifier:overridePathExtension:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$unc_applicationRecordIfEligibleToDeliverNotificationsForBundleIdentifier:
+ _swift_coroFrameAlloc
+ _symbolic Say______pG So32UNSSummaryServiceAdapterObserverP
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 25UserNotificationsServices0B12NotificationV s5ErrorP
- +[UNCNotificationSourceDescription(Factory) _validEnvironmentFromEnvironment:]
- +[UNCNotificationSourceDescription(Factory) applicationSourceDescriptionWithApplication:]
- +[UNCNotificationSourceDescription(Factory) applicationSourceDescriptionWithBundleIdentifier:]
- +[UNCNotificationSourceDescription(Factory) sourceDescriptionWithBundleIdentifier:]
- +[UNCNotificationSourceDescription(Factory) systemSourceDescriptionWithBundleIdentifier:]
- +[UNCNotificationSourceDescription(Factory) systemSourceDescriptionWithBundleURL:]
- +[UNCNotificationSourceDescription(Factory) systemSourceDirectoryURLs]
- +[UNCNotificationSourceDescription(Factory) systemSourcePathExtension]
- +[UNCNotificationSourceSettingsDescription(Factory) notificationSourceSettingsDescriptionFromDictionary:]
- -[UNCNotificationSourceDescription(Factory) setDefaultCategoriesFromArray:bundle:]
- -[UNCNotificationSourceDescription(Factory) setDefaultTopicsFromArray:bundle:]
- -[UNCNotificationSourceDescription(Factory) setIconFilesFromDictionary:]
- -[UNCNotificationSourceDescription(Factory) setSystemPropertiesFromDictionary:bundle:]
- _APSEnvironmentDemo
- _APSEnvironmentDevelopment
- _APSEnvironmentProduction
- _APSEnvironmentQA2
- _INBundleProxyCanDonateIntent
- _INReadAnnouncementIntentIdentifier
- _INSendMessageIntentIdentifier
- _INStartCallIntentIdentifier
- _OBJC_CLASS_$_BSCFBundle
- _OBJC_CLASS_$_UNCNotificationActionRecord
- _OBJC_CLASS_$_UNCNotificationCategoryRecord
- _OBJC_CLASS_$_UNCNotificationSourceSettingsDescription
- _OBJC_CLASS_$_UNCNotificationTopicRecord
- _OBJC_CLASS_$__UNNotificationCommunicationContextService
- _UIBackgroundModeRemoteNotification
- _UIBackgroundModesKey
- _UNLogCategories
- __OBJC_$_CATEGORY_CLASS_METHODS_UNCNotificationSourceDescription_$_Factory
- __OBJC_$_CATEGORY_CLASS_METHODS_UNCNotificationSourceSettingsDescription_$_Factory
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UNCNotificationSourceDescription_$_Factory
- __OBJC_$_CATEGORY_UNCNotificationSourceDescription_$_Factory
- __OBJC_$_CATEGORY_UNCNotificationSourceSettingsDescription_$_Factory
- ___70+[UNCNotificationSourceDescription(Factory) systemSourceDirectoryURLs]_block_invoke
- ___76-[UNSUserNotificationServer _buildForegroundAction:queue:completionHandler:]_block_invoke.66
- ___76-[UNSUserNotificationServer _buildForegroundAction:queue:completionHandler:]_block_invoke.68
- ___76-[UNSUserNotificationServer _buildForegroundAction:queue:completionHandler:]_block_invoke_2.70
- ___78-[UNCNotificationSourceDescription(Factory) setDefaultTopicsFromArray:bundle:]_block_invoke
- ___78-[UNSUserNotificationServer performAction:forNotification:inApp:withUserText:]_block_invoke.73
- ___78-[UNSUserNotificationServer performAction:forNotification:inApp:withUserText:]_block_invoke.73.cold.1
- ___78-[UNSUserNotificationServer performAction:forNotification:inApp:withUserText:]_block_invoke.74
- ___82-[UNCNotificationSourceDescription(Factory) setDefaultCategoriesFromArray:bundle:]_block_invoke
- ___block_descriptor_32_e18_16?0"NSString"8l
- ___block_descriptor_40_e8_32s_e22_16?0"NSDictionary"8ls32l8
- ___block_literal_global.328
- ___block_literal_global.57
- ___block_literal_global.61
- ___block_literal_global.63
- __kCFBundleDisplayNameKey
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_UserNotificationsServer
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_UserNotificationsServer
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_UserNotificationsServer
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_UserNotificationsServer
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_UserNotificationsServer
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_UserNotificationsServer
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_UserNotificationsServer
- _kCFBundleNameKey
- _kUNNotificationActionTypeDefault
- _objc_msgSend$_validEnvironmentFromEnvironment:
- _objc_msgSend$activityTypes
- _objc_msgSend$appClipMetadata
- _objc_msgSend$appState
- _objc_msgSend$applicationSourceDescriptionWithBundleIdentifier:
- _objc_msgSend$applicationType
- _objc_msgSend$boolValue
- _objc_msgSend$caseInsensitiveCompare:
- _objc_msgSend$entitlementValueForKey:ofClass:
- _objc_msgSend$entitlementValueForKey:ofClass:valuesOfClass:
- _objc_msgSend$fileURLWithPathComponents:
- _objc_msgSend$initWithURL:
- _objc_msgSend$isNewsstandApp
- _objc_msgSend$lastPathComponent
- _objc_msgSend$localizedName
- _objc_msgSend$notificationSourceSettingsDescriptionFromDictionary:
- _objc_msgSend$objectForInfoDictionaryKey:ofClass:
- _objc_msgSend$objectForInfoDictionaryKey:ofClass:inScope:
- _objc_msgSend$objectForInfoDictionaryKey:ofClass:valuesOfClass:
- _objc_msgSend$pathWithComponents:
- _objc_msgSend$plugInKitPlugins
- _objc_msgSend$setActionType:
- _objc_msgSend$setActions:
- _objc_msgSend$setActivityTypes:
- _objc_msgSend$setAllowAlternateLaunchBundleIdentifiers:
- _objc_msgSend$setAllowCalls:
- _objc_msgSend$setAllowCriticalAlerts:
- _objc_msgSend$setAllowIntercom:
- _objc_msgSend$setAllowMessages:
- _objc_msgSend$setAllowPrivateProperties:
- _objc_msgSend$setAllowServiceExtensionFiltering:
- _objc_msgSend$setAllowTimeSensitive:
- _objc_msgSend$setAllowUnlimitedContentBody:
- _objc_msgSend$setAlwaysDisplayNotificationsIndicator:
- _objc_msgSend$setAlwaysShowPreviews:
- _objc_msgSend$setAutomaticallyShowSettings:
- _objc_msgSend$setBundleIdentifier:
- _objc_msgSend$setBundleURL:
- _objc_msgSend$setCarPlayIconFile:
- _objc_msgSend$setDaemonShouldReceiveApplicationEvents:
- _objc_msgSend$setDaemonShouldReceiveBackgroundResponses:
- _objc_msgSend$setDaemonShouldReceiveNotificationSettingsUpdates:
- _objc_msgSend$setDataContainerURL:
- _objc_msgSend$setDefaultCategories:
- _objc_msgSend$setDefaultCategoriesFromArray:bundle:
- _objc_msgSend$setDefaultIconFile:
- _objc_msgSend$setDefaultSettings:
- _objc_msgSend$setDefaultTopics:
- _objc_msgSend$setDefaultTopicsFromArray:bundle:
- _objc_msgSend$setDestructive:
- _objc_msgSend$setDisplayName:
- _objc_msgSend$setEnablesAlerts:
- _objc_msgSend$setEnablesBadges:
- _objc_msgSend$setEnablesCarPlay:
- _objc_msgSend$setEnablesLockScreen:
- _objc_msgSend$setEnablesNotificationCenter:
- _objc_msgSend$setEnablesSounds:
- _objc_msgSend$setForeground:
- _objc_msgSend$setGroupContainerURLS:
- _objc_msgSend$setHasCustomDismissAction:
- _objc_msgSend$setHasCustomSilenceAction:
- _objc_msgSend$setHasFollowActivityAction:
- _objc_msgSend$setHasSystemIcon:
- _objc_msgSend$setHideSettings:
- _objc_msgSend$setIconFilesFromDictionary:
- _objc_msgSend$setIconImageName:
- _objc_msgSend$setIntentIdentifiers:
- _objc_msgSend$setIntentsBundleIdentifier:
- _objc_msgSend$setListPriority:
- _objc_msgSend$setModalAlertStyle:
- _objc_msgSend$setPlayMediaWhenRaised:
- _objc_msgSend$setPresentFullScreenAlertOverList:
- _objc_msgSend$setPreventAutomaticLock:
- _objc_msgSend$setPreventAutomaticRemovalFromRecent:
- _objc_msgSend$setPreventClearFromList:
- _objc_msgSend$setPreventDismissWhenClosed:
- _objc_msgSend$setPrivacyOptionShowSubtitle:
- _objc_msgSend$setPrivacyOptionShowTitle:
- _objc_msgSend$setPrivateBody:
- _objc_msgSend$setProvidesAppNotificationSettings:
- _objc_msgSend$setPushEnvironment:
- _objc_msgSend$setRequiresTopics:
- _objc_msgSend$setRestricted:
- _objc_msgSend$setRevealAdditionalContentWhenPresented:
- _objc_msgSend$setSettingsIconFile:
- _objc_msgSend$setSettingsSheetIconFile:
- _objc_msgSend$setShouldAllowActionsInCarPlay:
- _objc_msgSend$setShouldAllowInCarPlay:
- _objc_msgSend$setShouldAllowPersistentBannersInCarPlay:
- _objc_msgSend$setShouldPreventNotificationDismiss:
- _objc_msgSend$setSubordinateIconFile:
- _objc_msgSend$setSummaryFormat:
- _objc_msgSend$setSupportsAlerts:
- _objc_msgSend$setSupportsBadges:
- _objc_msgSend$setSupportsCarPlay:
- _objc_msgSend$setSupportsContentAvailableRemoteNotifications:
- _objc_msgSend$setSupportsCriticalAlerts:
- _objc_msgSend$setSupportsLockScreen:
- _objc_msgSend$setSupportsNotificationCenter:
- _objc_msgSend$setSupportsProvisionalAlerts:
- _objc_msgSend$setSupportsSounds:
- _objc_msgSend$setSupportsSpoken:
- _objc_msgSend$setSupportsTimeSensitive:
- _objc_msgSend$setSuppressDelayForForwardedNotifications:
- _objc_msgSend$setSuppressDismissActionInCarPlay:
- _objc_msgSend$setSuppressDismissalSync:
- _objc_msgSend$setSuppressIconMask:
- _objc_msgSend$setSuppressUserAuthorizationPrompt:
- _objc_msgSend$setSystemPropertiesFromDictionary:bundle:
- _objc_msgSend$setTextInputButtonTitle:
- _objc_msgSend$setTextInputPlaceholder:
- _objc_msgSend$setUniversalApplicationIdentifier:
- _objc_msgSend$setUrl:
- _objc_msgSend$setUseDefaultDataProvider:
- _objc_msgSend$setUsesCloudKit:
- _objc_msgSend$setWantsEphemeralNotifications:
- _objc_msgSend$setWatchList394hIconFile:
- _objc_msgSend$setWatchList430hIconFile:
- _objc_msgSend$setWatchList448hIconFile:
- _objc_msgSend$setWatchList484hIconFile:
- _objc_msgSend$setWatchListLargeIconFile:
- _objc_msgSend$setWatchListSmallIconFile:
- _objc_msgSend$setWatchQuickLook394hIconFile:
- _objc_msgSend$setWatchQuickLook430hIconFile:
- _objc_msgSend$setWatchQuickLook448hIconFile:
- _objc_msgSend$setWatchQuickLook484hIconFile:
- _objc_msgSend$setWatchQuickLookLargeIconFile:
- _objc_msgSend$setWatchQuickLookSmallIconFile:
- _objc_msgSend$stringByAppendingPathExtension:
- _objc_msgSend$systemSourceDescriptionWithBundleIdentifier:
- _objc_msgSend$un_isFirstPartyIdentifier
- _objc_msgSend$un_safeBoolValue
- _objc_msgSend$unkit_applicationRecordIfEligibleToDeliverNotificationsForBundleIdentifier:
- _swift_bridgeObjectRelease_n
- _symbolic _____y___________pG s6ResultOsRi_zrlE 25UserNotificationsServices0B12NotificationV s5ErrorP
CStrings:
+ "@\"UNSNotificationCommunicationContextService\""
+ "T@\"NSDictionary\",N,C"
+ "T@\"OS_dispatch_queue\",N,R,Vqueue"
+ "UNNotificationObliterateForRadar150366881"
+ "_removeStoreForBundleIdentifier:overridePathExtension:"
+ "boolForKey:"
+ "com.apple.usernotifications"
+ "initWithSuiteName:"
+ "setBool:forKey:"
+ "setQueue_observers:"
+ "unc_applicationRecordIfEligibleToDeliverNotificationsForBundleIdentifier:"
+ "uncplist"
- "@\"_UNNotificationCommunicationContextService\""
- "@16@?0@\"NSDictionary\"8"
- "@16@?0@\"NSString\"8"
- "AppleInternal"
- "Bundles"
- "Error: Category (%{public}@) has an action (%{public}@) whose title key (%{public}@) is mapped to a missing localized string."
- "Factory"
- "NSExtensionPointIdentifier"
- "SBAppUsesLocalNotifications"
- "UNActionAuthenticationRequired"
- "UNActionDestructive"
- "UNActionForeground"
- "UNActionIdentifier"
- "UNActionPreventNotificationDismissal"
- "UNActionSystemIconName"
- "UNActionTemplateIconName"
- "UNActionTextInput"
- "UNActionTextInputButtonTitle"
- "UNActionTextInputPlaceholder"
- "UNActionTitle"
- "UNActionURL"
- "UNAllowAlternateLaunchBundleIdentifiers"
- "UNAllowCalls"
- "UNAllowCriticalAlerts"
- "UNAllowIntercom"
- "UNAllowMessages"
- "UNAllowUnlimitedContentBody"
- "UNAutomaticallyShowSettings"
- "UNCategoryActions"
- "UNCategoryAllowActionsInCarPlay"
- "UNCategoryAllowInCarPlay"
- "UNCategoryAllowPersistentBannersInCarPlay"
- "UNCategoryAlwaysDisplayNotificationsIndicator"
- "UNCategoryBackgroundStyle"
- "UNCategoryCustomDismissAction"
- "UNCategoryCustomSilenceAction"
- "UNCategoryFollowActivityAction"
- "UNCategoryHiddenPreviewsBodyPlaceholder"
- "UNCategoryHiddenPreviewsShowSubtitle"
- "UNCategoryHiddenPreviewsShowTitle"
- "UNCategoryIdentifier"
- "UNCategoryIntentIdentifiers"
- "UNCategoryListPriority"
- "UNCategoryPlayMediaWhenRaised"
- "UNCategoryPresentFullScreenAlertOverList"
- "UNCategoryPreventAutomaticLock"
- "UNCategoryPreventAutomaticRemovalFromRecents"
- "UNCategoryPreventClearFromList"
- "UNCategoryPreventDismissWhenClosed"
- "UNCategoryRevealAdditionalContentWhenPresented"
- "UNCategorySummaryFormat"
- "UNCategorySuppressDelayForForwardedNotifications"
- "UNCategorySuppressDismissActionInCarPlay"
- "UNCategorySuppressPresentationInAmbient"
- "UNCustomSettingsBundle"
- "UNCustomSettingsDetailControllerClass"
- "UNDaemonShouldReceiveApplicationEvents"
- "UNDaemonShouldReceiveBackgroundResponses"
- "UNDaemonShouldReceiveNotificationSettingsUpdates"
- "UNDefaultCategories"
- "UNDefaultSettings"
- "UNDefaultTopics"
- "UNHideSettings"
- "UNIntentsBundleIdentifier"
- "UNNotificationIconCarPlay"
- "UNNotificationIconDefault"
- "UNNotificationIconSettings"
- "UNNotificationIconSettingsSheet"
- "UNNotificationIconSubordinate"
- "UNNotificationIconWatchList394h"
- "UNNotificationIconWatchList448h"
- "UNNotificationIconWatchListLarge"
- "UNNotificationIconWatchListSmall"
- "UNNotificationIconWatchQuickLook394h"
- "UNNotificationIconWatchQuickLook430h"
- "UNNotificationIconWatchQuickLook448h"
- "UNNotificationIconWatchQuickLook484h"
- "UNNotificationIconWatchQuickLookLarge"
- "UNNotificationIconWatchQuickLookSmall"
- "UNNotificationIcons"
- "UNRequiresTopics"
- "UNSettingAlerts"
- "UNSettingAlwaysShowPreviews"
- "UNSettingAnnouncement"
- "UNSettingBadges"
- "UNSettingCarPlay"
- "UNSettingCriticalAlerts"
- "UNSettingLockScreen"
- "UNSettingModalAlertStyle"
- "UNSettingNotificationCenter"
- "UNSettingProvidesAppNotificationSettings"
- "UNSettingSounds"
- "UNSettingSpoken"
- "UNSettingTimeSensitive"
- "UNSupportsProvisionalAlerts"
- "UNSuppressDismissalSync"
- "UNSuppressIconMask"
- "UNSuppressUserAuthorizationPrompt"
- "UNTopicDefaultSettings"
- "UNTopicDisplayName"
- "UNTopicIdentifier"
- "UNUniversalApplicationIdentifier"
- "UNUserNotificationCenter"
- "[%{public}@] Error: App has '%{public}@' entitlement but does not support donating [%{public}@,%{public}@,%{public}@]. Communication API features will be denied to app."
- "_validEnvironmentFromEnvironment:"
- "activityTypes"
- "appClipMetadata"
- "appState"
- "application-identifier"
- "applicationSourceDescriptionWithBundleIdentifier:"
- "applicationType"
- "boolValue"
- "caseInsensitiveCompare:"
- "cloudkit"
- "com.apple."
- "com.apple.developer.icloud-services"
- "com.apple.developer.usernotifications.communication"
- "com.apple.developer.usernotifications.critical-alerts"
- "com.apple.developer.usernotifications.filtering"
- "com.apple.developer.usernotifications.time-sensitive"
- "com.apple.internal.suiautomation"
- "com.apple.watchkit"
- "entitlementValueForKey:ofClass:"
- "entitlementValueForKey:ofClass:valuesOfClass:"
- "fileURLWithPathComponents:"
- "initWithURL:"
- "isNewsstandApp"
- "lastPathComponent"
- "localizedName"
- "newsstand-content"
- "notificationSourceSettingsDescriptionFromDictionary:"
- "objectForInfoDictionaryKey:ofClass:"
- "objectForInfoDictionaryKey:ofClass:inScope:"
- "objectForInfoDictionaryKey:ofClass:valuesOfClass:"
- "pathWithComponents:"
- "plugInKitPlugins"
- "setActionType:"
- "setActions:"
- "setActivityTypes:"
- "setAllowAlternateLaunchBundleIdentifiers:"
- "setAllowCalls:"
- "setAllowCriticalAlerts:"
- "setAllowIntercom:"
- "setAllowMessages:"
- "setAllowPrivateProperties:"
- "setAllowServiceExtensionFiltering:"
- "setAllowTimeSensitive:"
- "setAllowUnlimitedContentBody:"
- "setAlwaysDisplayNotificationsIndicator:"
- "setAlwaysShowPreviews:"
- "setAutomaticallyShowSettings:"
- "setBundleIdentifier:"
- "setBundleURL:"
- "setCarPlayIconFile:"
- "setDaemonShouldReceiveApplicationEvents:"
- "setDaemonShouldReceiveBackgroundResponses:"
- "setDaemonShouldReceiveNotificationSettingsUpdates:"
- "setDataContainerURL:"
- "setDefaultCategories:"
- "setDefaultCategoriesFromArray:bundle:"
- "setDefaultIconFile:"
- "setDefaultSettings:"
- "setDefaultTopics:"
- "setDefaultTopicsFromArray:bundle:"
- "setDestructive:"
- "setDisplayName:"
- "setEnablesAlerts:"
- "setEnablesBadges:"
- "setEnablesCarPlay:"
- "setEnablesLockScreen:"
- "setEnablesNotificationCenter:"
- "setEnablesSounds:"
- "setForeground:"
- "setGroupContainerURLS:"
- "setHasCustomDismissAction:"
- "setHasCustomSilenceAction:"
- "setHasFollowActivityAction:"
- "setHasSystemIcon:"
- "setHideSettings:"
- "setIconFilesFromDictionary:"
- "setIconImageName:"
- "setIntentIdentifiers:"
- "setIntentsBundleIdentifier:"
- "setListPriority:"
- "setModalAlertStyle:"
- "setPlayMediaWhenRaised:"
- "setPresentFullScreenAlertOverList:"
- "setPreventAutomaticLock:"
- "setPreventAutomaticRemovalFromRecent:"
- "setPreventClearFromList:"
- "setPreventDismissWhenClosed:"
- "setPrivacyOptionShowSubtitle:"
- "setPrivacyOptionShowTitle:"
- "setPrivateBody:"
- "setProvidesAppNotificationSettings:"
- "setPushEnvironment:"
- "setRequiresTopics:"
- "setRestricted:"
- "setRevealAdditionalContentWhenPresented:"
- "setSettingsIconFile:"
- "setSettingsSheetIconFile:"
- "setShouldAllowActionsInCarPlay:"
- "setShouldAllowInCarPlay:"
- "setShouldAllowPersistentBannersInCarPlay:"
- "setShouldPreventNotificationDismiss:"
- "setSubordinateIconFile:"
- "setSummaryFormat:"
- "setSupportsAlerts:"
- "setSupportsBadges:"
- "setSupportsCarPlay:"
- "setSupportsContentAvailableRemoteNotifications:"
- "setSupportsCriticalAlerts:"
- "setSupportsLockScreen:"
- "setSupportsNotificationCenter:"
- "setSupportsProvisionalAlerts:"
- "setSupportsSounds:"
- "setSupportsSpoken:"
- "setSupportsTimeSensitive:"
- "setSuppressDelayForForwardedNotifications:"
- "setSuppressDismissActionInCarPlay:"
- "setSuppressDismissalSync:"
- "setSuppressIconMask:"
- "setSuppressUserAuthorizationPrompt:"
- "setSystemPropertiesFromDictionary:bundle:"
- "setTextInputButtonTitle:"
- "setTextInputPlaceholder:"
- "setUniversalApplicationIdentifier:"
- "setUrl:"
- "setUseDefaultDataProvider:"
- "setUsesCloudKit:"
- "setWantsEphemeralNotifications:"
- "setWatchList394hIconFile:"
- "setWatchList430hIconFile:"
- "setWatchList448hIconFile:"
- "setWatchList484hIconFile:"
- "setWatchListLargeIconFile:"
- "setWatchListSmallIconFile:"
- "setWatchQuickLook394hIconFile:"
- "setWatchQuickLook430hIconFile:"
- "setWatchQuickLook448hIconFile:"
- "setWatchQuickLook484hIconFile:"
- "setWatchQuickLookLargeIconFile:"
- "setWatchQuickLookSmallIconFile:"
- "stringByAppendingPathExtension:"
- "systemSourceDescriptionWithBundleIdentifier:"
- "un_isFirstPartyIdentifier"
- "un_safeBoolValue"
- "unkit_applicationRecordIfEligibleToDeliverNotificationsForBundleIdentifier:"

```
