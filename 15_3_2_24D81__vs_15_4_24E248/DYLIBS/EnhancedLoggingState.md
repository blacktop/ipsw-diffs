## EnhancedLoggingState

> `/System/Library/PrivateFrameworks/EnhancedLoggingState.framework/Versions/A/EnhancedLoggingState`

```diff

 70.0.0.0.0
-  __TEXT.__text: 0x91d0
+  __TEXT.__text: 0x91c4
   __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_methlist: 0x91c
+  __TEXT.__objc_methlist: 0xb34
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x150e
   __TEXT.__oslogstring: 0x3c7
   __TEXT.__gcc_except_tab: 0xcc
   __TEXT.__dlopen_cstrs: 0x72
-  __TEXT.__unwind_info: 0x210
+  __TEXT.__unwind_info: 0x228
   __TEXT.__objc_classname: 0xfb
-  __TEXT.__objc_methname: 0x1f06
-  __TEXT.__objc_methtype: 0x599
+  __TEXT.__objc_methname: 0x1f52
+  __TEXT.__objc_methtype: 0x5eb
   __TEXT.__objc_stubs: 0x1800
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x780
+  __DATA_CONST.__objc_selrefs: 0x888
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x168
   __AUTH_CONST.__const: 0x270
   __AUTH_CONST.__cfstring: 0x1be0
-  __AUTH_CONST.__objc_const: 0x1530
+  __AUTH_CONST.__objc_const: 0x1178
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0xa8
   __DATA.__data: 0x1e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BB7FA1A4-3ABA-3DC2-A52F-F71FCEC90905
-  Functions: 217
-  Symbols:   761
-  CStrings:  935
+  UUID: 557B8471-801C-3C97-A0A6-C35E8E50A57C
+  Functions: 225
+  Symbols:   769
+  CStrings:  938
 
Symbols:
+ +[ELSDefaults sharedInstance].cold.1
+ +[ELSDocumentHelper sharedHelper].cold.1
+ +[ELSEnvironment sharedInstance].cold.1
+ +[ELSEvent createLoggingEventWith:postfix:].cold.2
+ +[ELSManager sharedManager].cold.1
+ +[ELSWhitelist whitelist].cold.1
+ -[ELSSnapshot init].cold.1
+ ELSLogHandleForCategory.cold.1
CStrings:
+ "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
+ "v44@0:8@16@24B32@?36"
+ "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"

```
