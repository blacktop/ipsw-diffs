## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-1394.100.151.0.1
-  __TEXT.__text: 0x2fca4
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x2a4c
-  __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x860
-  __TEXT.__cstring: 0x1944
+1394.120.27.0.0
+  __TEXT.__text: 0x301fc
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x2ab4
+  __TEXT.__const: 0xe8
+  __TEXT.__gcc_except_tab: 0x870
+  __TEXT.__cstring: 0x19bd
   __TEXT.__dlopen_cstrs: 0x1cd
-  __TEXT.__oslogstring: 0x2333
-  __TEXT.__unwind_info: 0xfdc
+  __TEXT.__oslogstring: 0x23a1
+  __TEXT.__unwind_info: 0x1000
   __TEXT.__objc_classname: 0x912
-  __TEXT.__objc_methname: 0x60c1
+  __TEXT.__objc_methname: 0x620a
   __TEXT.__objc_methtype: 0x1af1
-  __TEXT.__objc_stubs: 0x3fe0
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x19f8
+  __TEXT.__objc_stubs: 0x4040
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0x1a90
   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6840
-  __DATA_CONST.__objc_selrefs: 0x17a0
+  __DATA_CONST.__objc_const: 0x6870
+  __DATA_CONST.__objc_selrefs: 0x17e8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_classrefs: 0x2e0
   __DATA_CONST.__objc_superrefs: 0x1a8
   __AUTH_CONST.__objc_intobj: 0x228
-  __AUTH_CONST.__cfstring: 0x1840
-  __AUTH_CONST.__objc_const: 0x558
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__auth_got: 0x460
+  __AUTH_CONST.__cfstring: 0x1880
+  __AUTH_CONST.__objc_const: 0x3a8
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__auth_got: 0x468
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x250
-  __DATA.__data: 0xa98
-  __DATA.__bss: 0x178
-  __DATA_DIRTY.__const: 0x260
-  __DATA_DIRTY.__objc_const: 0x13f8
+  __DATA.__objc_ivar: 0x254
+  __DATA.__data: 0xaa0
+  __DATA.__bss: 0x170
+  __DATA_DIRTY.__const: 0x280
+  __DATA_DIRTY.__objc_const: 0x15a8
   __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 91763A2A-30CD-38D1-A84F-2AECCDA227F0
-  Functions: 1288
-  Symbols:   4569
-  CStrings:  2059
+  UUID: A8996B4E-2A6F-3AF0-BBDC-F48638FEC486
+  Functions: 1301
+  Symbols:   4605
+  CStrings:  2076
 
Symbols:
+ -[LAClient _synchronousRemoteObjectProxy:performCall:].cold.1
+ -[LAClient externalizedContext].cold.1
+ -[LAClient setWillRetryOnInterruptedConnection:]
+ -[LAClient willRetryOnInterruptedConnection]
+ -[LAContext optionAllowEnablementGracePeriod]
+ -[LAContext optionNoGracePeriodUI]
+ -[LAContext setOptionAllowEnablementGracePeriod:]
+ -[LAContext setOptionNoGracePeriodUI:]
+ -[LAStorage numberForKey:]
+ -[LAStorage numberForKey:completionHandler:]
+ -[LAStorage numberForKey:error:]
+ GCC_except_table102
+ GCC_except_table34
+ GCC_except_table40
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table54
+ GCC_except_table94
+ GCC_except_table98
+ _LACPolicyOptionAllowEnablementGracePeriod
+ _LACPolicyOptionNoGracePeriodUI
+ _LARatchetMaxEnablementGracePeriod
+ _OBJC_IVAR_$_LAClient._willRetryOnInterruptedConnection
+ ___32-[LAStorage numberForKey:error:]_block_invoke
+ ___54-[LAClient _synchronousRemoteObjectProxy:performCall:]_block_invoke.92
+ ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.130
+ ___70-[LAClient _checkIdResultForTCC:synchronous:error:retryBlock:finally:]_block_invoke.106
+ ___block_descriptor_48_e8_32r40r_e30_v24?0"NSNumber"8"NSError"16lr32l8r40l8
+ ___block_descriptor_57_e8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
+ ___block_literal_global.232
+ _objc_msgSend$numberForKey:completionHandler:
+ _objc_msgSend$numberForKey:error:
+ _objc_msgSend$setWillRetryOnInterruptedConnection:
+ _objc_msgSend$willRetryOnInterruptedConnection
+ _usleep
- GCC_except_table101
- GCC_except_table47
- GCC_except_table93
- GCC_except_table97
- ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.124
- ___70-[LAClient _checkIdResultForTCC:synchronous:error:retryBlock:finally:]_block_invoke.105
- ___block_descriptor_49_e8_32s40w_e5_v8?0ls32l8w40l8
- ___block_literal_global.223
- _objc_msgSend$setCachedExternalizedContext:
CStrings:
+ "%{public}@ connection to server interrupted (recovery: %d, willRetry: %d)"
+ "Retrying on an interrupted XPC connection"
+ "Retrying on cachedExternalizedContext"
+ "TB,V_willRetryOnInterruptedConnection"
+ "_willRetryOnInterruptedConnection"
+ "com.apple.private.LocalAuthentication.Storage.BiometricSuccessAge"
+ "com.apple.private.LocalAuthentication.Storage.Preboard"
+ "numberForKey:"
+ "numberForKey:completionHandler:"
+ "numberForKey:error:"
+ "optionAllowEnablementGracePeriod"
+ "optionNoGracePeriodUI"
+ "setOptionAllowEnablementGracePeriod:"
+ "setOptionNoGracePeriodUI:"
+ "setWillRetryOnInterruptedConnection:"
+ "willRetryOnInterruptedConnection"
- "%{public}@ connection to server interrupted"

```
