## vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

-904.0.0.0.0
-  __TEXT.__text: 0x9a184
+905.0.0.0.0
+  __TEXT.__text: 0x9c4c8
   __TEXT.__auth_stubs: 0x1850
-  __TEXT.__objc_stubs: 0xb900
+  __TEXT.__objc_stubs: 0xb940
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x646c
-  __TEXT.__cstring: 0x43ca
-  __TEXT.__objc_classname: 0xc95
-  __TEXT.__objc_methname: 0xee3b
-  __TEXT.__objc_methtype: 0x2faa
+  __TEXT.__objc_methlist: 0x64f4
+  __TEXT.__cstring: 0x43ea
+  __TEXT.__objc_classname: 0xcaf
+  __TEXT.__objc_methname: 0xf09a
+  __TEXT.__objc_methtype: 0x2fe6
   __TEXT.__const: 0x5a6
-  __TEXT.__gcc_except_tab: 0xc018
-  __TEXT.__oslogstring: 0x10277
+  __TEXT.__gcc_except_tab: 0xc408
+  __TEXT.__oslogstring: 0x10827
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x3b
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x32f8
+  __TEXT.__unwind_info: 0x33f0
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0xc40
   __DATA_CONST.__got: 0x7a0
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x2a38
-  __DATA_CONST.__cfstring: 0x4f40
-  __DATA_CONST.__objc_classlist: 0x280
+  __DATA_CONST.__const: 0x2c18
+  __DATA_CONST.__cfstring: 0x4f60
+  __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_intobj: 0x348
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xe938
-  __DATA.__objc_selrefs: 0x3b88
-  __DATA.__objc_ivar: 0x5f0
-  __DATA.__objc_data: 0x1960
+  __DATA.__objc_const: 0xeaa8
+  __DATA.__objc_selrefs: 0x3bd0
+  __DATA.__objc_ivar: 0x604
+  __DATA.__objc_data: 0x19b0
   __DATA.__data: 0x10a0
-  __DATA.__bss: 0x380
+  __DATA.__bss: 0x3c0
   __DATA.__common: 0x4
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 02AE031B-8A41-38B3-9DB5-F3D789219764
-  Functions: 2770
+  UUID: 56987C83-E02F-3825-B76B-30C44D581B33
+  Functions: 2805
   Symbols:   698
-  CStrings:  5485
+  CStrings:  5532
 
CStrings:
+ "+"
+ "<%@ %p> Adding asset model network observer"
+ "<%@ %p> Removing asset model network observer"
+ "<%@ %p> Speech locale %@, language %@, language identifier %@, GASR available: %@, pers transcription available: %@"
+ "<%@ %p> isDictationModelInstalled %@ [self language: %@, speech language: %@, installed assets: %@]"
+ "@\"VMTranscriptionAssetModel\""
+ "Completed InstallAssetModel - end, installed: %@"
+ "Completed InstallAssetModelWithType - end, installed: %@"
+ "Completed transcription model install operation, speech dictation model is available already"
+ "Completed transcription model install operation, speechRecognizer is nil"
+ "Executing InstallAssetModel - begin, isLID: %@"
+ "Executing InstallAssetModelWithType - begin, assetModelType: %lu, language: %@"
+ "InstallAsset: language %@, supportsOnDeviceRecognition %@"
+ "Network asset model observer available: %@"
+ "Requested InstallAssetModel, isLID: %@"
+ "Requested InstallAssetModelWithType, assetModelType: %lu, language: %@"
+ "Retrieving dictation for file at %@, locale %@, type %lu"
+ "Speech Asset Model install operation completed, success: %@."
+ "Starting LID model install operation"
+ "Starting SpeechAssetWithConfig model install operation for language: %@, taskHint: %ld"
+ "Starting fetchAssetsForLanguage %@"
+ "T@\"NSLocale\",R,N,V_matchedSystemLocale"
+ "T@\"VMTranscriptionAssetModel\",R,N,V_assetModel"
+ "TB,N,V_transcriptionAssetModelInstalling"
+ "TB,N,V_transcriptionAssetModelObservingNetwork"
+ "TB,N,V_transcriptionAssetModelWithTypeInstalling"
+ "TB,R,N,GisGasrModelAvailable,V_gasrModelAvailable"
+ "TB,R,N,GisPersTranscriptionAvailable,V_persTranscriptionAvailable"
+ "VMTranscriptionAssetModel"
+ "VMTranscriptionAssetModel.InstallAsset: Flag lvmExpansionLiveOnEnabled enabled"
+ "VMTranscriptionAssetModel.InstallSpeechAsset: fetchAssetWithConfig for %@"
+ "VMTranscriptionAssetModel: invalid VMAssetModelType %@"
+ "_assetModel"
+ "_installAsset:completion:"
+ "_installAssetForLanguage:speechRecognizer:completion:"
+ "_installAssetModel:isLID:completion:"
+ "_installAssetModelWithType:speechTaskHint:language:completion:"
+ "_installLIDAsset:"
+ "_installSpeechAssetWithConfig:speechTaskHint:completion:"
+ "_transcriptionAssetModelInstalling"
+ "_transcriptionAssetModelObservingNetwork"
+ "_transcriptionAssetModelWithTypeInstalling"
+ "addAssetModelNetworkObserver"
+ "assetModel"
+ "com.apple.voicemail.%@"
+ "invalid VMAssetModelType %@"
+ "performInstallAssetModel:isLID:queue:completion:"
+ "performInstallAssetModelWithType:speechTaskHint:language:queue:completion:"
+ "removeAssetModelNetworkObserver"
+ "setTranscriptionAssetModelInstalling:"
+ "setTranscriptionAssetModelObservingNetwork:"
+ "setTranscriptionAssetModelWithTypeInstalling:"
+ "transcriptionAssetModelInstalling"
+ "transcriptionAssetModelInstalling changed to %@"
+ "transcriptionAssetModelObservingNetwork"
+ "transcriptionAssetModelWithTypeInstalling"
+ "transcriptionAssetModelWithTypeInstalling changed to %@"
+ "tspt.asr"
+ "tspt.lid"
+ "tspt.mdl"
+ "v36@0:8@16B24@?28"
+ "v44@0:8@16B24@28@?36"
+ "v48@0:8q16q24@32@?40"
+ "v56@0:8q16q24@32@40@?48"
- "*"
- "@\"VMTranscriptionAssetModelOperation\""
- "@32@0:8@16@?24"
- "Asset model operation exists %@ and is executing (%@)."
- "Asset model operation is already in progress"
- "T@\"NSLocale\",C,N,V_matchedSystemLocale"
- "T@\"VMTranscriptionAssetModelOperation\",W,N,V_transcriptionAssetModelOperation"
- "TB,N,GisGasrModelAvailable,V_gasrModelAvailable"
- "TB,N,GisPersTranscriptionAvailable,V_persTranscriptionAvailable"
- "_transcriptionAssetModelOperation"
- "assetModelOperationWithCompletion:completion:"
- "requestAssetModelOperationWithCompletion:completion:"
- "setGasrModelAvailable:"
- "setMatchedSystemLocale:"
- "setPersTranscriptionAvailable:"
- "setTranscriptionAssetModelOperation:"
- "transcriptionAssetModelOperation"
- "transcriptionAssetModelOperationWithCompletion:"

```
