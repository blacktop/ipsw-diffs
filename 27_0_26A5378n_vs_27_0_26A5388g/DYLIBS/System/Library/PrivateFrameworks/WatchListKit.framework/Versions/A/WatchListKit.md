## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Versions/A/WatchListKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`

```diff

-952.0.0.0.0
-  __TEXT.__text: 0x650c8
+952.0.1.0.0
+  __TEXT.__text: 0x650e8
   __TEXT.__objc_methlist: 0x6d14
   __TEXT.__const: 0x19c
   __TEXT.__cstring: 0x7506
   __TEXT.__oslogstring: 0x5a21
   __TEXT.__gcc_except_tab: 0xd30
-  __TEXT.__unwind_info: 0x1c10
+  __TEXT.__unwind_info: 0x1c08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1950
+  __AUTH.__objc_data: 0x17c0
   __DATA.__objc_ivar: 0xa14
   __DATA.__data: 0x618
   __DATA.__bss: 0xe8
-  __DATA_DIRTY.__objc_data: 0x1b80
+  __DATA_DIRTY.__objc_data: 0x1d10
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x400
   __DATA_DIRTY.__common: 0x5

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2738
-  Symbols:   6645
+  Functions: 2737
+  Symbols:   6646
   CStrings:  1822
 
Symbols:
+ _dispatch_block_create_with_qos_class
Functions:
~ +[WLKAppLibrary defaultAppLibrary] : 68 -> 120
- +[WLKPostPlayAutoPlayManager defaultManager].cold.1
```
