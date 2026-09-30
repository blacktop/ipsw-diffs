## restorecameraispd

> `/usr/libexec/restorecameraispd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`

```diff

-20.57.3.0.0
-  __TEXT.__text: 0x1ce9c
+20.62.0.0.0
+  __TEXT.__text: 0x1cf84
   __TEXT.__auth_stubs: 0xf90
   __TEXT.__objc_stubs: 0x4a0
   __TEXT.__const: 0x16d0
-  __TEXT.__cstring: 0x3203
+  __TEXT.__cstring: 0x3259
   __TEXT.__gcc_except_tab: 0x4b8
-  __TEXT.__oslogstring: 0x2280
+  __TEXT.__oslogstring: 0x22c4
   __TEXT.__objc_methname: 0x32c
   __TEXT.__unwind_info: 0x570
   __DATA_CONST.__const: 0x80b0

   __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_selrefs: 0x128
-  __DATA.__data: 0x3aec00
+  __DATA.__data: 0x3bdc00
   __DATA.__common: 0x7
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libz.1.dylib
   Functions: 421
   Symbols:   301
-  CStrings:  627
+  CStrings:  630
 
Functions:
~ sub_100000db0 : 1192 -> 1276
~ sub_100013a48 -> sub_100013a9c : 264 -> 300
~ sub_100014630 -> sub_1000146a8 : 2188 -> 2300
CStrings:
+ "/usr/local/share/firmware/isp/0227_01XX.dat"
+ "/usr/local/share/firmware/isp/2226_01XX.dat"
+ "20.62"
+ "ISP still in use by another session; keeping shared interface open\n"
- "20.57.3"
```
