## Diagnostic-9010

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010`

```diff

 625.2.2.0.0
-  __TEXT.__text: 0xd44
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__objc_stubs: 0x1e0
-  __TEXT.__objc_methlist: 0xf4
-  __TEXT.__const: 0x28
+  __TEXT.__text: 0x1cdc
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_stubs: 0x780
+  __TEXT.__objc_methlist: 0x148
+  __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__oslogstring: 0x96
-  __TEXT.__cstring: 0xf4
-  __TEXT.__objc_methname: 0x514
+  __TEXT.__oslogstring: 0xfc
+  __TEXT.__cstring: 0x253
+  __TEXT.__objc_methname: 0x845
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
+  __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__objc_intobj: 0x120
   __DATA.__objc_const: 0x640
-  __DATA.__objc_selrefs: 0xf0
+  __DATA.__objc_selrefs: 0x228
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
+  Functions: 37
+  Symbols:   69
+  CStrings:  179
 
Symbols:
+ _objc_release_x25
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_OBBoldTrayButton
+ _OBJC_CLASS_$_OBLinkTrayButton
+ _OBJC_CLASS_$_UIColor
+ _OBJC_CLASS_$_NSBundle
+ _reboot3
+ _objc_release_x24
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retain_x3
+ _OBJC_CLASS_$_UIAlertController
+ __NSConcreteGlobalBlock
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_OBTableWelcomeController
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _objc_alloc
+ _objc_release_x27
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_CLASS_$_UIAlertAction
CStrings:
+ "_tryAgainButtonTapped:"
+ "actionWithTitle:style:handler:"
+ "setHidden:"
+ "bottomAnchor"
+ "numberWithInteger:"
+ "arrayWithObjects:count:"
+ "Reboot failed with error: %!d(MISSING)"
+ "arrowtriangle.left.circle"
+ "RESTART"
+ "TEST_RETRY_TITLE"
+ "setTitle:forState:"
+ "checkmark.circle"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "TRY_AGAIN"
+ "Try Again button tapped"
+ "mainBundle"
+ "Restart button tapped"
+ "v24@0:8Q16"
+ "LOST_MODE_DETAIL_TEXT"
+ "buttonTray"
+ "-[RepairResultViewController setupView]"
+ "alertControllerWithTitle:message:preferredStyle:"
+ "configurationWithHierarchicalColor:"
+ "endTestWithStatusCode:error:"
+ "LOST_MODE_TITLE"
+ "addButton:"
+ "ALERT_CANCEL"
+ "ALERT_RESTART"
+ "TEST_DONE_TITLE"
+ "rightAnchor"
+ "systemImageNamed:"
+ "imageByApplyingSymbolConfiguration:"
+ "v16@?0@\"UIAlertAction\"8"
+ "view"
+ "addChildViewController:"
+ "addTarget:action:forControlEvents:"
+ "addAction:"
+ "RepairResultPlugin-Release"
+ "TEST_FAILED_TITLE"
+ "activateConstraints:"
+ "systemBlueColor"
+ "isNetworkError"
+ "exclamationmark.triangle"
+ "TEST_DONE_DETAILS"
+ "TEST_RETRY_DETAILS"
+ "code"
+ "setupView"
+ "isLostMode"
+ "presentViewController:animated:completion:"
+ "topAnchor"
+ "v32@0:8q16@24"
+ "localizedStringForKey:value:table:"
+ "setShouldShowPressHomeLabel:"
+ "leftAnchor"
+ "setScrollingDisabled:"
+ "_restartButtonTapped:"
+ "constraintEqualToAnchor:"
+ "initWithTitle:detailText:icon:adoptTableViewScrollView:"
+ "Physical button event: %!l(MISSING)d"
+ "TEST_FAILED_DETAILS"
+ "addSubview:"

```
