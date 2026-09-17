## gpudebug

> `/usr/bin/gpudebug`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2027.0.39.0.0
-  __TEXT.__text: 0x1f260
+2027.0.44.0.0
+  __TEXT.__text: 0x1f33c
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_stubs: 0x2820
-  __TEXT.__objc_methlist: 0x24d4
+  __TEXT.__objc_stubs: 0x2840
+  __TEXT.__objc_methlist: 0x24ec
   __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x1d8
-  __TEXT.__cstring: 0x2c8c
-  __TEXT.__objc_methname: 0x3036
+  __TEXT.__oslogstring: 0x209
+  __TEXT.__cstring: 0x2ca9
+  __TEXT.__objc_methname: 0x3072
   __TEXT.__objc_classname: 0x504
   __TEXT.__objc_methtype: 0xa2e
   __TEXT.__ustring: 0x6a
   __TEXT.__unwind_info: 0x948
   __DATA_CONST.__const: 0x8f0
-  __DATA_CONST.__cfstring: 0x17c0
+  __DATA_CONST.__cfstring: 0x17e0
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x5a8
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x4610
-  __DATA.__objc_selrefs: 0xdb0
-  __DATA.__objc_ivar: 0x290
+  __DATA.__objc_const: 0x4640
+  __DATA.__objc_selrefs: 0xdc0
+  __DATA.__objc_ivar: 0x294
   __DATA.__objc_data: 0xff0
   __DATA.__data: 0xbd8
   __DATA.__common: 0x3000330

   - /usr/lib/libedit.3.dylib
   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 845
+  Functions: 848
   Symbols:   231
-  CStrings:  1366
+  CStrings:  1371
 
Symbols:
+ _APP_SANDBOX_READ_WRITE
- _APP_SANDBOX_READ
CStrings:
+ "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu accessLevel=%llu>"
+ "TQ,N,V_accessLevel"
+ "_accessLevel"
+ "accessLevel"
+ "failed to issue sandbox extension for %{public}@"
+ "setAccessLevel:"
- "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu>"
```
