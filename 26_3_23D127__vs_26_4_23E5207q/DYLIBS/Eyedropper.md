## Eyedropper

> `/System/Library/PrivateFrameworks/Eyedropper.framework/Eyedropper`

```diff

 9083.1.0.0.0
-  __TEXT.__text: 0x63d8
-  __TEXT.__auth_stubs: 0x510
+  __TEXT.__text: 0x6814
+  __TEXT.__auth_stubs: 0x4b0
   __TEXT.__objc_methlist: 0xc74
   __TEXT.__const: 0x158
   __TEXT.__cstring: 0x180
-  __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__unwind_info: 0x248
+  __TEXT.__gcc_except_tab: 0x94
+  __TEXT.__unwind_info: 0x258
   __TEXT.__objc_classname: 0x16f
   __TEXT.__objc_methname: 0x29df
   __TEXT.__objc_methtype: 0x155c

   __DATA_CONST.__objc_selrefs: 0xb30
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x298
+  __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x1118

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7342539-9DF1-36CA-86FD-5AAFCA562AB8
+  UUID: 14454798-EDD7-3610-9E03-EE19C20C4074
   Functions: 146
-  Symbols:   834
+  Symbols:   828
   CStrings:  619
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x8
Functions:
~ +[NSValue(EDColor) valueWithColor:] : 80 -> 84
~ -[EDAppDelegate init] : 228 -> 240
~ _EDDisplayIdentifierForWindowScene : 116 -> 140
~ -[EDAppDelegate _sceneWillConnect:] : 180 -> 196
~ -[EDAppDelegate _sceneDidDisconnect:] : 112 -> 120
~ -[EDAppDelegate mainScreenWindow] : 96 -> 104
~ -[EDAppDelegate mainScreenLensView] : 100 -> 112
~ -[EDAppDelegate activeLensView] : 68 -> 88
~ -[EDAppDelegate application:didFinishLaunchingWithOptions:] : 440 -> 452
~ -[EDAppDelegate performOnAllWindows:] : 396 -> 412
~ -[EDAppDelegate _enumerateRemoteClientsUsingBlock:] : 352 -> 360
~ -[EDAppDelegate hideSystemPointer:] : 124 -> 128
~ -[EDAppDelegate _updateDynamicRangeSamplingModesFromClientSettings] : 324 -> 332
~ -[EDAppDelegate beginShowingEyeDropper:settings:] : 328 -> 312
~ ___49-[EDAppDelegate beginShowingEyeDropper:settings:]_block_invoke : 860 -> 900
~ ___40-[EDAppDelegate cancelShowingEyeDropper]_block_invoke : 288 -> 292
~ -[EDAppDelegate _updateLastDisplayLocation:forLensView:] : 252 -> 272
~ -[EDAppDelegate _lastDisplayLocationForLensView:] : 172 -> 188
~ ___32-[EDAppDelegate floatEyeDropper]_block_invoke : 784 -> 840
~ -[EDAppDelegate lensView:didSelectColorsBySamplingMode:] : 208 -> 204
~ ___56-[EDAppDelegate lensView:didSelectColorsBySamplingMode:]_block_invoke : 220 -> 228
~ -[EDAppDelegate lensViewDidActivate:] : 212 -> 216
~ -[EDAppDelegate lensViewDynamicRangeSamplingModes:] : 16 -> 64
~ -[EDAppDelegate dismissEyedropper] : 800 -> 824
~ -[EDGridView initWithWithCellCount:] : 128 -> 132
~ -[EDGridView setStrokeColor:] : 72 -> 80
~ -[EDLensView(DND) dragItemsForInteraction:] : 344 -> 368
~ -[EDSceneDelegate appDelegate] : 84 -> 92
~ -[EDSceneDelegate scene:willConnectToSession:options:] : 204 -> 216
~ -[EDSceneDelegate lensView] : 88 -> 96
~ -[EDSceneDelegate trackedTouchesBegan:] : 272 -> 292
~ -[EDSceneDelegate trackedTouchesEnded:] : 324 -> 344
~ -[EDSceneDelegate trackedTouchesMoved:] : 304 -> 328
~ -[EDSceneDelegate setWindow:] : 20 -> 80
~ _ColorUIColorWithColorSpace : 172 -> 176
~ -[EDLensView initWithFrame:] : 1180 -> 1264
~ -[EDLensView _layoutStaticElements] : 692 -> 728
~ -[EDLensView selectColor] : 92 -> 96
~ -[EDLensView setActive:] : 256 -> 260
~ -[EDLensView updateLensViewWithEvent:] : 328 -> 336
~ -[EDLensView _isScreenScaleEven] : 88 -> 96
~ -[EDLensView _colorAtCenterForHeadroomMode:] : 1176 -> 1224
~ ___44-[EDLensView _colorAtCenterForHeadroomMode:]_block_invoke : 172 -> 180
~ -[EDLensView _displayLinkFired] : 444 -> 464
~ ___31-[EDLensView _displayLinkFired]_block_invoke : 136 -> 144
~ -[EDLensView _lensPosition] : 364 -> 380
~ -[EDWindow initWithWindowScene:] : 284 -> 296
~ -[EDWindow hitTest:withEvent:] : 252 -> 264
~ -[EDWindow touchesBegan:withEvent:] : 96 -> 100
~ -[EDWindow touchesMoved:withEvent:] : 96 -> 100
~ -[EDWindow touchesEnded:withEvent:] : 96 -> 100
~ -[EDWindow touchesCancelled:withEvent:] : 96 -> 100
~ -[EDColorAnalyzer colorsSuggestionsForSurface:maxSuggestions:clipToCircle:clipedToRect:] : 344 -> 364
~ -[EDColorAnalyzer removeSimilarColors:minDistance:] : 880 -> 908
~ -[EDColorAnalyzer kmeansColorsForColors:clusters:] : 2096 -> 2176
~ -[EDColorAnalyzer colorsInSurface:offset:clipToCircle:clipedToRect:] : 904 -> 912
~ -[EDColorAnalyzer colorAtCenterOfHDRSurface:SDRSurface:offset:] : 624 -> 640
~ -[EDColorAnalyzer colorAtCenterOfSurface:offset:] : 556 -> 560
~ -[EDColorAnalyzer getRandomColors:from:] : 388 -> 416
~ -[EDWindowRootViewController initWithScreenBounds:] : 284 -> 288
~ -[EDWindowRootViewController viewDidLoad] : 120 -> 128
~ -[EDWindowRootViewController setLensView:] : 20 -> 80

```
