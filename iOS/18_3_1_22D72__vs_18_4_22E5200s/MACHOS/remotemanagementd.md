## remotemanagementd

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd`

```diff

-502.2.7.0.0
-  __TEXT.__text: 0x88580
+560.4.9.0.0
+  __TEXT.__text: 0x91924
   __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_stubs: 0xbb40
-  __TEXT.__objc_methlist: 0x3d68
+  __TEXT.__objc_stubs: 0xc1c0
+  __TEXT.__objc_methlist: 0x48c8
   __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0x42a4
-  __TEXT.__cstring: 0x2d5d
-  __TEXT.__objc_classname: 0xf75
-  __TEXT.__objc_methname: 0xe5c4
-  __TEXT.__objc_methtype: 0x2524
-  __TEXT.__oslogstring: 0xb195
+  __TEXT.__gcc_except_tab: 0x4914
+  __TEXT.__cstring: 0x2e2d
+  __TEXT.__objc_classname: 0xfc8
+  __TEXT.__objc_methname: 0xef15
+  __TEXT.__objc_methtype: 0x2674
+  __TEXT.__oslogstring: 0xbbba
   __TEXT.__ustring: 0x246
-  __TEXT.__unwind_info: 0x1e20
+  __TEXT.__unwind_info: 0x1f90
   __DATA_CONST.__auth_got: 0x440
-  __DATA_CONST.__got: 0x920
-  __DATA_CONST.__const: 0x2590
-  __DATA_CONST.__cfstring: 0x3240
-  __DATA_CONST.__objc_classlist: 0x2d0
+  __DATA_CONST.__got: 0x960
+  __DATA_CONST.__const: 0x2648
+  __DATA_CONST.__cfstring: 0x32e0
+  __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x92c8
-  __DATA.__objc_selrefs: 0x3190
-  __DATA.__objc_ivar: 0x2a0
-  __DATA.__objc_data: 0x1c20
+  __DATA.__objc_const: 0x8368
+  __DATA.__objc_selrefs: 0x3490
+  __DATA.__objc_ivar: 0x2a8
+  __DATA.__objc_data: 0x1cc0
   __DATA.__data: 0xc68
-  __DATA.__bss: 0x530
+  __DATA.__bss: 0x550
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2349
-  Symbols:   436
-  CStrings:  3887
+  Functions: 2521
+  Symbols:   441
+  CStrings:  4020
 
Symbols:
+ _OBJC_CLASS_$_RMMDMHelper
+ _OBJC_CLASS_$_RMStoreAssetKey
+ _OBJC_CLASS_$_RMSynchronous
+ _RMStoreOptionEnrollmentURL
+ _RMStoreOptionMetaData
CStrings:
+ "\x01\x14"
+ "%@ or %@"
+ "@52@0:8@16@24@32B40^@44"
+ "@60@0:8@16@24@32@40@48B56"
+ "B44@0:8@16@24B32^@36"
+ "B48@0:8@16q24@32^@40"
+ "Cached asset data %{public}@"
+ "Cached asset data for %{public}@"
+ "Cached asset file %{public}@"
+ "Cached asset file for %{public}@"
+ "ClientController: taking ownership of management source DDM"
+ "Could not link store: %{public}@"
+ "Failed to cached asset data for %{public}@: %{public}@"
+ "Failed to cached asset file for %{public}@: %{public}@"
+ "Failed to clear restrictions: %{public}@"
+ "Failed to copy cached asset file for %{public}@: %{public}@"
+ "Failed to copy store asset cache file: %{public}@"
+ "Failed to create asset cache data: %{public}@"
+ "Failed to create asset cache file: %{public}@"
+ "Failed to create store asset cache directrory: %{public}@"
+ "Failed to fetch declaration status for store %{public}@..."
+ "Failed to find declaration status for %{public}@..."
+ "Failed to link store %{public}@"
+ "Failed to load declaration status for store %{public}@..."
+ "Failed to read cached asset data for %{public}@: %{public}@"
+ "Failed to read cached asset file for %{public}@: %{public}@"
+ "Failed to read store asset cache data: %{public}@"
+ "Failed to remove store asset cache directrory: %{public}@"
+ "Failed to remove store asset cache file: %{public}@"
+ "Failed to take ownership of %{public}@: %{public}@"
+ "Failed to write store asset cache data: %{public}@"
+ "Found cached asset data %{public}@"
+ "Found cached asset file %{public}@"
+ "Ignoring migration - no restrictions found"
+ "Invalid declaration status for %{public}@..."
+ "Invalid metadata - ignoring: %{public}@"
+ "LinkStoreIdentifier with %{public}@..."
+ "Linked store"
+ "Management source for %{public}@ disappeared before we could take ownership."
+ "No cached asset data %{public}@"
+ "No cached asset file %{public}@"
+ "No cached asset to remove %{public}@"
+ "No store asset cache directrory to remove %{public}@"
+ "Q40@0:8@16@24^@32"
+ "RMDeclarationStatusDidChangeNotification"
+ "RMMigrationMathSettings"
+ "RMStoreAssetCache"
+ "Removed cached asset %{public}@"
+ "Removed restrictions set by MathSettingsExtension"
+ "Removed store asset cache directrory %{public}@"
+ "Removing asset item: %{public}@:%{public}@"
+ "StoreXPCListenerDelegate: LinkStoreIdentifier from proxy handler"
+ "StoreXPCListenerDelegate: WaitForActiveAndValidDeclarations from proxy handler"
+ "TB,V_waitingForDeclarationStatusChanges"
+ "Taking ownership for DDM: %{public}@"
+ "Unable to fetch management source for (%{public}@): %{public}@"
+ "Using cached asset data for %{public}@"
+ "Using cached asset file for %{public}@"
+ "Wait for declarations failed: %{public}@"
+ "Wait for declarations success"
+ "WaitForActiveAndValidDeclarations already running"
+ "WaitForActiveAndValidDeclarations completed after notification with %{public}@..."
+ "WaitForActiveAndValidDeclarations completes immediately with %{public}@..."
+ "WaitForActiveAndValidDeclarations notification result %{public}@..."
+ "WaitForActiveAndValidDeclarations timed out with %{public}@..."
+ "WaitForActiveAndValidDeclarations with %{public}@..."
+ "_assetsRemoved:storeIdentifier:personaID:"
+ "_cacheDataAsset:storeIdentifier:resolvedAsset:"
+ "_cacheDirectoryForStoreWithIdentifier:createIfNeeded:error:"
+ "_cacheFileAsset:storeIdentifier:resolvedAsset:"
+ "_cacheFileForAssetWithIdentifier:serverToken:storeIdentifier:createIfNeeded:error:"
+ "_cachedDataAsset:storeIdentifier:unresolvedAsset:reference:url:useDDM:"
+ "_cachedFileAsset:storeIdentifier:unresolvedAsset:reference:url:useDDM:"
+ "_checkActiveAndValidDeclarations:storeIdentifier:error:"
+ "_clearAsset:personaID:error:"
+ "_clearKeychainAsset:personaID:error:"
+ "_enrollClientWithManagementSourceObjectID:managementSourceIdentifier:conduitType:account:accountStore:completionHandler:"
+ "_removeOldRestrictions:"
+ "_removedStoreAsset:storeIdentifier:personaID:isKeychain:"
+ "_resolveAsDataAsset:storeIdentifier:unresolvedAsset:reference:url:useDDM:useCache:completionHandler:"
+ "_resolveAsFileAsset:storeIdentifier:unresolvedAsset:reference:url:useDDM:useCache:completionHandler:"
+ "_resolveAsset:storeIdentifier:unresolvedAsset:isDDM:useCache:completionHandler:"
+ "_resolveAsset:storeIdentifier:unresolvedAsset:reference:url:useDDM:useCache:completionHandler:"
+ "_resolveKeychainAsset:storeIdentifier:unresolvedAsset:isDDM:enrollmentType:completionHandler:"
+ "_verifyUniqueStoreWithURL:enrollmentType:context:error:"
+ "_waitLock"
+ "_waitingForDeclarationStatusChanges"
+ "addObserverForName:object:queue:usingBlock:"
+ "allClientUUIDsForClientType:"
+ "assetCacheDirectoryURLCreateIfNeeded:"
+ "assetFile"
+ "cStringUsingEncoding:"
+ "cacheAssetWithIdentifier:serverToken:storeIdentifier:data:error:"
+ "cacheAssetWithIdentifier:serverToken:storeIdentifier:fileURL:error:"
+ "cachedAssetDataWithIdentifier:serverToken:storeIdentifier:error:"
+ "cachedAssetFileWithIdentifier:serverToken:storeIdentifier:error:"
+ "com.apple.RemoteManagement.MathSettingsExtension"
+ "complete"
+ "configurationUIWithTitle:description:details:hiddenDetails:"
+ "copyItemAtURL:toURL:error:"
+ "createTimeoutError"
+ "declarationStatusDidChange"
+ "enrollmentURLForProfileIdentifier:"
+ "linkStoreIdentifier:profileIdentifier:accountIdentifier:completionHandler:"
+ "migrationMathSettings"
+ "newAssetKeyWithAssetIdentifier:assetServerToken:"
+ "numberWithUnsignedInteger:"
+ "postNotificationName:object:"
+ "queryForDeclarationStatusWithManagementSourceIdentifier:error:"
+ "removeAllCachedAssetsForStoreIdentifier:error:"
+ "removeCachedAsset:serverToken:storeIdentifier:error:"
+ "removeObserver:"
+ "removedAsset:personaID:isKeychain:error:"
+ "resolveAsset:storeIdentifier:unresolvedAsset:personaID:isDDM:enrollmentType:completionHandler:"
+ "setActive:scope:"
+ "setWaitingForDeclarationStatusChanges:"
+ "statusActivations"
+ "statusActive"
+ "statusAssets"
+ "statusConfigurations"
+ "statusValid"
+ "storeAssetCache"
+ "subscriberIdentifier"
+ "takeOwnershipOfMDMStoreWithIdentifier:completionHandler:"
+ "useCache"
+ "v16@?0@\"NSNotification\"8"
+ "v44@0:8@16@24@32B40"
+ "v48@0:8@\"NSSet\"16d24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@16d24@32@?40"
+ "v56@0:8@16@24@32B40B44@?48"
+ "v64@0:8@16@24q32@40@48@?56"
+ "v68@0:8@16@24@32@40B48q52@?60"
+ "v72@0:8@16@24@32@40@48B56B60@?64"
+ "waitDeclarationsQueue"
+ "waitForActiveAndValidDeclarations:timeout:storeIdentifier:completionHandler:"
+ "waitForCompletionWithTimeout:"
+ "waitingForDeclarationStatusChanges"
+ "writeToURL:options:error:"
- "Removing asset keychain item: %{public}@:%{public}@"
- "_assetsRemoved:managementSourceIdentifier:personaID:"
- "_keychainAssetRemoved:managementSourceIdentifier:personaID:"
- "_removeKeychainAssets:"
- "_resolveAsset:unresolvedAsset:isDDM:completionHandler:"
- "_resolveAsset:unresolvedAsset:reference:url:useDDM:completionHandler:"
- "_resolveKeychainAsset:unresolvedAsset:isDDM:enrollmentType:completionHandler:"
- "configurationUIWithTitle:description:details:"
- "removedAsset:personaID:error:"
- "resolveAsset:unresolvedAsset:personaID:isDDM:enrollmentType:completionHandler:"
- "v52@0:8@16@24B32q36@?44"
- "v60@0:8@16@24@32@40B48@?52"

```
