## com.apple.DiagnosticsSessionAvailibility

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/XPCServices/com.apple.DiagnosticsSessionAvailibility.xpc/com.apple.DiagnosticsSessionAvailibility`

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
   __TEXT.__text: 0xbbc4
   __TEXT.__auth_stubs: 0x5d0
   __TEXT.__objc_stubs: 0x2140
   __TEXT.__objc_methlist: 0x1214
   __TEXT.__objc_classname: 0x257
-  __TEXT.__objc_methname: 0x2a04
+  __TEXT.__objc_methname: 0x29f8
   __TEXT.__objc_methtype: 0x777
   __TEXT.__cstring: 0xaed
   __TEXT.__const: 0x60

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libMobileGestalt.dylib
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
