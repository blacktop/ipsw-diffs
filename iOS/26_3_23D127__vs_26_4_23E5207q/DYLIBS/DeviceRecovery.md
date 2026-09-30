## DeviceRecovery

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery`

```diff

-103.80.1.0.1
-  __TEXT.__text: 0x1fdac
-  __TEXT.__auth_stubs: 0x640
+107.100.11.0.0
+  __TEXT.__text: 0x1d768
+  __TEXT.__auth_stubs: 0x5f0
   __TEXT.__objc_methlist: 0x5e8
   __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__cstring: 0x3c07
+  __TEXT.__gcc_except_tab: 0x2b8
+  __TEXT.__cstring: 0x3eab
   __TEXT.__oslogstring: 0xe90
-  __TEXT.__unwind_info: 0x5c0
+  __TEXT.__unwind_info: 0x5e0
   __TEXT.__objc_classname: 0xa2
   __TEXT.__objc_methname: 0x1074
   __TEXT.__objc_methtype: 0x2d5

   __DATA_CONST.__objc_selrefs: 0x488
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__auth_got: 0x308
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0xea0
   __AUTH_CONST.__objc_const: 0x788

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FFC36502-B0AD-3D2D-94A8-7E1359BB51A1
-  Functions: 748
-  Symbols:   1677
-  CStrings:  841
+  UUID: 5C198283-0D53-385D-B926-C526CF5355AF
+  Functions: 837
+  Symbols:   1883
+  CStrings:  842
 
Symbols:
+ -[DeviceRecoveryOverrideClient init].cold.3
+ _ACMContextCredentialGetPropertyEx
+ _LibCall_ACMSecContextCopyCredentialsArrayEx
+ _LibCall_ACMSecCredentialsArrayDelete
+ _LibSer_ContextCredentialGetPropertyEx_Deserialize
+ _LibSer_ContextCredentialGetPropertyEx_GetSize
+ _LibSer_ContextCredentialGetPropertyEx_Serialize
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _objc_retainAutoreleasedReturnValue
- GCC_except_table44
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x25
- _objc_retain_x8
CStrings:
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "/Library/Caches/com.apple.xbs/B00B08DE-3C06-4FE4-B2FF-E260184E7410/TemporaryDirectory.PXiZc7/Sources/DeviceRecovery/Common/DeviceRecoveryEnvironmentWorker.m"
+ "/Library/Caches/com.apple.xbs/B00B08DE-3C06-4FE4-B2FF-E260184E7410/TemporaryDirectory.PXiZc7/Sources/DeviceRecovery/Common/DeviceRecoveryHelpers.m"
+ "/Library/Caches/com.apple.xbs/B00B08DE-3C06-4FE4-B2FF-E260184E7410/TemporaryDirectory.PXiZc7/Sources/DeviceRecovery/Common/DeviceRecoveryOverrides.m"
+ "/Library/Caches/com.apple.xbs/B00B08DE-3C06-4FE4-B2FF-E260184E7410/TemporaryDirectory.PXiZc7/Sources/DeviceRecovery/DeviceRecovery_Framework/DeviceRecoveryController.m"
+ "/Library/Caches/com.apple.xbs/B00B08DE-3C06-4FE4-B2FF-E260184E7410/TemporaryDirectory.PXiZc7/Sources/DeviceRecovery/DeviceRecovery_Framework/DeviceRecoveryOverrideClient.m"
+ "ACMContextCredentialGetPropertyEx"
+ "LibCall_ACMSecContextCopyCredentialsArrayEx"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryEnvironmentWorker.m"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryHelpers.m"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryOverrides.m"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/DeviceRecovery_Framework/DeviceRecoveryController.m"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/DeviceRecovery_Framework/DeviceRecoveryOverrideClient.m"
- "ACMContextCredentialGetProperty"

```
