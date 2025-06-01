## sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

-3300.99.1.1.1
-  __TEXT.__text: 0x224d4
-  __TEXT.__auth_stubs: 0x1a70
+3301.11.1.0.0
+  __TEXT.__text: 0x2277c
+  __TEXT.__auth_stubs: 0x1a90
   __TEXT.__objc_methlist: 0x16c
   __TEXT.__const: 0x448
-  __TEXT.__objc_methname: 0x720
-  __TEXT.__swift5_typeref: 0x54f
-  __TEXT.__cstring: 0x1b4d
+  __TEXT.__objc_methname: 0x6f1
+  __TEXT.__swift5_typeref: 0x561
+  __TEXT.__cstring: 0x1b6d
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x4cc
   __TEXT.__swift5_reflstr: 0x1d4

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__oslogstring: 0x3b
-  __TEXT.__unwind_info: 0x4f0
+  __TEXT.__unwind_info: 0x4ec
   __TEXT.__eh_frame: 0x3f0
-  __DATA_CONST.__auth_got: 0xd38
-  __DATA_CONST.__got: 0x260
+  __DATA_CONST.__auth_got: 0xd48
+  __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0xd98
+  __DATA_CONST.__const: 0xda0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xce0
-  __DATA.__objc_selrefs: 0x1d0
+  __DATA.__objc_selrefs: 0x1b8
   __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0x80
+  __DATA.__objc_classrefs: 0x78
   __DATA.__objc_data: 0x5b0
-  __DATA.__data: 0xa88
+  __DATA.__data: 0xa98
   __DATA.__common: 0x60
   __DATA.__bss: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CAA1B266-ED95-3AA7-863A-F9D47FB13D3B
+  UUID: FFC6F977-A213-3CBB-BACD-D01BEE6F2A9E
   Functions: 449
-  Symbols:   572
-  CStrings:  282
+  Symbols:   575
+  CStrings:  280
 
Symbols:
+ _$s14SiriTTSService11NeuralUtilsC15compileANEModel9voicePathySS_tKFZ
+ _$s14SiriTTSService11NeuralUtilsC18isANEModelCompiled9voicePathSbSS_tFZ
+ _$s14SiriTTSService11NeuralUtilsC24isANECompilationPlatformSbvgZ
+ _$s14SiriTTSService11NeuralUtilsC6sharedACvgZ
+ _$s14SiriTTSService11NeuralUtilsCAA0C14VoiceUtilitiesAAWP
+ _$s14SiriTTSService11NeuralUtilsCMa
+ _$s14SiriTTSService20NeuralVoiceUtilitiesMp
+ _$s14SiriTTSService20NeuralVoiceUtilitiesP17currentSampleRate9voicePathSfSS_tFTj
+ _$s14SiriTTSService27SynthesizingRequestProtocolPAAE19disableCompactVoiceSbvg
- _$s14SiriTTSService11NeuralUtilsV15compileANEModel9voicePathySS_tKFZ
- _$s14SiriTTSService11NeuralUtilsV18isANEModelCompiled9voicePathSbSS_tFZ
- _$s14SiriTTSService11NeuralUtilsV24isANECompilationPlatformSbvgZ
- _$s14SiriTTSService20VoiceSelectionActionC06selectC07requestAA09SynthesisC0CSgAA27SynthesizingRequestProtocol_AA04BaseJ0CXc_tFTj
- _$sSo25NSProcessInfoThermalStateV14SiriTTSServiceE11descriptionSSvg
- _OBJC_CLASS_$_NSProcessInfo
CStrings:
+ "Prefer device synthesis due to high neural voice sampling rate: %f"
+ "Prefer osprey synthesis due to low neural voice sampling rate: %f"
+ "Unable to create audio workflow"
- "Prefer device synthesis since neural voice is available and good conditions"
- "Prefer osprey synthesis due to thermal condition: %s, isLowPowerMode: %{bool}d"
- "isLowPowerModeEnabled"
- "processInfo"
- "thermalState"

```
