## fskitd

> `usr/libexec/fskitd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-737.160.1.0.2
-  __TEXT.__text: 0x41078
+737.160.1.701.1
+  __TEXT.__text: 0x41188
   __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_stubs: 0x40c0
   __TEXT.__objc_methlist: 0x1b3c
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0x1e18
-  __TEXT.__cstring: 0x2a8f
-  __TEXT.__oslogstring: 0x3474
+  __TEXT.__cstring: 0x2aa7
+  __TEXT.__oslogstring: 0x34b0
   __TEXT.__objc_classname: 0x1f6
   __TEXT.__objc_methname: 0x50ce
   __TEXT.__objc_methtype: 0x1da5

   - /usr/lib/libutil.dylib
   Functions: 1242
   Symbols:   245
-  CStrings:  1695
+  CStrings:  1697
 
Functions:
~ sub_100010130 : 2296 -> 2568
CStrings:
+ "%s: caller euid %u not authorized to mount on %s (owner %u)"
+ "-[fskitdMounter mount:]"
```
