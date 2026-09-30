## KeyboardSettingsFeedback

> `/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`

```diff

 9126.6.3.0.0
-  __TEXT.__text: 0x1708
-  __TEXT.__auth_stubs: 0x270
+  __TEXT.__text: 0x178c
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_methlist: 0x1b4
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x476
+  __TEXT.__cstring: 0x4b7
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0xb8
+  __TEXT.__unwind_info: 0xc8
   __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0x838
+  __TEXT.__objc_methname: 0x857
   __TEXT.__objc_methtype: 0xb8
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0x70
+  __TEXT.__objc_stubs: 0x7a0
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x230
+  __DATA_CONST.__objc_selrefs: 0x240
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x140
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x2e0
+  __AUTH_CONST.__auth_got: 0x148
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0x340
   __AUTH_CONST.__objc_const: 0x310
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x28
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 57
-  Symbols:   200
-  CStrings:  141
+  Functions: 58
+  Symbols:   206
+  CStrings:  145
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_NSUserDefaults
+ ___47-[TUIFeedbackController feedbackFeatureEnabled]_block_invoke
+ _feedbackFeatureEnabled.is_internal_install
+ _feedbackFeatureEnabled.once_token
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$initWithSuiteName:
- _OUTLINED_FUNCTION_8
CStrings:
+ "%s Feedback %@: RC_SEED_BUILD: 0 enabled: %d"
+ "apple-internal-install"
+ "boolForKey:"
+ "com.apple.keyboard"
+ "initWithSuiteName:"
- "%s Feedback %@: RC_SEED_BUILD: 1 enabled: %d"
```
