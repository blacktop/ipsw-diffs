## AccessibilitySettingsLoader

> `/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader`

```diff

-3245.8.2.0.0
-  __TEXT.__text: 0x10f34
-  __TEXT.__objc_methlist: 0x11cc
+3245.8.4.2.0
+  __TEXT.__text: 0x117a8
+  __TEXT.__objc_methlist: 0x1204
   __TEXT.__dlopen_cstrs: 0x70c
-  __TEXT.__const: 0x78
+  __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x510
-  __TEXT.__cstring: 0x2036
-  __TEXT.__oslogstring: 0x651
-  __TEXT.__unwind_info: 0x838
+  __TEXT.__cstring: 0x2065
+  __TEXT.__oslogstring: 0x8aa
+  __TEXT.__unwind_info: 0x848
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x528
+  __DATA_CONST.__const: 0x548
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdb8
+  __DATA_CONST.__objc_selrefs: 0xdf0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x278
-  __AUTH_CONST.__const: 0x5e0
-  __AUTH_CONST.__cfstring: 0x1500
-  __AUTH_CONST.__objc_const: 0x23d0
+  __DATA_CONST.__got: 0x280
+  __AUTH_CONST.__const: 0x600
+  __AUTH_CONST.__cfstring: 0x1540
+  __AUTH_CONST.__objc_const: 0x2400
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x130

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 399
-  Symbols:   1014
-  CStrings:  324
+  Functions: 405
+  Symbols:   1027
+  CStrings:  336
 
Symbols:
+ -[AccessibilityFloatingUIKeyboardHelper _handleFirstResponderDidChangeNotification:]
+ -[AccessibilityFloatingUIKeyboardHelper _startObservingTextInput]
+ -[AccessibilityFloatingUIKeyboardHelper _stopObservingTextInput]
+ -[AccessibilityFloatingUIKeyboardHelper observingTextInput]
+ -[AccessibilityFloatingUIKeyboardHelper setObservingTextInput:]
+ GCC_except_table292
+ GCC_except_table293
+ GCC_except_table305
+ GCC_except_table312
+ GCC_except_table324
+ GCC_except_table338
+ GCC_except_table343
+ GCC_except_table348
+ GCC_except_table359
+ GCC_except_table361
+ GCC_except_table369
+ GCC_except_table399
+ _LiveSpeechLogCommon
+ _NSStringFromClass
+ _OBJC_CLASS_$_UIWindow
+ _OBJC_IVAR_$_AccessibilityFloatingUIKeyboardHelper._observingTextInput
+ ___84-[AccessibilityFloatingUIKeyboardHelper _handleFirstResponderDidChangeNotification:]_block_invoke
+ ___block_descriptor_32_e34_v24?0"NSDictionary"8"NSError"16l
+ _objc_release_x27
+ _objc_release_x28
- GCC_except_table289
- GCC_except_table290
- GCC_except_table303
- GCC_except_table310
- GCC_except_table318
- GCC_except_table320
- GCC_except_table336
- GCC_except_table337
- GCC_except_table353
- GCC_except_table355
- GCC_except_table363
- GCC_except_table393
CStrings:
+ "FloatingUIKB: first responder changed responder=%{public}@ isTextInput=%d scene=%{public}@ activationState=%ld"
+ "FloatingUIKB: ignoring, scene is not foreground active"
+ "FloatingUIKB: listener state update, liveSpeechEnabled=%d observing=%d"
+ "FloatingUIKB: observing first responder changes in %{public}@"
+ "FloatingUIKB: reporting text input to AXUIServer, scene %{public}@"
+ "FloatingUIKB: skipping monitoring in %{public}@ (pid %d)"
+ "FloatingUIKB: starting monitoring in %{public}@ (pid %d)"
+ "FloatingUIKB: stopped observing first responder changes in %{public}@"
+ "FloatingUIKB: text input report failed: %{public}@"
+ "nil"
+ "sceneID"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
```
