## libBasebandCommandDriversMIPC.dylib

> `/usr/lib/libBasebandCommandDriversMIPC.dylib`

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
-  __TEXT.__text: 0x879a8
+1580.0.0.0.0
+  __TEXT.__text: 0x879d4
   __TEXT.__init_offsets: 0x24
   __TEXT.__const: 0xa3f0
   __TEXT.__gcc_except_tab: 0x7940
-  __TEXT.__cstring: 0x1aff
+  __TEXT.__cstring: 0x1b08
   __TEXT.__oslogstring: 0x1f47
   __TEXT.__unwind_info: 0x22d8
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x298
+  __DATA.__data: 0x2a0
   __DATA.__common: 0x40
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x230

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1513
-  Symbols:   3232
-  CStrings:  560
+  Symbols:   3233
+  CStrings:  561
 
Symbols:
+ __ZN3abm5trace33kPCIDriverSnapshotDirectorySuffixE
Functions:
~ __ZN3abm5trace11isSupportedENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 712 -> 756
CStrings:
+ "-pci-bin"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1580"
- "AppleBasebandManager-AppleBasebandServices_Manager-1576"
```
