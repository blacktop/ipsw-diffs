## maphelperservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice`

```diff

-3060.0.8.0.2
-  __TEXT.__text: 0xbe78
+3060.0.16.0.0
+  __TEXT.__text: 0xbf6c
   __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_stubs: 0xc40
   __TEXT.__objc_methlist: 0x2b4
-  __TEXT.__const: 0x40c
-  __TEXT.__gcc_except_tab: 0xeb0
-  __TEXT.__cstring: 0x12c9
+  __TEXT.__const: 0x414
+  __TEXT.__gcc_except_tab: 0xec0
+  __TEXT.__cstring: 0x13a4
   __TEXT.__oslogstring: 0x1a7
   __TEXT.__objc_classname: 0x6b
   __TEXT.__objc_methname: 0xecd

   __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x3c0
-  __DATA_CONST.__cfstring: 0xf20
+  __DATA_CONST.__cfstring: 0xf60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: DBD31EAD-65A2-3725-A62E-98CBC9A54DAE
+  UUID: 5725D526-6960-3AC8-A9C4-3289CC2BF3FD
   Functions: 182
   Symbols:   225
-  CStrings:  465
+  CStrings:  469
 
Functions:
~ sub_10000b254 : 4552 -> 4752
~ sub_10000c4fc -> sub_10000c5c4 : 12 -> 56
CStrings:
+ "CLTSP,CLMM,MaphelperService,stopConstructRouteFromLocation"
+ "CLTSP,CVR,iterations,%d/%d,exceeded max"
+ "CLTSP,CVR,iterations,%d/%d,exceeded max allowed time,%.2lf"
+ "CLTSP,CVR,route construction completed,allowNetwork,%d,preferCachedTiles,%d,processingTimeMSec,%.2lf,iterations,%d/%d"
+ "CLTSP,CVR,route length exceeded max allowed,length,%.1lf,maxLength,%.1lf,iterations,%d/%d"
+ "CLTSP,CVR,search failed,processingTimeMSec,%.2lf,iterations,%d/%d"
- "CLTSP,CVR,iterations,%d,exceeded max,%d"
- "CLTSP,CVR,route construction completed,allowNetwork,%d,preferCachedTiles,%d"
- "CLTSP,CVR,route length exceeded max allowed,length,%.1lf,maxLength,%.1lf"
- "CLTSP,CVR,search failed"

```
