## exclave_pmm_exclave

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_pmm_exclave`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA.__data`
- `__DATA.__auth_ptr`
- `__DATA.__shared_cache`
- `__DATA.__mod_init_func`

```diff

-1490.40.21.0.0
-  __TEXT.__text: 0x4cc7c
+1490.40.25.0.0
+  __TEXT.__text: 0x4d4f8
   __TEXT.__const: 0x1d140
-  __TEXT.__cstring: 0x11dc5
+  __TEXT.__cstring: 0x1217c
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x60
   __TEXT.__eh_frame: 0x50
-  __DATA.__const: 0x1498
+  __DATA.__const: 0x14a0
   __DATA.__data: 0x2421
   __DATA.__auth_ptr: 0x30
   __DATA.__ENDPOINTS: 0x93f

   __PDATA.__shared_cache: 0x0
   Functions: 14
   Symbols:   4
-  CStrings:  1517
+  CStrings:  1531
 
Functions:
~ sub_80174e4 -> sub_8017574 : 125940 -> 127716
~ sub_8036b68 -> sub_80372e8 : 76952 -> 77200
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
