## Diagnostic-9012

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9012.appex/Diagnostic-9012`

```diff

 921.80.171.0.1
-  __TEXT.__text: 0x19f8
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x3dc
-  __TEXT.__const: 0x70
-  __TEXT.__objc_methname: 0xb8a
-  __TEXT.__cstring: 0x119
+  __TEXT.__text: 0x2ea8
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x444
+  __TEXT.__const: 0x80
+  __TEXT.__objc_methname: 0xec1
+  __TEXT.__cstring: 0x255
   __TEXT.__objc_classname: 0x5d
-  __TEXT.__objc_methtype: 0x240
+  __TEXT.__objc_methtype: 0x259
   __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__oslogstring: 0xb2
+  __TEXT.__oslogstring: 0x1b7
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0xb0
-  __DATA_CONST.__cfstring: 0xa0
+  __TEXT.__unwind_info: 0xf0
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_intobj: 0x78
   __DATA.__objc_const: 0x740
-  __DATA.__objc_selrefs: 0x350
+  __DATA.__objc_selrefs: 0x4a0
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D1D42C94-17AA-3467-8AC1-02554AA02DFC
-  Functions: 66
-  Symbols:   66
-  CStrings:  223
+  UUID: 4E9D9A3E-8DDC-36A2-B413-D7D4CCA4B85E
+  Functions: 79
+  Symbols:   87
+  CStrings:  300
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_CRIOServiceController
+ _OBJC_CLASS_$_CRMesaController
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_OBBoldTrayButton
+ _OBJC_CLASS_$_OBLinkTrayButton
+ _OBJC_CLASS_$_OBWelcomeController
+ _OBJC_CLASS_$_UINavigationController
+ __dispatch_main_q
+ _dispatch_async
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
CStrings:
+ ""
+ "-[RepairUnlockViewController setupView]"
+ "-[RepairUnlockViewController shouldPresentInHostApp]"
+ "-[RepairUnlockViewController viewDidAppear:]"
+ "-[RepairUnlockViewController viewDidLoad]"
+ "3kmXfug8VcxLI5yEmsqQKw"
+ "CANCEL"
+ "CONTINUE"
+ "Cancel button tapped"
+ "Continue button tapped"
+ "De-assert repair pin: %d"
+ "Detected gestures"
+ "Failed to assert repair_en"
+ "Failed to unlock mesa"
+ "InternalBuild"
+ "Mesa already unlocked"
+ "Mesa unlock not supported"
+ "Physical button event: %ld"
+ "Q"
+ "RepairUnlockPlugin-Release"
+ "Successfully unlocked mesa"
+ "UNLOCK_TOUCHID_BODY"
+ "UNLOCK_TOUCHID_TITLE"
+ "Volume button event: %ld"
+ "Waiting for keychord..."
+ "activateConstraints:"
+ "addButton:"
+ "addChildViewController:"
+ "addObject:"
+ "addSubview:"
+ "addTarget:action:forControlEvents:"
+ "arrayWithObjects:count:"
+ "assertRepairPin:"
+ "bottomAnchor"
+ "buttonTray"
+ "cancelTapped:"
+ "constraintEqualToAnchor:"
+ "containsObject:"
+ "contentView"
+ "continueTapped:"
+ "didMoveToParentViewController:"
+ "endTestWithStatusCode:error:"
+ "getProtocolVersion"
+ "iPad-Unlock"
+ "initWithRootViewController:"
+ "initWithTitle:detailText:icon:contentLayout:"
+ "isPhysicalPresenceAsserted"
+ "leftAnchor"
+ "localizedStringForKey:value:table:"
+ "navigationItem"
+ "numberWithInteger:"
+ "removeObject:"
+ "rightAnchor"
+ "setClipsToBounds:"
+ "setEnabled:"
+ "setHidden:"
+ "setHidesBackButton:"
+ "setNavigationBarHidden:"
+ "setScrollingDisabled:"
+ "setShouldShowPressHomeLabel:"
+ "setTitle:forState:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "setupView"
+ "shouldPresentInHostApp"
+ "topAnchor"
+ "v24@0:8Q16"
+ "v32@0:8q16@24"
+ "view"
+ "viewDidAppear:"
+ "viewDidLoad"
- "Diagnostics not available"

```
