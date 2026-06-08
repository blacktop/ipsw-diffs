## libdispatch.dylib

> `/usr/lib/system/introspection/libdispatch.dylib`

```diff

-1542.100.32.0.0
-  __TEXT.__text: 0x42d88
-  __TEXT.__auth_stubs: 0xd10
+1601.0.0.0.1
+  __TEXT.__text: 0x432f4
   __TEXT.__objc_methlist: 0x684
   __TEXT.__const: 0x830
-  __TEXT.__cstring: 0x646c
-  __TEXT.__unwind_info: 0xe60
+  __TEXT.__cstring: 0x6483
+  __TEXT.__unwind_info: 0xe88
   __TEXT.__eh_frame: 0xb8
+  __TEXT.__objc_stubs: 0x1e0
+  __TEXT.__auth_stubs: 0xd20
   __TEXT.__objc_classname: 0x499
   __TEXT.__objc_methname: 0x2b9
   __TEXT.__objc_methtype: 0x118
-  __TEXT.__objc_stubs: 0x1e0
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0xc78
+  __DATA_CONST.__const: 0xcc0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_nlclslist: 0xb8
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x698
+  __DATA_CONST.__got: 0xe8
   __AUTH_CONST.__const: 0x10ce8
   __AUTH_CONST.__objc_const: 0x1f00
+  __AUTH_CONST.__auth_got: 0x6a0
   __AUTH.__data: 0x70
   __DATA.__data: 0x11b8
   __DATA.__crash_info: 0x148

   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0xdf8
   __DATA_DIRTY.__data: 0xc50
-  __DATA_DIRTY.__common: 0x188
+  __DATA_DIRTY.__common: 0x190
   __DATA_DIRTY.__bss: 0x6b8
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: F04C45D1-3A3A-34A6-BB69-77C25DA1382A
-  Functions: 1474
-  Symbols:   2594
-  CStrings:  642
+  UUID: C1D55053-7A75-33B1-B356-7B0D3F608BCC
+  Functions: 1478
+  Symbols:   2602
+  CStrings:  643
 
Symbols:
+ __voucher_get_current_persona_id
+ __voucher_launch_persona_id
+ __voucher_launch_persona_id_init
+ __voucher_launch_persona_id_pred
+ _dispatch_thread_override_self_with_base
+ _dispatch_thread_reset_override_self
+ _kpersona_pidinfo
- _OUTLINED_FUNCTION_34
- _OUTLINED_FUNCTION_35
CStrings:
+ "BUG in libdispatch: %s - %lu - 0x%llx"
+ "com.apple.coremedia"
+ "target = %s[%p], ident = 0x%llx, mask = 0x%x, pending_data = 0x%llx, registered = %d, armed = %d, %s%s%s"
- "BUG in libdispatch: %s - %lu - 0x%lx"
- "target = %s[%p], ident = 0x%x, mask = 0x%x, pending_data = 0x%llx, registered = %d, armed = %d, %s%s%s"

```
