## tvremoted

> `/usr/libexec/tvremoted`

```diff

-548.10.21.0.0
-  __TEXT.__text: 0x104f8
+548.10.23.0.0
+  __TEXT.__text: 0x1081c
   __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0x2500
-  __TEXT.__objc_methlist: 0xf00
-  __TEXT.__const: 0xd2
-  __TEXT.__oslogstring: 0x24eb
+  __TEXT.__objc_methlist: 0xef0
+  __TEXT.__const: 0xda
+  __TEXT.__oslogstring: 0x267c
   __TEXT.__cstring: 0x83e
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__objc_methname: 0x31f7
+  __TEXT.__objc_methname: 0x3147
   __TEXT.__objc_classname: 0x14a
   __TEXT.__objc_methtype: 0xe81
   __TEXT.__unwind_info: 0x350
   __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x638
+  __DATA_CONST.__const: 0x660
   __DATA_CONST.__cfstring: 0x6c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0xe78
-  __DATA.__objc_selrefs: 0xc78
-  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_const: 0xe48
+  __DATA.__objc_selrefs: 0xc70
+  __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360
   __DATA.__bss: 0x40

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4BCE190E-8D99-39D8-809E-E794603921D4
+  UUID: F685670D-6242-3D98-94DC-9386DBDBD6FB
   Functions: 314
   Symbols:   2369
-  CStrings:  945
+  CStrings:  947
 
Symbols:
+ -[TVRDServer _findCachedDeviceForIdentifier:]
+ GCC_except_table95
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ _objc_msgSend$_findCachedDeviceForIdentifier:
+ _objc_msgSend$isEqual:
- -[TVRDServer informDeviceQueryObserversWithUpdatedSuggestions]
- -[TVRDServer setInformDeviceQueryObserversWithUpdatedSuggestions:]
- GCC_except_table94
- OBJC_IVAR_$_TVRDServer._informDeviceQueryObserversWithUpdatedSuggestions
- _objc_msgSend$informDeviceQueryObserversWithUpdatedSuggestions
- _objc_msgSend$setInformDeviceQueryObserversWithUpdatedSuggestions:
CStrings:
+ "After adding interested device to cachedDevices: %@"
+ "Could not find cached device with ID %{public}@, even though someone is already interested in that device. All cachedDevices - %{public}@"
+ "Device identifiers interested to connect: %{public}@"
+ "Existing cachedDevices: %{public}@"
+ "No cached device found with identifier: %{public}@. All cachedDevices - %{public}@"
+ "No cached device found with identifier: %{public}@. cachedDevices - %{public}@"
+ "Replaced cached device: %{public}@ with device: %{public}@. cachedDevices: %{public}@"
+ "Sending inputDataPayload: %{public}@ to device: %{public}@ from: %{public}@"
+ "Server lost interest in %{public}@, disconnecting and removing device %{public}@ from cachedDevices: %{public}@"
+ "Updated cachedDevices:%{public}@"
+ "_findCachedDeviceForIdentifier:"
+ "cachedDevices: %{public}@ _deviceIdentifiers: %{public}@"
- "Cached devices: %@ _deviceIdentifiers: %@"
- "Could not find cached device with ID %@, even though someone is already interested in that device. All cached devices - %@"
- "Device identifiers interested to connect: %@"
- "Existing cached devices: %@"
- "No cached device found with identifier: %{public}@. All cached devices - %{public}@"
- "Server lost interest in %{public}@, calling -disconnect on TVRCDevice %{public}@"
- "TB,N,V_informDeviceQueryObserversWithUpdatedSuggestions"
- "_informDeviceQueryObserversWithUpdatedSuggestions"
- "informDeviceQueryObserversWithUpdatedSuggestions"
- "setInformDeviceQueryObserversWithUpdatedSuggestions:"

```
