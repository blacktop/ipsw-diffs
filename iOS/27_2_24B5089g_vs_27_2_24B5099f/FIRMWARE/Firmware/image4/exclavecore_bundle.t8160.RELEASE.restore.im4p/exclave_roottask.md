## exclave_roottask

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_roottask`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA.__data`
- `__DATA.__shared_cache`
- `__DATA.__mod_init_func`
- `__DATA.__auth_ptr`
- `__DATA.__const`
- `__DATA.__got`
- `__DATA.__thread_vars`

```diff

-1490.40.25.0.0
-  __TEXT.__text: 0x4eabdc
+1490.40.28.0.0
+  __TEXT.__text: 0x4eadd0
   __TEXT.__lcxx_override: 0xd0
   __TEXT.__const: 0xf28a0
-  __TEXT.__cstring: 0x3d90c
+  __TEXT.__cstring: 0x3d93c
   __TEXT.__swift5_typeref: 0xd07c
   __TEXT.__swift5_capture: 0x155c
   __TEXT.__swift5_entry: 0x8

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x80
-  __TEXT.__eh_frame: 0x22254
+  __TEXT.__eh_frame: 0x222c4
   __DATA.__data: 0xcf70
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58

   __PDATA.__shared_cache: 0x0
   Functions: 841
   Symbols:   29
-  CStrings:  6110
+  CStrings:  6111
 
CStrings:
+ "Builtin.Borrow is not supported in runtime type lookup"
+ "Initialized count must be in 0 ... unsafeUninitializedCapacity."
- "Initialized count set to greater than specified capacity."
```
