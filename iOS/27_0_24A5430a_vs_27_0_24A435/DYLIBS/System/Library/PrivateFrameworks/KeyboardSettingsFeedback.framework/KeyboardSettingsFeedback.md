## KeyboardSettingsFeedback

> `/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback`

```diff

 9127.0.84.1.113
-  __TEXT.__text: 0x150c
+  __TEXT.__text: 0x15b4
   __TEXT.__objc_methlist: 0x1b4
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x478
+  __TEXT.__cstring: 0x4b9
   __TEXT.__oslogstring: 0x3
   __TEXT.__unwind_info: 0xc0
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x230
+  __DATA_CONST.__objc_selrefs: 0x240
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x70
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x2e0
+  __DATA_CONST.__got: 0x78
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0x340
   __AUTH_CONST.__objc_const: 0x310
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 54
-  Symbols:   200
-  CStrings:  34
+  Functions: 56
+  Symbols:   207
+  CStrings:  37
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_NSUserDefaults
+ ___47-[TUIFeedbackController feedbackFeatureEnabled]_block_invoke
+ _feedbackFeatureEnabled.is_internal_install
+ _feedbackFeatureEnabled.once_token
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$initWithSuiteName:
Functions:
~ -[TUIFeedbackController feedbackFeatureEnabled] : 84 -> 184
+ ___47-[TUIFeedbackController feedbackFeatureEnabled]_block_invoke
~ _OUTLINED_FUNCTION_1 : 24 -> 20
~ _OUTLINED_FUNCTION_3 : 20 -> 24
~ -[TUIFeedbackController feedbackFeatureEnabled].cold.1 : 136 -> 20
+ -[TUIFeedbackController feedbackFeatureEnabled].cold.2
CStrings:
+ "%s Feedback %@: RC_SEED_BUILD: 0 enabled: %d"
+ "apple-internal-install"
+ "com.apple.keyboard"
+ "feedbackFeatureEnabled"
- "%s Feedback %@: RC_SEED_BUILD: 1 enabled: %d"
```
