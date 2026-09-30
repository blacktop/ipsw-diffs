## videodecodeservice

> `/System/Library/Frameworks/VideoToolbox.framework/XPCServices/videodecodeservice.xpc/videodecodeservice`

```diff

-3185.16.2.0.0
-  __TEXT.__text: 0x2d4
-  __TEXT.__auth_stubs: 0xa0
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0xf1
-  __TEXT.__oslogstring: 0x84
+3185.17.1.0.0
+  __TEXT.__text: 0x64
+  __TEXT.__auth_stubs: 0x40
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x50
-  __DATA_CONST.__got: 0x10
-  __DATA_CONST.__cfstring: 0x40
-  __DATA.__common: 0x10
+  __DATA_CONST.__auth_got: 0x20
+  __DATA_CONST.__got: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /usr/lib/libSystem.B.dylib
   Functions: 1
-  Symbols:   16
-  CStrings:  10
+  Symbols:   8
+  CStrings:  0
 
Symbols:
+ _FigSignalErrorAt
- _FigSignalErrorAt3
- ___CFConstantStringClassReference
- ___stack_chk_fail
- ___stack_chk_guard
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _fig_note_initialize_category_with_default_work_cf
- _os_log_type_enabled
CStrings:
- "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
- "<<<< VDECS_Main >>>>"
- "<<<< VDECS_Main >>>> %!s(MISSING): VTVideoCodecService_ShouldUseSeparateCodecProcess: %!d(MISSING)"
- "<<<< VDECS_Main >>>> %!s(MISSING): videodecodeservice startup\n"
- "Should not launch videodecodeservice without feature flag!"
- "com.apple.coremedia"
- "kFigBaseObjectError_UnsupportedOperation"
- "main"
- "videodecodeservice_main.c"
- "videodecodeservice_trace"

```
