## IMTransferAgent

> `/System/Library/PrivateFrameworks/IMTransferAgent.framework/IMTransferAgent`

```diff

-1491.300.43.0.0
-  __TEXT.__text: 0x17614
+1491.300.74.0.0
+  __TEXT.__text: 0x17bec
   __TEXT.__objc_methlist: 0xa9c
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x17cc
-  __TEXT.__cstring: 0xbe5
-  __TEXT.__oslogstring: 0x2e2f
-  __TEXT.__unwind_info: 0x620
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x187c
+  __TEXT.__cstring: 0xc24
+  __TEXT.__oslogstring: 0x2f61
+  __TEXT.__unwind_info: 0x628
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8d0
+  __DATA_CONST.__const: 0x8c8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd98
+  __DATA_CONST.__objc_selrefs: 0xda0
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__got: 0x3b0
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0xdc0
+  __AUTH_CONST.__cfstring: 0xde0
   __AUTH_CONST.__objc_const: 0xdb0
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 256
-  Symbols:   269
-  CStrings:  362
+  Symbols:   271
+  CStrings:  367
 
Symbols:
+ _IMTransferAgentErrorDomain
+ _IMTransferAgentErrorFZErrorTypeKey
+ _NSLocalizedDescriptionKey
- _objc_retain_x4
Functions:
~ sub_28decce90 -> sub_28f693e90 : 264 -> 464
~ sub_28decd284 -> sub_28f69434c : 1796 -> 1772
~ sub_28dece17c -> sub_28f69522c : 3568 -> 3928
~ sub_28ded0b98 -> sub_28f697db0 : 1464 -> 1868
~ sub_28ded15e0 -> sub_28f69898c : 132 -> 540
~ sub_28ded1a2c -> sub_28f698f70 : 2680 -> 2684
~ sub_28ded2f8c -> sub_28f69a4d4 : 2712 -> 2772
~ sub_28ded3a24 -> sub_28f69afa8 : 3072 -> 3156
CStrings:
+ "  ** Encryption failed (errorType: %d) - failing without upload. path: %@ transferID: %@"
+ "  ** File is empty or unreadable - failing without upload. path: %@ transferID: %@ topic: %@"
+ "Failed to encrypt the file for upload"
+ "Failing upload for transfer %@ as MMCS reports a protocol file size of 0."
+ "Refusing to upload a zero-length or unreadable file"
+ "We will not try to re-upload as the file is empty"
- "IMTransferAgentErrorDomain"
```
