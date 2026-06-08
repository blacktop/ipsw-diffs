## MorphunAssets

> `/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets`

```diff

-3520.51.1.0.0
-  __TEXT.__text: 0x935c
-  __TEXT.__auth_stubs: 0x3e0
+3600.29.1.0.0
+  __TEXT.__text: 0x8a58
   __TEXT.__objc_methlist: 0x410
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x7e0
-  __TEXT.__cstring: 0xd0a
+  __TEXT.__cstring: 0xd0e
+  __TEXT.__gcc_except_tab: 0x77c
   __TEXT.__oslogstring: 0x1035
-  __TEXT.__unwind_info: 0x328
-  __TEXT.__objc_classname: 0x70
-  __TEXT.__objc_methname: 0xeb0
-  __TEXT.__objc_methtype: 0x12e
-  __TEXT.__objc_stubs: 0x1100
-  __DATA_CONST.__got: 0xf8
+  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x278
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c8
+  __DATA_CONST.__objc_selrefs: 0x4c0
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x208
+  __DATA_CONST.__got: 0xf0
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x740
   __AUTH_CONST.__objc_const: 0x328
+  __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x8
+  __DATA.__data: 0x10
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x68
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 52550EEE-9C68-3255-8FE8-46CAB29267FF
-  Functions: 147
-  Symbols:   642
-  CStrings:  408
+  UUID: 5282B31C-4B6E-3F74-A62E-126935B6800E
+  Functions: 145
+  Symbols:   636
+  CStrings:  219
 
Symbols:
+ GCC_except_table48
+ __ZNSt3__16__treeIN7morphun4util7ULocaleENS_4lessIS3_EENS_9allocatorIS3_EEE14__tree_deleterclB9fqe220100EPNS_11__tree_nodeIS3_PvEE
+ __ZSt9terminatev
+ ___71+[MorphunAssets onDemandDownloadForLocale:withProgress:withCompletion:]_block_invoke.393
+ ___71+[MorphunAssets onDemandDownloadForLocale:withProgress:withCompletion:]_block_invoke.395
+ ___71+[MorphunAssets onDemandDownloadForLocale:withProgress:withCompletion:]_block_invoke.398
+ ___block_literal_global.414
+ ___block_literal_global.417
+ ___block_literal_global.422
+ ___block_literal_global.437
+ ___clang_call_terminate
+ ___cxa_begin_catch
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- GCC_except_table52
- _OBJC_CLASS_$_UAFAssetSetObserver
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- ___71+[MorphunAssets onDemandDownloadForLocale:withProgress:withCompletion:]_block_invoke.372
- ___71+[MorphunAssets onDemandDownloadForLocale:withProgress:withCompletion:]_block_invoke.374
- ___71+[MorphunAssets onDemandDownloadForLocale:withProgress:withCompletion:]_block_invoke.377
- ___block_literal_global.393
- ___block_literal_global.396
- ___block_literal_global.401
- ___block_literal_global.416
- _objc_msgSend$initWithAssetSet:queue:updateHandler:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x28
CStrings:
- ".cxx_destruct"
- "@\"NSLock\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSUserDefaults\""
- "@\"UAFAssetSetObserver\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8r^v16"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@40@0:8@16Q24@?32"
- "B24@0:8@16"
- "B40@0:8@16@24@32"
- "EmbeddedLanguages"
- "EmbeddedLocales"
- "EmbeddedVersion"
- "MorphunAssetsLazyInitIfNeeded"
- "MorphunAssetsPrivate"
- "MorphunAssetsSubscription"
- "MorphunAssetsUtilities"
- "MorphunDomain"
- "NSSafeMutableDictionary"
- "Q16@0:8"
- "SupportedLanguages"
- "SupportedLocales"
- "SupportedSiriLanguages"
- "SupportedSiriLocales"
- "T@\"NSLock\",&,VsubscriptionViewLock"
- "T@\"NSMutableDictionary\",&,N,VsubscriptionView"
- "T@\"NSMutableDictionary\",&,VreadyLanguages"
- "T@\"NSString\",&,N,VsubscriptionProcessKey"
- "T@\"NSUserDefaults\",&,N,VsubscriptionCache"
- "T@\"UAFAssetSetObserver\",&,N,V_subscriptionAssetSetObserver"
- "URLWithString:"
- "_lock"
- "_storage"
- "_subscriptionAssetSetObserver"
- "absoluteString"
- "addObject:"
- "allObjects"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "assetNamed:"
- "assetPathDB"
- "bcpStringForComponentArray:"
- "bcpStringForLocale:"
- "blockingOnDemandDownloadForLocale:withTimeout:withProgress:"
- "blockingRemoveAssetForLocale:withTimeout:"
- "boolValue"
- "bundleWithIdentifier:"
- "canUpdateExistingAssetSet:withNewAssetSet:forUsageValue:"
- "compareVersion:"
- "componentArrayForLocale:"
- "componentsSeparatedByString:"
- "configFileValueForKey:"
- "configurationFromPropertiesFile:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryCode"
- "date"
- "deliveryMethodForLocale:"
- "dictionaryForKey:"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjects:forKeys:count:"
- "downloadLocaleIfNeeded:withCompletion:"
- "embeddedLanguages"
- "embeddedPath"
- "errorWithDomain:code:userInfo:"
- "get"
- "getAssetPathForCurrentSiriLanguage"
- "getAssetPathForLocale:"
- "getAssetPathForLocale:withError:"
- "getFactorNameForLocale:"
- "getFactorSuffixForLocale:"
- "getMorphunDataPathForLocale:"
- "getMorphunDataPathForLocale:withError:"
- "getUAFAssetForLocale:"
- "getUAFAssetName"
- "getUAFAssetSetForUsageValue:"
- "getUAFAssetSetName"
- "getUAFAssetSets"
- "getUAFUsageType"
- "getUAFUsageValueForLocale:"
- "i24@0:8@16"
- "init"
- "initForSiriX:"
- "initWithArray:"
- "initWithAssetSet:queue:updateHandler:"
- "initWithCharacters:length:"
- "initWithDictionary:"
- "initWithDomain:code:userInfo:"
- "initWithLocaleIdentifier:"
- "initWithName:assetSets:usageAliases:"
- "initWithObjects:forKeys:"
- "initWithString:"
- "initWithSuiteName:"
- "intValue"
- "isAssetReadyForLocale:"
- "isEqualToString:"
- "isLocaleDownloadSupported:"
- "isLocaleEmbedded:"
- "isSubscribedToLocale:"
- "keyEnumerator"
- "languageCode"
- "length"
- "libmorphunVersion"
- "listSubscriptions"
- "localeIdentifier"
- "localeWithLocaleIdentifier:"
- "localizedDescription"
- "location"
- "lock"
- "matchesInString:options:range:"
- "metadata"
- "name"
- "null"
- "numberWithBool:"
- "numberWithUnsignedInt:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeAssetSet:queue:handler:"
- "observeUAFAssetSet"
- "onDemandDownloadForLocale:withProgress:withCompletion:"
- "path"
- "pathForResource:ofType:"
- "processInfo"
- "processName"
- "processSubscriptions"
- "q24@0:8@16"
- "rangeAtIndex:"
- "readSubscriptionView"
- "readyLanguages"
- "referenceCountsFromSubscriptionView"
- "regularExpressionWithPattern:options:error:"
- "removeAllObjects"
- "removeAssetForLocale:withCompletion:"
- "removeLanguageIfNeeded:"
- "removeLastObject"
- "removeObject:"
- "removeObjectForKey:"
- "retrieveAssetSet:usages:"
- "scriptCode"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setReadyLanguages:"
- "setSubscriptionAssetSetObserver:"
- "setSubscriptionCache:"
- "setSubscriptionProcessKey:"
- "setSubscriptionView:"
- "setSubscriptionViewLock:"
- "sharedManager"
- "sharedPreferences"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringWithContentsOfFile:encoding:error:"
- "stringWithFormat:"
- "subscribe:subscriptions:queue:completion:"
- "subscribeToLocale:withCompletion:"
- "subscriptionAssetSetObserver"
- "subscriptionCache"
- "subscriptionDbInitializerWithKey:"
- "subscriptionProcessKey"
- "subscriptionView"
- "subscriptionViewLock"
- "subscriptionsForSubscriber:"
- "substringWithRange:"
- "timeIntervalSinceNow"
- "uLocaleToNSLocale:"
- "unlock"
- "unsignedIntValue"
- "unsubscribe:subscriptionNames:queue:completion:"
- "unsubscribeFromLocale:"
- "updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:"
- "updateUAFAssetSetForUsageValue:"
- "userSiriXLocales"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@16@?24@?32"
- "validateLanguageCode:"
- "validateLocale:"
- "writeSubscriptionView"

```
