## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2265.2.1.0.0
-  __TEXT.__text: 0x7db7bc
-  __TEXT.__objc_methlist: 0x3ada0
-  __TEXT.__const: 0xc690
-  __TEXT.__cstring: 0x9fe76
-  __TEXT.__oslogstring: 0x144ecb
+2265.4.1.0.0
+  __TEXT.__text: 0x7dd434
+  __TEXT.__objc_methlist: 0x3ae28
+  __TEXT.__const: 0xc780
+  __TEXT.__cstring: 0xa017b
+  __TEXT.__oslogstring: 0x145390
   __TEXT.__gcc_except_tab: 0x2ddc
   __TEXT.__ustring: 0x2d4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1b7c8
+  __TEXT.__unwind_info: 0x1b828
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7800
+  __DATA_CONST.__const: 0x7878
   __DATA_CONST.__objc_classlist: 0x14b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x508
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18ed8
+  __DATA_CONST.__objc_selrefs: 0x18f38
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x1260
   __DATA_CONST.__objc_arraydata: 0x27d8
   __DATA_CONST.__got: 0x1de0
   __AUTH_CONST.__const: 0x4588
-  __AUTH_CONST.__cfstring: 0x29e80
+  __AUTH_CONST.__cfstring: 0x29fe0
   __AUTH_CONST.__objc_const: 0x6d3b8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x52f8

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 35560
-  Symbols:   42092
-  CStrings:  34196
+  Functions: 35584
+  Symbols:   42121
+  CStrings:  34227
 
Symbols:
+ +[VCSession forceFIRThrottleExperimentsToControl:ifUnsupportedByRemoteFrameworkVersion:]
+ +[VCSession isFIRThrottleExperimentSupportedByRemoteFrameworkVersion:]
+ +[VCSessionParticipant isValidAudioPosition:]
+ +[VCSessionParticipant isValidVolume:]
+ -[VCRedundancyControlAlgorithmVideoMultiway envelopeTimeWithStorebagKey:userDefaultKey:improvedStorebagKey:improvedUserDefaultKey:defaultTime:]
+ -[VCSession dispatchToParticipantWithID:block:]
+ -[VCSession resetFIRThrottleExperimentsIfUnsupportedByRemoteParticipant:]
+ -[VCSession setMediaState:forMediaType:participantID:]
+ -[VCSession setScreenEnabled:forParticipantID:]
+ -[VCSession setVideoEnabled:forParticipantID:]
+ -[VCSession(OneToOne) dispatchedUpdateOneToOneRateControllerForVideoEnabled:screenEnabled:]
+ -[VCSessionParticipantLocal dispatchedSetMuted:]
+ GCC_except_table219
+ _VCFIRThrottleTierAThreshold
+ _VCFIRThrottleTierBThreshold
+ _VCRedundancyMultiwayImprovedAttackTime
+ _VCRedundancyMultiwayImprovedDecayTime
+ _VideoReceiver_ResolveFIRThrottleIntervalForExperiments
+ ___44-[VCSessionManager registerBlocksForService]_block_invoke_6
+ ___44-[VCSessionManager registerBlocksForService]_block_invoke_7
+ ___44-[VCSessionManager registerBlocksForService]_block_invoke_8
+ ___44-[VCSessionManager registerBlocksForService]_block_invoke_9
+ ___46-[VCSession setVideoEnabled:forParticipantID:]_block_invoke
+ ___47-[VCSession dispatchToParticipantWithID:block:]_block_invoke
+ ___47-[VCSession setScreenEnabled:forParticipantID:]_block_invoke
+ ___54-[VCSession setMediaState:forMediaType:participantID:]_block_invoke
+ ___block_descriptor_36_e30_v16?0"VCSessionParticipant"8l
+ ___block_descriptor_40_e8_32o_e30_v16?0"VCSessionParticipant"8ls32l8
+ _kVCExperimentFIRThrottleTierA
+ _kVCExperimentFIRThrottleTierB
- GCC_except_table211
CStrings:
+ " [%s] %s:%d %@(%p) KPI-VAR-STATE: multiwayImprovedFactor=%d decayTime=%.3f attackTime=%.3f"
+ " [%s] %s:%d KPI-VAR-STATE: multiwayImprovedFactor=%d decayTime=%.3f attackTime=%.3f"
+ " [%s] %s:%d [AR_TX][FTDC][%p] Dual capture disabled: restoring cached AR portraitAR=%.3f, landscapeAR=%.3f"
+ "+[VCSession forceFIRThrottleExperimentsToControl:ifUnsupportedByRemoteFrameworkVersion:]"
+ "-[VCSession dispatchToParticipantWithID:block:]"
+ "-[VCSession setMediaState:forMediaType:participantID:]_block_invoke"
+ "-[VCSession setScreenEnabled:forParticipantID:]_block_invoke"
+ "-[VCSession setVideoEnabled:forParticipantID:]_block_invoke"
+ "-[VCSessionManager registerBlocksForService]_block_invoke_4"
+ "-[VCSessionManager registerBlocksForService]_block_invoke_6"
+ "2265"
+ "2265.4.1"
+ "VCSession [%s] %s:%d %@(%p) changing VCSessionParticipant=%p mediaType=%d to state=%d"
+ "VCSession [%s] %s:%d %@(%p) changing VCSessionParticipant[%p] screenEnabled to %d"
+ "VCSession [%s] %s:%d %@(%p) changing VCSessionParticipant[%p] videoEnabled to %d"
+ "VCSession [%s] %s:%d %@(%p) nil block for participantID=%@"
+ "VCSession [%s] %s:%d FIRTHROTTLE-AB: failed to force control for remoteFrameworkVersion=%s tierA=%d tierB=%d"
+ "VCSession [%s] %s:%d FIRTHROTTLE-AB: remoteFrameworkVersion=%s predates the experiment, running control"
+ "VCSession [%s] %s:%d changing VCSessionParticipant=%p mediaType=%d to state=%d"
+ "VCSession [%s] %s:%d changing VCSessionParticipant[%p] screenEnabled to %d"
+ "VCSession [%s] %s:%d changing VCSessionParticipant[%p] videoEnabled to %d"
+ "VCSession [%s] %s:%d nil block for participantID=%@"
+ "VCVideoStream [%s] %s:%d %@(%p) FIRTHROTTLE-AB: senderMinKeyFrameIntervalMs=%.1f firThrottleIntervalMs=%.1f"
+ "VCVideoStream [%s] %s:%d FIRTHROTTLE-AB: senderMinKeyFrameIntervalMs=%.1f firThrottleIntervalMs=%.1f"
+ "VSTDurHist"
+ "VSTDurHistA"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] rejected out-of-range firThrottleIntervalMs=%.1f, falling back to defaultMs=%.1f"
+ "VideoReceiver [%s] %s:%d FIRTHROTTLE-AB: firThrottleIntervalMs=%.1f armTierA=%d armTierB=%d (videoReceiver=%p)"
+ "_VideoPacketBuffer_NormalizeFIRThrottleInterval"
+ "enableFIRThrottleTierA"
+ "enableFIRThrottleTierB"
+ "redundancyMultiwayImprovedAttackTime"
+ "redundancyMultiwayImprovedDecayTime"
+ "v16@?0@\"VCSessionParticipant\"8"
+ "vc-experiment-fir-throttle-tier-a-threshold"
+ "vc-experiment-fir-throttle-tier-b-threshold"
+ "vc-red-multiway-improved-attack-time"
+ "vc-red-multiway-improved-decay-time"
- " [%s] %s:%d %@(%p) KPI-VAR-STATE: multiwayImprovedFactor=%d"
- " [%s] %s:%d KPI-VAR-STATE: multiwayImprovedFactor=%d"
- " [%s] %s:%d changing VCSessionParticipant=%p mediaType=%d to state=%d"
- " [%s] %s:%d changing VCSessionParticipant[%p] screenEnabled to %d"
- " [%s] %s:%d changing VCSessionParticipant[%p] videoEnabled to %d"
- "-[VCSessionManager registerBlocksForService]_block_invoke_3"
- "2265.2.1"
```
