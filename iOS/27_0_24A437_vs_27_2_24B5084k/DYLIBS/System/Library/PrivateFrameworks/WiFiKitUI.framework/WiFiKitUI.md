## WiFiKitUI

> `/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`

```diff

-1205.81.4.2.0
-  __TEXT.__text: 0x914cc
-  __TEXT.__objc_methlist: 0x6600
-  __TEXT.__const: 0x2b24
-  __TEXT.__cstring: 0x7d30
-  __TEXT.__oslogstring: 0x337d
+1207.6.0.0.0
+  __TEXT.__text: 0x917ac
+  __TEXT.__objc_methlist: 0x6620
+  __TEXT.__const: 0x2b14
+  __TEXT.__cstring: 0x7d20
+  __TEXT.__oslogstring: 0x33bd
   __TEXT.__gcc_except_tab: 0xe9c
   __TEXT.__swift5_typeref: 0x4c22
   __TEXT.__swift5_reflstr: 0x8ea

   __TEXT.__swift5_proto: 0x88
   __TEXT.__swift5_types: 0x78
   __TEXT.__swift5_capture: 0x6a0
-  __TEXT.__unwind_info: 0x23a8
+  __TEXT.__unwind_info: 0x23b0
   __TEXT.__eh_frame: 0x370
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ce8
+  __DATA_CONST.__objc_selrefs: 0x3d18
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x150
-  __DATA_CONST.__got: 0x8d8
+  __DATA_CONST.__got: 0x8e0
   __AUTH_CONST.__const: 0x1ce0
-  __AUTH_CONST.__cfstring: 0x61e0
-  __AUTH_CONST.__objc_const: 0x12600
+  __AUTH_CONST.__cfstring: 0x6160
+  __AUTH_CONST.__objc_const: 0x12630
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xd48
   __AUTH.__objc_data: 0x20c8
   __AUTH.__data: 0x2c0
-  __DATA.__objc_ivar: 0x720
+  __DATA.__objc_ivar: 0x724
   __DATA.__data: 0x16f8
   __DATA.__common: 0xe0
   __DATA_DIRTY.__objc_data: 0x2c8

   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
+  - /System/Library/Frameworks/Symbols.framework/Symbols
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/CertInfo.framework/CertInfo

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3377
-  Symbols:   5328
-  CStrings:  1346
+  Functions: 3380
+  Symbols:   5339
+  CStrings:  1343
 
Symbols:
+ -[WFBuddyViewController _setUpHeaderSymbolView]
+ -[WFBuddyViewController didDrawOnHeaderSymbol]
+ -[WFBuddyViewController headerSymbolView]
+ -[WFBuddyViewController setDidDrawOnHeaderSymbol:]
+ -[WFBuddyViewController setHeaderSymbolView:]
+ GCC_except_table22
+ _OBJC_CLASS_$_NSSymbolDisappearEffect
+ _OBJC_CLASS_$_NSSymbolDrawOnEffect
+ _OBJC_CLASS_$_NSSymbolEffectOptions
+ _OBJC_IVAR_$_WFBuddyViewController._didDrawOnHeaderSymbol
+ _OBJC_IVAR_$_WFBuddyViewController._headerSymbolView
+ _objc_msgSend$_setUpHeaderSymbolView
+ _objc_msgSend$addSymbolEffect:options:animated:
+ _objc_msgSend$configurationWithColorRenderingMode:
+ _objc_msgSend$configurationWithPointSize:weight:
+ _objc_msgSend$customIconContainerView
+ _objc_msgSend$didDrawOnHeaderSymbol
+ _objc_msgSend$effect
+ _objc_msgSend$effectWithByLayer
+ _objc_msgSend$headerSymbolView
+ _objc_msgSend$options
+ _objc_msgSend$optionsWithNonRepeating
+ _objc_msgSend$setDidDrawOnHeaderSymbol:
+ _objc_msgSend$setHeaderSymbolView:
- -[WFBuddyViewController animationController]
- -[WFBuddyViewController setAnimationController:]
- GCC_except_table8
- _OBJC_CLASS_$_OBAnimationController
- _OBJC_CLASS_$_OBAnimationState
- _OBJC_IVAR_$_WFBuddyViewController._animationController
- _objc_msgSend$URLForResource:withExtension:
- _objc_msgSend$animationController
- _objc_msgSend$animationView
- _objc_msgSend$initWithStateName:transitionDuration:transitionSpeed:
- _objc_msgSend$initWithUrlToPackage:animationView:animatedStates:startAtFirstState:
- _objc_msgSend$setAnimationController:
- _objc_msgSend$startAnimation
CStrings:
+ "Buddy header has no custom icon container, leaving the header symbol unset"
- "State 1"
- "State 2"
- "WIFI"
- "ca"
```
