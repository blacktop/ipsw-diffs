## Diagnostic-9010

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010`

```diff

-645.42.1.0.0
-  __TEXT.__text: 0xd44
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__objc_stubs: 0x1e0
-  __TEXT.__objc_methlist: 0xf4
-  __TEXT.__const: 0x28
+645.42.2.0.0
+  __TEXT.__text: 0x1de4
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x154
+  __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__oslogstring: 0x96
-  __TEXT.__cstring: 0xf4
-  __TEXT.__objc_methname: 0x514
+  __TEXT.__oslogstring: 0xfc
+  __TEXT.__cstring: 0x273
+  __TEXT.__objc_methname: 0x84e
   __TEXT.__objc_classname: 0x4f
-  __TEXT.__objc_methtype: 0x169
+  __TEXT.__objc_methtype: 0x182
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0xb0
-  __DATA_CONST.__cfstring: 0x80
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0x138
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__objc_intobj: 0x138
   __DATA.__objc_const: 0x640
-  __DATA.__objc_selrefs: 0xf0
+  __DATA.__objc_selrefs: 0x230
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 27
-  Symbols:   48
-  CStrings:  118
+  Functions: 38
+  Symbols:   69
+  CStrings:  182
 
Symbols:
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_OBBoldTrayButton
+ _OBJC_CLASS_$_OBLinkTrayButton
+ _OBJC_CLASS_$_OBTableWelcomeController
+ _OBJC_CLASS_$_UIAlertAction
+ _OBJC_CLASS_$_UIAlertController
+ _OBJC_CLASS_$_UIColor
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ __NSConcreteGlobalBlock
+ _objc_alloc
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain_x3
+ _reboot3
CStrings:
+ "-[RepairResultViewController setupView]"
+ "ALERT_CANCEL"
+ "ALERT_RESTART"
+ "DENIED_DETAIL_TEXT"
+ "DENIED_TITLE"
+ "LOST_MODE_DETAIL_TEXT"
+ "LOST_MODE_TITLE"
+ "Physical button event: %!l(MISSING)d"
+ "RESTART"
+ "Reboot failed with error: %!d(MISSING)"
+ "RepairResultPlugin-Release"
+ "Restart button tapped"
+ "TEST_DONE_DETAILS"
+ "TEST_DONE_TITLE"
+ "TEST_FAILED_DETAILS"
+ "TEST_FAILED_TITLE"
+ "TEST_RETRY_DETAILS"
+ "TEST_RETRY_TITLE"
+ "TRY_AGAIN"
+ "Try Again button tapped"
+ "_restartButtonTapped:"
+ "_tryAgainButtonTapped:"
+ "actionWithTitle:style:handler:"
+ "activateConstraints:"
+ "addAction:"
+ "addButton:"
+ "addChildViewController:"
+ "addSubview:"
+ "addTarget:action:forControlEvents:"
+ "alertControllerWithTitle:message:preferredStyle:"
+ "arrayWithObjects:count:"
+ "arrowtriangle.left.circle"
+ "bottomAnchor"
+ "buttonTray"
+ "checkmark.circle"
+ "code"
+ "configurationWithHierarchicalColor:"
+ "constraintEqualToAnchor:"
+ "endTestWithStatusCode:error:"
+ "exclamationmark.triangle"
+ "imageByApplyingSymbolConfiguration:"
+ "initWithTitle:detailText:icon:adoptTableViewScrollView:"
+ "isDenied"
+ "isLostMode"
+ "isNetworkError"
+ "leftAnchor"
+ "localizedStringForKey:value:table:"
+ "mainBundle"
+ "numberWithInteger:"
+ "presentViewController:animated:completion:"
+ "rightAnchor"
+ "setHidden:"
+ "setScrollingDisabled:"
+ "setShouldShowPressHomeLabel:"
+ "setTitle:forState:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "setupView"
+ "systemBlueColor"
+ "systemImageNamed:"
+ "topAnchor"
+ "v16@?0@\"UIAlertAction\"8"
+ "v24@0:8Q16"
+ "v32@0:8q16@24"
+ "view"

```
