## gpucapture

> `/usr/bin/gpucapture`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2027.0.39.0.0
-  __TEXT.__text: 0x2a1ac
+2027.0.44.0.0
+  __TEXT.__text: 0x2a358
   __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_stubs: 0x29a0
-  __TEXT.__objc_methlist: 0x2fbc
+  __TEXT.__objc_stubs: 0x29c0
+  __TEXT.__objc_methlist: 0x2fd4
   __TEXT.__const: 0x140
   __TEXT.__oslogstring: 0xde1
-  __TEXT.__cstring: 0x3f4e
-  __TEXT.__objc_methname: 0x4bed
+  __TEXT.__cstring: 0x3f6b
+  __TEXT.__objc_methname: 0x4c29
   __TEXT.__objc_classname: 0x8d6
   __TEXT.__objc_methtype: 0x117c
-  __TEXT.__unwind_info: 0xba8
-  __DATA_CONST.__const: 0xb18
-  __DATA_CONST.__cfstring: 0x24e0
+  __TEXT.__unwind_info: 0xbb0
+  __DATA_CONST.__const: 0xb48
+  __DATA_CONST.__cfstring: 0x2500
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x508
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x68d0
-  __DATA.__objc_selrefs: 0x1200
-  __DATA.__objc_ivar: 0x3fc
+  __DATA.__objc_const: 0x6900
+  __DATA.__objc_selrefs: 0x1210
+  __DATA.__objc_ivar: 0x400
   __DATA.__objc_data: 0x1770
   __DATA.__data: 0x1690
   __DATA.__common: 0x3000318

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1102
+  Functions: 1106
   Symbols:   217
-  CStrings:  1604
+  CStrings:  1608
 
CStrings:
+ "2027.0.44"
+ "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu accessLevel=%llu>"
+ "TQ,N,V_accessLevel"
+ "_accessLevel"
+ "accessLevel"
+ "setAccessLevel:"
- "2027.0.39"
- "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu>"
```
