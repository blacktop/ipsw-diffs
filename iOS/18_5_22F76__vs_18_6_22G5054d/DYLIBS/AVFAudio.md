## AVFAudio

> `/System/Library/Frameworks/AVFAudio.framework/AVFAudio`

```diff

-684.603.0.0.0
-  __TEXT.__text: 0x114d34
+684.701.0.0.0
+  __TEXT.__text: 0x114e6c
   __TEXT.__auth_stubs: 0x1fd0
   __TEXT.__objc_methlist: 0x576c
   __TEXT.__dlopen_cstrs: 0xa9
   __TEXT.__const: 0x656
-  __TEXT.__gcc_except_tab: 0x14dc4
+  __TEXT.__gcc_except_tab: 0x14dd8
   __TEXT.__cstring: 0xe5b9
-  __TEXT.__oslogstring: 0x177de
+  __TEXT.__oslogstring: 0x1785d
   __TEXT.__unwind_info: 0x5ca0
   __TEXT.__objc_classname: 0xa13
   __TEXT.__objc_methname: 0xbc35

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2b0
   __AUTH_CONST.__auth_got: 0x1000
-  __AUTH_CONST.__const: 0x67b8
+  __AUTH_CONST.__const: 0x6788
   __AUTH_CONST.__cfstring: 0x3580
   __AUTH_CONST.__objc_const: 0x85c8
   __AUTH_CONST.__objc_intobj: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55A706AB-4390-32D2-8D85-65A954B832C1
+  UUID: 21F738D0-0BB4-3201-90BA-222A69B8401D
   Functions: 3820
-  Symbols:   12654
-  CStrings:  6270
+  Symbols:   12653
+  CStrings:  6271
 
Symbols:
+ ___Block_byref_object_copy_.5595
+ ___Block_byref_object_copy_.6385
+ ___Block_byref_object_copy_.7261
+ ___Block_byref_object_copy_.8262
+ ___Block_byref_object_copy_.8748
+ ___Block_byref_object_dispose_.5596
+ ___Block_byref_object_dispose_.6386
+ ___Block_byref_object_dispose_.7262
+ ___Block_byref_object_dispose_.8263
+ ___Block_byref_object_dispose_.8749
+ ___block_descriptor_tmp.6081
+ ___block_literal_global.193.8352
+ ___block_literal_global.5040
+ ___block_literal_global.5635
+ ___block_literal_global.6000
+ ___block_literal_global.6063
+ ___block_literal_global.6079
+ ___block_literal_global.6521
+ ___block_literal_global.7263
+ ___block_literal_global.8003
+ ___block_literal_global.8416
+ ___block_literal_global.8611
- ___Block_byref_object_copy_.5596
- ___Block_byref_object_copy_.6386
- ___Block_byref_object_copy_.7262
- ___Block_byref_object_copy_.8263
- ___Block_byref_object_copy_.8749
- ___Block_byref_object_dispose_.5597
- ___Block_byref_object_dispose_.6387
- ___Block_byref_object_dispose_.7263
- ___Block_byref_object_dispose_.8264
- ___Block_byref_object_dispose_.8750
- ___block_descriptor_60_ea8_40c44_ZTSNSt3__18weak_ptrI19AVVCRecordingEngineEE_e5_v8?0l
- ___block_descriptor_tmp.6082
- ___block_literal_global.193.8353
- ___block_literal_global.5041
- ___block_literal_global.5636
- ___block_literal_global.6001
- ___block_literal_global.6064
- ___block_literal_global.6080
- ___block_literal_global.6522
- ___block_literal_global.7264
- ___block_literal_global.8004
- ___block_literal_global.8417
- ___block_literal_global.8612
Functions:
~ __ZN19AVVCRecordingEngineC2E27AVVoiceControllerClientType : 868 -> 872
~ __ZN22AVVCHACRecordingEngine4Impl47AVVCHACRecordingEngineAudioAvailabilityCallbackE18CoreAudioTimestampPv : 1556 -> 1732
~ ____ZN22AVVCHACRecordingEngine11handleInputE18CoreAudioTimestamp_block_invoke : 424 -> 560
~ __ZN22AVVCHACRecordingEngineC1E27AVVoiceControllerClientType : 708 -> 704
CStrings:
+ "%25s:%-5d AVVCHACRecordingEngine::handleInput resetting ignoreInputCallback"
+ "%25s:%-5d HAC (%p) - First callback mIgnoreInputCallback (%d) -  Now: ( ht: %lld ), BuffStartTime: ( ht: %lld st: %lld ), SiriRequestedStartTime: ( ht: %lld ). Now-SiriRequestedStartTime: %0.6f ms, BuffStartTime-SiriRequestedStartTime: %0.6f ms."
+ "%25s:%-5d record internally stopped, so throwing away buffer. ignoreInputCallback(%d), StreamState(%s). RecordCancelled(%d)"
- "%25s:%-5d HAC (%p) - First callback -  Now: ( ht: %lld ), BuffStartTime: ( ht: %lld st: %lld ), SiriRequestedStartTime: ( ht: %lld ). Now-SiriRequestedStartTime: %0.6f ms, BuffStartTime-SiriRequestedStartTime: %0.6f ms."
- "%25s:%-5d record internally stopped, so throwing away buffer. StreamState(%s). RecordCancelled(%d)"

```
