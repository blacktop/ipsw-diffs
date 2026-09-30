## sptm.t8132.release.im4p

> `Firmware/sptm.t8132.release.im4p`

### Sections with Same Size but Changed Content

- `__LATE_CONST.__late_const`

```diff

-820.0.16.0.0
-  __TEXT.__cstring: 0x154af
+820.0.22.0.0
+  __TEXT.__cstring: 0x15790
   __TEXT.__const: 0xa74
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x14
-  __DATA_CONST.__const: 0x7be8
+  __DATA_CONST.__const: 0x7bf0
   __LATE_CONST.__late_const: 0x7c8f0
-  __TEXT_EXEC.__text: 0x5e9bc
+  __TEXT_EXEC.__text: 0x5f010
   __TEXT_EXEC.__exc: 0x2000
   __LAST.__pinst: 0xc
   __DATA.__data: 0xf

   __DATA.__bss: 0x60a8
   __DATA.__common: 0xe688
   __BOOTDATA.__data: 0x18000
-  Functions: 397
+  Functions: 398
   Symbols:   1
-  CStrings:  2516
+  CStrings:  2527
 
CStrings:
+ "%s: dart %p (%s:%u): DART instance %u: Attempt to modify locked reg at offset %x 0x%08x->0x%08x"
+ "%s: dart %p (%s:%u): DART instance %u: HW reported num_sids %u exceeds T8110_DART_MAX_SIDS %u"
+ "%s: dart %p (%s:%u): DART instance %u: SID %u: 3-level translation with noncompliant dead mappings and flush-by-DVA is unsupported on pre-Gen3 DARTs"
+ "%s: dart %p (%s:%u): DART instance %u: SID_CONFIG[%u] 0x%08x does not match shadow 0x%08x"
+ "%s: dart %p (%s:%u): DART instance %u: TTBR[%u] 0x%08x does not match shadow 0x%08x"
+ "%s: dart %p (%s:%u): DART instance %u: max_sid %#x doesn't match with the rest %#x"
+ "%s: non-canonical or unaligned output address %#llx"
+ "SPTM-820.0.22|2026-08-10:00:18:14.298301|"
+ "VIOLATION_T8110_DART_SID_TRANSLATION_DISABLED"
+ "hib_validate_io_buffer_page"
+ "sptm_t8110dart_sk_tlbi_request"
+ "t8110dart_read_dapf_reg"
+ "t8110dart_verify_sid_config"
+ "t8110dart_verify_sid_shadow_config"
- "%s: dart %p (%s:%u): DART instance %u: Attempt to modify locked reg %p 0x%08x->0x%08x"
- "SPTM-820.0.16|2026-07-10:21:42:00.266834|"
- "start_dva_offset"
```
