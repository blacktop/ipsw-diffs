## com.apple.kernel

> `com.apple.kernel`

```diff

   __TEXT.__const: 0x36310
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x84c42
-  __TEXT.__os_log: 0x3ded0
+  __TEXT.__cstring: 0x84c95
+  __TEXT.__os_log: 0x3df3f
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x119d30
+  __DATA_CONST.__const: 0x119d80
   __DATA_CONST.__kalloc_type: 0x14300
   __DATA_CONST.__assert: 0xc58
   __DATA_CONST.__kalloc_var: 0x78f0

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x8a34cc
+  __TEXT_EXEC.__text: 0x8a382c
   __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0x1460
   __LASTDATA_CONST.__mod_init_func: 0x8

   __DATA.__data: 0x17ff9
   __DATA.__lock_grp: 0x5ac0
   __DATA.__percpu: 0x7870
-  __DATA.__common: 0x775d8
+  __DATA.__common: 0x77618
   __DATA.__bss: 0xa3db8
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x13548
+  __BOOTDATA.__init_entry_set: 0x13560
   __BOOTDATA.__init: 0x5b5c8
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0

   __LINKINFO.__symbolsets: 0x4804e
   Functions: 21127
   Symbols:   0
-  CStrings:  20441
+  CStrings:  20446
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__assert : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__kern_brk_desc : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __KLDDATA.__const : content changed
~ __DATA.__data : content changed
~ __BOOTDATA.__init : content changed
Functions:
~ vm_map_copyout_internal : 1876 -> 2052
~ sub_fffffe000a785160 -> sub_fffffe000a785210 : 1748 -> 1868
~ phys_attribute_clear_range_internal : 1128 -> 1164
~ mach_make_memory_entry_internal : 4444 -> 4480
~ sub_fffffe000a79aaf0 -> sub_fffffe000a79ac60 : 440 -> 504
~ sub_fffffe000a7d5b68 -> vm_shared_region_map_file : 292 -> 2196
~ vm_shared_region_map_file -> sub_fffffe000a7d65ac : 2180 -> 2052
~ sub_fffffe000a7d6510 -> sub_fffffe000a7d6db0 : 2052 -> 1996
~ sub_fffffe000a7d6d14 -> vm_shared_region_map_file_final : 1784 -> 520
~ vm_shared_region_map_file_final -> sub_fffffe000a7d7784 : 520 -> 416
~ sub_fffffe000a7d7c50 -> sub_fffffe000a7d7f60 : 1500 -> 1568
~ shared_region_map_and_slide_2_np : 1928 -> 1940
~ sub_fffffe000aee0408 -> sub_fffffe000aee0768 : 48120 -> 47256
CStrings:
+ "%s: downgrade JIT for entry [%p, %p)"
+ "mem_entry_wimg_non_writable"
+ "vm_map_copy_remap"
+ "vm_map_copyout_internal"
+ "vm_map_remap"

```
