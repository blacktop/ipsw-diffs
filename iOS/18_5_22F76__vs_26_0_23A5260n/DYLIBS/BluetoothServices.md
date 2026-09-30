## BluetoothServices

> `/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices`

```diff

-25.4.0.0.0
-  __TEXT.__text: 0x168b8
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x1a0c
-  __TEXT.__const: 0xd0
+30.45.3.0.0
+  __TEXT.__text: 0x1695c
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x1a44
+  __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x68c
   __TEXT.__cstring: 0x4de0
-  __TEXT.__unwind_info: 0x670
+  __TEXT.__unwind_info: 0x680
   __TEXT.__objc_classname: 0x247
-  __TEXT.__objc_methname: 0x36b8
-  __TEXT.__objc_methtype: 0xcae
-  __TEXT.__objc_stubs: 0x1b80
+  __TEXT.__objc_methname: 0x36ef
+  __TEXT.__objc_methtype: 0xcd6
+  __TEXT.__objc_stubs: 0x1ba0
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x4d8
+  __DATA_CONST.__const: 0x4b0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc88
+  __DATA_CONST.__objc_selrefs: 0xc98
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x368
+  __AUTH_CONST.__auth_got: 0x360
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x3a0
-  __AUTH_CONST.__objc_const: 0x2da0
+  __AUTH_CONST.__objc_const: 0x2dd8
   __AUTH.__objc_data: 0x280
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x2cc
+  __DATA.__objc_ivar: 0x2d0
   __DATA.__data: 0x6e8
   __DATA.__bss: 0x34
   __DATA_DIRTY.__objc_data: 0x230

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1BD700A4-75B7-394A-80EA-B55A49193456
-  Functions: 723
-  Symbols:   2319
-  CStrings:  1338
+  UUID: F6F0D324-0FC0-3742-BA90-0B5D7AFB1FE9
+  Functions: 728
+  Symbols:   2321
+  CStrings:  1341
 
Symbols:
+ +[BTAudioRoutingRequest isSupported]
+ -[BTAudioRoutingRequest reason]
+ -[BTAudioRoutingRequest setReason:]
+ -[BTServicesClient showHIDConnectedBannerAperture:completion:]
+ GCC_except_table11
+ _OBJC_IVAR_$_BTAudioRoutingRequest._reason
+ ___55-[BTCloudServicesClient createDeviceRecord:completion:]_block_invoke.102
+ ___62-[BTServicesClient showHIDConnectedBannerAperture:completion:]_block_invoke
+ ___62-[BTServicesClient showHIDConnectedBannerAperture:completion:]_block_invoke_2
+ ___block_literal_global.366
+ _objc_msgSend$showHIDConnectedBannerAperture:completion:
- GCC_except_table14
- ___37-[BTAudioRoutingRequest activateSync]_block_invoke
- ___55-[BTCloudServicesClient createDeviceRecord:completion:]_block_invoke.84
- ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_literal_global.348
- _dispatch_sync
CStrings:
+ "isSupported"
+ "showHIDConnectedBannerAperture:completion:"
+ "v32@0:8@\"CBDevice\"16@?<v@?@\"NSError\">24"

```
