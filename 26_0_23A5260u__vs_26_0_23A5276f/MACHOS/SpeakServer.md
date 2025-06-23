## SpeakServer

> `/System/Library/AccessibilityBundles/SpeakServer.axuiservice/SpeakServer`

```diff

-3180.6.1.0.0
-  __TEXT.__text: 0x3364
+3183.1.0.0.0
+  __TEXT.__text: 0x33dc
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0xe60
+  __TEXT.__objc_stubs: 0xea0
   __TEXT.__objc_methlist: 0x40c
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x60
   __TEXT.__cstring: 0x1d8
   __TEXT.__objc_classname: 0x29
-  __TEXT.__objc_methname: 0x12fb
-  __TEXT.__oslogstring: 0x2fe
+  __TEXT.__objc_methname: 0x132a
+  __TEXT.__oslogstring: 0x34a
   __TEXT.__objc_methtype: 0x3e3
   __TEXT.__unwind_info: 0x130
   __DATA_CONST.__auth_got: 0x238
-  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x280
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x500
-  __DATA.__objc_selrefs: 0x4f8
+  __DATA.__objc_selrefs: 0x508
   __DATA.__objc_ivar: 0x40
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/SpeakTypingServices.framework/SpeakTypingServices
   - /System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9B829310-5FD4-3845-AE53-877A5915A338
+  UUID: 67FDC9B5-9B5F-336B-B74B-7CCBC10DFA12
   Functions: 64
-  Symbols:   113
-  CStrings:  304
+  Symbols:   115
+  CStrings:  307
 
Symbols:
+ _MCFeatureAccessibilityTypingFeedbackAllowed
+ _OBJC_CLASS_$_MCProfileConnection
Functions:
~ sub_3fdc -> sub_4054 : 240 -> 360
CStrings:
+ "Will NOT speak action due to ManagedConfiguration restrictions: %{private}@"
+ "effectiveBoolValueForSetting:"
+ "sharedConnection"

```
