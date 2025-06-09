## NanoPreferencesSync

> `/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync`

```diff

-314.1.0.0.0
-  __TEXT.__text: 0xa1e4
+320.0.0.0.0
+  __TEXT.__text: 0xa1f4
   __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0xc04
+  __TEXT.__objc_methlist: 0xc34
+  __TEXT.__cstring: 0xab2
   __TEXT.__const: 0xa0
   __TEXT.__oslogstring: 0xae7
-  __TEXT.__cstring: 0xad0
-  __TEXT.__gcc_except_tab: 0x128
-  __TEXT.__unwind_info: 0x348
-  __TEXT.__objc_classname: 0x116
-  __TEXT.__objc_methname: 0x1f73
+  __TEXT.__gcc_except_tab: 0xfc
+  __TEXT.__unwind_info: 0x340
+  __TEXT.__objc_classname: 0x12e
+  __TEXT.__objc_methname: 0x1fa9
   __TEXT.__objc_methtype: 0x52f
-  __TEXT.__objc_stubs: 0x17e0
+  __TEXT.__objc_stubs: 0x1860
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x500
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__const: 0x4d8
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8c8
+  __DATA_CONST.__objc_selrefs: 0x8f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x2b0
-  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__cfstring: 0x720
-  __AUTH_CONST.__objc_const: 0xe68
+  __AUTH_CONST.__objc_const: 0xef8
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x70
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0x4

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 62687C55-9C48-3C82-BB38-6F10AB574CB5
-  Functions: 284
-  Symbols:   1072
-  CStrings:  639
+  UUID: 501D959A-6BC0-322A-A63E-ECDABBBB7412
+  Functions: 288
+  Symbols:   1090
+  CStrings:  644
 
Symbols:
+ +[NPSPairedDeviceRegistry activeDevice]
+ +[NPSPairedDeviceRegistry registry]
+ +[NPSPairedDeviceRegistry registry].cold.1
+ -[NPSDomainAccessor initWithDomain:pdrDevice:]
+ _OBJC_CLASS_$_NPSPairedDeviceRegistry
+ _OBJC_CLASS_$_PDRDarwinNotifications
+ _OBJC_CLASS_$_PDRRegistry
+ _OBJC_METACLASS_$_NPSPairedDeviceRegistry
+ __OBJC_$_CLASS_METHODS_NPSPairedDeviceRegistry
+ __OBJC_CLASS_RO_$_NPSPairedDeviceRegistry
+ __OBJC_METACLASS_RO_$_NPSPairedDeviceRegistry
+ ___35+[NPSPairedDeviceRegistry registry]_block_invoke
+ _objc_msgSend$getActiveDevice
+ _objc_msgSend$pairingStorePath
+ _objc_msgSend$registry
+ _objc_msgSend$start
+ _objc_msgSend$watchDidBecomeActive
+ _registry.onceToken
+ _registry.result
- GCC_except_table1
- _NRPairedDeviceRegistryWatchDidBecomeActiveDarwinNotification
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- ___73+[NPSDomainAccessor resolveActivePairedDevicePairingID:pairingDataStore:]_block_invoke
- ___block_descriptor_48_e8_32r40r_e29_v24?0"NSString"8"NSUUID"16lr32l8r40l8
- _objc_msgSend$altAccountPairingStorePathPairingID:
CStrings:
+ "Failed to get notify token %s"
+ "NPSPairedDeviceRegistry"
+ "activeDevice"
+ "getActiveDevice"
+ "initWithDomain:pdrDevice:"
+ "registry"
+ "start"
+ "watchDidBecomeActive"
- "Failed to get notify token %@"
- "altAccountPairingStorePathPairingID:"
- "v24@?0@\"NSString\"8@\"NSUUID\"16"

```
