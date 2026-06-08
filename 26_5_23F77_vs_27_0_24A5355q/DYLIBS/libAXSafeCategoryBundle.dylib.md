## libAXSafeCategoryBundle.dylib

> `/usr/lib/libAXSafeCategoryBundle.dylib`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x121c
-  __TEXT.__auth_stubs: 0x320
+3229.1.6.0.0
+  __TEXT.__text: 0x1204
   __TEXT.__objc_methlist: 0xb0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x277
   __TEXT.__unwind_info: 0xc0
-  __TEXT.__objc_classname: 0x3e
-  __TEXT.__objc_methname: 0x342
-  __TEXT.__objc_methtype: 0x67
-  __TEXT.__objc_stubs: 0x320
-  __DATA_CONST.__got: 0x50
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x50
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x1

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C1FD5875-AE7F-37A7-BB73-58272CFEC83E
-  Functions: 26
-  Symbols:   158
-  CStrings:  79
+  UUID: 8B7F7701-6204-3367-9F85-14B1155A6CBF
+  Functions: 25
+  Symbols:   160
+  CStrings:  38
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x3
- __AXSafeCategoryLog.cold.1
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[UIAccessibilitySafeCategory safeCategoryTargetClass] : 84 -> 76
~ +[UIAccessibilitySafeCategory _initializeSafeCategoryFromValidationManager] : 100 -> 92
~ +[UIAccessibilitySafeCategory _installSafeCategoryValidationMethod] : 96 -> 88
~ +[UIAccessibilitySafeCategory _installLocalValidationMethodOnClassNamed:] : 356 -> 340
~ +[UIAccessibilitySafeCategory _addCategoryMethods:count:excluding:toClass:isClass:useReplace:] : 916 -> 912
~ +[UIAccessibilitySafeCategory _installSafeCategoryOnClass:isManaged:] : 656 -> 640
~ ___69+[UIAccessibilitySafeCategory _installSafeCategoryOnClass:isManaged:]_block_invoke : 104 -> 100
~ __AXSafeCategoryLog : 144 -> 160
~ _UIAccessibilityInstallSafeCategory : 196 -> 184
~ _UIAccessibilityInstallSafeCategories : 720 -> 752
~ __UIAccessibilityCopyClassPath : 184 -> 180
~ __UIAccessibilitySafeCategoryDependsOnSafeCategory : 256 -> 260
~ __UIAccessibilitySafeCategoryAddDependenciesToArray : 340 -> 364
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@24@0:8@16"
- "@28@0:8#16B24"
- "@28@0:8@16B24"
- "T@\"NSString\",C,D,N"
- "UIAccessibilitySafeCategory"
- "UTF8String"
- "_UIAccessibilitySwiftSafeCategory"
- "_accessibilityIgnoreSwiftInit"
- "_initializeSafeCategoryFromValidationManager"
- "_installLocalValidationMethodOnClassNamed:"
- "_installSafeCategoryOnClass:isManaged:"
- "_installSafeCategoryOnClassNamed:"
- "_installSafeCategoryOnClassNamed:isManaged:"
- "_installSafeCategoryValidationMethod"
- "accessibilityIdentifier"
- "addObject:"
- "addSafeCategoryMethods:count:excluding:toClass:isClass:"
- "arrayByAddingObject:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "defaultCenter"
- "initWithString:"
- "insertString:atIndex:"
- "isEqualToString:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "postNotificationName:object:"
- "removeAllObjects"
- "removeObjectAtIndex:"
- "safeCategoryAddDependenciesToCollection:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClass"
- "stringWithFormat:"
- "superclass"
- "v24@0:8@16"
- "v48@0:8^^{objc_method}16I24@28#36B44"

```
