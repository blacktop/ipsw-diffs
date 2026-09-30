## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3400.145.2.0.0
-  __TEXT.__text: 0x1706d0
+3400.150.4.1.1
+  __TEXT.__text: 0x170e04
   __TEXT.__auth_stubs: 0x1740
-  __TEXT.__objc_stubs: 0x1e1e0
-  __TEXT.__objc_methlist: 0x16d90
+  __TEXT.__objc_stubs: 0x1e200
+  __TEXT.__objc_methlist: 0x16da8
   __TEXT.__const: 0x338
-  __TEXT.__gcc_except_tab: 0x3890
-  __TEXT.__cstring: 0x2a2b6
-  __TEXT.__objc_methname: 0x3ddfd
-  __TEXT.__oslogstring: 0x2138c
-  __TEXT.__objc_classname: 0x35df
-  __TEXT.__objc_methtype: 0x86ba
+  __TEXT.__gcc_except_tab: 0x38c0
+  __TEXT.__cstring: 0x2a419
+  __TEXT.__objc_methname: 0x3de5f
+  __TEXT.__oslogstring: 0x2153c
+  __TEXT.__objc_classname: 0x35c7
+  __TEXT.__objc_methtype: 0x86c0
   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__info_plist: 0x41f
-  __TEXT.__unwind_info: 0x55f0
+  __TEXT.__unwind_info: 0x5600
   __DATA_CONST.__auth_got: 0xbb8
-  __DATA_CONST.__got: 0x1380
+  __DATA_CONST.__got: 0x1388
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x5c70
-  __DATA_CONST.__cfstring: 0x8340
+  __DATA_CONST.__cfstring: 0x8380
   __DATA_CONST.__objc_classlist: 0x990
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x500
+  __DATA_CONST.__objc_protolist: 0x4f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x7d0
+  __DATA_CONST.__objc_superrefs: 0x7d8
   __DATA_CONST.__objc_intobj: 0xca8
   __DATA_CONST.__objc_doubleobj: 0x80
   __DATA_CONST.__objc_arraydata: 0x270
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_floatobj: 0x4b0
-  __DATA.__objc_const: 0x2c360
-  __DATA.__objc_selrefs: 0xb548
+  __DATA.__objc_const: 0x2c318
+  __DATA.__objc_selrefs: 0xb560
   __DATA.__objc_ivar: 0x1efc
   __DATA.__objc_data: 0x5fa0
-  __DATA.__data: 0x3c00
+  __DATA.__data: 0x3ba0
   __DATA.__bss: 0x808
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets
-  - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition
   - /System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9600
-  Symbols:   1013
-  CStrings:  15627
+  Functions: 9602
+  Symbols:   1014
+  CStrings:  15644
 
Symbols:
+ _CSLogCategoryAdBlocker
CStrings:
+ "%!s(MISSING) Error reading file"
+ "%!s(MISSING) Failed to deregister for asset update notifications, status: %!u(MISSING)"
+ "%!s(MISSING) Failed to register for asset update notifications, status: %!u(MISSING)"
+ "%!s(MISSING) File does not exist: %!{(MISSING)public}@"
+ "%!s(MISSING) Found OEP asset for %!@(MISSING) at path: %!{(MISSING)public}@"
+ "%!s(MISSING) Invalid CSEndpointerAssetType: %!l(MISSING)u"
+ "%!s(MISSING) Magus is not supported since Flexible Followup is not enabled on device"
+ "%!s(MISSING) No OEP asset for %!@(MISSING) was found."
+ "%!s(MISSING) Registering for asset update notifications..."
+ "%!s(MISSING) Updating %!@(MISSING) asset with language: %!@(MISSING)"
+ "%!s(MISSING) Updating endpointer assets if needed..."
+ "%!s(MISSING) initilizing adBlockerAssetDecoder with assetPath: %!@(MISSING)"
+ "%!s(MISSING) isSupported=%!@(MISSING): Is request during active call? %!@(MISSING), isDeviceSupported: %!@(MISSING), isFFEnabledOnDevice: %!@(MISSING), isSupportedRequestType: %!@(MISSING), isFFUserDisabled: %!@(MISSING), isTypeToSiriEnabled: %!@(MISSING), isLocaleInDenyList:%!@(MISSING)"
+ "%!s(MISSING) tts Finished:%!u(MISSING) isRequestCompleted:%!u(MISSING)"
+ "+[CSEndpointerAssetManager _getFakeEndpointAsset]"
+ "+[CSEndpointerAssetManager _getOEPAssetWithLanguage:]"
+ "+[CSEndpointerAssetManager _getOEPVersionFromPath:]"
+ "-[CSAdBlockerAssetDecoder initWithAssetPath:]"
+ "-[CSAttSiriMagusSupportedPolicy _isMagusSupportedWithRecordRoute:playbackRoute:isInSplitterMode:isInActiveCall:isSupportedRequestType:audioSessionId:recordDeviceInfo:]"
+ "-[CSEndpointerAssetManager _notifyAssetsUpdateForObserver:]"
+ "-[CSEndpointerAssetManager _registerForAssetUpdateNotifications]"
+ "-[CSEndpointerAssetManager _updateAssetWithLanguage:assetType:]"
+ "-[CSEndpointerAssetManager _updateEndpointerAssetsIfNeeded]"
+ "-[CSEndpointerAssetManager dealloc]"
+ "B52@0:8@16@24@32I40@44"
+ "B56@0:8@16@24B32B36B40I44@48"
+ "HEP"
+ "Invalid CSEndpointerAssetType"
+ "T@\"NSData\",&,N,V_payLoadData"
+ "_assetUpdateNotificationToken"
+ "_getOEPAssetWithLanguage:"
+ "_isMagusSupportedWithRecordRoute:playbackRoute:isInSplitterMode:isInActiveCall:isSupportedRequestType:audioSessionId:recordDeviceInfo:"
+ "_isRouteValidForEchoCancellationWithAppleSiliconMac:"
+ "_notifyAssetsUpdateForObserver:"
+ "_payLoadData"
+ "_registerForAssetUpdateNotifications"
+ "_updateEndpointerAssetsIfNeeded"
+ "dataWithContentsOfFile:options:error:"
+ "initWithAssetPath:"
+ "initWithAssetType:language:regionId:"
+ "isContinuousConversationEnabled"
+ "isMagusSupportedWithAudioRecordContext:recordRoute:playbackRoute:audioSessionId:recordDeviceInfo:"
+ "payLoadData"
+ "setPayLoadData:"
+ "switchToNewAssetsForAssetType:"
+ "v32@?0@\"NSString\"8@\"NSString\"16@\"CSFAudioRecordDeviceInfo\"24"
- "%!s(MISSING) File doesn't exist: %!{(MISSING)public}@"
- "%!s(MISSING) _activeEndpointer: %!@(MISSING) should only be set to one of _hybridEndpointer: %!@(MISSING), _nnvadEndpointer: %!@(MISSING), or nil"
- "%!s(MISSING) installationString: %!@(MISSING), for language: %!@(MISSING)"
- "%!s(MISSING) isSupported=%!@(MISSING): Is request during active call? %!@(MISSING), isDeviceSupported: %!@(MISSING), isSupportedRequestType: %!@(MISSING), isFFUserDisabled: %!@(MISSING), isTypeToSiriEnabled: %!@(MISSING), isLocaleInDenyList:%!@(MISSING)"
- "%!s(MISSING) tts Finished:%!u(MISSING)"
- "-[CSAttSiriMagusSupportedPolicy _isMagusSupportedWithRecordRoute:playbackRoute:isInSplitterMode:isInActiveCall:isSupportedRequestType:audioSessionId:]"
- "-[CSEndpointerAssetManager _getFakeEndpointAsset]"
- "-[CSEndpointerAssetManager _getOEPVersionFromPath:]"
- "-[CSEndpointerAssetManager _updateOEPAssetsWithLanguage:]"
- "-[CSEndpointerAssetManager assetStatus:]"
- "-[CSEndpointerProxy _setActiveEndpointer:]"
- "B44@0:8@16@24@32I40"
- "B48@0:8@16@24B32B36B40I44"
- "SFEntitledAssetDelegate"
- "T@\"NSDictionary\",&,N,V_asrDatapackInstallationStatus"
- "TQ,N,V_lastUsedAnalyzerType"
- "_asrDatapackInstallationStatus"
- "_isMagusSupportedWithRecordRoute:playbackRoute:isInSplitterMode:isInActiveCall:isSupportedRequestType:audioSessionId:"
- "_lastUsedAnalyzerType"
- "_setActiveEndpointer:"
- "_updateOEPAssetsWithLanguage:"
- "asrDatapackInstallationStatus"
- "assetStatus:"
- "isMagusSupportedWithAudioRecordContext:recordRoute:playbackRoute:audioSessionId:"
- "lastUsedAnalyzerType"
- "registerAssetDelegate:assetType:"
- "setAsrDatapackInstallationStatus:"
- "setLastUsedAnalyzerType:"
- "updateEndpointerAssetsIfNeeded"

```
