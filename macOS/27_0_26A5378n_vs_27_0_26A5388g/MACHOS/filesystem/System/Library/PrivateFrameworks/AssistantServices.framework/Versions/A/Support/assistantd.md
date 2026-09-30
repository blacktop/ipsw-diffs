## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd`

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
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-3600.68.39.0.0
-  __TEXT.__text: 0x536904
-  __TEXT.__auth_stubs: 0x31b0
-  __TEXT.__objc_stubs: 0x42220
-  __TEXT.__objc_methlist: 0x2168c
-  __TEXT.__cstring: 0x49a2a
+3600.68.44.0.0
+  __TEXT.__text: 0x5316c4
+  __TEXT.__auth_stubs: 0x31d0
+  __TEXT.__objc_stubs: 0x42360
+  __TEXT.__objc_methlist: 0x2175c
+  __TEXT.__cstring: 0x49b42
   __TEXT.__const: 0xa2ec0
   __TEXT.__dlopen_cstrs: 0x56f
   __TEXT.__gcc_except_tab: 0x30a0
-  __TEXT.__oslogstring: 0x3e42a
-  __TEXT.__objc_classname: 0x4ded
-  __TEXT.__objc_methname: 0x5ad2e
-  __TEXT.__objc_methtype: 0xeb60
+  __TEXT.__oslogstring: 0x3e3e0
+  __TEXT.__objc_classname: 0x4dc9
+  __TEXT.__objc_methname: 0x5b084
+  __TEXT.__objc_methtype: 0xeb97
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0x95e8
+  __TEXT.__unwind_info: 0x96b8
   __TEXT.__eh_frame: 0x140
-  __DATA_CONST.__const: 0x22ff0
-  __DATA_CONST.__cfstring: 0x11280
+  __DATA_CONST.__const: 0x231d0
+  __DATA_CONST.__cfstring: 0x11360
   __DATA_CONST.__objc_classlist: 0xcb0
   __DATA_CONST.__objc_catlist: 0x630
-  __DATA_CONST.__objc_protolist: 0x6a8
+  __DATA_CONST.__objc_protolist: 0x6a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0xa98

   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA_CONST.__auth_got: 0x18e8
-  __DATA_CONST.__got: 0x39b8
+  __DATA_CONST.__auth_got: 0x18f8
+  __DATA_CONST.__got: 0x39b0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x31fc8
-  __DATA.__objc_selrefs: 0x13c78
-  __DATA.__objc_ivar: 0x245c
+  __DATA.__objc_const: 0x32000
+  __DATA.__objc_selrefs: 0x13d00
+  __DATA.__objc_ivar: 0x2470
   __DATA.__objc_data: 0x7ee0
-  __DATA.__data: 0x5a38
-  __DATA.__bss: 0x9a8
-  __DATA.__common: 0x1420
+  __DATA.__data: 0x5af8
+  __DATA.__bss: 0x9b8
+  __DATA.__common: 0x1428
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13759
-  Symbols:   2752
-  CStrings:  25533
+  Functions: 13804
+  Symbols:   2753
+  CStrings:  25567
 
Symbols:
+ _AFReplayCaptureSentinelURLMake
+ _OBJC_CLASS_$_ODDSiriSchemaODDSiriExtensionProvider
+ _dispatch_block_create
- _OBJC_CLASS_$_HMMutableHomeManagerConfiguration
- _OBJC_CLASS_$_NSOperationQueue
CStrings:
+ "%s #ODD: siriExtensionProviders count=%lu"
+ "%s #Replay: capturing setReplayCaptureRequested to pending block"
+ "%s #Replay: executing setReplayCaptureRequested"
+ "%s Could not move %@ aside for async cleanup (%@); removing in place"
+ "-[ADAssistantProperties _getSiriExtensionProviders]"
+ "-[ADCommandCenter setReplayCaptureRequested:toPath:]_block_invoke"
+ "-[ADHeadGestureManager _handleDetectedHeadGestureOnQueue:]"
+ "-[ADHeadGestureManager didStartStreamingWithIsStreaming:]_block_invoke"
+ "-[ADOdeonMediaGroupObserver currentMediaGroupsDataProvider:didReceiveCurrentMediaGroup:]_block_invoke"
+ ".cleanup-"
+ ".cleanup-%@"
+ "22"
+ "@\"HMCurrentMediaGroupProvider\""
+ "ADCommandCenter.SpeechCaptureCleanupQueue"
+ "MobileAssistantDaemons-3600.68.44"
+ "T@\"HMCurrentMediaGroupProvider\",&,N,V_currentMediaGroupProvider"
+ "TB,V_osEligibilitySiriModeCached"
+ "Vv28@0:8B16@\"NSURL\"20"
+ "Vv28@0:8B16@20"
+ "_ADCommandCenterMoveSpeechAudioDirectoryAsideForCleanup"
+ "_cleanUpAudioDirectoriesAsynchronously:"
+ "_currentLanguageCodeLock"
+ "_currentMediaGroupProvider"
+ "_existingSharedCommandCenter"
+ "_getSiriExtensionProviders"
+ "_handleDetectedHeadGestureOnQueue:"
+ "_observing"
+ "_osEligibilitySiriModeCached"
+ "_pendingAssetFetchBackstops"
+ "_publishDefaultUserAnalyticsIdUpdateForEphemeralId:"
+ "_remoteDataLock"
+ "_test_lockRemoteData"
+ "_test_unlockRemoteData"
+ "_updateAssetManifestCacheOnQueue:"
+ "adRequestSetReplayCaptureRequested:toPath:"
+ "arrayForKey:"
+ "com.apple.generativepartnerservicesettings"
+ "currentLanguageCode"
+ "homeInfoManagerDidUpdateHomes:"
+ "initForTesting"
+ "initWithLanguageCode:gender:isCustom:name:footprint:contentVersion:masteredVersion:pacePreset:expressivityPreset:"
+ "moveItemAtPath:toPath:error:"
+ "osEligibilitySiriModeCached"
+ "performBlockOnQueueForTesting:"
+ "providerName"
+ "removeObjectIdenticalTo:"
+ "setCurrentLanguageCode:"
+ "setCurrentMediaGroupProvider:"
+ "setIsProviderEnabled:"
+ "setIsProviderInstalled:"
+ "setOsEligibilitySiriModeCached:"
+ "setProviderName:"
+ "setProviders:"
+ "setReplayCaptureRequested:toPath:"
+ "siriExtensionProvidersMetricsSnapshot"
+ "v24@0:8@\"ADHomeInfoManager\"16"
+ "v28@0:8B16@\"NSURL\"20"
- "%s ADOdeonMediaGroupObserver: currentMediaGroupProvider not available"
- "%s ADOdeonMediaGroupObserver: homeManagerDidUpdateHomes - currentAccessory: %@, home: %@"
- "%s ADOdeonMediaGroupObserver: subscribed to media group provider"
- "%s ADOdeonMediaGroupObserver: triggered provider merge after homes update"
- "-[ADHeadGestureManager didDetectedWithHeadGesture:]"
- "-[ADHeadGestureManager didStartStreamingWithIsStreaming:]"
- "-[ADOdeonMediaGroupObserver currentMediaGroupsDataProvider:didReceiveCurrentMediaGroup:]"
- "-[ADOdeonMediaGroupObserver homeManagerDidUpdateHomes:]"
- "-[ADOdeonMediaGroupObserver startObserving]_block_invoke"
- "36"
- "HMCurrentMediaGroupProviderDelegate"
- "MobileAssistantDaemons-3600.68.39"
- "T@\"HMHomeManager\",&,N,V_homeManager"
- "currentAccessory"
- "home"
- "homeManager"
- "initWithConfiguration:"
- "initWithOptions:cachePolicy:"
- "setDelegateQueue:"
- "setHomeManager:"
- "setUnderlyingQueue:"
- "subscribe"
- "v32@0:8@\"HMCurrentMediaGroupProvider\"16@\"HMCurrentMediaGroup\"24"
```
