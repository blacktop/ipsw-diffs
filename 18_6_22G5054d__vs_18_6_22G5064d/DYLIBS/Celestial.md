## Celestial

> `/System/Library/PrivateFrameworks/Celestial.framework/Celestial`

```diff

-3235.8.2.0.0
-  __TEXT.__text: 0xc0c
-  __TEXT.__auth_stubs: 0x320
+3235.10.1.0.0
+  __TEXT.__text: 0x144c
+  __TEXT.__auth_stubs: 0x390
   __TEXT.__objc_methlist: 0x98
-  __TEXT.__const: 0x4
-  __TEXT.__cstring: 0x1484
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x14eb
+  __TEXT.__oslogstring: 0x2cc
   __TEXT.__unwind_info: 0x98
   __TEXT.__objc_classname: 0x25
   __TEXT.__objc_methname: 0x29f

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x198
-  __AUTH_CONST.__cfstring: 0x19c0
+  __AUTH_CONST.__auth_got: 0x1d0
+  __AUTH_CONST.__cfstring: 0x1a00
   __AUTH_CONST.__objc_const: 0x168
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x460
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 01834FD7-5739-3699-AF3E-4B5BBA7D53E3
+  UUID: 6251DD72-D285-3041-8140-6DD12C5E2AD9
   Functions: 45
-  Symbols:   547
-  CStrings:  451
+  Symbols:   555
+  CStrings:  467
 
Symbols:
+ _FigNote_AllowInternalDefaultLogs
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _gFigCheckpointTrace
+ _objc_release_x20
+ _objc_release_x22
+ _objc_release_x26
+ _os_log_type_enabled
- _objc_release_x25
- _objc_release_x27
Functions:
~ +[FigCheckpointSupport makeDictionary] : 1872 -> 3992
~ _FigAspenGetJPEGEncodeTiming : 16 -> 8
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
