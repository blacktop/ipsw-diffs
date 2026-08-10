## UARPAssetManagerServiceiCloud

> `/System/Library/PrivateFrameworks/UARPAssetManager.framework/XPCServices/UARPAssetManagerServiceiCloud.xpc/UARPAssetManagerServiceiCloud`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-1587.0.27.0.0
-  __TEXT.__text: 0x12070
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_stubs: 0x2560
-  __TEXT.__objc_methlist: 0xed4
-  __TEXT.__objc_classname: 0x289
-  __TEXT.__cstring: 0x197d
-  __TEXT.__objc_methname: 0x29a5
-  __TEXT.__objc_methtype: 0x83c
+1587.2.2.0.0
+  __TEXT.__text: 0x12c50
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_stubs: 0x2740
+  __TEXT.__objc_methlist: 0xfa4
+  __TEXT.__objc_classname: 0x2b4
+  __TEXT.__cstring: 0x1989
+  __TEXT.__objc_methname: 0x2ce1
+  __TEXT.__objc_methtype: 0x864
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0x1939
+  __TEXT.__oslogstring: 0x1a37
   __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__unwind_info: 0x450
+  __TEXT.__unwind_info: 0x470
   __DATA_CONST.__const: 0x640
-  __DATA_CONST.__cfstring: 0x11c0
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__cfstring: 0x1220
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x2198
-  __DATA.__objc_selrefs: 0xb20
-  __DATA.__objc_ivar: 0x100
-  __DATA.__objc_data: 0x4b0
+  __DATA.__objc_const: 0x2398
+  __DATA.__objc_selrefs: 0xba8
+  __DATA.__objc_ivar: 0x120
+  __DATA.__objc_data: 0x500
   __DATA.__data: 0x360
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 383
-  Symbols:   264
-  CStrings:  883
+  Functions: 408
+  Symbols:   269
+  CStrings:  919
 
Symbols:
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_UARPAssetManagerServiceiCloudPendingLookup
+ _OBJC_METACLASS_$_UARPAssetManagerServiceiCloudPendingLookup
+ _objc_setProperty_nonatomic_copy
CStrings:
+ ""
+ "%@_%d"
+ "%s: Failed to create download staging directory %{public}@ error:%{public}@"
+ "%s: Failed to move downloaded file to %{public}@ error:%{public}@"
+ "+[UARPAssetSubscriptioniCloud developmentEnvironmentForContainerID:]"
+ "+[UARPAssetSubscriptioniCloud resolvedContainerIDForContainerID:]"
+ "<%@: pgpn=%@-%@, containerID=%@ releaseNotes=%@ development=%@ domain=%@>"
+ "@28@0:8@16B24"
+ "@36@0:8@16B24@28"
+ "@48@0:8@16@24@32B40B44"
+ "@60@0:8@16@24@32B40B44B48@52"
+ "Deferring iCloud lookup for ContainerID:%{public}@ (development:%d); a lookup is already in progress"
+ "Failed to create iCloud bookkeeping directory %{public}@ error %{public}@"
+ "Performing Remote Check on iCloud ContainerID:%{public}@ (development:%d) for subscriptions: %{public}@"
+ "T@\"NSArray\",C,N,V_subscriptions"
+ "T@\"NSString\",C,N,V_containerID"
+ "TB,N,V_clearTokenCache"
+ "TB,N,V_developmentEnvironment"
+ "TB,N,V_periodicUpdate"
+ "TB,R,V_developmentEnvironment"
+ "UARPAssetManagerServiceiCloudPendingLookup"
+ "UUID"
+ "UUIDString"
+ "_clearTokenCache"
+ "_developmentEnvironment"
+ "_lookupInProgress"
+ "_pendingLookups"
+ "_subscriptions"
+ "a"
+ "bookkeepingDirectoryForContainerID:developmentEnvironment:"
+ "cacheSubdirectoryForContainerID:developmentEnvironment:"
+ "clearTokenCache"
+ "createContainerWithIdentifier:developmentEnvironment:"
+ "development"
+ "developmentEnvironmentForContainerID:"
+ "downloadAssetForSubscriptions:containerID:developmentEnvironment:clearTokenCache:periodicUpdate:"
+ "filePathForiCloudTokenCacheForContainerID:developmentEnvironment:"
+ "initWithContainerID:developmentEnvironment:tokenFilePath:"
+ "initWithDelegate:containerID:tokenFilePath:developmentEnvironment:periodicUpdate:"
+ "initWithProductGroup:productNumber:containerID:releaseNotesAsset:downloadOnCellularAllowed:developmentEnvironment:domain:"
+ "periodicUpdate"
+ "removeObjectAtIndex:"
+ "resolvedContainerIDForContainerID:"
+ "setClearTokenCache:"
+ "setContainerID:"
+ "setDevelopmentEnvironment:"
+ "setPeriodicUpdate:"
+ "setSubscriptions:"
+ "stringByAppendingString:"
+ "subscriptions"
+ "substringFromIndex:"
+ "v44@0:8@16@24B32B36B40"
- "%s: Error renaming file: %{public}@"
- "%s: Using filename: %{public}@ for download"
- "-[UARPAssetManageriCloudContainer createContainerWithIdentifier:]"
- "-[UARPiCloudDownloadManager downloadFileFromURL:assetHash:record:subscription:]_block_invoke_2"
- "<%@: pgpn=%@-%@, containerID=%@ releaseNotes=%@ domain=%@>"
- "@44@0:8@16@24@32B40"
- "@56@0:8@16@24@32B40B44@48"
- "Performing Remote Check on iCloud ContainerID:%{public}@ for subscriptions: %{public}@"
- "createContainerWithIdentifier:"
- "downloadAssetForSubscriptions:containerID:clearTokenCache:periodicUpdate:"
- "filePathForiCloudTokenCache"
- "initWithContainerID:tokenFilePath:"
- "initWithDelegate:containerID:tokenFilePath:periodicUpdate:"
- "initWithProductGroup:productNumber:containerID:releaseNotesAsset:downloadOnCellularAllowed:domain:"
- "localizedDescription"
- "v40@0:8@16@24B32B36"
```
