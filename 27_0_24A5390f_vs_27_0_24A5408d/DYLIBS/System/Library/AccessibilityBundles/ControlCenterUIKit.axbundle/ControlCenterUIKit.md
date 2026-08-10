## ControlCenterUIKit

> `/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/ControlCenterUIKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x586c
-  __TEXT.__objc_methlist: 0x82c
+3048.0.0.0.0
+  __TEXT.__text: 0x5864
+  __TEXT.__objc_methlist: 0x834
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x180
   __TEXT.__cstring: 0xe8c
-  __TEXT.__oslogstring: 0x8
   __TEXT.__unwind_info: 0x280
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 185
-  Symbols:   576
-  CStrings:  145
+  Functions: 186
+  Symbols:   574
+  CStrings:  144
 
Symbols:
+ -[CCUIButtonModuleViewControllerAccessibility viewWillAppear:]
+ GCC_except_table171
- GCC_except_table170
- _AXLogTemp
- __os_log_debug_impl
- _os_log_type_enabled
Functions:
~ -[CCUIButtonModuleViewControllerAccessibility _accessibilityControlCenterRoundButtonIdentifier] : 276 -> 192
CStrings:
- "SUP MAN"
```
