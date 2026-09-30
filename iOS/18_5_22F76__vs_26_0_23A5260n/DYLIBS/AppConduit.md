## AppConduit

> `/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit`

```diff

-382.0.0.0.0
-  __TEXT.__text: 0x1d69c
-  __TEXT.__auth_stubs: 0x820
+387.0.0.0.0
+  __TEXT.__text: 0x1d784
+  __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_methlist: 0x145c
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x6058
+  __TEXT.__cstring: 0x60cc
   __TEXT.__gcc_except_tab: 0x4e4
   __TEXT.__oslogstring: 0x7d
-  __TEXT.__unwind_info: 0x7c8
+  __TEXT.__unwind_info: 0x7c0
   __TEXT.__objc_classname: 0x147
-  __TEXT.__objc_methname: 0x50c7
-  __TEXT.__objc_methtype: 0xb19
-  __TEXT.__objc_stubs: 0x2dc0
+  __TEXT.__objc_methname: 0x50f4
+  __TEXT.__objc_methtype: 0xb0b
+  __TEXT.__objc_stubs: 0x2e40
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0x8e0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf80
+  __DATA_CONST.__objc_selrefs: 0xfa0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x420
+  __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x28e0
+  __AUTH_CONST.__cfstring: 0x2900
   __AUTH_CONST.__objc_const: 0x1b28
   __DATA.__objc_ivar: 0xf0
   __DATA.__data: 0x280

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED2C7DDC-CF0C-39FC-B75C-220C50724098
+  UUID: 8D9E696A-A803-36CE-9599-E93E134F92E2
   Functions: 564
-  Symbols:   2100
-  CStrings:  1610
+  Symbols:   2105
+  CStrings:  1615
 
Symbols:
+ -[ACXRemoteApplication isCompatibleWithDevice:]
+ _macho_arch_name_for_cpu_type
+ _objc_msgSend$cpuSubtype
+ _objc_msgSend$cpuType
+ _objc_msgSend$runnableArchNames
+ _objc_msgSend$unsignedIntValue
- -[ACXRemoteApplication isCompatibleWithCPUType:subtype:]
CStrings:
+ "-[ACXRemoteApplication isCompatibleWithDevice:]"
+ "Checking if %@ is compatible with cputype: 0x%x, subtype: 0x%x, runnableArchNames: %@"
+ "Unexpected NULL archName from macho_arch_name_for_cpu_type with sliceCpuType: 0x%x sliceSubType: 0x%x"
+ "cpuSubtype"
+ "cpuType"
+ "isCompatibleWithDevice:"
+ "runnableArchNames"
+ "unsignedIntValue"
- "-[ACXRemoteApplication isCompatibleWithCPUType:subtype:]"
- "B24@0:8i16i20"
- "Checking if %@ is compatible with cputype: 0x%x, subtype: 0x%x"
- "isCompatibleWithCPUType:subtype:"

```
