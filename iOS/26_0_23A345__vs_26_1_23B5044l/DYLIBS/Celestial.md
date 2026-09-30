## Celestial

> `/System/Library/PrivateFrameworks/Celestial.framework/Celestial`

```diff

-3255.79.1.8.0
-  __TEXT.__text: 0xc30
-  __TEXT.__auth_stubs: 0x270
+3285.5.1.11.1
+  __TEXT.__text: 0x1520
+  __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_methlist: 0xa0
-  __TEXT.__const: 0x4
-  __TEXT.__cstring: 0x509
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x570
+  __TEXT.__oslogstring: 0x2cc
   __TEXT.__unwind_info: 0x98
   __TEXT.__objc_classname: 0x25
   __TEXT.__objc_methname: 0x2b8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x140
-  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__auth_got: 0x160
+  __AUTH_CONST.__cfstring: 0x8e0
   __AUTH_CONST.__objc_const: 0x168
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x68
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A7F7FE3D-767F-3B25-A697-FDCC988B842C
+  UUID: 1E8A750E-BB79-35ED-8823-80085C873D6A
   Functions: 33
-  Symbols:   165
-  CStrings:  178
+  Symbols:   170
+  CStrings:  194
 
Symbols:
+ _FigNote_AllowInternalDefaultLogs
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _gFigCheckpointTrace
+ _os_log_type_enabled
- _objc_release_x21
- _objc_release_x26
Functions:
~ +[FigCheckpointSupport makeDictionary] : 8 -> 104
~ __computeCheckpoint : 1960 -> 4044
~ +[FigCheckpointSupport makeDictionaryForDevice:] : 8 -> 116
CStrings:
+ "<<<< FigCheckpointSupport >>>> %s: CHECKPOINT %@"
+ "<<<< FigCheckpointSupport >>>> %s: Finished creating audio codec list %@"
+ "<<<< FigCheckpointSupport >>>> %s: Finished creating complete list %@"
+ "<<<< FigCheckpointSupport >>>> %s: Finished creating video codec list %@"
+ "<<<< FigCheckpointSupport >>>> %s: Opening checkpointAdditionsSpecificationDictionary %@"
+ "<<<< FigCheckpointSupport >>>> %s: creating audio and video codec dictionary from input %@"
+ "<<<< FigCheckpointSupport >>>> %s: failed to create dictionary from %s"
+ "<<<< FigCheckpointSupport >>>> %s: specificationDictionary was NIL, audioSpecificationDictionary %@"
+ "<<<< FigCheckpointSupport >>>> %s: specificationDictionary was NIL, videoSpecificationDictionary %@"
+ "_addSpecificationAdditions"
+ "_computeCheckpoint"
+ "_twiddleCheckpoint"
+ "checkpoint_trace"
+ "com.apple.coremedia"

```
