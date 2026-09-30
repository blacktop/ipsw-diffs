## spctl

> `/usr/sbin/spctl`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_security_`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dupclass`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-823.0.3.0.0
-  __TEXT.__text: 0xc4fc
+823.1.1.0.0
+  __TEXT.__text: 0xc64c
   __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_stubs: 0x1020
+  __TEXT.__objc_stubs: 0x10a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x8c8
+  __TEXT.__objc_methlist: 0x8e8
   __TEXT.__const: 0x518
-  __TEXT.__cstring: 0x1a2c
+  __TEXT.__cstring: 0x1ac6
   __TEXT.__oslogstring: 0x8f3
   __TEXT.__objc_classname: 0x107
-  __TEXT.__objc_methname: 0x19e5
-  __TEXT.__objc_methtype: 0x8e9
+  __TEXT.__objc_methname: 0x1a5d
+  __TEXT.__objc_methtype: 0x8f5
   __TEXT.__gcc_except_tab: 0x5fc
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__dof_security_: 0x28e
-  __TEXT.__unwind_info: 0x508
-  __DATA_CONST.__const: 0xc68
+  __TEXT.__unwind_info: 0x518
+  __DATA_CONST.__const: 0xc88
   __DATA_CONST.__cfstring: 0xda0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__auth_got: 0x538
   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0xf20
-  __DATA.__objc_selrefs: 0x660
+  __DATA.__objc_const: 0xf28
+  __DATA.__objc_selrefs: 0x680
   __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x188

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 359
+  Functions: 363
   Symbols:   262
-  CStrings:  688
+  CStrings:  695
 
CStrings:
+ "@24@0:8^@16"
+ "Removed %lld unmounted policy scan cache entries.\n"
+ "System Policy Basic Usage:\n       spctl --assess [--type type] [-v] path ... # assessment\n       spctl --status # assessment system status\n       spctl --global-disable | --disable-status\n       spctl --purge # purge unmounted policy scan cache entries\n\n"
+ "failed to purge policy scan cache: %s"
+ "localizedDescription"
+ "longLongValue"
+ "purgeUnmountedPolicyScanCacheEntries:"
+ "purgeUnmountedPolicyScanCacheEntriesWithReply:"
- "System Policy Basic Usage:\n       spctl --assess [--type type] [-v] path ... # assessment\n       spctl --status # assessment system status\n       spctl --global-disable | --disable-status\n\n"
```
