## exclave_roottask

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.restore.im4p/exclave_roottask`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__chain_fixups`
- `__DATA.__shared_cache`
- `__DATA.__mod_init_func`
- `__DATA.__got`
- `__DATA.__thread_vars`
- `__DATA.__common`

```diff

-1490.0.5.0.0
-  __TEXT.__text: 0x4e9a88
+1490.0.20.0.0
+  __TEXT.__text: 0x4ea854
   __TEXT.__lcxx_override: 0xe4
-  __TEXT.__const: 0xf2260
-  __TEXT.__cstring: 0x3cbcc
-  __TEXT.__swift5_typeref: 0xcf0c
+  __TEXT.__const: 0xf2330
+  __TEXT.__cstring: 0x3d1fc
+  __TEXT.__swift5_typeref: 0xcf4c
   __TEXT.__swift5_capture: 0x155c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_reflstr: 0xb26c
+  __TEXT.__swift5_reflstr: 0xb27c
   __TEXT.__swift5_assocty: 0x7158
-  __TEXT.__swift5_fieldmd: 0x1256c
-  __TEXT.__constg_swiftt: 0x16368
+  __TEXT.__swift5_fieldmd: 0x125e0
+  __TEXT.__constg_swiftt: 0x163e0
   __TEXT.__swift5_builtin: 0xed8
   __TEXT.__swift5_mpenum: 0x534
   __TEXT.__swift5_protos: 0x494
-  __TEXT.__swift5_proto: 0x2e0c
-  __TEXT.__swift5_types: 0x1588
+  __TEXT.__swift5_proto: 0x2e14
+  __TEXT.__swift5_types: 0x1590
   __TEXT.__swift5_types2: 0x58
   __TEXT.__objc_methtype: 0x226
   __TEXT.__swift_as_entry: 0x22c

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x80
-  __TEXT.__eh_frame: 0x21dc4
-  __DATA.__data: 0xce60
+  __TEXT.__eh_frame: 0x21d6c
+  __DATA.__data: 0xcf50
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58
-  __DATA.__auth_ptr: 0x1130
-  __DATA.__const: 0x35668
+  __DATA.__auth_ptr: 0x1138
+  __DATA.__const: 0x353c8
   __DATA.__ENDPOINTS: 0xa46
   __DATA.__DEVICETREE: 0x30
   __DATA.__got: 0x190

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x20
   __DATA.__common: 0x21ff1
-  __DATA.__bss: 0x1b7e8
+  __DATA.__bss: 0x1b818
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 19227
+  Functions: 19267
   Symbols:   29
-  CStrings:  6041
+  CStrings:  6081
 
CStrings:
+ "  %s:"
+ "  frame permissions: read%s%s\n"
+ "  removed permissions: %#06lx\n"
+ " %s"
+ " bytes) does not fit in one frame ("
+ " execute"
+ " write"
+ "%s boot untyped %#018lx { ftid=%#03x; base=%#018llx; size=%#018llx; types=%#08llx; perms=%#06lx }\n"
+ "%s untyped { ftid=%#03x; base=%#018llx; size=%#018llx; types=%#08llx; perms=%#06lx }\n"
+ "%s(%zu): delete boot untyped %#018lx"
+ "%s(%zu): delete root normal r/w untyped cap"
+ "%s(%zu): delete root normal r/x untyped cap"
+ "(invalid type)"
+ "Boot-args string ("
+ "Empty-VLA endpoint marker missing argument position: "
+ "Empty-VLA marker collides with another argument at position "
+ "Failed to get bootargs "
+ "Failed to vas_slot_alloc() for boot-args"
+ "InternalExclaveLauncher/BootArgs.swift"
+ "L4_BootInfo_GetType(untyped_entry) == L4_Type_Untyped"
+ "L4_Type_"
+ "OWNERINFO"
+ "PMMInstance could not create Frame of "
+ "Unable to copy boot-args frame cap="
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
+ "dyld_enable_stdio"
+ "ensureDeviceTreeMapped()"
+ "exclave_disable_serial"
+ "exclaves_ec_initial_stack_frames"
+ "failed to mint boot-args cap"
+ "freed slot was not most recently allocated"
+ "init(allocateUntypedSize:with:rwFrames:)"
+ "integer value bound to non-value generic parameter"
+ "integer value where a type is required"
+ "keeping"
+ "received single-type untyped in roottask for type: %s"
+ "removed types"
+ "roottask finished"
+ "sanitized"
+ "types"
+ "x untyped must only be used to create r/x frame objects from normal managed memory, got (ftid: "
- "%s(%zu): Failed to copy frame parent cap to child cap"
- "%s(%zu): Failed to mint frame parent cap"
- "Creating launcher IPMM freelist span"
- "Creating launcher frame zero span"
- "Entered main Sc"
- "InternalExclaveLauncher/RunFlags.swift"
- "Parsing bundle device"
- "Serialized boot timing data"
- "Serializing boot timing data..."
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( frame_cap_parent, frame_cap_child)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Mint_Untyped( L4_BootInfo_GetSlot(entry), frame_cap_parent, (((L4_Word_t) 1) << (2)) | (((L4_Word_t) 1) << (1)), 0, 0, (((L4_TypeBitmap_t) 1) << (L4_Type_Arm64_FrameLevel0)), ((L4_Word_t) (0)) | (((L4_Word_t) 1) << (0)))'"
- "[StackshotConclaveSupport] discard_address_space_info no shared memory available"
- "[runflags warning] Couldn't get bootargs. Using metadata defaults only"
- "[xrt] liblibc_plat_cl4_entry:xrt__init_mapped_nonroot:default"
- "init(allocateUntypedSize:with:)"
- "mapDeviceTree()"
- "no fixup data for faultable range [%#lx, %#lx) found"
```
