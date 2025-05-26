## audiomxd

> `/usr/libexec/audiomxd`

```diff

-1387.4.2.0.0
-  __TEXT.__text: 0x3a84
-  __TEXT.__auth_stubs: 0x870
+1387.5.49.0.0
+  __TEXT.__text: 0x3ed0
+  __TEXT.__auth_stubs: 0x8a0
   __TEXT.__objc_stubs: 0x160
   __TEXT.__const: 0x8a
-  __TEXT.__gcc_except_tab: 0x2c0
-  __TEXT.__cstring: 0x347
-  __TEXT.__oslogstring: 0x304
+  __TEXT.__gcc_except_tab: 0x2e8
+  __TEXT.__cstring: 0x3fc
+  __TEXT.__oslogstring: 0x57a
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x102
   __TEXT.__unwind_info: 0x180
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__auth_got: 0x460
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x400
-  __DATA_CONST.__cfstring: 0x20
+  __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x30
   __DATA.__objc_selrefs: 0x58
-  __DATA.__objc_classrefs: 0x30
   __DATA.__data: 0x40
   __DATA.__bss: 0x58
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient
   - /usr/lib/libAudioToolboxUtility.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 64
-  Symbols:   176
-  CStrings:  85
+  Symbols:   179
+  CStrings:  99
 
Symbols:
+ _MGGetBoolAnswer
+ __ZN21PlatformUtilities_iOS15IsInternalBuildEv
+ _tb_conclave_endpoint_for_service
CStrings:
+ "%25s:%-5d [audiomxd conclave] Launching audiomxd conclave"
+ "%25s:%-5d [audiomxd conclave][AudioCaptureServer] conclave launch returned error:%u\n"
+ "%25s:%-5d [audiomxd conclave][AudioCaptureServer] conclave launch suceeded"
+ "%25s:%-5d [audiomxd conclave][MTD] conclave launch returned error:%u\n"
+ "%25s:%-5d [audiomxd conclave][MTD] conclave launch suceeded"
+ "%25s:%-5d [audiomxd conclave][Siri] conclave launch returned error:%u\n"
+ "%25s:%-5d [audiomxd conclave][Siri] conclave launch suceeded"
+ "%25s:%-5d [audiomxd conclave][SoundAnalysis] conclave launch returned error:%u\n"
+ "%25s:%-5d [audiomxd conclave][SoundAnalysis] conclave launch suceeded"
+ "ExclaveCapability"
+ "com.apple.audiomxd.AudioCaptureServer"
+ "com.apple.audiomxd.MTDAudioDSPControl"
+ "com.apple.audiomxd.SiriAudioDSPControl"
+ "com.apple.audiomxd.SoundAnalysisAudioDSPControl"

```
