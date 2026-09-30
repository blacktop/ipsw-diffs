## TVRemoteModule

> `/System/Library/ControlCenter/Bundles/TVRemoteModule.bundle/TVRemoteModule`

```diff

-548.30.4.0.0
-  __TEXT.__text: 0x2710
-  __TEXT.__auth_stubs: 0x230
+548.40.44.0.0
+  __TEXT.__text: 0x2ae8
+  __TEXT.__auth_stubs: 0x210
   __TEXT.__objc_methlist: 0x664
   __TEXT.__const: 0xb8
   __TEXT.__oslogstring: 0x367
   __TEXT.__cstring: 0x1a5
-  __TEXT.__unwind_info: 0x120
+  __TEXT.__unwind_info: 0x160
   __TEXT.__objc_classname: 0x7e
   __TEXT.__objc_methname: 0x1459
   __TEXT.__objc_methtype: 0x544

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x518
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x120
+  __AUTH_CONST.__auth_got: 0x110
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0xa90

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F5C43B1E-A6A0-383F-9CD5-B5EEE5575AB8
+  UUID: C944C156-F34F-3D29-8932-946AFCB0E62C
   Functions: 70
-  Symbols:   341
+  Symbols:   339
   CStrings:  312
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x21
- _objc_retain_x3
Functions:
~ -[TVRemoteModule setContentModuleContext:] : 188 -> 196
~ -[TVRemoteModule contentViewControllerForContext:] : 364 -> 392
~ -[TVRemoteModule setContentViewController:] : 12 -> 64
~ -[TVRemoteModule setModuleContext:] : 12 -> 64
~ -[TVRMContentViewController viewWillLayoutSubviews] : 400 -> 440
~ -[TVRMContentViewController title] : 120 -> 128
~ -[TVRMContentViewController supportedInterfaceOrientations] : 68 -> 72
~ -[TVRMContentViewController viewWillTransitionToSize:withTransitionCoordinator:] : 576 -> 572
~ ___80-[TVRMContentViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke : 68 -> 72
~ -[TVRMContentViewController customAnimator] : 612 -> 628
~ ___43-[TVRMContentViewController customAnimator]_block_invoke : 240 -> 264
~ ___43-[TVRMContentViewController customAnimator]_block_invoke.17 : 272 -> 296
~ -[TVRMContentViewController _createRemoteControlViewControllerIfNeeded] : 676 -> 748
~ -[TVRMContentViewController _startRemoteControlViewController] : 224 -> 240
~ -[TVRMContentViewController _stopRemoteControlViewController] : 292 -> 308
~ -[TVRMContentViewController buttonTapped:forEvent:] : 352 -> 372
~ -[TVRMContentViewController preferredExpandedContentHeight] : 128 -> 132
~ -[TVRMContentViewController preferredExpandedContentWidth] : 108 -> 112
~ -[TVRMContentViewController shouldFinishTransitionToExpandedContentModule] : 400 -> 416
~ -[TVRMContentViewController willTransitionToExpandedContentMode:] : 280 -> 288
~ -[TVRMContentViewController displayWillTurnOff] : 196 -> 200
~ -[TVRMContentViewController _dismissChildViewControllersPresentedContentAnimated:completion:] : 324 -> 328
~ ___93-[TVRMContentViewController _dismissChildViewControllersPresentedContentAnimated:completion:]_block_invoke : 88 -> 92
~ -[TVRMContentViewController canDismissPresentedContent] : 244 -> 256
~ -[TVRMContentViewController dismissPresentedContentAnimated:completion:] : 340 -> 344
~ ___72-[TVRMContentViewController dismissPresentedContentAnimated:completion:]_block_invoke : 88 -> 92
~ -[TVRMContentViewController shouldLaunchAsViewService] : 112 -> 120
~ -[TVRMContentViewController _requestLaunchAsViewService] : 240 -> 252
~ -[TVRMContentViewController _remoteLaunchedAsViewService:] : 176 -> 180
~ ___58-[TVRMContentViewController _remoteLaunchedAsViewService:]_block_invoke : 68 -> 72
~ -[TVRMContentViewController _prewarm] : 204 -> 212
~ -[TVRMContentViewController setContentModuleContext:] : 20 -> 80
~ -[TVRMContentViewController setBackgroundViewController:] : 20 -> 80
~ -[TVRMContentViewController setRemoteControlViewController:] : 20 -> 80
~ -[TVRMContentViewController setHintsViewController:] : 20 -> 80
~ -[TVRMContentViewController setLastActiveEndpointIdentifier:] : 20 -> 80
~ -[TVRMContentViewController setRemoteShowAnimator:] : 20 -> 80
~ -[TVRMContentViewController setRemoteDismissAnimator:] : 20 -> 80
~ +[TVRMDeviceInfo heightForCurrentDeviceWithOrientation:] : 572 -> 600
~ +[TVRMDeviceInfo widthForCurrentDevice] : 176 -> 180
~ +[TVRMDeviceInfo contentEdgeInsets] : 208 -> 216
~ +[TVRMDeviceInfo needsLandscapeOrientationForCurrentDevice] : 148 -> 152
~ +[TVRMDeviceInfo needsCompactLayoutForCurrentDevice] : 172 -> 184
~ +[TVRMDeviceInfo expandedRoundedCornerRadius] : 184 -> 196
~ __TVRMControlCenterLog : 68 -> 84

```
