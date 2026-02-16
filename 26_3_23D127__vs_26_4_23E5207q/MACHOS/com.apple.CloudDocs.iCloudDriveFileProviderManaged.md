## com.apple.CloudDocs.iCloudDriveFileProviderManaged

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged`

```diff

-4257.80.8.0.0
-  __TEXT.__text: 0x27874
-  __TEXT.__auth_stubs: 0x620
+4479.100.79.0.4
+  __TEXT.__text: 0x28400
+  __TEXT.__auth_stubs: 0x5d0
   __TEXT.__objc_stubs: 0x2c00
-  __TEXT.__objc_methlist: 0x1dc4
+  __TEXT.__objc_methlist: 0x1de4
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x2ce4
-  __TEXT.__objc_methname: 0x5277
-  __TEXT.__cstring: 0x4640
+  __TEXT.__gcc_except_tab: 0x2cd4
+  __TEXT.__objc_methname: 0x52a0
+  __TEXT.__cstring: 0x4682
   __TEXT.__oslogstring: 0x249d
   __TEXT.__objc_classname: 0x6e9
-  __TEXT.__objc_methtype: 0x35a2
-  __TEXT.__unwind_info: 0xa80
-  __DATA_CONST.__auth_got: 0x320
+  __TEXT.__objc_methtype: 0x3618
+  __TEXT.__unwind_info: 0xb08
+  __DATA_CONST.__auth_got: 0x2f8
   __DATA_CONST.__got: 0x270
   __DATA_CONST.__const: 0x10a8
   __DATA_CONST.__cfstring: 0x280

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA.__objc_const: 0x7c60
-  __DATA.__objc_selrefs: 0x1240
+  __DATA.__objc_const: 0x7cf8
+  __DATA.__objc_selrefs: 0x1250
   __DATA.__objc_ivar: 0x134
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0xae0

   - /System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
-  - /System/Library/PrivateFrameworks/AOSKit.framework/AOSKit
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
-  - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 8891F465-BF3A-331D-86AD-E631616605CB
-  Functions: 616
-  Symbols:   187
-  CStrings:  1463
+  UUID: 363E05A8-DA78-3B21-BBB2-1493A9C67DE0
+  Functions: 623
+  Symbols:   182
+  CStrings:  1465
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/os-plugins/fileprovider-extension-iclouddrive/BRDaemonConnection+FPFSExtensionAdditions.m"
+ "backupDatabaseWithURLWrapper:doNotObfuscate:reply:"
+ "computePurgeableSpaceWithReply:"
+ "createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:"
+ "getFPItemIDsForCKRecordIDs:reply:"
+ "handleUserNotificationResponse:reply:"
+ "isAccountCZM:"
+ "isRFAEmailSettingEnabledWithReply:"
+ "modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:"
+ "reclaimDiskSpaceWithReply:"
+ "setAllowsAccessRequests:defaultOn:"
+ "setRFAEmailSettingEnabled:reply:"
+ "v24@0:8@?<v@?@\"NSNumber\"@\"NSNumber\"@\"NSError\">16"
+ "v24@0:8@?<v@?q>16"
+ "v32@0:8@\"UNNotificationResponse\"16@?<v@?@\"NSError\">24"
+ "v36@0:8@\"FPSandboxingURLWrapper\"16B24@?<v@?@\"NSURL\"@\"NSError\">28"
+ "v36@?0@\"BRQueryItem\"8Q16B24@\"NSError\"28"
+ "v56@0:8@\"NSString\"16@\"NSFileProviderItemVersion\"24Q32@\"NSFileProviderRequest\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24Q32@40@?48"
+ "v72@0:8@\"<NSFileProviderItem>\"16Q24@\"FPSandboxingURLWrapper\"32Q40@\"NSFileProviderRequest\"48@\"NSDictionary\"56@?<v@?@\"BRQueryItem\"QB@\"NSError\">64"
+ "v72@0:8@16Q24@32Q40@48@56@?64"
+ "v80@0:8@\"<NSFileProviderItem>\"16@\"NSFileProviderItemVersion\"24Q32@\"FPSandboxingURLWrapper\"40Q48@\"NSFileProviderRequest\"56@\"NSDictionary\"64@?<v@?@\"BRQueryItem\"QB@\"NSError\">72"
+ "v80@0:8@16@24Q32@40Q48@56@64@?72"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/os-plugins/fileprovider-extension-iclouddrive/BRDaemonConnection+FPFSExtensionAdditions.m"
- "backupDatabaseWithURLWrapper:reply:"
- "computePurgeableSpaceForAllUrgenciesWithReply:"
- "createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:"
- "deleteItemWithIdentifier:baseVersion:options:completionHandler:"
- "dropSpotlightIndexWithReply:"
- "modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:"
- "purgeAmount:withUrgency:reply:"
- "reclaimAmount:withUrgency:reply:"
- "setSupportAllowingAccessRequests:"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSNumber\"@\"NSError\">16"
- "v32@0:8@\"FPSandboxingURLWrapper\"16@?<v@?@\"NSURL\"@\"NSError\">24"
- "v32@?0@\"BRQueryItem\"8Q16@\"NSError\"24"
- "v36@0:8q16i24@?28"
- "v36@0:8q16i24@?<v@?q>28"
- "v48@0:8@\"NSString\"16@\"NSFileProviderItemVersion\"24Q32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "v64@0:8@\"<NSFileProviderItem>\"16Q24@\"FPSandboxingURLWrapper\"32Q40@\"NSDictionary\"48@?<v@?@\"BRQueryItem\"Q@\"NSError\">56"
- "v64@0:8@16Q24@32Q40@48@?56"
- "v72@0:8@\"<NSFileProviderItem>\"16@\"NSFileProviderItemVersion\"24Q32@\"FPSandboxingURLWrapper\"40Q48@\"NSDictionary\"56@?<v@?@\"BRQueryItem\"Q@\"NSError\">64"
- "v72@0:8@16@24Q32@40Q48@56@?64"

```
