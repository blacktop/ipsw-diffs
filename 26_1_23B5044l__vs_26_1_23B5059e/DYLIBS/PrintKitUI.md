## PrintKitUI

> `/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI`

```diff

-78.1.0.0.0
-  __TEXT.__text: 0x5fbac
+78.2.0.0.0
+  __TEXT.__text: 0x5fdfc
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x6eec
+  __TEXT.__objc_methlist: 0x6efc
   __TEXT.__const: 0x320
-  __TEXT.__cstring: 0x26de
+  __TEXT.__cstring: 0x2706
   __TEXT.__ustring: 0x182
-  __TEXT.__gcc_except_tab: 0x13d0
+  __TEXT.__gcc_except_tab: 0x13f4
   __TEXT.__dlopen_cstrs: 0x95
-  __TEXT.__unwind_info: 0x1588
+  __TEXT.__unwind_info: 0x1598
   __TEXT.__objc_classname: 0xc0c
-  __TEXT.__objc_methname: 0x13e06
-  __TEXT.__objc_methtype: 0x3a69
-  __TEXT.__objc_stubs: 0xe7e0
+  __TEXT.__objc_methname: 0x13e4f
+  __TEXT.__objc_methtype: 0x3a74
+  __TEXT.__objc_stubs: 0xe800
   __DATA_CONST.__got: 0x8f8
-  __DATA_CONST.__const: 0xf30
+  __DATA_CONST.__const: 0xf50
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x47b8
+  __DATA_CONST.__objc_selrefs: 0x47b0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x34c0
-  __AUTH_CONST.__objc_const: 0xa660
+  __AUTH_CONST.__objc_const: 0xa680
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E6BE0DA2-B722-3874-B082-7EB425972038
-  Functions: 2226
-  Symbols:   8278
-  CStrings:  4639
+  UUID: 3DD6ADB0-AE85-3B48-ADA6-EF458CBB0545
+  Functions: 2227
+  Symbols:   8284
+  CStrings:  4645
 
Symbols:
+ -[UIPrintInteractionController completionHandler]
+ -[UIPrintInteractionController setCompletionHandler:]
+ -[UIPrintPaper paperOrientation]
+ -[UIPrintPaper pkPaper]
+ -[UIPrintPaper setPaperOrientation:]
+ -[UIPrintPaper setPkPaper:]
+ GCC_except_table56
+ _OBJC_IVAR_$_UIPrintPaper._pkPaper
+ ___block_descriptor_32_e39_B24?0"UIPrintPaper"8"NSDictionary"16l
+ _objc_msgSend$completionHandler
+ _objc_msgSend$paperOrientation
+ _objc_msgSend$pkPaper
+ _objc_msgSend$setPaperOrientation:
+ _objc_msgSend$setPkPaper:
- -[UIPrintInteractionController _completionHandler]
- -[UIPrintInteractionController set_completionHandler:]
- -[UIPrintPaper _paperOrientation]
- -[UIPrintPaper _pkPaper]
- -[UIPrintPaper _setPaperOrientation:]
- _OBJC_IVAR_$_UIPrintPaper._internal
- _objc_msgSend$_completionHandler
- _objc_msgSend$_pkPaper
- _objc_msgSend$_setPaperOrientation:
- _objc_msgSend$set_completionHandler:
CStrings:
+ "@\"PKPaper\""
+ "B24@?0@\"UIPrintPaper\"8@\"NSDictionary\"16"
+ "T@\"PKPaper\",&,V_pkPaper"
+ "T@\"PKPrinter\",&"
+ "T@\"PKPrinter\",&,V_printer"
+ "Ti,V_paperOrientation"
+ "paperOrientation"
+ "pkPaper"
+ "setPaperOrientation:"
+ "setPkPaper:"
+ "\xd1\xf0\x91"
- "T@\"PKPrinter\",&,N"
- "_internal"
- "_setPaperOrientation:"
- "set_completionHandler:"
- "\xe1\xf0\x81"

```
