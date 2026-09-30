## airportd

> `/usr/libexec/airportd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-19175.62.0.0.0
-  __TEXT.__text: 0xdf944
+19175.65.0.0.0
+  __TEXT.__text: 0xdf8d4
   __TEXT.__auth_stubs: 0x1fe0
-  __TEXT.__objc_stubs: 0x10320
+  __TEXT.__objc_stubs: 0x10300
   __TEXT.__objc_methlist: 0x5680
   __TEXT.__const: 0xb28
-  __TEXT.__objc_methname: 0x14aac
+  __TEXT.__objc_methname: 0x14a91
   __TEXT.__objc_classname: 0x3be
   __TEXT.__objc_methtype: 0x3400
   __TEXT.__gcc_except_tab: 0x2114

   __DATA_CONST.__got: 0x940
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0x6938
-  __DATA.__objc_selrefs: 0x4950
+  __DATA.__objc_selrefs: 0x4948
   __DATA.__objc_ivar: 0x728
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x424

   - /usr/lib/libz.1.dylib
   Functions: 2825
   Symbols:   831
-  CStrings:  7561
+  CStrings:  7560
 
Functions:
~ sub_100009184 : 3912 -> 3900
~ sub_100091004 -> sub_100090ff8 : 284 -> 540
~ sub_100091120 -> sub_100091214 : 440 -> 16
~ sub_1000912d8 -> sub_100091224 : 16 -> 156
~ sub_1000ce6ec -> sub_1000ce6c4 : 184 -> 112
CStrings:
+ "-[CWXPCInterfaceContext __scheduleBestConnectedScanWithInterval:]_block_invoke_4"
- "-[CWXPCInterfaceContext __scheduleBestConnectedScanWithInterval:]_block_invoke_5"
- "isUnconfiguredBaseStation:"
```
