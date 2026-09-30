## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Versions/A/Symbolication`

```diff

 64575.70.1.0.0
-  __TEXT.__text: 0xc45d0
+  __TEXT.__text: 0xc44dc
   __TEXT.__auth_stubs: 0x1f00
   __TEXT.__objc_methlist: 0x6aa0
   __TEXT.__const: 0x306
-  __TEXT.__gcc_except_tab: 0x55c4
-  __TEXT.__cstring: 0x10e30
+  __TEXT.__gcc_except_tab: 0x55a0
+  __TEXT.__cstring: 0x10e20
   __TEXT.__oslogstring: 0x18dc
   __TEXT.__ustring: 0x2c
   __TEXT.__swift5_typeref: 0x402

   __TEXT.__swift5_reflstr: 0x311
   __TEXT.__swift5_fieldmd: 0x2a8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2de8
+  __TEXT.__unwind_info: 0x2de0
   __TEXT.__objc_classname: 0x980
   __TEXT.__objc_methname: 0x10b85
   __TEXT.__objc_methtype: 0x6ba1

   __DATA_CONST.__objc_arraydata: 0x870
   __AUTH_CONST.__auth_got: 0xf98
   __AUTH_CONST.__const: 0x4870
-  __AUTH_CONST.__cfstring: 0xe480
+  __AUTH_CONST.__cfstring: 0xe460
   __AUTH_CONST.__objc_const: 0xca78
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswiftos.dylib
   Functions: 3408
   Symbols:   7507
-  CStrings:  6216
+  CStrings:  6215
 
Functions:
~ -[VMUProcessDescription _cpuTypeDescription] : 520 -> 420
~ -[VMUProcessDescription processDescriptionHeader] : 1692 -> 1628
~ -[VMUProcessObjectGraph parseMacOSArchitectureFromProcessDescription] : 724 -> 644
CStrings:
- ".X1"
```
