## ProgressUI

> `/System/Library/PrivateFrameworks/ProgressUI.framework/ProgressUI`

```diff

-2839.0.0.0.0
-  __TEXT.__text: 0x3238
+2842.0.0.0.0
+  __TEXT.__text: 0x3360
   __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x414
   __TEXT.__const: 0x248

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AADD3ED1-89A7-3CF5-B9AD-3197CBA35D1D
+  UUID: 55703B43-070D-3CC2-8BAE-ECEBF72560E9
   Functions: 57
   Symbols:   429
   CStrings:  378
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x24
- _objc_retain_x8
Functions:
~ -[PUIProgressWindow _initWithOptions:contextLevel:appearance:environment:] : 652 -> 684
~ -[PUIProgressWindow _appendErrorDescriptionWithString:] : 156 -> 164
~ -[PUIProgressWindow _unsupportedScreenClass] : 160 -> 168
~ -[PUIProgressWindow dealloc] : 176 -> 180
~ -[PUIProgressWindow _collectDisplayInfo] : 1548 -> 1576
~ -[PUIProgressWindow _createContext] : 336 -> 340
~ __IOSurfacePropertyDictionaryForRect : 460 -> 492
~ -[PUIProgressWindow _createLayer] : 1772 -> 1860
~ -[PUIProgressWindow setStatusText:] : 444 -> 452
~ -[PUIProgressWindow _layoutScreen] : 2196 -> 2216
~ -[PUIProgressWindow _createImageWithName:scale:displayHeight:] : 880 -> 892
~ +[PUIFramebufferSizeChangeNotifier sharedInstance] : 68 -> 84
~ -[PUIFramebufferSizeChangeNotifier addListener:] : 288 -> 296
~ -[PUIFramebufferSizeChangeNotifier removeListener:] : 148 -> 152
~ -[PUIFramebufferSizeChangeNotifier _onMainQueue_notifyListeners] : 536 -> 560

```
