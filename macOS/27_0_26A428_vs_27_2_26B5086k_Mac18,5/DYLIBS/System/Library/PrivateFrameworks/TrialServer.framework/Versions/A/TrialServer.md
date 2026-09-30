## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/Versions/A/TrialServer`

```diff

-511.0.0.0.0
-  __TEXT.__text: 0x165938
+511.1.2.0.0
+  __TEXT.__text: 0x166b48
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0xa28
   __TEXT.__lazy_helpers: 0xe8
-  __TEXT.__objc_methlist: 0xc734
+  __TEXT.__objc_methlist: 0xc7e4
   __TEXT.__const: 0xefc
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__cstring: 0x16e2a
+  __TEXT.__cstring: 0x16fcb
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x1df73
-  __TEXT.__gcc_except_tab: 0x7f0c
-  __TEXT.__unwind_info: 0x5250
+  __TEXT.__oslogstring: 0x1e0ea
+  __TEXT.__gcc_except_tab: 0x7f58
+  __TEXT.__unwind_info: 0x52b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1210
+  __DATA_CONST.__const: 0x1248
   __DATA_CONST.__objc_classlist: 0x9c0
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6540
+  __DATA_CONST.__objc_selrefs: 0x65a0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x630
-  __DATA_CONST.__objc_arraydata: 0x380
-  __DATA_CONST.__got: 0x1430
-  __AUTH_CONST.__const: 0x79d0
-  __AUTH_CONST.__cfstring: 0xf0a0
-  __AUTH_CONST.__objc_const: 0x181e8
+  __DATA_CONST.__objc_arraydata: 0x390
+  __DATA_CONST.__got: 0x1438
+  __AUTH_CONST.__const: 0x7a60
+  __AUTH_CONST.__cfstring: 0xf240
+  __AUTH_CONST.__objc_const: 0x18248
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_arrayobj: 0x360

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x10f0
   __AUTH.__data: 0x6e0
-  __DATA.__objc_ivar: 0x960
+  __DATA.__objc_ivar: 0x968
   __DATA.__data: 0x2ae8
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x20

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 5110
-  Symbols:   12418
-  CStrings:  4252
+  Functions: 5130
+  Symbols:   12464
+  CStrings:  4276
 
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
+ OBJC_IVAR_$_TRISystemInfo._safariSearchEngine
+ _TRIPersistentActivePowerlogTaskRequestNames
+ _TRISystemCovariate_ActivePowerlogTaskRequestNames
+ _TRISystemCovariate_DaysSinceLastPowerlogUpload
+ _TRISystemCovariate_SafariSearchEngine
+ __80-[TRIExternalParameterManager _processSafariSearchEngineBiomeEvent:streamError:]_block_invoke
+ ___49-[TRIExternalParameterManager safariSearchEngine]_block_invoke
+ ___55-[TRIExternalParameterManager _fetchSafariSearchEngine]_block_invoke
+ ___67-[TRIExternalParameterManager _subscribeToSafariSearchEngineUpdate]_block_invoke
+ ___68-[TRIExternalParameterManager _loadGuardedDataFromCachedDictionary:]_block_invoke
+ ___80-[TRIExternalParameterManager _processSafariSearchEngineBiomeEvent:streamError:]_block_invoke
+ ___block_descriptor_40_e8_32w_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_48_e8_32s40r_e41_v16?0"TRIExternalParameterGuardedData"8l
+ ___block_descriptor_48_e8_32s40s_e15_"NSString"8?0l
+ __powerlogSetting
+ _kCFPreferencesAnyHost
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
- "TrialXP-511"
```
