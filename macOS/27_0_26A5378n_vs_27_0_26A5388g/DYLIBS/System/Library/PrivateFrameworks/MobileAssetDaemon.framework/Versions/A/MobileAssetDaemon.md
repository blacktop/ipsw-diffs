## MobileAssetDaemon

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/Versions/A/MobileAssetDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2215.0.13.0.0
-  __TEXT.__text: 0x285090
-  __TEXT.__objc_methlist: 0x12a04
+2215.0.16.0.0
+  __TEXT.__text: 0x286318
+  __TEXT.__objc_methlist: 0x12a54
   __TEXT.__const: 0x155a
-  __TEXT.__cstring: 0x3ed82
-  __TEXT.__oslogstring: 0x5c937
-  __TEXT.__gcc_except_tab: 0xd874
+  __TEXT.__cstring: 0x3ed22
+  __TEXT.__oslogstring: 0x5cce7
+  __TEXT.__gcc_except_tab: 0xd864
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x146
   __TEXT.__swift5_fieldmd: 0x3c

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x4560
+  __TEXT.__unwind_info: 0x4578
   __TEXT.__eh_frame: 0x10c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xacf0
+  __DATA_CONST.__objc_selrefs: 0xad40
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x358
-  __DATA_CONST.__objc_arraydata: 0xed0
+  __DATA_CONST.__objc_arraydata: 0xf08
   __DATA_CONST.__got: 0x11f0
-  __AUTH_CONST.__const: 0x3250
-  __AUTH_CONST.__cfstring: 0x32540
-  __AUTH_CONST.__objc_const: 0x18aa8
-  __AUTH_CONST.__objc_arrayobj: 0x330
+  __AUTH_CONST.__const: 0x3270
+  __AUTH_CONST.__cfstring: 0x32560
+  __AUTH_CONST.__objc_const: 0x18b08
+  __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_intobj: 0x13b0
   __AUTH_CONST.__objc_dictobj: 0x2d0
-  __AUTH_CONST.__auth_got: 0x1140
+  __AUTH_CONST.__auth_got: 0x1158
   __AUTH.__objc_data: 0x828
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x17d8
+  __DATA.__objc_ivar: 0x17e0
   __DATA.__data: 0x1058
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x550
+  __DATA.__bss: 0x560
   __DATA_DIRTY.__objc_data: 0x2530
   __DATA_DIRTY.__data: 0xa8
   __DATA_DIRTY.__bss: 0x568

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7319
-  Symbols:   16438
-  CStrings:  10835
+  Functions: 7331
+  Symbols:   16465
+  CStrings:  10847
 
Symbols:
+ +[DownloadManager getAssetAudienceForPalletUpdateMode:]
+ +[DownloadManager getPallasServerURLForPalletUpdateMode:]
+ -[DownloadManager syncSplunkTasksWithRetryCount:]
+ -[MADAnalyticsManager _sendViaSessionIfApplicable:assetType:]
+ -[MADAnalyticsManager activeSessionId]
+ -[MADAnalyticsManager isGMSRelevantAssetType:]
+ -[MADAnalyticsManager sessionQueue]
+ -[MADAnalyticsManager setActiveSessionId:]
+ -[MADAnalyticsManager setSessionQueue:]
+ -[MADAutoAssetControlManager _logSetConfigurationEntries:forSetConfiguration:issuingDebugLog:]
+ GCC_except_table164
+ GCC_except_table166
+ GCC_except_table223
+ GCC_except_table229
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table237
+ OBJC_IVAR_$_MADAnalyticsManager._activeSessionId
+ OBJC_IVAR_$_MADAnalyticsManager._sessionQueue
+ _AnalyticsCreateSession
+ _AnalyticsEndSession
+ _AnalyticsSendEventWithSession
+ __49-[DownloadManager syncSplunkTasksWithRetryCount:]_block_invoke
+ ___46-[MADAnalyticsManager isGMSRelevantAssetType:]_block_invoke
+ ___49-[DownloadManager syncSplunkTasksWithRetryCount:]_block_invoke
+ ___49-[DownloadManager syncSplunkTasksWithRetryCount:]_block_invoke_2
+ ___61-[MADAnalyticsManager _sendViaSessionIfApplicable:assetType:]_block_invoke
+ _objc_msgSend$_logSetConfigurationEntries:forSetConfiguration:issuingDebugLog:
+ _objc_msgSend$_sendViaSessionIfApplicable:assetType:
+ _objc_msgSend$activeSessionId
+ _objc_msgSend$assetAudienceID:
+ _objc_msgSend$getAssetAudienceForPalletUpdateMode:
+ _objc_msgSend$getPallasServerURLForPalletUpdateMode:
+ _objc_msgSend$isGMSRelevantAssetType:
+ _objc_msgSend$pallasServerURL:
+ _objc_msgSend$sessionQueue
+ _objc_msgSend$setActiveSessionId:
+ _objc_msgSend$stringByResolvingSymlinksInPath
+ _objc_msgSend$syncSplunkTasksWithRetryCount:
+ isGMSRelevantAssetType:.onceToken
+ isGMSRelevantAssetType:.types
- +[MADAutoAssetStager controlAlteredSetConfiguration:]
- -[MADAutoAssetControlManager _logSetConfigurationEntries:forSetConfiguration:]
- -[MADAutoAssetStager action_AlteredDecideSameSetConfiguration:error:]
- GCC_except_table197
- GCC_except_table199
- GCC_except_table217
- GCC_except_table225
- GCC_except_table226
- GCC_except_table232
- GCC_except_table35
- ___34-[DownloadManager syncSplunkTasks]_block_invoke
- ___34-[DownloadManager syncSplunkTasks]_block_invoke_2
- _objc_msgSend$_logSetConfigurationEntries:forSetConfiguration:
- _objc_msgSend$action_AlteredDecideSameSetConfiguration:error:
CStrings:
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION-GRAFT-SET] {%{public}@} Recorded locker file for asset being grafted | BundlePath:%{public}@ | LockerPath:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION-GRAFT-SET] {%{public}@} Unable to determine locker file path for secure asset | BundlePath:%{public}@"
+ "%{public}@ {%{public}@}\n[CALCULATE_DOWNLOAD_SPACE] total required space for downloading set | totalRequiredSpace:%lld bytes | finalDownloadPolicy:%d | totalExpectedBytes:%ld | expectedTimeRemainingSecs:%ld | remainingAssetCount:%ld"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7wLoja/Sources/MobileAssetDaemon/ControlManager.m"
+ "Failed to fetch Pallas URL for pallet update mode | error:%{public}@"
+ "Failed to fetch audience for pallet update mode | error:%{public}@"
+ "Loaded built-in MobileAssetDaemon_Framework Jul 16 2026 00:53:23"
+ "Max retries exhausted. Giving up on state sync"
+ "Overriding config for pallet update mode | AssetAudience:%{public}@"
+ "Pallet mode override"
+ "Retrying sync of splunk state"
+ "Splunk session object not yet set up. Defering state sync"
+ "Successful"
+ "UAF.FM.Overrides"
+ "UAF.FM.Visual"
+ "[AUTO-SECURE][AUTO-GRAFT] Recorded locker file for asset being grafted | BundlePath:%{public}@ | LockerPath:%{public}@"
+ "[AUTO-SECURE][AUTO-GRAFT]: Asset being grafted has no locker file | BundlePath:%{public}@"
+ "[CoreAnalytics-Session] AnalyticsCreateSession returned nil"
+ "[CoreAnalytics-Session] Ended session: %{public}@"
+ "[CoreAnalytics-Session] Started session: %{public}@"
+ "[PallasNonce:%{public}@] Pallas JWS parsing did not yield 3 elements, elements: %lu"
+ "com.apple.mobileassetd.analyticsSessionQueue"
+ "if.planner"
+ "if.planner.overrides"
+ "modelcatalog"
+ "siri.understanding"
+ "siri.understanding.nl.overrides"
- "%{public}@ {%{public}@}\n[CALCULATE_DOWNLOAD_SPACE] total required space for downloading set | totalRequiredSpace:%lld bytes | finalDownloadPolicy:%d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ndbIMJ/Sources/MobileAssetDaemon/ControlManager.m"
- "6153ec74-f683-41d2-b6ba-66c230cd26ff"
- "AlteredDecideSameSetConfiguration"
- "ClientAlteredForgetDetermine"
- "ControlAlteredSetConfiguration"
- "Customer In-Box-Updater"
- "Internal In-Box-Updater"
- "Loaded built-in MobileAssetDaemon_Framework Jun 27 2026 02:59:40"
- "MADStager:AlteredDecideSameSetConfiguration"
- "[PallasNonce:%{public}@] Pallas JWS parsing did not yield 3 elements, elements: %lu bytes: %{public}@"
- "c1617c00-2852-4f4e-8581-3456811ab23b"
- "https://gdmf-auth-stg.apple.com/v2/assets"
- "https://gdmf-auth.apple.com/v2/assets"
- "{controlAlteredSetConfiguration} failed to locate shared AutoAssetStager"
```
