## DoNotDisturb

> `/System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb`

```diff

-371.16.0.0.0
+371.112.0.0.0
   __TEXT.__text: 0x42c08
   __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x3ca4

   __TEXT.__oslogstring: 0x52b3
   __TEXT.__unwind_info: 0x14d4
   __TEXT.__objc_classname: 0xed4
-  __TEXT.__objc_methname: 0x88dd
+  __TEXT.__objc_methname: 0x88ef
   __TEXT.__objc_methtype: 0x1e1a
   __TEXT.__objc_stubs: 0x4300
   __DATA_CONST.__got: 0x70

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xa930
   __DATA_CONST.__objc_selrefs: 0x1880
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x340
+  __DATA_CONST.__objc_superrefs: 0x1c0
   __AUTH_CONST.__cfstring: 0x3580
   __AUTH_CONST.__objc_const: 0x28e0
   __AUTH_CONST.__const: 0x420
   __AUTH_CONST.__auth_got: 0x300
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x340
-  __DATA.__objc_superrefs: 0x1c0
+  __AUTH.__objc_data: 0x500
   __DATA.__objc_ivar: 0x3a8
   __DATA.__data: 0xe50
-  __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0x15e0
+  __DATA.__bss: 0x8
+  __DATA_DIRTY.__objc_data: 0x1630
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0x1d8
+  __DATA_DIRTY.__bss: 0x1e8
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E2269F04-3ED3-32DB-BCA1-D31649B9BFFD
+  UUID: A86A1DFE-DDAB-3CF8-8245-9F7DD727E44D
   Functions: 1606
   Symbols:   5650
-  CStrings:  2761
+  CStrings:  2762
 
Symbols:
+ ___62-[DNDRemoteServiceConnection _connectionLock_createConnection]_block_invoke.264
+ ___62-[DNDRemoteServiceConnection _connectionLock_createConnection]_block_invoke.267
+ ___65-[DNDRemoteAvailabilityServiceConnection _queue_createConnection]_block_invoke.58
+ ___65-[DNDRemoteAvailabilityServiceConnection _queue_createConnection]_block_invoke.61
+ ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.274
+ ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.277
+ ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.281
+ ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.285
+ ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.288
+ ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke_2.280
+ ___69-[DNDRemoteAppConfigurationServiceConnection _queue_createConnection]_block_invoke.60
+ ___69-[DNDRemoteAppConfigurationServiceConnection _queue_createConnection]_block_invoke.63
+ ___block_literal_global.141
+ ___block_literal_global.263
+ ___block_literal_global.266
+ ___block_literal_global.269
+ ___block_literal_global.319
+ ___block_literal_global.325
+ ___block_literal_global.57
+ ___block_literal_global.60
+ ___block_literal_global.63
+ ___block_literal_global.65
- ___62-[DNDRemoteServiceConnection _connectionLock_createConnection]_block_invoke.263
- ___62-[DNDRemoteServiceConnection _connectionLock_createConnection]_block_invoke.266
- ___65-[DNDRemoteAvailabilityServiceConnection _queue_createConnection]_block_invoke.57
- ___65-[DNDRemoteAvailabilityServiceConnection _queue_createConnection]_block_invoke.60
- ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.273
- ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.275
- ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.280
- ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.283
- ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.286
- ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke_2.279
- ___69-[DNDRemoteAppConfigurationServiceConnection _queue_createConnection]_block_invoke.59
- ___69-[DNDRemoteAppConfigurationServiceConnection _queue_createConnection]_block_invoke.62
- ___block_literal_global.140
- ___block_literal_global.262
- ___block_literal_global.265
- ___block_literal_global.268
- ___block_literal_global.318
- ___block_literal_global.324
- ___block_literal_global.56
- ___block_literal_global.58
- ___block_literal_global.61
- ___block_literal_global.64
CStrings:
+ "T@\"NSString\",?,R,C"

```
