## AppSSOUI

> `/System/Library/PrivateFrameworks/AppSSOUI.framework/AppSSOUI`

```diff

-483.120.4.0.0
-  __TEXT.__text: 0x17f0
-  __TEXT.__auth_stubs: 0x2b0
+635.0.0.0.0
+  __TEXT.__text: 0x156c
   __TEXT.__objc_methlist: 0x274
   __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x10
   __TEXT.__oslogstring: 0x1b4
-  __TEXT.__cstring: 0x263
+  __TEXT.__cstring: 0x269
   __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0x6d
-  __TEXT.__objc_methname: 0x75d
-  __TEXT.__objc_methtype: 0x269
-  __TEXT.__objc_stubs: 0x420
-  __DATA_CONST.__got: 0x58
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xf8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x250
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x340
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x50
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0x120
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55A6EC8B-0A2F-3ED1-A5F2-86A7DC9D8964
-  Functions: 41
+  UUID: 5889C09D-AC2C-3809-9421-B601E753C28F
+  Functions: 39
   Symbols:   223
-  CStrings:  153
+  CStrings:  30
 
Symbols:
+ ___105-[SOUIAuthorizationViewController initWithExtensionViewController:hints:presentViewControllerCompletion:]_block_invoke.43
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- ___105-[SOUIAuthorizationViewController initWithExtensionViewController:hints:presentViewControllerCompletion:]_block_invoke.3
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<SOUIAuthorizationViewControllerDelegate>\""
- "@\"NSString\"16@0:8"
- "@\"NSTimer\""
- "@\"UIViewController\""
- "@\"_UIRemoteViewController\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@?32"
- "@?"
- "@?16@0:8"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIGestureRecognizer\"16"
- "B24@0:8@16"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIEvent\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIGestureRecognizer\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIPress\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UITouch\"24"
- "B32@0:8@16@24"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<SOUIAuthorizationViewControllerDelegate>\",W,V_delegate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"_UIRemoteViewController\",R,N"
- "T@?,C,N,V_dismissCompletionHandler"
- "TQ,R"
- "UIGestureRecognizerDelegate"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_UIRemoteViewControllerContaining"
- "_cancel"
- "_containedRemoteViewController"
- "_delegate"
- "_dismissCompletionHandler"
- "_extensionViewController"
- "_presentViewControllerCompletionBlock"
- "_presentViewControllerTimer"
- "_rootSheetPresentationController"
- "_setShouldScaleDownBehindDescendantSheets:"
- "addChildViewController:"
- "addGestureRecognizer:"
- "addSubview:"
- "addTimer:forMode:"
- "autorelease"
- "bottomAnchor"
- "class"
- "clearColor"
- "conformsToProtocol:"
- "constraintEqualToAnchor:"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "didMoveToParentViewController:"
- "dismissCompletionHandler"
- "dismissViewControllerAnimated:completion:"
- "gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:"
- "gestureRecognizer:shouldReceiveEvent:"
- "gestureRecognizer:shouldReceivePress:"
- "gestureRecognizer:shouldReceiveTouch:"
- "gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:"
- "gestureRecognizer:shouldRequireFailureOfGestureRecognizer:"
- "gestureRecognizerShouldBegin:"
- "hash"
- "init"
- "initWithExtensionViewController:hints:"
- "initWithExtensionViewController:hints:presentViewControllerCompletion:"
- "integerValue"
- "internalErrorWithMessage:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "keyWindow"
- "leadingAnchor"
- "loadView"
- "mainRunLoop"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setActive:"
- "setBackgroundColor:"
- "setDelegate:"
- "setDismissCompletionHandler:"
- "setModalPresentationStyle:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setView:"
- "shouldAutorotate"
- "superclass"
- "supportedInterfaceOrientations"
- "timerWithTimeInterval:repeats:block:"
- "topAnchor"
- "trailingAnchor"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v28@0:8B16@?20"
- "view"
- "viewControllerDidCancel:"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLoad"
- "viewWillAppear:"
- "viewWillDisappear:"
- "zone"

```
