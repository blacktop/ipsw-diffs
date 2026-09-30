## libBasebandCommandDriversARI.dylib

> `/usr/lib/libBasebandCommandDriversARI.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`

```diff

-1576.0.0.0.0
-  __TEXT.__text: 0xc14f4
+1580.0.0.0.0
+  __TEXT.__text: 0xc1520
   __TEXT.__init_offsets: 0x14
   __TEXT.__const: 0x8580
-  __TEXT.__cstring: 0x35ef
+  __TEXT.__cstring: 0x35f8
   __TEXT.__gcc_except_tab: 0xe288
   __TEXT.__oslogstring: 0x26ef
   __TEXT.__unwind_info: 0x39f8

   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x218
+  __DATA.__data: 0x220
   __DATA.__common: 0x40
   __DATA_DIRTY.__data: 0xf0
   __DATA_DIRTY.__bss: 0x110

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2232
-  Symbols:   4721
-  CStrings:  863
+  Symbols:   4722
+  CStrings:  864
 
Symbols:
+ __ZN3abm5trace33kPCIDriverSnapshotDirectorySuffixE
Functions:
~ __ZN3abm5trace11isSupportedENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 712 -> 756
CStrings:
+ "-pci-bin"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1580"
- "AppleBasebandManager-AppleBasebandServices_Manager-1576"
```
