## tailspind

> `/usr/libexec/tailspind`

```diff

-  __TEXT.__text: 0xe668
-  __TEXT.__auth_stubs: 0xc50
+  __TEXT.__text: 0xe888
+  __TEXT.__auth_stubs: 0xc60
   __TEXT.__objc_stubs: 0xba0
   __TEXT.__objc_methlist: 0x254
   __TEXT.__const: 0x134
-  __TEXT.__cstring: 0x134a
+  __TEXT.__cstring: 0x135f
   __TEXT.__objc_methname: 0xee2
-  __TEXT.__oslogstring: 0x29cc
+  __TEXT.__oslogstring: 0x2ab7
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x119
   __TEXT.__gcc_except_tab: 0x288
-  __TEXT.__unwind_info: 0x438
+  __TEXT.__unwind_info: 0x440
   __DATA_CONST.__const: 0x448
   __DATA_CONST.__cfstring: 0x840
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x638
+  __DATA_CONST.__auth_got: 0x640
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x3c0

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 284
-  Symbols:   254
-  CStrings:  586
+  Functions: 286
+  Symbols:   255
+  CStrings:  590
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _uuid_parse
CStrings:
+ "300MB buffer rollout: percent=%u, sampled=%{bool}d"
+ "Failed to parse kern.bootsessionuuid for 300MB buffer rollout sampling"
+ "Failed to read kern.bootsessionuuid for 300MB buffer rollout sampling: %{errno}d"
+ "is_12GB_or_greater: %{bool}d, is_feature_flag_enabled:  %{bool}d, is_in_rollout_sample: %{bool}d, is_300MB_eligible_device: %{bool}d, is_default_buffer_size: %{bool}d, is_game_mode_enabled: %{bool}d, should_apply_new_config: %{bool}d"
+ "kern.bootsessionuuid"
- "is_12GB_or_greater: %{bool}d, is_feature_flag_enabled:  %{bool}d, is_300MB_eligible_device: %{bool}d, is_default_buffer_size: %{bool}d, is_game_mode_enabled: %{bool}d, should_apply_new_config: %{bool}d"

```
