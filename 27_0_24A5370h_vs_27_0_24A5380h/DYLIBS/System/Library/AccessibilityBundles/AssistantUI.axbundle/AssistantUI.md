## AssistantUI

> `/System/Library/AccessibilityBundles/AssistantUI.axbundle/AssistantUI`

```diff

-  __TEXT.__text: 0x1d68
-  __TEXT.__objc_methlist: 0x20c
-  __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x62b
-  __TEXT.__oslogstring: 0x77
+  __TEXT.__text: 0x1b68
+  __TEXT.__objc_methlist: 0x204
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x5e7
+  __TEXT.__oslogstring: 0x35
   __TEXT.__unwind_info: 0xf0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x258
+  __DATA_CONST.__objc_selrefs: 0x238
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x800
+  __AUTH_CONST.__cfstring: 0x780
   __AUTH_CONST.__objc_const: 0x510
   __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 45
-  Symbols:   279
-  CStrings:  147
+  Functions: 44
+  Symbols:   271
+  CStrings:  138
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
- -[AFUISiriSessionAccessibility cancelRequest]
- _AXIsInternalInstall
- _OBJC_CLASS_$_NSNumber
- _objc_msgSend$_accessibilityBoolValueForKey:
- _objc_msgSend$_accessibilitySetBoolValue:forKey:
- _objc_msgSend$numberWithBool:
- _objc_unsafeClaimAutoreleasedReturnValue
Functions:
~ +[AFUISiriSessionAccessibility _accessibilityPerformValidations:] : 216 -> 148
- -[AFUISiriSessionAccessibility cancelRequest]
~ +[AFUISiriCompactViewAccessibility _accessibilityPerformValidations:] : 532 -> 472
~ ___68-[AFUISiriCompactViewAccessibility accessibilityElementDidLoseFocus]_block_invoke : 272 -> 184
CStrings:
- "Transferring voice cancel request in progress %@ to connection %@"
- "VoiceOverCancelRequestInProgress"
- "_connection"
- "_session"
- "cancelRequest"

```
