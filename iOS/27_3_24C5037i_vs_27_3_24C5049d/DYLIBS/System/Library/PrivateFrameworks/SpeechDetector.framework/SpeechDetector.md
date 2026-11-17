## SpeechDetector

> `/System/Library/PrivateFrameworks/SpeechDetector.framework/SpeechDetector`

```diff

-3610.11.1.0.0
-  __TEXT.__text: 0x19b4
-  __TEXT.__objc_methlist: 0x484
+3610.19.5.0.0
+  __TEXT.__text: 0x1a18
+  __TEXT.__objc_methlist: 0x49c
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x541
   __TEXT.__oslogstring: 0x20c
-  __TEXT.__unwind_info: 0xf8
+  __TEXT.__unwind_info: 0x108
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d0
+  __DATA_CONST.__objc_selrefs: 0x3f0
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x220
   __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0x910
+  __AUTH_CONST.__objc_const: 0x920
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0x0

   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 61
-  Symbols:   245
+  Functions: 63
+  Symbols:   247
   CStrings:  88
 
Symbols:
+ -[OSDAnalyzer _setupCaesuraSPGWithConfigFile:sampleRate:osdAnalyzerAssetLocker:quietRowsPerCompute:quietResumeAfterSilenceMs:]
+ -[OSDAnalyzer initWithConfigFile:sampleRate:context:queue:delegate:osdAnalyzerAssetLocker:quietRowsPerCompute:quietResumeAfterSilenceMs:]
+ -[OSDAnalyzer quietModeRows]
- -[OSDAnalyzer _setupCaesuraSPGWithConfigFile:sampleRate:osdAnalyzerAssetLocker:]
Functions:
~ -[OSDAnalyzer initWithConfigFile:sampleRate:context:queue:delegate:osdAnalyzerAssetLocker:] : 368 -> 36
- -[OSDAnalyzer _setupCaesuraSPGWithConfigFile:sampleRate:osdAnalyzerAssetLocker:]
+ -[OSDAnalyzer initWithConfigFile:sampleRate:context:queue:delegate:osdAnalyzerAssetLocker:quietRowsPerCompute:quietResumeAfterSilenceMs:]
+ -[OSDAnalyzer quietModeRows]
+ -[OSDAnalyzer _setupCaesuraSPGWithConfigFile:sampleRate:osdAnalyzerAssetLocker:quietRowsPerCompute:quietResumeAfterSilenceMs:]
```
