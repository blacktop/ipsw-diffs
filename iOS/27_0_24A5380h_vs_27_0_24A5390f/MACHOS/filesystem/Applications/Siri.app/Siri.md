## Siri

> `/Applications/Siri.app/Siri`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_stublist`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-3600.55.26.0.0
-  __TEXT.__text: 0xefca8
-  __TEXT.__auth_stubs: 0x3020
-  __TEXT.__objc_stubs: 0x1b460
-  __TEXT.__objc_methlist: 0xe308
-  __TEXT.__const: 0x30b4
-  __TEXT.__cstring: 0x24370
+3600.55.30.0.0
+  __TEXT.__text: 0xf0b5c
+  __TEXT.__auth_stubs: 0x3010
+  __TEXT.__objc_stubs: 0x1b4a0
+  __TEXT.__objc_methlist: 0xe330
+  __TEXT.__const: 0x30e4
+  __TEXT.__cstring: 0x243dd
   __TEXT.__oslogstring: 0xd774
   __TEXT.__objc_classname: 0x1f93
-  __TEXT.__objc_methtype: 0xaf31
+  __TEXT.__objc_methtype: 0xaf71
   __TEXT.__gcc_except_tab: 0x13bc
-  __TEXT.__objc_methname: 0x2b5cf
+  __TEXT.__objc_methname: 0x2b6bf
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x2616
-  __TEXT.__constg_swiftt: 0x24e8
-  __TEXT.__swift5_reflstr: 0x19c7
-  __TEXT.__swift5_fieldmd: 0x12bc
+  __TEXT.__swift5_typeref: 0x2622
+  __TEXT.__constg_swiftt: 0x2504
+  __TEXT.__swift5_reflstr: 0x19f1
+  __TEXT.__swift5_fieldmd: 0x12fc
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0x1e8
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_proto: 0x144
-  __TEXT.__swift5_types: 0x118
-  __TEXT.__swift5_capture: 0x6ec
+  __TEXT.__swift5_types: 0x11c
+  __TEXT.__swift5_capture: 0x6b8
   __TEXT.__swift_as_entry: 0x44
   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift_as_cont: 0x38
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3910
-  __TEXT.__eh_frame: 0xc08
-  __DATA_CONST.__const: 0x4cf8
+  __TEXT.__unwind_info: 0x3930
+  __TEXT.__eh_frame: 0xc88
+  __DATA_CONST.__const: 0x4d88
   __DATA_CONST.__cfstring: 0x3380
   __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x120

   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x150
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__auth_got: 0x1820
+  __DATA_CONST.__auth_got: 0x1818
   __DATA_CONST.__got: 0x1858
   __DATA_CONST.__auth_ptr: 0x900
-  __DATA.__objc_const: 0x10bb8
-  __DATA.__objc_selrefs: 0x8fa8
+  __DATA.__objc_const: 0x10be8
+  __DATA.__objc_selrefs: 0x8fc8
   __DATA.__objc_ivar: 0x8c4
-  __DATA.__objc_data: 0x4b10
-  __DATA.__data: 0x4768
+  __DATA.__objc_data: 0x4b18
+  __DATA.__data: 0x4780
   __DATA.__objc_stublist: 0x10
   __DATA.__bss: 0x2100
   __DATA.__common: 0x370

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5192
-  Symbols:   1861
-  CStrings:  9005
+  Functions: 5191
+  Symbols:   1860
+  CStrings:  9014
 
Symbols:
+ _$s7SwiftUI9UnitPointVN
- _$sBi32_WV
- _swift_retain_x25
CStrings:
+ "@\"<SFCardResourceLoader>\"16@0:8"
+ "Attending window elapsed, but dismissal was paused. Waiting for request end signal"
+ "CalendarUIPlugin"
+ "NotebookUIPlugin"
+ "] SiriDirectedSpeech: resuming and canceling any deferred dismissal."
+ "] Speech detected; pausing auto-dismissal until the turn resolves."
+ "] Turn resolved not-for-Siri; flushing the dismissal deferred while speaking."
+ "] Turn resolved not-for-Siri; re-arming attending window from now."
+ "] Turn resolved not-for-Siri; un-pausing. No window pending."
+ "_showWaveform"
+ "attendingDismissalGate"
+ "cardLoader"
+ "isLinwoodEnabled"
+ "siriSessionSetReplayCaptureRequested:toPath:"
+ "startReplayCaptureToPath:"
+ "stopReplayCapture"
+ "v28@0:8B16@\"NSURL\"20"
+ "v28@0:8B16@20"
- "Cancel any scheduled attending window closure and pending autodismiss due to SiriDirectedSpeech"
- "Cease attending due to speech mitigation"
- "Extending attending window by "
- "Speech detected but attending window already extended once; ignoring"
- "Speech detected with no active attending window; ignoring"
- "_waveFormOpacity"
- "extendAttendingWindowForSpeechDetectedIfEligible()"
- "s due to speech detected (one-time)"
- "speechDetectedExtensionUsed"
```
