## SiriAudioFlowTools

> `/System/Library/FlowTools/Tools/SiriAudioFlowTools.flowtool/Contents/MacOS/SiriAudioFlowTools`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-3600.33.17.0.0
-  __TEXT.__text: 0x62840
-  __TEXT.__auth_stubs: 0x1790
+3605.20.1.0.0
+  __TEXT.__text: 0x6c760
+  __TEXT.__auth_stubs: 0x1900
   __TEXT.__objc_stubs: 0x4c0
-  __TEXT.__const: 0x6ee0
-  __TEXT.__oslogstring: 0x3cd8
-  __TEXT.__constg_swiftt: 0x1478
-  __TEXT.__swift5_typeref: 0x1960
-  __TEXT.__swift5_reflstr: 0x14cf
-  __TEXT.__swift5_fieldmd: 0x180c
+  __TEXT.__const: 0x7008
+  __TEXT.__oslogstring: 0x4494
+  __TEXT.__constg_swiftt: 0x149c
+  __TEXT.__swift5_typeref: 0x19b8
+  __TEXT.__swift5_reflstr: 0x14c8
+  __TEXT.__swift5_fieldmd: 0x1828
   __TEXT.__swift5_assocty: 0x400
-  __TEXT.__cstring: 0xab5
-  __TEXT.__swift5_proto: 0x5e0
-  __TEXT.__swift5_types: 0x1a4
+  __TEXT.__cstring: 0xb75
+  __TEXT.__swift5_proto: 0x5ec
+  __TEXT.__swift5_types: 0x1a8
   __TEXT.__swift5_capture: 0x1b4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x6c
   __TEXT.__swift_as_entry: 0xf4
-  __TEXT.__swift_as_ret: 0x154
+  __TEXT.__swift_as_ret: 0x158
   __TEXT.__swift_as_cont: 0x94
   __TEXT.__objc_classname: 0x1ef
   __TEXT.__objc_methname: 0x480
   __TEXT.__objc_methtype: 0x26
   __TEXT.__swift5_protos: 0x4c
-  __TEXT.__unwind_info: 0x1978
-  __TEXT.__eh_frame: 0x2738
-  __DATA_CONST.__const: 0x34a0
+  __TEXT.__unwind_info: 0x19f0
+  __TEXT.__eh_frame: 0x27e8
+  __DATA_CONST.__const: 0x3520
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xbd0
-  __DATA_CONST.__got: 0x480
-  __DATA_CONST.__auth_ptr: 0x2170
+  __DATA_CONST.__auth_got: 0xc88
+  __DATA_CONST.__got: 0x4e8
+  __DATA_CONST.__auth_ptr: 0x2218
   __DATA.__objc_const: 0xae0
   __DATA.__objc_selrefs: 0x130
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x2530
+  __DATA.__data: 0x2588
   __DATA.__common: 0x268
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/HomeKit.framework/Versions/A/HomeKit
   - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/Versions/A/IntelligenceFlow
   - /System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote
+  - /System/Library/PrivateFrameworks/SiriAudioSupport.framework/Versions/A/SiriAudioSupport
   - /System/Library/PrivateFrameworks/SiriInformationSearch.framework/Versions/A/SiriInformationSearch
   - /System/Library/PrivateFrameworks/SiriInformationTypes.framework/Versions/A/SiriInformationTypes
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/Versions/A/SiriInstrumentation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1691
+  Functions: 1719
   Symbols:   159
-  CStrings:  323
+  CStrings:  341
 
CStrings:
+ "No PlayAudioIntent found on the client device for bundleId "
+ "PlayAudioAppIntentExecutionStrategy.makeDeviceTargetedInvocation() - no PlayAudioIntent on device %{private}s for home-speaker origin (deviceIdiom=%{public}s); refusing to fall back to local to avoid leaking playback onto the companion"
+ "PlayAudioAppIntentExecutionStrategy.remapPlaybackAttributes() - remapped collection element type to %s"
+ "PlayAudioAppIntentExecutionStrategy.remapQueueLocation() - remapped enum type to %{public}s"
+ "PlayAudioAppIntentExecutionStrategy.warmupAudioQueueIntent() - attributed %{public}s to the remote target"
+ "PlayAudioAppIntentExecutionStrategy.warmupAudioQueueIntent() - resolving warmup tool on client device %{private}s"
+ "PlayAudioAppIntentExecutionStrategy.warmupAudioQueueIntent() - skipping warmup: invocation targets %{public}s but the request came from %{private}s. Warmup must run on the requesting device."
+ "PlayAudioAppIntentExecutionStrategy.warmupTargetsRequestingDevice() - unknown target device kind %{public}s; refusing to warm"
+ "RemoteParameterAttribution.attributed() - %{public}s → %{public}s"
+ "RemoteParameterAttribution.attributingParameters() - parameter '%{public}s' is an un-attributed collection; it needs a schema-resolved target type (see findMatchingTargetType), not this helper"
+ "RemoteParameterAttribution.attributingParameters() - re-homed parameter '%{public}s' onto %{public}s"
+ "RemoteParameterAttribution.reducingToStableIdentifier() - %{public}s → %{public}s for remote resolution"
+ "WholeHouseAudioService.createSpeakerConnectionInvocation() - %{public}ld destination(s), element type %{public}s"
+ "WholeHouseAudioService.declaredDestinationsElementType() - '%s' is not device-attributed on %s; using the local type"
+ "WholeHouseAudioService.declaredDestinationsElementType() - tool definition %s declares no '%s' parameter"
+ "WholeHouseAudioService.declaredDestinationsElementType() - using declared type %s"
+ "home speaker originated request; refusing to fall back to the companion to avoid "
+ "leaking playback onto it"
```
