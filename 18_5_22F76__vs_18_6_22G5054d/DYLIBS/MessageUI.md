## MessageUI

> `/System/Library/Frameworks/MessageUI.framework/MessageUI`

```diff

-3826.600.51.2.1
-  __TEXT.__text: 0x10cac0
+3826.700.51.0.0
+  __TEXT.__text: 0x10cc7c
   __TEXT.__auth_stubs: 0x1f20
   __TEXT.__objc_methlist: 0x11e64
-  __TEXT.__gcc_except_tab: 0x2461c
+  __TEXT.__gcc_except_tab: 0x24654
   __TEXT.__cstring: 0x9008
-  __TEXT.__const: 0x914
-  __TEXT.__oslogstring: 0x51a3
+  __TEXT.__const: 0x934
+  __TEXT.__oslogstring: 0x5223
   __TEXT.__ustring: 0x4d2
   __TEXT.__swift5_typeref: 0x328
   __TEXT.__swift5_reflstr: 0xdd

   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x99a8
+  __TEXT.__unwind_info: 0x99b8
   __TEXT.__eh_frame: 0x1d8
   __TEXT.__objc_classname: 0x20da
-  __TEXT.__objc_methname: 0x3387a
+  __TEXT.__objc_methname: 0x33892
   __TEXT.__objc_methtype: 0xb08c
-  __TEXT.__objc_stubs: 0x22bc0
+  __TEXT.__objc_stubs: 0x22c00
   __DATA_CONST.__got: 0x1ab8
   __DATA_CONST.__const: 0x4618
   __DATA_CONST.__objc_classlist: 0x5e8
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x3c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbb90
+  __DATA_CONST.__objc_selrefs: 0xbba0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x4a0
   __DATA_CONST.__objc_arraydata: 0x608

   __AUTH.__objc_data: 0x2aa0
   __AUTH.__data: 0x1c0
   __DATA.__objc_ivar: 0x10c8
-  __DATA.__data: 0x2f88
+  __DATA.__data: 0x2f68
   __DATA.__bss: 0x7f8
   __DATA.__common: 0x2f8
   __DATA_DIRTY.__objc_data: 0x12e0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 567F55C7-7992-3D8B-AB96-3769E3B71E56
-  Functions: 5827
-  Symbols:   23688
-  CStrings:  12210
+  UUID: E8C41793-65D1-3EC2-A7DE-C7A30FA6C2D6
+  Functions: 5828
+  Symbols:   23693
+  CStrings:  12213
 
Symbols:
+ -[MFMailComposeView scrollViewDidScroll:].cold.1
+ _objc_msgSend$isMainFrame
+ _objc_msgSend$targetFrame
Functions:
~ -[MFComposeWebView webView:decidePolicyForNavigationAction:decisionHandler:] : 20 -> 456
~ -[MFMailComposeView scrollViewDidScroll:] : 556 -> 444
+ -[MFMailComposeView scrollViewDidScroll:].cold.1
CStrings:
+ "<%{public}@: %p>: Blocking navigation action for request whose target frame is not the main frame (iframe, probably): %@"
+ "Scroll view could not scroll: %@"
+ "isMainFrame"
+ "targetFrame"
- "Scroll view did scroll: %@"

```
