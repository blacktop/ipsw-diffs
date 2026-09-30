## MusicStoreUI

> `/System/Library/PrivateFrameworks/MusicStoreUI.framework/MusicStoreUI`

```diff

-1202.4.6.0.0
-  __TEXT.__text: 0x88f4
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0xc54
-  __TEXT.__cstring: 0x6a3
-  __TEXT.__const: 0x100
-  __TEXT.__unwind_info: 0x2f0
+1202.4.8.0.0
+  __TEXT.__text: 0x8d44
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_methlist: 0xc34
+  __TEXT.__const: 0x108
+  __TEXT.__gcc_except_tab: 0x10
+  __TEXT.__cstring: 0x6df
+  __TEXT.__unwind_info: 0x310
   __TEXT.__objc_classname: 0x252
-  __TEXT.__objc_methname: 0x2ef5
-  __TEXT.__objc_methtype: 0x630
-  __TEXT.__objc_stubs: 0x3380
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0x178
+  __TEXT.__objc_methname: 0x2f5e
+  __TEXT.__objc_methtype: 0x625
+  __TEXT.__objc_stubs: 0x33e0
+  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__const: 0x1c8
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1028
+  __DATA_CONST.__objc_selrefs: 0x1048
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x1b0
+  __AUTH_CONST.__auth_got: 0x1d0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__objc_const: 0x17f8
   __AUTH.__objc_data: 0x640
   __AUTH.__data: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C615E85-819B-3723-BBC6-C2BFFB9D3153
-  Functions: 219
-  Symbols:   1241
-  CStrings:  803
+  UUID: 946022DB-34A0-3779-AD14-59066B71DEC8
+  Functions: 226
+  Symbols:   1266
+  CStrings:  810
 
Symbols:
+ -[MSTonePurchaseContinuation _destroyAlert]
+ -[MSTonePurchaseContinuation viewControllerForPresenting]
+ GCC_except_table9
+ OBJC_IVAR_$_MSTonePurchaseContinuation._alertController
+ _OBJC_CLASS_$_UIAlertAction
+ _OBJC_CLASS_$_UIAlertController
+ _OBJC_CLASS_$_UIWindowScene
+ __Block_object_assign
+ __Block_object_dispose
+ __Unwind_Resume
+ ___35-[MSTonePurchaseContinuation start]_block_invoke
+ ___35-[MSTonePurchaseContinuation start]_block_invoke_2
+ ___35-[MSTonePurchaseContinuation start]_block_invoke_3
+ ___35-[MSTonePurchaseContinuation start]_block_invoke_4
+ ___52-[MSTonePurchaseContinuation _pickAssigneeToneStyle]_block_invoke
+ ___52-[MSTonePurchaseContinuation _pickAssigneeToneStyle]_block_invoke_2
+ ___52-[MSTonePurchaseContinuation _pickAssigneeToneStyle]_block_invoke_3
+ ___57-[MSTonePurchaseContinuation viewControllerForPresenting]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_40_e8_32o_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_descriptor_40_e8_32r_e28_v24?0"UISceneSession"8^B16lr32l8
+ ___objc_personality_v0
+ _objc_msgSend$_destroyAlert
+ _objc_msgSend$actionWithTitle:style:handler:
+ _objc_msgSend$addAction:
+ _objc_msgSend$alertControllerWithTitle:message:preferredStyle:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$openSessions
+ _objc_msgSend$popoverPresentationController
+ _objc_msgSend$scene
+ _objc_msgSend$viewControllerForPresenting
+ _objc_msgSend$windows
- -[MSTonePurchaseContinuation _destroyAlertView]
- -[MSTonePurchaseContinuation actionSheet:didDismissWithButtonIndex:]
- -[MSTonePurchaseContinuation actionSheetCancel:]
- -[MSTonePurchaseContinuation alertView:didDismissWithButtonIndex:]
- -[MSTonePurchaseContinuation alertViewCancel:]
- OBJC_IVAR_$_MSTonePurchaseContinuation._alertView
- _OBJC_CLASS_$_UIActionSheet
- _OBJC_CLASS_$_UIAlertView
- _objc_msgSend$addButtonWithTitle:
- _objc_msgSend$cancelButtonIndex
- _objc_msgSend$dismissWithClickedButtonIndex:animated:
- _objc_msgSend$setBodyText:
- _objc_msgSend$setCancelButtonIndex:
- _objc_msgSend$setTitle:
- _objc_msgSend$show
- _objc_msgSend$showInView:
CStrings:
+ "@\"UIAlertController\""
+ "Cancel"
+ "_alertController"
+ "_destroyAlert"
+ "actionWithTitle:style:handler:"
+ "addAction:"
+ "alertControllerWithTitle:message:preferredStyle:"
+ "enumerateObjectsUsingBlock:"
+ "mainBundle"
+ "openSessions"
+ "popoverPresentationController"
+ "scene"
+ "v16@?0@\"UIAlertAction\"8"
+ "v24@?0@\"UISceneSession\"8^B16"
+ "viewControllerForPresenting"
+ "windows"
- "@\"UIActionSheet\""
- "@\"UIAlertView\""
- "_alertView"
- "addButtonWithTitle:"
- "cancelButtonIndex"
- "dismissWithClickedButtonIndex:animated:"
- "setBodyText:"
- "setCancelButtonIndex:"
- "show"
- "showInView:"

```
