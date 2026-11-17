## AudioConferenceControlCenterModule

> `/System/Library/AccessibilityBundles/AudioConferenceControlCenterModule.axbundle/AudioConferenceControlCenterModule`

```diff

-3050.3.12.0.0
-  __TEXT.__text: 0x968
+3050.3.22.0.0
+  __TEXT.__text: 0x980
   __TEXT.__objc_methlist: 0x1d8
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x2f5

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0x510
+  __AUTH_CONST.__objc_const: 0x538
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x4
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libAXSafeCategoryBundle.dylib
+  - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 43
-  Symbols:   142
+  Symbols:   143
   CStrings:  31
 
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
