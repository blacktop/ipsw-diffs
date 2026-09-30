## Measure

> `/System/Library/AccessibilityBundles/Measure.axbundle/Measure`

```diff

-  __TEXT.__text: 0x6228
+  __TEXT.__text: 0x6210
   __TEXT.__objc_methlist: 0xcd8
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__cstring: 0xe83
+  __TEXT.__cstring: 0xe76
   __TEXT.__oslogstring: 0x96
   __TEXT.__unwind_info: 0x2b0
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x590
+  __DATA_CONST.__objc_selrefs: 0x598
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x15a0
+  __AUTH_CONST.__cfstring: 0x1580
   __AUTH_CONST.__objc_const: 0x21c0
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1220
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x8
-  __DATA.__bss: 0x24
+  __DATA.__bss: 0x2c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 251
-  Symbols:   1073
-  CStrings:  365
+  Symbols:   1076
+  CStrings:  363
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
Symbols:
+ -[LevelPageViewControllerAccessibility _axAnnounceOrientationChangeIfNeeded:]
+ -[LevelPageViewControllerAccessibility updateDisplay:]
+ __axAnnounceOrientationChangeIfNeeded:.LastAnnouncedOrientation
+ _objc_msgSend$_axAnnounceOrientationChangeIfNeeded:
+ _objc_msgSend$doubleValue
- -[LevelPageViewControllerAccessibility _updateForRotation:shiftAngle:]
- -[LevelPageViewControllerAccessibility _updateOffsetLabel:]
Functions:
~ -[AccessibilityStateObserverAccessibility axDescriptionForNumberOfPointsAndLines] : 1012 -> 1032
~ +[LevelPageViewControllerAccessibility _accessibilityPerformValidations:] : 328 -> 296
~ -[LevelPageViewControllerAccessibility _accessibilityLoadAccessibilityInformation] -> -[LevelPageViewControllerAccessibility _axAnnounceOrientationChangeIfNeeded:] : 256 -> 168
~ -[LevelPageViewControllerAccessibility viewDidLoad] -> -[LevelPageViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 76 -> 256
~ -[LevelPageViewControllerAccessibility _updateOffsetLabel:] -> -[LevelPageViewControllerAccessibility viewWillDisappear:] : 92 -> 76
~ -[LevelPageViewControllerAccessibility _updateForRotation:shiftAngle:] -> -[LevelPageViewControllerAccessibility updateDisplay:] : 232 -> 144
CStrings:
+ "Optional<LevelViewProtocol>"
+ "lastDisplayDegrees"
+ "updateDisplay:"
- "LevelView"
- "_orientation"
- "_updateForRotation: shiftAngle:"
- "_updateOffsetLabel:"

```
