## WebApp

> `/System/Library/PrivateFrameworks/WebApp.framework/WebApp`

```diff

-617.2.4.10.8
-  __TEXT.__text: 0x229c
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x264
-  __TEXT.__cstring: 0x1b0
+618.1.15.10.11
+  __TEXT.__text: 0x287c
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__objc_methlist: 0x2cc
+  __TEXT.__cstring: 0x1b9
   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x10
   __TEXT.__oslogstring: 0x156
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x12c
-  __TEXT.__objc_classname: 0x114
-  __TEXT.__objc_methname: 0x1b1e
-  __TEXT.__objc_methtype: 0xd6e
-  __TEXT.__objc_stubs: 0xce0
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0xf8
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__unwind_info: 0x13c
+  __TEXT.__objc_classname: 0x135
+  __TEXT.__objc_methname: 0x1cf4
+  __TEXT.__objc_methtype: 0xdc2
+  __TEXT.__objc_stubs: 0xec0
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1968
-  __DATA_CONST.__objc_selrefs: 0x3e8
-  __AUTH_CONST.__objc_const: 0x1b0
+  __DATA_CONST.__objc_const: 0x1aa0
+  __DATA_CONST.__objc_selrefs: 0x468
+  __DATA_CONST.__objc_classrefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0x20
+  __AUTH_CONST.__objc_const: 0x1f8
   __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x1e0
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_classrefs: 0x98
-  __DATA.__objc_superrefs: 0x18
-  __DATA.__objc_ivar: 0x54
+  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x240
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 61
-  Symbols:   435
-  CStrings:  390
+  Functions: 70
+  Symbols:   490
+  CStrings:  418
 
Symbols:
+ -[WebAppEligibilityViewController .cxx_destruct]
+ -[WebAppEligibilityViewController initWithWebClip:scene:]
+ -[WebAppEligibilityViewController loadView]
+ -[WebAppEligibilityViewController overrideShowAlert]
+ -[WebAppEligibilityViewController presentAlertIfNeeded]
+ -[WebAppEligibilityViewController setOverrideShowAlert:]
+ -[WebAppEligibilityViewController viewDidAppear:]
+ -[WebAppEligibilityViewController webClip]
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_UIContentUnavailableConfiguration
+ _OBJC_CLASS_$_UIContentUnavailableView
+ _OBJC_CLASS_$_UIDismissSceneAction
+ _OBJC_CLASS_$_WebAppEligibilityViewController
+ _OBJC_CLASS_$__SFFeatureAvailability
+ _OBJC_IVAR_$_WebAppEligibilityViewController._alertController
+ _OBJC_IVAR_$_WebAppEligibilityViewController._overrideShowAlert
+ _OBJC_IVAR_$_WebAppEligibilityViewController._unavailableView
+ _OBJC_IVAR_$_WebAppEligibilityViewController._webClip
+ _OBJC_IVAR_$_WebAppSceneDelegate._eligibilityViewController
+ _OBJC_IVAR_$_WebAppSceneDelegate._shouldLoadWebApp
+ _OBJC_METACLASS_$_WebAppEligibilityViewController
+ __OBJC_$_INSTANCE_METHODS_WebAppEligibilityViewController
+ __OBJC_$_INSTANCE_VARIABLES_WebAppEligibilityViewController
+ __OBJC_$_PROP_LIST_WebAppEligibilityViewController
+ __OBJC_CLASS_RO_$_WebAppEligibilityViewController
+ __OBJC_METACLASS_RO_$_WebAppEligibilityViewController
+ ___57-[WebAppEligibilityViewController initWithWebClip:scene:]_block_invoke
+ ___NSDictionary0__struct
+ ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ _objc_msgSend$_FBSScene
+ _objc_msgSend$eligibilityAlert:
+ _objc_msgSend$eligibilityStatus
+ _objc_msgSend$emptyConfiguration
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$initWithInfo:responder:
+ _objc_msgSend$initWithWebClip:scene:
+ _objc_msgSend$isHSWADisabled
+ _objc_msgSend$openURL:options:completionHandler:
+ _objc_msgSend$presentAlertIfNeeded
+ _objc_msgSend$presentingViewController
+ _objc_msgSend$sendActions:
+ _objc_msgSend$setAutoresizingMask:
+ _objc_msgSend$setOverrideShowAlert:
+ _objc_msgSend$setWithObject:
+ _objc_retain_x22
+ _objc_retain_x23
CStrings:
+ "\x02\x11"
+ "@\"UIAlertController\""
+ "@\"UIContentUnavailableView\""
+ "@\"WebAppEligibilityViewController\""
+ "T@\"NSString\",?,R,C"
+ "T@\"UIWindow\",?,&,N"
+ "TB,N,V_overrideShowAlert"
+ "WebAppEligibilityViewController"
+ "_FBSScene"
+ "_alertController"
+ "_eligibilityViewController"
+ "_overrideShowAlert"
+ "_shouldLoadWebApp"
+ "_unavailableView"
+ "eligibilityAlert:"
+ "eligibilityStatus"
+ "emptyConfiguration"
+ "initWithConfiguration:"
+ "initWithInfo:responder:"
+ "initWithWebClip:scene:"
+ "isHSWADisabled"
+ "openURL:options:completionHandler:"
+ "overrideShowAlert"
+ "presentAlertIfNeeded"
+ "presentingViewController"
+ "sendActions:"
+ "setAutoresizingMask:"
+ "setOverrideShowAlert:"
+ "setWithObject:"
+ "v12@?0B8"
- "\x02"
- "T@\"UIWindow\",&,N"

```
