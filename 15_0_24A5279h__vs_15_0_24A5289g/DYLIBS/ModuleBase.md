## ModuleBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/Versions/A/ModuleBase`

```diff

-1656.0.58.0.1
-  __TEXT.__text: 0x735c
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x68c
-  __TEXT.__const: 0xf0
+1656.0.75.0.0
+  __TEXT.__text: 0x74bc
+  __TEXT.__auth_stubs: 0x310
+  __TEXT.__objc_methlist: 0x6c4
+  __TEXT.__const: 0xe8
   __TEXT.__cstring: 0x8df
   __TEXT.__ustring: 0xc
-  __TEXT.__gcc_except_tab: 0x14
+  __TEXT.__gcc_except_tab: 0x68
   __TEXT.__oslogstring: 0x623
-  __TEXT.__unwind_info: 0x208
+  __TEXT.__unwind_info: 0x228
   __TEXT.__objc_classname: 0x155
-  __TEXT.__objc_methname: 0x1c87
-  __TEXT.__objc_methtype: 0xc62
-  __TEXT.__objc_stubs: 0x1320
+  __TEXT.__objc_methname: 0x1d10
+  __TEXT.__objc_methtype: 0xc6b
+  __TEXT.__objc_stubs: 0x1380
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x670
+  __DATA_CONST.__objc_selrefs: 0x698
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x190
+  __AUTH_CONST.__auth_got: 0x198
   __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__cfstring: 0x940
-  __AUTH_CONST.__objc_const: 0x1870
+  __AUTH_CONST.__objc_const: 0x1880
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0xc4

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/Versions/A/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 180
-  Symbols:   611
+  Functions: 185
+  Symbols:   622
   CStrings:  93
 
Symbols:
+ -[AuthenticationManager _agentProxy]
+ -[AuthenticationManager _clearAuthentication:]
+ -[AuthenticationManager _handleCompletionOfAuthentication:]
+ -[AuthenticationManager _handleCompletionOfAuthentication:].cold.1
+ -[AuthenticationManager completionHandler]
+ -[AuthenticationManager setCompletionHandler:]
+ GCC_except_table19
+ GCC_except_table23
+ __113-[AuthenticationManager authenticateForPolicy:constraintData:internalInfo:uiDelegate:originator:mechanism:reply:]_block_invoke.28
+ __78-[AuthenticationManager remoteAuthenticationInProgressWithPriority:pid:reply:]_block_invoke.48
+ ___59-[AuthenticationManager _handleCompletionOfAuthentication:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e5_v8?0l
+ ___copy_helper_block_e8_32s40w
+ __block_literal_global.110
+ _objc_msgSend$_agentProxy
+ _objc_msgSend$_clearAuthentication:
+ _objc_msgSend$_handleCompletionOfAuthentication:
+ _objc_setProperty_nonatomic_copy
- __113-[AuthenticationManager authenticateForPolicy:constraintData:internalInfo:uiDelegate:originator:mechanism:reply:]_block_invoke.29
- __44-[AuthenticationManager _runAuthentication:]_block_invoke.31
- __44-[AuthenticationManager _runAuthentication:]_block_invoke.cold.1
- __78-[AuthenticationManager remoteAuthenticationInProgressWithPriority:pid:reply:]_block_invoke.50
- ___block_descriptor_48_e8_32s40s_e5_v8?0l
- ___copy_helper_block_e8_32s40s
- __block_literal_global.104

```
