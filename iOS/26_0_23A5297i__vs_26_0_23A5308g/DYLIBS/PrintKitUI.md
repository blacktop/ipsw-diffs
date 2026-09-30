## PrintKitUI

> `/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI`

```diff

-77.0.0.0.0
-  __TEXT.__text: 0x5f914
+78.0.0.0.0
+  __TEXT.__text: 0x5f974
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x6edc
+  __TEXT.__objc_methlist: 0x6ef4
   __TEXT.__const: 0x320
   __TEXT.__cstring: 0x26de
   __TEXT.__ustring: 0x182
-  __TEXT.__gcc_except_tab: 0x13dc
+  __TEXT.__gcc_except_tab: 0x13d0
   __TEXT.__dlopen_cstrs: 0x95
-  __TEXT.__unwind_info: 0x1588
+  __TEXT.__unwind_info: 0x1590
   __TEXT.__objc_classname: 0xc1f
-  __TEXT.__objc_methname: 0x13dcd
+  __TEXT.__objc_methname: 0x13df7
   __TEXT.__objc_methtype: 0x3a69
   __TEXT.__objc_stubs: 0xe820
   __DATA_CONST.__got: 0x900

   __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x34c0
-  __AUTH_CONST.__objc_const: 0xa6c8
+  __AUTH_CONST.__objc_const: 0xa6f8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x7d8
+  __DATA.__objc_ivar: 0x7dc
   __DATA.__data: 0xcc8
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x1720

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 996BB14A-39AD-3BB1-8E08-02EF900D7413
-  Functions: 2222
-  Symbols:   8278
+  UUID: 8A633E8C-BBE2-32F9-A178-7A6372651749
+  Functions: 2225
+  Symbols:   8285
   CStrings:  4640
 
Symbols:
+ -[UIPrintPagesController initWithPrintInfo:delegate:usingWebKitFormatter:]
+ -[UIPrintPreviewViewController setUsingWebKitFormatter:]
+ -[UIPrintPreviewViewController usingWebKitFormatter]
+ -[UIPrintSheetController initWithPrintInfo:printPageImageDelegate:usingWebKitFormatter:]
+ _OBJC_IVAR_$_UIPrintPreviewViewController._usingWebKitFormatter
+ _drawPage
+ _objc_msgSend$initWithPrintInfo:delegate:usingWebKitFormatter:
+ _objc_msgSend$initWithPrintInfo:printPageImageDelegate:usingWebKitFormatter:
- -[UIPrintPagesController initWithPrintInfo:delegate:]
- -[UIPrintSheetController initWithPrintInfo:printPageImageDelegate:]
- _objc_msgSend$initWithPrintInfo:delegate:
- _objc_msgSend$initWithPrintInfo:printPageImageDelegate:
CStrings:
+ "initWithPrintInfo:delegate:usingWebKitFormatter:"
+ "initWithPrintInfo:printPageImageDelegate:usingWebKitFormatter:"
- "initWithPrintInfo:delegate:"
- "initWithPrintInfo:printPageImageDelegate:"

```
