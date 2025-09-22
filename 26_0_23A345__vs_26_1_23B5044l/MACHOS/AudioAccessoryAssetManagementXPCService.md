## AudioAccessoryAssetManagementXPCService

> `/System/Library/PrivateFrameworks/AudioAccessoryAssetManagement.framework/XPCServices/AudioAccessoryAssetManagementXPCService.xpc/AudioAccessoryAssetManagementXPCService`

```diff

-30.59.1.9.0
-  __TEXT.__text: 0x37f8
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0xea0
-  __TEXT.__objc_methlist: 0x2f4
+31.5.2.1.2
+  __TEXT.__text: 0x39b4
+  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__objc_stubs: 0xee0
+  __TEXT.__objc_methlist: 0x2fc
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__cstring: 0x1294
-  __TEXT.__objc_methname: 0xf70
+  __TEXT.__cstring: 0x13de
+  __TEXT.__objc_methname: 0xfc9
   __TEXT.__objc_classname: 0xe3
-  __TEXT.__objc_methtype: 0x3e0
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x1d8
+  __TEXT.__objc_methtype: 0x3fb
+  __TEXT.__unwind_info: 0x180
+  __DATA_CONST.__auth_got: 0x1e8
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x2e8
-  __DATA_CONST.__cfstring: 0x2a0
+  __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x688
-  __DATA.__objc_selrefs: 0x4a0
-  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_const: 0x6b0
+  __DATA.__objc_selrefs: 0x4b0
+  __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1f0
   - /System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D2A4C7F6-F2D5-3DB4-B26D-6B5A9445057C
-  Functions: 78
-  Symbols:   101
-  CStrings:  351
+  UUID: 2E1097FC-4CE6-382E-9396-E1B52C6F9532
+  Functions: 79
+  Symbols:   103
+  CStrings:  362
 
Symbols:
+ _getpid
+ _objc_retain_x23
+ _objc_retain_x25
- _objc_retain_x24
CStrings:
+ "-[AudioAccessoryAssetManagementClientXPCConnection _registerLaunchHandlerWithCompletion:]_block_invoke_5"
+ "-[AudioAccessoryAssetManagementClientXPCConnection downloadTranslationAssets:localeIdentifiers:useCellular:showDownloadCompleteNotification:bundleIdentifier:completion:]"
+ "-[AudioAccessoryAssetManagementClientXPCConnection downloadTranslationAssets:localeIdentifiers:useCellular:showDownloadCompleteNotification:bundleIdentifier:completion:]_block_invoke"
+ "AudioAccessoryAssetManagementClientXPCConnection downloadTranslationAssets %@ downloadRequestedLanguages %@ for _bundleIdentifier: %@"
+ "XPC connection ended: %@"
+ "XPC connection started: %@"
+ "_bundleIdentifier"
+ "_localesRequestedForDownload %@ _localesDownloadStatus %@"
+ "_submitBackgroundTask bundleIdentifier of main: %@ applicationBundleIdentifier %@"
+ "com.apple.HeadphoneProxService"
+ "downloadTranslationAssets:localeIdentifiers:useCellular:showDownloadCompleteNotification:bundleIdentifier:completion:"
+ "nil"
+ "pidOfDownloadTranslationAssetsXPCService:"
+ "serviceName"
+ "v20@0:8i16"
+ "v56@0:8@\"AudioAccessoryAssetManagementClient\"16@\"NSArray\"24B32B36@\"NSString\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24B32B36@40@?48"
- "-[AudioAccessoryAssetManagementClientXPCConnection downloadTranslationAssets:localeIdentifiers:useCellular:showDownloadCompleteNotification:completion:]"
- "-[AudioAccessoryAssetManagementClientXPCConnection downloadTranslationAssets:localeIdentifiers:useCellular:showDownloadCompleteNotification:completion:]_block_invoke"
- "AudioAccessoryAssetManagementClientXPCConnection downloadTranslationAssets %@ downloadRequestedLanguages %@"
- "XPC connection ended: %#{pid}"
- "XPC connection started: %#{pid}"
- "downloadTranslationAssets:localeIdentifiers:useCellular:showDownloadCompleteNotification:completion:"
- "v48@0:8@\"AudioAccessoryAssetManagementClient\"16@\"NSArray\"24B32B36@?<v@?@\"NSError\">40"
- "v48@0:8@16@24B32B36@?40"

```
