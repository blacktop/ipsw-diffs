## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.im4p/exclave_sharedcache`

```diff

-  __TEXT.__text: 0xd2c0d4
+  __TEXT.__text: 0xd2cee8
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__cstring: 0x969d1
-  __TEXT.__const: 0x17fed4
-  __TEXT.__swift5_typeref: 0x2789a
+  __TEXT.__cstring: 0x96d41
+  __TEXT.__const: 0x17fec4
+  __TEXT.__swift5_typeref: 0x278da
   __TEXT.__swift5_reflstr: 0x388d8
   __TEXT.__swift5_assocty: 0xd2e0
   __TEXT.__swift5_fieldmd: 0x56850

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x118
-  __TEXT.__eh_frame: 0x73600
+  __TEXT.__eh_frame: 0x73638
   __DATA.__TIGHTBEAM_VT: 0x11a0
   __DATA.__TIGHTBEAM: 0x470
   __DATA.__data: 0x45488
-  __DATA.__const: 0xdab80
+  __DATA.__const: 0xdac30
   __DATA.__mod_init_func: 0x40
   __DATA.__ENDPOINTS: 0x148c0
-  __DATA.__auth_ptr: 0x6e50
+  __DATA.__auth_ptr: 0x6e58
   __DATA.__DEVICETREE: 0x30
   __DATA.__shared_cache: 0x2a0
   __DATA.__DARTS: 0x93f

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x38
-  __DATA.__bss: 0x23770
+  __DATA.__bss: 0x237a0
   __DATA.__common: 0x29a9
   __PDATA.__data: 0x24e0
   __PDATA.__const: 0x5e38

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 50191
+  Functions: 50204
   Symbols:   1
-  CStrings:  14252
+  CStrings:  14277
 
Sections:
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__chain_fixups : content changed
~ __DATA.__TIGHTBEAM_VT : content changed
~ __DATA.__TIGHTBEAM : content changed
~ __DATA.__data : content changed
~ __DATA.__mod_init_func : content changed
~ __DATA.__shared_cache : content changed
~ __DATA.__got : content changed
~ __DATA.__thread_vars : content changed
~ __DATA.__common : content changed
~ __PDATA.__data : content changed
~ __PDATA.__const : content changed
~ __PDATA.__shared_cache : content changed
~ __PDATA.__mod_init_func : content changed
~ __PDATA.__auth_ptr : content changed
~ __PDATA.__bss : content changed
~ __PDATA.__common : content changed
CStrings:
+ "  %s:"
+ "  frame permissions: read%s%s\n"
+ "  removed permissions: %#06lx\n"
+ " %s"
+ " execute"
+ " write"
+ "%s untyped { ftid=%#03x; base=%#018llx; size=%#018llx; types=%#08llx; perms=%#06lx }\n"
+ "(invalid type)"
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Thu Jul  9 23:29:21 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
+ "Build Date: Wed Jul  8 23:43:39 PDT 2026"
+ "ExclaveOS Image4 Framework Version 7.0.0: Thu Jul  9 23:29:21 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
+ "ExclaveSISP-5.604"
+ "Fri Jul 10 00:06:45 PDT 2026"
+ "L4_BootInfo_GetType(untyped_entry) == L4_Type_Untyped"
+ "L4_Type_"
+ "PMMInstance could not create Frame of "
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( _boot_info.normal_untyped.rw_cap, frame_cap_parent )'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( frame_cap_parent, frame_cap_child )'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy(_boot_info.normal_untyped.rx_cap, slot)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(temp_slot)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Mint_Untyped( source_cap, dest_slot, (((L4_Word_t) 1) << (2)) | (((L4_Word_t) 1) << (1)), L4_BootInfo_Untyped_GetBase(untyped_entry), L4_BootInfo_Untyped_GetSize(untyped_entry), type_bitmap, permissions )'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Move(entry_slot, temp_slot)'"
+ "_mint_reduced_untyped"
+ "_sanitize_untyped_entry"
+ "attempted to copy non-existant normal r/x untyped"
+ "cannot sanitize untypeds before bootinfo initialized"
+ "cbinfo_copy_normal_rx_untyped"
+ "created"
+ "derived"
+ "freed slot was not most recently allocated"
+ "init(allocateUntypedSize:with:rwFrames:)"
+ "received single-type untyped in roottask for type: %s"
+ "removed types"
+ "sanitized"
+ "types"
+ "x untyped must only be used to create r/x frame objects from normal managed memory, got (ftid: "
- "%s(%zu): Failed to copy frame parent cap to child cap"
- "%s(%zu): Failed to mint frame parent cap"
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Fri Jun 26 16:50:51 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
- "Build Date: Fri Jun 26 16:39:28 PDT 2026"
- "ExclaveOS Image4 Framework Version 7.0.0: Fri Jun 26 16:50:51 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
- "ExclaveSISP-5.602"
- "Fri Jun 26 17:22:39 PDT 2026"
- "PMMInstance could not create Frame"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( frame_cap_parent, frame_cap_child)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Mint_Untyped( L4_BootInfo_GetSlot(entry), frame_cap_parent, (((L4_Word_t) 1) << (2)) | (((L4_Word_t) 1) << (1)), 0, 0, (((L4_TypeBitmap_t) 1) << (L4_Type_Arm64_FrameLevel0)), ((L4_Word_t) (0)) | (((L4_Word_t) 1) << (0)))'"
- "init(allocateUntypedSize:with:)"

```
