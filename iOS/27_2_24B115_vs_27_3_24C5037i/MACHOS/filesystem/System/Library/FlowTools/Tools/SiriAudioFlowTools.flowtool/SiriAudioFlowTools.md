## SiriAudioFlowTools

> `/System/Library/FlowTools/Tools/SiriAudioFlowTools.flowtool/SiriAudioFlowTools`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__DATA.__objc_data`

```diff

-3605.24.1.0.0
-  __TEXT.__text: 0x75c8c
-  __TEXT.__auth_stubs: 0x1ca0
-  __TEXT.__objc_stubs: 0x4a0
-  __TEXT.__const: 0x7168
-  __TEXT.__constg_swiftt: 0x1518
-  __TEXT.__swift5_typeref: 0x1a1c
-  __TEXT.__swift5_reflstr: 0x15ef
-  __TEXT.__swift5_fieldmd: 0x192c
-  __TEXT.__swift5_assocty: 0x400
-  __TEXT.__swift5_proto: 0x5f8
-  __TEXT.__swift5_types: 0x1ac
-  __TEXT.__cstring: 0xc05
-  __TEXT.__swift5_capture: 0x1d4
+3610.8.1.0.0
+  __TEXT.__text: 0x7d050
+  __TEXT.__auth_stubs: 0x1ee0
+  __TEXT.__objc_stubs: 0x4c0
+  __TEXT.__const: 0x7468
+  __TEXT.__swift5_typeref: 0x1b0e
+  __TEXT.__constg_swiftt: 0x1598
+  __TEXT.__swift5_reflstr: 0x164f
+  __TEXT.__swift5_fieldmd: 0x19a4
+  __TEXT.__swift5_assocty: 0x418
+  __TEXT.__cstring: 0xc65
+  __TEXT.__oslogstring: 0x4f28
+  __TEXT.__swift5_proto: 0x614
+  __TEXT.__swift5_types: 0x1b4
+  __TEXT.__swift5_protos: 0x54
+  __TEXT.__swift5_capture: 0x1e4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x6c
-  __TEXT.__oslogstring: 0x47e8
-  __TEXT.__swift_as_entry: 0x100
-  __TEXT.__swift_as_ret: 0x178
-  __TEXT.__swift_as_cont: 0xa0
-  __TEXT.__objc_classname: 0x1ef
-  __TEXT.__objc_methname: 0x410
+  __TEXT.__swift_as_entry: 0x11c
+  __TEXT.__swift_as_ret: 0x198
+  __TEXT.__swift_as_cont: 0xa8
+  __TEXT.__objc_classname: 0x21f
+  __TEXT.__objc_methname: 0x430
   __TEXT.__objc_methtype: 0x26
-  __TEXT.__swift5_protos: 0x50
-  __TEXT.__unwind_info: 0x1ad0
-  __TEXT.__eh_frame: 0x2c40
-  __DATA_CONST.__const: 0x3670
-  __DATA_CONST.__objc_classlist: 0x50
+  __TEXT.__unwind_info: 0x1bc8
+  __TEXT.__eh_frame: 0x2e80
+  __DATA_CONST.__const: 0x3798
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xe58
-  __DATA_CONST.__got: 0x548
-  __DATA_CONST.__auth_ptr: 0x22e8
-  __DATA.__objc_const: 0xae0
-  __DATA.__objc_selrefs: 0x128
+  __DATA_CONST.__auth_got: 0xf78
+  __DATA_CONST.__got: 0x5e8
+  __DATA_CONST.__auth_ptr: 0x2430
+  __DATA.__objc_const: 0xb98
+  __DATA.__objc_selrefs: 0x130
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x2628
+  __DATA.__data: 0x2790
   __DATA.__common: 0x268
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1761
-  Symbols:   205
-  CStrings:  352
+  Functions: 1817
+  Symbols:   206
+  CStrings:  373
 
Symbols:
+ _objc_retain_x27
CStrings:
+ "AudioContentSourceResolver.contentSource() - AudioSearch has no ranked results, content source unknown"
+ "AudioContentSourceResolver.contentSource() - SiriKit fallback entity is not for a 1P app, content source unknown"
+ "AudioContentSourceResolver.contentSource() - collection contentSource=%{public}d internalKind=%{public}s catalogIDCount=%{public}ld"
+ "AudioContentSourceResolver.contentSource() - contentSource=%{public}d matchedEntityId=%{bool,public}d rankedResultCount=%{public}ld"
+ "AudioContentSourceResolver.contentSource() - entity id is not a musicKit id, content source unknown"
+ "AudioContentSourceResolver.contentSource() - musicKit id contentSource=%{public}d"
+ "AudioContentSourceResolver.contentSource() - musicKit id has neither deviceLocalID nor catalogID, content source unknown"
+ "AudioContentSourceResolver.contentSource() - unknown RankingItem case: %s"
+ "PlayAudioAppIntentExecutionStrategy.handleDestinationsAndWarmupAudioQueue() - connecting %{public}ld route(s), hostsPlaybackHere=%{bool,public}d"
+ "PlayAudioAppIntentExecutionStrategy.requestingDeviceAirPlayRouteId() - home-speaker request carried no originating route, SFA unavailable: hasAirPlayContext=%{bool,public}d"
+ "PlayAudioAppIntentExecutionStrategy.requestingDeviceAirPlayRouteId() - no SFA route: deviceIdiom=%{public}s, isCompanionPaired=%{bool,public}d"
+ "PlayAudioAppIntentExecutionStrategy.siriForAirPlayRouteId() - client has its own PlayAudioIntent, playback stays native"
+ "PlayAudioAppIntentExecutionStrategy.siriForAirPlayRouteId() - no client PlayAudioIntent for %{sensitive}s, AirPlaying back to the requesting device"
+ "PlayAudioAppIntentExecutionStrategy.siriForAirPlayRouteId() - residency lookup failed, skipping SFA route setup: %s"
+ "PlayAudioAppIntentExecutionStrategy.warmupAudioQueueIntent() - skipping warmup on HomePod!"
+ "Smart Play can't start a third-party default music service"
+ "Smart Play could not start playback"
+ "SmartPlayTool.execute() default music service is third party: %{public}s"
+ "SmartPlayTool.execute() executorTraceID: %{public}s"
+ "SmartPlayTool.execute() failed: %{public}s"
+ "SmartPlayTool.execute() succeeded: %{public}s"
+ "ToolKitServiceProvider.getLocalToolDefinition() resolved local tool for %s: %s"
+ "WholeHouseAudioService.connectToSpeakers() connecting to %{public}ld route(s)"
+ "WholeHouseAudioService.connectToSpeakers() no route ids. Returning."
+ "WholeHouseAudioService.createSpeakerConnectionInvocation() runsOnThisDevice=%{bool,public}d"
+ "WholeHouseAudioService.hydrateMediaControlsDevices() hydrated %ld MediaControlsDevices"
+ "WholeHouseAudioService.hydrateMediaControlsDevices() hydrating MediaControlsDevice for route %s"
+ "WholeHouseAudioService.resolveAllAccessories() resolved %ld accessories from groupRepresentation: %s"
+ "_TtC14SiriAudioTools13SmartPlayTool"
+ "makeSmartPlay"
+ "setContentSource:"
- "PlayAudioAppIntentExecutionStrategy.handleDestinations() - processing %ld destinations"
- "PlayAudioAppIntentExecutionStrategy.handleDestinationsAndWarmupAudioQueue() - handle destinations"
- "WholeHouseAudioService.connectToSpeakers() connecting to %ld accessories"
- "WholeHouseAudioService.convertAccessoriesToMediaControlsDevices() converted %ld MediaControlsDevices"
- "WholeHouseAudioService.convertAccessoriesToMediaControlsDevices() converting accessory %s to MediaControlsDevice"
- "WholeHouseAudioService.createSpeakerConnectionInvocation()..."
- "WholeHouseAudioService.handleDestinations() empty destinations. Returning."
- "WholeHouseAudioService.handleDestinations() no accessories resolved from destinations"
- "WholeHouseAudioService.handleDestinations() processing %ld destinations"
- "WholeHouseAudioService.resolveAllAccessories() resolved %ld accessories from groupRepresentation"
```
