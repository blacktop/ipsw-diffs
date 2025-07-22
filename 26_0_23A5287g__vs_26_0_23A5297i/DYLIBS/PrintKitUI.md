## PrintKitUI

> `/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI`

```diff

-76.0.0.0.0
-  __TEXT.__text: 0x5f70c
-  __TEXT.__auth_stubs: 0xf10
+77.0.0.0.0
+  __TEXT.__text: 0x5f914
+  __TEXT.__auth_stubs: 0xf00
   __TEXT.__objc_methlist: 0x6edc
   __TEXT.__const: 0x320
   __TEXT.__cstring: 0x26de
   __TEXT.__ustring: 0x182
-  __TEXT.__gcc_except_tab: 0x13f8
+  __TEXT.__gcc_except_tab: 0x13dc
   __TEXT.__dlopen_cstrs: 0x95
-  __TEXT.__unwind_info: 0x1580
+  __TEXT.__unwind_info: 0x1588
   __TEXT.__objc_classname: 0xc1f
-  __TEXT.__objc_methname: 0x13d79
+  __TEXT.__objc_methname: 0x13dcd
   __TEXT.__objc_methtype: 0x3a69
-  __TEXT.__objc_stubs: 0xe7c0
-  __DATA_CONST.__got: 0x8f8
+  __TEXT.__objc_stubs: 0xe820
+  __DATA_CONST.__got: 0x900
   __DATA_CONST.__const: 0xf30
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x47b0
+  __DATA_CONST.__objc_selrefs: 0x47c8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x798
+  __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x34c0
   __AUTH_CONST.__objc_const: 0xa6c8

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CE715BFE-A7D8-3AFA-98DC-50AC31B6C5F5
+  UUID: 996BB14A-39AD-3BB1-8E08-02EF900D7413
   Functions: 2222
-  Symbols:   8275
-  CStrings:  4637
+  Symbols:   8278
+  CStrings:  4640
 
Symbols:
+ _OBJC_CLASS_$_NSFileHandle
+ ___block_literal_global.160
+ ___block_literal_global.184
+ _objc_msgSend$fileHandleForReadingFromURL:error:
+ _objc_msgSend$readDataUpToLength:error:
+ _objc_msgSend$setAccessibilityLabel:
- _CGDataProviderCopyData
- ___block_literal_global.159
- ___block_literal_global.183
Functions:
~ -[UIPrintInteractionController _cleanPrintState] : 316 -> 416
~ +[UIPrintInteractionController createCGPDFDocumentRefWithNSURL:] : 244 -> 300
~ -[UIPrintPreviewViewController setupLayoutControl] : 2536 -> 2420
~ -[UIPrintPreviewViewController viewWillDisappear:] : 60 -> 88
~ -[UIPrintPreviewViewController viewWillAppear:] : 60 -> 88
~ -[UIPrintPreviewViewController updateLayoutControl] : 1644 -> 2100
~ -[UIPrintPreviewViewController layoutPopupButtonChanged:] : 284 -> 96
~ -[UIPrintPreviewViewController updatePageRange:] : 472 -> 468
~ -[UIPrintPanelViewController showCompactPreview] : 3688 -> 3796
~ -[UIPrintPanelViewController viewWillAppear:] : 112 -> 164
CStrings:
+ "fileHandleForReadingFromURL:error:"
+ "readDataUpToLength:error:"
+ "setAccessibilityLabel:"

```
