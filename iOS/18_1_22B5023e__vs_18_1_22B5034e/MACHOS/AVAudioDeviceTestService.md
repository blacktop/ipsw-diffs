## AVAudioDeviceTestService

> `/System/Library/Frameworks/AVFAudio.framework/XPCServices/AVAudioDeviceTestService.xpc/AVAudioDeviceTestService`

```diff

-684.115.0.0.0
-  __TEXT.__text: 0x11bf4
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_stubs: 0x1b80
+684.201.0.0.0
+  __TEXT.__text: 0x1255c
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_stubs: 0x1bc0
   __TEXT.__objc_methlist: 0x7d4
   __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x2a6c
-  __TEXT.__cstring: 0x5ac
-  __TEXT.__oslogstring: 0x1b06
-  __TEXT.__objc_methname: 0x1fe8
+  __TEXT.__gcc_except_tab: 0x2b98
+  __TEXT.__cstring: 0x5b1
+  __TEXT.__oslogstring: 0x1c7d
+  __TEXT.__objc_methname: 0x2026
   __TEXT.__objc_classname: 0x10f
   __TEXT.__objc_methtype: 0x4e3
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x418
-  __DATA_CONST.__auth_got: 0x320
-  __DATA_CONST.__got: 0x170
+  __TEXT.__unwind_info: 0x420
+  __DATA_CONST.__auth_got: 0x348
+  __DATA_CONST.__got: 0x178
   __DATA_CONST.__const: 0x430
   __DATA_CONST.__cfstring: 0x6c0
   __DATA_CONST.__objc_classlist: 0x30

   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x1388
-  __DATA.__objc_selrefs: 0x898
+  __DATA.__objc_selrefs: 0x8a8
   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x58
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 204
-  Symbols:   209
-  CStrings:  692
+  Functions: 206
+  Symbols:   213
+  CStrings:  705
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _AVAudioSessionInterruptionTypeKey
+ _os_signpost_id_generate
+ _os_signpost_enabled
CStrings:
+ "%!s(MISSING):%!d(MISSING) No AVAudioSessionInterruptionTypeKey"
+ "freq=%!f(MISSING), lvl=%!f(MISSING)"
+ "duration timer"
+ "user tap"
+ "%!s(MISSING):%!d(MISSING) Unable to create pulse tone handler for sequence %!{(MISSING)public}@"
+ "-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke"
+ "%!s(MISSING):%!d(MISSING) Creating engine and tone handler"
+ "AVF tone playback"
+ "integerValue"
+ "%!s(MISSING):%!d(MISSING) Interruption began (%!{(MISSING)public}@) - %!{(MISSING)public}@"
+ "%!s(MISSING):%!d(MISSING) Failed to disable smart routing. { error=%!{(MISSING)public}@ }"
+ "adtssp"
+ "%!s(MISSING):%!d(MISSING) Unhandled interruption type"
+ "setEligibleForBTSmartRoutingConsideration:error:"
+ "%!s(MISSING):%!d(MISSING) Interruption ended (%!{(MISSING)public}@) - %!{(MISSING)public}@"
- "-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke_3"
- "%!s(MISSING):%!d(MISSING) interruption (%!@(MISSING)) with test error (%!l(MISSING)i) - %!@(MISSING)"

```
