## LiveFS

> `/System/Library/PrivateFrameworks/LiveFS.framework/Versions/A/LiveFS`

```diff

-474.60.43.0.0
-  __TEXT.__text: 0x20030
+531.101.1.0.0
+  __TEXT.__text: 0x200e8
   __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x1744
+  __TEXT.__objc_methlist: 0x1f8c
   __TEXT.__const: 0x130
   __TEXT.__cstring: 0x1038
   __TEXT.__oslogstring: 0x1483
   __TEXT.__gcc_except_tab: 0xd1c
-  __TEXT.__unwind_info: 0xa48
+  __TEXT.__unwind_info: 0xa40
   __TEXT.__objc_classname: 0x334
-  __TEXT.__objc_methname: 0x42e1
-  __TEXT.__objc_methtype: 0x2a8b
+  __TEXT.__objc_methname: 0x42d9
+  __TEXT.__objc_methtype: 0x2aac
   __TEXT.__objc_stubs: 0x2860
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf98
+  __DATA_CONST.__objc_selrefs: 0x1030
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xb0
   __AUTH_CONST.__auth_got: 0x328
   __AUTH_CONST.__const: 0xfc0
   __AUTH_CONST.__cfstring: 0x860
-  __AUTH_CONST.__objc_const: 0x3a30
+  __AUTH_CONST.__objc_const: 0x2a88
   __AUTH.__objc_data: 0x820
   __DATA.__objc_ivar: 0x200
   __DATA.__data: 0x728

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 421427D4-3A3C-353F-A3AC-D562C80FA6B1
-  Functions: 826
-  Symbols:   1898
-  CStrings:  1362
+  UUID: F7A8B2C0-0FFF-3A65-B897-0B39923314CF
+  Functions: 824
+  Symbols:   1897
+  CStrings:  1363
 
Symbols:
+ -[LiveFSServiceConnection blockmapFile:range:flags:operationID:reply:]
+ -[LiveFSVolume blockmapFile:range:flags:operationID:reply:]
+ GCC_except_table176
+ _objc_msgSend$blockmapFile:range:flags:operationID:reply:
+ getBootUUID.cold.1
+ livefs_std_log.cold.1
- -[LiveFSServiceConnection blockmapFile:range:startIO:flags:operationID:reply:]
- -[LiveFSVolume blockmapFile:range:startIO:flags:operationID:reply:]
- GCC_except_table178
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _objc_msgSend$blockmapFile:range:startIO:flags:operationID:reply:
CStrings:
+ "blockmapFile:range:flags:operationID:reply:"
+ "v60@0:8@\"NSString\"16{_NSRange=QQ}24I40Q44@?<v@?i@\"NSData\"@\"NSData\">52"
+ "v60@0:8@16{_NSRange=QQ}24I40Q44@?52"
- "blockmapFile:range:startIO:flags:operationID:reply:"
- "v64@0:8@\"NSString\"16{_NSRange=QQ}24i40I44Q48@?<v@?i@\"NSData\"@\"NSData\">56"

```
