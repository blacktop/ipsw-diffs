## FocusUI

> `/System/Library/PrivateFrameworks/FocusUI.framework/FocusUI`

```diff

-371.16.0.0.0
-  __TEXT.__text: 0x223e8
-  __TEXT.__auth_stubs: 0xad0
+371.112.0.0.0
+  __TEXT.__text: 0x2256c
+  __TEXT.__auth_stubs: 0xab0
   __TEXT.__objc_methlist: 0x193c
   __TEXT.__const: 0x1e6
   __TEXT.__gcc_except_tab: 0x248

   __TEXT.__objc_const_ax: 0xb24
   __TEXT.__unwind_info: 0xb78
   __TEXT.__objc_classname: 0x83d
-  __TEXT.__objc_methname: 0x759c
+  __TEXT.__objc_methname: 0x762e
   __TEXT.__objc_methtype: 0x1bee
   __TEXT.__objc_stubs: 0x5740
   __DATA_CONST.__got: 0x170

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xa0f8
   __DATA_CONST.__objc_selrefs: 0x1960
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x318
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__cfstring: 0xcc0
   __AUTH_CONST.__const: 0x3d8
   __AUTH_CONST.__objc_const: 0xef0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x578
-  __AUTH.__objc_data: 0x5e8
+  __AUTH_CONST.__auth_got: 0x568
+  __AUTH.__objc_data: 0x598
   __AUTH.__data: 0x50
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x318
-  __DATA.__objc_superrefs: 0xe0
   __DATA.__objc_ivar: 0x2f0
   __DATA.__objc_data: 0x20
   __DATA.__objc_const_ax: 0x0
   __DATA.__data: 0xee0
   __DATA.__bss: 0xd0
-  __DATA_DIRTY.__objc_data: 0x5f0
+  __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__bss: 0x18
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
+  - /System/Library/PrivateFrameworks/SystemAperture.framework/SystemAperture
+  - /System/Library/PrivateFrameworks/SystemApertureUI.framework/SystemApertureUI
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9CC14211-EAD8-306D-A4DB-D2EB2CE24652
+  UUID: CD859385-0BA3-31AF-AFA7-BFE3498DC093
   Functions: 956
-  Symbols:   3730
-  CStrings:  1716
+  Symbols:   3728
+  CStrings:  1722
 
Symbols:
+ ___block_literal_global.159
- ___block_literal_global.157
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "T@\"<BNPresentableContext>\",?,W,N"
+ "T@\"<BNTemplateItemProviding>\",?,R,N"
+ "T@\"<BNTemplateViewProviding>\",?,R,N"
+ "T@\"<SAActivityHosting>\",?,W,N"
+ "T@\"<SAActivityHosting>\",?,W,N,V_activityHost"
+ "T@\"<SAAlertHosting>\",?,W,N"
+ "T@\"<SAAlertHosting>\",?,W,N,V_alertHost"
+ "T@\"<SAElementHosting>\",?,W,N"
+ "T@\"<SAUILayoutHosting>\",?,W,N"
+ "T@\"<SAUILayoutHosting>\",?,W,N,V_layoutHost"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,C,N,V_preferredContentSizeCategory"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"UIGestureRecognizer\",?,R,N"
+ "T@\"UIView\",?,R,N"
+ "T@\"UIViewController\",?,R,N"
+ "TB,?,N,GisSelected"
+ "TB,?,R,N,GisDraggingDismissalEnabled"
+ "TB,?,R,N,GisDraggingInteractionEnabled"
+ "TB,?,R,N,GisInteractiveDismissalEnabled"
+ "TB,?,R,N,GisMinimalPresentationPossible"
+ "TB,?,R,N,GisRequestingMenuPresentation"
+ "TB,?,R,N,GisTouchOutsideDismissalEnabled"
+ "TQ,?,N"
+ "Tq,?,R,N"
+ "T{CGSize=dd},?,R,N"
- "T@\"<BNPresentableContext>\",W,N"
- "T@\"<BNTemplateItemProviding>\",R,N"
- "T@\"<BNTemplateViewProviding>\",R,N"
- "T@\"<SAActivityHosting>\",W,N"
- "T@\"<SAActivityHosting>\",W,N,V_activityHost"
- "T@\"<SAAlertHosting>\",W,N"
- "T@\"<SAAlertHosting>\",W,N,V_alertHost"
- "T@\"<SAElementHosting>\",W,N"
- "T@\"<SAUILayoutHosting>\",W,N"
- "T@\"<SAUILayoutHosting>\",W,N,V_layoutHost"
- "T@\"NSString\",C,N,V_preferredContentSizeCategory"
- "T@\"UIGestureRecognizer\",R,N"
- "T@\"UIViewController\",R,N"
- "TB,R,N,GisDraggingDismissalEnabled"
- "TB,R,N,GisDraggingInteractionEnabled"
- "TB,R,N,GisInteractiveDismissalEnabled"
- "TB,R,N,GisMinimalPresentationPossible"
- "TB,R,N,GisRequestingMenuPresentation"
- "TB,R,N,GisTouchOutsideDismissalEnabled"
- "TQ,N"
- "T{CGSize=dd},R,N"

```
