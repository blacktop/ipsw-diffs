## libBasebandCommandDriversQMI.dylib

> `/usr/lib/libBasebandCommandDriversQMI.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`

```diff

-1576.0.0.0.0
-  __TEXT.__text: 0x104fd0
+1580.0.0.0.0
+  __TEXT.__text: 0x104ffc
   __TEXT.__init_offsets: 0x14
   __TEXT.__const: 0x7a30
   __TEXT.__gcc_except_tab: 0x13818
-  __TEXT.__cstring: 0x3f86
+  __TEXT.__cstring: 0x3f8f
   __TEXT.__oslogstring: 0x248c
   __TEXT.__unwind_info: 0x6f10
   __TEXT.__eh_frame: 0x138

   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x1f8
+  __DATA.__data: 0x200
   __DATA_DIRTY.__data: 0xa0
   __DATA_DIRTY.__common: 0x40
   __DATA_DIRTY.__bss: 0x160

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 5158
-  Symbols:   7558
-  CStrings:  1044
+  Symbols:   7559
+  CStrings:  1045
 
Symbols:
+ __ZN3abm5trace33kPCIDriverSnapshotDirectorySuffixE
Functions:
~ __ZN3abm5trace11isSupportedENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 712 -> 756
CStrings:
+ "-pci-bin"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1580"
- "AppleBasebandManager-AppleBasebandServices_Manager-1576"
```
