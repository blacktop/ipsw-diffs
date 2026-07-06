## InCallService

> `/System/Library/AccessibilityBundles/InCallService.axbundle/InCallService`

```diff

-  __TEXT.__text: 0x4920
-  __TEXT.__objc_methlist: 0x858
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__cstring: 0xe3a
+  __TEXT.__text: 0x4d40
+  __TEXT.__objc_methlist: 0x8d8
+  __TEXT.__const: 0x20
+  __TEXT.__gcc_except_tab: 0xb8
+  __TEXT.__cstring: 0xf25
   __TEXT.__oslogstring: 0x5f
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__unwind_info: 0x268
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c0
-  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__const: 0x228
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e8
-  __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__objc_selrefs: 0x518
+  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1360
-  __AUTH_CONST.__objc_const: 0x1710
+  __AUTH_CONST.__cfstring: 0x1540
+  __AUTH_CONST.__objc_const: 0x1830
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__bss: 0x20
+  __AUTH.__objc_data: 0xa0
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0xcd0
+  __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 163
-  Symbols:   773
-  CStrings:  326
+  Functions: 176
+  Symbols:   818
+  CStrings:  356
 
Sections:
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[PHCarPlayNumberPadButtonAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[PHCarPlayNumberPadButtonAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[PHCarPlayNumberPadButtonAccessibility _accessibilityKeyboardKeyAllowsTouchTyping]
+ -[PHCarPlayNumberPadButtonAccessibility _accessibilityNumberPadCharacter]
+ -[PHCarPlayNumberPadButtonAccessibility accessibilityLabel]
+ -[PHCarPlayNumberPadButtonAccessibility accessibilityPath]
+ -[PHCarPlayNumberPadButtonAccessibility accessibilityTraits]
+ -[PHCarPlayNumberPadButtonAccessibility accessibilityValue]
+ -[PHCarPlayNumberPadButtonAccessibility isAccessibilityElement]
+ GCC_except_table156
+ GCC_except_table170
+ _NSClassFromString
+ _OBJC_CLASS_$_PHCarPlayNumberPadButtonAccessibility
+ _OBJC_CLASS_$___PHCarPlayNumberPadButtonAccessibility_super
+ _OBJC_METACLASS_$_PHCarPlayNumberPadButtonAccessibility
+ _OBJC_METACLASS_$___PHCarPlayNumberPadButtonAccessibility_super
+ _UIAccessibilityTraitKeyboardKey
+ _UIAccessibilityTraitPlaysSound
+ __OBJC_$_CLASS_METHODS_PHCarPlayNumberPadButtonAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_PHCarPlayNumberPadButtonAccessibility
+ __OBJC_CLASS_RO_$_PHCarPlayNumberPadButtonAccessibility
+ __OBJC_CLASS_RO_$___PHCarPlayNumberPadButtonAccessibility_super
+ __OBJC_METACLASS_RO_$_PHCarPlayNumberPadButtonAccessibility
+ __OBJC_METACLASS_RO_$___PHCarPlayNumberPadButtonAccessibility_super
+ ___59-[PHCarPlayNumberPadButtonAccessibility accessibilityValue]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ _objc_msgSend$_accessibilityCirclePathBasedOnBoundsWidth
+ _objc_msgSend$_accessibilityNumberPadCharacter
+ _objc_msgSend$intValue
+ _objc_msgSend$isHidden
+ _objc_msgSend$localizedLettersForCharacter:
+ _objc_release_x1
- GCC_except_table158
CStrings:
+ "2.key.hint"
+ "3.key.hint"
+ "4.key.hint"
+ "5.key.hint"
+ "6.key.hint"
+ "7.key.hint"
+ "8.key.hint"
+ "9.key.hint"
+ "PHCarPlayNumberPadButton"
+ "PHCarPlayNumberPadButtonAccessibility"
+ "TPNumberPadButton"
+ "character"
+ "number.pad.delete"
+ "number.pad.octothorpe"
+ "number.pad.star"

```
