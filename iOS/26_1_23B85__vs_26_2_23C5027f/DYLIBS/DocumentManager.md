## DocumentManager

> `/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager`

```diff

-367.1.9.0.0
-  __TEXT.__text: 0x35500
+367.2.3.0.0
+  __TEXT.__text: 0x35640
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x2e04
+  __TEXT.__objc_methlist: 0x2e1c
   __TEXT.__const: 0x180
-  __TEXT.__cstring: 0x4c45
+  __TEXT.__cstring: 0x4bec
   __TEXT.__ustring: 0x6a2
-  __TEXT.__oslogstring: 0x3176
+  __TEXT.__oslogstring: 0x31e7
   __TEXT.__gcc_except_tab: 0xa74
   __TEXT.__unwind_info: 0xdc8
   __TEXT.__objc_classname: 0x787
-  __TEXT.__objc_methname: 0xace0
+  __TEXT.__objc_methname: 0xacf9
   __TEXT.__objc_methtype: 0x16b6
-  __TEXT.__objc_stubs: 0x7cc0
+  __TEXT.__objc_stubs: 0x7ce0
   __DATA_CONST.__got: 0x638
-  __DATA_CONST.__const: 0x1718
+  __DATA_CONST.__const: 0x1708
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a38
+  __DATA_CONST.__objc_selrefs: 0x2a40
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x4140
-  __AUTH_CONST.__objc_const: 0x45a8
+  __AUTH_CONST.__cfstring: 0x4100
+  __AUTH_CONST.__objc_const: 0x45b0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x8c0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 95ACA1FD-DA46-3B13-8138-2D9CF91DA8C3
-  Functions: 1244
-  Symbols:   4794
-  CStrings:  3295
+  UUID: 4CEC706F-98CE-30DA-910D-B65FAA673AF4
+  Functions: 1245
+  Symbols:   4795
+  CStrings:  3294
 
Symbols:
+ -[UIDocumentBrowserViewController _shareActionWasCancelled]
+ GCC_except_table225
+ GCC_except_table228
+ GCC_except_table322
+ ___block_literal_global.755
+ _objc_msgSend$_shareActionWasCancelled
- GCC_except_table224
- GCC_except_table227
- GCC_except_table321
- _DOCUserDefaultsKeyUseDSEnumForExternalVolumes
- _DOCUserDefaultsKeyUseDSEnumForLocalStorage
- ___block_literal_global.754
Functions:
~ -[UIDocumentBrowserViewController dismissAllPresentedViewControllers:completion:] : 196 -> 204
~ ___146-[UIDocumentBrowserViewController _displayActivityControllerWithItemBookmarks:popoverTracker:isContentManaged:additionalActivities:activityProxy:]_block_invoke_3 : 304 -> 420
+ -[UIDocumentBrowserViewController _shareActionWasCancelled]
CStrings:
+ "Not presenting activity view controller - cancelled before presentation"
+ "Share action cancelled from service side"
+ "_shareActionWasCancelled"
- "DOCUserDefaultsKeyUseDSEnumForExternalVolumes"
- "DOCUserDefaultsKeyUseDSEnumForLocalStorage"

```
