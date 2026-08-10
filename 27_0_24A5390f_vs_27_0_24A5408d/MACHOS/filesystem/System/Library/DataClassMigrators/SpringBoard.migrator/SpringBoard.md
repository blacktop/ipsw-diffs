## SpringBoard

> `/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-4630.1.102.0.0
-  __TEXT.__text: 0xe3f8
-  __TEXT.__auth_stubs: 0x5d0
+4636.102.1.0.0
+  __TEXT.__text: 0xe4cc
+  __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_stubs: 0x19a0
   __TEXT.__objc_methlist: 0x64c
-  __TEXT.__const: 0x78
+  __TEXT.__const: 0x80
   __TEXT.__cstring: 0x18bb
   __TEXT.__objc_methname: 0x19e1
-  __TEXT.__oslogstring: 0x130b
+  __TEXT.__oslogstring: 0x139e
   __TEXT.__objc_classname: 0x11a
   __TEXT.__objc_methtype: 0x329
-  __TEXT.__gcc_except_tab: 0x140
+  __TEXT.__gcc_except_tab: 0x14c
   __TEXT.__unwind_info: 0x270
   __DATA_CONST.__const: 0x15f8
   __DATA_CONST.__cfstring: 0xf20

   __DATA_CONST.__objc_arraydata: 0x120
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0x228
   __DATA.__objc_const: 0xd28
   __DATA.__objc_selrefs: 0x7b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 641
-  Symbols:   378
-  CStrings:  691
+  Functions: 642
+  Symbols:   379
+  CStrings:  692
 
Symbols:
+ __os_log_fault_impl
CStrings:
+ "[performPosterBoardMigration] posterboard migration timed out after %{public}.0f seconds; not marking complete"
+ "[performPosterBoardMigration] tint color migration did not complete (error: %{public}@, timedOut: %{BOOL}u); will retry next launch"
- "[performPosterBoardMigration] tint color migration failed; migration error prevented completion"
```
