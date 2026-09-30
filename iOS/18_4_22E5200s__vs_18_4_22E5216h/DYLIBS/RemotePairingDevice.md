## RemotePairingDevice

> `/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice`

```diff

-199.100.14.0.0
-  __TEXT.__text: 0xc7838
+199.100.18.0.0
+  __TEXT.__text: 0xcb11c
   __TEXT.__auth_stubs: 0x2b40
   __TEXT.__objc_methlist: 0x4ac
-  __TEXT.__const: 0xe978
-  __TEXT.__cstring: 0x671c
-  __TEXT.__oslogstring: 0x39ec
+  __TEXT.__const: 0xeb48
+  __TEXT.__cstring: 0x69ec
+  __TEXT.__oslogstring: 0x3b7c
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__constg_swiftt: 0x3970
-  __TEXT.__swift5_typeref: 0x37dc
-  __TEXT.__swift5_reflstr: 0x28b0
-  __TEXT.__swift5_fieldmd: 0x3348
+  __TEXT.__constg_swiftt: 0x3a88
+  __TEXT.__swift5_typeref: 0x381c
+  __TEXT.__swift5_reflstr: 0x2910
+  __TEXT.__swift5_fieldmd: 0x3408
   __TEXT.__swift5_builtin: 0x21c
   __TEXT.__swift5_assocty: 0x258
-  __TEXT.__swift5_proto: 0xad8
-  __TEXT.__swift5_types: 0x3f0
-  __TEXT.__swift5_capture: 0x1b08
+  __TEXT.__swift5_proto: 0xae0
+  __TEXT.__swift5_types: 0x3fc
+  __TEXT.__swift5_capture: 0x1c10
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x188
-  __TEXT.__unwind_info: 0x3df8
-  __TEXT.__eh_frame: 0x3710
+  __TEXT.__unwind_info: 0x3f40
+  __TEXT.__eh_frame: 0x37d0
   __TEXT.__objc_classname: 0x13c
-  __TEXT.__objc_methname: 0xaa4
+  __TEXT.__objc_methname: 0xb60
   __TEXT.__objc_methtype: 0x127
   __TEXT.__objc_stubs: 0x260
-  __DATA_CONST.__got: 0x590
-  __DATA_CONST.__const: 0x7c8
-  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__got: 0x6f8
+  __DATA_CONST.__const: 0x7f8
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f0
+  __DATA_CONST.__objc_selrefs: 0x448
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x15b0
-  __AUTH_CONST.__auth_ptr: 0xc48
-  __AUTH_CONST.__const: 0xae50
+  __AUTH_CONST.__auth_ptr: 0x8e8
+  __AUTH_CONST.__const: 0xb208
   __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0x45e8
+  __AUTH_CONST.__objc_const: 0x46e0
   __AUTH.__objc_data: 0x590
-  __AUTH.__data: 0x18c8
+  __AUTH.__data: 0x1a88
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x26e8
+  __DATA.__data: 0x2738
   __DATA.__bss: 0xd590
   __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__data: 0x1a78
+  __DATA_DIRTY.__objc_data: 0x290
+  __DATA_DIRTY.__data: 0x1ad8
   __DATA_DIRTY.__bss: 0x7400
   __DATA_DIRTY.__common: 0x28
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7448
-  Symbols:   1949
-  CStrings:  1030
+  Functions: 7574
+  Symbols:   1973
+  CStrings:  1059
 
Symbols:
+ _OBJC_CLASS_$_CBReadRequest
+ _OBJC_CLASS_$_CBWriteRequest
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_generic_instantiateLayoutString
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initEnumMetadataSinglePayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
- _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
- _swift_singlePayloadEnumGeneric_getEnumTag
CStrings:
+ "%{public}s: CBConnection activated"
+ "%{public}s: CBConnection failed to activate: %s"
+ "%{public}s: CBConnection interrupted"
+ "%{public}s: CBConnection invalidated"
+ "%{public}s: Connection exceeded maximum permitted duration of %ld seconds. Invalidating connection"
+ "Device did not reply with expected raw public key"
+ "Failed to complete operation over Bluetooth within permitted time limit.."
+ "It is not possible to derive a network hostname from a Bluetooth LE connection"
+ "Read request completion was invoked but neither error nor data is set"
+ "RemotePairingDevice/BluetoothLEConnectionControlChannelTransport.swift"
+ "The bluetooth connection was interrupted"
+ "The bluetooth connection was invalidated"
+ "Updating last seen wire protocol version for peer with UDID %{public}s: %ld -> %ld"
+ "_TtC19RemotePairingDevice44BluetoothLEConnectionControlChannelTransport"
+ "activateWithCompletion:"
+ "data"
+ "hostPreferBTLEConnectionBasedControlChannels"
+ "lastSeenWireProtocolVersion"
+ "maxDurationTimeoutItem"
+ "pairingdatastorageprovider"
+ "readWithCBReadRequest:"
+ "setCompletion:"
+ "setDataArray:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setMaxLength:"
+ "setMinLength:"
+ "writeWithCBWriteRequest:"

```
