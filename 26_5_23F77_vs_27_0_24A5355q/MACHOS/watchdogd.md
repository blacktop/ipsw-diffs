## watchdogd

> `/usr/libexec/watchdogd`

```diff

 333.0.0.0.0
-  __TEXT.__text: 0xe120
-  __TEXT.__auth_stubs: 0xff0
+  __TEXT.__text: 0xdcd8
+  __TEXT.__auth_stubs: 0x1030
   __TEXT.__objc_stubs: 0x1020
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x574b
+  __TEXT.__cstring: 0x574e
   __TEXT.__oslogstring: 0x2a1
   __TEXT.__gcc_except_tab: 0x74
-  __TEXT.__objc_classname: 0x15
   __TEXT.__objc_methname: 0xbb3
+  __TEXT.__objc_classname: 0x11
   __TEXT.__objc_methtype: 0xa0
-  __TEXT.__unwind_info: 0x318
-  __DATA_CONST.__auth_got: 0x808
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__auth_ptr: 0x38
+  __TEXT.__unwind_info: 0x308
   __DATA_CONST.__const: 0x8f0
   __DATA_CONST.__cfstring: 0x9c0
   __DATA_CONST.__objc_classlist: 0x8

   __DATA_CONST.__objc_intobj: 0x378
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0x828
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__auth_ptr: 0x38
   __DATA.__objc_const: 0x1c0
   __DATA.__objc_selrefs: 0x418
   __DATA.__objc_ivar: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: B55C89FD-F480-3B24-BA0F-36672DAC43DB
-  Functions: 237
-  Symbols:   324
+  UUID: 6997D107-1BBA-3051-B77E-77C51B63A540
+  Functions: 235
+  Symbols:   328
   CStrings:  828
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28

```
