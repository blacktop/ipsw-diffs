## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
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
-  __TEXT.__text: 0x66b84
+952.0.1.0.0
+  __TEXT.__text: 0x66ba0
   __TEXT.__objc_methlist: 0x7174
   __TEXT.__const: 0x1a4
   __TEXT.__cstring: 0x7dfa

   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x19a0
+  __AUTH.__objc_data: 0x1810
   __DATA.__objc_ivar: 0xa4c
   __DATA.__data: 0x7a0
   __DATA.__bss: 0xf8
-  __DATA_DIRTY.__objc_data: 0x1c20
+  __DATA_DIRTY.__objc_data: 0x1db0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x450
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2785
-  Symbols:   6888
+  Functions: 2784
+  Symbols:   6889
   CStrings:  1927
 
Symbols:
+ _dispatch_block_create_with_qos_class
Functions:
~ +[WLKAppLibrary defaultAppLibrary] : 68 -> 116
- +[WLKLocationManager defaultLocationManager].cold.1
```
