## ProxCardKit

> `/System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-2131.10.1.2.11
-  __TEXT.__text: 0x1d74c
-  __TEXT.__objc_methlist: 0x2dd8
+2131.20.65.2.1
+  __TEXT.__text: 0x1d9b0
+  __TEXT.__objc_methlist: 0x2df0
   __TEXT.__const: 0x230
   __TEXT.__cstring: 0x74d
   __TEXT.__gcc_except_tab: 0xe8
   __TEXT.__oslogstring: 0x212
   __TEXT.__dlopen_cstrs: 0x151
-  __TEXT.__unwind_info: 0x990
+  __TEXT.__unwind_info: 0x9a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fe0
+  __DATA_CONST.__objc_selrefs: 0x2008
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__got: 0x400
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x5c0
-  __AUTH_CONST.__objc_const: 0x8f50
+  __AUTH_CONST.__objc_const: 0x8f70
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_ivar: 0x390
+  __DATA.__objc_ivar: 0x394
   __DATA.__data: 0x968
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 725
-  Symbols:   2412
+  Functions: 728
+  Symbols:   2421
   CStrings:  94
 
Symbols:
+ -[PRXCardContainerView deactivateKeyboardSpecificConstraintsIfNeeded]
+ -[PRXCardContainerViewController _updateContainerPreferredContentSizeForContainerSize:]
+ -[PRXCardContentView layoutSubviews]
+ _OBJC_CLASS_$_UIViewLayoutRegion
+ _OBJC_IVAR_$_PRXCardContainerView._contentMaxHeight
+ _objc_msgSend$_layoutRegionForBarOnDirectionalEdge:extent:
+ _objc_msgSend$_updateContainerPreferredContentSizeForContainerSize:
+ _objc_msgSend$deactivateKeyboardSpecificConstraintsIfNeeded
+ _objc_msgSend$directionalEdgeInsetsForLayoutRegion:
+ _objc_msgSend$hitTest:withEvent:
+ _objc_msgSend$layoutFrame
- _CGRectContainsPoint
- _objc_msgSend$convertRect:toView:
Functions:
~ -[PRXCardContainerViewController viewWillTransitionToSize:withTransitionCoordinator:] : 212 -> 220
~ -[PRXCardContainerViewController traitCollectionDidChange:] : 252 -> 336
~ -[PRXCardContainerViewController _updateContainerPreferredContentSize] : 204 -> 68
+ -[PRXCardContainerViewController _updateContainerPreferredContentSizeForContainerSize:]
~ -[PRXCardContainerViewController navigationController:willShowViewController:animated:] : 404 -> 412
+ -[PRXCardContentView layoutSubviews]
~ -[PRXCardContainerView initWithFrame:containerLayoutMargins:] : 2912 -> 2932
~ -[PRXCardContainerView setPreferredContentSize:] : 184 -> 204
~ -[PRXCardContainerView _updateKeyboardDeferred:] : 544 -> 744
+ -[PRXCardContainerView deactivateKeyboardSpecificConstraintsIfNeeded]
~ -[PRXCardContainerView gestureRecognizerShouldBegin:] : 276 -> 268
CStrings:
+ "\xf0\xe1"
- "\xf0\xd1"
```
