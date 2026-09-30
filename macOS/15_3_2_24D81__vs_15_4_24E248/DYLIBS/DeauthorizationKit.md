## DeauthorizationKit

> `/System/Library/PrivateFrameworks/DeauthorizationKit.framework/Versions/A/DeauthorizationKit`

```diff

 81.0.0.0.0
-  __TEXT.__text: 0x2f768
+  __TEXT.__text: 0x2ed04
   __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_methlist: 0x1c6c
+  __TEXT.__objc_methlist: 0x1e54
   __TEXT.__const: 0xc9
   __TEXT.__cstring: 0x2e79
   __TEXT.__gcc_except_tab: 0x6bc
   __TEXT.__oslogstring: 0x2144
-  __TEXT.__unwind_info: 0xad8
+  __TEXT.__unwind_info: 0xae8
   __TEXT.__objc_classname: 0x44e
   __TEXT.__objc_methname: 0x4bbe
   __TEXT.__objc_methtype: 0xb1c

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13d8
+  __DATA_CONST.__objc_selrefs: 0x1478
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x4b8
   __AUTH_CONST.__const: 0x9a0
   __AUTH_CONST.__cfstring: 0x1b20
-  __AUTH_CONST.__objc_const: 0x3620
+  __AUTH_CONST.__objc_const: 0x32a8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0xb90

   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D329914D-2B71-31DF-980D-DF84B6FF33DE
-  Functions: 1014
-  Symbols:   2367
+  UUID: 4C857A65-AACF-3A35-832E-3D6071B59039
+  Functions: 1125
+  Symbols:   2479
   CStrings:  1850
 
Symbols:
+ +[DKAppLaunchUtilities sharedInstance].cold.1
+ +[DKAuthContextManager sharedInstance].cold.1
+ +[DKDiskManagementUtilities sharedManager].cold.1
+ +[DKEraseAllContentAndSettingsManager sharedManager].cold.1
+ +[DKHelperDaemon sharedInstance].cold.1
+ +[DKHelperDaemonController sharedInstance].cold.1
+ +[DKPrefs sharedInstance].cold.1
+ ACMContextGetExternalForm.cold.1
+ DKLogObject.cold.1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __53-[DKHelperDaemon listener:shouldAcceptNewConnection:]_block_invoke.143
+ __53-[DKHelperDaemon listener:shouldAcceptNewConnection:]_block_invoke.143.cold.1
+ __65-[DKHelperDaemon removeApplePayWithUsername:password:completion:]_block_invoke.99
+ updateLogLevelFromKext.cold.1
- GCC_except_table20
- __53-[DKHelperDaemon listener:shouldAcceptNewConnection:]_block_invoke.137
- __53-[DKHelperDaemon listener:shouldAcceptNewConnection:]_block_invoke.137.cold.1
- __65-[DKHelperDaemon removeApplePayWithUsername:password:completion:]_block_invoke.93
- __isNullOrEqualMem2
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"

```
