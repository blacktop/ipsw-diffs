## libRPAC.dylib

> `/usr/lib/libRPAC.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__AUTH_CONST.__interpose`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 106.0.0.0.0
-  __TEXT.__text: 0x92b08
+  __TEXT.__text: 0x92b18
   __TEXT.__auth_stubs: 0xb30
   __TEXT.__objc_stubs: 0x1a0
   __TEXT.__init_offsets: 0x4
Functions:
~ _lockLockInDispatchLockMap : 16 -> 20
~ _unlockLockInDispatchLockMap : 16 -> 20
~ _lockLockInNSCondtionLockMap : 16 -> 20
~ _unlockLockInNSConditionLockMap : 16 -> 20
```
