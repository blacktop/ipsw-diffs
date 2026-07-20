## ColorSync

> `/System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-3924.1.0.0.0
-  __TEXT.__text: 0x80f94
-  __TEXT.__const: 0x1230e2
-  __TEXT.__cstring: 0x9672
+3926.0.0.0.0
+  __TEXT.__text: 0x814c4
+  __TEXT.__const: 0x123132
+  __TEXT.__cstring: 0x9675
   __TEXT.__oslogstring: 0xb
-  __TEXT.__gcc_except_tab: 0x1660
+  __TEXT.__gcc_except_tab: 0x166c
   __TEXT.__ustring: 0xd0
   __TEXT.__constg_swiftt: 0x204
   __TEXT.__swift5_types: 0x3c

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x1c90
+  __TEXT.__unwind_info: 0x1c98
   __TEXT.__eh_frame: 0x790
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x1f10
+  __DATA_CONST.__const: 0x1f58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__objc_selrefs: 0x30

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 2790
-  Symbols:   4672
-  CStrings:  1242
+  Functions: 2793
+  Symbols:   4676
+  CStrings:  1243
 
Symbols:
+ ColorSyncProfileCompareProfiles.relevant_tags
+ _ColorSyncProfileCompareProfiles
+ _ZL22cdr_constrain_headroomPK14__CFDictionaryfRfPKc
+ __ZL22cdr_constrain_headroomPK14__CFDictionaryfRfPKc
+ __ZNK26CMMConvHAGCurveToneMapping31HeadroomAdaptiveGainToneMappingEfff
+ _component_count
- _ZN25CMMConvFlexGTCLumaScaling26flexGTC_constrain_headroomEfjf
- __ZN25CMMConvFlexGTCLumaScaling26flexGTC_constrain_headroomEfjf
CStrings:
+ "AGC"
+ "Solarium: CDR %s Debug: edr_strength=%f, cdr_strength=%f, content_average_light_level=%f, target_headroom=%f, source_headroom=%f, desired_scale=%f, desired_target_headroom=%f, final_hr=%f, final_scaling=%f, combined headroom=%f"
- "Solarium: CDR AGC Debug: edr_strength=%f, cdr_strength=%f, content_average_light_level=%f, target_headroom=%f, source_headroom=%f, desired_scale=%f, desired_target_headroom=%f, final_hr=%f, final_scaling=%f, combined headroom=%f"
```
