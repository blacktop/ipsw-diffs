## AppSSOCore

> `/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore`

```diff

-417.120.4.0.0
-  __TEXT.__text: 0x11f54
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x11fc
-  __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x17d7
+483.0.6.0.1
+  __TEXT.__text: 0x12990
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_methlist: 0x1224
+  __TEXT.__const: 0x120
+  __TEXT.__cstring: 0x18bb
   __TEXT.__oslogstring: 0x1849
-  __TEXT.__gcc_except_tab: 0x388
-  __TEXT.__unwind_info: 0x500
+  __TEXT.__gcc_except_tab: 0x3a0
+  __TEXT.__unwind_info: 0x518
   __TEXT.__objc_classname: 0x223
-  __TEXT.__objc_methname: 0x26e8
-  __TEXT.__objc_methtype: 0x7bd
-  __TEXT.__objc_stubs: 0x1b20
+  __TEXT.__objc_methname: 0x2830
+  __TEXT.__objc_methtype: 0x7ea
+  __TEXT.__objc_stubs: 0x1ba0
   __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x458
+  __DATA_CONST.__const: 0x548
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x980
+  __DATA_CONST.__objc_selrefs: 0x9a8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xf80
+  __AUTH_CONST.__cfstring: 0xfa0
   __AUTH_CONST.__objc_const: 0x2bf8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 928470B1-CF4D-3ABB-9507-65FBADEE06E3
-  Functions: 497
-  Symbols:   1815
-  CStrings:  981
+  UUID: EF9E5103-526C-3C6C-90CE-D94D5E525705
+  Functions: 511
+  Symbols:   1845
+  CStrings:  993
 
Symbols:
+ +[SOAuthorizationCore _canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:]
+ +[SOAuthorizationCore _doAKshouldProcessURL:completion:]
+ +[SOAuthorizationCore canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:]
+ -[SOConfigurationClient willHandleURL:responseCode:callerBundleIdentifier:completion:]
+ GCC_except_table12
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table46
+ GCC_except_table56
+ GCC_except_table60
+ GCC_except_table8
+ GCC_except_table9
+ _OUTLINED_FUNCTION_5
+ ___123+[SOAuthorizationCore canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:]_block_invoke
+ ___123+[SOAuthorizationCore canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:]_block_invoke_2
+ ___123+[SOAuthorizationCore canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:]_block_invoke_2.cold.1
+ ___124+[SOAuthorizationCore _canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:]_block_invoke
+ ___124+[SOAuthorizationCore _canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:]_block_invoke_2
+ ___124+[SOAuthorizationCore _canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:]_block_invoke_3
+ ___43-[SOAuthorizationCore _cancelAuthorization]_block_invoke.18
+ ___43-[SOAuthorizationCore _cancelAuthorization]_block_invoke.18.cold.1
+ ___43-[SOAuthorizationCore _cancelAuthorization]_block_invoke.18.cold.2
+ ___56+[SOAuthorizationCore _doAKshouldProcessURL:completion:]_block_invoke
+ ___56+[SOAuthorizationCore _doAKshouldProcessURL:completion:]_block_invoke.cold.1
+ ___65-[SOAuthorizationCore _finishAuthorization:withCredential:error:]_block_invoke.38
+ ___86-[SOConfigurationClient willHandleURL:responseCode:callerBundleIdentifier:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_56_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_literal_global.139
+ ___block_literal_global.32
+ _dispatch_get_global_queue
+ _objc_msgSend$_canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:
+ _objc_msgSend$_doAKshouldProcessURL:completion:
+ _objc_msgSend$shouldProcessURL:completion:
+ _objc_msgSend$willHandleURL:responseCode:callerBundleIdentifier:completion:
- GCC_except_table10
- GCC_except_table20
- GCC_except_table21
- GCC_except_table23
- GCC_except_table37
- GCC_except_table47
- GCC_except_table51
- ___43-[SOAuthorizationCore _cancelAuthorization]_block_invoke.16
- ___43-[SOAuthorizationCore _cancelAuthorization]_block_invoke.16.cold.1
- ___43-[SOAuthorizationCore _cancelAuthorization]_block_invoke.16.cold.2
- ___65-[SOAuthorizationCore _finishAuthorization:withCredential:error:]_block_invoke.37
- ___block_literal_global.134
- ___block_literal_global.30
CStrings:
+ "+[SOAuthorizationCore _doAKshouldProcessURL:completion:]_block_invoke"
+ "+[SOAuthorizationCore canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:]_block_invoke_2"
+ "AccessKey"
+ "_canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:"
+ "_doAKshouldProcessURL:completion:"
+ "canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:"
+ "shouldProcessURL:completion:"
+ "v12@?0B8"
+ "v48@0:8@16q24@32@?40"
+ "v52@0:8@16q24@32B40@?44"
+ "willHandleURL:responseCode:callerBundleIdentifier:completion:"

```
