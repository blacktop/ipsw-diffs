## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__common`

```diff

-3600.68.39.1.1
-  __TEXT.__text: 0x36e7c0
-  __TEXT.__auth_stubs: 0x37d0
-  __TEXT.__objc_stubs: 0x47140
-  __TEXT.__objc_methlist: 0x234f8
+3600.68.45.0.0
+  __TEXT.__text: 0x3708a8
+  __TEXT.__auth_stubs: 0x3800
+  __TEXT.__objc_stubs: 0x472e0
+  __TEXT.__objc_methlist: 0x235e8
   __TEXT.__const: 0xed40
   __TEXT.__dlopen_cstrs: 0x99d
   __TEXT.__gcc_except_tab: 0x3a70
-  __TEXT.__cstring: 0x528d7
-  __TEXT.__oslogstring: 0x4575a
-  __TEXT.__objc_classname: 0x51f9
-  __TEXT.__objc_methname: 0x61552
-  __TEXT.__objc_methtype: 0xfed8
+  __TEXT.__cstring: 0x52b52
+  __TEXT.__oslogstring: 0x45808
+  __TEXT.__objc_classname: 0x51d5
+  __TEXT.__objc_methname: 0x61874
+  __TEXT.__objc_methtype: 0xff0f
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0xa468
+  __TEXT.__unwind_info: 0xa4e8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x14338
-  __DATA_CONST.__cfstring: 0x12240
+  __DATA_CONST.__const: 0x143e8
+  __DATA_CONST.__cfstring: 0x12320
   __DATA_CONST.__objc_classlist: 0xd40
   __DATA_CONST.__objc_catlist: 0x630
-  __DATA_CONST.__objc_protolist: 0x730
+  __DATA_CONST.__objc_protolist: 0x728
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0xb10

   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA_CONST.__auth_got: 0x1bf8
+  __DATA_CONST.__auth_got: 0x1c10
   __DATA_CONST.__got: 0x3e80
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x34b48
-  __DATA.__objc_selrefs: 0x154a8
-  __DATA.__objc_ivar: 0x2670
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA.__objc_const: 0x34b30
+  __DATA.__objc_selrefs: 0x15540
+  __DATA.__objc_ivar: 0x267c
   __DATA.__objc_data: 0x8480
-  __DATA.__data: 0x5da0
-  __DATA.__bss: 0xdb0
+  __DATA.__data: 0x5d60
+  __DATA.__bss: 0xdd0
   __DATA.__common: 0xa18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge
   - /System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech
   - /System/Library/PrivateFrameworks/CoreSpeechDataAnalytics.framework/CoreSpeechDataAnalytics
+  - /System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14562
-  Symbols:   2998
-  CStrings:  27784
+  Functions: 14601
+  Symbols:   3001
+  CStrings:  27824
 
Symbols:
+ _ADShouldEmitUEIRequestLinkForRequestId
+ _AFReplayCaptureSentinelURLMake
+ _OBJC_CLASS_$_ODDSiriSchemaODDSiriExtensionProvider
+ __os_crash
+ _snprintf
- _OBJC_CLASS_$_HMMutableHomeManagerConfiguration
- _abort
CStrings:
+ "%s #ODD: siriExtensionProviders count=%lu"
+ "%s #Replay: capturing setReplayCaptureRequested to pending block"
+ "%s #Replay: executing setReplayCaptureRequested"
+ "%s ADOdeonMediaGroupObserver: subscribed to shared media group provider"
+ "%s Could not move %@ aside for async cleanup (%@); removing in place"
+ "%s Logging ORCH→UEI RequestLink for triggerless/server-command reply turn with requestId=%@ turnId=%@"
+ "%s Skipping peer location request based on orchestration mode"
+ "-[ADAssistantProperties _getSiriExtensionProviders]"
+ "-[ADCommandCenter setReplayCaptureRequested:toPath:]_block_invoke"
+ "-[ADCommandCenter(Instrumentation) _logReplyTurnRequestLinkWithSpeechOptions:sessionUUID:]"
+ "-[ADHeadGestureManager _handleDetectedHeadGestureOnQueue:]"
+ "-[ADHeadGestureManager didStartStreamingWithIsStreaming:]_block_invoke"
+ "-[ADMultiUserCloudKitSyncer _deleteHomeMemberShipsFromCloud:]_block_invoke_2"
+ "-[ADOdeonMediaGroupObserver currentMediaGroupsDataProvider:didReceiveCurrentMediaGroup:]_block_invoke"
+ "-[ADOdeonMediaGroupObserver startObserving]_block_invoke_3"
+ ".cleanup-"
+ ".cleanup-%@"
+ "15"
+ "@\"HMCurrentMediaGroupProvider\""
+ "ADCommandCenter.SpeechCaptureCleanupQueue"
+ "MobileAssistantDaemons-3600.68.45"
+ "T@\"HMCurrentMediaGroupProvider\",&,N,V_currentMediaGroupProvider"
+ "Vv28@0:8B16@\"NSURL\"20"
+ "Vv28@0:8B16@20"
+ "_ADCommandCenterMoveSpeechAudioDirectoryAsideForCleanup"
+ "_cleanUpAudioDirectoriesAsynchronously:"
+ "_currentLanguageCodeLock"
+ "_currentMediaGroupProvider"
+ "_existingSharedCommandCenter"
+ "_getSiriExtensionProviders"
+ "_handleDetectedHeadGestureOnQueue:"
+ "_homeManagerOptions"
+ "_logReplyTurnRequestLinkWithSpeechOptions:sessionUUID:"
+ "_observing"
+ "_publishDefaultUserAnalyticsIdUpdateForEphemeralId:"
+ "_remoteDataLock"
+ "_shouldLogReplyTurnRequestLinkForSpeechEvent:"
+ "_test_lockRemoteData"
+ "_test_unlockRemoteData"
+ "_updateAssetManifestCacheOnQueue:"
+ "adRequestSetReplayCaptureRequested:toPath:"
+ "arrayForKey:"
+ "assistantd temp dir init: _set_user_dir_suffix/confstr(_CS_DARWIN_USER_TEMP_DIR) failed: %s"
+ "com.apple.generativepartnerservicesettings"
+ "currentLanguageCode"
+ "homeInfoManagerDidUpdateHomes:"
+ "initForTesting"
+ "initWithLanguageCode:gender:isCustom:name:footprint:contentVersion:masteredVersion:pacePreset:expressivityPreset:"
+ "moveItemAtPath:toPath:error:"
+ "performBlockOnQueueForTesting:"
+ "providerName"
+ "setCurrentLanguageCode:"
+ "setCurrentMediaGroupProvider:"
+ "setIsProviderEnabled:"
+ "setIsProviderInstalled:"
+ "setProviderName:"
+ "setProviders:"
+ "setReplayCaptureRequested:toPath:"
+ "siriExtensionProvidersMetricsSnapshot"
+ "v24@0:8@\"ADHomeInfoManager\"16"
+ "v28@0:8B16@\"NSURL\"20"
- "%s ADOdeonMediaGroupObserver: homeManagerDidUpdateHomes - currentAccessory: %@, home: %@"
- "%s ADOdeonMediaGroupObserver: subscribed to media group provider"
- "%s ADOdeonMediaGroupObserver: triggered provider merge after homes update"
- "%s Failed to initialize temp directory.  errno: %{public}s\n"
- "-[ADHeadGestureManager didDetectedWithHeadGesture:]"
- "-[ADHeadGestureManager didStartStreamingWithIsStreaming:]"
- "-[ADOdeonMediaGroupObserver currentMediaGroupsDataProvider:didReceiveCurrentMediaGroup:]"
- "-[ADOdeonMediaGroupObserver homeManagerDidUpdateHomes:]"
- "2"
- "HMCurrentMediaGroupProviderDelegate"
- "MobileAssistantDaemons-3600.68.39.1.1"
- "T@\"HMHomeManager\",&,N,V_homeManager"
- "_ADEnterSandbox"
- "currentAccessory"
- "homeManager"
- "initWithConfiguration:"
- "initWithOptions:cachePolicy:"
- "isSharedBackedUpMigrationEnabled"
- "setDelegateQueue:"
- "setHomeManager:"
- "v32@0:8@\"HMCurrentMediaGroupProvider\"16@\"HMCurrentMediaGroup\"24"
```
