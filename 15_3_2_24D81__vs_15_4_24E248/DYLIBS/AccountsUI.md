## AccountsUI

> `/System/Library/PrivateFrameworks/AccountsUI.framework/Versions/A/AccountsUI`

```diff

 150.0.0.0.0
-  __TEXT.__text: 0x21a78
+  __TEXT.__text: 0x219dc
   __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x1c84
+  __TEXT.__objc_methlist: 0x22a8
   __TEXT.__const: 0x98
   __TEXT.__cstring: 0x33b4
   __TEXT.__gcc_except_tab: 0x130
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x6b0
+  __TEXT.__unwind_info: 0x6b8
   __TEXT.__objc_classname: 0x34b
-  __TEXT.__objc_methname: 0x65f2
-  __TEXT.__objc_methtype: 0x159f
+  __TEXT.__objc_methname: 0x663e
+  __TEXT.__objc_methtype: 0x15f1
   __TEXT.__objc_stubs: 0x5400
   __DATA_CONST.__got: 0x4d0
   __DATA_CONST.__const: 0x198

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1970
+  __DATA_CONST.__objc_selrefs: 0x1c28
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x290
   __AUTH_CONST.__const: 0xb50
   __AUTH_CONST.__cfstring: 0x2800
-  __AUTH_CONST.__objc_const: 0x5be8
+  __AUTH_CONST.__objc_const: 0x5078
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __DATA.__objc_ivar: 0x220

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D8FECC8F-ABAC-33CC-90C0-EDFAD6ADDD32
-  Functions: 723
-  Symbols:   2167
-  CStrings:  2086
+  UUID: 95707910-12A6-376F-9FF0-4056E815EC2C
+  Functions: 730
+  Symbols:   2175
+  CStrings:  2089
 
Symbols:
+ +[ACAccountType(AccountsUI) accountTypeForHostname:].cold.1
+ +[ACUIAccountNotifier sharedNotifier].cold.1
+ +[ACUIPluginManager sharedManager].cold.1
+ +[ACUIUtilities appPathForDataclassIdentifier:].cold.1
+ +[ACUIUtilities shouldUseChineseAccountTypes].cold.1
+ -[ACAccountType(AccountsUI) _imageWithSuffix:].cold.1
+ ACUILog.cold.2
+ initSPSafariPlatformSupport.cold.1
CStrings:
+ "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
+ "v44@0:8@16@24B32@?36"
+ "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"

```
