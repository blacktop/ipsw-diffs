## com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

-3303.7.1.0.0
-  __TEXT.__text: 0x48a94
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_stubs: 0x7ca0
-  __TEXT.__objc_methlist: 0x1618
-  __TEXT.__gcc_except_tab: 0x1998
+3304.82.8.1.2
+  __TEXT.__text: 0x46eb0
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_stubs: 0x7b00
+  __TEXT.__objc_methlist: 0x1638
+  __TEXT.__gcc_except_tab: 0x19c8
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x408a
-  __TEXT.__objc_methname: 0x9a36
-  __TEXT.__oslogstring: 0x48c5
-  __TEXT.__objc_classname: 0x1f0
-  __TEXT.__objc_methtype: 0x1857
-  __TEXT.__unwind_info: 0x8b8
-  __DATA_CONST.__auth_got: 0x428
+  __TEXT.__cstring: 0x3f1b
+  __TEXT.__objc_methname: 0x994a
+  __TEXT.__oslogstring: 0x4595
+  __TEXT.__objc_classname: 0x1ef
+  __TEXT.__objc_methtype: 0x18a8
+  __TEXT.__unwind_info: 0x8b0
+  __DATA_CONST.__auth_got: 0x440
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xc08
-  __DATA_CONST.__cfstring: 0x26e0
+  __DATA_CONST.__const: 0xba0
+  __DATA_CONST.__cfstring: 0x2740
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x640
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2bc8
-  __DATA.__objc_selrefs: 0x2250
-  __DATA.__objc_classrefs: 0x628
-  __DATA.__objc_superrefs: 0x58
-  __DATA.__objc_ivar: 0x220
+  __DATA.__objc_const: 0x2ba8
+  __DATA.__objc_selrefs: 0x2248
+  __DATA.__objc_ivar: 0x21c
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x268
   __DATA.__bss: 0x140

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Speech.framework/Speech
   - /System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 634
-  Symbols:   363
-  CStrings:  2340
+  Functions: 643
+  Symbols:   369
+  CStrings:  2320
 
Symbols:
+ _AFBuildVersion
+ _AFDeviceSupportsSiriMUX
+ _AFIsCustomerInstall
+ _AFShouldRunAsrOnServerForUOD
+ _CPSharedResourcesDirectory
+ _OBJC_CLASS_$_CESRGeoLMRegionIDCache
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_CLASS_$_SFEntitledAssetConfig
+ _OBJC_CLASS_$_SFEntitledAssetManager
+ _SFEntitledAssetModelStatusPreferOverServer
+ _SFEntitledAssetTypeToString
+ _SFMappedLocaleForSpeechProfile
- _CESRAssetModelStatusPreferOverServer
- _CESRAssetTypeToString
- _CESRMappedLocaleForSpeechProfile
- _KVLMEDirectories
- _OBJC_CLASS_$_CESRAssetConfig
- _OBJC_CLASS_$_CESRAssetManager
- _OBJC_CLASS_$_CESRTrialAssetManager
- __AFPreferencesBoolValueForKeyWithContext
CStrings:
+ "\x06"
+ "%s Failed to cancel notification %@: %u"
+ "%s Failed to register for %@ update notifications: %u"
+ "%s Failed to resolve UserEx data site directories: %@"
+ "%s Language installation status query failed."
+ "%s Managed data sites: %@"
+ "-[ESAssetManager dealloc]_block_invoke"
+ "@\"SFEntitledAssetConfig\""
+ "CESR"
+ "Default"
+ "Library/Assistant/SiriVocabulary"
+ "Modules"
+ "T@\"NSString\",?,R,C"
+ "UserEx"
+ "Vv32@0:8@\"<CESRAssetConfigProtocol>\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "Vv32@0:8@\"SFEntitledAssetConfig\"16@?<v@?@\"CESRModelProperties\"@\"NSError\">24"
+ "Vv40@0:8@\"SFEntitledAssetConfig\"16@\"NSString\"24@\"NSURL\"32"
+ "_detectDataSites"
+ "_tokenForAssetUpdateNotification"
+ "bestSupportedLanguageCodeForLanguageCode:"
+ "buildVersion"
+ "com.apple.siri.uaf.com.apple.siri.understanding"
+ "config"
+ "currentDictationLanguageCodes"
+ "currentSiriLanguageCode"
+ "fileURLWithPath:isDirectory:relativeToURL:"
+ "isASRSupported"
+ "isAssistantEnabled"
+ "isCustomerInstall"
+ "isDictationEnabled"
+ "isOfflineDictationSupported"
+ "isSiriMuxSupported"
+ "isSiriUODSupported"
+ "isSiriUODwithASROnServerSupported"
+ "purgeUnusedGeoLMAssetsForLanguage:"
+ "purgeUnusedGeoLMRegionIdFromCacheForLanguage:"
+ "purgeUserDefaultsGeoLMAssetsInfoDictForLanguages:"
+ "refreshUnderstandingOnDeviceAssetsAvailableAsync"
+ "updateGeoLMAssetsInfoDictWithRegionId:language:"
+ "{rusage_info_v6=\"ri_uuid\"[16C]\"ri_user_time\"Q\"ri_system_time\"Q\"ri_pkg_idle_wkups\"Q\"ri_interrupt_wkups\"Q\"ri_pageins\"Q\"ri_wired_size\"Q\"ri_resident_size\"Q\"ri_phys_footprint\"Q\"ri_proc_start_abstime\"Q\"ri_proc_exit_abstime\"Q\"ri_child_user_time\"Q\"ri_child_system_time\"Q\"ri_child_pkg_idle_wkups\"Q\"ri_child_interrupt_wkups\"Q\"ri_child_pageins\"Q\"ri_child_elapsed_abstime\"Q\"ri_diskio_bytesread\"Q\"ri_diskio_byteswritten\"Q\"ri_cpu_time_qos_default\"Q\"ri_cpu_time_qos_maintenance\"Q\"ri_cpu_time_qos_background\"Q\"ri_cpu_time_qos_utility\"Q\"ri_cpu_time_qos_legacy\"Q\"ri_cpu_time_qos_user_initiated\"Q\"ri_cpu_time_qos_user_interactive\"Q\"ri_billed_system_time\"Q\"ri_serviced_system_time\"Q\"ri_logical_writes\"Q\"ri_lifetime_max_phys_footprint\"Q\"ri_instructions\"Q\"ri_cycles\"Q\"ri_billed_energy\"Q\"ri_serviced_energy\"Q\"ri_interval_max_phys_footprint\"Q\"ri_runnable_time\"Q\"ri_flags\"Q\"ri_user_ptime\"Q\"ri_system_ptime\"Q\"ri_pinstructions\"Q\"ri_pcycles\"Q\"ri_energy_nj\"Q\"ri_penergy_nj\"Q\"ri_secure_time_in_system\"Q\"ri_secure_ptime_in_system\"Q\"ri_reserved\"[12Q]}"
- "\x02\x14"
- "%s Checking for missing assets."
- "%s Encountered error trying to purge unused assistant ASR assets: %@"
- "%s Error getting installation status: %@"
- "%s Failed to purge unused GeoLM asset, error: %@"
- "%s Failed to register for assistant asset update notifications."
- "%s GeoLM: GeoLM region specific assets deletion is disabled, number of regionIds used till now: %ld"
- "%s GeoLM: Going to delete: %@"
- "%s GeoLM: Last used GeoLM regionId: %@"
- "%s GeoLM: No history of GeoLM usage. regionId: nil"
- "%s GeoLM: language is nil. Skipping."
- "%s GeoLM: regionIdToBePurged: %@, _geoLMAssetsInfoDict count: %ld"
- "%s GeoLM: regionIdToBePurged: %@, lastWhenUsed: %ld days ago"
- "%s GeoLM: supportedLanguages count:%ld"
- "%s Language installation status query failed: %@"
- "%s Not checking for missing assets because ASR has adopted UAF."
- "%s Purging Trial assets failed: %@"
- "%s Purging all assistant ASR assets"
- "%s Purging all assistant ASR assets except for %@"
- "%s Releasing all TRIClients."
- "%s Trial asset delivery disabled for assistant ASR assets. Bailing out of missing asset check."
- "-[ESAssetManager _purgeUserDefaultsGeoLMAssetsInfoDictExceptLanguages:cesrTrialAssetManager:]"
- "-[ESAssetManager _purgeUserDefaultsGeoLMAssetsInfoDictForLanguages:]"
- "-[ESAssetManager lastUsedGeoLMRegionIdForLanguage:]"
- "-[ESAssetManager purgeInstalledAssetsExceptLanguages:assetType:error:]_block_invoke_2"
- "-[ESAssetManager purgeUnusedGeoLMAssetsForLangauge:]_block_invoke"
- "-[ESAssetManager purgeUnusedGeoLMAssetsForLangauge:]_block_invoke_2"
- "-[ESAssetManager startMissingAssetDownload]"
- "."
- "@\"CESRAssetConfig\""
- "Disable GeoLM Deletion"
- "GeoLMAssetsInfo"
- "Vv32@0:8@\"CESRAssetConfig\"16@?<v@?@\"CESRModelProperties\"@\"NSError\">24"
- "Vv32@0:8@\"CESRAssetConfig\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "Vv40@0:8@\"CESRAssetConfig\"16@\"NSString\"24@\"NSURL\"32"
- "_assistantAssetUpdatedNotificationToken"
- "_geoLMAssetsInfoDict"
- "_loadGeoLMAssetsInfoDictForLanguage:"
- "_purgeUserDefaultsGeoLMAssetsInfoDictExceptLanguages:cesrTrialAssetManager:"
- "_purgeUserDefaultsGeoLMAssetsInfoDictForLanguages:"
- "_updateGeoLMAssetsInfoDictWithRegionId:language:"
- "_updateUserDefaultsWithGeoLMAssetsInfoDict:language:"
- "_userDefaultsGeoLMAssetsInfoDictKeyForLanguage:"
- "compare:"
- "dictionaryForKey:"
- "installationStatusForLanguagesForAssetType:includeDetailedStatus:error:"
- "installedAssetWithConfig:regionId:"
- "installedAssetWithConfig:regionId:triggerDownload:"
- "isASRAdoptingUAFEnabled"
- "keysSortedByValueUsingComparator:"
- "purgeInstalledAssetForAssetType:language:regionId:error:"
- "purgeUnusedGeoLMAssetsForLangauge:"
- "q24@?0@8@16"
- "releaseClients"
- "replaceCorruptAssetWithConfig:"
- "standardUserDefaults"
- "stringByAppendingString:"
- "supportedLanguagesWithAssetType:"
- "{rusage_info_v6=\"ri_uuid\"[16C]\"ri_user_time\"Q\"ri_system_time\"Q\"ri_pkg_idle_wkups\"Q\"ri_interrupt_wkups\"Q\"ri_pageins\"Q\"ri_wired_size\"Q\"ri_resident_size\"Q\"ri_phys_footprint\"Q\"ri_proc_start_abstime\"Q\"ri_proc_exit_abstime\"Q\"ri_child_user_time\"Q\"ri_child_system_time\"Q\"ri_child_pkg_idle_wkups\"Q\"ri_child_interrupt_wkups\"Q\"ri_child_pageins\"Q\"ri_child_elapsed_abstime\"Q\"ri_diskio_bytesread\"Q\"ri_diskio_byteswritten\"Q\"ri_cpu_time_qos_default\"Q\"ri_cpu_time_qos_maintenance\"Q\"ri_cpu_time_qos_background\"Q\"ri_cpu_time_qos_utility\"Q\"ri_cpu_time_qos_legacy\"Q\"ri_cpu_time_qos_user_initiated\"Q\"ri_cpu_time_qos_user_interactive\"Q\"ri_billed_system_time\"Q\"ri_serviced_system_time\"Q\"ri_logical_writes\"Q\"ri_lifetime_max_phys_footprint\"Q\"ri_instructions\"Q\"ri_cycles\"Q\"ri_billed_energy\"Q\"ri_serviced_energy\"Q\"ri_interval_max_phys_footprint\"Q\"ri_runnable_time\"Q\"ri_flags\"Q\"ri_user_ptime\"Q\"ri_system_ptime\"Q\"ri_pinstructions\"Q\"ri_pcycles\"Q\"ri_energy_nj\"Q\"ri_penergy_nj\"Q\"ri_reserved\"[14Q]}"

```
