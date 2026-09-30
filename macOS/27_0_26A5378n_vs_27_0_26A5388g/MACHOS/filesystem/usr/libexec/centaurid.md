## centaurid

> `/usr/libexec/centaurid`

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

-124.0.0.0.1
-  __TEXT.__text: 0x348c8
+127.0.0.0.0
+  __TEXT.__text: 0x349ac
   __TEXT.__auth_stubs: 0x930
   __TEXT.__objc_stubs: 0x3580
   __TEXT.__objc_methlist: 0x115c
   __TEXT.__const: 0x120
   __TEXT.__gcc_except_tab: 0x1604
-  __TEXT.__cstring: 0x19b9b
-  __TEXT.__oslogstring: 0x5f41
+  __TEXT.__cstring: 0x19bad
+  __TEXT.__oslogstring: 0x5f65
   __TEXT.__objc_methname: 0x33b5
   __TEXT.__objc_classname: 0x190
   __TEXT.__objc_methtype: 0x99c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 655
+  Functions: 656
   Symbols:   222
-  CStrings:  3522
+  CStrings:  3524
 
CStrings:
+ "%{public}@::%{public}@: version: %s"
+ "AppleCentauri-127"
```
