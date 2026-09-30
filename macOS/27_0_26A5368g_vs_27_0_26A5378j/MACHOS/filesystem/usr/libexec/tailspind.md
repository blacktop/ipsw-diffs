## tailspind

> `/usr/libexec/tailspind`

```diff

-  __TEXT.__text: 0xcd14
-  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__text: 0xcf38
+  __TEXT.__auth_stubs: 0xa20
   __TEXT.__objc_stubs: 0x8e0
   __TEXT.__objc_methlist: 0x254
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x11dc
+  __TEXT.__cstring: 0x11f1
   __TEXT.__objc_methname: 0xcf1
-  __TEXT.__oslogstring: 0x2281
+  __TEXT.__oslogstring: 0x236c
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x119
   __TEXT.__gcc_except_tab: 0x288

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x518
+  __DATA_CONST.__auth_got: 0x520
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x3c0

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 263
-  Symbols:   206
-  CStrings:  506
+  Functions: 265
+  Symbols:   207
+  CStrings:  510
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
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
