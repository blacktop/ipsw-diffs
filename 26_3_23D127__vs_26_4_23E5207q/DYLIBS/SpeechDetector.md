## SpeechDetector

> `/System/Library/PrivateFrameworks/SpeechDetector.framework/SpeechDetector`

```diff

-3515.11.1.0.0
-  __TEXT.__text: 0x19c0
-  __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_methlist: 0x454
-  __TEXT.__const: 0x44
+3520.87.3.1.5
+  __TEXT.__text: 0x1d30
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__objc_methlist: 0x484
+  __TEXT.__const: 0x84
   __TEXT.__cstring: 0x535
   __TEXT.__oslogstring: 0x20c
-  __TEXT.__unwind_info: 0xf8
+  __TEXT.__unwind_info: 0x130
   __TEXT.__objc_classname: 0xb3
-  __TEXT.__objc_methname: 0xdcc
-  __TEXT.__objc_methtype: 0x311
-  __TEXT.__objc_stubs: 0x840
+  __TEXT.__objc_methname: 0xee5
+  __TEXT.__objc_methtype: 0x341
+  __TEXT.__objc_stubs: 0x8a0
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a8
+  __DATA_CONST.__objc_selrefs: 0x3d0
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x170
+  __AUTH_CONST.__auth_got: 0x160
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0x8e0
+  __AUTH_CONST.__objc_const: 0x910
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x258
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 83C81279-3941-3DBE-8125-28B2FF900934
-  Functions: 57
-  Symbols:   358
-  CStrings:  379
+  UUID: BC862A19-50CE-354D-925E-B4B56A2A4F5B
+  Functions: 61
+  Symbols:   370
+  CStrings:  388
 
Symbols:
+ -[OSDAnalyzer _setupCaesuraSPGWithConfigFile:sampleRate:osdAnalyzerAssetLocker:]
+ -[OSDAnalyzer _setupOEPAssetManagerWithOSDAnalyzerAssetLocker:]
+ -[OSDAnalyzer initWithConfigFile:sampleRate:context:queue:delegate:osdAnalyzerAssetLocker:]
+ -[OSDAnalyzer osdAnalyzerAssetLocker]
+ -[OSDAnalyzer setOsdAnalyzerAssetLocker:]
+ _OBJC_IVAR_$_OSDAnalyzer._osdAnalyzerAssetLocker
+ _SpeechDetectorVersionNumber
+ _SpeechDetectorVersionString
+ _objc_msgSend$_setupCaesuraSPGWithConfigFile:sampleRate:osdAnalyzerAssetLocker:
+ _objc_msgSend$_setupOEPAssetManagerWithOSDAnalyzerAssetLocker:
+ _objc_msgSend$resetTimer
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- -[OSDAnalyzer initWithConfigFile:sampleRate:context:queue:delegate:]
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
CStrings:
+ "@\"<OSDAnalyzerAssetLocker>\""
+ "@64@0:8@16Q24@32@40@48@56"
+ "B40@0:8@16Q24@32"
+ "T@\"<OSDAnalyzerAssetLocker>\",&,N,V_osdAnalyzerAssetLocker"
+ "_osdAnalyzerAssetLocker"
+ "_setupCaesuraSPGWithConfigFile:sampleRate:osdAnalyzerAssetLocker:"
+ "_setupOEPAssetManagerWithOSDAnalyzerAssetLocker:"
+ "initWithConfigFile:sampleRate:context:queue:delegate:osdAnalyzerAssetLocker:"
+ "osdAnalyzerAssetLocker"
+ "resetTimer"
+ "setOsdAnalyzerAssetLocker:"
- "@56@0:8@16Q24@32@40@48"
- "A"
- "initWithConfigFile:sampleRate:context:queue:delegate:"

```
