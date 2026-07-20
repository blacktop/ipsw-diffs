## GameCenterUI_x86Support

> `/System/Library/PrivateFrameworks/GameCenterUI.framework/Versions/A/GameCenterUI_x86Support`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-821.0.18.0.0
-  __TEXT.__text: 0x7888
-  __TEXT.__objc_methlist: 0xc18
-  __TEXT.__cstring: 0x623
-  __TEXT.__const: 0x230
-  __TEXT.__oslogstring: 0x13a
+821.0.20.0.0
+  __TEXT.__text: 0xa3e4
+  __TEXT.__objc_methlist: 0xe90
+  __TEXT.__cstring: 0x863
+  __TEXT.__const: 0x250
+  __TEXT.__oslogstring: 0x1e4
+  __TEXT.__gcc_except_tab: 0x4c
   __TEXT.__swift5_typeref: 0x1a5
   __TEXT.__swift5_capture: 0x120
   __TEXT.__swift5_fieldmd: 0xcc

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0x14
-  __TEXT.__unwind_info: 0x380
+  __TEXT.__unwind_info: 0x480
   __TEXT.__eh_frame: 0x2b0
-  __TEXT.__objc_stubs: 0xac0
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_classname: 0x399
-  __TEXT.__objc_methname: 0x20cd
-  __TEXT.__objc_methtype: 0x805
-  __DATA_CONST.__const: 0x128
-  __DATA_CONST.__objc_classlist: 0x78
+  __TEXT.__objc_stubs: 0x1440
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_classname: 0x459
+  __TEXT.__objc_methname: 0x2891
+  __TEXT.__objc_methtype: 0x935
+  __DATA_CONST.__const: 0x168
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x790
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x1b0
-  __AUTH_CONST.__const: 0x358
-  __AUTH_CONST.__cfstring: 0x380
-  __AUTH_CONST.__objc_const: 0x18e0
+  __DATA_CONST.__objc_selrefs: 0xa00
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_arraydata: 0x78
+  __DATA_CONST.__got: 0x228
+  __AUTH_CONST.__const: 0x508
+  __AUTH_CONST.__cfstring: 0x660
+  __AUTH_CONST.__objc_const: 0x23d8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x3c0
-  __AUTH.__objc_data: 0x590
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x448
+  __AUTH.__objc_data: 0x680
   __AUTH.__data: 0x158
-  __DATA.__objc_ivar: 0x90
-  __DATA.__data: 0x230
-  __DATA.__bss: 0x10
+  __DATA.__objc_ivar: 0xb8
+  __DATA.__data: 0x350
+  __DATA.__bss: 0x30
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xc8
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 365
-  Symbols:   679
-  CStrings:  480
+  Functions: 438
+  Symbols:   920
+  CStrings:  619
 
Symbols:
+ +[GKNotificationBannerWindow notificationBannerWithTitle:message:]
+ +[GKNotificationBannerWindow queue]
+ +[GKNotificationBannerWindow semaphore]
+ -[GKMatchmakerViewController gkRosettiniDismiss]
+ -[GKMatchmakerViewController gkRosettiniPresentInWindow:]
+ -[GKMatchmakerViewController matchmakerHostServiceRequestsDismiss:]
+ -[GKMatchmakerViewController rosettiniHost]
+ -[GKMatchmakerViewController setRosettiniHost:]
+ -[GKNotificationBannerWindow .cxx_destruct]
+ -[GKNotificationBannerWindow avatarImageView]
+ -[GKNotificationBannerWindow hideAnimatedWithHandler:]
+ -[GKNotificationBannerWindow iconContainerView]
+ -[GKNotificationBannerWindow iconView]
+ -[GKNotificationBannerWindow label]
+ -[GKNotificationBannerWindow sendEvent:]
+ -[GKNotificationBannerWindow setAvatarImageView:]
+ -[GKNotificationBannerWindow setFrame:display:]
+ -[GKNotificationBannerWindow setIconContainerView:]
+ -[GKNotificationBannerWindow setIconView:]
+ -[GKNotificationBannerWindow setLabel:]
+ -[GKNotificationBannerWindow showForDuration:withCompletionHandler:]
+ -[GKNotificationBannerWindow showWithCompletionHandler:]
+ -[GKRosettiniMatchmakerHost .cxx_destruct]
+ -[GKRosettiniMatchmakerHost delegate]
+ -[GKRosettiniMatchmakerHost dismiss]
+ -[GKRosettiniMatchmakerHost hostRemoteView:inWindow:]
+ -[GKRosettiniMatchmakerHost panelWindow]
+ -[GKRosettiniMatchmakerHost presentForMatchRequest:hosted:matchmakingMode:canStartWithMinimumPlayers:inWindow:]
+ -[GKRosettiniMatchmakerHost remoteVC]
+ -[GKRosettiniMatchmakerHost serviceRequestedDismiss]
+ -[GKRosettiniMatchmakerHost setDelegate:]
+ -[GKRosettiniMatchmakerHost setPanelWindow:]
+ -[GKRosettiniMatchmakerHost setRemoteVC:]
+ -[GKRosettiniMatchmakerRemoteVC .cxx_destruct]
+ -[GKRosettiniMatchmakerRemoteVC exportedInterface]
+ -[GKRosettiniMatchmakerRemoteVC host]
+ -[GKRosettiniMatchmakerRemoteVC messageFromService:]
+ -[GKRosettiniMatchmakerRemoteVC serviceRequestsDismiss]
+ -[GKRosettiniMatchmakerRemoteVC serviceViewControllerInterface]
+ -[GKRosettiniMatchmakerRemoteVC setHost:]
+ -[GKTurnBasedMatchmakerViewController matchRequest]
+ GCC_except_table1
+ GCC_except_table11
+ OBJC_IVAR_$_GKMatchmakerViewController._rosettiniHost
+ OBJC_IVAR_$_GKNotificationBannerWindow._avatarImageView
+ OBJC_IVAR_$_GKNotificationBannerWindow._iconContainerView
+ OBJC_IVAR_$_GKNotificationBannerWindow._iconView
+ OBJC_IVAR_$_GKNotificationBannerWindow._label
+ OBJC_IVAR_$_GKRosettiniMatchmakerHost._delegate
+ OBJC_IVAR_$_GKRosettiniMatchmakerHost._panelWindow
+ OBJC_IVAR_$_GKRosettiniMatchmakerHost._remoteVC
+ OBJC_IVAR_$_GKRosettiniMatchmakerRemoteVC._host
+ OBJC_IVAR_$_GKTurnBasedMatchmakerViewController._matchRequest
+ _GKGameCenterUIFrameworkBundle
+ _GKRosettiniAllowedClasses
+ _NSZeroRect
+ _OBJC_CLASS_$_GKNotificationBannerWindow
+ _OBJC_CLASS_$_GKRosettiniMatchmakerHost
+ _OBJC_CLASS_$_GKRosettiniMatchmakerRemoteVC
+ _OBJC_CLASS_$_GKServiceInterface
+ _OBJC_CLASS_$_NSAnimationContext
+ _OBJC_CLASS_$_NSBezierPath
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSEvent
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSScreen
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_EHTYPE_id
+ _OBJC_METACLASS_$_GKNotificationBannerWindow
+ _OBJC_METACLASS_$_GKRosettiniMatchmakerHost
+ _OBJC_METACLASS_$_GKRosettiniMatchmakerRemoteVC
+ _OBJC_METACLASS_$_NSWindow
+ __111-[GKRosettiniMatchmakerHost presentForMatchRequest:hosted:matchmakingMode:canStartWithMinimumPlayers:inWindow:]_block_invoke
+ __111-[GKRosettiniMatchmakerHost presentForMatchRequest:hosted:matchmakingMode:canStartWithMinimumPlayers:inWindow:]_block_invoke_2
+ __OBJC_$_CLASS_METHODS_GKNotificationBannerWindow
+ __OBJC_$_INSTANCE_METHODS_GKNotificationBannerWindow
+ __OBJC_$_INSTANCE_METHODS_GKRosettiniMatchmakerHost
+ __OBJC_$_INSTANCE_METHODS_GKRosettiniMatchmakerRemoteVC
+ __OBJC_$_INSTANCE_VARIABLES_GKNotificationBannerWindow
+ __OBJC_$_INSTANCE_VARIABLES_GKRosettiniMatchmakerHost
+ __OBJC_$_INSTANCE_VARIABLES_GKRosettiniMatchmakerRemoteVC
+ __OBJC_$_PROP_LIST_GKNotificationBannerWindow
+ __OBJC_$_PROP_LIST_GKRosettiniMatchmakerHost
+ __OBJC_$_PROP_LIST_GKRosettiniMatchmakerRemoteVC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GKRemoteViewControllerHostProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GKRemoteViewControllerServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GKRosettiniMatchmakerHostDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GKRemoteViewControllerHostProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GKRemoteViewControllerServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GKRosettiniMatchmakerHostDelegate
+ __OBJC_$_PROTOCOL_REFS_GKRemoteViewControllerHostProtocol
+ __OBJC_$_PROTOCOL_REFS_GKRemoteViewControllerServiceProtocol
+ __OBJC_$_PROTOCOL_REFS_GKRosettiniMatchmakerHostDelegate
+ __OBJC_CLASS_PROTOCOLS_$_GKRosettiniMatchmakerRemoteVC
+ __OBJC_CLASS_RO_$_GKNotificationBannerWindow
+ __OBJC_CLASS_RO_$_GKRosettiniMatchmakerHost
+ __OBJC_CLASS_RO_$_GKRosettiniMatchmakerRemoteVC
+ __OBJC_LABEL_PROTOCOL_$_GKRemoteViewControllerHostProtocol
+ __OBJC_LABEL_PROTOCOL_$_GKRemoteViewControllerServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_GKRosettiniMatchmakerHostDelegate
+ __OBJC_METACLASS_RO_$_GKNotificationBannerWindow
+ __OBJC_METACLASS_RO_$_GKRosettiniMatchmakerHost
+ __OBJC_METACLASS_RO_$_GKRosettiniMatchmakerRemoteVC
+ __OBJC_PROTOCOL_$_GKRemoteViewControllerHostProtocol
+ __OBJC_PROTOCOL_$_GKRemoteViewControllerServiceProtocol
+ __OBJC_PROTOCOL_$_GKRosettiniMatchmakerHostDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_GKRemoteViewControllerHostProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_GKRemoteViewControllerServiceProtocol
+ __Unwind_Resume
+ ___111-[GKRosettiniMatchmakerHost presentForMatchRequest:hosted:matchmakingMode:canStartWithMinimumPlayers:inWindow:]_block_invoke
+ ___111-[GKRosettiniMatchmakerHost presentForMatchRequest:hosted:matchmakingMode:canStartWithMinimumPlayers:inWindow:]_block_invoke_2
+ ___35+[GKNotificationBannerWindow queue]_block_invoke
+ ___39+[GKNotificationBannerWindow semaphore]_block_invoke
+ ___47-[GKNotificationBannerWindow setFrame:display:]_block_invoke
+ ___54-[GKNotificationBannerWindow hideAnimatedWithHandler:]_block_invoke
+ ___54-[GKNotificationBannerWindow hideAnimatedWithHandler:]_block_invoke_2
+ ___55-[GKRosettiniMatchmakerRemoteVC serviceRequestsDismiss]_block_invoke
+ ___62-[GKLeaderboard(UI_Rosettini) loadImageWithCompletionHandler:]_block_invoke
+ ___65-[GKLeaderboardSet(UI_Rosettini) loadImageWithCompletionHandler:]_block_invoke
+ ___68-[GKNotificationBannerWindow showForDuration:withCompletionHandler:]_block_invoke
+ ___68-[GKNotificationBannerWindow showForDuration:withCompletionHandler:]_block_invoke_2
+ ___68-[GKNotificationBannerWindow showForDuration:withCompletionHandler:]_block_invoke_3
+ ___68-[GKNotificationBannerWindow showForDuration:withCompletionHandler:]_block_invoke_4
+ ___68-[GKNotificationBannerWindow showForDuration:withCompletionHandler:]_block_invoke_5
+ ___73-[GKAchievementDescription(UI_Rosettini) loadImageWithCompletionHandler:]_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e39_B40?0{CGRect={CGPoint=dd}{CGSize=dd}}8l
+ ___block_descriptor_40_e8_32bs_e16_v16?0"NSData"8l
+ ___block_descriptor_40_e8_32s_e5_v8?0l
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48w_e44_v24?0"NSRemoteViewController"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56s64w_e5_v8?0l
+ ___copy_helper_block_e8_32b
+ ___copy_helper_block_e8_32s
+ ___copy_helper_block_e8_32s40s48b
+ ___copy_helper_block_e8_32s40s48s56s64w
+ ___copy_helper_block_e8_32s40s48w
+ ___destroy_helper_block_e8_32s
+ ___destroy_helper_block_e8_32s40s48s
+ ___destroy_helper_block_e8_32s40s48s56s64w
+ ___destroy_helper_block_e8_32s40s48w
+ ___objc_personality_v0
+ _dispatch_after
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_sync
+ _dispatch_time
+ _objc_begin_catch
+ _objc_copyWeak
+ _objc_end_catch
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_gkForClientProcess
+ _objc_msgSend$_gkImageURLForSize:scale:
+ _objc_msgSend$_gkLoadRemoteImageDataForURL:session:subdirectory:filename:queue:handler:
+ _objc_msgSend$addObject:
+ _objc_msgSend$animator
+ _objc_msgSend$backingScaleFactor
+ _objc_msgSend$beginGrouping
+ _objc_msgSend$bezierPathWithRoundedRect:xRadius:yRadius:
+ _objc_msgSend$canStartWithMinimumPlayers
+ _objc_msgSend$center
+ _objc_msgSend$close
+ _objc_msgSend$contentRectForFrameRect:
+ _objc_msgSend$contentView
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$currentContext
+ _objc_msgSend$delegate
+ _objc_msgSend$endGrouping
+ _objc_msgSend$fill
+ _objc_msgSend$hideAnimatedWithHandler:
+ _objc_msgSend$host
+ _objc_msgSend$hostRemoteView:inWindow:
+ _objc_msgSend$hostSentIntitialState:
+ _objc_msgSend$iconView
+ _objc_msgSend$icons
+ _objc_msgSend$imageWithSize:flipped:drawingHandler:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$isHosted
+ _objc_msgSend$label
+ _objc_msgSend$layout
+ _objc_msgSend$length
+ _objc_msgSend$level
+ _objc_msgSend$loadNibNamed:owner:topLevelObjects:
+ _objc_msgSend$localPlayer
+ _objc_msgSend$mainScreen
+ _objc_msgSend$makeKeyWindow
+ _objc_msgSend$matchRequest
+ _objc_msgSend$matchmakerDelegate
+ _objc_msgSend$matchmakerHostServiceRequestsDismiss:
+ _objc_msgSend$matchmakingMode
+ _objc_msgSend$modifierFlags
+ _objc_msgSend$notificationBannerWithTitle:message:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$orderFront:
+ _objc_msgSend$orderOut:
+ _objc_msgSend$panelWindow
+ _objc_msgSend$plistClasses
+ _objc_msgSend$presentForMatchRequest:hosted:matchmakingMode:canStartWithMinimumPlayers:inWindow:
+ _objc_msgSend$queue
+ _objc_msgSend$remoteVC
+ _objc_msgSend$removeChildWindow:
+ _objc_msgSend$requestViewController:fromServiceWithBundleIdentifier:connectionHandler:
+ _objc_msgSend$safeAreaInsets
+ _objc_msgSend$semaphore
+ _objc_msgSend$sendEvent:
+ _objc_msgSend$serviceRequestedDismiss
+ _objc_msgSend$setAcceptsMouseMovedEvents:
+ _objc_msgSend$setAccessibilityIdentifier:
+ _objc_msgSend$setAlphaValue:
+ _objc_msgSend$setCapInsets:
+ _objc_msgSend$setCompletionHandler:
+ _objc_msgSend$setDuration:
+ _objc_msgSend$setHost:
+ _objc_msgSend$setMaskImage:
+ _objc_msgSend$setMovableByWindowBackground:
+ _objc_msgSend$setPanelWindow:
+ _objc_msgSend$setRemoteVC:
+ _objc_msgSend$setResizingMode:
+ _objc_msgSend$setStringValue:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$sharedDialogController
+ _objc_msgSend$showForDuration:withCompletionHandler:
+ _objc_msgSend$showWithCompletionHandler:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$unionSet:
+ _objc_msgSend$userErrorForCode:userInfo:
+ _objc_opt_class
+ queue.onceToken
+ queue.sQueue
+ semaphore.onceToken
+ semaphore.sSemaphore
CStrings:
+ ""
+ "%@\n%@"
+ "@\"<GKRosettiniMatchmakerHostDelegate>\""
+ "@\"GKRosettiniMatchmakerHost\""
+ "@\"GKRosettiniMatchmakerRemoteVC\""
+ "@\"NSImageView\""
+ "@\"NSPanel\""
+ "@\"NSTextField\""
+ "@\"NSView\""
+ "B40@?0{CGRect={CGPoint=dd}{CGSize=dd}}8"
+ "GKAchievement"
+ "GKGame"
+ "GKInviteInternal"
+ "GKLocalPlayer"
+ "GKMatchRequestInternal"
+ "GKNotificationBannerOSX"
+ "GKNotificationBannerWindow"
+ "GKPlayer"
+ "GKPlayerInternal"
+ "GKRemoteViewControllerHostProtocol"
+ "GKRemoteViewControllerServiceProtocol"
+ "GKRosettiniMatchmakerHost"
+ "GKRosettiniMatchmakerHostDelegate"
+ "GKRosettiniMatchmakerRemoteVC"
+ "GKTurnBasedMatchInternal"
+ "GameCenter.notificationBanner.image"
+ "GameCenter.notificationBanner.message"
+ "GameCenterViewService"
+ "Q"
+ "T@\"<GKRosettiniMatchmakerHostDelegate>\",W,V_delegate"
+ "T@\"GKRosettiniMatchmakerHost\",&,V_rosettiniHost"
+ "T@\"GKRosettiniMatchmakerHost\",W,V_host"
+ "T@\"GKRosettiniMatchmakerRemoteVC\",&,V_remoteVC"
+ "T@\"NSImageView\",&,V_avatarImageView"
+ "T@\"NSImageView\",&,V_iconView"
+ "T@\"NSPanel\",&,V_panelWindow"
+ "T@\"NSTextField\",&,V_label"
+ "T@\"NSView\",&,D"
+ "T@\"NSView\",&,V_iconContainerView"
+ "UIA.GameCenter.GKNotificationBanner"
+ "URLWithString:"
+ "[GameCenterUI x86] matchmaker remote VC request failed: %@"
+ "[GameCenterUI x86] matchmaker service proxy error: %@"
+ "[GameCenterUI x86] no host window for matchmaker overlay"
+ "_avatarImageView"
+ "_delegate"
+ "_gkForClientProcess"
+ "_gkImageURLForSize:scale:"
+ "_gkLoadRemoteImageDataForURL:session:subdirectory:filename:queue:handler:"
+ "_host"
+ "_iconContainerView"
+ "_iconView"
+ "_label"
+ "_panelWindow"
+ "_remoteVC"
+ "addObject:"
+ "animator"
+ "avatarImageView"
+ "backingScaleFactor"
+ "beginGrouping"
+ "bezierPathWithRoundedRect:xRadius:yRadius:"
+ "center"
+ "close"
+ "com.apple.GameKit.banner"
+ "com.apple.gamecenter.GameCenterUIService"
+ "contentRectForFrameRect:"
+ "contentView"
+ "countByEnumeratingWithState:objects:count:"
+ "currentContext"
+ "endGrouping"
+ "fill"
+ "game"
+ "hideAnimatedWithHandler:"
+ "host"
+ "hostRemoteView:inWindow:"
+ "hostSentIntitialState:"
+ "iconContainerView"
+ "iconView"
+ "icons"
+ "imageWithSize:flipped:drawingHandler:"
+ "initWithData:"
+ "label"
+ "layout"
+ "length"
+ "level"
+ "loadNibNamed:owner:topLevelObjects:"
+ "localPlayer"
+ "mainScreen"
+ "makeKeyWindow"
+ "matchmakerHostServiceRequestsDismiss:"
+ "matchmakerViewControllerWasCancelled:"
+ "messageFromHost:"
+ "messageFromService:"
+ "mode"
+ "modeSpecific"
+ "modifierFlags"
+ "notificationBannerWithTitle:message:"
+ "numberWithBool:"
+ "orderFront:"
+ "orderOut:"
+ "panelWindow"
+ "player"
+ "plistClasses"
+ "presentForMatchRequest:hosted:matchmakingMode:canStartWithMinimumPlayers:inWindow:"
+ "queue"
+ "removeChildWindow:"
+ "requestViewController:fromServiceWithBundleIdentifier:connectionHandler:"
+ "safeAreaInsets"
+ "semaphore"
+ "sendEvent:"
+ "serviceRequestedDismiss"
+ "serviceRequestsDismiss"
+ "setAcceptsMouseMovedEvents:"
+ "setAccessibilityIdentifier:"
+ "setAlphaValue:"
+ "setAvatarImageView:"
+ "setCapInsets:"
+ "setCompletionHandler:"
+ "setDuration:"
+ "setHost:"
+ "setIconContainerView:"
+ "setIconView:"
+ "setLabel:"
+ "setMaskImage:"
+ "setMovableByWindowBackground:"
+ "setPanelWindow:"
+ "setRemoteVC:"
+ "setResizingMode:"
+ "setStringValue:"
+ "setWithArray:"
+ "showForDuration:withCompletionHandler:"
+ "showWithCompletionHandler:"
+ "stringWithFormat:"
+ "unionSet:"
+ "userErrorForCode:userInfo:"
+ "v16@?0@\"NSData\"8"
+ "v24@0:8@\"GKRosettiniMatchmakerHost\"16"
+ "v24@0:8@\"NSDictionary\"16"
+ "v32@0:8d16@?24"
+ "v48@0:8@16B24q28B36@40"
+ "v52@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16B48"
- "list.number"
- "list.star"
```
