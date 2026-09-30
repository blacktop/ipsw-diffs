## sptm.t6041.release.im4p

> `Firmware/sptm.t6041.release.im4p`

### Sections with Same Size but Changed Content

- `__LATE_CONST.__late_const`
- `__DATA.__auth_ptr`

```diff

-820.0.22.0.0
-  __TEXT.__cstring: 0x15790
+820.40.18.0.0
+  __TEXT.__cstring: 0x158cc
   __TEXT.__const: 0xa74
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x14
-  __DATA_CONST.__const: 0x7bf0
+  __DATA_CONST.__const: 0x7bf8
   __LATE_CONST.__late_const: 0x7c9b0
-  __TEXT_EXEC.__text: 0x5f074
+  __TEXT_EXEC.__text: 0x5f0a4
   __TEXT_EXEC.__exc: 0x2000
   __LAST.__pinst: 0xc
   __DATA.__data: 0xf
   __DATA.__auth_ptr: 0x18
   __DATA.__common: 0x17088
   __BOOTDATA.__data: 0x18000
-  Functions: 398
+  Functions: 399
   Symbols:   1
-  CStrings:  2527
+  CStrings:  2536
 
CStrings:
+ "%s(%s:%d) - fte(%p), new_type(%s), page_flags(%u), read_refcnt(%d) iommu_read_refcnt(%u)\n"
+ "%s: %s: iommu_read_refcnt (0x%hhx) > read_refcnt(0x%x) for FTE %p"
+ "%s: unexpected size %u for property '%s'"
+ "/chosen/manifest-properties"
+ "SPTM-820.40.18|2026-09-04:20:00:32.449636|"
+ "VIOLATION_NVME_ILLEGAL_HIBERNATION_QUEUE_LATCH"
+ "enforce_no_hib_latch"
+ "internal-use-only-unit"
+ "iuos"
+ "sptm_allow_vm_isa_internal_guests"
+ "sptm_is_iuou_or_iuos_device"
- "%s(%s:%d) - fte(%p), new_type(%s), page_flags(%u), read_refcnt(%d)\n"
- "SPTM-820.0.22|2026-08-08:13:06:06.975686|"
```
