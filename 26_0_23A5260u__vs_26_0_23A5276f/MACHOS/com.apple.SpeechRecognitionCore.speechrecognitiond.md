## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.54.0.0
-  __TEXT.__text: 0xd4c68
-  __TEXT.__auth_stubs: 0x27a0
+6.3.57.0.0
+  __TEXT.__text: 0xd4668
+  __TEXT.__auth_stubs: 0x27d0
   __TEXT.__objc_stubs: 0x3440
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1904
+  __TEXT.__objc_methlist: 0x18d4
   __TEXT.__const: 0x6476
-  __TEXT.__gcc_except_tab: 0x9438
+  __TEXT.__gcc_except_tab: 0x9480
   __TEXT.__objc_methname: 0x49c2
-  __TEXT.__cstring: 0x4182
-  __TEXT.__oslogstring: 0x5754
-  __TEXT.__objc_classname: 0x34b
+  __TEXT.__cstring: 0x41a2
+  __TEXT.__oslogstring: 0x55b4
+  __TEXT.__objc_classname: 0x348
   __TEXT.__objc_methtype: 0x1003
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0xd4c
-  __TEXT.__swift5_reflstr: 0x798
+  __TEXT.__swift5_typeref: 0xd34
+  __TEXT.__swift5_reflstr: 0x7b8
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_fieldmd: 0x784
-  __TEXT.__constg_swiftt: 0x11e0
+  __TEXT.__constg_swiftt: 0x11c0
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift_as_entry: 0xa0
   __TEXT.__swift_as_ret: 0xac
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0x4ba8
-  __TEXT.__eh_frame: 0x36b4
-  __DATA_CONST.__auth_got: 0x13f0
+  __TEXT.__unwind_info: 0x4b98
+  __TEXT.__eh_frame: 0x36fc
+  __DATA_CONST.__auth_got: 0x1408
   __DATA_CONST.__got: 0x790
   __DATA_CONST.__auth_ptr: 0x278
-  __DATA_CONST.__const: 0x7690
-  __DATA_CONST.__cfstring: 0x1ce0
+  __DATA_CONST.__const: 0x7670
+  __DATA_CONST.__cfstring: 0x1cc0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0x2d20
+  __DATA.__objc_const: 0x2cd0
   __DATA.__objc_selrefs: 0x12b0
-  __DATA.__objc_ivar: 0x144
-  __DATA.__objc_data: 0x14b0
+  __DATA.__objc_ivar: 0x140
+  __DATA.__objc_data: 0x1490
   __DATA.__data: 0xfb8
   __DATA.__bss: 0x1010
   __DATA.__common: 0xa6

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F6546971-F94E-3904-8BF4-A8CF2718A03B
-  Functions: 3790
-  Symbols:   1138
-  CStrings:  2473
+  UUID: 5495C7F1-3818-363E-918C-B88147F02EF6
+  Functions: 3783
+  Symbols:   1134
+  CStrings:  2462
 
Symbols:
+ _swift_getErrorValue
- __ZN11RDQSREngine36ResetRecognitionWithStartedASREngineEv
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "AVC: Error setting MX propery for supressing recording state. %@"
+ "PrefersSuppressingRecordingState"
+ "isExclaveCapability"
- "AF notification didChangeStateFrom %lld to %lld "
- "AVC: AF notification didChangeStateFrom %llu to %llu"
- "AVC: Could not start recording after Siri request"
- "AVC: Siri is listening: %{bool}d"
- "AVC: Siri is speaking: %{bool}d"
- "AVC:Start recording from AV since Siri is Idle"
- "AVC:Stop recording from AV since Siri is active"
- "AVC:Temporarily StopRecording from AV"
- "ResetRecognition"
- "Start recording Independent VAD since Siri is Idle"
- "Stop recording from Independent VAD since Siri is active"

```
