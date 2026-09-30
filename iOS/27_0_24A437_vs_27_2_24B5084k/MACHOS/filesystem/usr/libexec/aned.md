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
-  __TEXT.__text: 0x7c720
-  __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_stubs: 0x34a0
-  __TEXT.__objc_methlist: 0x1184
+382.100.2.0.0
+  __TEXT.__text: 0x7c790
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__objc_stubs: 0x3480
+  __TEXT.__objc_methlist: 0x117c
   __TEXT.__const: 0x60ec
-  __TEXT.__gcc_except_tab: 0x619c
+  __TEXT.__gcc_except_tab: 0x61a0
   __TEXT.__cstring: 0x5cfc
-  __TEXT.__oslogstring: 0x6cd0
+  __TEXT.__oslogstring: 0x6ce5
   __TEXT.__objc_classname: 0x247
-  __TEXT.__objc_methname: 0x3ea7
+  __TEXT.__objc_methname: 0x3e6b
   __TEXT.__objc_methtype: 0xeaf
-  __TEXT.__unwind_info: 0x2c48
-  __DATA_CONST.__const: 0x2b48
+  __TEXT.__unwind_info: 0x2c58
+  __DATA_CONST.__const: 0x2b68
   __DATA_CONST.__cfstring: 0xb00
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x7d0
-  __DATA_CONST.__got: 0x3c0
+  __DATA_CONST.__auth_got: 0x7d8
+  __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x1cb8
-  __DATA.__objc_selrefs: 0xfc0
-  __DATA.__objc_ivar: 0xe8
+  __DATA.__objc_const: 0x1c98
+  __DATA.__objc_selrefs: 0xfb8
+  __DATA.__objc_ivar: 0xe4
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x490
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2787
-  Symbols:   4173
-  CStrings:  1758
+  Symbols:   4176
+  CStrings:  1755
 
Symbols:
+ GCC_except_table21
+ GCC_except_table59
+ __32-[_ANEServer maxModelMemorySize]_block_invoke
+ __ZZ32-[_ANEServer maxModelMemorySize]E19sMaxModelMemorySize
+ __ZZ32-[_ANEServer maxModelMemorySize]E9onceToken
+ ___32-[_ANEServer maxModelMemorySize]_block_invoke
+ _kANEFModelMutableClusterIndexKey
+ _usleep
- -[_ANEServer setMaxModelMemorySize:]
- GCC_except_table44
- GCC_except_table55
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
