## AudioFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin`

```diff

-3304.71.3.1.1
-  __TEXT.__text: 0x299940
-  __TEXT.__auth_stubs: 0x5f00
+3305.20.1.1.1
+  __TEXT.__text: 0x29d408
+  __TEXT.__auth_stubs: 0x6000
   __TEXT.__objc_methlist: 0x35c
-  __TEXT.__const: 0x97f2
-  __TEXT.__cstring: 0x2768c
-  __TEXT.__swift5_typeref: 0x4472
+  __TEXT.__const: 0x8e22
+  __TEXT.__cstring: 0x27a9c
+  __TEXT.__swift5_typeref: 0x4454
   __TEXT.__constg_swiftt: 0x5c2c
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_reflstr: 0x49b1

   __TEXT.__swift5_proto: 0x4f8
   __TEXT.__swift5_types: 0x348
   __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x269a
+  __TEXT.__objc_methname: 0x293d
   __TEXT.__objc_methtype: 0x3ef
   __TEXT.__swift5_fieldmd: 0x38cc
-  __TEXT.__swift5_capture: 0x3d84
+  __TEXT.__swift5_capture: 0x38a0
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x4538
-  __TEXT.__eh_frame: 0x3288
-  __DATA_CONST.__auth_got: 0x2f80
-  __DATA_CONST.__got: 0x1618
+  __TEXT.__unwind_info: 0x44a0
+  __TEXT.__eh_frame: 0x3248
+  __DATA_CONST.__auth_got: 0x3000
+  __DATA_CONST.__got: 0x1648
   __DATA_CONST.__auth_ptr: 0x410
-  __DATA_CONST.__const: 0xfbd8
+  __DATA_CONST.__const: 0xef60
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_classrefs: 0x310
   __DATA.__objc_const: 0x9968
-  __DATA.__objc_selrefs: 0xc58
+  __DATA.__objc_selrefs: 0xc70
   __DATA.__objc_data: 0x1200
-  __DATA.__data: 0xe558
+  __DATA.__data: 0xebb0
   __DATA.__bss: 0x8d10
-  __DATA.__common: 0x428
+  __DATA.__common: 0x388
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight

   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine
+  - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7135
+  Functions: 6915
   Symbols:   351
-  CStrings:  2894
+  CStrings:  2914
 
CStrings:
+ "AddMediaFlowStrategy#actionForInput"
+ "AddMediaFlowStrategy#makeIntentFrom"
+ "AddMediaFlowStrategy#makeIntentFrom received pommesResponse: %{private}@"
+ "AudioIntentDetails decoding error"
+ "CommonFlowStrategy#actionForInput received pommesResponse parse"
+ "CommonFlowStrategy#makeIntentFromParse received pommesResponse: %{private}@"
+ "ConverterHelpers#audioIntentDetails error serializing"
+ "ConverterHelpers#audioIntentDetails: len=%ld"
+ "ConverterHelpers#itemDetails: error serializing"
+ "Parse#getSiriKitIntent failed to get task from usoParse"
+ "Parse#getSiriKitIntent firstUserDialogAct No user dialog act found in usoParse"
+ "Parse#getSiriKitIntent found .uso in primary parse of input %{private}s"
+ "Parse#getSiriKitIntent uso affinity task"
+ "PlayMediaFlowStrategy#actionForInput"
+ "PlayMediaFlowStrategy#makeIntentFrom"
+ "PlayMediaRCHFlowWrapper#dialogForError using special dialog for ageVerificationExplicitContent (explicitContentRestricted) code"
+ "SearchForMediaFlowStrategy#actionForInput"
+ "SearchForMediaFlowStrategy#makeIntentFrom"
+ "initWithAppSelectionEnabled:appInferred:audioSearchResults:privateMediaIntentData:appSelectionSignalsEnabled:appSelectionSignalsFrequencyDenominator:shouldSuppressCommonWholeHouseAudioRoutes:immediatelyStartPlayback:isAmbiguousPlay:isPersonalizedRequest:internalSignals:entityConfidenceSignalsEnabled:entityConfidenceSignalsFrequencyDenominatorInternal:entityConfidenceSignalsFrequencyDenominatorProd:entityConfidenceSignalsMaxItemsToDisambiguate:alternativeProviderBundleIdentifier:ampPAFDataSetID:pegasusMetaData:"
+ "initWithPrivateMediaIntentData:audioSearchResults:internalSignals:appInferred:pegasusMetaData:"
+ "initWithPrivateMediaIntentData:audioSearchResults:internalSignals:pegasusMetaData:"
+ "initWithRecommendationId:assetInfo:sharedUserIdFromPlayableMusicAccount:punchoutURI:requiresSubscription:provider:isAvailable:isHardBan:bundleId:universalResourceLink:providerAppName:internalSignals:ampConfidenceScore:ampConfidenceLevel:pegasusMetaData:mediaSubItems:"
+ "pegasusMetaData"
- "ConverterHelpers#convertPrivateAddMediaIntentData audioSearchResults: %s"
- "initWithPrivateMediaIntentData:audioSearchResults:"
- "initWithRecommendationId:assetInfo:sharedUserIdFromPlayableMusicAccount:punchoutURI:requiresSubscription:provider:isAvailable:isHardBan:bundleId:universalResourceLink:providerAppName:internalSignals:ampConfidenceScore:ampConfidenceLevel:mediaSubItems:"

```
