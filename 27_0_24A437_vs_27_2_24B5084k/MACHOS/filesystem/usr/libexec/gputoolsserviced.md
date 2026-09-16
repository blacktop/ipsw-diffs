## gputoolsserviced

> `/usr/libexec/gputoolsserviced`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2027.0.37.0.0
-  __TEXT.__text: 0x323dc
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_stubs: 0x55e0
-  __TEXT.__objc_methlist: 0x35fc
+2027.0.44.0.0
+  __TEXT.__text: 0x32900
+  __TEXT.__auth_stubs: 0xf20
+  __TEXT.__objc_stubs: 0x5680
+  __TEXT.__objc_methlist: 0x363c
   __TEXT.__const: 0x4d0
-  __TEXT.__oslogstring: 0x18ec
-  __TEXT.__cstring: 0x4689
-  __TEXT.__objc_methname: 0x7770
+  __TEXT.__oslogstring: 0x1928
+  __TEXT.__cstring: 0x46e2
+  __TEXT.__objc_methname: 0x7829
   __TEXT.__objc_classname: 0x84d
   __TEXT.__objc_methtype: 0x1404
-  __TEXT.__unwind_info: 0xd30
-  __DATA_CONST.__const: 0xb80
-  __DATA_CONST.__cfstring: 0x33c0
+  __TEXT.__unwind_info: 0xd40
+  __DATA_CONST.__const: 0xba8
+  __DATA_CONST.__cfstring: 0x3400
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x7a0
+  __DATA_CONST.__auth_got: 0x798
   __DATA_CONST.__got: 0x288
-  __DATA.__objc_const: 0x6e90
-  __DATA.__objc_selrefs: 0x1dc0
-  __DATA.__objc_ivar: 0x440
+  __DATA.__objc_const: 0x6f00
+  __DATA.__objc_selrefs: 0x1de8
+  __DATA.__objc_ivar: 0x448
   __DATA.__objc_data: 0x19a0
   __DATA.__data: 0xff8
   __DATA.__common: 0x18

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1171
-  Symbols:   329
-  CStrings:  2090
+  Functions: 1180
+  Symbols:   328
+  CStrings:  2100
 
Symbols:
- _objc_retain_x28
CStrings:
+ "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu accessLevel=%llu>"
+ "Rejecting untrusted message to restricted service port %llu"
+ "TB,N,V_originatorUntrusted"
+ "TQ,N,V_accessLevel"
+ "_accessLevel"
+ "_originatorUntrusted"
+ "accessLevel"
+ "accessLevelForPort:"
+ "originatorUntrusted"
+ "patchMessage:toConnection:"
+ "setAccessLevel:"
+ "setOriginatorUntrusted:"
- "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu>"
- "patchMessage:"
```
