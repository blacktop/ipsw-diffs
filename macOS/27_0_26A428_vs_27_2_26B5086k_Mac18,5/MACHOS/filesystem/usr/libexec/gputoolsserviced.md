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

-2027.0.39.0.0
-  __TEXT.__text: 0x374b4
+2027.0.44.0.0
+  __TEXT.__text: 0x37dcc
   __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_stubs: 0x5740
-  __TEXT.__objc_methlist: 0x362c
+  __TEXT.__objc_stubs: 0x5820
+  __TEXT.__objc_methlist: 0x366c
   __TEXT.__const: 0x490
-  __TEXT.__oslogstring: 0x1d3e
-  __TEXT.__cstring: 0x4c8e
-  __TEXT.__objc_methname: 0x7ab1
+  __TEXT.__oslogstring: 0x1d96
+  __TEXT.__cstring: 0x4d0e
+  __TEXT.__objc_methname: 0x7b6a
   __TEXT.__objc_classname: 0x84d
   __TEXT.__objc_methtype: 0x1404
-  __TEXT.__unwind_info: 0xdd0
-  __DATA_CONST.__const: 0xc60
-  __DATA_CONST.__cfstring: 0x3660
+  __TEXT.__unwind_info: 0xdf0
+  __DATA_CONST.__const: 0xc90
+  __DATA_CONST.__cfstring: 0x36e0
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x6d8
   __DATA_CONST.__got: 0x248
-  __DATA.__objc_const: 0x6eb0
-  __DATA.__objc_selrefs: 0x1e98
-  __DATA.__objc_ivar: 0x444
+  __DATA.__objc_const: 0x6f20
+  __DATA.__objc_selrefs: 0x1ec0
+  __DATA.__objc_ivar: 0x44c
   __DATA.__objc_data: 0x19a0
   __DATA.__data: 0xff8
   __DATA.__common: 0x18

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1216
+  Functions: 1226
   Symbols:   296
-  CStrings:  2162
+  CStrings:  2173
 
CStrings:
+ "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu accessLevel=%llu>"
+ "Failed to patch message, %@"
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
