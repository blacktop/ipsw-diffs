## hpmdiagnose

> `/usr/bin/hpmdiagnose`

```diff

-570.100.13.0.0
-  __TEXT.__text: 0xf710
+614.0.0.0.0
+  __TEXT.__text: 0x10030
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0x17a0
-  __TEXT.__objc_methlist: 0xf08
-  __TEXT.__cstring: 0x1e5f
+  __TEXT.__objc_stubs: 0x19e0
+  __TEXT.__objc_methlist: 0xff0
+  __TEXT.__cstring: 0x1e71
   __TEXT.__const: 0x93
-  __TEXT.__objc_methname: 0x23a5
-  __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methtype: 0x5cb
-  __TEXT.__unwind_info: 0x308
+  __TEXT.__objc_methname: 0x25a4
+  __TEXT.__objc_classname: 0xc4
+  __TEXT.__objc_methtype: 0x604
+  __TEXT.__unwind_info: 0x320
   __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x2660
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__cfstring: 0x26a0
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x12a8
   __DATA_CONST.__objc_arraydata: 0xe28
   __DATA_CONST.__objc_arrayobj: 0x348
   __DATA_CONST.__objc_dictobj: 0xed8
-  __DATA.__objc_const: 0xb58
-  __DATA.__objc_selrefs: 0x898
-  __DATA.__objc_ivar: 0x8c
-  __DATA.__objc_data: 0x2d0
+  __DATA.__objc_const: 0xc88
+  __DATA.__objc_selrefs: 0x948
+  __DATA.__objc_ivar: 0x98
+  __DATA.__objc_data: 0x320
   __DATA.__data: 0xb0
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31B45988-ADFD-32B9-A59A-577CCF7292E0
-  Functions: 312
+  UUID: 49B55269-D9BE-378A-9E47-BEE442014072
+  Functions: 330
   Symbols:   100
-  CStrings:  1096
+  CStrings:  1133
 
CStrings:
+ "%-32s %@"
+ "0x%x"
+ "@\"NSArray\""
+ "@32@0:8@16*24"
+ "ERROR: fail code=0x%X\n"
+ "PDControllerType6"
+ "PDRegisters"
+ "T@\"NSArray\",&,N,V_PDRegisters"
+ "T@\"NSDictionary\",&,N,V_registerDecodes"
+ "TI,N,V_remote_vid"
+ "_PDRegisters"
+ "_registerDecodes"
+ "_remote_vid"
+ "alloc"
+ "byteOffset"
+ "decodeFieldWithValue:"
+ "decodeRegister:withArray:fromBuffer:"
+ "fieldName"
+ "forceUSBDeviceMode:withDevice:"
+ "i28@0:8I16Q20"
+ "i40@0:8@16@24^v32"
+ "initWithCapacity:"
+ "initWithChar:"
+ "initWithUnsignedLongLong:"
+ "printRegisterTitle:andData:"
+ "registerDecodes"
+ "registerName"
+ "remote_vid"
+ "setObject:atIndexedSubscript:"
+ "setPDRegisters:"
+ "setRegisterDecodes:"
+ "setRemote_vid:"
+ "setupRegisterDecodes"
+ "size"
+ "valueForKey:"
- "remote read failed"

```
