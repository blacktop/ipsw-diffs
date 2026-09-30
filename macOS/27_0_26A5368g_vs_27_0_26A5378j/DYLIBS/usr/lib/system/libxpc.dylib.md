## libxpc.dylib

> `/usr/lib/system/libxpc.dylib`

```diff

-  __TEXT.__text: 0x464e8
+  __TEXT.__text: 0x464b4
   __TEXT.__lazy_helpers: 0x1a4
   __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0x638

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__got: 0x1e8
   __AUTH_CONST.__const: 0x2698
   __AUTH_CONST.__objc_const: 0x2338
   __AUTH_CONST.__lazy_load_got: 0x28

   __AUTH.__objc_data: 0x50
   __DATA.__data: 0xbb0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0xaf0
-  __DATA_DIRTY.__bss: 0x120
+  __DATA_DIRTY.__bss: 0x118
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__dof_libxpc : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_nlclslist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__lazy_load_got : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ __xpc_bundle_resolve_executable : 620 -> 624
~ __xpc_uint64_hash : 84 -> 72
~ __xpc_uuid_hash : 48 -> 40
~ __xpc_date_hash : 48 -> 40
~ __xpc_double_hash : 48 -> 40
~ __xpc_int64_hash : 84 -> 72
~ __xpc_pointer_hash : 48 -> 40

```
