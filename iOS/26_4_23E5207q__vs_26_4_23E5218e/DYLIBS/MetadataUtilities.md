## MetadataUtilities

> `/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities`

```diff

-2418.4.8.2.100
-  __TEXT.__text: 0x57a74
-  __TEXT.__auth_stubs: 0x1a30
-  __TEXT.__objc_methlist: 0x47c
-  __TEXT.__const: 0x3d46
-  __TEXT.__cstring: 0x6f88
-  __TEXT.__oslogstring: 0x1498
+2418.4.10.1.0
+  __TEXT.__text: 0x581fc
+  __TEXT.__auth_stubs: 0x1a80
+  __TEXT.__objc_methlist: 0x494
+  __TEXT.__const: 0x3d36
+  __TEXT.__cstring: 0x7022
+  __TEXT.__oslogstring: 0x14f9
   __TEXT.__ustring: 0x9a
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0xb28
+  __TEXT.__unwind_info: 0xb48
   __TEXT.__objc_classname: 0xdc
-  __TEXT.__objc_methname: 0xfe6
-  __TEXT.__objc_methtype: 0x641
-  __TEXT.__objc_stubs: 0x900
+  __TEXT.__objc_methname: 0x102c
+  __TEXT.__objc_methtype: 0x6bb
+  __TEXT.__objc_stubs: 0x940
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__const: 0x1048
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d8
+  __DATA_CONST.__objc_selrefs: 0x3e8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x370
-  __AUTH_CONST.__auth_got: 0xd28
+  __AUTH_CONST.__auth_got: 0xd50
   __AUTH_CONST.__const: 0x8d8
   __AUTH_CONST.__cfstring: 0x4b20
-  __AUTH_CONST.__objc_const: 0x1158
+  __AUTH_CONST.__objc_const: 0x1178
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x30
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_ivar: 0x148
   __DATA.__data: 0x20774
   __DATA.__bss: 0x338
   __DATA.__common: 0x870

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 800628B4-FFAD-3B65-9B34-7093A00DB2D8
-  Functions: 1354
-  Symbols:   3561
-  CStrings:  2123
+  UUID: A89451F0-29A3-3F85-8C07-10AFBE28E129
+  Functions: 1364
+  Symbols:   3583
+  CStrings:  2131
 
Symbols:
+ -[_MDMutablePlistBytes initWithCapacity:owner:]
+ -[_MDMutablePlistBytes initWithCapacity:useMalloc:zone:owner:]
+ -[_MDMutablePlistBytes initWithCapacity:useMalloc:zone:owner:].cold.1
+ OBJC_IVAR_$__MDPlistBytes._owner
+ __MDPlistBytesCreateMutableWithOwner
+ __MDStoreOIDArrayCreateMutableCopyWithOwner
+ __MDStoreOIDArrayCreateMutableWithOwner
+ ___block_descriptor_tmp.180
+ ___block_descriptor_tmp.181
+ ___block_descriptor_tmp.183
+ ___block_descriptor_tmp.184
+ ___block_literal_global.113
+ ___block_literal_global.133
+ ___block_literal_global.135
+ ___block_literal_global.187
+ ___block_literal_global.86
+ __mach_vm_allocate_with_owner
+ __mach_vm_allocate_with_owner.cold.1
+ __mach_vm_deallocate
+ _fd_copyfile_change_guard_and_update_assertion
+ _fd_copyfile_change_guard_and_update_assertion.cold.1
+ _fd_copyfile_no_fallback
+ _mach_make_memory_entry_64
+ _mach_memory_entry_ownership
+ _mach_port_deallocate
+ _mach_vm_deallocate
+ _mach_vm_map
+ _objc_msgSend$initWithCapacity:owner:
+ _objc_msgSend$initWithCapacity:useMalloc:zone:owner:
- -[_MDMutablePlistBytes initWithCapacity:useMalloc:zone:].cold.1
- ___block_descriptor_tmp.186
- ___block_descriptor_tmp.188
- ___block_descriptor_tmp.189
- ___block_descriptor_tmp.190
- ___block_literal_global.108
- ___block_literal_global.128
- ___block_literal_global.130
- ___block_literal_global.192
- ___block_literal_global.85
- _fd_copyfile.cold.1
CStrings:
+ "%s: mach_make_memory_entry_64 returned partial allocation: requested %llu, got %llu"
+ "%s:%u: failed assertion '%s' %s copy file with fallback=false but cloning disabled: %s(parent:%d) %s(parent:%d) fb:%d cl:%d"
+ "/Library/Caches/com.apple.xbs/958D8764-684B-4CCC-9F3C-3D6F59306129/TemporaryDirectory.jiKZyg/Sources/SpotlightCore/spotlight/MetadataUtilities/MDPathFilter.m"
+ "/Library/Caches/com.apple.xbs/958D8764-684B-4CCC-9F3C-3D6F59306129/TemporaryDirectory.jiKZyg/Sources/SpotlightCore/spotlight/MetadataUtilities/MDPathFilterGenerator.m"
+ "/Library/Caches/com.apple.xbs/958D8764-684B-4CCC-9F3C-3D6F59306129/TemporaryDirectory.jiKZyg/Sources/SpotlightCore/spotlight/MetadataUtilities/_MDPlistBytes.m"
+ "@28@0:8Q16I24"
+ "@40@0:8Q16B24^{_malloc_zone_t=^v^v^?^?^?^?^?^?^?*^?^?^{malloc_introspection_t}I^?^?^?^?^?^?^?^?^?^?^?}28I36"
+ "PlistBytes initWithCapacity memory allocation err:%d kr:%s"
+ "_mach_vm_allocate_with_owner"
+ "_owner"
+ "initWithCapacity:owner:"
+ "initWithCapacity:useMalloc:zone:owner:"
+ "v16@?0^{__MDStoreOIDArray={__CFRuntimeBase=QAQ}Q@?IIb1b1b1I^q}8"
- "/Library/Caches/com.apple.xbs/728B2065-5898-40CC-9EA6-A65614EEDB88/TemporaryDirectory.WUjkFH/Sources/SpotlightCore/spotlight/MetadataUtilities/MDPathFilter.m"
- "/Library/Caches/com.apple.xbs/728B2065-5898-40CC-9EA6-A65614EEDB88/TemporaryDirectory.WUjkFH/Sources/SpotlightCore/spotlight/MetadataUtilities/MDPathFilterGenerator.m"
- "/Library/Caches/com.apple.xbs/728B2065-5898-40CC-9EA6-A65614EEDB88/TemporaryDirectory.WUjkFH/Sources/SpotlightCore/spotlight/MetadataUtilities/_MDPlistBytes.m"
- "PlistBytes initWithCapacity mmap err:%d kr:%d"
- "v16@?0^{__MDStoreOIDArray={__CFRuntimeBase=QAQ}Q@?IIb1b1b1^q}8"

```
