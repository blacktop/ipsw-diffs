## wifivelocityd

> `/usr/libexec/wifivelocityd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1172.1.0.0.0
-  __TEXT.__text: 0xa3e0c
+  __TEXT.__text: 0xa4ea4
   __TEXT.__auth_stubs: 0x1200
-  __TEXT.__objc_stubs: 0xd320
-  __TEXT.__objc_methlist: 0x53d4
+  __TEXT.__objc_stubs: 0xd380
+  __TEXT.__objc_methlist: 0x53f4
   __TEXT.__dlopen_cstrs: 0x2c2
   __TEXT.__const: 0x398
   __TEXT.__gcc_except_tab: 0x18c8
-  __TEXT.__objc_methname: 0xdd89
+  __TEXT.__objc_methname: 0xddfe
   __TEXT.__oslogstring: 0xb2c7
-  __TEXT.__cstring: 0xc3c4
+  __TEXT.__cstring: 0xc437
   __TEXT.__objc_classname: 0x832
   __TEXT.__objc_methtype: 0x2405
   __TEXT.__ustring: 0x8c
-  __TEXT.__unwind_info: 0x1e00
+  __TEXT.__unwind_info: 0x1e48
   __DATA_CONST.__auth_got: 0x910
   __DATA_CONST.__got: 0x570
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x2c48
-  __DATA_CONST.__cfstring: 0xb0e0
+  __DATA_CONST.__cfstring: 0xb180
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_intobj: 0xe88
-  __DATA_CONST.__objc_arraydata: 0x2468
+  __DATA_CONST.__objc_arraydata: 0x2478
   __DATA_CONST.__objc_dictobj: 0x14c8
-  __DATA_CONST.__objc_arrayobj: 0x1680
+  __DATA_CONST.__objc_arrayobj: 0x16b0
   __DATA_CONST.__objc_doubleobj: 0x80
-  __DATA.__objc_const: 0x8af0
-  __DATA.__objc_selrefs: 0x3b08
-  __DATA.__objc_ivar: 0x6d0
+  __DATA.__objc_const: 0x8b60
+  __DATA.__objc_selrefs: 0x3b20
+  __DATA.__objc_ivar: 0x6dc
   __DATA.__objc_data: 0x1770
   __DATA.__data: 0x660
   __DATA.__bss: 0x140

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - @rpath/BloodhoundKit.framework/Versions/A/BloodhoundKit
-  Functions: 2458
+  Functions: 2479
   Symbols:   475
-  CStrings:  5289
+  CStrings:  5301
 
CStrings:
+ "-dbg=print_nan_avail"
+ "-nan"
+ "-nan_peers"
+ "Filtered known networks for customer install without MegaWiFi profile\n"
+ "T@\"W5WiFiInterface\",R,&,V_nan"
+ "__startNANPerfLogging"
+ "__startNANQueryTimer"
+ "_nan"
+ "_nanQueryFileHandle"
+ "_nanQueryTimer"
+ "nan"
+ "nan_%@"
```
