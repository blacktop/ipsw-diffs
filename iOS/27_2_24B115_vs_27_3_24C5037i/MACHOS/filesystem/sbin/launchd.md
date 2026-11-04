## launchd

> `/sbin/launchd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__dof_launchd`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__os_assumes_log`

```diff

-3298.42.1.0.0
-  __TEXT.__text: 0x5abac
-  __TEXT.__auth_stubs: 0x2720
+3298.60.14.0.0
+  __TEXT.__text: 0x59934
+  __TEXT.__auth_stubs: 0x26a0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x20c
-  __TEXT.__const: 0x500
+  __TEXT.__const: 0x4f0
   __TEXT.__launchd: 0x1
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_typeref: 0x5e

   __TEXT.__swift5_fieldmd: 0x60
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__cstring: 0x16986
+  __TEXT.__cstring: 0x16870
   __TEXT.__swift5_capture: 0x14
   __TEXT.__objc_methtype: 0xf
   __TEXT.__objc_classname: 0x212
   __TEXT.__objc_methname: 0x1c
-  __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__oslogstring: 0xd5
   __TEXT.__config: 0x2a50
   __TEXT.__dof_launchd: 0x67c
-  __TEXT.__unwind_info: 0x1778
+  __TEXT.__unwind_info: 0x16f0
   __TEXT.__eh_frame: 0x210
   __DATA_CONST.__const: 0x59e8
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__auth_got: 0x1398
-  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__auth_got: 0x1350
+  __DATA_CONST.__got: 0x208
   __DATA_CONST.__auth_ptr: 0xa0
   __DATA.__objc_const: 0xdf0
   __DATA.__objc_selrefs: 0x8
   __DATA.__objc_data: 0x6e0
-  __DATA.__data: 0xac0
+  __DATA.__data: 0xab8
   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x7f8
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  Functions: 1484
-  Symbols:   712
-  CStrings:  2834
+  Functions: 1468
+  Symbols:   702
+  CStrings:  2818
 
Symbols:
- __Unwind_Resume
- __ZSt9terminatev
- ___assert_rtn
- ___cxa_begin_catch
- ___gxx_personality_v0
- ___mac_syscall
- __os_log_default
- __os_log_impl
- _malloc_type_free
- _os_log_type_enabled
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sat Oct 24 01:33:14 PDT 2026; root:libxpc_executables-3298.60.14~14/launchd/RELEASE_ARM64E"
+ "Darwin Bootstrapper Version 7.0.0: Sat Oct 24 01:33:14 PDT 2026; root:libxpc_executables-3298.60.14~14/launchd/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Wed Oct  7 23:41:26 PDT 2026; root:libxpc_executables-3298.42.1~13/launchd/RELEASE_ARM64E"
- "Darwin Bootstrapper Version 7.0.0: Wed Oct  7 23:41:26 PDT 2026; root:libxpc_executables-3298.42.1~13/launchd/RELEASE_ARM64E"
- "EndpointSecurity"
- "Failed to pack event for downcall using ES syscall %d"
- "Failed to submit event using ES syscall %d: %d %s"
- "Invalid enum value on pack: %d\n"
- "Is this process entitled properly for submitting events to EndpointSecurity?"
- "Maybe.h"
- "PackedDataBuffer.cpp"
- "Queue.h"
- "SentinelA"
- "ess bootstrap_look_up: audit_token_for_pid(%d) → %d for service %s, JOB arm"
- "ess bootstrap_look_up: endpoint owner == NULL for service %s"
- "exists()"
- "pushBackMulti"
- "size >= sizeof(uint64_t)"
- "src != (A *)data_"
- "writeBytes"
```
