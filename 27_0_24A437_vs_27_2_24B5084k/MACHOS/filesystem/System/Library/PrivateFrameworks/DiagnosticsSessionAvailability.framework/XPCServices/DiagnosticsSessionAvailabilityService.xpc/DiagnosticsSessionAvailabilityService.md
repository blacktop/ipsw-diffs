## DiagnosticsSessionAvailabilityService

> `/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/XPCServices/DiagnosticsSessionAvailabilityService.xpc/DiagnosticsSessionAvailabilityService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1374.2.2.0.0
+1374.40.35.0.0
   __TEXT.__text: 0xb454
   __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_stubs: 0x1fe0

   __TEXT.__cstring: 0x9f4
   __TEXT.__oslogstring: 0x9fc
   __TEXT.__objc_classname: 0x24c
-  __TEXT.__objc_methname: 0x27c9
+  __TEXT.__objc_methname: 0x27bd
   __TEXT.__objc_methtype: 0x70c
   __TEXT.__unwind_info: 0x520
   __DATA_CONST.__const: 0x478

   - /System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit
   - /System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ _PDRDevicePropertyKeySerialNumber
+ _PDRDidPairNotification
+ _PDRDidUnpairNotification
+ _PDRNotificationKeyDevice
- _NRDevicePropertySerialNumber
- _NRPairedDeviceRegistryDevice
- _NRPairedDeviceRegistryDeviceDidPairNotification
- _NRPairedDeviceRegistryDeviceDidUnpairNotification
- _OBJC_CLASS_$_NRPairedDeviceRegistry
CStrings:
+ "_createDeviceWithWatchDevice:"
+ "_watchDevicePaired:"
+ "_watchDeviceUnpaired:"
+ "initWithWatchDevice:"
- "_createDeviceWithNanoDevice:"
- "_nanoRegistryDevicePaired:"
- "_nanoRegistryDeviceUnpaired:"
- "initWithNanoDevice:"
```
