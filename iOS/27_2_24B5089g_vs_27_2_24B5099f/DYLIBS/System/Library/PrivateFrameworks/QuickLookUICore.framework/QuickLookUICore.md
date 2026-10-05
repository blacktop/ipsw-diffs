## QuickLookUICore

> `/System/Library/PrivateFrameworks/QuickLookUICore.framework/QuickLookUICore`

```diff

-1034.1.3.0.0
-  __TEXT.__text: 0x20864
+1034.1.4.0.0
+  __TEXT.__text: 0x209d4
   __TEXT.__delay_stubs: 0x1c0
   __TEXT.__delay_helper: 0x25c
-  __TEXT.__objc_methlist: 0x314c
+  __TEXT.__objc_methlist: 0x317c
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x1ffe
-  __TEXT.__gcc_except_tab: 0x850
+  __TEXT.__cstring: 0x2011
+  __TEXT.__gcc_except_tab: 0x868
   __TEXT.__oslogstring: 0x1892
   __TEXT.__unwind_info: 0xca8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2100
+  __DATA_CONST.__objc_selrefs: 0x2110
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__got: 0x4e0
   __AUTH_CONST.__const: 0x1f0
-  __AUTH_CONST.__cfstring: 0x2020
-  __AUTH_CONST.__objc_const: 0x7628
+  __AUTH_CONST.__cfstring: 0x2040
+  __AUTH_CONST.__objc_const: 0x7688
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x3a8
+  __DATA.__objc_ivar: 0x3b0
   __DATA.__data: 0x78c
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x30

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1030
-  Symbols:   2149
-  CStrings:  409
+  Functions: 1034
+  Symbols:   2155
+  CStrings:  410
 
Symbols:
+ -[QLItem canEnterFullScreen]
+ -[QLItem setCanEnterFullScreen:]
+ -[QLPreviewContext canEnterFullScreen]
+ -[QLPreviewContext setCanEnterFullScreen:]
+ _OBJC_IVAR_$_QLItem._canEnterFullScreen
+ _OBJC_IVAR_$_QLPreviewContext._canEnterFullScreen
Functions:
~ -[QLItem _commonInit] : 16 -> 20
~ -[QLItem internalCopy] : 564 -> 576
~ -[QLItem encodeWithCoder:] : 1644 -> 1672
~ -[QLItem initWithCoder:] : 1352 -> 1400
~ -[QLItem createPreviewContext] : 576 -> 596
- -[QLItem setInternalShouldCreateTemporaryDirectoryInHost:]
+ -[QLItem setInternalShouldCreateTemporaryDirectoryInHost:]
- -[QLItem setSandboxingURLWrapper:]
+ -[QLItem setClientPreviewItemDisplayState:]
+ -[QLItem generatedItemContentType]
+ -[QLItem setGeneratedReplyType:]
~ -[QLItem(PreviewInfo) _uncachedPreviewItemTypeForContentType:] : 664 -> 780
~ -[QLPreviewContext isEqual:] : 972 -> 1000
~ -[QLPreviewContext encodeWithCoder:] : 976 -> 1004
~ -[QLPreviewContext initWithCoder:] : 840 -> 888
+ -[QLPreviewContext shouldPreventMachineReadableCodeDetection]
+ -[QLPreviewContext setEditedFileBehavior:]
CStrings:
+ "canEnterFullScreen"
```
