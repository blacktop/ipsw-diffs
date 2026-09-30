## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions`

```diff

-73.0.0.0.2
-  __TEXT.__text: 0x104f0
+75.0.0.0.0
+  __TEXT.__text: 0x10480
   __TEXT.__objc_methlist: 0xfe0
-  __TEXT.__const: 0x5b0
+  __TEXT.__const: 0x5c0
   __TEXT.__cstring: 0x180c
   __TEXT.__gcc_except_tab: 0x250
-  __TEXT.__oslogstring: 0x7f3
+  __TEXT.__oslogstring: 0x803
   __TEXT.__ustring: 0x1bc
   __TEXT.__swift5_typeref: 0x102
   __TEXT.__constg_swiftt: 0x220

   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xae0
+  __DATA_CONST.__objc_selrefs: 0xad8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x78

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 461
-  Symbols:   1467
+  Symbols:   1466
   CStrings:  301
 
Symbols:
+ +[WCRBrowserEngineClient _askToBrowsePopoverSourceRectForBounds:safeAreaInsets:]
+ _objc_msgSend$_askToBrowsePopoverSourceRectForBounds:safeAreaInsets:
- +[WCRBrowserEngineClient _askToBrowsePopoverSourceRectForBounds:safeAreaInsets:isPad:]
- _objc_msgSend$_askToBrowsePopoverSourceRectForBounds:safeAreaInsets:isPad:
- _objc_msgSend$traitCollection
Functions:
~ +[WCRBrowserEngineClient _askToBrowsePopoverSourceRectForBounds:safeAreaInsets:isPad:] -> +[WCRBrowserEngineClient _askToBrowsePopoverSourceRectForBounds:safeAreaInsets:] : 176 -> 212
~ ___113-[WCRBrowserEngineClient _presentAskToBrowseMenuForURL:state:presentingView:presentingViewController:completion:]_block_invoke : 1012 -> 940
~ -[WCRPopoverPresentationControllerDelegate popoverPresentationController:willRepositionPopoverToRect:inView:] : 224 -> 148
CStrings:
+ "overridePolicy from DC unrecognized: %{public}s"
+ "overridePolicy from DC: %{public}s"
- "overridePolicy from DC unrecognized: %s"
- "overridePolicy from DC: %s"
```
