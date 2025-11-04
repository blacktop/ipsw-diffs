## KeyboardSettingsFeedback

> `/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback`

```diff

-9126.1.12.1.105
-  __TEXT.__text: 0x1764
-  __TEXT.__auth_stubs: 0x2b0
+9126.2.2.0.0
+  __TEXT.__text: 0x16c0
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x1b4
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x4b7
+  __TEXT.__cstring: 0x476
   __TEXT.__oslogstring: 0x3
   __TEXT.__unwind_info: 0xc0
   __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0x857
+  __TEXT.__objc_methname: 0x838
   __TEXT.__objc_methtype: 0xb8
-  __TEXT.__objc_stubs: 0x7a0
-  __DATA_CONST.__got: 0x78
+  __TEXT.__objc_stubs: 0x760
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x240
+  __DATA_CONST.__objc_selrefs: 0x230
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x160
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x340
+  __AUTH_CONST.__auth_got: 0x158
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0x2e0
   __AUTH_CONST.__objc_const: 0x310
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x28
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63835748-16FE-375C-94B3-F7A6E9FFDAA1
-  Functions: 53
-  Symbols:   269
-  CStrings:  171
+  UUID: 18CB5C8A-2C5C-39EF-8599-68309F2B8B45
+  Functions: 51
+  Symbols:   258
+  CStrings:  163
 
Symbols:
+ ___block_literal_global.175
- -[TUIFeedbackController feedbackFeatureEnabled].cold.2
- _MGGetBoolAnswer
- _OBJC_CLASS_$_NSUserDefaults
- ___47-[TUIFeedbackController feedbackFeatureEnabled]_block_invoke
- ___block_literal_global.176
- ___block_literal_global.181
- _feedbackFeatureEnabled.is_internal_install
- _feedbackFeatureEnabled.once_token
- _objc_msgSend$boolForKey:
- _objc_msgSend$initWithSuiteName:
Functions:
~ -[TUIFeedbackController feedbackFeatureEnabled] : 184 -> 84
- ___47-[TUIFeedbackController feedbackFeatureEnabled]_block_invoke
~ -[TUIFeedbackController feedbackFeatureEnabled].cold.1 : 20 -> 204
- -[TUIFeedbackController feedbackFeatureEnabled].cold.2
CStrings:
+ "%s Feedback %@: RC_SEED_BUILD: 1 enabled: %d"
- "%s Feedback %@: RC_SEED_BUILD: 0 enabled: %d"
- "apple-internal-install"
- "boolForKey:"
- "com.apple.keyboard"
- "initWithSuiteName:"

```
