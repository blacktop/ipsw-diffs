## AVFAudio

> `/System/Library/Frameworks/AVFAudio.framework/AVFAudio`

```diff

-684.115.0.0.0
-  __TEXT.__text: 0x112c28
-  __TEXT.__auth_stubs: 0x1f50
+684.201.0.0.0
+  __TEXT.__text: 0x113aa8
+  __TEXT.__auth_stubs: 0x1fd0
   __TEXT.__objc_methlist: 0x5180
   __TEXT.__const: 0x626
-  __TEXT.__gcc_except_tab: 0x14cec
-  __TEXT.__cstring: 0xe418
-  __TEXT.__oslogstring: 0x1739a
+  __TEXT.__gcc_except_tab: 0x14ecc
+  __TEXT.__cstring: 0xe393
+  __TEXT.__oslogstring: 0x17548
   __TEXT.__dlopen_cstrs: 0xa9
-  __TEXT.__unwind_info: 0x5ca8
+  __TEXT.__unwind_info: 0x5cf0
   __TEXT.__objc_classname: 0xa12
   __TEXT.__objc_methname: 0xbb1b
   __TEXT.__objc_methtype: 0x2761

   __DATA_CONST.__objc_selrefs: 0x3158
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2b0
-  __AUTH_CONST.__auth_got: 0xfc0
-  __AUTH_CONST.__const: 0x6778
+  __AUTH_CONST.__auth_got: 0x1000
+  __AUTH_CONST.__const: 0x6738
   __AUTH_CONST.__cfstring: 0x3420
   __AUTH_CONST.__objc_const: 0x8f58
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x414
   __DATA.__data: 0x7e0
-  __DATA.__bss: 0x160
+  __DATA.__bss: 0x180
   __DATA_DIRTY.__objc_data: 0x1db0
   __DATA_DIRTY.__data: 0xd0
   __DATA_DIRTY.__bss: 0x268

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3838
-  Symbols:   4856
-  CStrings:  5796
+  Functions: 3845
+  Symbols:   4873
+  CStrings:  5805
 
Symbols:
+ __ZNK5caulk10concurrent7details23lf_read_sync_write_impl10end_accessEv
+ __ZN5caulk10concurrent7details23lf_read_sync_write_implC1Ev
+ __ZN5caulk10concurrent7details23lf_read_sync_write_impl12begin_mutateEv
+ __ZNK5caulk10concurrent7details23lf_read_sync_write_impl12begin_accessEv
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ __os_signpost_emit_with_name_impl
+ __ZN5caulk10concurrent7details23lf_read_sync_write_impl10end_mutateEj
CStrings:
+ "duration timer"
+ "%!s(MISSING):%!d(MISSING) Interruption ended (%!{(MISSING)public}@) - %!{(MISSING)public}@"
+ "user tap"
+ "AVF tone playback"
+ "freq=%!f(MISSING), lvl=%!f(MISSING)"
+ "%!s(MISSING):%!d(MISSING) Unable to create pulse tone handler for sequence %!{(MISSING)public}@"
+ "%!s(MISSING):%!d(MISSING) Engine@%!p(MISSING): total number of attached nodes %!d(MISSING)"
+ "adtssp"
+ "%!s(MISSING):%!d(MISSING) Unhandled interruption type"
+ "%!s(MISSING):%!d(MISSING) Interruption began (%!{(MISSING)public}@) - %!{(MISSING)public}@"
+ "%!s(MISSING):%!d(MISSING) Failed to disable smart routing. { error=%!{(MISSING)public}@ }"
+ "%!s(MISSING):%!d(MISSING) No AVAudioSessionInterruptionTypeKey"
+ "-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke"
+ "%!s(MISSING):%!d(MISSING) Creating engine and tone handler"
- "%!s(MISSING):%!d(MISSING) interruption (%!@(MISSING)) with test error (%!l(MISSING)i) - %!@(MISSING)"
- "bus < _inMutexes.size()"
- "/Library/Caches/com.apple.xbs/Sources/AVFAudio/Source/AVFAudio/AVAudioEngine/AVAEGraph/AVAEGraphNode.h"
- "InputMutex"
- "-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke_3"

```
