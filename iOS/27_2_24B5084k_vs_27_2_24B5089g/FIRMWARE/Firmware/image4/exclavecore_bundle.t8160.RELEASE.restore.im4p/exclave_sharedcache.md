## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__data`
- `__DATA.__mod_init_func`
- `__DATA.__auth_ptr`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__DATA.__thread_vars`
- `__PDATA.__auth_ptr`
- `__PDATA.__mod_init_func`
- `__PDATA.__data`
- `__PDATA.__shared_cache`

```diff

-1777.40.23.502.2
-  __TEXT.__text: 0x5fa338
+1777.40.28.0.2
+  __TEXT.__text: 0x5faa84
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0x50a21
-  __TEXT.__const: 0x123d84
+  __TEXT.__cstring: 0x50df1
+  __TEXT.__const: 0x123fa4
   __TEXT.__swift5_typeref: 0x144ee
   __TEXT.__swift5_reflstr: 0x13508
   __TEXT.__swift5_assocty: 0x7d10

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xb8
-  __TEXT.__eh_frame: 0x35db0
+  __TEXT.__eh_frame: 0x35da8
   __DATA.__TIGHTBEAM_VT: 0x8a0
   __DATA.__TIGHTBEAM: 0x238
-  __DATA.__const: 0x3e5d0
+  __DATA.__const: 0x3e5e0
   __DATA.__data: 0x19110
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1a536
+  __DATA.__ENDPOINTS: 0x1a744
   __DATA.__auth_ptr: 0x2490
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x380

   __DATA.__thread_bss: 0x30
   __DATA.__common: 0x72a
   __PDATA.__auth_ptr: 0x280
-  __PDATA.__const: 0x6800
+  __PDATA.__const: 0x6810
   __PDATA.__objc_imageinfo: 0x8
   __PDATA.__mod_init_func: 0x18
   __PDATA.__data: 0x2af0
   __PDATA.__ENDPOINTS: 0x838
   __PDATA.__shared_cache: 0x70
-  __PDATA.__bss: 0xba48
+  __PDATA.__bss: 0xbae8
   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   Functions: 657
   Symbols:   1
-  CStrings:  7418
+  CStrings:  7432
 
Functions:
~ sub_7ffe468 : 141032 -> 141184
~ sub_8024458 -> sub_80244f0 : 425680 -> 427472
~ sub_808c328 -> sub_808cac0 : 173736 -> 173984
~ sub_80b6b48 -> sub_80b73d8 : 184 -> 232
~ sub_818bb84 -> sub_818c444 : 970800 -> 970580
~ sub_82c68f4 -> sub_82c70d8 : 409180 -> 409228
~ sub_85931d8 -> sub_85939ec : 407420 -> 407220
~ sub_85f6954 -> sub_85f70a0 : 4004 -> 4008
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
