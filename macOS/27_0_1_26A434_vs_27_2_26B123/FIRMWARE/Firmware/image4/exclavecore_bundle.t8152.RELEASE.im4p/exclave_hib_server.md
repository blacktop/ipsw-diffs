## exclave_hib_server

> `Firmware/image4/exclavecore_bundle.t8152.RELEASE.im4p/exclave_hib_server`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA.__data`
- `__DATA.__auth_ptr`
- `__DATA.__shared_cache`
- `__DATA.__mod_init_func`

```diff

-1490.0.21.0.0
-  __TEXT.__text: 0x3ece8
+1490.40.28.0.0
+  __TEXT.__text: 0x3f478
   __TEXT.__const: 0x1c910
-  __TEXT.__cstring: 0xde78
+  __TEXT.__cstring: 0xe291
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0

   __TEXT.__eh_frame: 0x50
   __DATA.__MMIOREGS: 0x287
   __DATA.__data: 0x20a8
-  __DATA.__const: 0xda8
+  __DATA.__const: 0xdb0
   __DATA.__ENDPOINTS: 0x62a
   __DATA.__auth_ptr: 0x8
   __DATA.__shared_cache: 0x38

   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__bss: 0x4e9b8
+  __DATA.__bss: 0x4ea58
   __DATA.__common: 0x1760
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0

   __PDATA.__shared_cache: 0x0
   Functions: 16
   Symbols:   4
-  CStrings:  1240
+  CStrings:  1258
 
Functions:
~ sub_800cbf8 -> sub_800ccb0 : 7400 -> 7476
~ sub_800e8e0 -> sub_800e9e4 : 123048 -> 124900
~ sub_802d428 -> sub_802dc68 : 18728 -> 18184
~ sub_8031dc0 -> sub_80323e0 : 39784 -> 40152
CStrings:
+ "!DO_CHUNKS_OVERLAP(currp, victimp) && !DO_CHUNKS_OVERLAP(currp->next, victimp)"
+ "!os_add_overflow(round_bytes, HEADER_UNIT_SIZE * UNIT_SIZE, &alloc_bytes)"
+ "!os_mul_overflow(units, UNIT_SIZE, &nb)"
+ "!overflow"
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
+ "_insecure_random_buf"
+ "applyFixups: rebase failed for %#lx (region %zd)"
+ "applyFixups: region %zd has NULL fixup_metadata_pointer"
+ "delta_output != fault->write_buffer"
+ "lcm"
+ "round_bytes >= alloc_bytes"
+ "s[0] || s[1]"
+ "vas_return_code(drop_depop) != VAS_SUCCESS"
- "!(alignment % sizeof(Header)) && !(alignment % UNIT_SIZE)"
- "!os_mul_overflow(nu + PAD_ALLOC(align), UNIT_SIZE, &nb)"
- "B16@?0^{vas_core_span={?=CQQCCCCC^vQ}iC[3C]{?=^?^?}^vQQ^{vas_core_vas}^{vas_core_span}^{vas_core_span}Q^{vas_segment}{spanmap_struct=b2b4b22b36}{_liblibc_mtx=[16C]}B{?=^{vas_core_span}^^{vas_core_span}}{spanmap_struct=b2b4b22b36}}8"
- "alloc_bytes >= sz"
- "p->size * UNIT_SIZE >= sizeof(Header)"
```
