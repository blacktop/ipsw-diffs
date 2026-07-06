## SIMSetupUIService

> `/System/Library/AccessibilityBundles/SIMSetupUIService.axbundle/SIMSetupUIService`

```diff

-  __TEXT.__text: 0x5e4
-  __TEXT.__objc_methlist: 0xdc
-  __TEXT.__cstring: 0x16b
-  __TEXT.__unwind_info: 0x90
+  __TEXT.__text: 0x8b0
+  __TEXT.__objc_methlist: 0x12c
+  __TEXT.__cstring: 0x1f4
+  __TEXT.__unwind_info: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__objc_selrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__cfstring: 0x280
+  __AUTH_CONST.__objc_const: 0x3f0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x190
+  __AUTH.__objc_data: 0x230
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18
-  Symbols:   113
-  CStrings:  34
+  Functions: 23
+  Symbols:   150
+  CStrings:  46
 
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
Symbols:
+ +[TSDeviceInfoViewControllerAccessibility _accessibilityPerformValidations:]
+ +[TSDeviceInfoViewControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[TSDeviceInfoViewControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[TSDeviceInfoViewControllerAccessibility _accessibilityLoadAccessibilityInformation]
+ -[TSDeviceInfoViewControllerAccessibility tableView:viewForHeaderInSection:]
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_TSDeviceInfoViewControllerAccessibility
+ _OBJC_CLASS_$_UITableView
+ _OBJC_CLASS_$___TSDeviceInfoViewControllerAccessibility_super
+ _OBJC_METACLASS_$_TSDeviceInfoViewControllerAccessibility
+ _OBJC_METACLASS_$___TSDeviceInfoViewControllerAccessibility_super
+ _UIAccessibilitySpeechAttributeSpellOut
+ __OBJC_$_CLASS_METHODS_TSDeviceInfoViewControllerAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_TSDeviceInfoViewControllerAccessibility
+ __OBJC_CLASS_RO_$_TSDeviceInfoViewControllerAccessibility
+ __OBJC_CLASS_RO_$___TSDeviceInfoViewControllerAccessibility_super
+ __OBJC_METACLASS_RO_$_TSDeviceInfoViewControllerAccessibility
+ __OBJC_METACLASS_RO_$___TSDeviceInfoViewControllerAccessibility_super
+ ___UIAccessibilityCastAsClass
+ ___kCFBooleanTrue
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _abort
+ _objc_alloc
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$initWithString:attributes:
+ _objc_msgSend$length
+ _objc_msgSend$reloadData
+ _objc_msgSend$setAccessibilityAttributedLabel:
+ _objc_release_x22
+ _objc_release_x23
CStrings:
+ "TSDeviceInfoViewController"
+ "TSDeviceInfoViewControllerAccessibility"
+ "UITableViewCell"
+ "tableView"
+ "tableView:viewForHeaderInSection:"
+ "textLabel"

```
