## Diagnostic-9006

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006`

```diff

 625.2.2.0.0
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
+  __TEXT.__text: 0x45bc
+  __TEXT.__auth_stubs: 0x330
+  __TEXT.__objc_stubs: 0x1180
+  __TEXT.__objc_methlist: 0x37c
+  __TEXT.__cstring: 0x517
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
+  __DATA_CONST.__cfstring: 0x6e0
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
+  CStrings:  496
 
Symbols:
+ _dispatch_async
+ _dispatch_semaphore_signal
+ _OBJC_CLASS_$_CRRepairStatus
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _objc_release_x27
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_UIFont
+ _OBJC_METACLASS_$_UnknownPartViewController
+ _dispatch_time
+ _objc_autoreleaseReturnValue
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_UIColor
+ _objc_release_x26
+ _OBJC_CLASS_$_CRPreflightUtils
+ _dispatch_semaphore_create
+ _OBJC_CLASS_$_CRPreflightController
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_UITableView
+ _OBJC_CLASS_$_UITableViewCell
+ _CRErrorDomain
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_OBTableWelcomeController
+ _objc_release_x24
+ _dispatch_get_global_queue
+ _dispatch_semaphore_wait
+ _OBJC_CLASS_$_UnknownPartViewController
+ _objc_opt_class
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_OBWelcomeController
+ __dispatch_main_q
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _OBJC_METACLASS_$_OBWelcomeController
+ _objc_release_x25
+ _objc_retain_x3
+ _objc_retain_x9
+ _OBJC_CLASS_$_OBBoldTrayButton
+ _objc_msgSendSuper2
+ _objc_release_x28
+ _CGRectZero
+ _objc_storeWeak
+ _OBJC_CLASS_$_OBLinkTrayButton
+ _OBJC_CLASS_$_UINavigationController
+ _objc_enumerationMutation
+ _objc_retain_x19
+ _objc_retain_x21
+ _objc_release_x8
+ _NSLocalizedDescriptionKey
+ _objc_alloc
CStrings:
+ "preflight:withReply:"
+ "addTarget:action:forControlEvents:"
+ "setFrame:"
+ "RECOVER"
+ "UnknownPartViewController"
+ "setScrollingDisabled:"
+ "v32@0:8q16@24"
+ "CANCEL"
+ "setShouldShowPressHomeLabel:"
+ "Preflight time out"
+ "font"
+ "systemGreenColor"
+ "unauth"
+ "countByEnumeratingWithState:objects:count:"
+ "errorWithDomain:code:userInfo:"
+ "IPAD COMP DISPLAY"
+ "boldSystemFontOfSize:"
+ "contentView"
+ "localizedStringForKey:value:table:"
+ "setFont:"
+ "constraintEqualToAnchor:multiplier:"
+ "mutableCopy"
+ "TEXT_LOCK"
+ "clearColor"
+ "setCoordinator:"
+ "addButton:"
+ "endTestWithStatusCode:error:"
+ "InternalBuild"
+ "updateViewWithRepairSummary"
+ "activateConstraints:"
+ "setBackgroundColor:"
+ "-[RepairSummaryViewController viewDidAppear:]"
+ "lost"
+ "v28@?0B8@\"NSDictionary\"12@\"NSError\"20"
+ "_systemImageNamed:"
+ "getComponentString:"
+ "textProperties"
+ "UNKOWN_PART_DETAIL_TEXT"
+ "T@\"<RepairSummaryNavigationCoordinator>\",W,N,V_coordinator"
+ "isServicePartWithError:"
+ "setTintColor:"
+ "spcResults:"
+ "base64EncodedStringWithOptions:"
+ "IPHONE COMP FACEID"
+ "objectAtIndexedSubscript:"
+ "pass"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "registerClass:forCellReuseIdentifier:"
+ "Move to next view"
+ "exclamationmark.triangle.fill"
+ "3kmXfug8VcxLI5yEmsqQKw"
+ "Missing partSPCs"
+ "mainBundle"
+ "PART_TRUE_DEPTH_CAMERA"
+ "blackColor"
+ "lock.circle.fill"
+ "IPAD FRONT CAMERA"
+ "preflightPartSPC"
+ "PART_BATTERY"
+ "denied"
+ "A new %!@(MISSING) was detected and must be repaired"
+ "PART_DISPLAY"
+ "RepairSummaryPlugin-Release"
+ "lock"
+ "IPHONE COMP ENCL"
+ "Preflight results: %!@(MISSING)"
+ "viewDidLoad"
+ "pointSize"
+ "pushViewController:animated:"
+ "setDataSource:"
+ "IPHONE COMP RCAM"
+ "Physical button event: %!l(MISSING)d"
+ "addSubview:"
+ "dequeueReusableCellWithIdentifier:forIndexPath:"
+ "initWithTitle:detailText:icon:"
+ "-[RepairSummaryViewController updateViewWithRepairSummary]"
+ "No more views."
+ "exclamationmark.triangle"
+ "IPHONE COMP DISPLAY"
+ "PART_REAR_CAMERA"
+ "code"
+ "coordinator"
+ "sealed"
+ "initWithFrame:style:"
+ "IPHONE COMP BATTERY"
+ "\x01"
+ "shouldPresentInHostApp"
+ "-[RepairSummaryViewController shouldPresentInHostApp]"
+ "objectForKeyedSubscript:"
+ "configurationWithHierarchicalColor:"
+ "findmy"
+ "fail"
+ "Cell"
+ "Preflight success: %!d(MISSING)"
+ "@\"<RepairSummaryNavigationCoordinator>\""
+ "setTableView:"
+ "setText:"
+ "Continue button tapped"
+ "PART_BACK_GLASS"
+ "systemImageNamed:"
+ "removeObjectAtIndex:"
+ "IPHONE BACK GLASS"
+ "TEST_DETAILS"
+ "CONTINUE"
+ "Unknown SPC: %!@(MISSING)"
+ "addChildViewController:"
+ "TEXT_UNKNOWN"
+ "didMoveToParentViewController:"
+ "keyBlob"
+ "stringWithFormat:"
+ "v24@0:8Q16"
+ "imageByApplyingSymbolConfiguration:"
+ "view"
+ "initWithTitle:detailText:icon:adoptTableViewScrollView:"
+ "TEST_TITLE"
+ "systemGroupedBackgroundColor"
+ "setHidden:"
+ "Cancel button tapped"
+ "numberWithInteger:"
+ "PART_ENCLOSURE"
+ "screwdriver.fill"
+ "buttonTray"
+ "defaultContentConfiguration"
+ "setBackgroundView:"
+ "systemYellowColor"
+ "setHidesBackButton:"
+ "setTitle:forState:"
+ "setDelegate:"
+ "setImage:"
+ "navigationItem"
+ "TEXT_DENIED"
+ "Preflight error: %!@(MISSING)"
+ "imageProperties"
+ "systemBlueColor"
+ "Service part mTub/MLB not supported"
+ "TEXT_LOST"
+ "viewDidAppear:"
+ "_coordinator"
+ "continueTapped:"
+ "heightAnchor"
+ "setSecondaryText:"
+ "IPAD REAR CAMERA"
+ "setContentConfiguration:"
+ "tableView"
+ "TEXT_PASS"
+ "Missing preflight RIK"
+ "addObject:"
+ "count"
+ "1"
+ "checkmark.seal.fill"
+ "initRepairSummaryTable"
+ "initWithComponent:"
+ "-[RepairSummaryViewController viewDidLoad]"
+ "UNKOWN_PART_TITLE"
+ "_continueTapped"
+ "bounds"
+ "row"
+ "-[RepairSummaryViewController moveToNextViewController]"
+ "cancelTapped:"
+ "IPHONE COMP CAMERA"
+ "arrayWithObjects:count:"

```
