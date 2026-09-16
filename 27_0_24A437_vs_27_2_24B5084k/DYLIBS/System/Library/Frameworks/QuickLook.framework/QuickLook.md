## QuickLook

> `/System/Library/Frameworks/QuickLook.framework/QuickLook`

```diff

-1034.0.0.0.0
-  __TEXT.__text: 0xd564c
+1034.1.3.0.0
+  __TEXT.__text: 0xd57ec
   __TEXT.__delay_helper: 0x948
   __TEXT.__objc_methlist: 0xb894
   __TEXT.__const: 0x3b94
-  __TEXT.__gcc_except_tab: 0x1758
+  __TEXT.__gcc_except_tab: 0x175c
   __TEXT.__cstring: 0x5354
-  __TEXT.__oslogstring: 0x56d7
+  __TEXT.__oslogstring: 0x57d7
   __TEXT.__ustring: 0x1c
   __TEXT.__swift5_typeref: 0x1d4a
   __TEXT.__swift5_reflstr: 0x9a7

   __TEXT.__swift_as_cont: 0x4ec
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5630
+  __TEXT.__unwind_info: 0x5628
   __TEXT.__eh_frame: 0x49ac
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x98
   __DATA_CONST.__got: 0xfe8
-  __AUTH_CONST.__const: 0x3958
+  __AUTH_CONST.__const: 0x3938
   __AUTH_CONST.__cfstring: 0x3360
   __AUTH_CONST.__objc_const: 0x11bb0
   __AUTH_CONST.__objc_intobj: 0x228

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 5745
-  Symbols:   10439
-  CStrings:  904
+  Symbols:   10438
+  CStrings:  906
 
Symbols:
- ___75-[QLPageViewController _setCurrentPageIndex:direction:animated:completion:]_block_invoke_3
Functions:
~ -[QLPreviewController _refreshCurrentPreviewItemAnimated:] : 100 -> 284
~ -[QLItemAggregatedViewController showPreviewViewController:animatingWithCrossfade:] : 1696 -> 1672
~ -[QLPageViewController _setCurrentPageIndex:direction:animated:completion:] : 608 -> 824
~ ___75-[QLPageViewController _setCurrentPageIndex:direction:animated:completion:]_block_invoke_3 -> ___75-[QLPageViewController _setCurrentPageIndex:direction:animated:completion:]_block_invoke.18 : 4 -> 44
CStrings:
+ "Data source returned no view controller for index %lu (current page index %ld). Showing an empty placeholder. #PreviewCollection"
+ "Not refreshing the current preview item at index %ld because the preview collection still needs to be configured. #PreviewController"
```
