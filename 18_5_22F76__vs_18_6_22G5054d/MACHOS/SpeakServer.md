## SpeakServer

> `/System/Library/AccessibilityBundles/SpeakServer.axuiservice/SpeakServer`

```diff

-3148.15.26.0.0
-  __TEXT.__text: 0x3344
+3148.15.34.0.0
+  __TEXT.__text: 0x33bc
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0xe40
+  __TEXT.__objc_stubs: 0xe80
   __TEXT.__objc_methlist: 0x40c
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x60
   __TEXT.__cstring: 0x1d8
   __TEXT.__objc_classname: 0x29
-  __TEXT.__objc_methname: 0x12ee
-  __TEXT.__oslogstring: 0x34a
+  __TEXT.__objc_methname: 0x131d
+  __TEXT.__oslogstring: 0x396
   __TEXT.__objc_methtype: 0x3e3
   __TEXT.__unwind_info: 0x128
   __DATA_CONST.__auth_got: 0x238
-  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x258
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x500
-  __DATA.__objc_selrefs: 0x4f0
+  __DATA.__objc_selrefs: 0x500
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
-  UUID: EE1E022C-17CB-3150-B571-A5954C30A468
+  UUID: 692B5C38-86E5-3D28-B7A1-0A59BEA652E4
   Functions: 63
-  Symbols:   113
-  CStrings:  304
+  Symbols:   115
+  CStrings:  307
 
Symbols:
+ _MCFeatureAccessibilityTypingFeedbackAllowed
+ _OBJC_CLASS_$_MCProfileConnection
Functions:
~ sub_3fbc -> sub_4034 : 240 -> 360
CStrings:
+ "Will NOT speak action due to ManagedConfiguration restrictions: %{private}@"
+ "effectiveBoolValueForSetting:"
+ "sharedConnection"

```
