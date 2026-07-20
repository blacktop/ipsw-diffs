## mmaintenanced

> `/usr/libexec/mmaintenanced`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-233.0.0.502.1
-  __TEXT.__text: 0x24480
-  __TEXT.__auth_stubs: 0x13c0
+233.0.5.0.0
+  __TEXT.__text: 0x24d84
+  __TEXT.__auth_stubs: 0x13e0
   __TEXT.__objc_stubs: 0x540
-  __TEXT.__init_offsets: 0x8
-  __TEXT.__oslogstring: 0x2d76
-  __TEXT.__const: 0x7f8
-  __TEXT.__cstring: 0x1bbd
-  __TEXT.__gcc_except_tab: 0x864
+  __TEXT.__init_offsets: 0x4
+  __TEXT.__const: 0x7b8
+  __TEXT.__gcc_except_tab: 0x96c
+  __TEXT.__cstring: 0x1bfd
+  __TEXT.__oslogstring: 0x2dc6
   __TEXT.__swift5_typeref: 0xfe
   __TEXT.__swift5_capture: 0x1ec
   __TEXT.__constg_swiftt: 0x44

   __TEXT.__swift5_proto: 0x8
   __TEXT.__objc_methtype: 0x1d
   __TEXT.__objc_methname: 0x352
-  __TEXT.__unwind_info: 0x9d0
+  __TEXT.__unwind_info: 0xa00
   __TEXT.__eh_frame: 0x230
-  __DATA_CONST.__const: 0x1438
+  __DATA_CONST.__const: 0x1458
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x9f0
-  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__auth_got: 0xa00
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__auth_ptr: 0xa0
   __DATA.__objc_selrefs: 0x150
   __DATA.__data: 0x1a8
-  __DATA.__bss: 0x2d0
+  __DATA.__bss: 0x280
   __DATA.__common: 0x64
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 695
+  Functions: 698
   Symbols:   1405
-  CStrings:  478
+  CStrings:  485
 
Symbols:
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/MemoryMaintenance/install/TempContent/Objects/MemoryMaintenance.build/mmaintenanced.build/Objects-normal/arm64e/ecc_api.o
+ _Z21migrate_file_locationRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_16migrate_option_t
+ _Z32setup_environment_for_ecc_daemonv
+ _Z37update_path_ownership_and_permissionsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEjjtb
+ __Z21migrate_file_locationRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_16migrate_option_t
+ __Z29system_supports_ecc_reportingv
+ __Z32setup_environment_for_ecc_daemonv
+ __Z37update_path_ownership_and_permissionsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEjjtb
+ __ZN3ecc9constants5paths13retired_db_v1L9full_pathEv
+ __ZN3ecc9constants5paths13retired_db_v2L9full_pathEv
+ __ZN3ecc9constants5paths16cumulative_db_v2L9full_pathEv
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ __ZNSt3__14__fs10filesystem4pathC2B9fqe220106INS_17basic_string_viewIcNS_11char_traitsIcEEEEvEERKT_NS2_6formatE
+ _getpwnam
+ ecc_api.cpp
- _GLOBAL__sub_I_ecc_logging.cpp
- _Z23validate_file_ownershipRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEjj
- _Z25validate_file_permissionsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEt
- _Z37update_file_ownership_and_permissionsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEjjt
- _Z46move_file_and_update_permissions_and_ownershipRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_ttt
- __Z16is_ecc_supportedv
- __Z23validate_file_ownershipRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEjj
- __Z25validate_file_permissionsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEt
- __Z37update_file_ownership_and_permissionsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEjjt
- __Z46move_file_and_update_permissions_and_ownershipRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_ttt
- __ZN3ecc9constants5paths13retired_db_v1L4pathE
- __ZN3ecc9constants5paths13retired_db_v2L4pathE
- __ZN3ecc9constants5paths16cumulative_db_v2L4pathE
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
- __ZNSt3__14__fs10filesystem4pathC2B9fqe220106INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEvEERKT_NS2_6formatE
- __ZNSt3__1plB9fqe220106IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_SB_
CStrings:
+ "/var/db/mmaintenanced/"
+ "Created database directory at '%s'."
+ "Failed to create directory '%s': %d (%s)"
+ "Failed to migrate database from '%s' to '%s'."
+ "Failed to query data for '%s': (%d) %s"
+ "Failed to update ownership/permissions for '%s'"
+ "Failed to update permisions to %04o and/or user/group ownership to %d/%d for '%s'."
+ "dramecc.db"
+ "memory_errors.db"
+ "mobile"
+ "vm.ecc.enabled"
- "Failed to update permissions to %04o and/or user/group ownership to %d/%d for '%s'."
- "Failed to update permissions to %04o for '%s': %d (%s)"
- "Failed to update user/group ownership to %d/%d for '%s': %d (%s)"
- "dram-ecc"
```
