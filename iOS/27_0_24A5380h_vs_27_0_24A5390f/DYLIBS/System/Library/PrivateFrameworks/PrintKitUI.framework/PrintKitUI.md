## PrintKitUI

> `/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-93.0.0.0.0
-  __TEXT.__text: 0x655d8
+94.0.0.0.0
+  __TEXT.__text: 0x6560c
   __TEXT.__objc_methlist: 0x716c
   __TEXT.__const: 0x310
   __TEXT.__gcc_except_tab: 0x1c9c

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4968
+  __DATA_CONST.__objc_selrefs: 0x4970
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x358

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2299
-  Symbols:   6204
+  Symbols:   6205
   CStrings:  559
 
Symbols:
+ -[UIPrintPreviewViewController printPanelDidDismiss]
+ _objc_msgSend$printPanelDidDismiss
- -[UIPrintPreviewViewController dealloc]
Functions:
~ -[UIPrintInteractionController _printPageWithDelay:] : 216 -> 204
~ -[UIPrintPagesController baseImageForPageNum:] : 808 -> 800
~ -[UIPrintPreviewViewController dealloc] -> -[UIPrintPreviewViewController printPanelDidDismiss] : 964 -> 952
~ -[UIPrintPanelViewController printNavigationConrollerDidDismiss] : 316 -> 380
~ -[UIPrintPanelViewController dismissPrintPanelWithAction:animated:completionHandler:] : 500 -> 548
~ -[UIPrintPageRenderer _drawPageAtIndex:withScale:drawingToPDF:] : 264 -> 236
```
