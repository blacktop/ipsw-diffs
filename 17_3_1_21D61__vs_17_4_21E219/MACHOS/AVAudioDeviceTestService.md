## AVAudioDeviceTestService

> `/System/Library/Frameworks/AVFAudio.framework/XPCServices/AVAudioDeviceTestService.xpc/AVAudioDeviceTestService`

```diff

-629.3.5.0.0
-  __TEXT.__text: 0xdfc0
-  __TEXT.__auth_stubs: 0x620
+629.5.30.0.0
+  __TEXT.__text: 0xe324
+  __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_stubs: 0x1ac0
   __TEXT.__objc_methlist: 0x784
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x1ad0
-  __TEXT.__cstring: 0x567
+  __TEXT.__gcc_except_tab: 0x1aec
+  __TEXT.__cstring: 0x59a
   __TEXT.__oslogstring: 0xfcb
-  __TEXT.__objc_methname: 0x1f00
+  __TEXT.__objc_methname: 0x1f14
   __TEXT.__objc_classname: 0x10f
   __TEXT.__objc_methtype: 0x4ae
-  __TEXT.__unwind_info: 0x3b4
+  __TEXT.__dlopen_cstrs: 0x5a
+  __TEXT.__unwind_info: 0x3c0
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x458
+  __DATA_CONST.__const: 0x4b8
   __DATA_CONST.__cfstring: 0x6a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x12f8
   __DATA.__objc_selrefs: 0x848
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xe0
-  __DATA.__objc_superrefs: 0x28
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 03D37112-F5D2-3DA5-A9A6-66F9CDFFE92C
-  Functions: 195
-  Symbols:   168
-  CStrings:  677
+  UUID: 016D9EB1-CADB-323E-8DA1-0965516214D6
+  Functions: 199
+  Symbols:   170
+  CStrings:  682
 
Symbols:
+ __sl_dlopen
+ _abort_report_np
+ _dlerror
+ _dlsym
- _MSNMonitorBeginException
- _MSNMonitorEndException
CStrings:
+ "%s"
+ "MSNMonitorBeginException"
+ "MSNMonitorEndException"
+ "T@\"NSString\",?,R,C"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet"

```
