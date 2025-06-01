## GameCenterUICore

> `/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore`

```diff

-818.1.10.2.3
-  __TEXT.__text: 0x25b7c
-  __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x2030
+818.2.24.1.1
+  __TEXT.__text: 0x2a39c
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__objc_methlist: 0x21d8
   __TEXT.__const: 0x4b4
-  __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__cstring: 0x3cf0
+  __TEXT.__gcc_except_tab: 0x1e4
+  __TEXT.__cstring: 0x48e0
   __TEXT.__oslogstring: 0xe
   __TEXT.__dlopen_cstrs: 0xa8
   __TEXT.__constg_swiftt: 0xf8

   __TEXT.__swift5_reflstr: 0x60
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x30
-  __TEXT.__unwind_info: 0x93c
-  __TEXT.__eh_frame: 0x140
-  __TEXT.__objc_classname: 0x3d7
-  __TEXT.__objc_methname: 0x6664
-  __TEXT.__objc_methtype: 0xe6a
-  __TEXT.__objc_stubs: 0x5020
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0xb08
-  __DATA_CONST.__objc_classlist: 0x138
-  __DATA_CONST.__objc_catlist: 0x78
+  __TEXT.__unwind_info: 0xa28
+  __TEXT.__eh_frame: 0x160
+  __TEXT.__objc_classname: 0x41e
+  __TEXT.__objc_methname: 0x6d26
+  __TEXT.__objc_methtype: 0xe94
+  __TEXT.__objc_stubs: 0x53c0
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__const: 0xc78
+  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x31d8
-  __DATA_CONST.__objc_selrefs: 0x1c38
-  __AUTH_CONST.__cfstring: 0x1dc0
-  __AUTH_CONST.__objc_const: 0x1218
-  __AUTH_CONST.__const: 0x530
-  __AUTH_CONST.__auth_got: 0x690
-  __AUTH.__objc_data: 0xc40
+  __DATA_CONST.__objc_const: 0x33c8
+  __DATA_CONST.__objc_selrefs: 0x1db8
+  __AUTH_CONST.__cfstring: 0x1e40
+  __AUTH_CONST.__objc_const: 0x12e8
+  __AUTH_CONST.__const: 0x570
+  __AUTH_CONST.__auth_got: 0x698
+  __AUTH.__objc_data: 0xce0
   __AUTH.__data: 0xc0
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x2e0
+  __DATA.__objc_classrefs: 0x308
   __DATA.__objc_superrefs: 0xb0
-  __DATA.__objc_ivar: 0x154
-  __DATA.__data: 0x490
-  __DATA.__bss: 0x750
+  __DATA.__objc_ivar: 0x160
+  __DATA.__data: 0x5b0
+  __DATA.__bss: 0x770
   __DATA.__common: 0x2
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0B7711A5-058C-3B10-BEE0-7A9918CF459A
-  Functions: 959
-  Symbols:   3295
-  CStrings:  1935
+  UUID: 3C20E128-8532-3C40-AD35-2EDAF6A31304
+  Functions: 1057
+  Symbols:   3458
+  CStrings:  2053
 
Symbols:
+ +[GKAppLevelSignInVisibility didShowBanner]
+ +[GKAppLevelSignInVisibility didShowFullscreen]
+ +[GKAppLevelSignInVisibility fetchAppLevelVisibilityConstraintsWithHandler:]
+ +[GKAppLevelSignInVisibility fetchConfigsWithHandler:]
+ +[GKSignInVisibilityManager(UISingletons) sharedWithoutPersistence]
+ +[GKSignInVisibilityManager(UISingletons) shared]
+ -[GKAppLevelSignInVisibilityData appLevelBannerDisabled]
+ -[GKAppLevelSignInVisibilityData appLevelFullscreenDisabled]
+ -[GKAppLevelSignInVisibilityData processLevelPromptDisabled]
+ -[GKAppLevelSignInVisibilityData setAppLevelBannerDisabled:]
+ -[GKAppLevelSignInVisibilityData setAppLevelFullscreenDisabled:]
+ -[GKAppLevelSignInVisibilityData setProcessLevelPromptDisabled:]
+ -[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBannerWithSignInOrigin:]
+ -[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBannerWithSignInOrigin:].cold.1
+ -[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBannerWithSignInOrigin:].cold.2
+ -[GKLocalPlayer(AuthenticationPrivate) authenticationDidCompleteWithError:signInOrigin:]
+ -[GKLocalPlayer(AuthenticationPrivate) authenticationDidCompleteWithError:signInOrigin:].cold.1
+ -[GKLocalPlayer(AuthenticationPrivate) authenticationDidCompleteWithError:signInOrigin:].cold.2
+ -[GKLocalPlayer(AuthenticationPrivate) authenticationDidCompleteWithError:signInOrigin:].cold.3
+ -[GKLocalPlayer(AuthenticationPrivate) authenticationDidCompleteWithError:signInOrigin:].cold.4
+ -[GKLocalPlayerAuthenticator _handleEditedAuthResponse:error:handler:]
+ -[GKLocalPlayerAuthenticator _shouldDisableWithGlobalDisabled:appLevelDisabled:processLevelDisabled:]
+ GCC_except_table10
+ GCC_except_table23
+ _GKAppLevelSignInBannerLimit
+ _GKAppLevelSignInSheetLimit
+ _GKProcessLevelSignInPromptLimit
+ _GKSignInBannerEnabled
+ _OBJC_CLASS_$_GCUILocalizedStrings
+ _OBJC_CLASS_$_GKAppLevelSignInVisibility
+ _OBJC_CLASS_$_GKAppLevelSignInVisibilityData
+ _OBJC_CLASS_$_GKSignInOriginManager
+ _OBJC_CLASS_$_GKSignInVisibilityConfig
+ _OBJC_CLASS_$_GKSignInVisibilityManager
+ _OBJC_IVAR_$_GKAppLevelSignInVisibilityData._appLevelBannerDisabled
+ _OBJC_IVAR_$_GKAppLevelSignInVisibilityData._appLevelFullscreenDisabled
+ _OBJC_IVAR_$_GKAppLevelSignInVisibilityData._processLevelPromptDisabled
+ _OBJC_METACLASS_$_GCUILocalizedStrings
+ _OBJC_METACLASS_$_GKAppLevelSignInVisibility
+ _OBJC_METACLASS_$_GKAppLevelSignInVisibilityData
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ __CLASS_PROPERTIES_GCUILocalizedStrings
+ __DATA_GCUILocalizedStrings
+ __METACLASS_DATA_GCUILocalizedStrings
+ __OBJC_$_CATEGORY_GKSignInVisibilityManager_$_UISingletons
+ __OBJC_$_CLASS_METHODS_GCUILocalizedStrings
+ __OBJC_$_CLASS_METHODS_GKAppLevelSignInVisibility
+ __OBJC_$_CLASS_METHODS_GKSignInVisibilityManager(UISingletons)
+ __OBJC_$_INSTANCE_METHODS_GCUILocalizedStrings
+ __OBJC_$_INSTANCE_METHODS_GKAppLevelSignInVisibilityData
+ __OBJC_$_INSTANCE_VARIABLES_GKAppLevelSignInVisibilityData
+ __OBJC_$_PROP_LIST_GKAppLevelSignInVisibilityData
+ __OBJC_CLASS_RO_$_GKAppLevelSignInVisibility
+ __OBJC_CLASS_RO_$_GKAppLevelSignInVisibilityData
+ __OBJC_METACLASS_RO_$_GKAppLevelSignInVisibility
+ __OBJC_METACLASS_RO_$_GKAppLevelSignInVisibilityData
+ ___49+[GKSignInVisibilityManager(UISingletons) shared]_block_invoke
+ ___54+[GKAppLevelSignInVisibility fetchConfigsWithHandler:]_block_invoke
+ ___64-[GKLocalPlayerAuthenticator _handleAuthResponse:error:handler:]_block_invoke
+ ___64-[GKLocalPlayerAuthenticator _handleAuthResponse:error:handler:]_block_invoke_2
+ ___67+[GKSignInVisibilityManager(UISingletons) sharedWithoutPersistence]_block_invoke
+ ___75-[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBannerWithSignInOrigin:]_block_invoke
+ ___75-[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBannerWithSignInOrigin:]_block_invoke_2
+ ___76+[GKAppLevelSignInVisibility fetchAppLevelVisibilityConstraintsWithHandler:]_block_invoke
+ ___76+[GKAppLevelSignInVisibility fetchAppLevelVisibilityConstraintsWithHandler:]_block_invoke_2
+ ___76+[GKAppLevelSignInVisibility fetchAppLevelVisibilityConstraintsWithHandler:]_block_invoke_3
+ ___76+[GKAppLevelSignInVisibility fetchAppLevelVisibilityConstraintsWithHandler:]_block_invoke_4
+ ___76+[GKAppLevelSignInVisibility fetchAppLevelVisibilityConstraintsWithHandler:]_block_invoke_5
+ ___76+[GKAppLevelSignInVisibility fetchAppLevelVisibilityConstraintsWithHandler:]_block_invoke_6
+ ___83-[GKLocalPlayer(AuthenticationPrivate) startAuthenticationForExistingPrimaryPlayer]_block_invoke.173
+ ___88-[GKLocalPlayer(AuthenticationPrivate) authenticationDidCompleteWithError:signInOrigin:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e63_v24?0"GKSignInVisibilityConfig"8"GKSignInVisibilityConfig"16ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e11_v16?0B8B12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e40_v16?0"GKAppLevelSignInVisibilityData"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.2
+ _objc_msgSend$_handleEditedAuthResponse:error:handler:
+ _objc_msgSend$_shouldDisableWithGlobalDisabled:appLevelDisabled:processLevelDisabled:
+ _objc_msgSend$_showWelcomeBannerWithSignInOrigin:
+ _objc_msgSend$appLevelBannerDisabled
+ _objc_msgSend$appLevelFullscreenDisabled
+ _objc_msgSend$authenticationDidCompleteWithError:signInOrigin:
+ _objc_msgSend$authenticationShowSignInUIForLocalPlayer:origin:dismiss:
+ _objc_msgSend$bannerConfig
+ _objc_msgSend$dictionary
+ _objc_msgSend$didShowBanner
+ _objc_msgSend$didShowFullscreen
+ _objc_msgSend$fetchAppLevelVisibilityConstraintsWithHandler:
+ _objc_msgSend$fetchConfigsWithHandler:
+ _objc_msgSend$gamePlayerID
+ _objc_msgSend$getStoreBagValuesForKeys:handler:
+ _objc_msgSend$initWithPersistence
+ _objc_msgSend$initWithoutPersistence
+ _objc_msgSend$integerValueFromKey:defaultValue:
+ _objc_msgSend$loginBannerDisabled
+ _objc_msgSend$loginDisabledWithConfig:scope:handler:
+ _objc_msgSend$onboarding
+ _objc_msgSend$processLevelPromptDisabled
+ _objc_msgSend$promptsDisabledWithConfig:scope:handler:
+ _objc_msgSend$recordPageWithID:pageContext:pageType:refApp:
+ _objc_msgSend$setAppLevelBannerDisabled:
+ _objc_msgSend$setAppLevelFullscreenDisabled:
+ _objc_msgSend$setLimit:
+ _objc_msgSend$setLoginBannerDisabled:
+ _objc_msgSend$setLoginDisabled:
+ _objc_msgSend$setProcessLevelPromptDisabled:
+ _objc_msgSend$setShouldPreserveOnboardingUI:
+ _objc_msgSend$sharedWithoutPersistence
+ _objc_msgSend$sheetConfig
+ _objc_msgSend$showOnboardingUIFromViewController:signInOrigin:
+ _objc_msgSend$showSignInBannerForLocalPlayer:completionHandler:
+ _objc_msgSend$stringForOrigin:
+ _sharedWithoutPersistence.onceToken
+ _sharedWithoutPersistence.sharedInstance
- -[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBanner]
- -[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBanner].cold.1
- -[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBanner].cold.2
- -[GKLocalPlayer(AuthenticationPrivate) authenticationDidCompleteWithError:].cold.1
- -[GKLocalPlayer(AuthenticationPrivate) authenticationDidCompleteWithError:].cold.2
- -[GKLocalPlayer(AuthenticationPrivate) authenticationDidCompleteWithError:].cold.3
- -[GKLocalPlayer(AuthenticationPrivate) authenticationDidCompleteWithError:].cold.4
- GCC_except_table21
- _OBJC_CLASS_$__TtC16GameCenterUICore20GCUILocalizedStrings
- _OBJC_METACLASS_$__TtC16GameCenterUICore20GCUILocalizedStrings
- __CLASS_PROPERTIES__TtC16GameCenterUICore20GCUILocalizedStrings
- __DATA__TtC16GameCenterUICore20GCUILocalizedStrings
- __METACLASS_DATA__TtC16GameCenterUICore20GCUILocalizedStrings
- __OBJC_$_CLASS_METHODS__TtC16GameCenterUICore20GCUILocalizedStrings
- __OBJC_$_INSTANCE_METHODS__TtC16GameCenterUICore20GCUILocalizedStrings
- ___58-[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBanner]_block_invoke
- ___58-[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBanner]_block_invoke_2
- ___75-[GKLocalPlayer(AuthenticationPrivate) authenticationDidCompleteWithError:]_block_invoke
- _objc_msgSend$_showWelcomeBanner
- _objc_msgSend$authenticationShowSignInUIForLocalPlayer:dismiss:
- _objc_msgSend$bundleIdentifier
- _objc_msgSend$currentGame
- _objc_msgSend$gamePlayerIDForBundleID:
- _objc_msgSend$recordPageWithID:pageContext:pageType:
- _objc_msgSend$showOnboardingUIFromViewController:
CStrings:
+ "-[GKLocalPlayerAuthenticator _handleEditedAuthResponse:error:handler:]"
+ "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterUI/CommonUI/GKLocalPlayerAuthenticator.m"
+ "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterUI/CommonUI/GKThemeBrush.m"
+ "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterUI/iOS/Framework/GKColorPalette.m"
+ "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterUI/iOS/Framework/GKTextStyle.m"
+ "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterUI/iOS/Framework/GKUIKitAdditions.m"
+ "ACHIEVEMENT_PENDING_APPROVAL"
+ "B28@0:8B16B20B24"
+ "Copy for friends who earned this count is gerater than 3."
+ "Copy for leaderboard list item subtitle when friends are playing."
+ "Copy for when friend earned an achievement days ago"
+ "Copy for when friend earned an achievement hr ago"
+ "Copy for when friend earned an achievement min ago"
+ "Copy for when friend earned an achievement sec ago"
+ "Copy for when friend earned an achievement weeks ago"
+ "DEVELOPER"
+ "Describes to a developer that a leaderboard is not live because it hasn't been approved yet"
+ "Describes to a developer that an achievement is not live because it hasn't been approved yet"
+ "FRIENDS_WHO_HAVE_THIS"
+ "FRIEND_WHO_EARNED_THIS_AVATAR_COUNT"
+ "FRIEND_WHO_EARNED_THIS_AVATAR_COUNTWithCOUNT:"
+ "FRIEND_WHO_EARNED_THIS_DAY_AGO"
+ "FRIEND_WHO_EARNED_THIS_DAY_AGOWithDay:"
+ "FRIEND_WHO_EARNED_THIS_HOUR_AGO"
+ "FRIEND_WHO_EARNED_THIS_HOUR_AGOWithHr:"
+ "FRIEND_WHO_EARNED_THIS_MIN_AGO"
+ "FRIEND_WHO_EARNED_THIS_MIN_AGOWithMin:"
+ "FRIEND_WHO_EARNED_THIS_SECTION_SHOW_LESS_TITLE"
+ "FRIEND_WHO_EARNED_THIS_SECTION_SHOW_MORE_TITLE"
+ "FRIEND_WHO_EARNED_THIS_SEC_AGO"
+ "FRIEND_WHO_EARNED_THIS_SEC_AGOWithSec:"
+ "FRIEND_WHO_EARNED_THIS_WEEK_AGO"
+ "FRIEND_WHO_EARNED_THIS_WEEK_AGOWithWeek:"
+ "Friends Who Have This"
+ "Friends who have this section, title for the button that collapses the list"
+ "Friends who have this section, title for the button that expands the list"
+ "GKAppLevelSignInVisibility"
+ "GKAppLevelSignInVisibilityData"
+ "LEADERBOARD_LIST_ITEM_SUBTITLE_FRIENDS_PLAYING"
+ "LEADERBOARD_LIST_ITEM_SUBTITLE_FRIENDS_PLAYINGWithCOUNT:"
+ "LEADERBOARD_PENDING_APPROVAL"
+ "Nearby Players with the game open and WLAN or Bluetooth turned on will appear above. Don't see people nearby? Try holding the top of this iPhone near another iPhone."
+ "Nearby Players with the game open and Wi-Fi or Bluetooth turned on will appear above. Don't see people nearby? Try holding the top of this iPhone near another iPhone."
+ "PLAYER_PICKER_NEARBY_OR_BOOP_INSTRUCTIONAL_MESSAGE"
+ "PLAYER_PICKER_NEARBY_OR_BOOP_INSTRUCTIONAL_MESSAGE_WLAN"
+ "PRERELEASE_ITEM"
+ "READY_FOR_REVIEW"
+ "Ready for review"
+ "SIGN_IN_BANNER_SUBTITLE"
+ "SIGN_IN_BANNER_TITLE"
+ "Section header for friends who have this achievement list"
+ "Section header on a card for information targeting app develoeprs"
+ "ShowAuthenticationBanner"
+ "Sign in to Game Center"
+ "Sign-in banner subtitle"
+ "Sign-in banner title"
+ "TB,N,V_appLevelBannerDisabled"
+ "TB,N,V_appLevelFullscreenDisabled"
+ "TB,N,V_processLevelPromptDisabled"
+ "This achievement is not yet live, pending submission in App Store Connect."
+ "This leaderboard is not yet live, pending submission in App Store Connect."
+ "Track your scores and achievements"
+ "UISingletons"
+ "Used to indicate an achievement is in the \"Ready for review\" state."
+ "Used to indicate an item (e.g. achievement, leaderboard) is in the \"Pre-release\" state."
+ "_appLevelBannerDisabled"
+ "_appLevelFullscreenDisabled"
+ "_handleEditedAuthResponse:error:handler:"
+ "_processLevelPromptDisabled"
+ "_shouldDisableWithGlobalDisabled:appLevelDisabled:processLevelDisabled:"
+ "_showWelcomeBannerWithSignInOrigin:"
+ "appLevelBannerDisabled"
+ "appLevelFullscreenDisabled"
+ "authenticationDidCompleteWithError:signInOrigin:"
+ "authenticationShowSignInUIForLocalPlayer:origin:dismiss:"
+ "bannerConfig"
+ "dictionary"
+ "didShowBanner"
+ "didShowFullscreen"
+ "fetchAppLevelVisibilityConstraintsWithHandler:"
+ "fetchConfigsWithHandler:"
+ "gamePlayerID"
+ "getStoreBagValuesForKeys:handler:"
+ "initWithPersistence"
+ "initWithoutPersistence"
+ "instructions for searching for nearby or airdrop/boop players in the suggestions shelf"
+ "instructions for searching for nearby players which uses WLAN instead of Wi-Fi for Chinese-config devices or airdrop/boop players in the suggestions shelf"
+ "integerValueFromKey:defaultValue:"
+ "loginBannerDisabled"
+ "loginDisabledWithConfig:scope:handler:"
+ "onboarding"
+ "processLevelPromptDisabled"
+ "promptsDisabledWithConfig:scope:handler:"
+ "recordPageWithID:pageContext:pageType:refApp:"
+ "setAppLevelBannerDisabled:"
+ "setAppLevelFullscreenDisabled:"
+ "setLimit:"
+ "setLoginBannerDisabled:"
+ "setLoginDisabled:"
+ "setProcessLevelPromptDisabled:"
+ "setShouldPreserveOnboardingUI:"
+ "sharedWithoutPersistence"
+ "sheetConfig"
+ "showOnboardingUIFromViewController:signInOrigin:"
+ "showSignInBannerForLocalPlayer:completionHandler:"
+ "stringForOrigin:"
+ "v12@?0B8"
+ "v16@?0@\"GKAppLevelSignInVisibilityData\"8"
+ "v16@?0B8B12"
+ "v24@0:8Q16"
+ "v24@?0@\"GKSignInVisibilityConfig\"8@\"GKSignInVisibilityConfig\"16"
+ "v32@0:8@16Q24"
- "-[GKLocalPlayerAuthenticator _handleAuthResponse:error:handler:]"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/GameCenterUI/CommonUI/GKLocalPlayerAuthenticator.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/GameCenterUI/CommonUI/GKThemeBrush.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/GameCenterUI/iOS/Framework/GKColorPalette.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/GameCenterUI/iOS/Framework/GKTextStyle.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/GameCenterUI/iOS/Framework/GKUIKitAdditions.m"
- "_TtC16GameCenterUICore20GCUILocalizedStrings"
- "_showWelcomeBanner"
- "authenticationShowSignInUIForLocalPlayer:dismiss:"
- "bundleIdentifier"
- "currentGame"
- "gamePlayerIDForBundleID:"
- "recordPageWithID:pageContext:pageType:"
- "showOnboardingUIFromViewController:"

```
