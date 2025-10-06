## AccountsDaemon

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon`

```diff

-956.0.0.0.0
-  __TEXT.__text: 0x6674c
-  __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_methlist: 0x31e8
+962.2.0.0.0
+  __TEXT.__text: 0x66828
+  __TEXT.__auth_stubs: 0xc60
+  __TEXT.__objc_methlist: 0x31f8
   __TEXT.__const: 0x50
-  __TEXT.__oslogstring: 0x7f71
-  __TEXT.__cstring: 0x379b
+  __TEXT.__oslogstring: 0x7fa8
+  __TEXT.__cstring: 0x37ad
   __TEXT.__gcc_except_tab: 0x1eb8
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x16e4
+  __TEXT.__unwind_info: 0x16ec
   __TEXT.__objc_classname: 0x5f3
-  __TEXT.__objc_methname: 0xb003
+  __TEXT.__objc_methname: 0xb025
   __TEXT.__objc_methtype: 0x246c
-  __TEXT.__objc_stubs: 0x8ee0
+  __TEXT.__objc_stubs: 0x8f00
   __DATA_CONST.__got: 0x8e0
   __DATA_CONST.__const: 0x15b8
   __DATA_CONST.__objc_classlist: 0x198

   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x40b0
-  __DATA_CONST.__objc_selrefs: 0x2728
+  __DATA_CONST.__objc_selrefs: 0x2730
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x3b0
+  __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__objc_const: 0x1438
-  __AUTH_CONST.__cfstring: 0x31e0
+  __AUTH_CONST.__cfstring: 0x3200
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__auth_got: 0x638
+  __AUTH_CONST.__const: 0x460
+  __AUTH_CONST.__auth_got: 0x640
   __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x3b0
-  __DATA.__objc_superrefs: 0x120
   __DATA.__objc_ivar: 0x2a4
   __DATA.__data: 0x5c8
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__crash_info: 0x40
   __DATA_DIRTY.__bss: 0x168

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E437A9FC-3DE0-316D-8F50-04DB0735D09B
-  Functions: 1954
-  Symbols:   6624
-  CStrings:  3379
+  UUID: AA46D54D-551C-357C-80F7-38172CB2AA58
+  Functions: 1958
+  Symbols:   6637
+  CStrings:  3384
 
Symbols:
+ -[ACDServer _handleLanguageChangedDarwinNotification].cold.2
+ -[ACDServer _isHomePod]
+ GCC_except_table43
+ _MGGetSInt32Answer
+ ___23-[ACDServer _isHomePod]_block_invoke
+ ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.101
+ ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.114
+ ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.114.cold.1
+ ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.123
+ ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.123.cold.1
+ ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.97
+ ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.97.cold.1
+ ___block_literal_global.128
+ __isHomePod.onceToken
+ __isHomePod.result
+ _objc_msgSend$_isHomePod
- GCC_except_table39
- ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.100
- ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.112
- ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.112.cold.1
- ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.121
- ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.121.cold.1
- ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.95
- ___48-[ACDServer listener:shouldAcceptNewConnection:]_block_invoke.95.cold.1
CStrings:
+ "\"Language changed, but we're on homepod, not exiting.\""
+ "DeviceClassNumber"
+ "T@\"NSString\",?,R,C"
+ "_isHomePod"

```
