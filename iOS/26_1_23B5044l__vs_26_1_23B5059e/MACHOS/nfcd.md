## nfcd

> `/usr/libexec/nfcd`

```diff

-361.2.0.0.0
-  __TEXT.__text: 0x27a068
+361.5.0.0.0
+  __TEXT.__text: 0x27a46c
   __TEXT.__auth_stubs: 0x1840
   __TEXT.__delay_stubs: 0x370
   __TEXT.__delay_helper: 0x120c
   __TEXT.__objc_stubs: 0xd460
   __TEXT.__objc_methlist: 0x9cb0
   __TEXT.__const: 0x13c0
-  __TEXT.__objc_methname: 0x17d87
-  __TEXT.__cstring: 0x2f83f
+  __TEXT.__objc_methname: 0x17dc2
+  __TEXT.__cstring: 0x2f9af
   __TEXT.__objc_classname: 0x1d5f
   __TEXT.__objc_methtype: 0x567d
-  __TEXT.__oslogstring: 0x269f8
+  __TEXT.__oslogstring: 0x26a91
   __TEXT.__unwind_info: 0x2c48
   __DATA_CONST.__auth_got: 0xcc8
   __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x83b8
-  __DATA_CONST.__cfstring: 0x11160
+  __DATA_CONST.__cfstring: 0x11260
   __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x390

   __DATA_CONST.__objc_arraydata: 0x1d88
   __DATA_CONST.__objc_arrayobj: 0x2b8
   __DATA_CONST.__objc_dictobj: 0xfa0
-  __DATA.__objc_const: 0x14928
+  __DATA.__objc_const: 0x14908
   __DATA.__objc_selrefs: 0x55e0
-  __DATA.__objc_ivar: 0x10ac
+  __DATA.__objc_ivar: 0x10a8
   __DATA.__objc_data: 0x3d90
   __DATA.__data: 0x2b94
   __DATA.__bss: 0x288

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8C332F25-DB3F-3D1F-AE09-C4743CFA8C34
+  UUID: 16DE66B5-BF6A-3231-9E48-B235BACC036A
   Functions: 4156
   Symbols:   592
-  CStrings:  14606
+  CStrings:  14629
 
CStrings:
+ "%c[%{public}s %{public}s]:%i Error : Unexpected state : unknown."
+ "%c[%{public}s %{public}s]:%i Failed to acquire power assertion, system heading to sleep"
+ "-[_NFHardwareManager init]_block_invoke"
+ "DPD Check timer"
+ "Last OS Reset"
+ "NFCD built from (B&I) Stockholm_Base-361.5"
+ "Post startup timer"
+ "SE Active"
+ "Updated Pairing"
+ "User shutdown"
+ "Will Sleep"
+ "_expressConfigInitWithBugCaptureReport:"
+ "_postStartUpOnceTimer"
+ "consistencyCheckWithConfig:bugCaptureReportEnable:"
+ "didPreWarmHardware"
+ "hwState"
+ "hwState == NFDriverHWStateUnknown"
+ "strongself->_driverWrapper != nil"
+ "updateExpressConfigsWithBugCaptureReport:"
- "NFCD built from (B&I) Stockholm_Base-361.2"
- "_expressConfigInit"
- "_stockholmDispatchOnceTimer"
- "consistencyCheckWithConfig:"
- "didPrewWarmHardware"

```
