## FindMyBluetooth

> `/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth`

```diff

-62.33.10.29.3
-  __TEXT.__text: 0xa7c5c
-  __TEXT.__auth_stubs: 0x14b0
-  __TEXT.__objc_methlist: 0x148
-  __TEXT.__swift5_typeref: 0x1692
-  __TEXT.__cstring: 0x19ba
-  __TEXT.__swift5_reflstr: 0x16f7
-  __TEXT.__swift5_assocty: 0x560
-  __TEXT.__const: 0x3a38
-  __TEXT.__constg_swiftt: 0x1a20
-  __TEXT.__swift5_fieldmd: 0x1154
+62.34.7.11.22
+  __TEXT.__text: 0xa5194
+  __TEXT.__auth_stubs: 0x1590
+  __TEXT.__objc_methlist: 0x4cc
+  __TEXT.__swift5_typeref: 0x178c
+  __TEXT.__cstring: 0x181a
+  __TEXT.__swift5_reflstr: 0x18d7
+  __TEXT.__swift5_assocty: 0x5c0
+  __TEXT.__const: 0x41e8
+  __TEXT.__constg_swiftt: 0x1bc8
+  __TEXT.__swift5_fieldmd: 0x1394
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_proto: 0x330
-  __TEXT.__swift5_types: 0xfc
-  __TEXT.__swift5_capture: 0x7b0
-  __TEXT.__swift5_protos: 0x20
-  __TEXT.__oslogstring: 0x18c3
+  __TEXT.__swift5_proto: 0x380
+  __TEXT.__swift5_types: 0x110
+  __TEXT.__swift5_capture: 0x7c8
+  __TEXT.__swift_as_entry: 0x4c8
+  __TEXT.__swift_as_ret: 0x3c0
+  __TEXT.__swift5_protos: 0x24
+  __TEXT.__oslogstring: 0x1b5f
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x2ee8
-  __TEXT.__eh_frame: 0x8d40
-  __TEXT.__objc_classname: 0x6e
-  __TEXT.__objc_methname: 0xf7a
+  __TEXT.__unwind_info: 0x2f58
+  __TEXT.__eh_frame: 0x9678
+  __TEXT.__objc_classname: 0x7c
+  __TEXT.__objc_methname: 0x1033
   __TEXT.__objc_methtype: 0x7a6
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x278
-  __DATA_CONST.__objc_classlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a8
-  __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0xa58
-  __AUTH_CONST.__auth_ptr: 0x698
-  __AUTH_CONST.__const: 0x20b8
-  __AUTH_CONST.__objc_const: 0x1f78
+  __DATA_CONST.__objc_selrefs: 0x498
+  __DATA_CONST.__objc_protorefs: 0x30
+  __AUTH_CONST.__auth_got: 0xac8
+  __AUTH_CONST.__auth_ptr: 0x720
+  __AUTH_CONST.__const: 0x2540
+  __AUTH_CONST.__objc_const: 0x19f8
   __AUTH.__objc_data: 0x4a0
-  __AUTH.__data: 0x1338
-  __DATA.__data: 0x1ea0
-  __DATA.__bss: 0x5d80
-  __DATA.__common: 0x120
+  __AUTH.__data: 0x1468
+  __DATA.__data: 0x20e8
+  __DATA.__bss: 0x6780
+  __DATA.__common: 0x140
   __DATA_DIRTY.__objc_data: 0x208
-  __DATA_DIRTY.__data: 0x1198
+  __DATA_DIRTY.__data: 0x11e0
   __DATA_DIRTY.__bss: 0x880
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2875
-  Symbols:   226
-  CStrings:  513
+  Functions: 2919
+  Symbols:   265
+  CStrings:  539
 
Symbols:
+ _OBJC_CLASS_$_CBController
+ _OBJC_CLASS_$_CBDevice
+ __xpc_event_key_name
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
+ _swift_unknownObjectRelease_n
+ _swift_unknownObjectRetain_n
+ _xpc_dictionary_get_dictionary
+ _xpc_dictionary_get_string
+ _xpc_set_event_stream_handler
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
CStrings:
+ " manufacturerData:"
+ "%s"
+ "%s %{public}s"
+ "%s %{public}s!"
+ "%s Failed to init Device with error: %{public}@"
+ "%s Missing underlying CBDevice!"
+ "%s scanRate:%{public}s rssiThreshold:%{public}s"
+ "%s: didUpdateValue %s"
+ "%{public}s"
+ ".proximityPairingBuffer"
+ "Discovered device with out of range RSSI: %s"
+ "Discovered device with unknown RSSI: %s"
+ "Failed to create CBDevice %{public}@"
+ "No rssiThreshold %s - yield discovered device: %s"
+ "OS_xpc_object"
+ "Received accessory discovery %s"
+ "Unable to get CBDevice dict from %s"
+ "Unable to get event type from %s"
+ "Unsupported event type %s"
+ "Using classic/public btAddressData: %s with type: %s"
+ "_TtC15FindMyBluetooth10Controller"
+ "bleAddressData"
+ "bleAddressData is available: %s"
+ "bleAddressData: %s"
+ "bleChannel"
+ "bleScanRate"
+ "com.apple.bluetooth.discovery"
+ "deleteDevice:completion:"
+ "device"
+ "devicesWithDiscoveryFlags:error:"
+ "eventType"
+ "init(scanRate:rssiThreshold:)"
+ "initWithXPCEventRepresentation:error:"
+ "model"
+ "name"
+ "productID"
+ "proximityPairingBuffer"
+ "rssiThreshold"
+ "scanRate"
+ "setBleScanRate:"
+ "subscribeToAttributesChanges()"
+ "subscribeToXPCDiscoveryEvents(for:)"
+ "v16@?0@\"<OS_xpc_object>\"8"
+ "vendorID"
- " manufacturerData: "
- "%s: didUpdateValue"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"
- "manufacturerData"

```
