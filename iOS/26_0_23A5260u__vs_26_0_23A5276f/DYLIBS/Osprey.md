## Osprey

> `/System/Library/PrivateFrameworks/Osprey.framework/Osprey`

```diff

-3400.4.1.0.0
-  __TEXT.__text: 0x64ed0
+3500.3.1.0.0
+  __TEXT.__text: 0x64f2c
   __TEXT.__auth_stubs: 0x760
   __TEXT.__objc_methlist: 0x1218
   __TEXT.__const: 0x102a0

   __TEXT.__unwind_info: 0x810
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x3ae
-  __TEXT.__objc_methname: 0x2ce1
+  __TEXT.__objc_methname: 0x2d2b
   __TEXT.__objc_methtype: 0xd60
-  __TEXT.__objc_stubs: 0x22c0
+  __TEXT.__objc_stubs: 0x2300
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0x828
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_selrefs: 0xb00
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x3c8

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C11DF158-DAA1-356C-A3B8-76E10F3AD069
+  UUID: C274C844-C4D2-3E7C-8C05-39A63A7522BA
   Functions: 715
-  Symbols:   2166
-  CStrings:  1061
+  Symbols:   2168
+  CStrings:  1063
 
Symbols:
+ _objc_msgSend$TLSMinimumSupportedProtocolVersion
+ _objc_msgSend$setTLSMinimumSupportedProtocolVersion:
Functions:
~ -[OspreyGRPCChannel initWithURL:configuration:queue:] : 456 -> 484
~ -[OspreyConnectionPool connectionForConfiguration:] : 504 -> 568
CStrings:
+ "TLSMinimumSupportedProtocolVersion"
+ "setTLSMinimumSupportedProtocolVersion:"

```
