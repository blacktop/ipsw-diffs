## SiriTTS

> `/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS`

```diff

-3402.50.1.0.0
-  __TEXT.__text: 0x7e26b4
-  __TEXT.__auth_stubs: 0x25f0
+3402.56.1.0.0
+  __TEXT.__text: 0x7e342c
+  __TEXT.__auth_stubs: 0x2600
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__gcc_except_tab: 0x3a394
-  __TEXT.__cstring: 0x651f0
+  __TEXT.__gcc_except_tab: 0x3a484
+  __TEXT.__cstring: 0x65268
   __TEXT.__const: 0xd6a4e
-  __TEXT.__oslogstring: 0x81e3
+  __TEXT.__oslogstring: 0x823b
   __TEXT.__ustring: 0x4a0
-  __TEXT.__unwind_info: 0x17628
+  __TEXT.__unwind_info: 0x17650
   __TEXT.__eh_frame: 0x260
   __TEXT.__objc_classname: 0x1c
   __TEXT.__objc_methname: 0x119

   __DATA_CONST.__objc_selrefs: 0x88
   __DATA_CONST.__objc_classrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1308
+  __AUTH_CONST.__auth_got: 0x1310
   __AUTH_CONST.__auth_ptr: 0x120
   __AUTH_CONST.__const: 0x32d48
   __AUTH_CONST.__cfstring: 0x180

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 21989
-  Symbols:   23455
-  CStrings:  17564
+  Functions: 21994
+  Symbols:   23461
+  CStrings:  17570
 
Symbols:
+ __ZN14TTSSynthesizer16get_neural_styleEv
+ __ZN14TTSSynthesizer16set_neural_styleERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN14TTSSynthesizer18set_synthesis_modeENS_13SynthesisModeE
+ __os_log_debug_impl
+ __os_log_fault_impl
+ _dispatch_activate
+ _dispatch_workloop_create_inactive
+ _dispatch_workloop_set_scheduler_priority
- _pthread_attr_getschedparam
- _pthread_attr_setinheritsched
- _pthread_attr_setschedparam
- _pthread_attr_setschedpolicy
CStrings:
+ "/AppleInternal/Library/BuildRoots/11914d60-911b-11ef-aa10-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/boost/utility/string_ref.hpp"
+ "BNNS execution failed with return code %!d(MISSING)"
+ "Detected issue in MLInference output, remaining try count: %!d(MISSING)"
+ "Exception in AsyncContainerModule worker."
+ "Model input %!s(MISSING) is not set correctly!"
+ "Neural Style changed to: '%!s(MISSING)'"
+ "Set input: %!s(MISSING)"
+ "Set synthesis mode as: %!d(MISSING)"
+ "execute"
+ "has_input(input_name)"
- "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/boost/utility/string_ref.hpp"
- "BNNS execution finished with return code %!d(MISSING)"
- "Invalid SoundStorm output"
- "com.apple.siritts.NashvilleFE"
- "com.apple.siritts.pthreadQueue"
- "tts.metrics.audio_has_click"

```
