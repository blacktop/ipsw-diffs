## rapportd

> `usr/libexec/rapportd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-716.700.11.0.0
-  __TEXT.__text: 0x159960
-  __TEXT.__auth_stubs: 0x33c0
-  __TEXT.__objc_stubs: 0xf560
-  __TEXT.__objc_methlist: 0x76cc
+753.100.1.0.0
+  __TEXT.__text: 0x15b22c
+  __TEXT.__auth_stubs: 0x33d0
+  __TEXT.__objc_stubs: 0xf6c0
+  __TEXT.__objc_methlist: 0x770c
   __TEXT.__const: 0x5e10
-  __TEXT.__cstring: 0x27d46
+  __TEXT.__cstring: 0x282d6
   __TEXT.__objc_classname: 0xddf
   __TEXT.__objc_methtype: 0x3dd1
-  __TEXT.__gcc_except_tab: 0x2180
-  __TEXT.__objc_methname: 0x15f9f
+  __TEXT.__gcc_except_tab: 0x21c8
+  __TEXT.__objc_methname: 0x1618f
   __TEXT.__oslogstring: 0x2b32
   __TEXT.__swift5_typeref: 0x156c
   __TEXT.__swift5_capture: 0xb50

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_acfuncs: 0x104
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4c00
+  __TEXT.__unwind_info: 0x4c48
   __TEXT.__eh_frame: 0x5294
-  __DATA_CONST.__auth_got: 0x19f0
-  __DATA_CONST.__got: 0x940
+  __DATA_CONST.__auth_got: 0x19f8
+  __DATA_CONST.__got: 0x948
   __DATA_CONST.__auth_ptr: 0x5a0
-  __DATA_CONST.__const: 0x72c8
-  __DATA_CONST.__cfstring: 0x5980
+  __DATA_CONST.__const: 0x7370
+  __DATA_CONST.__cfstring: 0x5b40
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x130

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xdb88
-  __DATA.__objc_selrefs: 0x4ad0
+  __DATA.__objc_selrefs: 0x4b30
   __DATA.__objc_ivar: 0xd34
   __DATA.__objc_data: 0x2338
   __DATA.__data: 0x3048

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6673
-  Symbols:   1300
-  CStrings:  8612
+  Functions: 6691
+  Symbols:   1302
+  CStrings:  8661
 
Symbols:
+ _$s14LocalStatusKit16LSKStatusOptionsV10DeviceTypeO13homeAccessoryyA2EmFWC
+ _$s7Network9NWBrowserC10DescriptorO7OptionsV10DeviceTypeV13homeAccessoryAIvgZ
CStrings:
+ " homeAccessory"
+ "### Failed to find multi-user device for identifier %@\n"
+ "### Received multi-user device add event without identifier: %@\n"
+ "### Received multi-user device removed event without identifier: %@\n"
+ "-[RPCompanionLinkDaemon _multiUserDevice:receivedRequestID:request:options:responseHandler:cnx:]"
+ "-[RPCompanionLinkDaemon _multiUserDeviceAdded:connection:responseHandler:]"
+ "-[RPCompanionLinkDaemon _multiUserDeviceAdded:connection:responseHandler:]_block_invoke"
+ "-[RPCompanionLinkDaemon _multiUserDeviceRemoved:connection:]"
+ "-[RPCompanionLinkXPCConnection _effectiveMultiUserDestinationForDestination:]"
+ "Add multi-user active device: %@ from connection %@ altDSID %@\n"
+ "AudioAccessory11,1"
+ "B525ish"
+ "Bonjour unauth peer changed. BLE Address: <%{private}@>, device: %{private}@, changed flags: %#{flags}, found over AWDL: %@\n"
+ "Bonjour unauth peer found. BLE Address: <%{private}@>, device: %{private}@, found over AWDL: %@\n"
+ "Bonjour unauth peer lost <%{private}@>: %{private}@\n"
+ "Connection to %@ is to multi-user destination %@"
+ "EventID '%@' for multi-user device is not allowed on unauthenticated connection"
+ "Found better matching multi-user device='%@'\n"
+ "HomeAccessory"
+ "HomeAccessory17,1"
+ "HomeAccessory17,2"
+ "J490Setup"
+ "J491Setup"
+ "Multi-user device identifier missing"
+ "Multi-user device not found"
+ "Received EventID '%@' for multi-user device '%@'\n"
+ "Received requestID '%@' for multi-user device %@"
+ "Remove multi-user active device ( %@ ) from connection ( %@ )\n"
+ "Replacing existing multi-user device ( %@ ) with new ( %@ ) on %@\n"
+ "Unable to map DirectPeer to destination ID"
+ "_aaltDSID"
+ "_destinationID:matchesMultiUserDeviceOnCnx:"
+ "_effectiveMultiUserDestinationForDestination:"
+ "_idHKU"
+ "_muDI"
+ "_multiDevAdd"
+ "_multiDevRem"
+ "_multiUserDevice:receivedRequestID:request:options:responseHandler:cnx:"
+ "_multiUserDeviceAdded:connection:responseHandler:"
+ "_multiUserDeviceRemoved:connection:"
+ "_multiUserUpdateOptions:withDestination:"
+ "_sigHKU"
+ "_sigPD"
+ "_sigRP"
+ "homeAccessoryVariant"
+ "multiUserDevID"
+ "multiUserDevices"
+ "setMultiUserDevices:"
+ "updateMultiUserDeviceWithPeer:"
+ "v16@?0Q8"
+ "verifyIdentityProof:accountAltDSID:"
+ "verifyMUHomeKitIdentityProof:identifier:accountAltDSID:completion:"
- "Bonjour unauth peer changed. BLE Address: <%@>, device: %@, changed flags: %#{flags}, found over AWDL: %@\n"
- "Bonjour unauth peer found. BLE Address: <%@>, device: %@, found over AWDL: %@\n"
- "Bonjour unauth peer lost <%@>: %@\n"
```
