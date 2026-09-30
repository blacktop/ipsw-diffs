## SiriUI

> `/System/Library/AccessibilityBundles/SiriUI.axbundle/SiriUI`

```diff

-  __TEXT.__text: 0x1404
+  __TEXT.__text: 0x1294
   __TEXT.__objc_methlist: 0x344
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__cstring: 0x5b9
-  __TEXT.__unwind_info: 0x100
+  __TEXT.__cstring: 0x54d
+  __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x180
+  __DATA_CONST.__objc_selrefs: 0x170
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__got: 0x60
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x820
+  __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__objc_const: 0xbd0
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x8

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 64
-  Symbols:   324
-  CStrings:  139
+  Functions: 63
+  Symbols:   319
+  CStrings:  127
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
- ___69-[SiriUISiriStatusViewAccessibility accessibilityElementDidLoseFocus]_block_invoke
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- _objc_msgSend$_accessibilitySetBoolValue:forKey:
- _objc_msgSend$stopRequestWithOptions:
Functions:
~ +[SiriUISiriStatusViewAccessibility _accessibilityPerformValidations:] : 288 -> 184
~ -[SiriUISiriStatusViewAccessibility accessibilityElementDidLoseFocus] : 128 -> 60
- ___69-[SiriUISiriStatusViewAccessibility accessibilityElementDidLoseFocus]_block_invoke
CStrings:
- "AFUISiriSession"
- "AFUISiriView"
- "AFUISiriViewController"
- "VoiceOverCancelRequestInProgress"
- "_session"
- "cancelRequest"

```
