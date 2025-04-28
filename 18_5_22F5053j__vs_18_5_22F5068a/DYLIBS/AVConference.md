## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2115.4.1.0.0
-  __TEXT.__text: 0x6cbb44
+2115.6.1.0.0
+  __TEXT.__text: 0x6cc0dc
   __TEXT.__auth_stubs: 0x5050
-  __TEXT.__objc_methlist: 0x31260
-  __TEXT.__const: 0x7a70
-  __TEXT.__cstring: 0x80b93
-  __TEXT.__oslogstring: 0xee802
+  __TEXT.__objc_methlist: 0x312a8
+  __TEXT.__const: 0x7a80
+  __TEXT.__cstring: 0x80c55
+  __TEXT.__oslogstring: 0xee83e
   __TEXT.__gcc_except_tab: 0x26d8
   __TEXT.__ustring: 0x144
-  __TEXT.__unwind_info: 0xeef8
+  __TEXT.__unwind_info: 0xef00
   __TEXT.__objc_classname: 0x47d1
-  __TEXT.__objc_methname: 0x72d9d
+  __TEXT.__objc_methname: 0x72e48
   __TEXT.__objc_methtype: 0x2490a
-  __TEXT.__objc_stubs: 0x485c0
+  __TEXT.__objc_stubs: 0x48600
   __DATA_CONST.__got: 0x18e0
   __DATA_CONST.__const: 0x61c0
   __DATA_CONST.__objc_classlist: 0x1180
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x440
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14d38
+  __DATA_CONST.__objc_selrefs: 0x14d48
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xfa8
   __DATA_CONST.__objc_arraydata: 0x25a0
   __AUTH_CONST.__auth_got: 0x2840
   __AUTH_CONST.__auth_ptr: 0xd8
   __AUTH_CONST.__const: 0x3368
-  __AUTH_CONST.__cfstring: 0x22ce0
-  __AUTH_CONST.__objc_const: 0x5bf40
+  __AUTH_CONST.__cfstring: 0x22d00
+  __AUTH_CONST.__objc_const: 0x5c090
   __AUTH_CONST.__objc_intobj: 0x4608
   __AUTH_CONST.__objc_arrayobj: 0x1a58
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x6458
+  __DATA.__objc_ivar: 0x647c
   __DATA.__data: 0x74b0
   __DATA.__bss: 0xa68
   __DATA.__common: 0x55

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 28548
-  Symbols:   88874
-  CStrings:  47571
+  Functions: 28560
+  Symbols:   88909
+  CStrings:  47583
 
Symbols:
+ -[VCSessionParticipantConfig forceL4SHighDataRate]
+ -[VCSessionParticipantConfig setForceL4SHighDataRate:]
+ -[VCVideoStreamConfig forceL4SHighDataRate]
+ -[VCVideoStreamConfig setForceL4SHighDataRate:]
+ -[VCVideoTransmitterConfig forceL4SHighDataRate]
+ -[VCVideoTransmitterConfig setForceL4SHighDataRate:]
+ _OBJC_IVAR_$_AVCStatisticsCollector._l4SHighDataRateEnabled
+ _OBJC_IVAR_$_VCRateControlBandwidthEstimator._l4sHighDataRateEnabled
+ _OBJC_IVAR_$_VCRateControlBandwidthEstimatorMap._l4sHighDataRateEnabled
+ _OBJC_IVAR_$_VCSession._forceHighDataRateFaceTime
+ _OBJC_IVAR_$_VCSessionParticipantConfig._forceL4SHighDataRate
+ _OBJC_IVAR_$_VCSessionParticipantLocal._forceL4SHighDataRate
+ _OBJC_IVAR_$_VCVideoStreamConfig._forceL4SHighDataRate
+ _OBJC_IVAR_$_VCVideoTransmitterConfig._forceL4SHighDataRate
+ _OBJC_IVAR_$_VCVideoTransmitterDefault._forceL4SHighDataRate
+ _VCRateControlBandwidthEstimatorMap_SetL4SHighDataRateEnabled
+ _VCRateControlBandwidthEstimatorMap_SetL4SHighDataRateEnabled.cold.1
+ _VCRateControlBandwidthEstimator_SetL4SHighDataRateEnabled
+ _VCRateControlBandwidthEstimator_SetL4SHighDataRateEnabled.cold.1
+ _VCStatisticsCollector_SetL4SHighDataRateEnabled
+ _VCStatisticsCollector_SetL4SHighDataRateEnabled.cold.1
+ ___28-[VCSession dispatchedStart]_block_invoke.545
+ ___28-[VCSession dispatchedStart]_block_invoke.546
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.539
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.541
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke_2.542
+ ___49-[VCSession vcSessionParticipantDidStopReacting:]_block_invoke.257
+ ___50-[VCSession dispatchedParticipant:didStart:error:]_block_invoke.553
+ ___51-[VCSession vcSessionParticipant:reactionDidStart:]_block_invoke.252
+ ___53-[VCSession dispatchedStopWithError:didRemoteCancel:]_block_invoke.552
+ ___63-[VCSession vcSessionParticipant:audioPaused:didSucceed:error:]_block_invoke.206
+ ___63-[VCSession vcSessionParticipant:videoPaused:didSucceed:error:]_block_invoke.216
+ ___64-[VCSession vcSessionParticipant:audioEnabled:didSucceed:error:]_block_invoke.178
+ ___64-[VCSession vcSessionParticipant:videoEnabled:didSucceed:error:]_block_invoke.188
+ ___65-[VCSession vcSessionParticipant:screenEnabled:didSucceed:error:]_block_invoke.193
+ ___69-[VCSession rateController:targetBitrateDidChange:rateChangeCounter:]_block_invoke.258
+ ___83-[VCSession vcSessionParticipant:mediaMixingDidChangeForMediaType:mixingMediaType:]_block_invoke.242
+ ___84-[VCSession vcSessionParticipant:mediaStateDidChange:forMediaType:didSucceed:error:]_block_invoke.241
+ ___block_literal_global.367
+ _objc_msgSend$forceL4SHighDataRate
+ _objc_msgSend$setForceL4SHighDataRate:
- ___28-[VCSession dispatchedStart]_block_invoke.542
- ___28-[VCSession dispatchedStart]_block_invoke.543
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.536
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.538
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke_2.539
- ___49-[VCSession vcSessionParticipantDidStopReacting:]_block_invoke.254
- ___50-[VCSession dispatchedParticipant:didStart:error:]_block_invoke.550
- ___51-[VCSession vcSessionParticipant:reactionDidStart:]_block_invoke.249
- ___53-[VCSession dispatchedStopWithError:didRemoteCancel:]_block_invoke.549
- ___63-[VCSession vcSessionParticipant:audioPaused:didSucceed:error:]_block_invoke.203
- ___63-[VCSession vcSessionParticipant:videoPaused:didSucceed:error:]_block_invoke.213
- ___64-[VCSession vcSessionParticipant:audioEnabled:didSucceed:error:]_block_invoke.175
- ___64-[VCSession vcSessionParticipant:videoEnabled:didSucceed:error:]_block_invoke.185
- ___65-[VCSession vcSessionParticipant:screenEnabled:didSucceed:error:]_block_invoke.190
- ___69-[VCSession rateController:targetBitrateDidChange:rateChangeCounter:]_block_invoke.255
- ___83-[VCSession vcSessionParticipant:mediaMixingDidChangeForMediaType:mixingMediaType:]_block_invoke.239
- ___84-[VCSession vcSessionParticipant:mediaStateDidChange:forMediaType:didSucceed:error:]_block_invoke.238
- ___block_literal_global.364
CStrings:
+ "2115.6.1"
+ "TB,N,V_forceL4SHighDataRate"
+ "VCRC [%s] %s:%d Set l4sHighDataRateEnabled=%d, estimator=%p"
+ "VCRateControlBandwidthEstimatorMap_SetL4SHighDataRateEnabled"
+ "VCRateControlBandwidthEstimator_SetL4SHighDataRateEnabled"
+ "VCStatisticsCollector_SetL4SHighDataRateEnabled"
+ "_forceHighDataRateFaceTime"
+ "_forceL4SHighDataRate"
+ "_l4SHighDataRateEnabled"
+ "_l4sHighDataRateEnabled"
+ "forceL4SHighDataRate"
+ "rateControlL4SHighDataRate"
+ "setForceL4SHighDataRate:"
- "2115.4.1"

```
