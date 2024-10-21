## Diagnostic-9006

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006`

```diff

-645.42.1.0.0
-  __TEXT.__text: 0xf5c
-  __TEXT.__auth_stubs: 0x1c0
-  __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x29c
-  __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__cstring: 0xd8
-  __TEXT.__oslogstring: 0x70
-  __TEXT.__objc_methname: 0x1805
-  __TEXT.__objc_classname: 0xb2
-  __TEXT.__objc_methtype: 0xac0
+645.42.2.0.0
+  __TEXT.__text: 0x467c
+  __TEXT.__auth_stubs: 0x330
+  __TEXT.__objc_stubs: 0x1180
+  __TEXT.__objc_methlist: 0x37c
+  __TEXT.__cstring: 0x533
+  __TEXT.__objc_methname: 0x1f04
+  __TEXT.__oslogstring: 0x14f
+  __TEXT.__objc_classname: 0xce
+  __TEXT.__objc_methtype: 0xb01
+  __TEXT.__const: 0x40
+  __TEXT.__gcc_except_tab: 0x60
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0xf0
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0xb0
-  __DATA_CONST.__cfstring: 0x40
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__cfstring: 0x720
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1440
-  __DATA.__objc_selrefs: 0x208
-  __DATA.__objc_ivar: 0x60
-  __DATA.__objc_data: 0xa0
+  __DATA.__objc_const: 0x1510
+  __DATA.__objc_selrefs: 0x4e0
+  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_data: 0xf0
   __DATA.__data: 0x240
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 62
-  Symbols:   47
-  CStrings:  334
+  Functions: 87
+  Symbols:   98
+  CStrings:  498
 
Symbols:
+ _CGRectZero
+ _CRErrorDomain
+ _MGGetBoolAnswer
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_CRPreflightController
+ _OBJC_CLASS_$_CRPreflightUtils
+ _OBJC_CLASS_$_CRRepairStatus
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_OBBoldTrayButton
+ _OBJC_CLASS_$_OBLinkTrayButton
+ _OBJC_CLASS_$_OBTableWelcomeController
+ _OBJC_CLASS_$_OBWelcomeController
+ _OBJC_CLASS_$_UIColor
+ _OBJC_CLASS_$_UIFont
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _OBJC_CLASS_$_UINavigationController
+ _OBJC_CLASS_$_UITableView
+ _OBJC_CLASS_$_UITableViewCell
+ _OBJC_CLASS_$_UnknownPartViewController
+ _OBJC_METACLASS_$_OBWelcomeController
+ _OBJC_METACLASS_$_UnknownPartViewController
+ __dispatch_main_q
+ _dispatch_async
+ _dispatch_get_global_queue
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _objc_alloc
+ _objc_autoreleaseReturnValue
+ _objc_enumerationMutation
+ _objc_msgSendSuper2
+ _objc_opt_class
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain_x19
+ _objc_retain_x21
+ _objc_retain_x3
+ _objc_retain_x9
+ _objc_storeWeak
CStrings:
+ "\x01"
+ "-[RepairSummaryViewController moveToNextViewController]"
+ "-[RepairSummaryViewController shouldPresentInHostApp]"
+ "-[RepairSummaryViewController updateViewWithRepairSummary]"
+ "-[RepairSummaryViewController viewDidAppear:]"
+ "-[RepairSummaryViewController viewDidLoad]"
+ "1"
+ "3kmXfug8VcxLI5yEmsqQKw"
+ "@\"<RepairSummaryNavigationCoordinator>\""
+ "A new %!@(MISSING) was detected and must be repaired"
+ "CANCEL"
+ "CONTINUE"
+ "Cancel button tapped"
+ "Cell"
+ "Continue button tapped"
+ "IPAD COMP DISPLAY"
+ "IPAD FRONT CAMERA"
+ "IPAD REAR CAMERA"
+ "IPAD TOUCH ID"
+ "IPHONE BACK GLASS"
+ "IPHONE COMP BATTERY"
+ "IPHONE COMP CAMERA"
+ "IPHONE COMP DISPLAY"
+ "IPHONE COMP ENCL"
+ "IPHONE COMP FACEID"
+ "IPHONE COMP RCAM"
+ "InternalBuild"
+ "Missing partSPCs"
+ "Missing preflight RIK"
+ "Move to next view"
+ "No more views."
+ "PART_BACK_GLASS"
+ "PART_BATTERY"
+ "PART_DISPLAY"
+ "PART_ENCLOSURE"
+ "PART_REAR_CAMERA"
+ "PART_TOUCH_ID"
+ "PART_TRUE_DEPTH_CAMERA"
+ "Physical button event: %!l(MISSING)d"
+ "Preflight error: %!@(MISSING)"
+ "Preflight results: %!@(MISSING)"
+ "Preflight success: %!d(MISSING)"
+ "Preflight time out"
+ "RECOVER"
+ "RepairSummaryPlugin-Release"
+ "Service part mTub/MLB not supported"
+ "T@\"<RepairSummaryNavigationCoordinator>\",W,N,V_coordinator"
+ "TEST_DETAILS"
+ "TEST_TITLE"
+ "TEXT_DENIED"
+ "TEXT_LOCK"
+ "TEXT_LOST"
+ "TEXT_PASS"
+ "TEXT_UNKNOWN"
+ "UNKOWN_PART_DETAIL_TEXT"
+ "UNKOWN_PART_TITLE"
+ "Unknown SPC: %!@(MISSING)"
+ "UnknownPartViewController"
+ "_continueTapped"
+ "_coordinator"
+ "_systemImageNamed:"
+ "activateConstraints:"
+ "addButton:"
+ "addChildViewController:"
+ "addObject:"
+ "addSubview:"
+ "addTarget:action:forControlEvents:"
+ "arrayWithObjects:count:"
+ "base64EncodedStringWithOptions:"
+ "blackColor"
+ "boldSystemFontOfSize:"
+ "bounds"
+ "buttonTray"
+ "cancelTapped:"
+ "checkmark.seal.fill"
+ "clearColor"
+ "code"
+ "configurationWithHierarchicalColor:"
+ "constraintEqualToAnchor:multiplier:"
+ "contentView"
+ "continueTapped:"
+ "coordinator"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "defaultContentConfiguration"
+ "denied"
+ "dequeueReusableCellWithIdentifier:forIndexPath:"
+ "didMoveToParentViewController:"
+ "endTestWithStatusCode:error:"
+ "errorWithDomain:code:userInfo:"
+ "exclamationmark.triangle"
+ "exclamationmark.triangle.fill"
+ "fail"
+ "findmy"
+ "font"
+ "getComponentString:"
+ "heightAnchor"
+ "imageByApplyingSymbolConfiguration:"
+ "imageProperties"
+ "initRepairSummaryTable"
+ "initWithComponent:"
+ "initWithFrame:style:"
+ "initWithTitle:detailText:icon:"
+ "initWithTitle:detailText:icon:adoptTableViewScrollView:"
+ "isServicePartWithError:"
+ "keyBlob"
+ "localizedStringForKey:value:table:"
+ "lock"
+ "lock.circle.fill"
+ "lost"
+ "mainBundle"
+ "mutableCopy"
+ "navigationItem"
+ "numberWithInteger:"
+ "objectAtIndexedSubscript:"
+ "objectForKeyedSubscript:"
+ "pass"
+ "pointSize"
+ "preflight:withReply:"
+ "preflightPartSPC"
+ "pushViewController:animated:"
+ "registerClass:forCellReuseIdentifier:"
+ "removeObjectAtIndex:"
+ "row"
+ "screwdriver.fill"
+ "sealed"
+ "setBackgroundColor:"
+ "setBackgroundView:"
+ "setContentConfiguration:"
+ "setCoordinator:"
+ "setDataSource:"
+ "setDelegate:"
+ "setFont:"
+ "setFrame:"
+ "setHidden:"
+ "setHidesBackButton:"
+ "setImage:"
+ "setScrollingDisabled:"
+ "setSecondaryText:"
+ "setShouldShowPressHomeLabel:"
+ "setTableView:"
+ "setText:"
+ "setTintColor:"
+ "setTitle:forState:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "shouldPresentInHostApp"
+ "spcResults:"
+ "stringWithFormat:"
+ "systemBlueColor"
+ "systemGreenColor"
+ "systemGroupedBackgroundColor"
+ "systemImageNamed:"
+ "systemYellowColor"
+ "tableView"
+ "textProperties"
+ "unauth"
+ "updateViewWithRepairSummary"
+ "v24@0:8Q16"
+ "v28@?0B8@\"NSDictionary\"12@\"NSError\"20"
+ "v32@0:8q16@24"
+ "view"
+ "viewDidAppear:"
+ "viewDidLoad"

```
