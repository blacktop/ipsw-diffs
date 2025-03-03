## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3404.71.4.1.1
-  __TEXT.__text: 0xb3bec
+3404.79.2.0.0
+  __TEXT.__text: 0xb45bc
   __TEXT.__auth_stubs: 0x1d90
-  __TEXT.__objc_methlist: 0xb968
+  __TEXT.__objc_methlist: 0xb9d0
   __TEXT.__const: 0x7e0
   __TEXT.__dlopen_cstrs: 0x174
   __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_typeref: 0x185
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__cstring: 0x139a5
+  __TEXT.__cstring: 0x13bdf
   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_reflstr: 0x84
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__gcc_except_tab: 0x3194
-  __TEXT.__oslogstring: 0xdde9
-  __TEXT.__unwind_info: 0x2fb8
+  __TEXT.__oslogstring: 0xdf2b
+  __TEXT.__unwind_info: 0x2fd0
   __TEXT.__eh_frame: 0xe8
-  __TEXT.__objc_classname: 0x1a0d
-  __TEXT.__objc_methname: 0x1f75a
-  __TEXT.__objc_methtype: 0x43a1
-  __TEXT.__objc_stubs: 0x104a0
-  __DATA_CONST.__got: 0xf10
-  __DATA_CONST.__const: 0x23a0
-  __DATA_CONST.__objc_classlist: 0x670
+  __TEXT.__objc_classname: 0x1a26
+  __TEXT.__objc_methname: 0x1f8e8
+  __TEXT.__objc_methtype: 0x43b4
+  __TEXT.__objc_stubs: 0x10580
+  __DATA_CONST.__got: 0xf20
+  __DATA_CONST.__const: 0x2440
+  __DATA_CONST.__objc_classlist: 0x678
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6790
+  __DATA_CONST.__objc_selrefs: 0x67c8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x4d8
   __DATA_CONST.__objc_arraydata: 0x198
   __AUTH_CONST.__auth_got: 0xee0
   __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__const: 0x1530
-  __AUTH_CONST.__cfstring: 0x8900
-  __AUTH_CONST.__objc_const: 0x12070
+  __AUTH_CONST.__const: 0x1550
+  __AUTH_CONST.__cfstring: 0x89c0
+  __AUTH_CONST.__objc_const: 0x12100
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x1b0
-  __AUTH.__objc_data: 0x4b0
+  __AUTH.__objc_data: 0x500
   __DATA.__objc_ivar: 0xbfc
   __DATA.__data: 0x12d8
-  __DATA.__bss: 0x8e8
+  __DATA.__bss: 0x8f8
   __DATA_DIRTY.__objc_data: 0x3c68
   __DATA_DIRTY.__data: 0x2c8
   __DATA_DIRTY.__bss: 0x360

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4461
-  Symbols:   5896
-  CStrings:  8585
+  Functions: 4471
+  Symbols:   5909
+  CStrings:  8611
 
Symbols:
+ _OBJC_CLASS_$_CSAssetTelemetryReporter
+ _OBJC_METACLASS_$_CSAssetTelemetryReporter
+ _kUAFAssetMetadataAssetSpecifierKey
CStrings:
+ "%s AOP listening property on notification : %{public}d"
+ "%s Generated core analytics payload for assetName: %@, assetConfigVersion: %@, asset map latency:%f"
+ "%s Generated core analytics payload for assetName: %@, assetConfigVersion: %@, errorDomain:%@ errorCode: %ld"
+ "%s Query value for listening property in AOP : %{public}d"
+ "%s Start monitoring : AOP Listening state"
+ "+[CSUtils(LanguageCode) getBestSupportedSiriLanguageWithFallback:]"
+ "-[CSAlwaysOnProcessorStateMonitor _startMonitoringWithQueue:]"
+ "-[CSAssetTelemetryReporter reportAssetMapFailTelemetryForError:assetSpecifier:assetConfigVersion:]_block_invoke"
+ "-[CSAssetTelemetryReporter reportAssetMapLatencyTelemetry:assetSpecifier:assetConfigVersion:]_block_invoke"
+ "-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke_3"
+ "CSAssetTelemetryReporter"
+ "_isAudioStreamTypeBuiltIn"
+ "_logMapFailTelemetryAndSubmitDiagnosticReportForError:assetSpecifier:assetConfigVersion:"
+ "_logMapOperationLatencyTelemetry:assetSpecifier:assetConfigVersion:"
+ "_mapVoiceTriggerAsset:asset:completion:"
+ "assetConfigVersion"
+ "assetSpecifier"
+ "com.apple.corespeech.secureasset.assetmapfailed"
+ "com.apple.corespeech.secureasset.exclavemaplatency"
+ "errorCode"
+ "errorDomain"
+ "getBestSupportedSiriLanguageWithFallback:"
+ "keywordDetectResult"
+ "reportAssetMapFailTelemetryForError:assetSpecifier:assetConfigVersion:"
+ "reportAssetMapLatencyTelemetry:assetSpecifier:assetConfigVersion:"
+ "sharedReporter"
+ "speakerDetectResult"
+ "submitSecureAssetMapFailDiagnosticReportForError:"
+ "v24@?0d8@\"NSError\"16"
+ "v28@0:8B16@?<v@?QQdIQQQQ>20"
+ "v40@0:8d16@24@32"
- "%s listening property in AOP : %{public}d"
- "-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:completion:]_block_invoke_3"
- "_fileAssetMapFailDiagnosticReport:"
- "_mapVoiceTriggerAsset:completion:"
- "v28@0:8B16@?<v@?QQdIQQ>20"

```
