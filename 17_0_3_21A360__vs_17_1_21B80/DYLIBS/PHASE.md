## PHASE

> `/System/Library/Frameworks/PHASE.framework/PHASE`

```diff

-249.30.1.0.0
-  __TEXT.__text: 0x1dc1b8
-  __TEXT.__auth_stubs: 0x1860
+265.0.0.0.0
+  __TEXT.__text: 0x1dd668
+  __TEXT.__auth_stubs: 0x18b0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x4b7c
-  __TEXT.__const: 0x2e4c
-  __TEXT.__gcc_except_tab: 0x1e718
-  __TEXT.__oslogstring: 0x1ac95
-  __TEXT.__cstring: 0x1035a
-  __TEXT.__unwind_info: 0xa158
+  __TEXT.__const: 0x2e0c
+  __TEXT.__gcc_except_tab: 0x1e7f0
+  __TEXT.__oslogstring: 0x1b1d5
+  __TEXT.__cstring: 0x1039f
+  __TEXT.__unwind_info: 0xa17c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0xc59
-  __TEXT.__objc_methname: 0xafc6
+  __TEXT.__objc_methname: 0xafd4
   __TEXT.__objc_methtype: 0x582d
-  __TEXT.__objc_stubs: 0x6400
-  __DATA_CONST.__got: 0x230
+  __TEXT.__objc_stubs: 0x6420
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0xe08
   __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x6810
-  __DATA_CONST.__objc_selrefs: 0x23d0
+  __DATA_CONST.__objc_selrefs: 0x23d8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__const: 0x98b8
-  __AUTH_CONST.__cfstring: 0x4460
+  __AUTH_CONST.__const: 0x98f8
+  __AUTH_CONST.__cfstring: 0x4480
   __AUTH_CONST.__objc_const: 0x3918
   __AUTH_CONST.__auth_ptr: 0xb0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0xc40
+  __AUTH_CONST.__auth_got: 0xc68
   __AUTH.__objc_data: 0x2670
   __DATA.__got_weak: 0x8
   __DATA.__objc_protorefs: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 8128
-  Symbols:   21690
-  CStrings:  5679
+  Functions: 8133
+  Symbols:   21710
+  CStrings:  5701
 
Symbols:
+ GCC_except_table164
+ GCC_except_table227
+ _.str.110
+ _.str.33
+ _.str.43
+ _.str.55
+ _.str.85
+ __ZN5Phase10Controller11Spatializer6CreateINS0_19BinauralSpatializerEJNS1_14InitParametersEN2IR16IRDataAttributesEbEEEPS1_DpT0_
+ __ZN5Phase10Controller17StreamSamplerBase15InternalSeekDVMEd
+ __ZN5Phase10Controller19BinauralSpatializerC2ERKNS0_11Spatializer14InitParametersERKN2IR16IRDataAttributesEb
+ __ZN5Phase10Controller29InitializeBinauralSpatializerEPPNS0_11SpatializerERKNS1_14InitParametersEb
+ __ZN5Phase14PhaseOSCBundle16WriteNextMessageINS_10Controller6DVM_RT16DVMNRTOSCCommandEJPNS_8DspLayer9VoicePoolExiEEEiT_DpT0_
+ __ZN5Phase7CommandILi128EE7InvokerIPFvPPNS_10Controller11SpatializerERKNS4_14InitParametersEbEJvS6_S7_bEE4CallEv
+ __ZN5Phase7CommandILi128EE7InvokerIPFvPPNS_10Controller11SpatializerERKNS4_14InitParametersEbEJvS6_S7_bEED0Ev
+ __ZN5Phase7CommandILi128EE7InvokerIPFvPPNS_10Controller11SpatializerERKNS4_14InitParametersEbEJvS6_S7_bEED1Ev
+ __ZN5caulk10concurrent9messenger7enqueueERNS0_7messageE
+ __ZN5caulk15deferred_logger14create_messageEm13os_log_type_t
+ __ZN5caulk15deferred_logger8create_vEPv
+ __ZNK5Phase10Controller13SystemAudioIO11AudioIOBase11IOProcErrorIJEEEvPKcDpOT_
+ __ZNK5Phase10Controller13SystemAudioIO11AudioIOBase11IOProcErrorIJRKiRKjEEEvPKcDpOT_
+ __ZNK5Phase10Controller13SystemAudioIO11AudioIOUnit17GetLastFrameCountEv
+ __ZNK5Phase10Controller13SystemAudioIO22AudioIOPlatformAdapter17GetLastFrameCountEv
+ __ZNKSt3__18functionIFvPfmEEclES1_m
+ __ZTVN5Phase7CommandILi128EE7InvokerIPFvPPNS_10Controller11SpatializerERKNS4_14InitParametersEbEJvS6_S7_bEEE
+ __os_log_default
+ __os_log_pack_fill
+ __os_log_pack_size
+ _objc_msgSend$mainMixerNode
- GCC_except_table228
- _.str.109
- _.str.42
- _.str.54
- _.str.84
- __ZN5Phase10Controller11Spatializer6CreateINS0_19BinauralSpatializerEJNS1_14InitParametersEN2IR16IRDataAttributesEEEEPS1_DpT0_
- __ZN5Phase10Controller15DSPVoiceManager14Implementation14IORenderOutputEx
- __ZN5Phase10Controller19BinauralSpatializerC2ERKNS0_11Spatializer14InitParametersERKN2IR16IRDataAttributesE
- __ZN5Phase10Controller29InitializeBinauralSpatializerEPPNS0_11SpatializerERKNS1_14InitParametersE
- __ZN5Phase13CalendarQueueILi32ELi256ENS_10Controller6DVM_RT12SamplerStateEE5ClearEv
- __ZN5Phase13CalendarQueueILi32ELi256EPNSt3__18functionIFvPfmEEEE5ClearEv
- __ZN5Phase13CalendarQueueILi64ELi512ENS_10Controller6DVM_RT7OSCDataEE5ClearEv
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIN5Phase14UniqueObjectIdENS_10shared_ptrINS2_16ActionTreeObjectEEEEENS_22__unordered_map_hasherIS3_S7_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S7_SC_SA_Lb1EEENS_9allocatorIS7_EEE5clearEv
CStrings:
+ "%25s:%-5d (sound event: %llu) - sound event was stopped by engine teardown"
+ "%25s:%-5d (sound event: %llu) - the sound event state should be stopped prior to its teardown. (rendering state: %s)"
+ "%25s:%-5d Added child %@ to parent %@"
+ "%25s:%-5d Created %@"
+ "%25s:%-5d DVM-RT is reset @ Frame %llu"
+ "%25s:%-5d DVM_NRT unable to reserve %iB in message pipe to DVM_RT after %llims. Pipe has only %zuB available, will stop trying."
+ "%25s:%-5d Destroyed %@"
+ "%25s:%-5d EXCEPTION (IdAlreadyExists) [not addSubmixResult.IsOkay() is true]: \"mpDspVoiceManager->AddSubmix() failed with error code: %hhd\""
+ "%25s:%-5d NRT set %s vid %llu (on %sId %llu) to %s with %.3f sec. delay."
+ "%25s:%-5d NRT state set to %s, for DspNode type %s, id %llu with %.3f sec. delay."
+ "%25s:%-5d Removed child %@ from parent %@"
+ "%25s:%-5d Setting reverb to Environment10"
+ "%25s:%-5d VoiceEngineCallback: the IConvolver (%p):%llu is NULL @ Frame %llu"
+ "%25s:%-5d VoiceEngineCallback: the PullStreamSampler (%p):%llu does not exist in DVM_RT.mSamplerMap @ Frame %llu"
+ "%25s:%-5d VoiceEngineCallback: the PushStreamSampler (%p):%llu does not exist in DVM_RT.mSamplerMap @ Frame %llu"
+ "%25s:%-5d VoiceEngineCallback: the ResidentSampler (%p):%llu does not exist in DVM_RT.mSamplerMap @ Frame %llu"
+ "%25s:%-5d VoiceEngineCallback: the Tapper (%p):%llu does not exist in DVM_RT.mTapperMap @ Frame %llu"
+ "%25s:%-5d [AudioIO::EndRouteChange] invalid mSuspendIOSemaphore value. Was the route change interrupted?"
+ "%25s:%-5d graph@%p: can't add a generatorId %llu, to a submixId %llu that is stopping!!"
+ "%25s:%-5d impl@%p: configuring with sample rate %.f Hz, channels [out %d, in %d]"
+ "<invalid render group index>"
+ "AudioIOPlatformAdapter: skipping IO input cycle at host time %llu for %u frames"
+ "AudioIOPlatformAdapter: skipping IO output cycle at host time %llu for %u frames"
+ "AudioIOUnit: skipping IO input cycle at host time %llu for %u frames"
+ "AudioIOUnit: skipping IO output cycle at host time %llu for %u frames"
+ "DVM_RT_VoiceEngineCallback.cpp"
+ "Environment10"
+ "mainMixerNode"
+ "mpDspVoiceManager->AddSubmix() failed with error code: %hhd"
- "%25s:%-5d (sound event: %llu) - Rendering state should be 'stopped' prior to invoking internalCleanup(). Ensure that sound events are stopped and invalidated prior to stopping the engine. (rendering state: %s)"
- "%25s:%-5d DVM_NRT unable to reserve %iB in message pipe to DVM_RT after %llims. Pipe is full!"
- "%25s:%-5d NRT set %s vid %llu (on %sId %llu) to %s. \n"
- "%25s:%-5d NRT state set to %s, for DspNode type %s, id %llu \n"
- "%25s:%-5d Setting reverb to LargeRoom. In the future, return Environment10"
- "%25s:%-5d mpDspVoiceManager->AddSubmix() failed with error code: %hhd"
- "(%d): impl@%p: [IO] st@%u: -> DVM has 0 current frames to render"

```
