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
-  __TEXT.__text: 0x485c
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x39c
+1587.2.2.0.0
+  __TEXT.__text: 0x5230
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_stubs: 0xc20
+  __TEXT.__objc_methlist: 0x3dc
   __TEXT.__const: 0x50
-  __TEXT.__objc_methname: 0xd01
-  __TEXT.__cstring: 0x6f7
-  __TEXT.__oslogstring: 0x79f
+  __TEXT.__cstring: 0x7e8
+  __TEXT.__objc_methname: 0xe1b
+  __TEXT.__oslogstring: 0x8be
   __TEXT.__objc_classname: 0x6f
-  __TEXT.__objc_methtype: 0x253
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__const: 0x120
-  __DATA_CONST.__cfstring: 0x740
+  __TEXT.__objc_methtype: 0x259
+  __TEXT.__unwind_info: 0x188
+  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__cfstring: 0x7e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__auth_got: 0x2c0
   __DATA_CONST.__got: 0xc0
-  __DATA.__objc_const: 0x978
-  __DATA.__objc_selrefs: 0x370
-  __DATA.__objc_ivar: 0xbc
+  __DATA.__objc_const: 0x9a8
+  __DATA.__objc_selrefs: 0x3b0
+  __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 136
-  Symbols:   117
-  CStrings:  351
+  Functions: 148
+  Symbols:   118
+  CStrings:  373
 
Symbols:
+ _objc_retain_x24
+ _objc_retain_x26
- _objc_retain_x25
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
