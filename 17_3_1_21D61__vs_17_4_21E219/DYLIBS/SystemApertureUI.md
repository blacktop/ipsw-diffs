## SystemApertureUI

> `/System/Library/PrivateFrameworks/SystemApertureUI.framework/SystemApertureUI`

```diff

-61.3.0.0.0
-  __TEXT.__text: 0x10bb0
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0x11f4
+61.107.0.0.0
+  __TEXT.__text: 0x10f28
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_methlist: 0x123c
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0xa11
-  __TEXT.__oslogstring: 0x8ea
+  __TEXT.__cstring: 0xa82
+  __TEXT.__oslogstring: 0x9e1
   __TEXT.__gcc_except_tab: 0x7f0
-  __TEXT.__unwind_info: 0x710
+  __TEXT.__unwind_info: 0x720
   __TEXT.__objc_classname: 0x5a2
-  __TEXT.__objc_methname: 0x4253
-  __TEXT.__objc_methtype: 0x11cf
-  __TEXT.__objc_stubs: 0x2880
+  __TEXT.__objc_methname: 0x4371
+  __TEXT.__objc_methtype: 0x1238
+  __TEXT.__objc_stubs: 0x2920
   __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x4b0
+  __DATA_CONST.__const: 0x4d0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5e10
-  __DATA_CONST.__objc_selrefs: 0xd10
-  __AUTH_CONST.__cfstring: 0x8c0
+  __DATA_CONST.__objc_const: 0x5f20
+  __DATA_CONST.__objc_selrefs: 0xd38
+  __DATA_CONST.__objc_classrefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0x78
+  __AUTH_CONST.__cfstring: 0x9a0
   __AUTH_CONST.__objc_const: 0x5d8
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__auth_got: 0x2b0
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_classrefs: 0x140
-  __DATA.__objc_superrefs: 0x78
+  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x134
   __DATA.__data: 0xba0
-  __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x8
+  __DATA_DIRTY.__objc_data: 0x3c0
+  __DATA_DIRTY.__bss: 0x28
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/SystemAperture.framework/SystemAperture
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C0841F4D-887B-32FF-A513-6584F82F8976
-  Functions: 431
-  Symbols:   1874
-  CStrings:  1002
+  UUID: 940C9A17-CDA8-3B56-B5F2-B827D3E67AB2
+  Functions: 439
+  Symbols:   1899
+  CStrings:  1031
 
Symbols:
+ -[SAUIElementViewController handleElementTap:]
+ -[SAUIElementViewController viewWillTransitionToSize:withTransitionCoordinator:].cold.1
+ -[SAUIIndicatorElementViewController handleElementLongPress:]
+ -[SAUIIndicatorElementViewController handleElementTap:]
+ -[SAUILayoutModePreference layoutModePreferenceMayBeImplicitlyInvalidated]
+ -[SAUILayoutSpecifyingElementViewController _alertingActivityAssertionWithReason:implicitlyDismissable:withPreferredLayoutMode:]
+ -[SAUILayoutSpecifyingElementViewController alertWithReason:implicitlyDismissable:]
+ -[SAUILayoutSpecifyingElementViewController handleElementLongPress:]
+ -[SAUILayoutSpecifyingElementViewController handleElementTap:]
+ -[SAUIPreferredLayoutModeAssertion layoutModePreferenceMayBeImplicitlyInvalidated]
+ GCC_except_table18
+ GCC_except_table19
+ GCC_except_table23
+ GCC_except_table24
+ GCC_except_table56
+ GCC_except_table63
+ GCC_except_table73
+ GCC_except_table91
+ GCC_except_table94
+ _BSStringFromBOOL
+ _NSStringFromCGSize
+ _SAUIStringFromElementViewInteractionResult
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SAUIElementViewControlling
+ ___128-[SAUILayoutSpecifyingElementViewController _alertingActivityAssertionWithReason:implicitlyDismissable:withPreferredLayoutMode:]_block_invoke
+ ___46-[SAUIElementViewController handleElementTap:]_block_invoke
+ ___83-[SAUILayoutSpecifyingElementViewController alertWithReason:implicitlyDismissable:]_block_invoke
+ _objc_msgSend$_alertingActivityAssertionWithReason:implicitlyDismissable:withPreferredLayoutMode:
+ _objc_msgSend$handleElementLongPress:
+ _objc_msgSend$handleElementTap:
+ _objc_msgSend$layoutModePreferenceMayBeImplicitlyInvalidated
+ _objc_msgSend$setUserInteractionEnabled:
+ _objc_msgSend$valueForKey:
+ _objc_retain_x28
- -[SAUIElementViewController handleTap:]
- -[SAUILayoutSpecifyingElementViewController _alertingActivityAssertionWithReason:withPreferredLayoutMode:]
- -[SAUILayoutSpecifyingElementViewController alertWithReason:]
- GCC_except_table15
- GCC_except_table16
- GCC_except_table21
- GCC_except_table22
- GCC_except_table46
- GCC_except_table59
- GCC_except_table67
- GCC_except_table89
- GCC_except_table92
- ___106-[SAUILayoutSpecifyingElementViewController _alertingActivityAssertionWithReason:withPreferredLayoutMode:]_block_invoke
- ___39-[SAUIElementViewController handleTap:]_block_invoke
- ___61-[SAUILayoutSpecifyingElementViewController alertWithReason:]_block_invoke
- _objc_msgSend$_alertingActivityAssertionWithReason:withPreferredLayoutMode:
CStrings:
+ "@\"<SAAutomaticallyInvalidatable>\"28@0:8@\"NSString\"16B24"
+ "@36@0:8@16B24q28"
+ "Custom"
+ "Expand"
+ "T@\"<SAUILayoutHosting>\",?,W,N"
+ "T@\"<SAUILayoutHosting>\",?,W,N,V_layoutHost"
+ "T@\"<SAUILayoutModePreferring>\",?,R,N"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"SAUIPreferredLayoutModeAssertion\",?,R,N"
+ "TB,?,R,N,GisInteractiveDismissalEnabled"
+ "TB,?,R,N,GisMinimalPresentationPossible"
+ "TB,?,R,N,GisRequestingMenuPresentation"
+ "TB,R,N"
+ "TQ,?,N"
+ "TQ,?,N,V_layoutAxis"
+ "T{CGSize=dd},?,R,N"
+ "Unhandled"
+ "View will transition isTransitioning:%{public}@ isInActiveTransition:%{public}@ clientShouldLayoutImmediately:%{public}@"
+ "View will transition to size: %{public}@, layoutMode: %{public}@ -> %{public}@"
+ "View will transition with settings: %{public}@"
+ "__animator"
+ "__mainContext"
+ "_alertingActivityAssertionWithReason:implicitlyDismissable:withPreferredLayoutMode:"
+ "_fluidBehaviorSettings"
+ "alertWithReason:implicitlyDismissable:"
+ "handleElementLongPress:"
+ "handleElementTap:"
+ "implicitly dismissable alerting activity"
+ "layoutModePreferenceMayBeImplicitlyInvalidated"
+ "q24@0:8@\"UIGestureRecognizer\"16"
+ "setUserInteractionEnabled:"
+ "valueForKey:"
- "T@\"<SAUILayoutHosting>\",W,N"
- "T@\"<SAUILayoutModePreferring>\",R,N"
- "T@\"SAUIPreferredLayoutModeAssertion\",R,N"
- "TB,R,N,GisInteractiveDismissalEnabled"
- "TB,R,N,GisMinimalPresentationPossible"
- "TB,R,N,GisRequestingMenuPresentation"
- "TQ,N"
- "TQ,N,V_layoutAxis"
- "T{CGSize=dd},R,N"
- "_alertingActivityAssertionWithReason:withPreferredLayoutMode:"
- "alertWithReason:"

```
