## uarphidd

> `/usr/libexec/uarphidd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1587.0.27.0.0
-  __TEXT.__text: 0x51b0
+1587.1.3.0.0
+  __TEXT.__text: 0x5c00
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x39c
+  __TEXT.__objc_stubs: 0xc60
+  __TEXT.__objc_methlist: 0x3dc
   __TEXT.__const: 0x58
-  __TEXT.__objc_methname: 0xd1d
-  __TEXT.__cstring: 0x7fa
-  __TEXT.__oslogstring: 0x8e2
+  __TEXT.__cstring: 0x8eb
+  __TEXT.__objc_methname: 0xe37
+  __TEXT.__oslogstring: 0xa01
   __TEXT.__objc_classname: 0x6f
-  __TEXT.__objc_methtype: 0x253
-  __TEXT.__unwind_info: 0x198
-  __DATA_CONST.__const: 0x140
-  __DATA_CONST.__cfstring: 0x7a0
+  __TEXT.__objc_methtype: 0x259
+  __TEXT.__unwind_info: 0x1a8
+  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__cfstring: 0x840
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0xc8
-  __DATA.__objc_const: 0x978
-  __DATA.__objc_selrefs: 0x380
-  __DATA.__objc_ivar: 0xbc
+  __DATA.__objc_const: 0x9a8
+  __DATA.__objc_selrefs: 0x3c0
+  __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/UARPKit.framework/Versions/A/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 147
+  Functions: 159
   Symbols:   102
-  CStrings:  369
+  CStrings:  391
 
CStrings:
+ "%s: endpointUUID %@ is already instantiated as a UARPHIDDevice, ignoring"
+ "%s: endpointUUID %@ is not a known HID device, ignoring"
+ "%s: endpointUUID %s is not a valid UUID"
+ "%s: endpointUUID = %s, uarpTransportDomain = %s"
+ "%s: endpointUUID missing from event"
+ "%s: known entrey matching dict %@"
+ "-[UARPHIDManager handleEndpointAssetAvailable:]"
+ "-[UARPHIDManager matchAndStartServiceForKnownEntry:]"
+ "@56@0:8@16@24@32@40@48"
+ "ServiceName"
+ "T@\"NSString\",R,V_serviceName"
+ "VID <%@>, PID <%@>, Serial Number <%@>, UUID <%@>, Service Name <%@>"
+ "_serviceName"
+ "checkDatabaseForKnownVendorID:productID:serialNumber:serviceName:"
+ "com.apple.uarp.endpoint.assetavailable"
+ "com.apple.uarp.endpoint.assetavailable.subscriber"
+ "deviceForUUID:"
+ "handleEndpointAssetAvailable:"
+ "initWithUUIDString:"
+ "initWithVendorID:productID:serialNumber:serviceName:"
+ "initWithVendorID:productID:serialNumber:uuid:serviceName:"
+ "knownDatabaseEntryForUUID:"
+ "matchAndStartServiceForKnownEntry:"
+ "serviceName"
+ "setDeviceTransportDomain:"
+ "startEndpointAssetAvailabilityMatching"
+ "uarpTransportDomain"
- "@40@0:8@16@24@32"
- "VID <%@>, PID <%@>, Serial Number <%@>, UUID <%@>"
- "checkDatabaseForKnownVendorID:productID:serialNumber:"
- "initWithVendorID:productID:serialNumber:"
- "initWithVendorID:productID:serialNumber:uuid:"
```
