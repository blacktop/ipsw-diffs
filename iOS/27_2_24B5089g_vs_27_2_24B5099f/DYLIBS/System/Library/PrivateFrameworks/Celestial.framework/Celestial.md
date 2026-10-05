## Celestial

> `/System/Library/PrivateFrameworks/Celestial.framework/Celestial`

```diff

-3385.8.1.11.1
-  __TEXT.__text: 0x169c
+3385.12.1.0.0
+  __TEXT.__text: 0xda0
   __TEXT.__objc_methlist: 0xa0
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x57d
-  __TEXT.__oslogstring: 0x2cc
+  __TEXT.__const: 0x4
+  __TEXT.__cstring: 0x516
   __TEXT.__unwind_info: 0xe8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x48
-  __AUTH_CONST.__cfstring: 0x8e0
+  __AUTH_CONST.__cfstring: 0x8a0
   __AUTH_CONST.__objc_const: 0x168
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x8
-  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 33
-  Symbols:   139
-  CStrings:  83
+  Symbols:   135
+  CStrings:  69
 
Symbols:
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x28
- _FigNote_AllowInternalDefaultLogs
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _fig_note_initialize_category_with_default_work_cf
- _gFigCheckpointTrace
- _os_log_type_enabled
Functions:
~ +[FigCheckpointSupport makeDictionary] : 92 -> 8
~ __computeCheckpoint : 4080 -> 1960
~ +[FigCheckpointSupport makeDictionaryForDevice:] : 104 -> 8
CStrings:
- "<<<< FigCheckpointSupport >>>> %s: CHECKPOINT %@"
- "<<<< FigCheckpointSupport >>>> %s: Finished creating audio codec list %@"
- "<<<< FigCheckpointSupport >>>> %s: Finished creating complete list %@"
- "<<<< FigCheckpointSupport >>>> %s: Finished creating video codec list %@"
- "<<<< FigCheckpointSupport >>>> %s: Opening checkpointAdditionsSpecificationDictionary %@"
- "<<<< FigCheckpointSupport >>>> %s: creating audio and video codec dictionary from input %@"
- "<<<< FigCheckpointSupport >>>> %s: failed to create dictionary from %s"
- "<<<< FigCheckpointSupport >>>> %s: specificationDictionary was NIL, audioSpecificationDictionary %@"
- "<<<< FigCheckpointSupport >>>> %s: specificationDictionary was NIL, videoSpecificationDictionary %@"
- "_addSpecificationAdditions"
- "_computeCheckpoint"
- "_twiddleCheckpoint"
- "checkpoint_trace"
- "com.apple.coremedia"
```
