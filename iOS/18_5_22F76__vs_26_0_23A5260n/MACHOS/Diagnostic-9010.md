## Diagnostic-9010

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010`

```diff

-696.120.5.0.0
-  __TEXT.__text: 0x1edc
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__const: 0x38
+921.0.34.0.0
+  __TEXT.__text: 0x2df0
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_stubs: 0xc80
+  __TEXT.__objc_methlist: 0x39c
+  __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__oslogstring: 0xfd
-  __TEXT.__cstring: 0x2cb
-  __TEXT.__objc_methname: 0x86b
-  __TEXT.__objc_classname: 0x4f
-  __TEXT.__objc_methtype: 0x18d
+  __TEXT.__oslogstring: 0x187
+  __TEXT.__cstring: 0x366
+  __TEXT.__objc_methname: 0xd93
+  __TEXT.__objc_classname: 0xa5
+  __TEXT.__objc_methtype: 0x216
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x140
-  __DATA_CONST.__got: 0x80
+  __TEXT.__unwind_info: 0xe8
+  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0x118
-  __DATA_CONST.__cfstring: 0x2e0
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__cfstring: 0x3e0
+  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x138
-  __DATA.__objc_const: 0x400
-  __DATA.__objc_selrefs: 0x2e0
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_intobj: 0x180
+  __DATA.__objc_const: 0x6d8
+  __DATA.__objc_selrefs: 0x458
+  __DATA.__objc_ivar: 0x34
+  __DATA.__objc_data: 0x140
+  __DATA.__data: 0x120
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 38467255-137C-3218-912D-B13D124E77E6
-  Functions: 40
-  Symbols:   70
-  CStrings:  208
+  UUID: B68968CC-9B0A-30F4-BC4D-792A86166AE5
+  Functions: 57
+  Symbols:   94
+  CStrings:  297
 
Symbols:
+ _Diagnostic_9010VersionNumber
+ _Diagnostic_9010VersionString
+ _OBJC_CLASS_$_CRDeviceMap
+ _OBJC_CLASS_$_FailedPartViewController
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_OBBoldSubtitleController
+ _OBJC_CLASS_$_OBWelcomeController
+ _OBJC_CLASS_$_UIFont
+ _OBJC_CLASS_$_UIFontDescriptor
+ _OBJC_CLASS_$_UILabel
+ _OBJC_CLASS_$_UINavigationController
+ _OBJC_METACLASS_$_FailedPartViewController
+ _OBJC_METACLASS_$_OBBoldSubtitleController
+ _OBJC_METACLASS_$_OBWelcomeController
+ _UIFontTextStyleBody
+ _UIFontTextStyleTitle2
+ __UISolariumEnabled
+ _objc_alloc_init
+ _objc_autoreleaseReturnValue
+ _objc_enumerationMutation
+ _objc_opt_class
+ _objc_storeWeak
CStrings:
+ "\n"
+ "-[RepairResultViewController moveToNextViewController]"
+ "@\"<RepairResultNavigationCoordinator>\""
+ "@\"NSArray\""
+ "@\"NSMutableArray\""
+ "@\"NSString\""
+ "@\"UINavigationController\""
+ "@24@0:8@16"
+ "@48@0:8@16@24@32@40"
+ "CONTINUE"
+ "Continue button tapped"
+ "FAILED_PARTS_DETAIL_TEXT"
+ "FAILED_PART_DETAIL_TEXT"
+ "FAILED_PART_TITLE"
+ "FailedPartViewController"
+ "Move to next view"
+ "NO"
+ "NSArrayFromKey:types:maxLength:defaultValue:failed:"
+ "No more views."
+ "OBBoldSubtitleController"
+ "RepairResultNavigationCoordinator"
+ "T@\"<RepairResultNavigationCoordinator>\",W,N,V_coordinator"
+ "T@\"NSArray\",R,N,VremovedPartSPC"
+ "T@\"NSMutableArray\",&,N,V_viewControllers"
+ "T@\"NSString\",&,N,V_failedComponentName"
+ "T@\"NSString\",&,N,V_subtitleText"
+ "T@\"UINavigationController\",&,N,V_navigationController"
+ "YES"
+ "_continueTapped"
+ "_coordinator"
+ "_failedComponentName"
+ "_navigationController"
+ "_subtitleText"
+ "_viewControllers"
+ "addObject:"
+ "addObjectsFromArray:"
+ "array"
+ "bounds"
+ "componentsJoinedByString:"
+ "constraintEqualToAnchor:constant:"
+ "contentView"
+ "coordinator"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "didMoveToParentViewController:"
+ "failedComponentName"
+ "fontDescriptorWithSymbolicTraits:"
+ "fontWithDescriptor:size:"
+ "getComponentNameWithSPC:"
+ "initWithComponents:"
+ "initWithTitle:detailText:icon:"
+ "initWithTitle:subtitle:detailText:icon:"
+ "labelColor"
+ "leadingAnchor"
+ "length"
+ "moveToNextViewController"
+ "navigationController"
+ "navigationItem"
+ "objectAtIndexedSubscript:"
+ "preferredFontDescriptorWithTextStyle:"
+ "preferredFontForTextStyle:"
+ "pushViewController:animated:"
+ "removeObjectAtIndex:"
+ "removedPartSPC"
+ "removedPartSPC: %@ validationFailed: %@"
+ "secondaryLabelColor"
+ "setCoordinator:"
+ "setFailedComponentName:"
+ "setFont:"
+ "setFrame:"
+ "setHidesBackButton:"
+ "setNavigationController:"
+ "setNumberOfLines:"
+ "setSubtitleText:"
+ "setText:"
+ "setTextAlignment:"
+ "setTextColor:"
+ "setViewControllers:"
+ "setWithObject:"
+ "subtitleText"
+ "testIdentifier: %@ validationFailed: %@"
+ "testStatusCode : %@ validationFailed: %@"
+ "trailingAnchor"
+ "viewControllers"
- "leftAnchor"
- "rightAnchor"
- "testIdentifier: %@"
- "testStatusCode : %@"

```
