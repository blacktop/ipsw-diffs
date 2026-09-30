## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-940.21.1.0.0
-  __TEXT.__text: 0xa5c94
+940.22.2.0.0
+  __TEXT.__text: 0xa5f08
   __TEXT.__auth_stubs: 0x3260
-  __TEXT.__objc_methlist: 0x13d4
-  __TEXT.__cstring: 0x2c39d
+  __TEXT.__objc_methlist: 0x13e4
+  __TEXT.__cstring: 0x2c40f
   __TEXT.__const: 0x3e0
   __TEXT.__gcc_except_tab: 0x71c
   __TEXT.__oslogstring: 0x16e
   __TEXT.__dlopen_cstrs: 0x1f3
   __TEXT.__unwind_info: 0x2868
   __TEXT.__objc_classname: 0x1f5
-  __TEXT.__objc_methname: 0x4bf8
-  __TEXT.__objc_methtype: 0x100e
-  __TEXT.__objc_stubs: 0x43a0
+  __TEXT.__objc_methname: 0x4c27
+  __TEXT.__objc_methtype: 0x101f
+  __TEXT.__objc_stubs: 0x43c0
   __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__const: 0x3680
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14d0
+  __DATA_CONST.__objc_selrefs: 0x14d8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x1940
   __AUTH_CONST.__const: 0x2b68
-  __AUTH_CONST.__cfstring: 0x5e80
+  __AUTH_CONST.__cfstring: 0x5ea0
   __AUTH_CONST.__objc_const: 0x1ce0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90A8D236-AB17-3DEF-B6BC-C8E6EF86BC2B
-  Functions: 4923
-  Symbols:   12630
-  CStrings:  5943
+  UUID: 63040493-2A2D-3905-AF87-2240F62A22D6
+  Functions: 4927
+  Symbols:   12639
+  CStrings:  5950
 
Symbols:
+ -[APBonjourCacheManager _updateDeviceMap:deviceIdentifier:deviceAdded:]
+ _OBJC_IVAR_$_APBonjourCacheManager._p2pDeviceMap
+ ___41-[APBonjourCacheManager _recheckDevices:]_block_invoke_2
+ ___block_descriptor_88_e8_32o40o48o56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ _objc_msgSend$_updateDeviceMap:deviceIdentifier:deviceAdded:
- _OBJC_IVAR_$_APBonjourCacheManager._removedItems
- ___block_descriptor_80_e8_32o40o48o56r_e5_v8?0lr56l8s32l8s40l8s48l8
CStrings:
+ "940.22.2"
+ "Ignoring P2P only device: %llu, %'@"
+ "NANDS [%{ptr}] retain activation ( %lu -> %lu, seed: %llu )"
+ "_APBonjourBrowserSendAirPlayNANDeviceEvents"
+ "_p2pDeviceMap"
+ "_updateDeviceMap:deviceIdentifier:deviceAdded:"
+ "addOrUpdate"
+ "p2pOnly"
+ "v36@0:8@16@24B32"
+ "void _APTNANDataSessionInvalidate(FigCFWeakReferenceHolderRef, const uint64_t)_block_invoke"
- "940.21.1"
- "NANDS [%{ptr}] retain activation ( %lu -> %lu )"
- "_removedItems"
- "void _APTNANDataSessionInvalidate(FigCFWeakReferenceHolderRef, const void *)_block_invoke"

```
