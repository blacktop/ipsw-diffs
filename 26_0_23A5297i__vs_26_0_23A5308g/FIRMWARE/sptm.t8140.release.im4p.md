## sptm.t8140.release.im4p

> `sptm.t8140.release.im4p`

```diff

-611.0.21.0.1
+611.0.26.0.0
+  __TEXT.__cstring: 0x1101a
   __TEXT.__const: 0xa00
-  __TEXT.__cstring: 0x10d37
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
-  __DATA_CONST.__const: 0x73d0
+  __DATA_CONST.__const: 0x73e0
   __LATE_CONST.__late_const: 0x65880
-  __TEXT_EXEC.__text: 0x576b8
+  __TEXT_EXEC.__text: 0x57c84
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0xf
-  __DATA.__bss: 0x5e28
+  __DATA.__bss: 0x6028
   __DATA.__common: 0x5938
   __BOOTDATA.__data: 0x14000
-  UUID: F0A2B582-B678-36FD-9FBA-8DD69FA641C7
-  Functions: 361
+  UUID: C48B270A-7B8A-3AAE-ACF5-B3835467346D
+  Functions: 365
   Symbols:   1
-  CStrings:  2151
+  CStrings:  2168
 
CStrings:
+ "!((uint64_t)sptm_hib_unaligned_read_uint32(&range->flags) & (uint64_t)(HIB_PHYS_RANGE_FLAG_PROHIBITED | HIB_PHYS_RANGE_FLAG_DEV_MEM))"
+ "!(io_range->flags & HIB_PHYS_RANGE_FLAG_PROHIBITED)"
+ "!(wimg & (PMAP_IO_RANGE_NOT_IO | PMAP_IO_RANGE_PROHIBIT_HIB_WRITE))"
+ "%s: %u addr 0x%llx length 0x%llx wimg %#x overlaps managed physical memory"
+ "%s: region marked as both needing hibernation and forbidden for write during hib restore: addr %p, size %zu, wimg %#x"
+ "SPTM-611.0.26|2025-07-24:22:38:39.658493|"
+ "VIOLATION_UAT_ILLEGAL_HW_FW_PERMS"
+ "VIOLATION_UAT_ILLEGAL_MAP_OPTION"
+ "bitmap_page_is_valid(first_free_paddr, header, &temp_dt)"
+ "dt != NULL"
+ "fw_read"
+ "fw_write"
+ "hw_fw_perms_to_dprr_index"
+ "hw_read"
+ "hw_write"
+ "io_range != NULL && (io_range->flags & HIB_PHYS_RANGE_FLAG_NEEDS_HIB)"
+ "io_range == NULL || !(io_range->flags & HIB_PHYS_RANGE_FLAG_PROHIBITED)"
+ "io_range->flags & HIB_PHYS_RANGE_FLAG_NEEDS_HIB"
+ "lut_index"
+ "upper != NULL"
- "%s: %u addr 0x%llx length 0x%llx overlaps managed physical memory"
- "SPTM-611.0.21.0.1|2025-07-14:23:07:48.703895|"
- "bitmap_page_is_valid(first_free_paddr, header)"

```
