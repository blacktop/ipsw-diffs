## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

```diff

-2333.18.0.8.0
-  __TEXT.__text: 0x19b24
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x10cc
-  __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x1375
-  __TEXT.__oslogstring: 0x16e7
-  __TEXT.__gcc_except_tab: 0x768
-  __TEXT.__unwind_info: 0x530
-  __TEXT.__objc_classname: 0x131
-  __TEXT.__objc_methname: 0x2b6b
-  __TEXT.__objc_methtype: 0x4af
-  __TEXT.__objc_stubs: 0x2da0
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x3c0
-  __DATA_CONST.__objc_classlist: 0x70
+2333.7.0.1.0
+  __TEXT.__text: 0x222a4
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x13e8
+  __TEXT.__const: 0xc8
+  __TEXT.__gcc_except_tab: 0x95c
+  __TEXT.__cstring: 0x1692
+  __TEXT.__oslogstring: 0x1a2c
+  __TEXT.__unwind_info: 0x758
+  __TEXT.__objc_classname: 0x1b4
+  __TEXT.__objc_methname: 0x321d
+  __TEXT.__objc_methtype: 0x57f
+  __TEXT.__objc_stubs: 0x32e0
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0x960
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdc0
-  __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x970
-  __AUTH_CONST.__auth_got: 0x2d0
-  __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x3ba0
-  __AUTH_CONST.__objc_const: 0x1730
+  __DATA_CONST.__objc_selrefs: 0xf28
+  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_arraydata: 0x980
+  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x3d80
+  __AUTH_CONST.__objc_const: 0x1e98
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_ivar: 0x130
-  __DATA.__data: 0x180
-  __DATA.__bss: 0x58
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x178
+  __DATA.__data: 0x310
+  __DATA.__bss: 0xf0
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__data: 0xc8
-  __DATA_DIRTY.__bss: 0x240
+  __DATA_DIRTY.__bss: 0x220
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec
   - /System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices
   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
+  - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 493
-  Symbols:   682
-  CStrings:  1291
+  Functions: 689
+  Symbols:   932
+  CStrings:  1464
 
Symbols:
+ _OBJC_CLASS_$_CSXPCConnection
+ _OBJC_CLASS_$_MAAsset
+ _OBJC_CLASS_$_SRAssertion
+ _OBJC_CLASS_$_SRAssetBundleCache
+ _OBJC_CLASS_$_SRAssetBundleCacheEntry
+ _OBJC_CLASS_$_SRAssetBundleQuery
+ _OBJC_CLASS_$_SRLanguageConfiguration
+ _OBJC_CLASS_$_SRXPCConnection
+ _OBJC_CLASS_$_SRXPCListener
+ _OBJC_METACLASS_$_CSXPCConnection
+ _OBJC_METACLASS_$_SRAssertion
+ _OBJC_METACLASS_$_SRAssetBundleCache
+ _OBJC_METACLASS_$_SRAssetBundleCacheEntry
+ _OBJC_METACLASS_$_SRAssetBundleQuery
+ _OBJC_METACLASS_$_SRLanguageConfiguration
+ _OBJC_METACLASS_$_SRXPCConnection
+ _OBJC_METACLASS_$_SRXPCListener
+ _SRGetResourcePath
+ _SRIsRunningInServer
+ _SRLogCategoryAssets
+ _SRLogCategoryTrial
+ __xpc_error_connection_interrupted
+ __xpc_error_connection_invalid
+ __xpc_runtime_is_app_sandboxed
+ __xpc_type_array
+ __xpc_type_dictionary
+ _assetTypeID
+ _assetTypeString
+ _assetUUIDFromPath
+ _deliveryTypeID
+ _deliveryTypeString
+ _dispatch_activate
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _dispatch_queue_create_with_target$V2
+ _dispatch_workloop_create
+ _getContentVersionFromPath
+ _objc_retainAutoreleasedReturnValue
+ _xpc_array_append_value
+ _xpc_array_apply
+ _xpc_array_create_empty
+ _xpc_connection_send_message
+ _xpc_connection_send_message_with_reply
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_array
+ _xpc_dictionary_get_int64
+ _xpc_dictionary_get_remote_connection
+ _xpc_dictionary_get_string
+ _xpc_dictionary_get_uint64
+ _xpc_dictionary_get_value
+ _xpc_dictionary_set_int64
+ _xpc_dictionary_set_string
+ _xpc_dictionary_set_uint64
+ _xpc_dictionary_set_value
+ _xpc_get_type
- __dispatch_main_q
- _dispatch_group_async
- _objc_retain_x27
CStrings:
+ "\x05"
+ "\x06\x12\x17"
+ "\x14"
+ "!!"
+ "%@\nSupported Languages:\n%@\nCache:\n%@\n"
+ "%@/assetBundleCache.plist"
+ "%@:%@:%@:%@"
+ "%s does not exist at %s"
+ "%s does not exist at path <%s>"
+ "(%ld, %s)"
+ "(%llu, %@) for asset (%@, %@, %@)"
+ "(AssetServerInit) configure asset type: %s (%lu)"
+ "(AssetServerInit) configuring asset type: %s (%lu)"
+ "(_loadAssets) loading asset: %s, %s, %s, %s"
+ "(_loadAssets) skipping over asset: %s, %s"
+ "(_unloadAssetsForLocale) unloading assets for locale: %s"
+ "(assertions) (version %ld) removing assertion: %s"
+ "(assertions) adding assertion : %s"
+ "(assertions) keeping assertion : %s"
+ "(assertions) removing assertion : %s"
+ "(fetchedLanguages) add fetch for language: %s"
+ "(fetchedLanguages) remove fetch for language: %s"
+ "(fetchedLanguages) update fetched languages: %@ --> %@"
+ "(forceLoad) Failed to get assets from server: %@"
+ "(forceLoad) Got asset bundles from server for %s"
+ "(forceLoad) Sending query to server for %s"
+ "/var/mobile/Library/Spotlight/Assets"
+ "9999.99.99"
+ ":"
+ "@\"SRLanguageConfiguration\""
+ "@32@0:8@16B24B28"
+ "@36@0:8@16@24B32"
+ "@40@0:8@16B24@28B36"
+ "@40@0:8q16@24q32"
+ "Add query entry (%@, %@, %@)"
+ "Asset bundle (%@, %@, %@) at %@ is not a directory"
+ "Asset bundle (%@, %@, %@) does not exist at path %@"
+ "AssetAddedProperties"
+ "AssetId"
+ "AssetPurpose"
+ "AssetState"
+ "Assets"
+ "B24@?0Q8@\"NSObject<OS_xpc_object>\"16"
+ "B32@0:8Q16@24"
+ "ContentVersion"
+ "Error fetching content version from %@"
+ "Error handling message: %@"
+ "Error loading asset properties: %@"
+ "Error loading cache %@"
+ "Error refreshing cache for languages %@: %@"
+ "Error writing to cache: %@"
+ "Failed to get assets from server: %@"
+ "Failed to set up client connection"
+ "Got asset bundles from server for %s"
+ "Got updated assets from DDS for %s"
+ "Handle message %p"
+ "Has SRA roots installed, setting content version to 9999 for %@"
+ "Invalid asset type %@ for (%@, %@)"
+ "Invalid assetType %@ for %@"
+ "Invalid assetType %@ in cache"
+ "Invalid assetType %@ in cache file"
+ "Invalid delivery type %@ for (%@, %@)"
+ "Invalid deliveryType %@ in cache"
+ "Invalid deliveryType %@ in cache file"
+ "Invalid query entry type %d"
+ "Invalid query type %d"
+ "LinguisticAssetType"
+ "Loading %s at path <%s>"
+ "Loading RequiredAssets_root at path <%s>"
+ "Malformed assertionID %@"
+ "No assets for (%@, %@, %@)"
+ "Null content version for asset (%@, %@, %@)"
+ "Null path for asset bundle (%@, %@, %@)"
+ "Parser"
+ "Path"
+ "Q"
+ "Refreshed cache for %@"
+ "Refreshing cache!"
+ "Reply for message[%llu] = %p"
+ "SRAssertion"
+ "SRAssetBundleCache"
+ "SRAssetBundleCacheEntry"
+ "SRAssetBundleQuery"
+ "SRLanguageConfiguration"
+ "SRResources dealloc (%@, %@): %p"
+ "SRResources init (%@, %@): %p"
+ "SRXPCConnection"
+ "SRXPCListener"
+ "Sandboxed client"
+ "Sending message[%llu] = %p"
+ "Sending query to server for %s"
+ "Should not refresh cache in Spotlight daemon"
+ "T@\"NSMutableDictionary\",R,N,V_queryEntries"
+ "T@\"NSMutableSet\",R,N,V_cachedOTALanguages"
+ "T@\"NSMutableSet\",R,N,V_requestedOTALanguages"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_notifyQueue"
+ "T@\"NSString\",R,N,V_assetType"
+ "T@\"NSString\",R,N,V_deliveryType"
+ "T@\"NSString\",R,N,V_language"
+ "T@\"NSString\",R,N,V_path"
+ "TB,R,N,V_isResult"
+ "TQ,R,N,V_contentVersion"
+ "Tq,R,N,V_assetType"
+ "Unknown asset type %ld"
+ "_assertionID"
+ "_cache"
+ "_cachedOTALanguages"
+ "_contentVersion"
+ "_contentVersions"
+ "_fetchedLanguages"
+ "_isResult"
+ "_isSR"
+ "_langConfig"
+ "_language"
+ "_loadAssets:shouldUpdate:"
+ "_loadedContentVersions"
+ "_notifyQueue"
+ "_path"
+ "_queryEntries"
+ "_queue"
+ "_requestedOTALanguages"
+ "_supportedLanguageMap"
+ "a"
+ "addFetchForLanguage:"
+ "addQueryEntriesForLanguage:assetType:deliveryTypes:"
+ "assertionID"
+ "assetBundleForLocale:client:force:"
+ "assetTypeString"
+ "assets"
+ "assetsForQuery:error:"
+ "cacheFilePath"
+ "cachedOTALanguages"
+ "code"
+ "com.apple.MobileAsset.LinguisticData"
+ "com.apple.spotlight.IndexAgent"
+ "com.apple.spotlight.resources.assetsQuery.queue"
+ "com.apple.spotlight.resources.assetsQuery.workloop"
+ "com.apple.spotlightresources.notifyDelegates"
+ "command"
+ "componentsSeparatedByString:"
+ "connection"
+ "d"
+ "default_factors_%@.pb"
+ "deliveryTypeString"
+ "didUpdateDefaultsWithLanguage:contentVersions:trial:"
+ "dumpCache"
+ "e"
+ "enumerateEntriesForLanguage:block:"
+ "fetchAllParametersForLanguages:"
+ "fetchedLanguages"
+ "flushCacheToFile"
+ "getLocalFileUrl"
+ "handleAssetsCommand:"
+ "handleMessage:error:"
+ "initWithAssertionID:"
+ "initWithAssetType:language:deliveryType:"
+ "initWithAttributes:"
+ "initWithDomain:code:userInfo:"
+ "initWithLocale:contentVersions:"
+ "initWithMachServiceName:"
+ "initWithXPCObject:isResult:"
+ "intValue"
+ "isResult"
+ "isResultNone"
+ "isSupportedLanguage:deliveryType:"
+ "l"
+ "language"
+ "loadCacheFromFile"
+ "loadDefaultsForLocale:reload:force:"
+ "loadOTAAssetsForLanguage:reload:assetTypes:force:"
+ "loadOTA[%llu] (%@, %d, %d, %@)"
+ "loadOTA[%llu] client 1"
+ "loadOTA[%llu] client 2"
+ "loadOTA[%llu] client 2.1"
+ "loadOTA[%llu] client 2.2"
+ "loadOTA[%llu] client 2.3"
+ "loadOTA[%llu] client 3"
+ "loadOTA[%llu] client 3.1"
+ "loadOTA[%llu] client 3.2"
+ "loadOTA[%llu] client 3.3"
+ "loadOTA[%llu] load"
+ "loadOTA[%llu] server 1"
+ "loadOTA[%llu] server 2"
+ "loadOTA[%llu] server 2.1"
+ "loadOTA[%llu] server 3"
+ "loadOTA[%llu] server 3.1"
+ "loadOTA[%llu] server 3.2"
+ "loadSupportedLanguages:"
+ "loadSystemAssetsForLanguage:assetTypes:"
+ "loadTestAssetsForLanguage:assetTypes:"
+ "localURL"
+ "makeResultNone"
+ "makeResultWithContentVersion:path:"
+ "notifyObserversWithLanguage:contentVersions:"
+ "notifyQueue"
+ "numberWithUnsignedInteger:"
+ "numberWithUnsignedLongLong:"
+ "objectAtIndexedSubscript:"
+ "p"
+ "qi"
+ "queryCache:"
+ "queryEntries"
+ "queryServerCache:completion:"
+ "refreshCacheForLanguages:completion:"
+ "removeAssetBundleWithAssetType:language:deliveryType:"
+ "requestAssets update for %@"
+ "requestedOTALanguages"
+ "resourcePath"
+ "ri"
+ "sendMessageAsync:completion:"
+ "setLatestOnly:"
+ "sharedConnection"
+ "shouldReloadLanguage:forContentVersions:"
+ "shouldUpdateForContentVersions:"
+ "stringByDeletingLastPathComponent"
+ "stringByDeletingPathExtension"
+ "stringWithUTF8String:"
+ "unsignedIntegerValue"
+ "updateCacheWithResults:"
+ "updateContentVersions:forLanguage:"
+ "updateFetchedLanguages:"
+ "upsertAssetBundleWithAssetType:language:deliveryType:contentVersion:path:"
+ "v"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "v16@?0@\"SRAssetBundleCacheEntry\"8"
+ "v24@?0@\"NSString\"8^B16"
+ "v24@?0@\"SRAssetBundleQuery\"8@\"NSError\"16"
+ "v32@0:8@16@?24"
+ "v32@0:8@16^@24"
+ "v32@?0@\"DDSAsset\"8Q16^B24"
+ "v32@?0@\"NSNumber\"8Q16^B24"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
+ "v32@?0@\"NSString\"8@\"SRAssetBundleCacheEntry\"16^B24"
+ "v36@0:8@\"NSString\"16@\"NSDictionary\"24B32"
+ "v56@0:8@16@24@32Q40@48"
+ "xpcObject"
- "\x02"
- "\x05\x12\x14"
- "\x06"
- "%@/locales.plist"
- "(forceLoad on) Error fetching assets for query (%s, %s, %s): %@"
- "(forceLoad on) Invalid dds asset (%@, %@, %@, %@)"
- "(forceLoad on) Not fetching asset with type %s for deliveryType %s"
- "(forceLoad=off) type %@, deliveryType %@"
- "(forceLoad=on) type %@, deliveryType %@"
- "."
- "Copy supported locales from %@ to %@"
- "Error fetching assets for query (%s, %s, %s): %@"
- "Invalid dds asset (%@, %@, %@, %@)"
- "Not fetching asset with type %s for deliveryType %s"
- "SRResources dealloc (%@, %@)"
- "SRResources init (%@, %@)"
- "SRSafetyDDSForceLoad"
- "SRSafetyDDSLoad"
- "SpotlightResources:%@:%@"
- "SpotlightResources:%@:%@:%@"
- "Supported locales copy from %@ to %@ failed with %@"
- "TB,N,V_forceLoad"
- "[SR_INFO][DefaultsManager] (AssetServerInit) configure asset type: %s (%lu)"
- "[SR_INFO][DefaultsManager] (_loadAssets) loading asset: %s, %s, %s, %s"
- "[SR_INFO][DefaultsManager] (_loadAssets) skipping over asset: %s, %s"
- "[SR_INFO][DefaultsManager] (_unloadAssetsForLocale) unloading assets for locale: %s"
- "[SR_INFO][DefaultsManager] (addAssertionWithIdentifier) adding assertion: %s"
- "[SR_INFO][DefaultsManager] (addAssertionWithIdentifier) keeping assertion: %s"
- "[SR_INFO][DefaultsManager] (addFetchForLocale) asset fetch for locale: %s"
- "[SR_INFO][DefaultsManager] (fetchedLocales) update fetched locales: %@ --> %@"
- "[SR_INFO][DefaultsManager] (removeAssertionWithIdentifier) (%ld) removing assertion: %s"
- "[SR_INFO][DefaultsManager] (removeAssertionWithIdentifier) removing assertion: %s"
- "[SR_INFO][DefaultsManager] (removeFetchForLanguage) remove asset fetch for language: %s"
- "[SR_INFO][DefaultsManager] (removeFetchForLocale) remove asset fetch for locale: %s"
- "[SR_INFO][DefaultsManager] did update assets with type %s"
- "[SR_INFO][DefaultsManager] loading assets at path <%s>"
- "[SR_INFO][DefaultsManager] loading defaults at path <%s>"
- "_fetchedLocales"
- "_loadAssets:deliveryType:shouldUpdate:"
- "_localeMap"
- "_localesVersion"
- "_supportedLocalesPath"
- "addFetchForLocale:"
- "allContentItemsMatchingQuery:error:"
- "assetBundleForLocale:client:"
- "copyItemAtURL:toURL:error:"
- "deliveryTypeFromString:"
- "deliveryTypeString:"
- "fetchAllParametersForLanguages:resourcePath:"
- "fetchedLocales"
- "fileName"
- "initWithLocale:"
- "isValidLocale:deliveryType:"
- "loadDefaultsForLocale:reload:"
- "loadSupportedLocalesFromFile:"
- "loc:%s, v:%lu"
- "localeMap: %@\n"
- "notifyObservers"
- "parentAsset"
- "removeFetchForLocale:"
- "requestAssetsForLanguages:resourcePath:"
- "setByAddingObject:"
- "setForceLoad:"
- "setLocales:"
- "setOptions:"
- "supportedLocalesVersion"
- "updateFetchedLocales:"

```
