## CameraKit

> `/System/Library/PrivateFrameworks/CameraKit.framework/CameraKit`

```diff

-832.0.107.0.0
-  __TEXT.__text: 0x1c10
+840.1.220.0.0
+  __TEXT.__text: 0x1d48
   __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_methlist: 0x228
   __TEXT.__const: 0x90

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0906EDF2-047B-3B83-A918-9015AA1C8839
+  UUID: 018B6A0C-0FEE-341C-A96D-953735B803B7
   Functions: 47
   Symbols:   230
   CStrings:  160
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
Functions:
~ +[CAMShutterButton shutterButtonWithSpec:] : 76 -> 80
~ -[CMKShutterButton _updateSpinningAnimations] : 520 -> 524
~ -[CMKShutterButton _performModeSwitchAnimationFromMode:toMode:animated:] : 3044 -> 3268
~ -[CMKShutterButton _performHighlightAnimation] : 344 -> 364
~ -[CMKShutterButton setShowDisabled:] : 216 -> 232
~ -[CMKShutterButton _updateOuterAndInnerLayers] : 396 -> 424
~ -[CMKShutterButton _colorForMode:] : 144 -> 152
~ -[CMKShutterButton layoutSubviews] : 340 -> 348

```
