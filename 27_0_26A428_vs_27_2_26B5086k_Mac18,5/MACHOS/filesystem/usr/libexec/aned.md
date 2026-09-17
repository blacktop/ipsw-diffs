## aned

> `/usr/libexec/aned`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-382.15.1.0.0
-  __TEXT.__text: 0x7db84
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_stubs: 0x3480
-  __TEXT.__objc_methlist: 0x118c
+382.100.0.0.0
+  __TEXT.__text: 0x7dbfc
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_stubs: 0x3460
+  __TEXT.__objc_methlist: 0x1184
   __TEXT.__const: 0x60fc
-  __TEXT.__gcc_except_tab: 0x5f64
+  __TEXT.__gcc_except_tab: 0x5f68
   __TEXT.__cstring: 0x5cf2
-  __TEXT.__oslogstring: 0x6d27
+  __TEXT.__oslogstring: 0x6d3c
   __TEXT.__objc_classname: 0x247
-  __TEXT.__objc_methname: 0x3ece
+  __TEXT.__objc_methname: 0x3e92
   __TEXT.__objc_methtype: 0xeaf
-  __TEXT.__unwind_info: 0x2b68
-  __DATA_CONST.__const: 0x2c18
+  __TEXT.__unwind_info: 0x2b78
+  __DATA_CONST.__const: 0x2c38
   __DATA_CONST.__cfstring: 0xaa0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x710
-  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__auth_got: 0x718
+  __DATA_CONST.__got: 0x3b8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x1cb8
-  __DATA.__objc_selrefs: 0xfc8
-  __DATA.__objc_ivar: 0xe8
+  __DATA.__objc_const: 0x1c98
+  __DATA.__objc_selrefs: 0xfc0
+  __DATA.__objc_ivar: 0xe4
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x490
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2798
-  Symbols:   4144
-  CStrings:  1763
+  Symbols:   4143
+  CStrings:  1760
 
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
