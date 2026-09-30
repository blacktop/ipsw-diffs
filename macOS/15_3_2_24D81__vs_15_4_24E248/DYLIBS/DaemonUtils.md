## DaemonUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/Versions/A/DaemonUtils`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x36520
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x1b44
-  __TEXT.__const: 0x170
-  __TEXT.__cstring: 0x5023
-  __TEXT.__oslogstring: 0x1c05
-  __TEXT.__gcc_except_tab: 0xcd0
-  __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0xa30
-  __TEXT.__objc_classname: 0x3d9
-  __TEXT.__objc_methname: 0x446a
-  __TEXT.__objc_methtype: 0xa2f
-  __TEXT.__objc_stubs: 0x3f00
-  __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0x1d8
+1656.100.223.0.0
+  __TEXT.__text: 0x365f4
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_methlist: 0x1e44
+  __TEXT.__const: 0x178
+  __TEXT.__cstring: 0x5007
+  __TEXT.__oslogstring: 0x1b33
+  __TEXT.__gcc_except_tab: 0xe50
+  __TEXT.__dlopen_cstrs: 0xaa
+  __TEXT.__unwind_info: 0xc70
+  __TEXT.__objc_classname: 0x3db
+  __TEXT.__objc_methname: 0x434e
+  __TEXT.__objc_methtype: 0xa7a
+  __TEXT.__objc_stubs: 0x3d80
+  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__const: 0x1f0
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1308
+  __DATA_CONST.__objc_selrefs: 0x1330
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x468
-  __AUTH_CONST.__const: 0x8b0
-  __AUTH_CONST.__cfstring: 0x1b00
-  __AUTH_CONST.__objc_const: 0x43b0
+  __AUTH_CONST.__auth_got: 0x438
+  __AUTH_CONST.__const: 0x890
+  __AUTH_CONST.__cfstring: 0x1a40
+  __AUTH_CONST.__objc_const: 0x3ed0
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/Versions/A/LocalAuthenticationCore
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
-  - /System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA1B4102-38CC-30C1-B4C5-DBF98ED2B620
-  Functions: 1129
-  Symbols:   2540
-  CStrings:  2129
+  UUID: 716DE5D4-0B57-3218-955F-DD022E0C1159
+  Functions: 1285
+  Symbols:   2709
+  CStrings:  2108
 
Symbols:
+ +[DaemonUtils _updateDFRStatus].cold.1
+ +[DaemonUtils deviceHasPearl].cold.1
+ +[DaemonUtils deviceHasSEP].cold.1
+ +[DaemonUtils deviceHasTouchID].cold.1
+ +[DaemonUtils sharedInstance].cold.1
+ +[InstalledAppsCache sharedInstance].cold.1
+ +[LAAnalyticsPasscodeFallbackPeriod _persistedInstancesStorage].cold.1
+ +[LANVRAM sharedInstance].cold.1
+ +[LASecureIOAsset stringFromLASIOAssetButtonAction:].cold.1
+ +[LASecureIOAsset stringFromLASIOAssetFormat:].cold.1
+ +[LASecureIOAsset stringFromLASIOAssetType:].cold.1
+ +[LASecureIOHelper sharedInstance].cold.1
+ +[LASecureIOScene stringFromLASIOSceneSecureIOType:].cold.1
+ +[PreflightCache sharedInstance].cold.1
+ +[PreflightCacheInvalidationSource voidInvalidationSource].cold.1
+ +[PushButtonMonitor sharedInstance].cold.1
+ +[Request requestFromCurrentConnection].cold.2
+ +[TrustedAccessoryHelper sharedInstance].cold.1
+ +[WatchMonitor sharedInstance].cold.1
+ -[Caller isEqualToAuditTokenData:].cold.2
+ -[DarwinNotificationInvalidationSource initWithPreflightCache:notificationName:].cold.2
+ -[EvaluationRequest analyticsData]
+ -[EvaluationRequest isImmediateSuccess]
+ -[EvaluationRequest isInteractive]
+ -[EvaluationRequest setAnalyticsData:]
+ -[LAAnalytics _collect].cold.1
+ -[WatchMonitor start].cold.1
+ ACMContextGetExternalForm.cold.1
+ GCC_except_table103
+ GCC_except_table104
+ GCC_except_table105
+ GCC_except_table108
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table117
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table150
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table60
+ GCC_except_table89
+ GCC_except_table90
+ GCC_except_table91
+ LA_LOG.cold.1
+ LA_LOG_AirDb.cold.1
+ LA_LOG_INTERACTIVE.cold.1
+ LA_LOG_MechanismWatchMonitor.cold.1
+ OBJC_IVAR_$_EvaluationRequest.analyticsData
+ OBJC_IVAR_$_EvaluationRequest.immediateSuccess
+ SharingLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_LACAnalyticsData
+ _OBJC_CLASS_$_LACInstalledAppsCache
+ _OBJC_CLASS_$_LACPolicyUtilities
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
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __21-[WatchMonitor start]_block_invoke.10
+ __21-[WatchMonitor start]_block_invoke.10.cold.1
+ __21-[WatchMonitor start]_block_invoke.5
+ __21-[WatchMonitor start]_block_invoke.6.cold.1
+ ___SharingLibraryCore_block_invoke
+ ___getSFApproveDiscoveryClass_block_invoke
+ __block_literal_global.53
+ _audit_stringSharing
+ _getSFApproveDiscoveryClass
+ _objc_msgSend$analyticsData
+ _objc_msgSend$bundleId
+ _objc_msgSend$bundlePathForPid:stripXPCService:
+ _objc_msgSend$displayName
+ _objc_msgSend$infoForPid:
+ _objc_msgSend$isImmediateSuccess
+ _objc_msgSend$setAnalyticsData:
+ getSFApproveDiscoveryClass.softClass
+ updateLogLevelFromKext.cold.1
- -[EvaluationRequest immediateSuccess]
- -[EvaluationRequest interactive]
- -[InstalledAppsCache _bundleForPid:]
- -[InstalledAppsCache _bundleForPid:].cold.1
- -[InstalledAppsCache _bundlePathForPid:]
- -[InstalledAppsCache _bundlePathForPid:].cold.1
- -[InstalledAppsCache _localizedNameForBundle:]
- -[InstalledAppsCache _localizedNameForPath:]
- -[InstalledAppsCache _localizedNameFromInfoDict:path:]
- -[Request interactive]
- OBJC_IVAR_$_EvaluationRequest._immediateSuccess
- OBJC_IVAR_$_Request._interactive
- _CFBundleCopyBundleURL
- _CFBundleCopyInfoDictionaryForURL
- _CFURLCreateWithFileSystemPath
- _NSURLLocalizedNameKey
- _OBJC_CLASS_$_NSLocale
- _OBJC_CLASS_$_SFApproveDiscovery
- __21-[WatchMonitor start]_block_invoke.11
- __21-[WatchMonitor start]_block_invoke.11.cold.1
- __21-[WatchMonitor start]_block_invoke.7
- __21-[WatchMonitor start]_block_invoke.7.cold.1
- __CFBundleCreateWithExecutableURLIfLooksLikeBundle
- __LSASNCreateWithPid
- __LSCopyApplicationInformation
- __block_literal_global.41
- __block_literal_global.54
- __isNullOrEqualMem2
- __kLSBundlePathKey
- _objc_msgSend$URLForResource:withExtension:subdirectory:localization:
- _objc_msgSend$_bundleForPid:
- _objc_msgSend$_bundlePathForPid:
- _objc_msgSend$_localizedNameForBundle:
- _objc_msgSend$_localizedNameForPath:
- _objc_msgSend$_localizedNameFromInfoDict:path:
- _objc_msgSend$appNameForPid:bundleId:
- _objc_msgSend$bundleIdentifier
- _objc_msgSend$bundlePath
- _objc_msgSend$bundleWithURL:
- _objc_msgSend$dictionaryWithContentsOfURL:
- _objc_msgSend$getResourceValue:forKey:error:
- _objc_msgSend$immediateSuccess
- _objc_msgSend$localizations
- _objc_msgSend$localizedInfoDictionary
- _objc_msgSend$preferredLanguages
- _objc_msgSend$preferredLocalizationsFromArray:forPreferences:
- _objc_msgSend$stringByDeletingPathExtension
- _objc_msgSend$substringToIndex:
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/LASecureIO/LASecureIO.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/LASecureIOLocal/LASecureIODisplay.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/LASecureIOLocal/LASecureIOLocal.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/LASecureIOd/LASecureIOServer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOArchive.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOCommunication.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOUtils.m"
+ "/System/Library/PrivateFrameworks/Sharing.framework/Contents/MacOS/Sharing"
+ "@\"LACAnalyticsData\""
+ "@\"LACAnalyticsData\"16@0:8"
+ "Approve discovery not available"
+ "T@\"LACAnalyticsData\",&,N"
+ "T@\"LACAnalyticsData\",&,N,VanalyticsData"
+ "TB,N,GisImmediateSuccess"
+ "TB,N,GisImmediateSuccess,VimmediateSuccess"
+ "analyticsData"
+ "bundleId"
+ "displayName"
+ "infoForPid:"
+ "isImmediateSuccess"
+ "isInteractive"
+ "setAnalyticsData:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/Sharing.framework/Sharing"
+ "v24@0:8@\"LACAnalyticsData\"16"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/LASecureIO/LASecureIO.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/LASecureIOLocal/LASecureIODisplay.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/LASecureIOLocal/LASecureIOLocal.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/LASecureIOd/LASecureIOServer.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOArchive.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOCommunication.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOUtils.m"
- "/Contents/XPCServices/"
- "CFBundleDisplayName"
- "CFBundleName"
- "CFBundleVisibleComponentName"
- "Determined localized name for bundle %{public}@: `%{public}@`"
- "Determined localized name for path %{public}@: `%{public}@`"
- "Determined path for PID %d: %{public}@"
- "Failed to determine bundle path for pid: %d"
- "Failed to determine path for pid: %d"
- "InfoPlist"
- "TB,N,V_immediateSuccess"
- "TB,R,N,V_interactive"
- "URLForResource:withExtension:subdirectory:localization:"
- "_bundleForPid:"
- "_bundlePathForPid:"
- "_immediateSuccess"
- "_interactive"
- "_localizedNameForBundle:"
- "_localizedNameForPath:"
- "_localizedNameFromInfoDict:path:"
- "bundleIdentifier"
- "bundlePath"
- "bundleWithURL:"
- "dictionaryWithContentsOfURL:"
- "getResourceValue:forKey:error:"
- "interactive"
- "localizations"
- "localizedInfoDictionary"
- "preferredLanguages"
- "preferredLocalizationsFromArray:forPreferences:"
- "stringByDeletingPathExtension"
- "strings"
- "substringToIndex:"

```
