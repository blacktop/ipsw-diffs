## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-720.2.1.0.0
-  __TEXT.__text: 0xbd428
+720.3.1.0.0
+  __TEXT.__text: 0xbd500
   __TEXT.__auth_stubs: 0x1a60
   __TEXT.__objc_stubs: 0xd640
   __TEXT.__objc_methlist: 0x66dc
   __TEXT.__const: 0x3b8
-  __TEXT.__oslogstring: 0x1192f
+  __TEXT.__oslogstring: 0x11980
   __TEXT.__cstring: 0x14a5b
   __TEXT.__objc_classname: 0xa69
   __TEXT.__objc_methname: 0x13da2

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3311
+  Functions: 3312
   Symbols:   816
-  CStrings:  6608
+  CStrings:  6609
 
Functions:
~ sub_1000a3368 : 1488 -> 1568
+ sub_1000be968
CStrings:
+ " [ERROR] %{public}s:%d sample buffer missing color space for streamID=%{public}@"
```
