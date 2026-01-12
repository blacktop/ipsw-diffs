## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3300.3.1.0.0
-  __TEXT.__text: 0xfd49dc
+3300.4.1.0.0
+  __TEXT.__text: 0xfd50a4
   __TEXT.__auth_stubs: 0xb480
   __TEXT.__objc_methlist: 0x2484
   __TEXT.__const: 0x4e690
-  __TEXT.__cstring: 0x12fd2c
-  __TEXT.__oslogstring: 0x14d6bd
+  __TEXT.__cstring: 0x12fe36
+  __TEXT.__oslogstring: 0x14d7b0
   __TEXT.__ustring: 0x23e
   __TEXT.__gcc_except_tab: 0x17cc
   __TEXT.__dlopen_cstrs: 0x1c8
-  __TEXT.__unwind_info: 0x13d60
+  __TEXT.__unwind_info: 0x13d68
   __TEXT.__eh_frame: 0x258
   __TEXT.__objc_classname: 0x82d
   __TEXT.__objc_methname: 0x6b60
   __TEXT.__objc_methtype: 0x2901
   __TEXT.__objc_stubs: 0x6260
-  __DATA_CONST.__got: 0x3920
-  __DATA_CONST.__const: 0x23808
+  __DATA_CONST.__got: 0x3928
+  __DATA_CONST.__const: 0x23810
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x5a58
-  __AUTH_CONST.__const: 0x41588
-  __AUTH_CONST.__cfstring: 0x53560
+  __AUTH_CONST.__const: 0x41598
+  __AUTH_CONST.__cfstring: 0x535a0
   __AUTH_CONST.__objc_const: 0x4db8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7EE09E7A-B0AB-3822-A3A6-1B57B371D50E
-  Functions: 43982
-  Symbols:   118533
-  CStrings:  67097
+  UUID: 65D0E796-FC11-3CA8-91B3-6E63A968EF4F
+  Functions: 43983
+  Symbols:   118541
+  CStrings:  67106
 
Symbols:
+ ___block_descriptor_tmp.233
+ ___block_descriptor_tmp.237
+ ___block_descriptor_tmp.246
+ ___block_descriptor_tmp.247
+ ___block_descriptor_tmp.252
+ ___block_descriptor_tmp.255
+ ___block_literal_global.182
+ ___block_literal_global.185
+ ___fbapspManager_PostInspectSampleBuffer_block_invoke.230
+ ___fbapspManager_flushFromTime_block_invoke.248
+ ___fbapspManager_flushFromTime_block_invoke.249.cold.1
+ ___fbapspManager_flushFromTime_block_invoke.249.cold.2
+ ___fbapspManager_flushFromTime_block_invoke.251
+ _fbapspManager_tapToRadar
+ _figPlaybackCoordinator_SetProperty.cold.2
+ _figPlaybackCoordinator_playerAirPlayVideoActiveDidChange
+ _figPlaybackCoordinator_updateLocalCoordinationAirplaySuspension
+ _kFigPlayerProperty_IsCoordinatedMultiViewPlaybackAllowedForExternalPlayback
+ _kFigTimelineCoordinatorProperty_IsLocallyCoordinated
- _FigAssetCreateWithFormatReader.cold.1
- _FigAssetCreateWithFormatReader.cold.2
- _FigAssetCreateWithFormatReader.cold.3
- _FigAssetCreateWithFormatReader.cold.4
- _OUTLINED_FUNCTION_1241
- ___block_descriptor_tmp.188
- ___block_descriptor_tmp.230
- ___block_descriptor_tmp.235
- ___block_descriptor_tmp.240
- ___block_descriptor_tmp.243
- ___block_descriptor_tmp.244
- ___block_descriptor_tmp.248
- ___block_descriptor_tmp.251
- ___block_descriptor_tmp.256
- ___block_descriptor_tmp.257
- ___fbapspManager_PostInspectSampleBuffer_block_invoke.228
- ___fbapspManager_flushFromTime_block_invoke.246
- ___fbapspManager_flushFromTime_block_invoke.247
- ___fbapspManager_flushFromTime_block_invoke.247.cold.1
- ___fbapspManager_flushFromTime_block_invoke.247.cold.2
CStrings:
+ "\noptionsDict = <redacted>"
+ "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s ERROR: Found transitionID='%@' but invalid propertiesToUpdateAtTransition dictionary %p."
+ "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s Error: initiating Tap-to-Radar because %@"
+ "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s Found transitionID='%@' with TransitionID OPTS=%1.3f. Send propertiesToUpdateAtTransition at RetimedStartMediaTime=%1.3f using mixStartMediaTimeOffset=%1.3f properties=%@"
+ "<<<< FigPlaybackCoordinator >>>> %s: %p [%d]: AirPlayVideoActiveDidChange from %d to %d. Forcing transition to item %p"
+ "Invalid propertiesToUpdateAtTransition dictionary"
+ "Invalidating during mixing when timelineMilestone has not been reached yet!"
+ "IsCoordinatedMultiViewPlaybackAllowedForExternalPlayback"
+ "figPlaybackCoordinator_playerAirPlayVideoActiveDidChange"
- "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s Error: invalidating during mixing when timelineMilestone has not been reached yet!"
- "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s Found transitionID='%@' with TransitionID OPTS=%1.3f. Send propertiesToUpdateAtTransition at RetimedStartMediaTime=%1.3f using mixStartMediaTimeOffset=%1.3f."

```
