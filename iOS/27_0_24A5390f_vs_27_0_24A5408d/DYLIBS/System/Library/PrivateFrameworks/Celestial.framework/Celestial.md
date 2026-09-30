## Celestial

> `/System/Library/PrivateFrameworks/Celestial.framework/Celestial`

```diff

-3350.71.2.11.1
-  __TEXT.__text: 0x16c0
+3350.75.2.0.0
+  __TEXT.__text: 0xdac
   __TEXT.__objc_methlist: 0xa0
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x57d
-  __TEXT.__oslogstring: 0x2cc
+  __TEXT.__const: 0x4
+  __TEXT.__cstring: 0x516
   __TEXT.__unwind_info: 0x98
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
   __DATA.__data: 0x68
-  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 33
-  Symbols:   156
-  CStrings:  83
+  Symbols:   152
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
~ +[FigCheckpointSupport makeDictionary] : 104 -> 8
~ __computeCheckpoint : 4080 -> 1960
~ +[FigCheckpointSupport makeDictionaryForDevice:] : 116 -> 8
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
