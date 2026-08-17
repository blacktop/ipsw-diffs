## apfs_condenser

> `System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_condenser`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.0.4
-  __TEXT.__text: 0x4c930
+2811.160.7.701.3
+  __TEXT.__text: 0x4c9b0
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__cstring: 0xfa58
+  __TEXT.__cstring: 0xfa6c
   __TEXT.__const: 0x240
   __TEXT.__unwind_info: 0x818
   __DATA_CONST.__auth_got: 0x410

   - /usr/lib/libutil.dylib
   Functions: 670
   Symbols:   144
-  CStrings:  1286
+  CStrings:  1287
 
Functions:
~ sub_100000bb4 : 1248 -> 1268
~ sub_10000cbdc -> sub_10000cbf0 : 592 -> 640
~ sub_100017920 -> sub_100017964 : 488 -> 516
~ sub_1000289e0 -> sub_100028a40 : 488 -> 524
~ sub_10002efdc -> sub_10002f060 : 292 -> 288
CStrings:
+ "2811.160.7.701.3"
+ "apfs_sanity_check"
- "2811.160.7.0.4"
```
