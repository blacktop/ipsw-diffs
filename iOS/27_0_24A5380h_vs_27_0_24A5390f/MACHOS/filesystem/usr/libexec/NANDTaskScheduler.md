## NANDTaskScheduler

> `/usr/libexec/NANDTaskScheduler`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-847.0.0.0.0
-  __TEXT.__text: 0xf5e8
+849.0.5.0.0
+  __TEXT.__text: 0xf904
   __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_stubs: 0x1600
   __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0x1b0
   __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__cstring: 0x1259
+  __TEXT.__cstring: 0x12b4
   __TEXT.__objc_methname: 0x15fe
-  __TEXT.__oslogstring: 0x2f6f
+  __TEXT.__oslogstring: 0x2fcf
   __TEXT.__objc_classname: 0xed
   __TEXT.__objc_methtype: 0x352
   __TEXT.__unwind_info: 0x310
   __DATA_CONST.__const: 0x690
-  __DATA_CONST.__cfstring: 0xa60
+  __DATA_CONST.__cfstring: 0xa80
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 249
   Symbols:   199
-  CStrings:  749
+  CStrings:  753
 
Functions:
~ sub_10000a354 : 7544 -> 7988
~ sub_10000d95c -> sub_10000db18 : 3044 -> 3072
~ sub_10000e6a8 -> sub_10000e880 : 1228 -> 1552
CStrings:
+ "Failed to deregister bdr throughput tracking: %@"
+ "Failed to register bdr throughput tracking: %@"
+ "INVALID PING RESPONSE - STOPPING"
+ "idlestack.bdr"
```
