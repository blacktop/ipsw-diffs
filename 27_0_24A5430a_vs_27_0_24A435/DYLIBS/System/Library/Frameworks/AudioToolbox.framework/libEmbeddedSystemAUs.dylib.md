## libEmbeddedSystemAUs.dylib

> `/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib`

```diff

 1638.104.3.0.0
-  __TEXT.__text: 0xd1554
-  __TEXT.__realtime: 0x38a84
+  __TEXT.__text: 0xd15a8
+  __TEXT.__realtime: 0x38ad0
   __TEXT.__const: 0xb344
   __TEXT.__dlopen_cstrs: 0x2c1
-  __TEXT.__gcc_except_tab: 0x77d0
+  __TEXT.__gcc_except_tab: 0x77d8
   __TEXT.__cstring: 0xa0c9
   __TEXT.__oslogstring: 0xc167
-  __TEXT.__unwind_info: 0x4700
+  __TEXT.__unwind_info: 0x4708
   __TEXT.__eh_frame: 0x108
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xe70
Functions:
~ __ZN19AUMultiChannelMixer9MixerCore8SumInputEjP31AUMultiChannelMixerInputElementRK24CAStreamBasicDescriptionNS3_15CommonPCMFormatEP15AudioBufferListjffjb : 1712 -> 1716
~ __ZN7MixLoopI10MCF32toF32E9MonoUnityINS1_6AssignEEEvjPKfjPfj : 76 -> 84
~ __ZN25MCM3DynamicStateAllocator17_CheckAllocationsEv : 2272 -> 2276
~ __ZN9AUNBandEQ10InitializeEv : 872 -> 868
~ __ZN9AUNBandEQ5ResetEjj : 580 -> 588
~ __ZN5ausdk9AUElement20UseIndexedParametersEj : 316 -> 304
~ __ZN8TFileBSD18AsyncFileIOHandlerEPv : 552 -> 556
~ __ZN16TArrayMarshallerIjE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerIiE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerIyE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerIfE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerI15AudioValueRangeE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerI19AudioFormatListItemE11DeserializeER14CADeserializerRPvRj : 188 -> 192
~ __ZN16TArrayMarshallerI27AudioStreamBasicDescriptionE11DeserializeER14CADeserializerRPvRj : 188 -> 192
~ __ZN16TArrayMarshallerI31AudioStreamPacketDependencyInfoE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerI16ProfileLevelInfoE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerI10OriginInfoE11DeserializeER14CADeserializerRPvRj : 188 -> 192
~ __ZN16TArrayMarshallerI20SplicingRequirementsE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN15PhaseVocoderTwo10CopyOutputERjP15AudioBufferListRd : 1396 -> 1388
~ __ZNSt3__16vectorIP9DlsRegionNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 184 -> 176
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJjEEEPjDpOT_ : 184 -> 176
~ __ZN15MatrixMixerCore18ResetInputMeteringEt : 80 -> 84
~ __ZN15MatrixMixerCore19ResetOutputMeteringEt : 80 -> 84
~ __ZN9DLSSample13GetMoreFramesEyyPv : 280 -> 284
~ __ZN12SFCollection16GetPresetGenItemEiiiR9SFGenItem : 340 -> 336
~ __ZlsR12CASerializerRKPK10__CFString : 204 -> 208
~ __ZNSt3__16vectorIP9StateViewN5caulk12rt_allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 212 -> 216
~ __ZN11GlobalState25RestoreWithoutGlobalStateERK14CACFDictionary : 4216 -> 4212
~ __ZN10FileSample11LoadFromURLEPK7__CFURLb : 12740 -> 12744
~ __ZNKSt3__111basic_regexIcNS_12regex_traitsIcEEE21__match_at_start_ecmaINS_9allocatorINS_9sub_matchIPKcEEEEEEbS8_S8_RNS_13match_resultsIS8_T_EENS_15regex_constants15match_flag_typeEb : 1264 -> 1256
~ __ZNSt3__16vectorINS_9sub_matchIPKcEENS_9allocatorIS4_EEE6assignEmRKS4_ : 340 -> 336
~ __ZNKSt3__111basic_regexIcNS_12regex_traitsIcEEE16__match_at_startINS_9allocatorINS_9sub_matchIPKcEEEEEEbS8_S8_RNS_13match_resultsIS8_T_EENS_15regex_constants15match_flag_typeEb : 4968 -> 5004
~ __ZNSt3__15dequeINS_7__stateIcEENS_9allocatorIS2_EEE9push_backEOS2_ : 788 -> 792
~ __ZNSt3__114__split_bufferIPNS_7__stateIcEERNS_9allocatorIS3_EEE12emplace_backIJS3_EEEvDpOT_ : 248 -> 252
~ __ZN10LayerState29LoadFromEXS24GroupAndDefaultsERK12SamplerGroupRK15SamplerDefaultsRj : 15432 -> 15408
~ __ZNSt3__16vectorIN9AUNBandEQ9PolarDescENS_9allocatorIS2_EEE6resizeEm : 356 -> 360
~ __ZN9AUNBandEQ11GetPropertyEjjjPv : 1628 -> 1640
~ __ZN14AURoundTripAAC20MatchParamsForPresetEi : 172 -> 180
~ __ZN14AURoundTripAAC12RestoreStateEPKv : 368 -> 372
~ __ZN10PowerMeter7ProcessEPKfii : 776 -> 780
~ __ZNK5ausdk9AUElement19GetParameterOrErrorEj : 148 -> 152
~ __ZN5ausdk9AUElement19SetParameterOrErrorEjfb : 980 -> 992
~ __ZN9AUNBandEQ18ProcessBufferListsERjRK15AudioBufferListRS1_j : 2780 -> 2784
~ __ZN11SamplerNote6RenderEyjPP15AudioBufferListjj : 5488 -> 5480
~ __ZN9VoiceZone12NewVoiceZoneEP11SamplerNoteP9ZoneStateffj : 5260 -> 5264
~ __ZN7AUPitch6RenderERjRK14AudioTimeStampj : 16268 -> 16248
~ __ZN7AUPitch17BypassBufferArray10PullOutputEPN5ausdk15AUOutputElementEPj : 416 -> 428
~ __ZN13AUMatrixMixer12GetParameterEjjjRf : 1484 -> 1492
~ __ZN13Biquad_8dot2438Process16InterleavedTo824DeinterleavedEPKsPijjjRNS_5StateE : 192 -> 204
~ __ZN17AudioStreamerImpl12RefillBufferEj : 856 -> 844
~ __ZN13ABLRingBufferIfE8ReadFromEjP15AudioBufferList : 400 -> 404
~ __ZN12AUSimpleTime6RenderERjRK14AudioTimeStampj : 3296 -> 3312
~ __ZN10PowerMeter13Process_Int16EPKsii : 164 -> 168
~ __ZN10PowerMeter13Process_Int32EPKiii : 168 -> 172
~ __ZN18AUMatrixReverbLite26ProcessMultipleBufferListsERjjjPPK15AudioBufferListjPPS1_ : 4464 -> 4496
~ __ZN11AUVarispeed6RenderERjRK14AudioTimeStampj : 2368 -> 2364
```
