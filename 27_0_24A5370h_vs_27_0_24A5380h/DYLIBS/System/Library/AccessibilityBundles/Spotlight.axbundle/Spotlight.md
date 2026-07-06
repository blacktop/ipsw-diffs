## Spotlight

> `/System/Library/AccessibilityBundles/Spotlight.axbundle/Spotlight`

```diff

-  __TEXT.__text: 0x7ac
-  __TEXT.__objc_methlist: 0xd4
-  __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x137
-  __TEXT.__oslogstring: 0x51
-  __TEXT.__unwind_info: 0xa0
+  __TEXT.__text: 0x1b0
+  __TEXT.__objc_methlist: 0x14
+  __TEXT.__cstring: 0x62
+  __TEXT.__unwind_info: 0x70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb8
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__objc_selrefs: 0x48
+  __DATA_CONST.__got: 0x18
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__cfstring: 0x80
+  __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 20
-  Symbols:   133
-  CStrings:  31
+  Functions: 5
+  Symbols:   47
+  CStrings:  9
 
Sections:
~ __AUTH_CONST.__const : content changed
Symbols:
- +[SPUISearchBarWindowAccessibility _accessibilityPerformValidations:]
- +[SPUISearchBarWindowAccessibility(SafeCategory) safeCategoryBaseClass]
- +[SPUISearchBarWindowAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[SPUISecureWindowAccessibility _accessibilityPerformValidations:]
- +[SPUISecureWindowAccessibility(SafeCategory) safeCategoryBaseClass]
- +[SPUISecureWindowAccessibility(SafeCategory) safeCategoryTargetClassName]
- -[SPUISearchBarWindowAccessibility _accessibilityIgnoresStatusBarFrame]
- -[SPUISearchBarWindowAccessibility _accessibilityLoadAccessibilityInformation]
- -[SPUISearchBarWindowAccessibility accessibilityElementsHidden]
- -[SPUISearchBarWindowAccessibility dealloc]
- -[SPUISearchBarWindowAccessibility init]
- -[SPUISecureWindowAccessibility accessibilityElementsHidden]
- _AXLogCommon
- _AXPerformBlockAsynchronouslyOnMainThread
- _OBJC_CLASS_$_AXSpringBoardServer
- _OBJC_CLASS_$_SPUISearchBarWindowAccessibility
- _OBJC_CLASS_$_SPUISecureWindowAccessibility
- _OBJC_CLASS_$_UIAccessibilitySafeCategory
- _OBJC_CLASS_$_UIWindow
- _OBJC_CLASS_$___SPUISearchBarWindowAccessibility_super
- _OBJC_CLASS_$___SPUISecureWindowAccessibility_super
- _OBJC_METACLASS_$_SPUISearchBarWindowAccessibility
- _OBJC_METACLASS_$_SPUISecureWindowAccessibility
- _OBJC_METACLASS_$_UIAccessibilitySafeCategory
- _OBJC_METACLASS_$___SPUISearchBarWindowAccessibility_super
- _OBJC_METACLASS_$___SPUISecureWindowAccessibility_super
- __NSConcreteStackBlock
- __OBJC_$_CLASS_METHODS_SPUISearchBarWindowAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_SPUISecureWindowAccessibility(SafeCategory)
- __OBJC_$_INSTANCE_METHODS_SPUISearchBarWindowAccessibility
- __OBJC_$_INSTANCE_METHODS_SPUISecureWindowAccessibility
- __OBJC_CLASS_RO_$_SPUISearchBarWindowAccessibility
- __OBJC_CLASS_RO_$_SPUISecureWindowAccessibility
- __OBJC_CLASS_RO_$___SPUISearchBarWindowAccessibility_super
- __OBJC_CLASS_RO_$___SPUISecureWindowAccessibility_super
- __OBJC_METACLASS_RO_$_SPUISearchBarWindowAccessibility
- __OBJC_METACLASS_RO_$_SPUISecureWindowAccessibility
- __OBJC_METACLASS_RO_$___SPUISearchBarWindowAccessibility_super
- __OBJC_METACLASS_RO_$___SPUISecureWindowAccessibility_super
- ___78-[SPUISearchBarWindowAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
- ___UIAccessibilityCastAsClass
- ___block_descriptor_40_e8_32s_e18_v16?0"NSString"8ls32l8
- ___block_descriptor_40_e8_32s_e25_v24?0q8"NSDictionary"16ls32l8
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- __os_log_debug_impl
- __os_log_impl
- _abort
- _objc_msgSend$_accessibilityBoolValueForKey:
- _objc_msgSend$_accessibilityLoadAccessibilityInformation
- _objc_msgSend$_accessibilitySetBoolValue:forKey:
- _objc_msgSend$_accessibilitySetRetainedValue:forKey:
- _objc_msgSend$_accessibilityValueForKey:
- _objc_msgSend$activationState
- _objc_msgSend$boolValue
- _objc_msgSend$installSafeCategory:canInteractWithTargetClass:
- _objc_msgSend$isSpotlightVisible
- _objc_msgSend$objectForKeyedSubscript:
- _objc_msgSend$registerSpringBoardActionHandler:withIdentifierCallback:
- _objc_msgSend$removeActionHandler:
- _objc_msgSend$server
- _objc_msgSend$validateClass:isKindOfClass:
- _objc_msgSend$windowScene
- _objc_msgSendSuper2
- _objc_release
- _objc_release_x20
- _objc_release_x21
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x2
- _os_log_type_enabled
Functions:
~ ___48+[AXSpotlightGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 4
CStrings:
- "SPUISearchBarWindow"
- "SPUISearchBarWindowAccessibility"
- "SPUISecureWindow"
- "SPUISecureWindowAccessibility"
- "Spotlight register: %@"
- "Spotlight visible change: %@"
- "Spotlight visible status: %d"
- "UIWindow"
- "actionHandlerIdentifier"
- "isSpotlightVisible"
- "isVisible"
- "v16@?0@\"NSString\"8"
- "v24@?0q8@\"NSDictionary\"16"
- "v8@?0"

```
