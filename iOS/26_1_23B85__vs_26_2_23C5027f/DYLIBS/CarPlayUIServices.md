## CarPlayUIServices

> `/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`

```diff

-526.16.2.3.0
-  __TEXT.__text: 0x1b64c
+526.23.1.0.0
+  __TEXT.__text: 0x1bdb4
   __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x2d5c
+  __TEXT.__objc_methlist: 0x2e4c
   __TEXT.__const: 0x1f0
   __TEXT.__oslogstring: 0xc48
-  __TEXT.__cstring: 0x1328
+  __TEXT.__cstring: 0x1331
   __TEXT.__gcc_except_tab: 0x420
-  __TEXT.__unwind_info: 0x960
-  __TEXT.__objc_classname: 0xefa
-  __TEXT.__objc_methname: 0x5af1
-  __TEXT.__objc_methtype: 0x1339
-  __TEXT.__objc_stubs: 0x3d60
-  __DATA_CONST.__got: 0x3d8
+  __TEXT.__unwind_info: 0x980
+  __TEXT.__objc_classname: 0xf18
+  __TEXT.__objc_methname: 0x5dc1
+  __TEXT.__objc_methtype: 0x1460
+  __TEXT.__objc_stubs: 0x3fa0
+  __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__const: 0x8f0
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1528
+  __DATA_CONST.__objc_selrefs: 0x15e0
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x290
   __AUTH_CONST.__const: 0x4e0
   __AUTH_CONST.__cfstring: 0x11a0
-  __AUTH_CONST.__objc_const: 0xef08
+  __AUTH_CONST.__objc_const: 0xefe8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1900
-  __DATA.__objc_ivar: 0x31c
-  __DATA.__data: 0xfc8
+  __DATA.__objc_ivar: 0x32c
+  __DATA.__data: 0x1028
   __DATA.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EDF8704C-439B-3376-9DFC-EB793CB53082
-  Functions: 932
-  Symbols:   4058
-  CStrings:  1663
+  UUID: 23EF59F9-B798-3064-BB1F-F4D98BA003E3
+  Functions: 948
+  Symbols:   4120
+  CStrings:  1703
 
Symbols:
+ -[CRSUICAPackageView availableStates]
+ -[CRSUICAPackageView dealloc]
+ -[CRSUICAPackageView delegate]
+ -[CRSUICAPackageView displayLinkDidFire:]
+ -[CRSUICAPackageView displayLink]
+ -[CRSUICAPackageView hasNotifiedPlaybackFinished]
+ -[CRSUICAPackageView hasState:]
+ -[CRSUICAPackageView initWithPackage:state:dynamicStateProvider:delegate:]
+ -[CRSUICAPackageView initWithPackage:state:dynamicStateProvider:delegate:].cold.1
+ -[CRSUICAPackageView setDelegate:]
+ -[CRSUICAPackageView setDisplayLink:]
+ -[CRSUICAPackageView setHasNotifiedPlaybackFinished:]
+ -[CRSUICAPackageView startDisplayLink]
+ -[CRSUICAPackageView stateController:didSetStateOfLayer:]
+ -[CRSUICAPackageView stateController:transitionDidStart:speed:]
+ -[CRSUICAPackageView stateController:transitionDidStop:completed:]
+ -[CRSUICAPackageView stopDisplayLink]
+ _NSRunLoopCommonModes
+ _OBJC_CLASS_$_CADisplayLink
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_IVAR_$_CRSUICAPackageView._delegate
+ _OBJC_IVAR_$_CRSUICAPackageView._displayLink
+ _OBJC_IVAR_$_CRSUICAPackageView._hasNotifiedPlaybackFinished
+ _OBJC_IVAR_$_CRSUICAPackageView._stateControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CAStateControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAStateControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CRSUICAPackageView
+ __OBJC_LABEL_PROTOCOL_$_CAStateControllerDelegate
+ __OBJC_PROTOCOL_$_CAStateControllerDelegate
+ _objc_msgSend$addToRunLoop:forMode:
+ _objc_msgSend$allKeys
+ _objc_msgSend$array
+ _objc_msgSend$caPackageView:didCompleteStateTransition:toState:
+ _objc_msgSend$caPackageViewDidFinishPlayback:
+ _objc_msgSend$displayLink
+ _objc_msgSend$displayLinkWithTarget:selector:
+ _objc_msgSend$documentDuration
+ _objc_msgSend$hasNotifiedPlaybackFinished
+ _objc_msgSend$initWithPackage:state:dynamicStateProvider:delegate:
+ _objc_msgSend$mainRunLoop
+ _objc_msgSend$performSelector:
+ _objc_msgSend$setDisplayLink:
+ _objc_msgSend$setHasNotifiedPlaybackFinished:
+ _objc_msgSend$setInitialStatesOfLayer:
+ _objc_msgSend$startDisplayLink
+ _objc_msgSend$stopDisplayLink
+ _objc_msgSend$toState
- -[CRSUICAPackageView initWithPackage:state:dynamicStateProvider:].cold.1
CStrings:
+ "!A"
+ "-[CRSUICAPackageView initWithPackage:state:dynamicStateProvider:delegate:]"
+ "@\"<CRSUICAPackageViewDelegate>\""
+ "@\"CADisplayLink\""
+ "@\"NSObject<CAStateControllerDelegate>\""
+ "@48@0:8@16@24@?32@40"
+ "CAStateControllerDelegate"
+ "T@\"<CRSUICAPackageViewDelegate>\",W,N"
+ "T@\"CADisplayLink\",&,N,V_displayLink"
+ "TB,N,V_hasNotifiedPlaybackFinished"
+ "_displayLink"
+ "_hasNotifiedPlaybackFinished"
+ "_stateControllerDelegate"
+ "addToRunLoop:forMode:"
+ "allKeys"
+ "array"
+ "availableStates"
+ "caPackageView:didCompleteStateTransition:toState:"
+ "caPackageViewDidFinishPlayback:"
+ "displayLink"
+ "displayLinkDidFire:"
+ "displayLinkWithTarget:selector:"
+ "hasNotifiedPlaybackFinished"
+ "hasState:"
+ "initWithPackage:state:dynamicStateProvider:delegate:"
+ "mainRunLoop"
+ "setDisplayLink:"
+ "setHasNotifiedPlaybackFinished:"
+ "setInitialStatesOfLayer:"
+ "startDisplayLink"
+ "stateController:didSetStateOfLayer:"
+ "stateController:transitionDidStart:speed:"
+ "stateController:transitionDidStop:completed:"
+ "states"
+ "stopDisplayLink"
+ "toState"
+ "v32@0:8@\"CAStateController\"16@\"CALayer\"24"
+ "v36@0:8@\"CAStateController\"16@\"CAStateTransition\"24B32"
+ "v36@0:8@\"CAStateController\"16@\"CAStateTransition\"24f32"
+ "v36@0:8@16@24B32"
+ "v36@0:8@16@24f32"
- "-[CRSUICAPackageView initWithPackage:state:dynamicStateProvider:]"

```
