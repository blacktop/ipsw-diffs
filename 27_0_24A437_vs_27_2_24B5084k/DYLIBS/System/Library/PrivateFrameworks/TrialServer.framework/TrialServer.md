## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

```diff

-511.0.0.0.0
-  __TEXT.__text: 0x14d1cc
+511.1.2.0.0
+  __TEXT.__text: 0x14e3b4
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0x794
   __TEXT.__lazy_helpers: 0xe8
-  __TEXT.__objc_methlist: 0xc7ac
-  __TEXT.__const: 0xeec
+  __TEXT.__objc_methlist: 0xc86c
+  __TEXT.__const: 0xef4
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__cstring: 0x16925
+  __TEXT.__cstring: 0x16ae5
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x1def5
-  __TEXT.__gcc_except_tab: 0x7f28
-  __TEXT.__unwind_info: 0x5060
+  __TEXT.__oslogstring: 0x1e09f
+  __TEXT.__gcc_except_tab: 0x7f74
+  __TEXT.__unwind_info: 0x50c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6938
+  __DATA_CONST.__const: 0x69e8
   __DATA_CONST.__objc_classlist: 0x9c0
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6570
+  __DATA_CONST.__objc_selrefs: 0x65d8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x630
-  __DATA_CONST.__objc_arraydata: 0x388
+  __DATA_CONST.__objc_arraydata: 0x398
   __DATA_CONST.__got: 0x1430
   __AUTH_CONST.__const: 0x1320
-  __AUTH_CONST.__cfstring: 0xee80
-  __AUTH_CONST.__objc_const: 0x182e0
+  __AUTH_CONST.__cfstring: 0xf020
+  __AUTH_CONST.__objc_const: 0x18348
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0xe40
   __AUTH_CONST.__objc_arrayobj: 0x378

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1258
   __AUTH.__data: 0x6e0
-  __DATA.__objc_ivar: 0x968
+  __DATA.__objc_ivar: 0x970
   __DATA.__data: 0x2b40
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x28

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 4979
-  Symbols:   12210
-  CStrings:  4227
+  Functions: 4999
+  Symbols:   12258
+  CStrings:  4253
 
Symbols:
+ -[TRIDServer _handlePowerlogTaskingNotificationWithContext:]
+ -[TRIExternalParameterManager _fetchSafariSearchEngine]
+ -[TRIExternalParameterManager _loadGuardedDataFromCachedDictionary:]
+ -[TRIExternalParameterManager _processSafariSearchEngineBiomeEvent:streamError:]
+ -[TRIExternalParameterManager _subscribeToSafariSearchEngineUpdate]
+ -[TRIExternalParameterManager safariSearchEngine]
+ -[TRIPersistentUserSettings persistActivePowerlogTaskRequestNames:]
+ -[TRIPersistentUserSettings persistedActivePowerlogTaskRequestNames]
+ -[TRISystemConfiguration safariSearchEngine]
+ -[TRISystemConfiguration(Server) activePowerlogTaskRequestNames]
+ -[TRISystemConfiguration(Server) lastPowerlogUploadDate]
+ -[TRISystemInfo _getSafariSearchEngine]
+ -[TRISystemInfo safariSearchEngine]
+ -[TRISystemInfo setSafariSearchEngine:]
+ OBJC_IVAR_$_TRIExternalParameterGuardedData.guardedSafariSearchEngine
+ _CFStringCreateWithCString
+ _OBJC_IVAR_$_TRISystemInfo._safariSearchEngine
+ _TRIPersistentActivePowerlogTaskRequestNames
+ _TRISystemCovariate_ActivePowerlogTaskRequestNames
+ _TRISystemCovariate_DaysSinceLastPowerlogUpload
+ _TRISystemCovariate_SafariSearchEngine
+ __CFPreferencesAppSynchronizeWithContainer
+ __CFPreferencesCopyAppValueWithContainer
+ ___49-[TRIExternalParameterManager safariSearchEngine]_block_invoke
+ ___55-[TRIExternalParameterManager _fetchSafariSearchEngine]_block_invoke
+ ___67-[TRIExternalParameterManager _subscribeToSafariSearchEngineUpdate]_block_invoke
+ ___68-[TRIExternalParameterManager _loadGuardedDataFromCachedDictionary:]_block_invoke
+ ___80-[TRIExternalParameterManager _processSafariSearchEngineBiomeEvent:streamError:]_block_invoke
+ ___block_descriptor_40_e8_32w_e34_v24?0"NSDictionary"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32s40r_e41_v16?0"TRIExternalParameterGuardedData"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e15_"NSString"8?0ls32l8s40l8
+ __powerlogSetting
+ _container_system_group_path_for_identifier
+ _kPowerlogLastUploadDateKey
+ _kPowerlogPreferenceDomain
+ _kPowerlogTaskingRequestsKey
+ _objc_msgSend$_fetchSafariSearchEngine
+ _objc_msgSend$_getSafariSearchEngine
+ _objc_msgSend$_handlePowerlogTaskingNotificationWithContext:
+ _objc_msgSend$_loadGuardedDataFromCachedDictionary:
+ _objc_msgSend$_processSafariSearchEngineBiomeEvent:streamError:
+ _objc_msgSend$_subscribeToSafariSearchEngineUpdate
+ _objc_msgSend$activePowerlogTaskRequestNames
+ _objc_msgSend$lastPowerlogUploadDate
+ _objc_msgSend$persistActivePowerlogTaskRequestNames:
+ _objc_msgSend$persistedActivePowerlogTaskRequestNames
+ _objc_msgSend$readLastDataStreamEventForIdentifier:eventHandler:
+ _objc_msgSend$safariSearchEngine
+ _objc_msgSend$subscribeDataStreamForIdentifier:eventHandler:
- ___54-[TRIExternalParameterManager initWithProvider:paths:]_block_invoke
CStrings:
+ "-[TRIDServer _handlePowerlogTaskingNotificationWithContext:]"
+ "@\"NSString\"8@?0"
+ "ActivePowerlogTaskRequestNames"
+ "DaysSinceLastPowerlogUpload"
+ "Empty event for %@"
+ "Error reading %@ data stream: %{public}@"
+ "External parameter changed, sending SystemInfo update notification."
+ "Failed to look up %{public}s container, error %llu"
+ "Invalid type for %@ event: %{public}@"
+ "PLLastUploadDate"
+ "PLTaskingRequests"
+ "Powerlog tasking notification relevancy: %d"
+ "Reading SafariSearchEngine from Biome."
+ "Safari.SearchEngine"
+ "SafariSearchEngine"
+ "Subscribing to SafariSearchEngine changes from Biome."
+ "TaskedOTA"
+ "TrialXP-511.1.2"
+ "Updaing Safari.SearchEngine to %{public}@"
+ "Update event received for %@."
+ "com.apple.powerlog.tasking_completed"
+ "com.apple.powerlog.tasking_received"
+ "com.apple.powerlogd"
+ "com.apple.triald.persisted.activePowerlogTaskRequestNames"
+ "safariSearchEngine"
+ "searchEngineIdentifier"
+ "systemgroup.com.apple.powerlog"
- "TrialXP-511"
```
