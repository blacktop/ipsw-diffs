## UVFSService

> `/System/Library/PrivateFrameworks/UVFSXPCService.framework/XPCServices/UVFSService.xpc/UVFSService`

```diff

-713.0.0.0.0
-  __TEXT.__text: 0x23f08
+716.100.3.0.0
+  __TEXT.__text: 0x23d90
   __TEXT.__auth_stubs: 0x940
   __TEXT.__objc_stubs: 0x3040
-  __TEXT.__objc_methlist: 0x123c
-  __TEXT.__cstring: 0x11b6
+  __TEXT.__objc_methlist: 0x1560
+  __TEXT.__cstring: 0x1180
   __TEXT.__objc_classname: 0x1eb
-  __TEXT.__objc_methname: 0x40e8
-  __TEXT.__objc_methtype: 0x14b4
-  __TEXT.__oslogstring: 0x3fcc
+  __TEXT.__objc_methname: 0x40d8
+  __TEXT.__objc_methtype: 0x14d2
+  __TEXT.__oslogstring: 0x3f6b
   __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x954
-  __TEXT.__unwind_info: 0x590
+  __TEXT.__gcc_except_tab: 0x950
+  __TEXT.__unwind_info: 0x588
   __DATA_CONST.__auth_got: 0x4b0
   __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x718
-  __DATA_CONST.__cfstring: 0xc00
+  __DATA_CONST.__const: 0x740
+  __DATA_CONST.__cfstring: 0xc20
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x29a0
-  __DATA.__objc_selrefs: 0xf88
+  __DATA.__objc_const: 0x23c8
+  __DATA.__objc_selrefs: 0x1020
   __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x278

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 745
+  Functions: 738
   Symbols:   287
-  CStrings:  1464
+  CStrings:  1462
 
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
- "LFN[%p]: Generated fileID is less then 3: %llu"
- "blockmapFile:range:startIO:flags:operationID:reply:"
- "blockmapWithRange:startIO:flags:operationID:extentCount:extents:"
- "i64@0:8{_NSRange=QQ}16i32I36Q40^I48@\"NSData\"56"
- "i64@0:8{_NSRange=QQ}16i32I36Q40^I48@56"

```
