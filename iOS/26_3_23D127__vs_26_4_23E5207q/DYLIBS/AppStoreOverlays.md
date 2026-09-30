## AppStoreOverlays

> `/System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays`

```diff

-8.3.1.0.0
-  __TEXT.__text: 0x60b8
-  __TEXT.__auth_stubs: 0x3f0
+8.4.11.0.0
+  __TEXT.__text: 0x658c
+  __TEXT.__auth_stubs: 0x3a0
   __TEXT.__objc_methlist: 0xb8c
   __TEXT.__const: 0xb0
   __TEXT.__cstring: 0x641
   __TEXT.__oslogstring: 0x942
-  __TEXT.__gcc_except_tab: 0x6c
+  __TEXT.__gcc_except_tab: 0x70
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x260
+  __TEXT.__unwind_info: 0x2a0
   __TEXT.__objc_classname: 0x212
   __TEXT.__objc_methname: 0x1a15
   __TEXT.__objc_methtype: 0x62d

   __DATA_CONST.__objc_selrefs: 0x798
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x208
+  __AUTH_CONST.__auth_got: 0x1e0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x3c0
   __AUTH_CONST.__objc_const: 0x1348

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1ECDCD3A-1BC2-39A4-84E9-F5A17682537A
+  UUID: 0F51B342-E1C4-3B93-9EC3-ABD549CF95FD
   Functions: 213
-  Symbols:   950
+  Symbols:   945
   CStrings:  525
 
Symbols:
+ _objc_autorelease
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutorelease
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
Functions:
~ -[ASOOverlayAppClipConfiguration initWithStorage:] : 116 -> 108
~ -[ASOOverlayAppClipConfiguration initWithCoder:] : 308 -> 320
~ -[ASOOverlayAppClipConfiguration copyWithZone:] : 112 -> 116
~ -[ASOOverlayAppClipConfiguration setPosition:] : 104 -> 108
~ -[ASOOverlayAppClipConfiguration position] : 84 -> 88
~ -[ASOOverlayAppClipConfiguration additionalValueForKey:serviceContext:] : 168 -> 172
~ -[ASOOverlayAppClipConfiguration encodeWithCoder:] : 112 -> 116
~ -[ASOOverlayAppClipConfiguration description] : 180 -> 196
~ -[ASOOverlayAppConfiguration initWithStorage:] : 116 -> 108
~ -[ASOOverlayAppConfiguration initWithCoder:] : 308 -> 320
~ -[ASOOverlayAppConfiguration copyWithZone:] : 112 -> 116
~ -[ASOOverlayAppConfiguration setPosition:] : 104 -> 108
~ -[ASOOverlayAppConfiguration position] : 84 -> 88
~ -[ASOOverlayAppConfiguration setUserDismissible:] : 104 -> 108
~ -[ASOOverlayAppConfiguration userDismissible] : 84 -> 88
~ -[ASOOverlayAppConfiguration additionalValueForKey:] : 108 -> 116
~ -[ASOOverlayAppConfiguration encodeWithCoder:] : 112 -> 116
~ -[ASOOverlayAppConfiguration description] : 180 -> 196
~ -[ASOOverlayManager initWithScene:] : 268 -> 264
~ -[ASOOverlayManager presentOverlay:] : 348 -> 356
~ ___36-[ASOOverlayManager presentOverlay:]_block_invoke : 268 -> 296
~ ___35-[ASOOverlayManager dismissOverlay]_block_invoke : 120 -> 128
~ -[ASOOverlayManager willStartPresentingOverlay] : 244 -> 268
~ ___47-[ASOOverlayManager didFinishDismissingOverlay]_block_invoke : 180 -> 192
~ -[ASOOverlayManager makeViewControllerIfNeeded] : 228 -> 248
~ -[ASOOverlayManager setViewController:] : 12 -> 64
~ -[UIWindowScene(AppOverlayManager) _aso_appOverlayManager] : 304 -> 316
~ -[ASOOverlayTransitionContext initWithCoder:] : 232 -> 240
~ -[ASOOverlayTransitionContext addAnimationBlock:] : 116 -> 120
~ -[ASOOverlayTransitionContext encodeWithCoder:] : 212 -> 220
~ -[ASOOverlayTransitionContext setAnimationBlocks:] : 12 -> 64
~ _getASCSignpostSpanClass : 224 -> 220
~ _ASOViewRenderOverlayRequested : 272 -> 276
~ -[ASODismissRemoteOverlayOperation start] : 368 -> 376
~ -[ASOPresentRemoteOverlayOperation start] : 444 -> 464
~ ___41-[ASOPresentRemoteOverlayOperation start]_block_invoke : 108 -> 112
~ -[ASOPresentRemoteOverlayOperation setRemoteOverlay:] : 20 -> 80
~ +[ASORemoteOverlay log] : 68 -> 84
~ -[ASORemoteOverlay initWithOverlay:contextProvider:hostSpan:] : 188 -> 176
~ -[ASORemoteOverlay finishWithError:] : 304 -> 312
~ -[ASORemoteOverlay context] : 76 -> 84
~ -[ASORemoteOverlay overlayConfiguration] : 232 -> 252
~ ___61-[ASORemoteOverlay remoteStoreOverlayDidFailToLoadWithError:]_block_invoke : 332 -> 360
~ -[ASORemoteOverlay remoteStoreOverlayWillStartPresenting:executeBlock:] : 224 -> 212
~ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartPresenting:executeBlock:]_block_invoke : 560 -> 604
~ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartPresenting:executeBlock:]_block_invoke.14 : 244 -> 248
~ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartPresenting:executeBlock:]_block_invoke.16 : 248 -> 252
~ -[ASORemoteOverlay remoteStoreOverlayDidFinishPresentation:] : 168 -> 164
~ ___60-[ASORemoteOverlay remoteStoreOverlayDidFinishPresentation:]_block_invoke : 332 -> 360
~ -[ASORemoteOverlay remoteStoreOverlayWillStartDismissing:executeBlock:] : 196 -> 188
~ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartDismissing:executeBlock:]_block_invoke : 560 -> 600
~ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartDismissing:executeBlock:]_block_invoke.21 : 244 -> 248
~ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartDismissing:executeBlock:]_block_invoke.22 : 248 -> 252
~ ___57-[ASORemoteOverlay remoteStoreOverlayDidFinishDismissal:]_block_invoke : 332 -> 360
~ -[ASORemoteOverlay setOverlay:] : 12 -> 64
~ -[ASORemoteOverlay setPresentationTransitionContext:] : 12 -> 64
~ -[ASOOverlayViewController initWithNibName:bundle:] : 212 -> 216
~ -[ASOOverlayViewController viewDidLoad] : 332 -> 352
~ -[ASOOverlayViewController viewDidLayoutSubviews] : 236 -> 252
~ -[ASOOverlayViewController presentOverlay:] : 368 -> 388
~ -[ASOOverlayViewController dismissOverlay] : 248 -> 260
~ -[ASOOverlayViewController failAllQueuedOverlaysWithError:] : 580 -> 600
~ -[ASOOverlayViewController loadViewServiceIfNeeded] : 136 -> 140
~ ___51-[ASOOverlayViewController loadViewServiceIfNeeded]_block_invoke : 192 -> 188
~ -[ASOOverlayViewController _loadViewServiceIfNeeded:] : 444 -> 452
~ ___53-[ASOOverlayViewController _loadViewServiceIfNeeded:]_block_invoke : 848 -> 872
~ ___53-[ASOOverlayViewController _loadViewServiceIfNeeded:]_block_invoke.14 : 224 -> 232
~ ___54-[ASOOverlayViewController _loadRemoteViewController:]_block_invoke : 488 -> 496
~ ___54-[ASOOverlayViewController _loadRemoteViewController:]_block_invoke.21 : 188 -> 196
~ -[ASOOverlayViewController willStartPresentingOverlay:transitionContext:] : 208 -> 212
~ -[ASOOverlayViewController didFinishDismissingOverlay:] : 200 -> 204
~ -[ASOOverlayViewController viewServiceDidTerminateWithError:] : 332 -> 368
~ -[ASOOverlayViewController shutdownViewServiceIfOverlayOffScreen] : 208 -> 216
~ -[ASOOverlayViewController setRemoteViewController:] : 20 -> 80
~ -[ASOOverlayViewController setCurrentOverlay:] : 20 -> 80
~ -[ASOOverlayViewController setViewServiceQueue:] : 20 -> 80
~ -[ASOOverlayViewController setPresentationQueue:] : 20 -> 80
~ +[ASOHostContext _extensionAuxiliaryHostProtocol] : 68 -> 84
~ ___49+[ASOHostContext _extensionAuxiliaryHostProtocol]_block_invoke : 72 -> 76
~ +[ASOHostContext _extensionAuxiliaryVendorProtocol] : 68 -> 84
~ ___51+[ASOHostContext _extensionAuxiliaryVendorProtocol]_block_invoke : 328 -> 344
~ -[ASOHostContext serviceContext] : 76 -> 84
~ -[ASOHostContext presentOverlayWithConfiguration:delegate:reply:] : 144 -> 140
~ -[ASOHostContext dismissOverlayWithReply:] : 96 -> 100
~ -[ASORemoteViewController viewServiceDidTerminateWithError:] : 332 -> 348

```
