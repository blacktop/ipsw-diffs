## PhoneNumberResolver

> `/System/Library/PrivateFrameworks/PhoneNumberResolver.framework/PhoneNumberResolver`

```diff

 40.32.10.16.1
-  __TEXT.__text: 0x61fc
-  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__text: 0x5ebc
   __TEXT.__objc_methlist: 0x370
   __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x118
-  __TEXT.__cstring: 0x3c6
+  __TEXT.__gcc_except_tab: 0xdc
+  __TEXT.__cstring: 0x3cf
   __TEXT.__oslogstring: 0x767
   __TEXT.__unwind_info: 0x1c0
-  __TEXT.__objc_classname: 0xa1
-  __TEXT.__objc_methname: 0xeb1
-  __TEXT.__objc_methtype: 0x222
-  __TEXT.__objc_stubs: 0xfc0
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x268
+  __DATA_CONST.__got: 0xf0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x8e0
   __AUTH_CONST.__objc_const: 0x638
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x40
   __DATA.__data: 0x8
   __DATA_DIRTY.__objc_data: 0x1e0

   - /System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D85268A0-FB20-342D-B19D-115B6DA3A0CB
-  Functions: 107
-  Symbols:   562
-  CStrings:  392
+  UUID: 88232BE3-3191-35C2-8953-76C022877FFE
+  Functions: 105
+  Symbols:   556
+  CStrings:  188
 
Symbols:
+ ___60-[PNRPhoneNumberResolver resolvePhoneNumbers:queue:handler:]_block_invoke.70
+ ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.72
+ ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.74
+ ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.74.cold.1
+ ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.78
+ ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.78.cold.1
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x4
+ _objc_retain_x8
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- ___60-[PNRPhoneNumberResolver resolvePhoneNumbers:queue:handler:]_block_invoke.71
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.73
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.75
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.75.cold.1
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.79
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.79.cold.1
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
- ".cxx_destruct"
- "@\"NSCache\""
- "@\"NSDate\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@36@0:8@16B24@28"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16^v24^I32"
- "B16@0:8"
- "B24@0:8@16"
- "I"
- "Internal"
- "PNRPhoneNumberResolutionResult"
- "PNRPhoneNumberResolutionResultSet"
- "PNRPhoneNumberResolver"
- "PNRResourceManager"
- "PNRStringsFileReaderResult"
- "PNRUtils"
- "Q"
- "T@\"NSString\",&,N,V_city"
- "T@\"NSString\",&,N,V_country"
- "T@\"NSString\",&,N,V_region"
- "T@\"NSString\",R,N,V_locationName"
- "Tq,R,N"
- "Tq,R,N,V_dataSource"
- "URLByAppendingPathComponent:"
- "URLForResource:withExtension:"
- "UTF8String"
- "_PNRAssetQueryErrorWithUserInfo:"
- "_PNRAssetUnavailableErrorWithUserInfo:"
- "_PNRBadMagicErrorWithUserInfo:"
- "_PNRNotFoundErrorWithUserInfo:"
- "_URLForInstalledResourceOfType:logId:resultBlock:"
- "_assetQueryForPNRResource:"
- "_bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:"
- "_catalogDownloadFinishedWithResult:"
- "_catalogLoadRetryMultiplier"
- "_city"
- "_country"
- "_currentCountry"
- "_currentLocale"
- "_dataSource"
- "_downloadsInflight"
- "_downloadsInflightLock"
- "_fileDataCache"
- "_getDataFrom:zeroCacheCost:logId:"
- "_isValidPhoneNumber:"
- "_lastCatalogLoadTime"
- "_localizedCountryNameForISOCountryCode:result:"
- "_locationName"
- "_log"
- "_lookupString:inTrieMemory:value:"
- "_maCache"
- "_notAPhoneNumberError"
- "_notFullyQualifiedError"
- "_openLatestAssetWithBasename:maType:logId:resultBlock:"
- "_preferredLanguages"
- "_recordUsageAnalyticForCountryCode:success:"
- "_region"
- "_resolveQueue"
- "_results"
- "_resultsLock"
- "_setLastCatalogLoadTime:"
- "_stateCaptureHandle"
- "_stringByStrippingFormattingAndNotVisiblyAllowable:"
- "_updateCatalog"
- "_updateCatalogAfterDelay:"
- "addEntriesFromDictionary:"
- "addKeyValuePair:with:"
- "addObject:"
- "aggregateStringWhileInCountry:forLanguage:"
- "array"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "attributes"
- "bundleForClass:"
- "bytes"
- "caseInsensitiveCompare:"
- "catalogLoadThen:"
- "characterDirectionForLanguage:"
- "city"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "country"
- "countryCode"
- "currentLocale"
- "dataSource"
- "dataWithContentsOfURL:options:error:"
- "dealloc"
- "description"
- "dictionaryWithCapacity:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "displayNameForKey:value:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateResolutionsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "evaluateWithObject:"
- "getLocalFileUrl"
- "getLocalUrl"
- "groupingSeparator"
- "hasPrefix:"
- "init"
- "initWithBytes:length:encoding:"
- "initWithCountry:region:city:"
- "initWithFormat:"
- "initWithLocationName:locationDataSource:"
- "initWithType:"
- "insertObject:atIndex:"
- "intValue"
- "isEqualTo:"
- "isEqualToString:"
- "isPlaceHolderForEmpty"
- "languageCode"
- "length"
- "locationName"
- "lookupAssetSliceForPhoneNumber:logId:withResult:"
- "lookupISOCountryCodeFromNumber:logId:withResult:"
- "lookupStringForPhoneNumber:inSlice:countryCodeOfDevice:logId:withResult:"
- "maxPossibleScore"
- "mostPreferredLanguageOf:withPreferredLanguages:forUsage:options:"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "openAssetSliceFileUsingLogId:withResult:"
- "openIntlFileUsingLogId:withResult:"
- "openPNRFilesForSlice:logId:withResult:"
- "predicateWithFormat:"
- "preferredLanguages"
- "q"
- "q16@0:8"
- "queryMetaDataSync"
- "region"
- "removeObject:"
- "resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:"
- "resolvePhoneNumber:countryCode:error:"
- "resolvePhoneNumbers:handler:queue:"
- "resolvePhoneNumbers:queue:handler:"
- "returnTypes:"
- "score"
- "separatorForLanguage:"
- "setAllowsCellularAccess:"
- "setAllowsExpensiveAccess:"
- "setCity:"
- "setCountry:"
- "setDiscretionary:"
- "setDoNotBlockBeforeFirstUnlock:"
- "setError:forPhoneNumber:"
- "setName:"
- "setObject:forKey:"
- "setObject:forKey:cost:"
- "setObject:forKeyedSubscript:"
- "setRegion:"
- "setResult:resultDataSource:forPhoneNumber:"
- "setTotalCostLimit:"
- "sharedConfiguration"
- "sharedManager"
- "shouldOrderCityFirstForLanguage:"
- "standardUserDefaults"
- "startAccessingSecurityScopedResource"
- "startCatalogDownload:options:then:"
- "startDownload:then:"
- "state"
- "stopAccessingSecurityScopedResource"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "substringWithRange:"
- "unsignedIntValue"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@?24@32"
- "v40@0:8@16q24@32"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@16@24@32@40@?48"
- "v72@0:8@16@24@32@40@48@56@?64"
- "valueForKey:"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
