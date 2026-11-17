## ReplayKitModule

> `/System/Library/AccessibilityBundles/ReplayKitModule.axbundle/ReplayKitModule`

```diff

-3050.3.12.0.0
-  __TEXT.__text: 0x5d8
+3050.3.22.0.0
+  __TEXT.__text: 0x5f0
   __TEXT.__objc_methlist: 0x108
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x177

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__got: 0x40
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x240
+  __AUTH_CONST.__objc_const: 0x268
   __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x4
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libAXSafeCategoryBundle.dylib
+  - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 25
-  Symbols:   94
+  Symbols:   95
   CStrings:  18
 
Symbols:
+ _OBJC_IVAR_$_AXReplayKitClientDelegate._didDisableScreenCurtain
+ __AXSVoiceOverTouchScreenCurtainEnabled
+ __AXSVoiceOverTouchSetScreenCurtainEnabled
+ __OBJC_$_INSTANCE_VARIABLES_AXReplayKitClientDelegate
- _UIAccessibilityPostNotification
- ___kCFBooleanFalse
- ___kCFBooleanTrue
Functions:
~ -[AXReplayKitClientDelegate didStopRecordingOrBroadcast] : 120 -> 132
~ -[AXReplayKitClientDelegate didStartRecordingOrBroadcast] : 120 -> 132
```
