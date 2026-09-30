## ANEStorageMaintainer

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-382.11.0.0.0
-  __TEXT.__text: 0x7800
+382.12.0.0.0
+  __TEXT.__text: 0x7990
   __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x3b4
+  __TEXT.__objc_stubs: 0xf20
+  __TEXT.__objc_methlist: 0x3c4
   __TEXT.__const: 0xc8
   __TEXT.__oslogstring: 0xd7d
   __TEXT.__objc_classname: 0x86
-  __TEXT.__objc_methname: 0xf94
+  __TEXT.__objc_methname: 0xfe6
   __TEXT.__objc_methtype: 0x26b
   __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__cstring: 0x1e3
+  __TEXT.__cstring: 0x1e8
   __TEXT.__unwind_info: 0x190
   __DATA_CONST.__const: 0x118
-  __DATA_CONST.__cfstring: 0x2c0
+  __DATA_CONST.__cfstring: 0x300
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0xd0
   __DATA.__objc_const: 0x450
-  __DATA.__objc_selrefs: 0x4d8
+  __DATA.__objc_selrefs: 0x4f8
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x130

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 96
-  Symbols:   380
-  CStrings:  318
+  Functions: 97
+  Symbols:   384
+  CStrings:  324
 
Symbols:
+ +[_ANEStorageHelper isPath:safelyWithinDirectory:]
+ GCC_except_table10
+ GCC_except_table6
+ _objc_msgSend$containsObject:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$stringByAppendingString:
- GCC_except_table5
- GCC_except_table9
Functions:
+ +[_ANEStorageHelper isPath:safelyWithinDirectory:]
CStrings:
+ ".."
+ "/"
+ "containsObject:"
+ "hasSuffix:"
+ "isPath:safelyWithinDirectory:"
+ "stringByAppendingString:"
```
