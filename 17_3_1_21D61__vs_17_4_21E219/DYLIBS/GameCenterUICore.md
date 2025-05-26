## GameCenterUICore

> `/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore`

```diff

-818.3.4.2.1
-  __TEXT.__text: 0x2a39c
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x21d8
+818.4.37.2.1
+  __TEXT.__text: 0x26074
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__objc_methlist: 0x21f0
   __TEXT.__const: 0x4b4
-  __TEXT.__gcc_except_tab: 0x1e4
-  __TEXT.__cstring: 0x48e0
-  __TEXT.__oslogstring: 0xe
+  __TEXT.__gcc_except_tab: 0x168
+  __TEXT.__cstring: 0x3100
+  __TEXT.__oslogstring: 0x1b96
   __TEXT.__dlopen_cstrs: 0xa8
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_typeref: 0x114

   __TEXT.__swift5_reflstr: 0x60
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x30
-  __TEXT.__unwind_info: 0xa28
+  __TEXT.__unwind_info: 0xa20
   __TEXT.__eh_frame: 0x160
   __TEXT.__objc_classname: 0x41e
-  __TEXT.__objc_methname: 0x6d26
+  __TEXT.__objc_methname: 0x6e00
   __TEXT.__objc_methtype: 0xe94
-  __TEXT.__objc_stubs: 0x53c0
+  __TEXT.__objc_stubs: 0x5460
   __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0xc78
+  __DATA_CONST.__const: 0xcc8
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x33c8
-  __DATA_CONST.__objc_selrefs: 0x1db8
-  __AUTH_CONST.__cfstring: 0x1e40
+  __DATA_CONST.__objc_selrefs: 0x1de0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x308
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __AUTH_CONST.__cfstring: 0x1200
   __AUTH_CONST.__objc_const: 0x12e8
   __AUTH_CONST.__const: 0x570
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x698
+  __AUTH_CONST.__auth_got: 0x688
   __AUTH.__objc_data: 0xce0
   __AUTH.__data: 0xc0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x308
-  __DATA.__objc_superrefs: 0xb0
   __DATA.__objc_ivar: 0x160
   __DATA.__data: 0x5b0
   __DATA.__bss: 0x770

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1057
-  Symbols:   3458
-  CStrings:  1811
+  Functions: 1055
+  Symbols:   3459
+  CStrings:  1825
 
Symbols:
+ -[GKLocalPlayer(AuthenticationPrivate) presentAuthenticationUIForLocalPlayer:]
+ -[GKLocalPlayer(AuthenticationPrivate) showOnboardingUIWithSignInOrigin:]
+ GCC_except_table11
+ GCC_except_table26
+ GCC_except_table6
+ _GKOSLoggers
+ ___117-[GKNetworkImageSource loadAndCacheAvatarFromGamedForURLString:useUIImage:cacheSubdirectory:reference:queue:handler:]_block_invoke.252
+ ___117-[GKNetworkImageSource loadAndCacheAvatarFromGamedForURLString:useUIImage:cacheSubdirectory:reference:queue:handler:]_block_invoke.258
+ ___117-[GKNetworkImageSource loadAndCacheAvatarFromGamedForURLString:useUIImage:cacheSubdirectory:reference:queue:handler:]_block_invoke_2.253
+ ___117-[GKNetworkImageSource loadAndCacheAvatarFromGamedForURLString:useUIImage:cacheSubdirectory:reference:queue:handler:]_block_invoke_2.259
+ ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.129
+ ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.129.cold.1
+ ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.129.cold.2
+ ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.129.cold.3
+ ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.132
+ ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.132.cold.1
+ ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.132.cold.2
+ ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.132.cold.3
+ ___67-[GKLocalImageSource cachedImageFromGamedWithSubdirectory:handler:]_block_invoke.280
+ ___67-[GKLocalImageSource cachedImageFromGamedWithSubdirectory:handler:]_block_invoke.280.cold.1
+ ___67-[GKLocalImageSource cachedImageFromGamedWithSubdirectory:handler:]_block_invoke.280.cold.2
+ ___67-[GKLocalImageSource cachedImageFromGamedWithSubdirectory:handler:]_block_invoke.280.cold.3
+ ___67-[GKLocalImageSource cachedImageFromGamedWithSubdirectory:handler:]_block_invoke.281
+ ___69-[UIViewController(GKAdditions) _gkSetContentsNeedUpdateWithHandler:]_block_invoke.24
+ ___69-[UIViewController(GKAdditions) _gkSetContentsNeedUpdateWithHandler:]_block_invoke.24.cold.1
+ ___69-[UIViewController(GKAdditions) _gkSetContentsNeedUpdateWithHandler:]_block_invoke.26
+ ___69-[UIViewController(GKAdditions) _gkSetContentsNeedUpdateWithHandler:]_block_invoke_2.28
+ ___69-[UIViewController(GKAdditions) _gkSetContentsNeedUpdateWithHandler:]_block_invoke_3.29
+ ___75-[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBannerWithSignInOrigin:]_block_invoke.138
+ ___75-[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBannerWithSignInOrigin:]_block_invoke.cold.1
+ ___75-[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBannerWithSignInOrigin:]_block_invoke.cold.2
+ ___77-[GKNetworkImageSource loadImageForURLString:loader:reference:queue:handler:]_block_invoke.260
+ ___77-[GKNetworkImageSource loadImageForURLString:loader:reference:queue:handler:]_block_invoke_2.261
+ ___83-[GKLocalPlayer(AuthenticationPrivate) startAuthenticationForExistingPrimaryPlayer]_block_invoke.153
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_73_e8_32s40s48s56s_e8_v12?0B8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.142
+ ___block_literal_global.152
+ ___block_literal_global.165
+ ___block_literal_global.181
+ ___block_literal_global.220
+ ___block_literal_global.248
+ _objc_msgSend$didShowWelcomeBannerInOverlayWithNewUserState:
+ _objc_msgSend$dispatchGroupWithName:
+ _objc_msgSend$isAppUnlistedAndDisallowed:
+ _objc_msgSend$named:execute:
+ _objc_msgSend$presentAuthenticationUIForLocalPlayer:
+ _objc_msgSend$setIsWelcomeOrSignInBannerEnqueued:
+ _objc_msgSend$showOnboardingUIWithSignInOrigin:
+ _os_log_GKAccount
+ _os_log_GKAccountError
+ _os_log_GKCache
+ _os_log_GKDaemon
+ _os_log_GKError
+ _os_log_GKGeneral
+ _os_log_GKOnboarding
+ _os_log_GKPerf
+ _os_log_GKTrace
- -[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBannerWithSignInOrigin:].cold.1
- -[GKLocalPlayer(AuthenticationPrivate) _showWelcomeBannerWithSignInOrigin:].cold.2
- GCC_except_table10
- GCC_except_table23
- GCC_except_table5
- _GKActiveLogBits
- _GKOSLogInit
- ___117-[GKNetworkImageSource loadAndCacheAvatarFromGamedForURLString:useUIImage:cacheSubdirectory:reference:queue:handler:]_block_invoke.277
- ___117-[GKNetworkImageSource loadAndCacheAvatarFromGamedForURLString:useUIImage:cacheSubdirectory:reference:queue:handler:]_block_invoke.292
- ___117-[GKNetworkImageSource loadAndCacheAvatarFromGamedForURLString:useUIImage:cacheSubdirectory:reference:queue:handler:]_block_invoke_2.278
- ___117-[GKNetworkImageSource loadAndCacheAvatarFromGamedForURLString:useUIImage:cacheSubdirectory:reference:queue:handler:]_block_invoke_2.293
- ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.159
- ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.159.cold.1
- ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.159.cold.2
- ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.159.cold.3
- ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.171
- ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.171.cold.1
- ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.171.cold.2
- ___133-[GKLocalPlayerAuthenticator _authenticateUsingAuthUI:authenticationResults:usernameEditable:authUIDismissHandler:completionHandler:]_block_invoke.171.cold.3
- ___67-[GKLocalImageSource cachedImageFromGamedWithSubdirectory:handler:]_block_invoke.323
- ___67-[GKLocalImageSource cachedImageFromGamedWithSubdirectory:handler:]_block_invoke.323.cold.1
- ___67-[GKLocalImageSource cachedImageFromGamedWithSubdirectory:handler:]_block_invoke.323.cold.2
- ___67-[GKLocalImageSource cachedImageFromGamedWithSubdirectory:handler:]_block_invoke.323.cold.3
- ___67-[GKLocalImageSource cachedImageFromGamedWithSubdirectory:handler:]_block_invoke.333
- ___69-[UIViewController(GKAdditions) _gkSetContentsNeedUpdateWithHandler:]_block_invoke.30
- ___69-[UIViewController(GKAdditions) _gkSetContentsNeedUpdateWithHandler:]_block_invoke.30.cold.1
- ___69-[UIViewController(GKAdditions) _gkSetContentsNeedUpdateWithHandler:]_block_invoke.35
- ___69-[UIViewController(GKAdditions) _gkSetContentsNeedUpdateWithHandler:]_block_invoke_2.37
- ___69-[UIViewController(GKAdditions) _gkSetContentsNeedUpdateWithHandler:]_block_invoke_3.38
- ___77-[GKNetworkImageSource loadImageForURLString:loader:reference:queue:handler:]_block_invoke.300
- ___77-[GKNetworkImageSource loadImageForURLString:loader:reference:queue:handler:]_block_invoke_2.301
- ___83-[GKLocalPlayer(AuthenticationPrivate) startAuthenticationForExistingPrimaryPlayer]_block_invoke.173
- ___block_literal_global.141
- ___block_literal_global.151
- ___block_literal_global.179
- ___block_literal_global.180
- ___block_literal_global.219
- ___block_literal_global.247
- _objc_msgSend$dispatchGroup
- _objc_msgSend$execute:
- _objc_retain_x28
- _os_log_GKLogAccount
- _os_log_GKLogAccountError
- _os_log_GKLogCache
- _os_log_GKLogDaemon
- _os_log_GKLogError
- _os_log_GKLogGeneral
- _os_log_GKLogOnboarding
- _os_log_GKLogPerf
- _os_log_GKLogTrace
CStrings:
+ "%s:%d %s"
+ "+[GKAppLevelSignInVisibility fetchAppLevelVisibilityConstraintsWithHandler:]_block_invoke"
+ "-[GKLocalImageSource cacheImageUsingGamed:cacheSubdirectory:withHandler:]"
+ "-[GKLocalImageSource cachedImageFromGamedWithSubdirectory:handler:]"
+ "-[GKLocalImageSource deleteImageUsingGamedWithSubdirectory:withHandler:]"
+ "-[GKLocalPlayer(AuthenticationPrivate) startAuthenticationForExistingPrimaryPlayer]"
+ "-[GKLocalPlayerAuthenticator handleAuthKitResultsForUnder13WithContinuationData:altDSID:password:]"
+ "-[GKNetworkImageSource loadAndCacheAvatarFromGamedForURLString:useUIImage:cacheSubdirectory:reference:queue:handler:]"
+ "-[GKNetworkImageSource loadImageForURLString:loader:reference:queue:handler:]"
+ "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterUI/CommonUI/GKImageSource.m"
+ "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterUI/iOS/Framework/GKAppLevelSignInVisibility.m"
+ "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterUI/iOS/Framework/GKLocalPlayer+Authentication_iOS.m"
+ "Copy for friends who earned this count is greater than 3."
+ "Section header on a card for information targeting app developers"
+ "T@\"NSString\",?,R,C"
+ "Your friend request isn’t ready yet. Try sending again later."
+ "didShowWelcomeBannerInOverlayWithNewUserState:"
+ "dispatchGroupWithName:"
+ "isAppUnlistedAndDisallowed:"
+ "named:execute:"
+ "presentAuthenticationUIForLocalPlayer:"
+ "setIsWelcomeOrSignInBannerEnqueued:"
+ "showOnboardingUIWithSignInOrigin:"
- "%{public}@"
- "Copy for friends who earned this count is gerater than 3."
- "Invite creation is in process, please try again in a moment."
- "Section header on a card for information targeting app develoeprs"
- "dispatchGroup"
- "execute:"
- "friending_improvements"
- "shouldShowFriendSuggestionsScreen? NO -- friending_improvements is off"

```
