## sptm.t8103.release.im4p

> `Firmware/sptm.t8103.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA.__auth_ptr`

```diff

-820.0.16.0.0
-  __TEXT.__cstring: 0x12020
+820.0.22.0.0
+  __TEXT.__cstring: 0x12e46
   __TEXT.__const: 0xa2c
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x14
-  __DATA_CONST.__const: 0x6dc8
-  __LATE_CONST.__late_const: 0x7c838
-  __TEXT_EXEC.__text: 0x53c10
+  __DATA_CONST.__const: 0x7490
+  __LATE_CONST.__late_const: 0x7c840
+  __TEXT_EXEC.__text: 0x55c78
   __TEXT_EXEC.__exc: 0x2000
   __LAST.__pinst: 0xc
   __DATA.__data: 0xf

   __DATA.__bss: 0x5fb0
   __DATA.__common: 0xb288
   __BOOTDATA.__data: 0x18000
-  Functions: 354
+  Functions: 370
   Symbols:   1
-  CStrings:  2183
+  CStrings:  2278
 
CStrings:
+ "%s(%s:%d) - fte(%p), fte->type(%s), flags(%u), action(%u)\n"
+ "%s(%s:%d) - fte(%p), fte->type(%s), fte->in_flight_ops(%u), action(%u)\n"
+ "%s(%s:%d) - fte(%p), fte->type(%s), policy(%u), action(%u)\n"
+ "%s: Frame expected to have been acquired shared has not been acquired shared %p %s %u"
+ "%s: Only CPUTrace is allowed to call %s() with type %u - %s/%s"
+ "%s: assert '!(paddr >> PROD_TRC_STRM_BASE_ADDR_SIZE)' failed."
+ "%s: assert '!(region_size & SPTM_PAGE_MASK)' failed."
+ "%s: assert '!(region_start & SPTM_PAGE_MASK)' failed."
+ "%s: assert '!(size_limit >> PROD_TRC_STRM_BASE_VALID_BASE)' failed."
+ "%s: assert '!__builtin_add_overflow(carveout_start_paddr, carveout_size, &carveout_end_paddr)' failed."
+ "%s: assert '!__builtin_add_overflow(cputrace_instance->initialized_count, 1, &cputrace_instance->initialized_count)' failed."
+ "%s: assert '!__builtin_add_overflow(region_size, SPTM_PAGE_SIZE, &region_size)' failed."
+ "%s: assert '!__builtin_add_overflow(region_start, region_size, &region_end)' failed."
+ "%s: assert '!__builtin_sub_overflow(cputrace_instance->initialized_count, 1, &cputrace_instance->initialized_count)' failed."
+ "%s: assert '(!region_start) == (!region_size)' failed."
+ "%s: assert 'carveout_size' failed."
+ "%s: assert 'carveout_start_paddr' failed."
+ "%s: assert 'cluster_id < CPUTRACE_NB_CLUSTERS' failed."
+ "%s: assert 'nb_units' failed."
+ "%s: assert 'region_size >= SPTM_PAGE_SIZE' failed."
+ "%s: carveout_nb_frames %#llx %#llx does not fit in an unsigned int."
+ "%s: cluster not deinitialized before hibernating."
+ "%s: clusters not deinitialized before hibernating."
+ "%s: invalid bootstrap frames type %s, expected SPTM_IOMMU_BOOTSTRAP or XNU_CPUTRACE_PA_BUFFER."
+ "%s: non-canonical or unaligned output address %#llx"
+ "(&cputrace_instance->va_guard)"
+ "CPUTRACE"
+ "SPTM-820.0.22|2026-08-10:00:18:14.298301|"
+ "SPTM_CPUTRACE_ENDPOINTID_IS_MODE"
+ "SPTM_CPUTRACE_ENDPOINTID_PA_CRV_ADDR"
+ "SPTM_CPUTRACE_ENDPOINTID_PA_CRV_SIZE"
+ "SPTM_CPUTRACE_ENDPOINTID_PA_SET_BASE"
+ "SPTM_CPUTRACE_ENDPOINTID_PA_START"
+ "SPTM_CPUTRACE_ENDPOINTID_PA_STOP"
+ "SPTM_CPUTRACE_ENDPOINTID_VA_DEINIT"
+ "SPTM_CPUTRACE_ENDPOINTID_VA_FRM_LOCK"
+ "SPTM_CPUTRACE_ENDPOINTID_VA_FRM_UNLOCK"
+ "SPTM_CPUTRACE_ENDPOINTID_VA_INIT"
+ "SPTM_CPUTRACE_ENDPOINTID_VA_SET_BASE"
+ "SPTM_CPUTRACE_ENDPOINTID_VA_START"
+ "SPTM_CPUTRACE_ENDPOINTID_VA_STOP"
+ "VIOLATION_CPUTRACE_MODE_MISMATCH"
+ "VIOLATION_CPUTRACE_PA_BUFFER"
+ "VIOLATION_CPUTRACE_STRM_BASE"
+ "VIOLATION_CPUTRACE_VA_BUFFER"
+ "VIOLATION_CPUTRACE_VA_DEINITIALIZED"
+ "VIOLATION_CPUTRACE_VA_FRAME"
+ "VIOLATION_CPUTRACE_VA_INITIALIZED"
+ "VIOLATION_CPUTRACE_VA_RACE"
+ "VIOLATION_CPUTRACE_VA_REGION"
+ "VIOLATION_CPUTRACE_VA_TYPE"
+ "VIOLATION_CPUTRACE_VA_UNMAPPED"
+ "VIOLATION_T8020_DART_PS_WR_DIS_RACE"
+ "VIOLATION_T8020_DART_SID_TRANSLATION_DISABLED"
+ "apt-carveout-size-mb"
+ "cputrace.c"
+ "cputrace_bootstrap"
+ "cputrace_get_carveout_size_mib"
+ "cputrace_get_cluster_id"
+ "cputrace_get_cluster_id()"
+ "cputrace_instance->initialized_count"
+ "cputrace_mode_bits()"
+ "cputrace_pa_get_stream_base"
+ "cputrace_va_get_stream_base"
+ "cputrace_va_locked_frame_lock"
+ "cputrace_va_locked_frame_unlock"
+ "cputrace_va_locked_region_add"
+ "cputrace_va_locked_region_remove"
+ "cputrace_validation.c"
+ "frame_paddr"
+ "frame_vaddr"
+ "hib_validate_io_buffer_page"
+ "iommu_bootstrap_alloc_frames_type"
+ "iommu_set_page_pinned_state"
+ "new_frame_paddr"
+ "region_size"
+ "region_start"
+ "set_page_pinned_state"
+ "sptm_cputrace_hib_wake"
+ "sptm_cputrace_set_base"
+ "sptm_cputrace_start"
+ "sptm_cputrace_stop"
+ "sptm_cputrace_va_deinit"
+ "sptm_cputrace_va_frame_lock"
+ "sptm_cputrace_va_frame_unlock"
+ "sptm_cputrace_va_init"
+ "sptm_cputrace_va_set_base"
+ "sptm_cputrace_va_start"
+ "sptm_cputrace_va_stop"
+ "va_region_id"
+ "validate_cputrace_pa_buffer"
+ "validate_cputrace_strm_base_id"
+ "validate_cputrace_va_buffer"
+ "validate_cputrace_va_frame_vaddr"
+ "validate_cputrace_va_region_id"
+ "validate_sptm_cputrace_mode"
- "SPTM-820.0.16|2026-07-10:21:42:00.266834|"
```
