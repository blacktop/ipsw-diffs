## remotepairingd

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/XPCServices/remotepairingd.xpc/Contents/MacOS/remotepairingd`

```diff

-199.60.1.0.0
-  __TEXT.__text: 0x805dc
-  __TEXT.__auth_stubs: 0x31c0
+199.100.20.0.0
+  __TEXT.__text: 0x7a65c
+  __TEXT.__auth_stubs: 0x3270
   __TEXT.__objc_stubs: 0x80
-  __TEXT.__objc_methlist: 0x5c
-  __TEXT.__const: 0x1638
-  __TEXT.__oslogstring: 0x477f
-  __TEXT.__cstring: 0x558f
-  __TEXT.__objc_methname: 0x51a
-  __TEXT.__swift5_typeref: 0x15e2
+  __TEXT.__objc_methlist: 0x1b4
+  __TEXT.__const: 0x1608
+  __TEXT.__oslogstring: 0x499f
+  __TEXT.__cstring: 0x53ca
+  __TEXT.__objc_methname: 0x534
+  __TEXT.__swift5_typeref: 0x153c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x163c
+  __TEXT.__constg_swiftt: 0x1618
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0xe79
-  __TEXT.__swift5_fieldmd: 0xb70
+  __TEXT.__swift5_reflstr: 0xe59
+  __TEXT.__swift5_fieldmd: 0xb14
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_capture: 0xba8
+  __TEXT.__swift5_capture: 0xbc8
   __TEXT.__swift5_proto: 0xc8
-  __TEXT.__swift5_types: 0xa8
+  __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_mpenum: 0x2c
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x12b8
-  __TEXT.__eh_frame: 0x1238
-  __DATA_CONST.__auth_got: 0x18e8
-  __DATA_CONST.__got: 0x758
-  __DATA_CONST.__auth_ptr: 0x728
-  __DATA_CONST.__const: 0x2008
+  __TEXT.__unwind_info: 0x12c0
+  __TEXT.__eh_frame: 0x1288
+  __DATA_CONST.__auth_got: 0x1940
+  __DATA_CONST.__got: 0x770
+  __DATA_CONST.__auth_ptr: 0x660
+  __DATA_CONST.__const: 0x1fb0
   __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x1908
-  __DATA.__objc_selrefs: 0x1b8
+  __DATA.__objc_selrefs: 0x258
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x80
-  __DATA.__objc_data: 0x680
-  __DATA.__data: 0x2ce9
+  __DATA.__objc_classrefs: 0x88
+  __DATA.__objc_data: 0x3f0
+  __DATA.__data: 0x2c59
   __DATA.__s_async_hook: 0x190
   __DATA.__swift56_hooks: 0xb0
   __DATA.__common: 0x148

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFoundation.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNetwork.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 481BF680-4962-323D-8F06-B242E2A9C9C1
-  Functions: 2510
-  Symbols:   365
-  CStrings:  872
+  UUID: AEC9B3C0-800D-351A-BEC1-604DFBB4C3BA
+  Functions: 2460
+  Symbols:   368
+  CStrings:  866
 
Symbols:
+ _NSLocalizedRecoverySuggestionErrorKey
+ _OBJC_CLASS_$_CBConnection
+ __RPIsDarwinOS
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftQuartzCore
- _NSClassFromString
- _os_variant_is_darwinos
CStrings:
+ "%{public}s: Cancelling tunnel bringup attempt because it exceeded maximum permitted time: %{public}s"
+ "%{public}s: attempting to bringup tunnel connectivity over BLE using BT device %s"
+ "%{public}s: will use LE connection for tunnel bringup"
+ "%{public}s: will use NearbyAction (type 21) bluetooth advert for tunnel bringup (deviceSupportsBTLEBringup=%{bool}d, hostOSSupportsBTLEBringup=%{bool}d, preferBTLEBringup=%{bool}d"
+ "Control channel connection was invalidated while attempting to establish tunnel connection"
+ "ControlChannelConnection %{public}s failed to update last seen wire protocol version on pairing record: %s"
+ "DeveloperModeStatus"
+ "Ensure no network firewall configuration is preventing connections from being established to the device."
+ "Ensure the device is accessible from this machine over an infrastructure network, or ensure WiFi is enabled on both machines."
+ "Ensure the device is paired with this machine."
+ "Failed to fetch developer mode status: %{public}s"
+ "The device rejected the connection request."
+ "The device reported that it is not paired with this machine"
+ "Timed out while attempting to establish tunnel using negotiated network parameters."
+ "Timed out while attempting to negotiate tunnel parameters"
+ "Unable to fetch sysctl "
+ "Unable to obtain an endpoint to connect to the device's tunnel listener"
+ "com.apple.security.mac.amfi"
+ "security.mac.amfi.developer_mode_status"
+ "setBlePSM:"
+ "setPeerDevice:"
+ "usbmuxd-543"
- "%{public}s: Cancelling tunnel bringup attempt because it exceeded maximum permitted time."
- "Bluetooth-initiated connections are only supported in macOS 12 and later."
- "Control channel connection was invalidated while creating tunnel connection"
- "Device did not reply with expected raw public key"
- "Index out of range"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Range requires lowerBound <= upperBound"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Timed out attempting to establish tunnel to the device."
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "com.apple.RemotePairing"
- "invalid Collection: less than 'count' elements in collection"
- "usbmuxd-540.80.1"

```
