## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/Versions/A/TVRemoteCore`

```diff

-496.30.3.0.0
-  __TEXT.__text: 0x5fc08
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x6e74
+496.40.31.0.0
+  __TEXT.__text: 0x611b8
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_methlist: 0x7fe0
   __TEXT.__const: 0x200
   __TEXT.__gcc_except_tab: 0xb30
-  __TEXT.__cstring: 0x4b97
-  __TEXT.__oslogstring: 0x62c1
-  __TEXT.__unwind_info: 0x1548
-  __TEXT.__objc_classname: 0xc99
-  __TEXT.__objc_methname: 0xea7b
-  __TEXT.__objc_methtype: 0x285d
-  __TEXT.__objc_stubs: 0x9160
-  __DATA_CONST.__got: 0x508
-  __DATA_CONST.__const: 0x7b0
-  __DATA_CONST.__objc_classlist: 0x358
+  __TEXT.__cstring: 0x4c62
+  __TEXT.__oslogstring: 0x63ae
+  __TEXT.__unwind_info: 0x1578
+  __TEXT.__objc_classname: 0xca5
+  __TEXT.__objc_methname: 0xecf9
+  __TEXT.__objc_methtype: 0x2923
+  __TEXT.__objc_stubs: 0x9280
+  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__const: 0x808
+  __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3308
+  __DATA_CONST.__objc_selrefs: 0x38d0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x2b8
+  __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__auth_got: 0x440
   __AUTH_CONST.__const: 0x1408
-  __AUTH_CONST.__cfstring: 0x6840
-  __AUTH_CONST.__objc_const: 0xe268
+  __AUTH_CONST.__cfstring: 0x69e0
+  __AUTH_CONST.__objc_const: 0xc6b0
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x2170
-  __DATA.__objc_ivar: 0x848
+  __AUTH.__objc_data: 0x21c0
+  __DATA.__objc_ivar: 0x860
   __DATA.__data: 0xa90
   __DATA.__bss: 0x178
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B2AD09F-AA4D-3C9F-B687-2038CC1D890E
-  Functions: 2649
-  Symbols:   5893
-  CStrings:  5357
+  UUID: FEFBAEC1-0264-3CB5-A8E5-0D98740434CD
+  Functions: 2683
+  Symbols:   5973
+  CStrings:  5415
 
Symbols:
+ +[TVRCAnalytics sharedInstance].cold.1
+ +[TVRCAppInfo appInfoWithBundleID:dictionary:]
+ +[TVRCAppInfo appInfoWithLocalizedName:bundleID:imageData:MRUCount:appGenre:appType:]
+ +[TVRCAppInfo supportsSecureCoding]
+ +[TVRCHMHomeObserver sharedInstance].cold.1
+ +[TVRCMediaRemoteEndpointManager sharedInstance].cold.1
+ +[TVRCSiriRemoteConnectionManager sharedInstance].cold.1
+ +[TVRCXPCClient sharedInstance].cold.1
+ +[TVRMSNowPlayingArtworkCache sharedArtworkCache].cold.1
+ -[TVRCAppInfo .cxx_destruct]
+ -[TVRCAppInfo MRUCount]
+ -[TVRCAppInfo appGenre]
+ -[TVRCAppInfo appInfoWithMRUCount:]
+ -[TVRCAppInfo appType]
+ -[TVRCAppInfo bundleID]
+ -[TVRCAppInfo copyWithZone:]
+ -[TVRCAppInfo description]
+ -[TVRCAppInfo encodeWithCoder:]
+ -[TVRCAppInfo hash]
+ -[TVRCAppInfo imageData]
+ -[TVRCAppInfo initWithCoder:]
+ -[TVRCAppInfo initWithLocalizedName:bundleID:imageData:MRUCount:appGenre:appType:]
+ -[TVRCAppInfo isEqual:]
+ -[TVRCAppInfo isTVApp]
+ -[TVRCAppInfo localizedName]
+ -[TVRCDevice fetchLaunchableAppsWithCompletion:]
+ -[TVRCDevice launchAppWithBundleID:completion:]
+ -[TVRCPerson _formattedDateWithDate:].cold.1
+ -[TVRCPerson formattedAge].cold.1
+ -[TVRCRPCompanionLinkClientWrapper fetchLaunchableAppsWithCompletion:]
+ -[TVRCRPCompanionLinkClientWrapper launchAppWithBundleID:completion:]
+ -[TVRCRapportDeviceImpl fetchLaunchableAppsWithCompletion:]
+ -[TVRCRapportDeviceImpl launchAppWithBundleID:completion:]
+ -[TVRCXPCClient fetchLaunchableAppsForDeviceWithIdentifier:completion:]
+ -[TVRCXPCClient launchAppForDeviceWithIdentifier:bundleID:completion:]
+ -[TVRXDevice fetchLaunchableAppsWithCompletion:]
+ -[TVRXDevice launchAppWithBundleID:completion:]
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table109
+ GCC_except_table117
+ GCC_except_table122
+ GCC_except_table128
+ GCC_except_table138
+ GCC_except_table147
+ GCC_except_table59
+ GCC_except_table96
+ GCC_except_table98
+ OBJC_IVAR_$_TVRCAppInfo._MRUCount
+ OBJC_IVAR_$_TVRCAppInfo._appGenre
+ OBJC_IVAR_$_TVRCAppInfo._appType
+ OBJC_IVAR_$_TVRCAppInfo._bundleID
+ OBJC_IVAR_$_TVRCAppInfo._imageData
+ OBJC_IVAR_$_TVRCAppInfo._localizedName
+ TVRMSLogEx.cold.1
+ _OBJC_CLASS_$_TVRCAppInfo
+ _OBJC_METACLASS_$_TVRCAppInfo
+ _TVRCApplicationGenreKey
+ _TVRCApplicationTypeKey
+ _TVRCBLEDiscoveryLog.cold.1
+ _TVRCBundleIDKey
+ _TVRCGeneralLog.cold.1
+ _TVRCHomeKitLog.cold.1
+ _TVRCImageKey
+ _TVRCIncludeAppMetadataKey
+ _TVRCLaunchAppEvent
+ _TVRCLocalizedAppNameKey
+ _TVRCMDMLog.cold.1
+ _TVRCMediaEventsLog.cold.1
+ _TVRCMediaRemoteLog.cold.1
+ _TVRCPreferredDeviceLog.cold.1
+ _TVRCRMSLog.cold.1
+ _TVRCRapportLog.cold.1
+ _TVRCRemoteTextInputLog.cold.1
+ _TVRCXPCLog.cold.1
+ __OBJC_$_CLASS_METHODS_TVRCAppInfo
+ __OBJC_$_CLASS_PROP_LIST_TVRCAppInfo
+ __OBJC_$_INSTANCE_METHODS_TVRCAppInfo
+ __OBJC_$_INSTANCE_VARIABLES_TVRCAppInfo
+ __OBJC_$_PROP_LIST_TVRCAppInfo
+ __OBJC_CLASS_PROTOCOLS_$_TVRCAppInfo
+ __OBJC_CLASS_RO_$_TVRCAppInfo
+ __OBJC_METACLASS_RO_$_TVRCAppInfo
+ ___69-[TVRCRPCompanionLinkClientWrapper launchAppWithBundleID:completion:]_block_invoke
+ ___70-[TVRCRPCompanionLinkClientWrapper fetchLaunchableAppsWithCompletion:]_block_invoke
+ ___RMSLoggingInitialize_block_invoke_2.cold.1
+ _objc_msgSend$MRUCount
+ _objc_msgSend$appGenre
+ _objc_msgSend$appType
+ _objc_msgSend$fetchLaunchableAppsForDeviceWithIdentifier:completion:
+ _objc_msgSend$fetchLaunchableAppsWithCompletion:
+ _objc_msgSend$initWithLocalizedName:bundleID:imageData:MRUCount:appGenre:appType:
+ _objc_msgSend$launchAppForDeviceWithIdentifier:bundleID:completion:
+ _objc_msgSend$launchAppWithBundleID:completion:
+ _objc_msgSend$localizedName
- +[TVRCFeatures testarossaEnabled]
- GCC_except_table105
- GCC_except_table113
- GCC_except_table118
- GCC_except_table124
- GCC_except_table134
- GCC_except_table143
- GCC_except_table57
- GCC_except_table88
- GCC_except_table90
- GCC_except_table97
- GCC_except_table99
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _fmod
CStrings:
+ "82"
+ "<%@ %p: name=%@; bundleID=%@; appType=%@; appGenre=%@; mruCount=%@>"
+ "@64@0:8@16@24@32Q40Q48q56"
+ "ApplicationGenreKey"
+ "ApplicationTypeKey"
+ "Asking tvremoted for launchable apps for %{public}@"
+ "Asking tvremoted to launch app %{public}@ for %{public}@"
+ "BundleIDKey"
+ "Found existing device = [%{public}@] for device = [%{public}@]"
+ "ImageKey"
+ "IncludeAppMetadataKey"
+ "Invalid bundleID sent to %@"
+ "LaunchApp"
+ "LocalizedAppName"
+ "MRUCount"
+ "Sending companion request with ID %@"
+ "T@\"NSData\",R,N,V_imageData"
+ "T@\"NSString\",R,N,V_bundleID"
+ "T@\"NSString\",R,N,V_localizedName"
+ "TQ,R,N,V_MRUCount"
+ "TQ,R,N,V_appGenre"
+ "TVRCAppInfo"
+ "Tq,R,N,V_appType"
+ "_MRUCount"
+ "_appGenre"
+ "_appType"
+ "_localizedName"
+ "appGenre"
+ "appInfoWithBundleID:dictionary:"
+ "appInfoWithLocalizedName:bundleID:imageData:MRUCount:appGenre:appType:"
+ "appInfoWithMRUCount:"
+ "appType"
+ "fetchLaunchableAppsForDeviceWithIdentifier:completion:"
+ "fetchLaunchableAppsWithCompletion:"
+ "initWithLocalizedName:bundleID:imageData:MRUCount:appGenre:appType:"
+ "inputSession:documentStateDidChange:withMergeResult:"
+ "isTVApp"
+ "launchAppForDeviceWithIdentifier:bundleID:completion:"
+ "launchAppWithBundleID:completion:"
+ "localizedName"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v40@0:8@\"RTIInputSystemSession\"16@\"RTIDocumentState\"24Q32"
+ "v40@0:8@16@24Q32"
- "TVApp"
- "testarossa"
- "testarossaEnabled"

```
