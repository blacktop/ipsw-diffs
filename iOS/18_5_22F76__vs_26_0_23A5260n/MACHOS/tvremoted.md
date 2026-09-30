## tvremoted

> `/usr/libexec/tvremoted`

```diff

-496.50.7.0.0
-  __TEXT.__text: 0xf030
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_stubs: 0x23c0
-  __TEXT.__objc_methlist: 0xed0
+548.0.1.0.0
+  __TEXT.__text: 0xf760
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_stubs: 0x2420
+  __TEXT.__objc_methlist: 0xee0
   __TEXT.__const: 0xd2
-  __TEXT.__oslogstring: 0x1fec
-  __TEXT.__cstring: 0x822
+  __TEXT.__oslogstring: 0x2141
+  __TEXT.__cstring: 0x828
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__objc_methname: 0x315f
+  __TEXT.__objc_methname: 0x3179
   __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methtype: 0xe4f
-  __TEXT.__unwind_info: 0x320
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x678
-  __DATA_CONST.__cfstring: 0x680
+  __TEXT.__objc_methtype: 0xe5d
+  __TEXT.__unwind_info: 0x328
+  __DATA_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x658
+  __DATA_CONST.__cfstring: 0x6a0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0xe78
-  __DATA.__objc_selrefs: 0xc40
+  __DATA.__objc_selrefs: 0xc50
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 55CAAFDC-203D-3B19-8174-C7B079B654F2
-  Functions: 295
-  Symbols:   2284
-  CStrings:  909
+  UUID: 042EF70F-FEF9-3E4D-BF0E-B6B4AE64B081
+  Functions: 305
+  Symbols:   2328
+  CStrings:  922
 
Symbols:
+ -[TVRDIRSessionManager _candidateForDevice:createIfNeeded:]
+ -[TVRDIRSessionManager processNewDevices:].cold.1
+ -[TVRDIRSessionManager processNewDevices:].cold.2
+ -[TVRDIRSessionManager processNewDevices:].cold.3
+ -[TVRDIRSessionManager processNewDevices:].cold.4
+ -[TVRDIRSessionManager processNewDevices:].cold.5
+ -[TVRDIRSessionManager removeDevice:].cold.1
+ -[TVRDServer _publishUserPresenceForDevice:]
+ GCC_except_table79
+ GCC_except_table91
+ _OUTLINED_FUNCTION_3
+ _TVRCPublishPresenceEvent
+ __39-[TVRDServer _activateIRSessionManager]_block_invoke.86
+ __39-[TVRDServer _activateIRSessionManager]_block_invoke.86.cold.1
+ __44-[TVRDServer _publishUserPresenceForDevice:]_block_invoke.cold.1
+ ___44-[TVRDServer _publishUserPresenceForDevice:]_block_invoke
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_tvremoted
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_tvremoted
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_tvremoted
+ _objc_msgSend$_candidateForDevice:createIfNeeded:
+ _objc_msgSend$_publishUserPresenceForDevice:
+ _objc_msgSend$_setIdentifier:name:supportedButtons:
+ _objc_msgSend$paired
+ _objc_msgSend$removeDevice:
+ _objc_retain_x24
- -[TVRDIRSessionManager _candidateForDevice:]
- GCC_except_table77
- GCC_except_table89
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.83
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.83.cold.1
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_tvremoted
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_tvremoted
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_tvremoted
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_tvremoted
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_tvremoted
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_tvremoted
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_tvremoted
- _objc_msgSend$_candidateForDevice:
- _objc_msgSend$_setIdentifier:alternateIdentifiers:name:model:supportedButtons:
CStrings:
+ "@28@0:8@16B24"
+ "Added new %{public}@. Total connections: %@"
+ "Adding new candidates %{public}@"
+ "Adding new device: %{public}@"
+ "After processing - identifierToDeviceMap %{public}@"
+ "Before processing - identifierToDeviceMap %{public}@"
+ "Device identifier shouldn't be nil. deviceMap: %{public}@"
+ "Failed to publish user presence %{public}@"
+ "Removing candidate %{public}@"
+ "Removing device %{public}@"
+ "Successfully published user presence %@"
+ "Updated deviceState: %{public}@"
+ "_candidateForDevice:createIfNeeded:"
+ "_publishUserPresenceForDevice:"
+ "_setIdentifier:name:supportedButtons:"
+ "guest"
+ "identifierToDeviceMap %@"
+ "lastKnownDevices: %{public}@"
+ "newDevices: %{public}@"
+ "paired"
- "Added new %{public}@. Total connections: %ld"
- "Delete candidate %@"
- "General device query updated deviceStates %{public}@"
- "New devices %@"
- "Removing candidate %@"
- "Updating candidates %@"
- "_candidateForDevice:"
- "_setIdentifier:alternateIdentifiers:name:model:supportedButtons:"

```
