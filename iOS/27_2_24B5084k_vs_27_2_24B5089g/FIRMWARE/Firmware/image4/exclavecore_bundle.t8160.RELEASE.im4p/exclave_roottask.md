## exclave_roottask

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.im4p/exclave_roottask`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__chain_fixups`
- `__TEXT.__eh_frame`
- `__DATA.__shared_cache`
- `__DATA.__mod_init_func`
- `__DATA.__auth_ptr`
- `__DATA.__got`
- `__DATA.__thread_vars`

```diff

-1490.40.21.0.0
-  __TEXT.__text: 0x4ea31c
+1490.40.25.0.0
+  __TEXT.__text: 0x4eabdc
   __TEXT.__lcxx_override: 0xd0
   __TEXT.__const: 0xf28a0
-  __TEXT.__cstring: 0x3d54c
+  __TEXT.__cstring: 0x3d90c
   __TEXT.__swift5_typeref: 0xd07c
   __TEXT.__swift5_capture: 0x155c
   __TEXT.__swift5_entry: 0x8

   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x80
   __TEXT.__eh_frame: 0x22254
-  __DATA.__data: 0xcf68
+  __DATA.__data: 0xcf70
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58
   __DATA.__auth_ptr: 0x1178
-  __DATA.__const: 0x358b8
+  __DATA.__const: 0x358c8
   __DATA.__ENDPOINTS: 0xa46
   __DATA.__DEVICETREE: 0x30
   __DATA.__got: 0x190

   __PDATA.__shared_cache: 0x0
   Functions: 841
   Symbols:   29
-  CStrings:  6096
+  CStrings:  6110
 
Functions:
~ sub_c0067e9c : 234948 -> 236876
~ sub_c01394dc -> sub_c0139c64 : 96756 -> 96764
~ sub_c0151048 -> sub_c01517d8 : 184 -> 232
~ sub_c01586c8 -> sub_c0158e88 : 481228 -> 481232
~ sub_c04dbb90 -> sub_c04dc354 : 58900 -> 59152
CStrings:
+ "%s(%zu): failed to delete delta scratch RO span slot"
+ "%s(%zu): failed to delete delta scratch RO temp cap"
+ "%s(%zu): failed to map frame into delta scratch RO span"
+ "B16@?0^{vas_core_span={?=CQQCCCCC^vQ}iC[3C]{?=^?^?^?}^vQQ^{vas_core_vas}^{vas_core_span}^{vas_core_span}Q^{vas_segment}{spanmap_struct=b2b4b22b36}{_liblibc_mtx=[16C]}B{?=^{vas_core_span}^^{vas_core_span}}{spanmap_struct=b2b4b22b36}}8"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(scratch->ro_span_slot)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(scratch->ro_temp_slot)'"
+ "Unexpected L4_Error: %s(%zu) err='_map_this_frame_readonly(scratch->ro_span, (uintptr_t)ro_words, scratch->ro_temp_slot)'"
+ "[VAS abort in function %s at line %d] [%s] could not allocate fixup span for fault handler\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] Could not depopulate temp span (drop): %s (0x%04hx)\n\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] _delta_page_against_original returned unexpected result(%p)\n"
+ "_delta_page_against_original"
+ "applyFixups: rebase failed for %#lx (region %zd)"
+ "applyFixups: region %zd has NULL fixup_metadata_pointer"
+ "delta_output != fault->write_buffer"
+ "vas_return_code(drop_depop) != VAS_SUCCESS"
- "B16@?0^{vas_core_span={?=CQQCCCCC^vQ}iC[3C]{?=^?^?}^vQQ^{vas_core_vas}^{vas_core_span}^{vas_core_span}Q^{vas_segment}{spanmap_struct=b2b4b22b36}{_liblibc_mtx=[16C]}B{?=^{vas_core_span}^^{vas_core_span}}{spanmap_struct=b2b4b22b36}}8"
```
