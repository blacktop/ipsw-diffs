## GameCenterUI_x86Support

> `/System/Library/PrivateFrameworks/GameCenterUI.framework/Versions/A/GameCenterUI_x86Support`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_ret`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-821.0.20.0.0
-  __TEXT.__text: 0xa3e4
-  __TEXT.__objc_methlist: 0xe90
-  __TEXT.__cstring: 0x863
-  __TEXT.__const: 0x250
-  __TEXT.__oslogstring: 0x1e4
+821.0.25.0.0
+  __TEXT.__text: 0xd5a0
+  __TEXT.__objc_methlist: 0xf78
+  __TEXT.__cstring: 0x963
+  __TEXT.__const: 0x2c2
+  __TEXT.__oslogstring: 0x219
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__swift5_typeref: 0x1a5
-  __TEXT.__swift5_capture: 0x120
+  __TEXT.__swift5_typeref: 0x1e2
+  __TEXT.__swift5_capture: 0x204
   __TEXT.__swift5_fieldmd: 0xcc
   __TEXT.__constg_swiftt: 0x158
   __TEXT.__swift5_reflstr: 0x6b
   __TEXT.__swift5_types: 0x14
-  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__swift_as_cont: 0x14
-  __TEXT.__unwind_info: 0x480
-  __TEXT.__eh_frame: 0x2b0
-  __TEXT.__objc_stubs: 0x1440
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_classname: 0x459
-  __TEXT.__objc_methname: 0x2891
-  __TEXT.__objc_methtype: 0x935
-  __DATA_CONST.__const: 0x168
-  __DATA_CONST.__objc_classlist: 0x90
+  __TEXT.__swift_as_cont: 0x28
+  __TEXT.__unwind_info: 0x598
+  __TEXT.__eh_frame: 0x500
+  __TEXT.__objc_stubs: 0x1ac0
+  __TEXT.__auth_stubs: 0x880
+  __TEXT.__objc_classname: 0x499
+  __TEXT.__objc_methname: 0x2d1b
+  __TEXT.__objc_methtype: 0x985
+  __DATA_CONST.__const: 0x180
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa00
+  __DATA_CONST.__objc_selrefs: 0xb48
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x78
-  __DATA_CONST.__got: 0x228
-  __AUTH_CONST.__const: 0x508
-  __AUTH_CONST.__cfstring: 0x660
-  __AUTH_CONST.__objc_const: 0x23d8
+  __DATA_CONST.__got: 0x270
+  __AUTH_CONST.__const: 0x7a0
+  __AUTH_CONST.__cfstring: 0x780
+  __AUTH_CONST.__objc_const: 0x2818
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x448
-  __AUTH.__objc_data: 0x680
+  __AUTH_CONST.__auth_got: 0x450
+  __AUTH.__objc_data: 0x6d0
   __AUTH.__data: 0x158
-  __DATA.__objc_ivar: 0xb8
-  __DATA.__data: 0x350
-  __DATA.__bss: 0x30
+  __DATA.__objc_ivar: 0xc0
+  __DATA.__data: 0x3b0
+  __DATA.__bss: 0x31
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xc8
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 438
-  Symbols:   920
-  CStrings:  619
+  Functions: 515
+  Symbols:   1039
+  CStrings:  678
 
Symbols:
+ +[GKNotificationBanner isBannerVisible]
+ +[GKRosettiniEventDelivery deliverReceivedTurnEventForMatch:didBecomeActive:]
+ +[GKRosettiniEventDelivery deliverWantsToPlayChallenge:]
+ +[GKRosettiniEventDelivery deliverWantsToQuitMatch:]
+ -[GKAccessPoint gameCenterViewControllerDidFinish:]
+ -[GKAccessPoint presentDashboard:handler:]
+ -[GKAccessPoint presentedDashboard]
+ -[GKAccessPoint setPresentedDashboard:]
+ -[GKGameCenterViewController dashboardPlayerID]
+ -[GKGameCenterViewController setDashboardPlayerID:]
+ -[GKGameCenterViewController viewDidAppear]
+ -[GKLocalPlayer(LegacyAuthX86Support) startLegacyAuthenticationWithCompletionHandler:]
+ -[GKPlayer(UI_Rosettini) _rosettiniLoadPhotoForSize:withCompletionHandler:]
+ -[GKPlayer(UI_Rosettini) _rosettiniPlaceholderPhoto]
+ OBJC_IVAR_$_GKAccessPoint._presentedDashboard
+ OBJC_IVAR_$_GKGameCenterViewController._dashboardPlayerID
+ _GKGetLocalizedStringFromTableInBundle
+ _GKSignInBannerEnabled
+ _OBJC_CLASS_$_GKChallengeEventHandler
+ _OBJC_CLASS_$_GKDaemonProxy
+ _OBJC_CLASS_$_GKRosettiniEventDelivery
+ _OBJC_CLASS_$_NSAlert
+ _OBJC_METACLASS_$_GKRosettiniEventDelivery
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
+ __OBJC_$_CLASS_METHODS_GKRosettiniEventDelivery
+ __OBJC_$_INSTANCE_METHODS_GKLocalPlayer(AuthenticationExtras_Rosettini|LegacyAuthX86Support)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GKGameCenterControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GKGameCenterControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_GKGameCenterControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_GKAccessPoint
+ __OBJC_CLASS_RO_$_GKRosettiniEventDelivery
+ __OBJC_LABEL_PROTOCOL_$_GKGameCenterControllerDelegate
+ __OBJC_METACLASS_RO_$_GKRosettiniEventDelivery
+ __OBJC_PROTOCOL_$_GKGameCenterControllerDelegate
+ ___65-[GKPlayer(UI_Rosettini) loadPhotoForSize:withCompletionHandler:]_block_invoke_2
+ ___75-[GKPlayer(UI_Rosettini) _rosettiniLoadPhotoForSize:withCompletionHandler:]_block_invoke
+ ___75-[GKPlayer(UI_Rosettini) _rosettiniLoadPhotoForSize:withCompletionHandler:]_block_invoke_2
+ ___77-[GKLocalPlayer(AuthenticationExtras_Rosettini) showCancelledAlertForPlayer:]_block_invoke
+ ___80-[GKLocalPlayer(AuthenticationExtras_Rosettini) alertUserInStoreDemoModeEnabled]_block_invoke
+ ___86-[GKLocalPlayer(LegacyAuthX86Support) startLegacyAuthenticationWithCompletionHandler:]_block_invoke
+ ___98-[GKLocalPlayer(AuthenticationExtras_Rosettini) showSignInBannerForLocalPlayer:completionHandler:]_block_invoke
+ ___NSDictionary0__struct
+ ___block_descriptor_40_e8_32bs_e38_v24?0"NSViewController"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e16_v16?0"NSData"8l
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8l
+ __swift_closure_destructor.34Tm
+ _objc_msgSend$_gkIsEligibleForOnboardingUI
+ _objc_msgSend$_rosettiniLoadPhotoForSize:withCompletionHandler:
+ _objc_msgSend$_rosettiniPlaceholderPhoto
+ _objc_msgSend$accountService
+ _objc_msgSend$addButtonWithTitle:
+ _objc_msgSend$baseLeaderboardID
+ _objc_msgSend$beginSheetModalForWindow:completionHandler:
+ _objc_msgSend$dashboardPlayerID
+ _objc_msgSend$deliverReceivedTurnEventForMatch:didBecomeActive:
+ _objc_msgSend$deliverWantsToPlayChallenge:
+ _objc_msgSend$deliverWantsToQuitMatch:
+ _objc_msgSend$didShowSignInBanner
+ _objc_msgSend$didShowWelcomeBannerInOverlayWithNewUserState:uponReturnToForeground:
+ _objc_msgSend$dismissOnboardingUIIfPresent
+ _objc_msgSend$displayNameWithOptions:
+ _objc_msgSend$eventEmitter
+ _objc_msgSend$getStoreBagValuesForKeys:handler:
+ _objc_msgSend$hideAccessPoint
+ _objc_msgSend$initWithAchievementID:
+ _objc_msgSend$initWithLeaderboardID:playerScope:timeScope:
+ _objc_msgSend$initWithLeaderboardSetID:
+ _objc_msgSend$initWithPlayer:
+ _objc_msgSend$initWithState:
+ _objc_msgSend$integerValueFromKey:defaultValue:
+ _objc_msgSend$isBannerVisible
+ _objc_msgSend$isNewToGameCenter
+ _objc_msgSend$isStoreDemoModeEnabled
+ _objc_msgSend$loadProfileWithCompletionHandler:
+ _objc_msgSend$localPlayerDidSelectChallenge:
+ _objc_msgSend$localizedStringWithFormat:
+ _objc_msgSend$photos
+ _objc_msgSend$player:receivedTurnEventForMatch:didBecomeActive:
+ _objc_msgSend$player:wantsToPlayChallenge:
+ _objc_msgSend$player:wantsToQuitMatch:
+ _objc_msgSend$playerID
+ _objc_msgSend$presentDashboard:handler:
+ _objc_msgSend$presentedDashboard
+ _objc_msgSend$proxyForLocalPlayer
+ _objc_msgSend$runModal
+ _objc_msgSend$setAccessPointActive:location:
+ _objc_msgSend$setAuthenticateHandler:
+ _objc_msgSend$setGameCenterDelegate:
+ _objc_msgSend$setInformativeText:
+ _objc_msgSend$setMessageText:
+ _objc_msgSend$setPresentedDashboard:
+ _objc_msgSend$showAccessPoint
+ _objc_msgSend$showBannerWithTitle:message:completionHandler:
+ _objc_msgSend$showWelcomeBannerWithNewToGameCenter:returnToForeground:
+ _objc_msgSend$updateAccessPointLocation:
+ _objc_msgSend$updateAccessPointWithLocation:gameInternal:sceneIdentifier:
+ _objc_msgSend$utilityService
+ _objc_msgSend$window
+ _sBannerVisible
+ _symbolic Si
+ _symbolic So11GKChallengeC
+ _symbolic So16GKTurnBasedMatchC
+ _symbolic _____ 24GameCenterOverlayService20AccessPointAnchoringO
+ _symbolic _____XMT 22GameCenterUI_Rosettini12OverlayProbeC
- __OBJC_$_CATEGORY_INSTANCE_METHODS_GKLocalPlayer_$_AuthenticationExtras_Rosettini
CStrings:
+ "@\"GKGameCenterViewController\""
+ "E"
+ "GAME_CENTER_ACCOUNT_LOCKED"
+ "GAME_CENTER_DEMO_MODE"
+ "GAME_INVITE_CANCELED_ALERT_MESSAGE_ALIAS_ONLY_FORMAT"
+ "GKGameCenterControllerDelegate"
+ "GKRosettiniEventDelivery"
+ "LegacyAuthX86Support"
+ "OK_BUTTON"
+ "SIGN_IN_BANNER_SUBTITLE"
+ "SIGN_IN_BANNER_TITLE"
+ "T@\"GKGameCenterViewController\",&,N,V_presentedDashboard"
+ "T@\"NSString\",C,V_dashboardPlayerID"
+ "[GameCenterUI x86] Triggering welcome banner overlay"
+ "_dashboardPlayerID"
+ "_gkIsEligibleForOnboardingUI"
+ "_presentedDashboard"
+ "_rosettiniLoadPhotoForSize:withCompletionHandler:"
+ "_rosettiniPlaceholderPhoto"
+ "accountService"
+ "addButtonWithTitle:"
+ "b"
+ "baseLeaderboardID"
+ "beginSheetModalForWindow:completionHandler:"
+ "dashboardPlayerID"
+ "deliverReceivedTurnEventForMatch:didBecomeActive:"
+ "deliverWantsToPlayChallenge:"
+ "deliverWantsToQuitMatch:"
+ "didShowSignInBanner"
+ "displayNameWithOptions:"
+ "eventEmitter"
+ "getStoreBagValuesForKeys:handler:"
+ "integerValueFromKey:defaultValue:"
+ "isNewToGameCenter"
+ "isStoreDemoModeEnabled"
+ "loadProfileWithCompletionHandler:"
+ "localPlayerDidSelectChallenge:"
+ "localizedStringWithFormat:"
+ "photos"
+ "player:receivedTurnEventForMatch:didBecomeActive:"
+ "player:wantsToPlayChallenge:"
+ "player:wantsToQuitMatch:"
+ "playerID"
+ "presentDashboard:handler:"
+ "presentedDashboard"
+ "proxyForLocalPlayer"
+ "runModal"
+ "setAccessPointActive:location:"
+ "setAuthenticateHandler:"
+ "setDashboardPlayerID:"
+ "setInformativeText:"
+ "setMessageText:"
+ "setPresentedDashboard:"
+ "startLegacyAuthenticationWithCompletionHandler:"
+ "updateAccessPointLocation:"
+ "utilityService"
+ "v24@0:8@\"GKGameCenterViewController\"16"
+ "v24@?0@\"NSViewController\"8@\"NSError\"16"
+ "v28@0:8B16q20"
+ "viewDidAppear"
+ "window"
- "D"
- "a"
```
