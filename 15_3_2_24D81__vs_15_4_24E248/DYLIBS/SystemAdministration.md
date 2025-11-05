## SystemAdministration

> `/System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration`

```diff

-948.2.2.0.0
-  __TEXT.__text: 0x23d64
+948.3.4.0.0
+  __TEXT.__text: 0x23fe4
   __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_methlist: 0x27f8
+  __TEXT.__objc_methlist: 0x2bec
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x4cee
   __TEXT.__oslogstring: 0x1ba7
-  __TEXT.__gcc_except_tab: 0x26c
-  __TEXT.__unwind_info: 0xb18
+  __TEXT.__gcc_except_tab: 0x270
+  __TEXT.__unwind_info: 0xb30
   __TEXT.__objc_classname: 0x436
   __TEXT.__objc_methname: 0x6d80
   __TEXT.__objc_methtype: 0x1438

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f38
+  __DATA_CONST.__objc_selrefs: 0x20a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x4d8
   __AUTH_CONST.__auth_got: 0x7c0
   __AUTH_CONST.__const: 0xa00
   __AUTH_CONST.__cfstring: 0x4460
-  __AUTH_CONST.__objc_const: 0x2e78
+  __AUTH_CONST.__objc_const: 0x26e8
   __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_dictobj: 0x5c8
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libcups.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libodfde.dylib
-  UUID: 3EBA3418-B0B8-3E3E-BA54-C6A9F9591BF9
-  Functions: 1056
-  Symbols:   2628
+  UUID: 3423694A-BD55-325D-8199-F73A239E7F72
+  Functions: 1073
+  Symbols:   2645
   CStrings:  2680
 
Symbols:
+ +[ADMDSNode closeDefaultLocalNode].cold.1
+ +[ADMDSNode openDefaultLocalNode].cold.1
+ +[ADMGroup adminGroup].cold.1
+ +[ADMGuestUserConfig syncGuestState].cold.1
+ +[ADMUser shouldHide500Users].cold.1
+ +[ADMUser(UserPrivate) _AOSFrameworkBundle].cold.1
+ +[ADMUser(UserPrivate) _PlatformSSOFrameworkBundle].cold.1
+ +[ADMUser(UserPrivate) _sharedPOLoginUser].cold.1
+ +[ADMUserAccountUtilities changePasswordForUser:oldPassword:newPassword:cdpCompletionHandler:].cold.1
+ +[ADMUserAccountUtilities changePasswordForUser:oldPassword:newPassword:cdpCompletionHandler:].cold.2
+ +[WriteConfigClient sharedClient].cold.1
+ -[ADMInternetServices _netFSServerFrameworkBundle].cold.1
+ -[ADMUser setInputSourcesImmediately:].cold.1
+ -[ADMUser(APFS) setSecureTokenAuthorizationEnabled:userPassword:authorizingUserName:authorizingUserPassword:].cold.1
+ -[ADMUser(APFS) setSecureTokenAuthorizationEnabled:userPassword:authorizingUserName:authorizingUserPassword:].cold.2
+ -[ADMUser(APFS) setSecureTokenAuthorizationEnabled:userPassword:authorizingUserName:authorizingUserPassword:].cold.3
+ coreTimeFrameworkBundle.cold.1
+ debugLoggingEnabled.cold.1
+ initBiometricKit.cold.1
+ initCKTouchIDGetPreference.cold.1
+ initLAContext.cold.1
+ isInternalBuild.cold.1
+ loadAppKit.cold.1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_9
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/ADMCredential.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/ADMSystem.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/AdminDirectoryService.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/AuthenticatedOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/DSAuthenticator.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/DSNode.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/DSRecord.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/Group.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/InternetServices.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/NVRAMConfig.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/RemoteUser.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/SFAuthorizationExtentions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/User.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/UserCSFDESupport.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/UserPrivate.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/UserUtilities.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/UserWC.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Admin/cXMLDataConvertor.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/ADMCredential.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/ADMSystem.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/AdminDirectoryService.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/AuthenticatedOperation.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/DSAuthenticator.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/DSNode.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/DSRecord.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/Group.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/InternetServices.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/NVRAMConfig.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/RemoteUser.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/SFAuthorizationExtentions.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/User.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/UserCSFDESupport.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/UserPrivate.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/UserUtilities.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/UserWC.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Admin/cXMLDataConvertor.m"

```
