## netbiosd

> `/usr/sbin/netbiosd`

```diff

-  __TEXT.__text: 0x27808
+  __TEXT.__text: 0x277e8
   __TEXT.__auth_stubs: 0xfc0
   __TEXT.__init_offsets: 0x18
   __TEXT.__const: 0x758
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ __ZN4nbns9workgroup9remove_bbERN8platform11counted_ptrINS_11name_recordEEE : 712 -> 716
~ __ZN4nbns9workgroup12get_bb_namesEiPNS_10names_list13NB_NAMES_LISTE : 396 -> 388
~ __ZNSt3__15dequeIP12nbt_packet_tNS_9allocatorIS2_EEE19__add_back_capacityEv : 480 -> 468
~ __Z14cifsd_bytedumpP10__CFStringPKvm : 444 -> 448
~ __ZL17nbt_put_nb_fqnamePvmmPK12netbios_name : 148 -> 152
~ __ZL11wg_get_infoN8platform11counted_ptrIN4nbns9workgroupEEE15BB_RENEW_TARGET : 2416 -> 2396
~ __ZL30nbb_process_mb_status_responseP15nb_chore_base_tPv : 1232 -> 1228

```
