## MobileAssetDaemon

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon`

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
-  __TEXT.__text: 0x261884
-  __TEXT.__objc_methlist: 0x12c04
+2215.0.16.0.0
+  __TEXT.__text: 0x262998
+  __TEXT.__objc_methlist: 0x12c54
   __TEXT.__const: 0x15aa
-  __TEXT.__cstring: 0x3f146
-  __TEXT.__oslogstring: 0x5e40d
-  __TEXT.__gcc_except_tab: 0xda84
+  __TEXT.__cstring: 0x3f116
+  __TEXT.__oslogstring: 0x5e7cd
+  __TEXT.__gcc_except_tab: 0xda74
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x146

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
-  __TEXT.__unwind_info: 0x4818
+  __TEXT.__unwind_info: 0x4828
   __TEXT.__eh_frame: 0x10c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaec0
+  __DATA_CONST.__objc_selrefs: 0xaf08
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x358
-  __DATA_CONST.__objc_arraydata: 0xec0
+  __DATA_CONST.__objc_arraydata: 0xef8
   __DATA_CONST.__got: 0x1280
-  __AUTH_CONST.__const: 0x1040
-  __AUTH_CONST.__cfstring: 0x32820
-  __AUTH_CONST.__objc_const: 0x18ed0
-  __AUTH_CONST.__objc_arrayobj: 0x330
+  __AUTH_CONST.__const: 0x1060
+  __AUTH_CONST.__cfstring: 0x32860
+  __AUTH_CONST.__objc_const: 0x18f30
+  __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_intobj: 0x13c8
   __AUTH_CONST.__objc_dictobj: 0x2d0
-  __AUTH_CONST.__auth_got: 0x1210
+  __AUTH_CONST.__auth_got: 0x1228
   __AUTH.__objc_data: 0x878
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x1810
+  __DATA.__objc_ivar: 0x1818
   __DATA.__data: 0x1118
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x550
+  __DATA.__bss: 0x560
   __DATA_DIRTY.__objc_data: 0x2530
   __DATA_DIRTY.__data: 0xa8
   __DATA_DIRTY.__bss: 0x5b0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7268
-  Symbols:   16412
-  CStrings:  10947
+  Functions: 7280
+  Symbols:   16440
+  CStrings:  10960
 
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
+ GCC_except_table156
+ GCC_except_table173
+ GCC_except_table175
+ _AnalyticsCreateSession
+ _AnalyticsEndSession
+ _AnalyticsSendEventWithSession
+ _OBJC_IVAR_$_MADAnalyticsManager._activeSessionId
+ _OBJC_IVAR_$_MADAnalyticsManager._sessionQueue
+ ___46-[MADAnalyticsManager isGMSRelevantAssetType:]_block_invoke
+ ___49-[DownloadManager syncSplunkTasksWithRetryCount:]_block_invoke
+ ___49-[DownloadManager syncSplunkTasksWithRetryCount:]_block_invoke_2
+ ___61-[MADAnalyticsManager _sendViaSessionIfApplicable:assetType:]_block_invoke
+ _isGMSRelevantAssetType:.onceToken
+ _isGMSRelevantAssetType:.types
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
+ _objc_msgSend$syncSplunkTasksWithRetryCount:
- +[MADAutoAssetStager controlAlteredSetConfiguration:]
- -[MADAutoAssetControlManager _logSetConfigurationEntries:forSetConfiguration:]
- -[MADAutoAssetStager action_AlteredDecideSameSetConfiguration:error:]
- ___34-[DownloadManager syncSplunkTasks]_block_invoke
- ___34-[DownloadManager syncSplunkTasks]_block_invoke_2
- _objc_msgSend$_logSetConfigurationEntries:forSetConfiguration:
- _objc_msgSend$action_AlteredDecideSameSetConfiguration:error:
CStrings:
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION-GRAFT-SET] {%{public}@} Recorded locker file for asset being grafted | BundlePath:%{public}@ | LockerPath:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION-GRAFT-SET] {%{public}@} Unable to determine locker file path for secure asset | BundlePath:%{public}@"
+ "%{public}@ {%{public}@}\n[CALCULATE_DOWNLOAD_SPACE] total required space for downloading set | totalRequiredSpace:%lld bytes | finalDownloadPolicy:%d | totalExpectedBytes:%ld | expectedTimeRemainingSecs:%ld | remainingAssetCount:%ld"
+ "Failed to fetch Pallas URL for pallet update mode | error:%{public}@"
+ "Failed to fetch audience for pallet update mode | error:%{public}@"
+ "Loaded built-in MobileAssetDaemon_Framework Jul 11 2026 05:39:25"
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
- "AlteredDecideSameSetConfiguration"
- "ClientAlteredForgetDetermine"
- "ControlAlteredSetConfiguration"
- "Customer In-Box-Updater"
- "Internal In-Box-Updater"
- "Loaded built-in MobileAssetDaemon_Framework Jun 27 2026 04:21:22"
- "MADStager:AlteredDecideSameSetConfiguration"
- "[PallasNonce:%{public}@] Pallas JWS parsing did not yield 3 elements, elements: %lu bytes: %{public}@"
- "cd060049-2465-43e3-bbb5-d769a66da2d7"
- "ffc25f86-b83c-4139-b8ad-91131d0e5429"
- "https://gdmf-auth-stg.apple.com/v2/assets"
- "{controlAlteredSetConfiguration} failed to locate shared AutoAssetStager"
```
