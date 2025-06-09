## InCallService

> `/System/Library/AccessibilityBundles/InCallService.axbundle/InCallService`

```diff

-2963.10.30.1.0
-  __TEXT.__text: 0x5e2c
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0xa68
-  __TEXT.__cstring: 0x11b1
+2994.2.0.0.0
+  __TEXT.__text: 0x4ea0
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_methlist: 0x8c8
+  __TEXT.__cstring: 0xf0a
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x100
+  __TEXT.__gcc_except_tab: 0xc8
   __TEXT.__oslogstring: 0x5f
-  __TEXT.__unwind_info: 0x2b0
-  __TEXT.__objc_classname: 0x7cf
-  __TEXT.__objc_methname: 0x1425
-  __TEXT.__objc_methtype: 0x120
-  __TEXT.__objc_stubs: 0x1160
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x208
-  __DATA_CONST.__objc_classlist: 0x188
+  __TEXT.__unwind_info: 0x250
+  __TEXT.__objc_classname: 0x6dd
+  __TEXT.__objc_methname: 0x1189
+  __TEXT.__objc_methtype: 0xc1
+  __TEXT.__objc_stubs: 0xe80
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__const: 0x1e8
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x648
-  __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x270
-  __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x16e0
-  __AUTH_CONST.__objc_const: 0x1b90
-  __AUTH_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_selrefs: 0x538
+  __DATA_CONST.__objc_superrefs: 0x78
+  __AUTH_CONST.__auth_got: 0x230
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x14c0
+  __AUTH_CONST.__objc_const: 0x1830
+  __AUTH_CONST.__objc_intobj: 0x18
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0xf50
+  __DATA_DIRTY.__objc_data: 0xd70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6599FA59-124E-3ED2-8C36-D0DE78E9D106
-  Functions: 205
-  Symbols:   957
-  CStrings:  658
+  UUID: 1143C0E5-0A56-30C7-B84E-2C1E7B1E7268
+  Functions: 171
+  Symbols:   814
+  CStrings:  575
 
Symbols:
+ ___block_literal_global.312
+ ___block_literal_global.321
- +[PHHandsetDialerDeleteButtonAccessibility _accessibilityPerformValidations:]
- +[PHHandsetDialerDeleteButtonAccessibility(SafeCategory) safeCategoryBaseClass]
- +[PHHandsetDialerDeleteButtonAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[PHHandsetDialerLCDViewAccessibility _accessibilityPerformValidations:]
- +[PHHandsetDialerLCDViewAccessibility(SafeCategory) safeCategoryBaseClass]
- +[PHHandsetDialerLCDViewAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[PHLCDViewTextFieldAccessibility _accessibilityPerformValidations:]
- +[PHLCDViewTextFieldAccessibility(SafeCategory) safeCategoryBaseClass]
- +[PHLCDViewTextFieldAccessibility(SafeCategory) safeCategoryTargetClassName]
- -[PHHandsetDialerDeleteButtonAccessibility _axDeleteButtonWasHidden]
- -[PHHandsetDialerDeleteButtonAccessibility _axSetDeleteButtonWasHidden:]
- -[PHHandsetDialerDeleteButtonAccessibility accessibilityLabel]
- -[PHHandsetDialerDeleteButtonAccessibility accessibilityTraits]
- -[PHHandsetDialerDeleteButtonAccessibility setAlpha:]
- -[PHHandsetDialerLCDViewAccessibility _accessibilityAllowedGeometryOverlap]
- -[PHHandsetDialerLCDViewAccessibility _accessibilityLoadAccessibilityInformation]
- -[PHHandsetDialerLCDViewAccessibility _accessibilitySubviews]
- -[PHHandsetDialerLCDViewAccessibility _voStatusChanged:]
- -[PHHandsetDialerLCDViewAccessibility dealloc]
- -[PHHandsetDialerLCDViewAccessibility deleteBackward]
- -[PHHandsetDialerLCDViewAccessibility deleteCharacter]
- -[PHHandsetDialerLCDViewAccessibility hasText]
- -[PHHandsetDialerLCDViewAccessibility initWithFrame:forDialerType:]
- -[PHHandsetDialerLCDViewAccessibility insertText:]
- -[PHHandsetDialerLCDViewAccessibility setText:needsFormat:]
- -[PHHandsetDialerLCDViewAccessibility shouldGroupAccessibilityChildren]
- -[PHHandsetDialerLCDViewAccessibility updateAddAndDeleteButtonForText:name:animated:]
- -[PHLCDViewTextFieldAccessibility _accessibilityPaste]
- -[PHLCDViewTextFieldAccessibility accessibilityValue]
- _NSClassFromString
- _OBJC_CLASS_$_NSCharacterSet
- _OBJC_CLASS_$_PHHandsetDialerDeleteButtonAccessibility
- _OBJC_CLASS_$_PHHandsetDialerLCDViewAccessibility
- _OBJC_CLASS_$_PHLCDViewTextFieldAccessibility
- _OBJC_CLASS_$_UIKeyboardImpl
- _OBJC_CLASS_$_UIView
- _OBJC_CLASS_$_UIWindow
- _OBJC_CLASS_$___PHHandsetDialerDeleteButtonAccessibility_super
- _OBJC_CLASS_$___PHHandsetDialerLCDViewAccessibility_super
- _OBJC_CLASS_$___PHLCDViewTextFieldAccessibility_super
- _OBJC_METACLASS_$_PHHandsetDialerDeleteButtonAccessibility
- _OBJC_METACLASS_$_PHHandsetDialerLCDViewAccessibility
- _OBJC_METACLASS_$_PHLCDViewTextFieldAccessibility
- _OBJC_METACLASS_$___PHHandsetDialerDeleteButtonAccessibility_super
- _OBJC_METACLASS_$___PHHandsetDialerLCDViewAccessibility_super
- _OBJC_METACLASS_$___PHLCDViewTextFieldAccessibility_super
- _UIAXStringForAllChildren
- _UIAccessibilityTokenSpeakDigits
- _UIAccessibilityTokenTextDeletion
- _UIAccessibilityTokenTextInsertion
- _UIAccessibilityTraitDeleteKey
- _UIAccessibilityTraitKeyboardKey
- _UIAccessibilityVoiceOverStatusDidChangeNotification
- _UIUnformattedPhoneNumberFromString
- __AXAssert
- __OBJC_$_CLASS_METHODS_PHHandsetDialerDeleteButtonAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_PHHandsetDialerLCDViewAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_PHLCDViewTextFieldAccessibility(SafeCategory)
- __OBJC_$_INSTANCE_METHODS_PHHandsetDialerDeleteButtonAccessibility
- __OBJC_$_INSTANCE_METHODS_PHHandsetDialerLCDViewAccessibility
- __OBJC_$_INSTANCE_METHODS_PHLCDViewTextFieldAccessibility
- __OBJC_CLASS_RO_$_PHHandsetDialerDeleteButtonAccessibility
- __OBJC_CLASS_RO_$_PHHandsetDialerLCDViewAccessibility
- __OBJC_CLASS_RO_$_PHLCDViewTextFieldAccessibility
- __OBJC_CLASS_RO_$___PHHandsetDialerDeleteButtonAccessibility_super
- __OBJC_CLASS_RO_$___PHHandsetDialerLCDViewAccessibility_super
- __OBJC_CLASS_RO_$___PHLCDViewTextFieldAccessibility_super
- __OBJC_METACLASS_RO_$_PHHandsetDialerDeleteButtonAccessibility
- __OBJC_METACLASS_RO_$_PHHandsetDialerLCDViewAccessibility
- __OBJC_METACLASS_RO_$_PHLCDViewTextFieldAccessibility
- __OBJC_METACLASS_RO_$___PHHandsetDialerDeleteButtonAccessibility_super
- __OBJC_METACLASS_RO_$___PHHandsetDialerLCDViewAccessibility_super
- __OBJC_METACLASS_RO_$___PHLCDViewTextFieldAccessibility_super
- ___50-[PHHandsetDialerLCDViewAccessibility insertText:]_block_invoke
- ___50-[PHHandsetDialerLCDViewAccessibility insertText:]_block_invoke_2
- ___61-[PHHandsetDialerLCDViewAccessibility _accessibilitySubviews]_block_invoke
- ___81-[PHHandsetDialerLCDViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
- ___81-[PHHandsetDialerLCDViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2
- ___PHHandsetDialerDeleteButton___axDeleteButtonWasHidden
- ___block_descriptor_32_e11_B24?08Q16l
- ___block_literal_global.309
- ___block_literal_global.318
- _objc_msgSend$_axDeleteButtonWasHidden
- _objc_msgSend$_axSetDeleteButtonWasHidden:
- _objc_msgSend$_callButtonPressed:
- _objc_msgSend$_voStatusChanged:
- _objc_msgSend$activeInstance
- _objc_msgSend$axFilterObjectsUsingBlock:
- _objc_msgSend$boolValue
- _objc_msgSend$bounds
- _objc_msgSend$canPerformAction:withSender:
- _objc_msgSend$characterAtIndex:
- _objc_msgSend$characterIsMember:
- _objc_msgSend$decimalDigitCharacterSet
- _objc_msgSend$firstResponder
- _objc_msgSend$keyWindow
- _objc_msgSend$numberWithDouble:
- _objc_msgSend$paste:
- _objc_msgSend$phonePad:appendString:
- _objc_msgSend$removeObserver:
- _objc_msgSend$setAccessibilityIdentifier:
- _objc_msgSend$setAccessibilityLabelBlock:
- _objc_msgSend$setDelegate:
- _objc_msgSend$substringFromIndex:
- _objc_msgSend$superview
- _objc_opt_isKindOfClass
- _objc_opt_respondsToSelector
- _objc_retain_x20
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
- "-[PHHandsetDialerLCDViewAccessibility insertText:]"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias6/MobilePhoneAccessibility/Accessibility/PHHandsetDialerLCDViewAccessibility.m"
- "@52@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16i48"
- "B24@?0@8Q16"
- "Delegate is not a dialerController"
- "DialerController"
- "PHDialerContactResultButtonView"
- "PHHandsetDialerDeleteButton"
- "PHHandsetDialerDeleteButtonAccessibility"
- "PHHandsetDialerLCDView"
- "PHHandsetDialerLCDViewAccessibility"
- "PHLCDViewTextField"
- "PHLCDViewTextFieldAccessibility"
- "__PHHandsetDialerDeleteButtonAccessibility_super"
- "__PHHandsetDialerLCDViewAccessibility_super"
- "__PHLCDViewTextFieldAccessibility_super"
- "_accessibilityAllowedGeometryOverlap"
- "_accessibilityPaste"
- "_accessibilitySubviews"
- "_axDeleteButtonWasHidden"
- "_axSetDeleteButtonWasHidden:"
- "_callButtonPressed:"
- "_numberTextField"
- "_voStatusChanged:"
- "activeInstance"
- "axFilterObjectsUsingBlock:"
- "boolValue"
- "bounds"
- "canPerformAction:withSender:"
- "characterAtIndex:"
- "characterIsMember:"
- "contactCountButton"
- "contactResultButton"
- "d16@0:8"
- "decimalDigitCharacterSet"
- "delete.title"
- "deleteBackward"
- "deleteCharacter"
- "firstResponder"
- "hasText"
- "initWithFrame: forDialerType:"
- "initWithFrame:forDialerType:"
- "insertText:"
- "keyWindow"
- "numberWithDouble:"
- "paste:"
- "phonePad:appendString:"
- "phonePadView"
- "removeObserver:"
- "setAccessibilityIdentifier:"
- "setAccessibilityLabelBlock:"
- "setAlpha:"
- "setDelegate:"
- "setText:needsFormat:"
- "substringFromIndex:"
- "superview"
- "updateAddAndDeleteButtonForText: name: animated:"
- "updateAddAndDeleteButtonForText:name:animated:"
- "v24@0:8d16"
- "v28@0:8@16B24"
- "v36@0:8@16@24B32"
- "{CGRect={CGPoint=dd}{CGSize=dd}}"

```
