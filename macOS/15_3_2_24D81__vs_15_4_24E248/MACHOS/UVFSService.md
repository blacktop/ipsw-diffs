## UVFSService

> `/System/Library/PrivateFrameworks/UVFSXPCService.framework/Versions/A/XPCServices/UVFSService.xpc/Contents/MacOS/UVFSService`

```diff

-713.0.0.0.0
-  __TEXT.__text: 0x25670
+716.100.4.0.0
+  __TEXT.__text: 0x255f0
   __TEXT.__auth_stubs: 0x720
   __TEXT.__objc_stubs: 0x2ee0
-  __TEXT.__objc_methlist: 0x1218
-  __TEXT.__cstring: 0x115a
+  __TEXT.__objc_methlist: 0x1538
+  __TEXT.__cstring: 0x1124
   __TEXT.__objc_classname: 0x1eb
-  __TEXT.__objc_methname: 0x3f1c
-  __TEXT.__objc_methtype: 0x14a2
-  __TEXT.__oslogstring: 0x3def
+  __TEXT.__objc_methname: 0x3f0c
+  __TEXT.__objc_methtype: 0x14c0
+  __TEXT.__oslogstring: 0x3dbd
   __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x91c
-  __TEXT.__unwind_info: 0x5a8
+  __TEXT.__gcc_except_tab: 0x918
+  __TEXT.__unwind_info: 0x5a0
   __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x7d0
-  __DATA_CONST.__cfstring: 0xc00
+  __DATA_CONST.__const: 0x800
+  __DATA_CONST.__cfstring: 0xc20
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2970
-  __DATA.__objc_selrefs: 0xf40
+  __DATA.__objc_const: 0x2398
+  __DATA.__objc_selrefs: 0xfd8
   __DATA.__objc_ivar: 0x1a4
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x278

   - /System/Library/PrivateFrameworks/LiveFS.framework/Versions/A/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E8422C7C-D110-3B58-A09F-5CC558E3B661
-  Functions: 776
+  UUID: DEC1E0D3-76FA-333D-A17E-7DBB24944F41
+  Functions: 770
   Symbols:   251
   CStrings:  1532
 
CStrings:
+ "%s(%@): flags = 0x%x, opID = %llu."
+ "-[userFSVolume blockmapFile:range:flags:operationID:reply:]"
+ "_N_f_bused"
+ "blockmapFile:range:flags:operationID:reply:"
+ "blockmapWithRange:flags:operationID:extentCount:extents:"
+ "i60@0:8{_NSRange=QQ}16I32Q36^I44@\"NSData\"52"
+ "i60@0:8{_NSRange=QQ}16I32Q36^I44@52"
+ "v60@0:8@16{_NSRange=QQ}24I40Q44@?52"
- "%s(%@): startIO = %u, flags = 0x%x, opID = %llu."
- "%s: %p *%p %llu"
- "%s: %p[%lu] %p[%lu]"
- "-[liveFSNode setFileSystemAttributes:toValue:andResult:]"
- "-[userFSVolume blockmapFile:range:startIO:flags:operationID:reply:]"
- "blockmapFile:range:startIO:flags:operationID:reply:"
- "blockmapWithRange:startIO:flags:operationID:extentCount:extents:"
- "i64@0:8{_NSRange=QQ}16i32I36Q40^I48@\"NSData\"56"
- "i64@0:8{_NSRange=QQ}16i32I36Q40^I48@56"

```
