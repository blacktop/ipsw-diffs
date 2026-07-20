## InCallService

> `/System/Library/AccessibilityBundles/InCallService.axbundle/InCallService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-3042.0.0.0.0
-  __TEXT.__text: 0x4d40
+3045.0.0.0.0
+  __TEXT.__text: 0x4d0c
   __TEXT.__objc_methlist: 0x8d8
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__cstring: 0xf25
+  __TEXT.__cstring: 0xf33
   __TEXT.__oslogstring: 0x5f
-  __TEXT.__unwind_info: 0x268
+  __TEXT.__unwind_info: 0x260
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x228
+  __DATA_CONST.__const: 0x200
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x518
+  __DATA_CONST.__objc_selrefs: 0x520
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1540
+  __AUTH_CONST.__cfstring: 0x1560
   __AUTH_CONST.__objc_const: 0x1830
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 176
-  Symbols:   644
-  CStrings:  187
+  Symbols:   643
+  CStrings:  188
 
Symbols:
+ _objc_msgSend$buttonPressed
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- _objc_msgSend$buttonPressed:
Functions:
~ +[PHSOSViewControllerAccessibility _accessibilityPerformValidations:] : 424 -> 416
~ -[PHSOSViewControllerAccessibility accessibilityPerformEscape] : 192 -> 152
~ ___62-[PHSOSViewControllerAccessibility accessibilityPerformEscape]_block_invoke : 12 -> 8
CStrings:
+ "buttonPressed"
```
