## InCallService

> `/System/Library/AccessibilityBundles/InCallService.axbundle/InCallService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x4d0c
+3048.0.0.0.0
+  __TEXT.__text: 0x4e7c
   __TEXT.__objc_methlist: 0x8d8
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__cstring: 0xf33
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__cstring: 0xf44
   __TEXT.__oslogstring: 0x5f
   __TEXT.__unwind_info: 0x260
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__const: 0x200
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x520
+  __DATA_CONST.__objc_selrefs: 0x528
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1560
+  __AUTH_CONST.__cfstring: 0x1580
   __AUTH_CONST.__objc_const: 0x1830
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 176
-  Symbols:   643
-  CStrings:  188
+  Functions: 177
+  Symbols:   645
+  CStrings:  189
 
Symbols:
+ GCC_except_table157
+ GCC_except_table171
+ ___72-[PHSlidingViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2
+ _objc_msgSend$attributedText
- GCC_except_table156
- GCC_except_table170
Functions:
~ +[PHSlidingViewAccessibility _accessibilityPerformValidations:] : 372 -> 400
~ -[PHSlidingViewAccessibility _accessibilityLoadAccessibilityInformation] : 320 -> 560
+ -[PHSlidingViewAccessibility repeatingUpdateAnimatedSliderForCountdownNumber:forModel:]
CStrings:
+ "descriptionLabel"
```
