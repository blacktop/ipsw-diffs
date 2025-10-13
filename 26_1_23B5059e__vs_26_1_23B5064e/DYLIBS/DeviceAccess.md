## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-321.7.2.0.0
-  __TEXT.__text: 0x29b08
+321.8.0.0.0
+  __TEXT.__text: 0x2a0f0
   __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_methlist: 0x267c
-  __TEXT.__cstring: 0x5417
+  __TEXT.__objc_methlist: 0x26ac
+  __TEXT.__cstring: 0x54d7
   __TEXT.__gcc_except_tab: 0x75c
   __TEXT.__const: 0x24a
   __TEXT.__swift5_typeref: 0x119

   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x9b8
   __TEXT.__objc_classname: 0x382
-  __TEXT.__objc_methname: 0x560f
+  __TEXT.__objc_methname: 0x5693
   __TEXT.__objc_methtype: 0x7b9
-  __TEXT.__objc_stubs: 0x2bc0
+  __TEXT.__objc_stubs: 0x2c60
   __DATA_CONST.__got: 0x300
   __DATA_CONST.__const: 0x928
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1360
+  __DATA_CONST.__objc_selrefs: 0x1388
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd8
   __AUTH_CONST.__auth_got: 0x728
   __AUTH_CONST.__const: 0x458
-  __AUTH_CONST.__cfstring: 0x21a0
+  __AUTH_CONST.__cfstring: 0x21c0
   __AUTH_CONST.__objc_const: 0x45e0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x3e4
-  __DATA.__data: 0x738
+  __DATA.__data: 0x7a8
   __DATA.__bss: 0x140
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__data: 0x78

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 09DFC283-BEA6-3A9C-A41B-D087B9CB7C18
-  Functions: 1183
-  Symbols:   3622
-  CStrings:  2244
+  UUID: D6D946AC-F615-3A34-A4B9-D43B6E61896A
+  Functions: 1187
+  Symbols:   3636
+  CStrings:  2254
 
Symbols:
+ -[DADevice decodeAdvDataWithCoder:]
+ -[DADevice decodeAdvDataWithCoder:xpcObject:]
+ -[DADevice decodeAdvDataWithXPC:]
+ -[DADevice encodeAdvDataWithCoder:]
+ -[DADevice encodeAdvDataWithCoder:xpcObject:]
+ -[DADevice encodeAdvDataWithXPC:]
+ ___45-[DADevice decodeAdvDataWithCoder:xpcObject:]_block_invoke
+ ___45-[DADevice encodeAdvDataWithCoder:xpcObject:]_block_invoke
+ _gLogCategory_DADevice
+ _objc_msgSend$allKeys
+ _objc_msgSend$decodeAdvDataWithCoder:
+ _objc_msgSend$decodeAdvDataWithCoder:xpcObject:
+ _objc_msgSend$decodeAdvDataWithXPC:
+ _objc_msgSend$encodeAdvDataWithCoder:
+ _objc_msgSend$encodeAdvDataWithCoder:xpcObject:
+ _objc_msgSend$encodeAdvDataWithXPC:
- -[DADevice decodeXPCAdvData:]
- -[DADevice encodeXPCAdvData:]
- ___29-[DADevice decodeXPCAdvData:]_block_invoke
- ___29-[DADevice encodeXPCAdvData:]_block_invoke
- _objc_msgSend$decodeXPCAdvData:
- _objc_msgSend$encodeXPCAdvData:
CStrings:
+ "-[DADevice encodeAdvDataWithCoder:xpcObject:]"
+ "DADevice ADV Data encode flat keys error: %@, flatKeys: %@"
+ "DADevice ADV Data encode nested keys error: %@, nestedKeys: %@"
+ "allKeys"
+ "decodeAdvDataWithCoder:"
+ "decodeAdvDataWithCoder:xpcObject:"
+ "decodeAdvDataWithXPC:"
+ "encodeAdvDataWithCoder:"
+ "encodeAdvDataWithCoder:xpcObject:"
+ "encodeAdvDataWithXPC:"
- "decodeXPCAdvData:"
- "encodeXPCAdvData:"

```
