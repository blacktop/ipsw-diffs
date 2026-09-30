## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3404.50.4.1.3
-  __TEXT.__text: 0x66110
+3404.58.2.0.0
+  __TEXT.__text: 0x689a0
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x33dc
+  __TEXT.__objc_methlist: 0x34d8
   __TEXT.__const: 0xf8
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__gcc_except_tab: 0x134c
-  __TEXT.__cstring: 0x9afd
-  __TEXT.__oslogstring: 0xb322
-  __TEXT.__unwind_info: 0x1110
-  __TEXT.__objc_classname: 0x413
-  __TEXT.__objc_methname: 0x9cd3
-  __TEXT.__objc_methtype: 0xf69
-  __TEXT.__objc_stubs: 0x7e80
+  __TEXT.__gcc_except_tab: 0x1358
+  __TEXT.__cstring: 0x9e5d
+  __TEXT.__oslogstring: 0xbbc1
+  __TEXT.__unwind_info: 0x1158
+  __TEXT.__objc_classname: 0x424
+  __TEXT.__objc_methname: 0x9f26
+  __TEXT.__objc_methtype: 0xfe4
+  __TEXT.__objc_stubs: 0x8100
   __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__const: 0x1aa8
-  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__const: 0x1b40
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2648
+  __DATA_CONST.__objc_selrefs: 0x26f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x5b0
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x4000
-  __AUTH_CONST.__objc_const: 0x4238
+  __AUTH_CONST.__cfstring: 0x40a0
+  __AUTH_CONST.__objc_const: 0x42d0
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x34c
   __DATA.__data: 0x230
   __DATA.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1384
-  Symbols:   1980
-  CStrings:  3540
+  Functions: 1408
+  Symbols:   2009
+  CStrings:  3616
 
Symbols:
+ _OBJC_CLASS_$_UAFExpiredAssets
+ _OBJC_METACLASS_$_UAFExpiredAssets
+ _kUAFAutoAssetDiscretionaryReason
+ _kUAFCacheDir
+ _kUAFExpiredAssetsDir
+ _kUAFTokenExtension
- _XPC_ACTIVITY_PRIORITY_MAINTENANCE
CStrings:
+ "%s Asset set %{public}@ incompatible with current OS, removing"
+ "%s AssetSet Token: %{public}@: %{public}@"
+ "%s Attempting force remove of asset set '%{public}@'"
+ "%s Auto asset set %{public}@ is configured, has atomic instance %{public}@, is available to clients, and current OS supported but current assets %{public}@ are marked as expired"
+ "%s Commit of exclusive transaction of tables creation failed"
+ "%s Could not get AFSiriCapabilitiesServiceClient class"
+ "%s Could not initialize a new AFSiriCapabilitiesClient"
+ "%s Could not set discretionary policy for asset set %{public}@ : %{public}@"
+ "%s Emitting asset set arrived daily status event for auto asset set %{public}@, pre-staged:%d"
+ "%s Emitting daily status scheduled event for asset set %{public}@, pre-staged: %d"
+ "%s Expired Asset Set Token: %{public}@"
+ "%s Expired assets token from %{public}@ does match %{public}@: %{public}@"
+ "%s Expired assets token from %{public}@ does not match %{public}@: %{public}@"
+ "%s Failed to archive expired assets token %{public}@: %{public}@"
+ "%s Failed to create expired assets token dir %{public}@ for token %{public}@: %{public}@"
+ "%s Failed to get expired assets token dir for %{public}@: %{public}@"
+ "%s Failed to get expired assets token dir: %{public}@"
+ "%s Failed to read expired assets token from %{public}@: %{public}@"
+ "%s Failed to remove token at %{public}@: %{public}@"
+ "%s Failed to unarchive expired assets token from %{public}@: %{public}@"
+ "%s Failed to write expired assets token %{public}@ to %{public}@: %{public}@"
+ "%s Force remove of asset set '%{public}@' failed: %@"
+ "%s Generating expired asset set tokens"
+ "%s Invalid Pallas override URL: %{public}@ population: %{public}@"
+ "%s Invalid Pallas server URL: %{public}@ population: %{public}@"
+ "%s Marking token %{public}@ expired completed (error = %{public}@)"
+ "%s Reconfiguration of %{public}@ produced no autoAssetSet"
+ "%s Removal of incompatible asset set %{public}@ complete, reconfiguring"
+ "%s Rollback exclusive transaction of tables creation failed"
+ "%s Rolling back exclusive transaction of tables creation"
+ "%s Setting need policy for asset set '%{public}@' to not user initiated"
+ "%s Setting nil default for Pallas server URL for population %{public}@"
+ "%s Siri IE is now: wants assets: %d, language: %{public}@, mode: %{public}@"
+ "%s Siri configured for: language %{public}@, mode: %{public}@ (assistant enabled: %d, assistant language: %{public}@)"
+ "%s Wrote expired assets token %{public}@ to %{public}@"
+ "%s markAssetsExpired of %{public}@ complete"
+ "%s markAssetsExpired of %{public}@ failed with: %@"
+ "+[UAFAutoAssetManager configureAssetSet:specifiers:changed:downloaded:currentPolicy:]"
+ "+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:]"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke_2"
+ "+[UAFAutoAssetManager releaseIncompatibleAssetSet:specifiers:configuration:]"
+ "+[UAFAutoAssetManager releaseIncompatibleAssetSet:specifiers:configuration:]_block_invoke"
+ "+[UAFAutoAssetManager setBackgroundNeedPolicy:]"
+ "+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:downloaded:experiment:locked:userInitiated:removalNeeded:]"
+ "+[UAFCommonUtilities _setUAFPopulation:forAssetTypes:url:]"
+ "+[UAFCommonUtilities deviceSupportAssistantEngine]"
+ "+[UAFExpiredAssets assetsExpired:error:]"
+ "+[UAFExpiredAssets expiredTokens:]"
+ "+[UAFExpiredAssets loadToken:error:]"
+ "+[UAFExpiredAssets markAssetsExpired:error:]"
+ "+[UAFExpiredAssets removeToken:]"
+ "+[UAFInstrumentationProvider _constructSelfAssetSet:storeManager:]"
+ "-[UAFAssetSetManager markAssetsExpired:completion:]_block_invoke"
+ "-[UAFSubscriptionStoreManager _dropTable:]"
+ "-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke"
+ "-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke_2"
+ "@48@0:8@16@24B32B36@40"
+ "@56@0:8@16@24^B32^B40^@48"
+ "@60@0:8@16@24B32^B36^B44^@52"
+ "AFSiriCapabilitiesServiceClient"
+ "AssetSetTokens"
+ "B72@0:8@16@24B32B36@40^B48^B56^B64"
+ "DROP TABLE IF EXISTS %@"
+ "ExpiredAssetSetTokens"
+ "ExpiredAssets"
+ "UAFExpiredAssets"
+ "URLForDirectory:inDomain:appropriateForURL:create:error:"
+ "Vv32@0:8@\"UAFAssetSetConsistencyToken\"16@?<v@?@\"NSError\">24"
+ "_assistantUsageAliasForMode:"
+ "_currentAssistantMode:"
+ "_dropTable:"
+ "_setUAFPopulation:forAssetTypes:url:"
+ "assetsExpired:error:"
+ "backgroundNeedPolicy"
+ "configureAssetSet:specifiers:changed:downloaded:currentPolicy:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "discretionary"
+ "expiredTokens:"
+ "fromPreSoftwareUpdateStaging"
+ "getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:"
+ "getSpecifiers:assetSetUsages:experiment:"
+ "hasIdenticalAssets:includeBootUUID:"
+ "immediateNeedPolicy"
+ "jsonDictionary"
+ "loadToken:error:"
+ "manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:"
+ "manageGMSSiriLanguageSubscription:language:mode:"
+ "markAssetsExpired:completion:"
+ "markAssetsExpired:error:"
+ "new"
+ "q24@0:8^@16"
+ "releaseIncompatibleAssetSet:specifiers:configuration:"
+ "removeToken:"
+ "setBackgroundNeedPolicy:"
+ "setUAFPopulation:url:"
+ "shouldCheckAssetSet:autoAssetSet:changed:downloaded:experiment:locked:userInitiated:removalNeeded:"
+ "shouldDownloadAssetsForSiriSystemAssistantExperienceSync"
+ "tokenDir:"
+ "tokenFilename:"
+ "uaftoken"
+ "userInitiated"
+ "v36@0:8B16@20q28"
+ "writeToURL:options:error:"
- "%@/%@"
- "%s Emitting asset set arrived daily status event for auto asset set %{public}@:"
- "%s Experimentation not enabled for asset set %{public}@"
- "%s Siri IE is now: wants assets: %d, language: %@"
- "%s Siri configured for: language %{public}@, mode: %{public}@"
- "%s Unexpected experiment file content for Asset Set %{public}@"
- "+[UAFAutoAssetManager configureAssetSet:specifiers:changed:downloaded:]"
- "+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:]"
- "+[UAFAutoAssetManager getSpecifiers:assetSetUsages:disableExperimentation:]"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]_block_invoke"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]_block_invoke_2"
- "+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:downloaded:locked:userInitiated:removalNeeded:]"
- "+[UAFCommonUtilities _setUAFPopulation:forAssetTypes:]"
- "@48@0:8@16@24^B32^B40"
- "@52@0:8@16@24B32^B36^B44"
- "AFDeviceSupportsSAE"
- "B64@0:8@16@24B32B36^B40^B48^B56"
- "_setUAFPopulation:forAssetTypes:"
- "checkResourceIsReachableAndReturnError:"
- "configureAssetSet:specifiers:changed:downloaded:"
- "defaultNeedPolicy"
- "getAutoAssetSet:specifiers:addEntries:configured:downloaded:"
- "getSpecifiers:assetSetUsages:"
- "getSpecifiers:assetSetUsages:disableExperimentation:"
- "initFileURLWithPath:"
- "manageAssetSet:specifiers:lockIfUnchanged:userInitiated:"
- "manageGMSSiriLanguageSubscription:language:"
- "shouldCheckAssetSet:autoAssetSet:changed:downloaded:locked:userInitiated:removalNeeded:"

```
