## abmlite

> `/usr/bin/abmlite`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1576.0.0.0.0
-  __TEXT.__text: 0x1c8d8
-  __TEXT.__auth_stubs: 0x8c0
+1580.0.0.0.0
+  __TEXT.__text: 0x1cd44
+  __TEXT.__auth_stubs: 0x8f0
   __TEXT.__objc_stubs: 0x560
   __TEXT.__init_offsets: 0x10
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x530
-  __TEXT.__gcc_except_tab: 0x20f0
-  __TEXT.__cstring: 0xa59
+  __TEXT.__gcc_except_tab: 0x214c
+  __TEXT.__cstring: 0xa73
   __TEXT.__oslogstring: 0xc6
   __TEXT.__objc_classname: 0xc
   __TEXT.__objc_methtype: 0x14
   __TEXT.__objc_methname: 0x31e
-  __TEXT.__unwind_info: 0x568
+  __TEXT.__unwind_info: 0x578
   __DATA_CONST.__const: 0x540
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__auth_got: 0x490
+  __DATA_CONST.__got: 0x2f0
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x158
   __DATA.__objc_data: 0x50

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libedit.3.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 175
-  Symbols:   360
-  CStrings:  163
+  Functions: 176
+  Symbols:   361
+  CStrings:  165
 
Symbols:
+ __ZN3abm5trace33kPCIDriverSnapshotDirectorySuffixE
CStrings:
+ "PCI = "
+ "Watchdog timed out"
```
