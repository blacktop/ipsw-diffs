## InternationalSupport

> `/System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport`

```diff

-85.201.0.0.0
-  __TEXT.__text: 0x46ac
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0x2b4
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x1c24
-  __TEXT.__ustring: 0x286c
+85.310.0.0.0
+  __TEXT.__text: 0x7238
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_methlist: 0x5e4
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x1e26
+  __TEXT.__ustring: 0x2c0c
+  __TEXT.__gcc_except_tab: 0x8c
+  __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__oslogstring: 0xf0
-  __TEXT.__unwind_info: 0x148
-  __TEXT.__objc_classname: 0x2c
-  __TEXT.__objc_methname: 0xd26
-  __TEXT.__objc_methtype: 0x11b
-  __TEXT.__objc_stubs: 0xbc0
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__objc_classlist: 0x8
+  __TEXT.__unwind_info: 0x218
+  __TEXT.__objc_classname: 0x6e
+  __TEXT.__objc_methname: 0x16f6
+  __TEXT.__objc_methtype: 0x21a
+  __TEXT.__objc_stubs: 0x1360
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__const: 0x180
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x70
-  __DATA_CONST.__objc_selrefs: 0x3d8
-  __DATA_CONST.__objc_arraydata: 0x9b30
-  __AUTH_CONST.__cfstring: 0xdbe0
-  __AUTH_CONST.__objc_dictobj: 0x2c10
-  __AUTH_CONST.__objc_arrayobj: 0x1ce0
+  __DATA_CONST.__objc_const: 0x478
+  __DATA_CONST.__objc_selrefs: 0x670
+  __DATA_CONST.__objc_classrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_arraydata: 0x9dd8
+  __AUTH_CONST.__cfstring: 0xe020
+  __AUTH_CONST.__objc_dictobj: 0x2c88
+  __AUTH_CONST.__objc_arrayobj: 0x1d10
+  __AUTH_CONST.__objc_const: 0x230
   __AUTH_CONST.__objc_doubleobj: 0x350
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__objc_const: 0xc8
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x218
-  __DATA.__objc_classrefs: 0x70
-  __DATA.__bss: 0x58
+  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x50
+  __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D240E2CB-0C74-3677-8313-95E836C8020F
-  Functions: 62
-  Symbols:   391
-  CStrings:  3090
+  UUID: C521E5EE-2C9D-36D4-9D4F-C6927E46631E
+  Functions: 151
+  Symbols:   732
+  CStrings:  3284
 
Symbols:
+ +[ISLanguageCarousel guessedRegion]
+ +[ISLanguageCarousel rankedItemsFromItems:usingSystemLanguages:preferredLanguages:region:]
+ +[ISLanguageCarousel rankedItemsFromItems:usingSystemLanguages:preferredLanguages:region:].cold.1
+ +[ISLanguageCarousel rankedItemsFromItems:usingSystemLanguages:preferredLanguages:region:].cold.2
+ +[ISRegionDetector sharedRegionDetector]
+ +[NSLocale(InternationalSupportExtensions) _displayNameForNormalizedLanguage:context:displayLanguage:length:isGreenTea:]
+ -[ISLanguageCarousel .cxx_destruct]
+ -[ISLanguageCarousel allItems]
+ -[ISLanguageCarousel cycle]
+ -[ISLanguageCarousel initWithItems:]
+ -[ISLanguageCarousel items]
+ -[ISLanguageCarousel mergeDuplicates]
+ -[ISLanguageCarousel nextItem]
+ -[ISLanguageCarousel queueIndex]
+ -[ISLanguageCarousel queue]
+ -[ISLanguageCarousel randomize]
+ -[ISLanguageCarousel rankedItemsUsingPreferredLanguages:guessedRegion:]
+ -[ISLanguageCarousel rankingUsesGuessedRegion]
+ -[ISLanguageCarousel rankingUsesPreferredLanguages]
+ -[ISLanguageCarousel reloadQueue]
+ -[ISLanguageCarousel setCycle:]
+ -[ISLanguageCarousel setItems:]
+ -[ISLanguageCarousel setMergeDuplicates:]
+ -[ISLanguageCarousel setQueue:]
+ -[ISLanguageCarousel setQueueIndex:]
+ -[ISLanguageCarousel setRandomize:]
+ -[ISLanguageCarousel setRankingUsesGuessedRegion:]
+ -[ISLanguageCarousel setRankingUsesPreferredLanguages:]
+ -[ISLanguageCarousel setWeightedRepetition:]
+ -[ISLanguageCarousel weightedRepetition]
+ -[ISLanguageCarouselItem .cxx_destruct]
+ -[ISLanguageCarouselItem data]
+ -[ISLanguageCarouselItem description]
+ -[ISLanguageCarouselItem initWithLanguageIdentifier:data:]
+ -[ISLanguageCarouselItem initWithLocale:data:]
+ -[ISLanguageCarouselItem languageIdentifier]
+ -[ISLanguageCarouselItem locale]
+ -[ISLanguageCarouselItem setData:]
+ -[ISLanguageCarouselItem setLanguageIdentifier:]
+ -[ISRegionDetector .cxx_destruct]
+ -[ISRegionDetector _checkForAliases:]
+ -[ISRegionDetector _checkForAliasesOrInvalid:]
+ -[ISRegionDetector _checkedArrayForString:]
+ -[ISRegionDetector _closeWifiConnection]
+ -[ISRegionDetector _closeWifiConnection].cold.1
+ -[ISRegionDetector _countryFromTelephony]
+ -[ISRegionDetector _getWifiDevice]
+ -[ISRegionDetector _getWifiDevice].cold.1
+ -[ISRegionDetector _getWifiDevice].cold.2
+ -[ISRegionDetector _scanComplete:error:]
+ -[ISRegionDetector _scanComplete:error:].cold.1
+ -[ISRegionDetector _scanWifiListWithDevice:]
+ -[ISRegionDetector _scanWifiList]
+ -[ISRegionDetector _scanWifiList].cold.1
+ -[ISRegionDetector _startWifiScan]
+ -[ISRegionDetector _startWifiScan].cold.1
+ -[ISRegionDetector _startWifiScan].cold.2
+ -[ISRegionDetector _startWifiScan].cold.3
+ -[ISRegionDetector dealloc]
+ -[ISRegionDetector fakeMode]
+ -[ISRegionDetector firstGuessedLanguages]
+ -[ISRegionDetector getCountryFromTelephony]
+ -[ISRegionDetector guessedCountries]
+ -[ISRegionDetector guessedCountryFromTelephony]
+ -[ISRegionDetector guessedLanguages]
+ -[ISRegionDetector init]
+ -[ISRegionDetector numberOfWiFiScanAttemptsRemaining]
+ -[ISRegionDetector reset]
+ -[ISRegionDetector setFakeMode:]
+ -[ISRegionDetector setFirstGuessedLanguages:]
+ -[ISRegionDetector setGuessedCountries:]
+ -[ISRegionDetector setNumberOfWiFiScanAttemptsRemaining:]
+ -[ISRegionDetector setWirelessScanStartDate:]
+ -[ISRegionDetector wirelessScanStartDate]
+ GCC_except_table10
+ GCC_except_table12
+ GCC_except_table14
+ GCC_except_table17
+ GCC_except_table18
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _CFGetTypeID
+ _CFRelease
+ _CFRetain
+ _CFRunLoopGetCurrent
+ _LanguageNameOverrides_GreenTea
+ _MGGetBoolAnswer
+ _MobileWiFiLibrary
+ _MobileWiFiLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_CoreTelephonyClient
+ _OBJC_CLASS_$_ISLanguageCarousel
+ _OBJC_CLASS_$_ISLanguageCarouselItem
+ _OBJC_CLASS_$_ISRegionDetector
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_IVAR_$_ISLanguageCarousel._cycle
+ _OBJC_IVAR_$_ISLanguageCarousel._items
+ _OBJC_IVAR_$_ISLanguageCarousel._mergeDuplicates
+ _OBJC_IVAR_$_ISLanguageCarousel._queue
+ _OBJC_IVAR_$_ISLanguageCarousel._queueIndex
+ _OBJC_IVAR_$_ISLanguageCarousel._randomize
+ _OBJC_IVAR_$_ISLanguageCarousel._rankingUsesGuessedRegion
+ _OBJC_IVAR_$_ISLanguageCarousel._rankingUsesPreferredLanguages
+ _OBJC_IVAR_$_ISLanguageCarousel._weightedRepetition
+ _OBJC_IVAR_$_ISLanguageCarouselItem._data
+ _OBJC_IVAR_$_ISLanguageCarouselItem._languageIdentifier
+ _OBJC_IVAR_$_ISRegionDetector._fakeMode
+ _OBJC_IVAR_$_ISRegionDetector._firstGuessedLanguages
+ _OBJC_IVAR_$_ISRegionDetector._guessedCountries
+ _OBJC_IVAR_$_ISRegionDetector._guessedCountryFromTelephony
+ _OBJC_IVAR_$_ISRegionDetector._numberOfWiFiScanAttemptsRemaining
+ _OBJC_IVAR_$_ISRegionDetector._validCountries
+ _OBJC_IVAR_$_ISRegionDetector._wirelessScanStartDate
+ _OBJC_IVAR_$_ISRegionDetector.fWifiDevice
+ _OBJC_IVAR_$_ISRegionDetector.fWifiManager
+ _OBJC_METACLASS_$_ISLanguageCarousel
+ _OBJC_METACLASS_$_ISLanguageCarouselItem
+ _OBJC_METACLASS_$_ISRegionDetector
+ __Block_object_dispose
+ __OBJC_$_CLASS_METHODS_ISLanguageCarousel
+ __OBJC_$_CLASS_METHODS_ISRegionDetector
+ __OBJC_$_INSTANCE_METHODS_ISLanguageCarousel
+ __OBJC_$_INSTANCE_METHODS_ISLanguageCarouselItem
+ __OBJC_$_INSTANCE_METHODS_ISRegionDetector
+ __OBJC_$_INSTANCE_VARIABLES_ISLanguageCarousel
+ __OBJC_$_INSTANCE_VARIABLES_ISLanguageCarouselItem
+ __OBJC_$_INSTANCE_VARIABLES_ISRegionDetector
+ __OBJC_$_PROP_LIST_ISLanguageCarousel
+ __OBJC_$_PROP_LIST_ISLanguageCarouselItem
+ __OBJC_$_PROP_LIST_ISRegionDetector
+ __OBJC_CLASS_RO_$_ISLanguageCarousel
+ __OBJC_CLASS_RO_$_ISLanguageCarouselItem
+ __OBJC_CLASS_RO_$_ISRegionDetector
+ __OBJC_METACLASS_RO_$_ISLanguageCarousel
+ __OBJC_METACLASS_RO_$_ISLanguageCarouselItem
+ __OBJC_METACLASS_RO_$_ISRegionDetector
+ __Unwind_Resume
+ ___33-[ISRegionDetector _scanWifiList]_block_invoke
+ ___90+[ISLanguageCarousel rankedItemsFromItems:usingSystemLanguages:preferredLanguages:region:]_block_invoke
+ ___MobileWiFiLibraryCore_block_invoke
+ ___assert_rtn
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32s_e39_B32?0"ISLanguageCarouselItem"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e5_v8?0l
+ ___block_literal_global.274
+ ___getWiFiDeviceClientGetTypeIDSymbolLoc_block_invoke
+ ___getWiFiDeviceClientScanAsyncSymbolLoc_block_invoke
+ ___getWiFiManagerClientCopyDevicesSymbolLoc_block_invoke
+ ___getWiFiManagerClientCreateSymbolLoc_block_invoke
+ ___getWiFiManagerClientRegisterDeviceAttachmentCallbackSymbolLoc_block_invoke
+ ___getWiFiManagerClientScheduleWithRunLoopSymbolLoc_block_invoke
+ ___getWiFiManagerClientUnscheduleFromRunLoopSymbolLoc_block_invoke
+ ___getWiFiNetworkGet11dCountryCodeFromIeSymbolLoc_block_invoke
+ ___objc_personality_v0
+ ___wifidDidBecomeAlive_block_invoke
+ __dispatch_main_q
+ __sl_dlopen
+ __unnamed_array_storage.249
+ __unnamed_array_storage.252
+ __unnamed_array_storage.8
+ __unnamed_array_storage.9
+ _abort_report_np
+ _arc4random_uniform
+ _audit_stringMobileWiFi
+ _dispatch_after
+ _dispatch_time
+ _dlerror
+ _dlsym
+ _free
+ _getWiFiDeviceClientGetTypeIDSymbolLoc.ptr
+ _getWiFiDeviceClientScanAsyncSymbolLoc.ptr
+ _getWiFiManagerClientCopyDevicesSymbolLoc.ptr
+ _getWiFiManagerClientCreateSymbolLoc.ptr
+ _getWiFiManagerClientRegisterDeviceAttachmentCallbackSymbolLoc.ptr
+ _getWiFiManagerClientScheduleWithRunLoopSymbolLoc.ptr
+ _getWiFiManagerClientUnscheduleFromRunLoopSymbolLoc.ptr
+ _getWiFiNetworkGet11dCountryCodeFromIeSymbolLoc.ptr
+ _kCFAllocatorDefault
+ _kCFRunLoopCommonModes
+ _objc_msgSend$_checkForAliases:
+ _objc_msgSend$_checkForAliasesOrInvalid:
+ _objc_msgSend$_checkedArrayForString:
+ _objc_msgSend$_closeWifiConnection
+ _objc_msgSend$_countryFromTelephony
+ _objc_msgSend$_displayNameForNormalizedLanguage:context:displayLanguage:length:isGreenTea:
+ _objc_msgSend$_getWifiDevice
+ _objc_msgSend$_scanComplete:error:
+ _objc_msgSend$_scanWifiList
+ _objc_msgSend$_scanWifiListWithDevice:
+ _objc_msgSend$_startWifiScan
+ _objc_msgSend$allObjects
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$canonicalLocaleIdentifierFromString:
+ _objc_msgSend$copyMobileCountryCode:error:
+ _objc_msgSend$copyMobileSubscriberIsoCountryCode:error:
+ _objc_msgSend$countForObject:
+ _objc_msgSend$cycle
+ _objc_msgSend$data
+ _objc_msgSend$date
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$getCountryFromTelephony
+ _objc_msgSend$getSubscriptionInfoWithError:
+ _objc_msgSend$guessedCountries
+ _objc_msgSend$guessedRegion
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$initWithBytes:length:encoding:
+ _objc_msgSend$initWithLanguageIdentifier:data:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$items
+ _objc_msgSend$lastObject
+ _objc_msgSend$numberOfWiFiScanAttemptsRemaining
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$preferredLanguages
+ _objc_msgSend$queue
+ _objc_msgSend$queueIndex
+ _objc_msgSend$randomize
+ _objc_msgSend$rankedItemsFromItems:usingSystemLanguages:preferredLanguages:region:
+ _objc_msgSend$rankedItemsUsingPreferredLanguages:guessedRegion:
+ _objc_msgSend$rankingUsesGuessedRegion
+ _objc_msgSend$rankingUsesPreferredLanguages
+ _objc_msgSend$reloadQueue
+ _objc_msgSend$removeLastObject
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$replaceObjectsInRange:withObjectsFromArray:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$setCycle:
+ _objc_msgSend$setData:
+ _objc_msgSend$setFirstGuessedLanguages:
+ _objc_msgSend$setGuessedCountries:
+ _objc_msgSend$setItems:
+ _objc_msgSend$setLanguageIdentifier:
+ _objc_msgSend$setNumberOfWiFiScanAttemptsRemaining:
+ _objc_msgSend$setQueue:
+ _objc_msgSend$setQueueIndex:
+ _objc_msgSend$setWeightedRepetition:
+ _objc_msgSend$setWirelessScanStartDate:
+ _objc_msgSend$sharedRegionDetector
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$subscriptionsInUse
+ _objc_msgSend$valueForKey:
+ _objc_msgSendSuper2
+ _objc_opt_isKindOfClass
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x26
+ _objc_retain_x4
+ _objc_storeStrong
+ _scanComplete
+ _sharedRegionDetector.sharedInstance
+ _wifidDidBecomeAlive
+ _wifidDidBecomeAlive.onceToken
- ___block_literal_global.268
- __unnamed_array_storage.246
CStrings:
+ "\x02"
+ "\x032"
+ "\x12"
+ "%s"
+ "+[ISLanguageCarousel rankedItemsFromItems:usingSystemLanguages:preferredLanguages:region:]"
+ ", language = %@, data = %@"
+ ".cxx_destruct"
+ "@"
+ "@\"NSArray\""
+ "@\"NSDate\""
+ "@\"NSSet\""
+ "@\"NSString\""
+ "@24@0:8B16B20"
+ "@48@0:8@16@24@32@40"
+ "@52@0:8@16q24@32Q40B48"
+ "B16@0:8"
+ "B32@?0@\"ISLanguageCarouselItem\"8Q16^B24"
+ "BYCountryScanCompletedNotification"
+ "CS"
+ "Chinese (Mandarin - Taiwan [China])"
+ "ISLanguageCarousel"
+ "ISLanguageCarousel.m"
+ "ISLanguageCarouselItem"
+ "ISRegionDetector"
+ "LanguageNameOverrides_GreenTea.plist"
+ "ME"
+ "Q"
+ "Q16@0:8"
+ "RS"
+ "T@\"NSArray\",&,N,V_firstGuessedLanguages"
+ "T@\"NSArray\",&,N,V_guessedCountries"
+ "T@\"NSArray\",&,N,V_items"
+ "T@\"NSArray\",&,N,V_queue"
+ "T@\"NSDate\",&,N,V_wirelessScanStartDate"
+ "T@\"NSLocale\",R,N"
+ "T@\"NSString\",&,N,V_languageIdentifier"
+ "T@,&,N,V_data"
+ "TB,N,V_cycle"
+ "TB,N,V_fakeMode"
+ "TB,N,V_mergeDuplicates"
+ "TB,N,V_randomize"
+ "TB,N,V_rankingUsesGuessedRegion"
+ "TB,N,V_rankingUsesPreferredLanguages"
+ "TB,N,V_weightedRepetition"
+ "TQ,N,V_numberOfWiFiScanAttemptsRemaining"
+ "TQ,N,V_queueIndex"
+ "WiFiDeviceClientGetTypeID"
+ "WiFiDeviceClientScanAsync"
+ "WiFiManagerClientCopyDevices"
+ "WiFiManagerClientCreate"
+ "WiFiManagerClientRegisterDeviceAttachmentCallback"
+ "WiFiManagerClientScheduleWithRunLoop"
+ "WiFiManagerClientUnscheduleFromRunLoop"
+ "WiFiNetworkGet11dCountryCodeFromIe"
+ "^{__WiFiDeviceClient=}"
+ "^{__WiFiManagerClient=}"
+ "_checkForAliases:"
+ "_checkForAliasesOrInvalid:"
+ "_checkedArrayForString:"
+ "_closeWifiConnection"
+ "_countryFromTelephony"
+ "_cycle"
+ "_data"
+ "_displayNameForNormalizedLanguage:context:displayLanguage:length:isGreenTea:"
+ "_fakeMode"
+ "_firstGuessedLanguages"
+ "_getWifiDevice"
+ "_guessedCountries"
+ "_guessedCountryFromTelephony"
+ "_items"
+ "_languageIdentifier"
+ "_mergeDuplicates"
+ "_numberOfWiFiScanAttemptsRemaining"
+ "_queue"
+ "_queueIndex"
+ "_randomize"
+ "_rankingUsesGuessedRegion"
+ "_rankingUsesPreferredLanguages"
+ "_scanComplete:error:"
+ "_scanWifiList"
+ "_scanWifiListWithDevice:"
+ "_startWifiScan"
+ "_validCountries"
+ "_weightedRepetition"
+ "_wirelessScanStartDate"
+ "allItems"
+ "allObjects"
+ "arrayWithObject:"
+ "canonicalLocaleIdentifierFromString:"
+ "copyMobileCountryCode:error:"
+ "copyMobileSubscriberIsoCountryCode:error:"
+ "countForObject:"
+ "cycle"
+ "data"
+ "date"
+ "dealloc"
+ "defaultCenter"
+ "description"
+ "fWifiDevice"
+ "fWifiManager"
+ "fakeMode"
+ "firstGuessedLanguages"
+ "getCountryFromTelephony"
+ "getSubscriptionInfoWithError:"
+ "green-tea"
+ "guessedCountries"
+ "guessedCountryFromTelephony"
+ "guessedLanguages"
+ "guessedRegion"
+ "indexOfObjectPassingTest:"
+ "init"
+ "initWithBytes:length:encoding:"
+ "initWithItems:"
+ "initWithLanguageIdentifier:data:"
+ "initWithLocale:data:"
+ "initWithQueue:"
+ "items"
+ "languages.count > 0"
+ "lastObject"
+ "locale"
+ "mergeDuplicates"
+ "nextItem"
+ "numberOfWiFiScanAttemptsRemaining"
+ "postNotificationName:object:"
+ "preferred.count > 0"
+ "preferredLanguages"
+ "queue"
+ "queueIndex"
+ "randomize"
+ "rankedItemsFromItems:usingSystemLanguages:preferredLanguages:region:"
+ "rankedItemsUsingPreferredLanguages:guessedRegion:"
+ "rankingUsesGuessedRegion"
+ "rankingUsesPreferredLanguages"
+ "reloadQueue"
+ "removeLastObject"
+ "removeObjectAtIndex:"
+ "replaceObjectsInRange:withObjectsFromArray:"
+ "reset"
+ "reverseObjectEnumerator"
+ "s"
+ "setCycle:"
+ "setData:"
+ "setFakeMode:"
+ "setFirstGuessedLanguages:"
+ "setGuessedCountries:"
+ "setItems:"
+ "setLanguageIdentifier:"
+ "setMergeDuplicates:"
+ "setNumberOfWiFiScanAttemptsRemaining:"
+ "setQueue:"
+ "setQueueIndex:"
+ "setRandomize:"
+ "setRankingUsesGuessedRegion:"
+ "setRankingUsesPreferredLanguages:"
+ "setWeightedRepetition:"
+ "setWirelessScanStartDate:"
+ "sharedRegionDetector"
+ "sjd-Cyrl"
+ "sje-Latn"
+ "sju-Latn"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi"
+ "stringByAppendingFormat:"
+ "subscriptionsInUse"
+ "v16@0:8"
+ "v20@0:8B16"
+ "v24@0:8@16"
+ "v24@0:8Q16"
+ "v24@0:8^{__WiFiDeviceClient=}16"
+ "v28@0:8@16B24"
+ "valueForKey:"
+ "weightedRepetition"
+ "wirelessScanStartDate"
+ "\x8eN؞\xa9\x85s|\x87e"
+ "\xaevyr\xa9\x85s|\x87e"
+ "\xfaW>r\x01N\xa9\x85s|\x87e"
- "Kildin Sami"
- "Kildin sami"
- "Pite Sami"
- "Pite sami"
- "Sami di Kildin"
- "Sami di Pite"
- "Sami di Skolt"
- "Sami di Ume"
- "Ume Sami"
- "Ume sami"
- "sami kildin"
- "sami pite"
- "sami ume"
- "\x8eN؞\xa9\x85s|\x9e\x8a"
- "\xaevyr\xa9\x85s|\x9e\x8a"
- "\xfaW>r\x01N\xa9\x85s|\x9e\x8a"

```
