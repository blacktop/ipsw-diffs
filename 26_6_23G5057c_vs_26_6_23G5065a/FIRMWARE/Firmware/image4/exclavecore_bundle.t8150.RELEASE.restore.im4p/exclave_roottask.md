## exclave_roottask

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.restore.im4p/exclave_roottask`

```diff

-  __TEXT.__text: 0x4b7f14
+  __TEXT.__text: 0x4b93d4
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__const: 0xedbe0
-  __TEXT.__cstring: 0x3a98c
-  __TEXT.__swift5_typeref: 0xc122
+  __TEXT.__const: 0xedba0
+  __TEXT.__cstring: 0x3aecc
+  __TEXT.__swift5_typeref: 0xc152
   __TEXT.__swift5_capture: 0x1608
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_fieldmd: 0x11008

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x78
-  __TEXT.__eh_frame: 0x1ccfc
+  __TEXT.__eh_frame: 0x1ccac
   __DATA.__data: 0xbe90
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58
-  __DATA.__auth_ptr: 0xfa0
-  __DATA.__const: 0x30b88
+  __DATA.__auth_ptr: 0xfa8
+  __DATA.__const: 0x30c38
   __DATA.__ENDPOINTS: 0xa46
   __DATA.__DEVICETREE: 0x30
   __DATA.__got: 0x198

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
   __DATA.__common: 0x21fb1
-  __DATA.__bss: 0x13100
+  __DATA.__bss: 0x13130
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 17670
+  Functions: 17685
   Symbols:   27
-  CStrings:  5884
+  CStrings:  5918
 
Sections:
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__chain_fixups : content changed
~ __DATA.__data : content changed
~ __DATA.__mod_init_func : content changed
~ __DATA.__got : content changed
~ __DATA.__thread_vars : content changed
~ __DATA.__common : content changed
CStrings:
+ "  %s:"
+ "  frame permissions: read%s%s\n"
+ "  removed permissions: %#06lx\n"
+ " %s"
+ " execute"
+ " write"
+ "%s boot untyped %#018lx { ftid=%#03x; base=%#018llx; size=%#018llx; types=%#08llx; perms=%#06lx }\n"
+ "%s untyped { ftid=%#03x; base=%#018llx; size=%#018llx; types=%#08llx; perms=%#06lx }\n"
+ "%s(%zu): delete boot untyped %#018lx"
+ "%s(%zu): delete root normal r/w untyped cap"
+ "%s(%zu): delete root normal r/x untyped cap"
+ "(invalid type)"
+ "L4_BootInfo_GetType(untyped_entry) == L4_Type_Untyped"
+ "L4_Type_"
+ "PMMInstance could not create Frame of "
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( _boot_info.normal_untyped.rw_cap, frame_cap_parent )'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( frame_cap_parent, frame_cap_child )'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy(_boot_info.normal_untyped.rx_cap, slot)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(L4_BootInfo_GetSlot(entry))'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(_boot_info.normal_untyped.rw_cap)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(_boot_info.normal_untyped.rx_cap)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Mint_Untyped( source_cap, dest_slot, (((L4_Word_t) 1) << (2)) | (((L4_Word_t) 1) << (1)), L4_BootInfo_Untyped_GetBase(untyped_entry), L4_BootInfo_Untyped_GetSize(untyped_entry), type_bitmap, permissions )'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Move(entry_slot, temp_slot)'"
+ "_mint_reduced_untyped"
+ "_sanitize_untyped_entry"
+ "attempted to copy non-existant normal r/x untyped"
+ "cannot sanitize untypeds before bootinfo initialized"
+ "cbinfo_copy_normal_rx_untyped"
+ "cbinfo_drop_untypeds"
+ "created"
+ "deleting"
+ "derived"
+ "freed slot was not most recently allocated"
+ "init(allocateUntypedSize:with:rwFrames:)"
+ "keeping"
+ "received single-type untyped in roottask for type: %s"
+ "removed types"
+ "sanitized"
+ "types"
+ "x untyped must only be used to create r/x frame objects from normal managed memory, got (ftid: "
- "%s(%zu): Failed to copy frame parent cap to child cap"
- "%s(%zu): Failed to mint frame parent cap"
- "PMMInstance could not create Frame"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( frame_cap_parent, frame_cap_child)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Mint_Untyped( L4_BootInfo_GetSlot(entry), frame_cap_parent, (((L4_Word_t) 1) << (2)) | (((L4_Word_t) 1) << (1)), 0, 0, (((L4_TypeBitmap_t) 1) << (L4_Type_Arm64_FrameLevel0)), ((L4_Word_t) (0)) | (((L4_Word_t) 1) << (0)))'"
- "init(allocateUntypedSize:with:)"

```
