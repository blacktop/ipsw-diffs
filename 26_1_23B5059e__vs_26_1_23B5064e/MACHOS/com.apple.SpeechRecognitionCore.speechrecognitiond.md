## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.68.1.0
-  __TEXT.__text: 0xc6b2c
-  __TEXT.__auth_stubs: 0x2620
-  __TEXT.__objc_stubs: 0x3440
+6.3.68.2.0
+  __TEXT.__text: 0xc7a3c
+  __TEXT.__auth_stubs: 0x2680
+  __TEXT.__objc_stubs: 0x34a0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x18d4
-  __TEXT.__const: 0x5d66
-  __TEXT.__gcc_except_tab: 0xa318
-  __TEXT.__objc_methname: 0x49e2
-  __TEXT.__cstring: 0x4076
-  __TEXT.__oslogstring: 0x5664
+  __TEXT.__const: 0x5da6
+  __TEXT.__gcc_except_tab: 0xa344
+  __TEXT.__objc_methname: 0x4a7c
+  __TEXT.__cstring: 0x40b6
+  __TEXT.__oslogstring: 0x56d4
   __TEXT.__objc_classname: 0x348
   __TEXT.__objc_methtype: 0x1012
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xacc
-  __TEXT.__swift5_typeref: 0x71a
-  __TEXT.__swift5_reflstr: 0x488
-  __TEXT.__swift5_fieldmd: 0x48c
+  __TEXT.__constg_swiftt: 0xb94
+  __TEXT.__swift5_typeref: 0x736
+  __TEXT.__swift5_reflstr: 0x4c8
+  __TEXT.__swift5_fieldmd: 0x4cc
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_capture: 0x49c
-  __TEXT.__swift5_types: 0x54
+  __TEXT.__swift5_types: 0x58
   __TEXT.__swift_as_entry: 0x5c
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0x4788
-  __TEXT.__eh_frame: 0x2bb4
-  __DATA_CONST.__auth_got: 0x1330
-  __DATA_CONST.__got: 0x760
-  __DATA_CONST.__auth_ptr: 0x1b8
-  __DATA_CONST.__const: 0x6df8
+  __TEXT.__unwind_info: 0x47b8
+  __TEXT.__eh_frame: 0x2b4c
+  __DATA_CONST.__auth_got: 0x1360
+  __DATA_CONST.__got: 0x770
+  __DATA_CONST.__auth_ptr: 0x1c8
+  __DATA_CONST.__const: 0x6ed8
   __DATA_CONST.__cfstring: 0x1ce0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0x2c38
-  __DATA.__objc_selrefs: 0x12b8
+  __DATA.__objc_const: 0x2cc0
+  __DATA.__objc_selrefs: 0x12f0
   __DATA.__objc_ivar: 0x140
-  __DATA.__objc_data: 0x1488
-  __DATA.__data: 0xf60
-  __DATA.__bss: 0x3e8
+  __DATA.__objc_data: 0x14b0
+  __DATA.__data: 0xf68
+  __DATA.__bss: 0x470
   __DATA.__common: 0xa6
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B2622287-5714-3495-A049-611E611F965D
-  Functions: 3556
-  Symbols:   1117
-  CStrings:  2485
+  UUID: 3926A93D-8A00-3854-ADD2-D18B04F29F8A
+  Functions: 3573
+  Symbols:   1122
+  CStrings:  2497
 
Symbols:
+ _OBJC_CLASS_$_SRDMachTime
+ _OBJC_CLASS_$_VCCommon
+ __swift_isClassOrObjCExistentialType
+ _swift_allocateGenericClassMetadata
+ _swift_getGenericMetadata
+ _swift_initClassMetadata2
- _CMTimeGetSeconds
CStrings:
+ "SpeechAnalyzer final results, sampleSent = %lld, startSampleNumber = %lld, endSampleNumber = %lld lateny milliseconds = %f"
+ "SpeechAnalyzer partial results, sampleSent = %lld, endSampleNumber = %lld, lateny milliseconds = %f"
+ "_circularArray"
+ "capacity"
+ "elements"
+ "initWithMachTime:"
+ "machAbsoluteTimeToMilliseconds:"
+ "mach_time"
+ "setTimeAsrResultReceived:"
+ "setTimeSRDResponseSent:"
+ "setTimeUtteranceEnd:"
+ "setTimeUtteranceStart:"
+ "writeLinearIndex"
- "SpeechDonation ::totalSamplesSent =%lld ::newUtteranceBeginSampleNumber :: start = %lld :: newUtteranceEndSampleNumber = %lld"

```
