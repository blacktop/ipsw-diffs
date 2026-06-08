## RemoteUIFramework

> `/System/Library/AccessibilityBundles/RemoteUIFramework.axbundle/RemoteUIFramework`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x197c
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_methlist: 0x19c
-  __TEXT.__cstring: 0x318
-  __TEXT.__const: 0x20
+3036.2.0.0.0
+  __TEXT.__text: 0x18d8
+  __TEXT.__objc_methlist: 0x1fc
+  __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x9c
+  __TEXT.__cstring: 0x35d
   __TEXT.__unwind_info: 0x100
-  __TEXT.__objc_classname: 0x128
-  __TEXT.__objc_methname: 0x5e5
-  __TEXT.__objc_methtype: 0x4e
-  __TEXT.__objc_stubs: 0x640
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x120
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x500
-  __AUTH_CONST.__objc_const: 0x510
+  __AUTH_CONST.__cfstring: 0x540
+  __AUTH_CONST.__objc_const: 0x630
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xa0
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6FEC3A8A-68FA-34BE-87ED-0088910ED4F6
-  Functions: 42
-  Symbols:   251
-  CStrings:  167
+  UUID: 19A089BD-37B1-316D-A7E4-E116E9B97342
+  Functions: 48
+  Symbols:   274
+  CStrings:  92
 
Symbols:
+ +[RemoteUIModernTableViewCellAccessibility _accessibilityPerformValidations:]
+ +[RemoteUIModernTableViewCellAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[RemoteUIModernTableViewCellAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[RemoteUIModernTableViewCellAccessibility accessibilityLabel]
+ -[RemoteUIModernTableViewCellAccessibility accessibilityTraits]
+ -[RemoteUIModernTableViewCellAccessibility isAccessibilityElement]
+ GCC_except_table26
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table40
+ _OBJC_CLASS_$_RemoteUIModernTableViewCellAccessibility
+ _OBJC_CLASS_$___RemoteUIModernTableViewCellAccessibility_super
+ _OBJC_METACLASS_$_RemoteUIModernTableViewCellAccessibility
+ _OBJC_METACLASS_$___RemoteUIModernTableViewCellAccessibility_super
+ _UIAXStringForAllChildren
+ __OBJC_$_CLASS_METHODS_RemoteUIModernTableViewCellAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_RemoteUIModernTableViewCellAccessibility
+ __OBJC_CLASS_RO_$_RemoteUIModernTableViewCellAccessibility
+ __OBJC_CLASS_RO_$___RemoteUIModernTableViewCellAccessibility_super
+ __OBJC_METACLASS_RO_$_RemoteUIModernTableViewCellAccessibility
+ __OBJC_METACLASS_RO_$___RemoteUIModernTableViewCellAccessibility_super
+ ___Block_byref_object_copy_.107
+ ___Block_byref_object_dispose_.108
+ ___block_literal_global.32
+ ___block_literal_global.369
+ ___block_literal_global.375
+ ___block_literal_global.68
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x8
- GCC_except_table11
- GCC_except_table3
- GCC_except_table5
- GCC_except_table9
- ___block_literal_global.348
- ___block_literal_global.354
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x24
CStrings:
+ "RemoteUIModernTableViewCell"
+ "RemoteUIModernTableViewCellAccessibility"
- "#16@0:8"
- "@16@0:8"
- "AXRemoteUIGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "URLAttributeForImageName:getScale:"
- "__RUIPageAccessibility_super"
- "__RUITableViewRowAccessibility_super"
- "__RUIWebContainerViewAccessibility_super"
- "__RemoteUITableViewCellAccessibility_super"
- "_accessibilityActivationDelay"
- "_accessibilityAncestorIsKindOf:"
- "_accessibilityFindSubviewDescendant:"
- "_accessibilityLeafDescendantsWithOptions:"
- "_accessibilityPerformValidations:"
- "_axSubviewText"
- "_privateAccessibilityCustomActions"
- "absoluteString"
- "accessibilityActivationPoint"
- "accessibilityContainer"
- "accessibilityIdentifier"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityPerformEscape"
- "accessibilityTraits"
- "ax_filteredArrayUsingBlock:"
- "bundleForClass:"
- "childViewControllers"
- "componentsSeparatedByString:"
- "count"
- "dataSource"
- "defaultVoiceOverOptions"
- "dismissViewControllerAnimated:completion:"
- "f16@0:8"
- "firstObject"
- "indexPathForCell:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "intValue"
- "isAccessibilityElement"
- "isEqualToString:"
- "lastObject"
- "lastPathComponent"
- "localizedStringForKey:value:table:"
- "navigationController"
- "objectForKey:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "popViewControllerAnimated:"
- "presentingViewController"
- "safeArrayForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeUIViewForKey:"
- "safeValueForKey:"
- "safeValueForKeyPath:"
- "setAccessibilityIdentifier:"
- "setDebugBuild:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "{CGPoint=dd}16@0:8"

```
