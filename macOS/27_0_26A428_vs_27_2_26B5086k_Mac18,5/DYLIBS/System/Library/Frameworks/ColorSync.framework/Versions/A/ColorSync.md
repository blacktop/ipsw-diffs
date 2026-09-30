## ColorSync

> `/System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync`

```diff

-3929.0.0.0.0
-  __TEXT.__text: 0x801e4
-  __TEXT.__const: 0x123132
-  __TEXT.__cstring: 0x96aa
+3929.1.3.0.0
+  __TEXT.__text: 0x815bc
+  __TEXT.__const: 0x123142
+  __TEXT.__cstring: 0x95ff
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0x166c
   __TEXT.__ustring: 0xd0

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x2438
+  __TEXT.__unwind_info: 0x2470
   __TEXT.__eh_frame: 0x7b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x30
   __DATA_CONST.__got: 0x148
   __AUTH_CONST.__const: 0x9940
-  __AUTH_CONST.__cfstring: 0x5f20
+  __AUTH_CONST.__cfstring: 0x5e60
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__auth_got: 0x990
   __AUTH.__data: 0xf0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 2794
-  Symbols:   4677
-  CStrings:  1244
+  Functions: 2809
+  Symbols:   4695
+  CStrings:  1238
 
Symbols:
+ ColorSyncProfileGetContentHeadroom
+ ColorSyncProfileGetFlexGTCHeadroom
+ _ColorSyncProfileCreateHDRProfileDescription
+ _ColorSyncProfileGetContentHeadroom
+ _ColorSyncProfileGetFlexGTCHeadroom
+ _ColorSyncProfileGetISO5AverageLightLevel
+ _ColorSyncProfileGetISO5Headroom
+ _ColorSyncProfileGetMetaAndHAGCMD5
+ _ColorSyncProfileReconcileMetaTagWithHAGC
+ _applyHAGCurveDescriptionAndHeader
+ _bt2020_normalized_float_from_dictionary
+ _create_copy_with_hagc_reference_white_patched
+ _create_iso5_dicts_from_headroom_reference_white_pair
+ _create_iso5_meta_tag_data
+ _get_D50_XYZ_for_cicp_primaries
+ _headroom_reference_white_pair_from_hagc
+ _headroom_reference_white_pair_from_iso5_metadata
+ _kColorSyncDerivedISO5Metadata
+ _reference_white_from_iso5_metadata
+ _strip_flexGTC_tag_in_place
+ get_D50_XYZ_for_cicp_primaries
- _create_name_from_cicp_and_md5
- _get_hagc_data_md5
- _kColorSyncMetadataDisplayName
CStrings:
+ "HDR Metadata"
+ "com.apple.cmm.DerivedISO5Metadata"
- "Adaptive Gain Curve"
- "Adaptive Soft Clip Curve"
- "Content Color Volume"
- "Content HDR Reference White Luminance"
- "Content Light Level"
- "Headroom Adaptive Gain Curve"
- "Mastering Display Color Volume"
- "com.apple.cmm.MetadataDisplayName"
```
