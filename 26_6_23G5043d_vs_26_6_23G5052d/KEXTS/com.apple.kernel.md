## com.apple.kernel

> `com.apple.kernel`

```diff

   __TEXT.__const: 0x36400
   __TEXT.__copyio_vectors: 0x2c0
   __TEXT.__cstring: 0x886d1
-  __TEXT.__os_log: 0x3df95
+  __TEXT.__os_log: 0x3e026
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
   __DATA_CONST.__const: 0x119e90

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x8b83d8
+  __TEXT_EXEC.__text: 0x8b8434
   __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0x1460
   __LASTDATA_CONST.__mod_init_func: 0x8

   __DATA.__lock_grp: 0x5b70
   __DATA.__percpu: 0x7870
   __DATA.__common: 0x777b8
-  __DATA.__bss: 0xa3e08
+  __DATA.__bss: 0xa4140
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init_entry_set: 0x13668
   __BOOTDATA.__init: 0x5b5c8

   __LINKINFO.__symbolsets: 0x48096
   Functions: 21340
   Symbols:   0
-  CStrings:  20759
+  CStrings:  20761
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__copyio_vectors : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__exclaves_bt : content changed
~ __DATA_CONST.__kern_brk_desc : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __LASTDATA_CONST.__mod_init_func : content changed
~ __KLDDATA.__const : content changed
~ __KLDDATA.__mod_init_func : content changed
~ __KLDDATA.__mod_term_func : content changed
~ __DATA.__data : content changed
~ __BOOTDATA.__init_entry_set : content changed
~ __BOOTDATA.__init : content changed
~ __BOOTDATA.__static_ifinit : content changed
Functions:
~ sub_fffffe000a75ecf0 -> sub_fffffe000a766cf0 : 592 -> 596
~ vm_map_enter : 5112 -> 5100
~ sub_fffffe000a94e09c -> sub_fffffe000a956094 : 1848 -> 1804
~ tracker_action : 1992 -> 1976
~ tracker_dump : 2412 -> 2496
~ tracker_entry_dump : 692 -> 768
~ sub_fffffe000af95314 -> sub_fffffe000af9d370 : 44268 -> 44176
CStrings:
+ "TRACKER - %s:%d Could not dump entries, entry tlv size %lu exceeds scratch pad size %lu\n"
+ "TRACKER - %s:%d Could not dump entry, buffer too small\n"

```
