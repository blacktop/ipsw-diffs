## aneuserd

> `/usr/libexec/aneuserd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-382.15.1.0.0
-  __TEXT.__text: 0x7ebf0
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x3660
-  __TEXT.__objc_methlist: 0x12cc
+382.100.0.0.0
+  __TEXT.__text: 0x7ec68
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_stubs: 0x3640
+  __TEXT.__objc_methlist: 0x12c4
   __TEXT.__const: 0x6100
-  __TEXT.__cstring: 0x650c
-  __TEXT.__objc_methname: 0x416a
-  __TEXT.__oslogstring: 0x6d99
+  __TEXT.__cstring: 0x6529
+  __TEXT.__objc_methname: 0x412e
+  __TEXT.__oslogstring: 0x6dae
   __TEXT.__objc_classname: 0x261
   __TEXT.__objc_methtype: 0xecd
-  __TEXT.__gcc_except_tab: 0x5f64
-  __TEXT.__unwind_info: 0x2bb8
-  __DATA_CONST.__const: 0x2c80
-  __DATA_CONST.__cfstring: 0x14a0
+  __TEXT.__gcc_except_tab: 0x5f68
+  __TEXT.__unwind_info: 0x2bc8
+  __DATA_CONST.__const: 0x2ca0
+  __DATA_CONST.__cfstring: 0x14c0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x718
+  __DATA_CONST.__auth_got: 0x720
   __DATA_CONST.__got: 0x280
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x1fa8
-  __DATA.__objc_selrefs: 0x1068
-  __DATA.__objc_ivar: 0xf8
+  __DATA.__objc_const: 0x1f88
+  __DATA.__objc_selrefs: 0x1060
+  __DATA.__objc_ivar: 0xf4
   __DATA.__objc_data: 0x640
-  __DATA.__data: 0x6a0
+  __DATA.__data: 0x6a8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2824
-  Symbols:   4242
-  CStrings:  1870
+  Symbols:   4241
+  CStrings:  1868
 
Symbols:
+ GCC_except_table21
+ GCC_except_table34
+ GCC_except_table67
+ GCC_except_table71
+ __32-[_ANEServer maxModelMemorySize]_block_invoke
+ __ZZ32-[_ANEServer maxModelMemorySize]E19sMaxModelMemorySize
+ __ZZ32-[_ANEServer maxModelMemorySize]E9onceToken
+ ___32-[_ANEServer maxModelMemorySize]_block_invoke
+ _kANEFModelMutableClusterIndexKey
+ _usleep
- -[_ANEServer setMaxModelMemorySize:]
- GCC_except_table32
- GCC_except_table49
- GCC_except_table50
- GCC_except_table59
- GCC_except_table62
- GCC_except_table63
- GCC_except_table66
- GCC_except_table69
- OBJC_IVAR_$__ANEServer._maxModelMemorySize
- _objc_msgSend$setMaxModelMemorySize:
CStrings:
+ "ANEFModelMutableClusterIndex"
+ "TQ,R,N"
+ "maxModelMemorySize: 0x%llx"
+ "maxModelMemorySize: non-internal build, using 0"
+ "maxModelMemorySize: unable to connect to ANE device"
+ "maxModelMemorySize: unable to create device controller"
- "Maximum model memory size: %llu"
- "TQ,V_maxModelMemorySize"
- "Unable to connect to ANE device."
- "Unable to create device controller"
- "_maxModelMemorySize"
- "set maxModelMemorySize to 0"
- "set maxModelMemorySize to 0x%llx"
- "setMaxModelMemorySize:"
```
