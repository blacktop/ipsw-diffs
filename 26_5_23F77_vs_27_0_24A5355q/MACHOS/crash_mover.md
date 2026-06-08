## crash_mover

> `/usr/libexec/crash_mover`

```diff

-1050.0.0.0.0
-  __TEXT.__text: 0x203c
-  __TEXT.__auth_stubs: 0x550
+1052.0.0.0.0
+  __TEXT.__text: 0x1f00
+  __TEXT.__auth_stubs: 0x540
   __TEXT.__objc_stubs: 0x4a0
   __TEXT.__const: 0x193
   __TEXT.__gcc_except_tab: 0x34

   __TEXT.__cstring: 0x2d8
   __TEXT.__objc_methname: 0x35c
   __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x138
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__got: 0xa8
   __DATA.__objc_selrefs: 0x128
   __DATA.__data: 0x5
   __DATA.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A688F1CD-71CF-351C-8190-05EF2EDEE83A
-  Functions: 29
-  Symbols:   115
+  UUID: 22A78DE0-C596-305D-8C34-1904222615DA
+  Functions: 27
+  Symbols:   114
   CStrings:  115
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x25
+ _objc_retain_x1
+ _objc_retain_x2
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x27

```
