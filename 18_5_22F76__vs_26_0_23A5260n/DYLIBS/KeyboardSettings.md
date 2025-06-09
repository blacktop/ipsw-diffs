## KeyboardSettings

> `/System/Library/PrivateFrameworks/KeyboardSettings.framework/KeyboardSettings`

```diff

-109.300.0.0.0
-  __TEXT.__text: 0x28364
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x2960
+119.0.0.0.0
+  __TEXT.__text: 0x28d9c
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_methlist: 0x2990
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x2fc
-  __TEXT.__cstring: 0x34f1
+  __TEXT.__cstring: 0x3617
   __TEXT.__oslogstring: 0x3
   __TEXT.__dlopen_cstrs: 0x117
   __TEXT.__ustring: 0x52
-  __TEXT.__unwind_info: 0x8f0
+  __TEXT.__unwind_info: 0x8f8
   __TEXT.__objc_classname: 0x5c7
-  __TEXT.__objc_methname: 0x8906
-  __TEXT.__objc_methtype: 0x16f0
-  __TEXT.__objc_stubs: 0x6640
-  __DATA_CONST.__got: 0x730
+  __TEXT.__objc_methname: 0x89ff
+  __TEXT.__objc_methtype: 0x17c0
+  __TEXT.__objc_stubs: 0x6660
+  __DATA_CONST.__got: 0x740
   __DATA_CONST.__const: 0x798
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22c0
+  __DATA_CONST.__objc_selrefs: 0x22e8
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x2b8
-  __AUTH_CONST.__auth_got: 0x570
-  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__auth_got: 0x578
+  __AUTH_CONST.__const: 0x2e0
   __AUTH_CONST.__cfstring: 0x3360
-  __AUTH_CONST.__objc_const: 0x3430
+  __AUTH_CONST.__objc_const: 0x3450
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_doubleobj: 0x20

   __AUTH.__objc_data: 0xaa0
   __DATA.__objc_ivar: 0x1d4
   __DATA.__data: 0x540
-  __DATA.__bss: 0xd8
+  __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D811D33-DB40-3919-BA57-FDDC7CEE13A7
-  Functions: 846
-  Symbols:   3444
-  CStrings:  2466
+  UUID: 669A0F1A-947D-3B55-8617-0B2355CC1DF1
+  Functions: 853
+  Symbols:   3455
+  CStrings:  2482
 
Symbols:
+ -[KSSoftwareLayoutDetailControllerViewController removeInputModeInMultilingualSet:].cold.1
+ GCC_except_table68
+ _OBJC_CLASS_$_NSOrderedSet
+ _TIInputModePropertiesSupportedMultiscriptInputModes
+ _TIUIGetProposedMultilingualSetByAddingInputMode.cold.1
+ _TIUIGetProposedMultilingualSetByAddingInputMode.cold.2
+ _TIUIGetProposedMultilingualSetsForAddingInputMode.cold.2
+ _TIUIGetProposedMultilingualSetsForAddingInputMode.cold.3
+ _TIUIKeyboardGetSupportedSoftwareMultiscriptLayouts
+ _TIUIMultilingualSetIsMonoscriptInput
+ _TIUIMultilingualSetIsMultiscriptInput
+ __TIUIMultilingualSetIsMultiscriptInputInOrder
+ ___block_literal_global.147
+ ___block_literal_global.155
+ ___block_literal_global.190
+ ___block_literal_global.389
+ ___block_literal_global.729
+ _objc_msgSend$minusOrderedSet:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_retain_x28
- -[KSKeyboardController feedbackFeatureEnabled].cold.2
- GCC_except_table69
- ___46-[KSKeyboardController feedbackFeatureEnabled]_block_invoke
- ___block_literal_global.113
- ___block_literal_global.138
- ___block_literal_global.146
- ___block_literal_global.181
- ___block_literal_global.237
- ___block_literal_global.401
- ___block_literal_global.741
- _feedbackFeatureEnabled.is_internal_install
- _feedbackFeatureEnabled.once_token
- _objc_msgSend$boolForKey:
CStrings:
+ "%s Feedback %@: RC_SEED_BUILD: 1 enabled: %d"
+ "-[KSSoftwareLayoutDetailControllerViewController removeInputModeInMultilingualSet:]"
+ "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
+ "@\"UIMenu\"40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSArray\"32"
+ "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
+ "B40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSString\"32"
+ "KeyboardMultiscriptEnabled"
+ "SWLayouts-Multiscript"
+ "TIUIGetProposedMultilingualSetByAddingInputMode"
+ "TIUIGetProposedMultilingualSetsForAddingInputMode"
+ "[proposedSet count] == 2"
+ "[supportedMultiscriptLayouts count] > 0"
+ "firstLayout"
+ "minusOrderedSet:"
+ "multiscript_keyboard_expansion1"
+ "reverseObjectEnumerator"
+ "textField:editMenuForCharactersInRanges:suggestedActions:"
+ "textField:shouldChangeCharactersInRanges:replacementString:"
+ "textView:editMenuForTextInRanges:suggestedActions:"
+ "textView:shouldChangeTextInRanges:replacementText:"
- "%s Feedback %@: RC_SEED_BUILD: 0 enabled: %d"
- "apple-internal-install"
- "boolForKey:"

```
