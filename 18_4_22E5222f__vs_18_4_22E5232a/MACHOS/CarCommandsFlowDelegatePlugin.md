## CarCommandsFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin`

```diff

-3404.26.1.0.0
-  __TEXT.__text: 0x14d418
-  __TEXT.__auth_stubs: 0x3400
+3404.26.2.0.0
+  __TEXT.__text: 0x151060
+  __TEXT.__auth_stubs: 0x3430
   __TEXT.__objc_stubs: 0x6e0
   __TEXT.__objc_methlist: 0xd70
-  __TEXT.__const: 0xb1f4
+  __TEXT.__const: 0xb374
   __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__objc_methname: 0x2366
-  __TEXT.__cstring: 0x1217d
+  __TEXT.__objc_methname: 0x240e
+  __TEXT.__cstring: 0x1267d
   __TEXT.__oslogstring: 0x84f
   __TEXT.__objc_classname: 0x1a4
   __TEXT.__objc_methtype: 0x99a
-  __TEXT.__constg_swiftt: 0x6ed8
-  __TEXT.__swift5_typeref: 0x46c8
-  __TEXT.__swift5_fieldmd: 0x3aa8
+  __TEXT.__constg_swiftt: 0x703c
+  __TEXT.__swift5_typeref: 0x4758
+  __TEXT.__swift5_fieldmd: 0x3b78
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x4013
+  __TEXT.__swift5_reflstr: 0x4163
   __TEXT.__swift5_assocty: 0x11c8
-  __TEXT.__swift5_proto: 0x9b0
-  __TEXT.__swift5_types: 0x3f8
-  __TEXT.__swift5_protos: 0x144
-  __TEXT.__swift_as_entry: 0xdb8
-  __TEXT.__swift_as_ret: 0x1210
+  __TEXT.__swift5_proto: 0x9bc
+  __TEXT.__swift5_types: 0x404
+  __TEXT.__swift5_protos: 0x148
+  __TEXT.__swift_as_entry: 0xe00
+  __TEXT.__swift_as_ret: 0x1264
   __TEXT.__swift5_capture: 0x5bc
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x6d30
-  __TEXT.__eh_frame: 0x137d8
-  __DATA_CONST.__auth_got: 0x1a10
-  __DATA_CONST.__got: 0xb20
-  __DATA_CONST.__auth_ptr: 0x1e10
-  __DATA_CONST.__const: 0xa5d8
+  __TEXT.__unwind_info: 0x6ea8
+  __TEXT.__eh_frame: 0x13d58
+  __DATA_CONST.__auth_got: 0x1a28
+  __DATA_CONST.__got: 0xb28
+  __DATA_CONST.__auth_ptr: 0x1800
+  __DATA_CONST.__const: 0xa818
   __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x290
+  __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x5978
-  __DATA.__objc_selrefs: 0xca0
+  __DATA.__objc_const: 0x5ad0
+  __DATA.__objc_selrefs: 0xcd0
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x21f0
-  __DATA.__data: 0xc268
+  __DATA.__data: 0xc4a8
   __DATA.__common: 0x448
   __DATA.__bss: 0xd200
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8659
-  Symbols:   345
-  CStrings:  1977
+  Functions: 8780
+  Symbols:   346
+  CStrings:  2009
 
Symbols:
+ _OBJC_CLASS_$_CAFNowPlaying
CStrings:
+ " converted to khz: "
+ " does not have band and frequency. Not attempting to tune by frequency"
+ "$__lazy_storage_$_audioSource"
+ "$__lazy_storage_$_hasChannelAndBandFromEntitySpans"
+ "$__lazy_storage_$_hasFrequencyAndBandFromEntitySpans"
+ "$__lazy_storage_$_hasRadioBandFromEntitySpans"
+ "$__lazy_storage_$_radioStationBandFromEntitySpans"
+ "$__lazy_storage_$_radioStationCallSignFromEntitySpans"
+ "$__lazy_storage_$_radioStationChannelFromEntitySpans"
+ "$__lazy_storage_$_radioStationFrequencyFromEntitySpans"
+ "$__lazy_storage_$_radioStationNameFromEntitySpans"
+ ", expected SetCarRadioStationIntent"
+ ". Not attempting to tune by frequency"
+ "/Library/Caches/com.apple.xbs/Sources/SiriCarCommands/CarCommandsFlowDelegatePlugin/Flow/SetCarAudioSourceAction/SetCarAudioSourceAction.swift"
+ "/Library/Caches/com.apple.xbs/Sources/SiriCarCommands/CarCommandsFlowDelegatePlugin/IntentHandling/Protocols/CarRadio/CarAudioSourceControllerProtocol.swift"
+ "Could not find matching audio source for band: "
+ "Could not resolve radio or nowPlaying when changing audio source"
+ "Found matching media sources: "
+ "No audio sources available"
+ "No band when switching audio source"
+ "No matching audio source for band: "
+ "No matching media sources for band: "
+ "No valid radio station band found in IntentRadioBand"
+ "Siri parse frequency: "
+ "Station has identifier. Not attempting to tune by frequency"
+ "Switching audio source to "
+ "Trying to play the current audio source"
+ "_TtC29CarCommandsFlowDelegatePlugin23SetCarAudioSourceAction"
+ "_audioSources"
+ "asCarRadioStationBand"
+ "carAudioSourceController"
+ "carService"
+ "changeMediaSourceWithIdentifier:completion:"
+ "currentMediaSourceIdentifier"
+ "floatValue"
+ "isMalformedPlayRadioStationTask(task:)"
+ "matchingMediaSourcesFromBand(_:)"
+ "mediaSourceIdentifierForFrequencyTuning(_:)"
+ "nowPlaying"
+ "nowPlayingInformation"
+ "playAudioSource(_:)"
+ "setCarAudioSource"
+ "tuneToFrequency:inSourceWithIdentifier:completion:"
+ "✅ Tuning via frequency: "
- "$__lazy_storage_$_hasChannelAndBand"
- "$__lazy_storage_$_hasFrequencyAndBand"
- "$__lazy_storage_$_radioStationBand"
- "$__lazy_storage_$_radioStationCallSign"
- "$__lazy_storage_$_radioStationChannel"
- "$__lazy_storage_$_radioStationFrequency"
- "$__lazy_storage_$_radioStationName"
- ". This may be a sign Siri is trying to tune to a bogus station"
- "/Library/Caches/com.apple.xbs/Sources/SiriCarCommands/CarCommandsFlowDelegatePlugin/IntentHandling/Protocols/CarRadio/SetCarRadioStationIntent+CarRadioStation.swift"
- "No valid radio station band found in "
- "isMalformedRadioTask(task:)"
- "radioStationBand"
- "⚠️ Did not find exact radio entity span matches: "

```
