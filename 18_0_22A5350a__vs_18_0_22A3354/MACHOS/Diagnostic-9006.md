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
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_UITableView
+ _OBJC_METACLASS_$_UnknownPartViewController
+ _OBJC_CLASS_$_UIImage
+ _OBJC_METACLASS_$_OBWelcomeController
+ _OBJC_CLASS_$_NSNumber
+ _dispatch_semaphore_wait
+ _objc_release_x24
+ _objc_retain_x21
+ _CGRectZero
+ _OBJC_CLASS_$_UIColor
+ _objc_release_x28
+ _OBJC_CLASS_$_OBWelcomeController
+ _OBJC_CLASS_$_OBLinkTrayButton
+ _OBJC_CLASS_$_OBTableWelcomeController
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _OBJC_CLASS_$_UINavigationController
+ _OBJC_CLASS_$_CRPreflightUtils
+ _OBJC_CLASS_$_OBBoldTrayButton
+ _OBJC_CLASS_$_UIFont
+ _objc_retain_x19
+ _dispatch_time
+ _objc_enumerationMutation
+ _objc_msgSendSuper2
+ _OBJC_CLASS_$_CRPreflightController
+ _objc_release_x8
+ _dispatch_async
+ _dispatch_get_global_queue
+ _dispatch_semaphore_signal
+ _MGGetBoolAnswer
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_UnknownPartViewController
+ _OBJC_CLASS_$_NSString
+ _objc_storeWeak
+ _CRErrorDomain
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_UITableViewCell
+ _dispatch_semaphore_create
+ _objc_retain_x3
+ _OBJC_CLASS_$_CRRepairStatus
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _objc_autoreleaseReturnValue
+ _objc_release_x27
+ _objc_retain_x9
+ __dispatch_main_q
+ _objc_alloc
+ _objc_opt_class
+ _objc_release_x25
+ _objc_release_x26
+ _OBJC_CLASS_$_NSError
CStrings:
+ "UNKOWN_PART_DETAIL_TEXT"
+ "Continue button tapped"
+ "cancelTapped:"
+ "setSecondaryText:"
+ "initWithTitle:detailText:icon:adoptTableViewScrollView:"
+ "mainBundle"
+ "pass"
+ "spcResults:"
+ "TEST_TITLE"
+ "preflightPartSPC"
+ "arrayWithObjects:count:"
+ "systemYellowColor"
+ "updateViewWithRepairSummary"
+ "Preflight success: %!d(MISSING)"
+ "endTestWithStatusCode:error:"
+ "pointSize"
+ "PART_BATTERY"
+ "defaultContentConfiguration"
+ "lost"
+ "-[RepairSummaryViewController shouldPresentInHostApp]"
+ "clearColor"
+ "CONTINUE"
+ "exclamationmark.triangle"
+ "PART_BACK_GLASS"
+ "IPHONE COMP BATTERY"
+ "v28@?0B8@\"NSDictionary\"12@\"NSError\"20"
+ "errorWithDomain:code:userInfo:"
+ "findmy"
+ "systemGroupedBackgroundColor"
+ "3kmXfug8VcxLI5yEmsqQKw"
+ "RepairSummaryPlugin-Release"
+ "setHidesBackButton:"
+ "RECOVER"
+ "Unknown SPC: %!@(MISSING)"
+ "1"
+ "navigationItem"
+ "-[RepairSummaryViewController viewDidAppear:]"
+ "v24@0:8Q16"
+ "Missing partSPCs"
+ "PART_TRUE_DEPTH_CAMERA"
+ "TEXT_DENIED"
+ "setDataSource:"
+ "InternalBuild"
+ "setScrollingDisabled:"
+ "addButton:"
+ "setContentConfiguration:"
+ "T@\"<RepairSummaryNavigationCoordinator>\",W,N,V_coordinator"
+ "setFrame:"
+ "Physical button event: %!l(MISSING)d"
+ "TEST_DETAILS"
+ "systemImageNamed:"
+ "lock"
+ "contentView"
+ "setBackgroundColor:"
+ "setImage:"
+ "CANCEL"
+ "bounds"
+ "fail"
+ "setCoordinator:"
+ "dequeueReusableCellWithIdentifier:forIndexPath:"
+ "IPHONE COMP ENCL"
+ "Preflight error: %!@(MISSING)"
+ "UNKOWN_PART_TITLE"
+ "pushViewController:animated:"
+ "shouldPresentInHostApp"
+ "Preflight results: %!@(MISSING)"
+ "addTarget:action:forControlEvents:"
+ "row"
+ "_systemImageNamed:"
+ "countByEnumeratingWithState:objects:count:"
+ "initWithTitle:detailText:icon:"
+ "Preflight time out"
+ "systemGreenColor"
+ "view"
+ "initWithComponent:"
+ "TEXT_LOCK"
+ "PART_REAR_CAMERA"
+ "setDelegate:"
+ "viewDidLoad"
+ "setBackgroundView:"
+ "textProperties"
+ "IPAD REAR CAMERA"
+ "setFont:"
+ "activateConstraints:"
+ "screwdriver.fill"
+ "setHidden:"
+ "stringWithFormat:"
+ "imageByApplyingSymbolConfiguration:"
+ "setTintColor:"
+ "constraintEqualToAnchor:multiplier:"
+ "removeObjectAtIndex:"
+ "\x01"
+ "IPHONE BACK GLASS"
+ "IPHONE COMP DISPLAY"
+ "boldSystemFontOfSize:"
+ "keyBlob"
+ "buttonTray"
+ "numberWithInteger:"
+ "objectAtIndexedSubscript:"
+ "Cell"
+ "No more views."
+ "_coordinator"
+ "denied"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "Move to next view"
+ "imageProperties"
+ "sealed"
+ "setShouldShowPressHomeLabel:"
+ "IPAD FRONT CAMERA"
+ "Missing preflight RIK"
+ "-[RepairSummaryViewController viewDidLoad]"
+ "registerClass:forCellReuseIdentifier:"
+ "setTableView:"
+ "blackColor"
+ "IPAD COMP DISPLAY"
+ "configurationWithHierarchicalColor:"
+ "addObject:"
+ "-[RepairSummaryViewController moveToNextViewController]"
+ "isServicePartWithError:"
+ "IPHONE COMP FACEID"
+ "didMoveToParentViewController:"
+ "initRepairSummaryTable"
+ "preflight:withReply:"
+ "TEXT_PASS"
+ "exclamationmark.triangle.fill"
+ "objectForKeyedSubscript:"
+ "setText:"
+ "addSubview:"
+ "mutableCopy"
+ "-[RepairSummaryViewController updateViewWithRepairSummary]"
+ "tableView"
+ "base64EncodedStringWithOptions:"
+ "_continueTapped"
+ "v32@0:8q16@24"
+ "viewDidAppear:"
+ "unauth"
+ "initWithFrame:style:"
+ "TEXT_LOST"
+ "UnknownPartViewController"
+ "getComponentString:"
+ "count"
+ "systemBlueColor"
+ "code"
+ "A new %!@(MISSING) was detected and must be repaired"
+ "@\"<RepairSummaryNavigationCoordinator>\""
+ "font"
+ "PART_ENCLOSURE"
+ "coordinator"
+ "lock.circle.fill"
+ "TEXT_UNKNOWN"
+ "Service part mTub/MLB not supported"
+ "IPHONE COMP CAMERA"
+ "Cancel button tapped"
+ "setTitle:forState:"
+ "continueTapped:"
+ "IPHONE COMP RCAM"
+ "checkmark.seal.fill"
+ "heightAnchor"
+ "localizedStringForKey:value:table:"
+ "addChildViewController:"
+ "PART_DISPLAY"

```
