## bluetoothd

> `usr/sbin/bluetoothd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_classname`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_data`

```diff

-196.5.0.0.0
-  __TEXT.__text: 0x832120
-  __TEXT.__auth_stubs: 0x42e0
-  __TEXT.__objc_stubs: 0x139e0
+196.5.0.3.0
+  __TEXT.__text: 0x837404
+  __TEXT.__auth_stubs: 0x4320
+  __TEXT.__objc_stubs: 0x13a80
   __TEXT.__init_offsets: 0x5c
-  __TEXT.__objc_methlist: 0x7a74
-  __TEXT.__gcc_except_tab: 0x67204
-  __TEXT.__const: 0x846c
-  __TEXT.__cstring: 0xb0ab6
-  __TEXT.__oslogstring: 0xaf743
-  __TEXT.__objc_methname: 0x18649
+  __TEXT.__objc_methlist: 0x7aa4
+  __TEXT.__gcc_except_tab: 0x67664
+  __TEXT.__const: 0x864c
+  __TEXT.__cstring: 0xb10f8
+  __TEXT.__oslogstring: 0xafd8d
+  __TEXT.__objc_methname: 0x18727
   __TEXT.__objc_classname: 0x769
   __TEXT.__objc_methtype: 0x4080
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x70
-  __TEXT.__unwind_info: 0x219b0
-  __DATA_CONST.__auth_got: 0x2188
+  __TEXT.__unwind_info: 0x21b20
+  __DATA_CONST.__auth_got: 0x21a8
   __DATA_CONST.__got: 0x8b0
   __DATA_CONST.__auth_ptr: 0x1e8
-  __DATA_CONST.__const: 0x2e5a0
-  __DATA_CONST.__cfstring: 0x21600
+  __DATA_CONST.__const: 0x2e7c8
+  __DATA_CONST.__cfstring: 0x21720
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x190
-  __DATA_CONST.__objc_intobj: 0x900
-  __DATA_CONST.__objc_arraydata: 0x3f8
+  __DATA_CONST.__objc_intobj: 0x930
+  __DATA_CONST.__objc_arraydata: 0x400
   __DATA_CONST.__objc_dictobj: 0x348
-  __DATA_CONST.__objc_arrayobj: 0x180
-  __DATA.__objc_const: 0xd388
-  __DATA.__objc_selrefs: 0x5b48
-  __DATA.__objc_ivar: 0xef4
+  __DATA_CONST.__objc_arrayobj: 0x198
+  __DATA.__objc_const: 0xd3e0
+  __DATA.__objc_selrefs: 0x5b70
+  __DATA.__objc_ivar: 0xefc
   __DATA.__objc_data: 0x1590
-  __DATA.__data: 0x46e0
+  __DATA.__data: 0x46e8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1fdb2
+  __DATA.__bss: 0x1fdca
   __DATA.__common: 0x15170
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio

   - /usr/lib/libiconv.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 33437
-  Symbols:   1364
-  CStrings:  37929
+  Functions: 33509
+  Symbols:   1368
+  CStrings:  38006
 
Symbols:
+ _amfi_interface_query_bootarg_state
+ _xpc_array_create_empty
+ _xpc_connection_set_peer_lightweight_code_requirement
+ _xpc_dictionary_create_empty
CStrings:
+ "### Connect L2CAP offload start failed: %@"
+ "### L2CAP offload connectOffloadCallback init device failed: %@"
+ "$query"
+ "-[CBDaemonXPCConnection _xpcCBConnectionActivate:]_block_invoke_3"
+ "-[CBStackControllerBTStack connectDataOffloadWithCBConnection:completionHandler:]"
+ "-[CBStackControllerBTStack connectDataOffloadWithCBConnection:completionHandler:]_block_invoke"
+ "-[CBStackControllerBTStack connectDataOffloadWithCBConnection:completionHandler:]_block_invoke_2"
+ "/Library/Application Support/BTServer/countryCodeATV5.0.plist"
+ "/Library/Application Support/BTServer/countryCodes0x202B.plist"
+ "245b126d262dfe728b314ee4d1d1091bf7b406c8b7edd85b798173be285059e0"
+ "74f61a772a9da1812f68ab5854db675447cde80c20675e52a70ac43a7601865d"
+ "Adaptive Controls Manager Message Received from device \"%{public}s\", len -> %u"
+ "AdaptiveControlsManager"
+ "Apple TV"
+ "BD_VSC_SET_DATA_OFFLOAD"
+ "BT chip support for L2CAP Offload : %s"
+ "Connect L2CAP offload failed %@"
+ "Connect L2CAP offload start: %@"
+ "Connect L2CAP offload with invalid use case %s"
+ "Connecting L2CAP offload channel for device %{public}s"
+ "Device %{public}s Adaptive Controls Manager msg received, len: %d"
+ "Disconnecting L2CAP offload channel for device %{public}s"
+ "EnableL2CAPOffload"
+ "Failed setting peer LWCR on cloudkit.xpc service (%d); not registering listener"
+ "Fragmented frame overflow: offset=%zu len=%zu cap=%zu, dropping frame"
+ "GET_ELEMENT_ATTRIBUTES numAttr %d exceeds buffer capacity %d"
+ "J490Setup"
+ "J491Setup"
+ "KatsuraA"
+ "L2CAP offload No device ID"
+ "L2CAP offload No use case"
+ "L2CAP offload already connected for device %{public}s"
+ "L2CAP offload channel VSC failed result:%d"
+ "L2CAP offload channel cleanup for device %{public}s"
+ "L2CAP offload channel connected for device %{public}s cid:0x%x result:%d"
+ "L2CAP offload channel disconnected for device %{public}s with CID 0x%x reason %d"
+ "L2CAP offload channel disconnected for unknown CID 0x%x expected 0x%x reason %d"
+ "L2CAP offload connectOffloadCallback %@, result %@"
+ "L2CAP offload for device %{public}s already connected with CID 0x%x"
+ "L2CAP offload not supported"
+ "L2CAP offload timed out"
+ "Mask gattName as Apple TV in gattDatabaseAccessedCb"
+ "Mask name as Apple TV in notifyHostnameChanged"
+ "Mask productType as Apple TV in readHostname"
+ "Mask productType as Apple TV in readProductType"
+ "MaskLocalNameAsAppleTV"
+ "MatsuA"
+ "MatsuB"
+ "OI_STATUS _ACI_SetDataOffload(uint16_t, uint16_t, _Bool, _Bool, BT_VSC_COMPLETE_CB)"
+ "OI_STATUS _BCM_SetDataOffload(uint16_t, uint16_t, _Bool, _Bool, BT_VSC_COMPLETE_CB)"
+ "Overriding L2CAP Offload=%d"
+ "Policy enforcement stalled for %: (%d deciseconds), force-disconnecting ACL"
+ "Set Data Offload callback status=%d"
+ "Skipping scan prioritization over WiFi (highest agent scan percent:%d%%)"
+ "Support for L2CAP Offload is %s"
+ "TC,N,V_secureSensorCapability"
+ "VAR32 length %u exceeds maximum"
+ "WhitepineA"
+ "_additionalCBUseCaseList"
+ "_secureSensorCapability"
+ "accessory"
+ "bbb07f3ec1b610c6e72cd1cbb77b3971c9ad7a8c03a609b7d00a1854e9eee042"
+ "cloudkit.xpc peer LWCR %s (AMFI enforcing: %s)"
+ "connectDataOffloadWithCBConnection:completionHandler:"
+ "entitlements"
+ "installed"
+ "nearbyActionColorCode"
+ "not enforced"
+ "sccp"
+ "secureSensorCapability"
+ "sendAdaptiveControlsManagerMessage: Failed to send Adaptive Controls Message with status = %{bluetooth:OI_STATUS}u"
+ "sendAdaptiveControlsManagerMessage: Sending Adaptive Controls Message of length %u to %{private, mask.hash}s"
+ "sendAdaptiveControlsManagerMessage: Stack not ready"
+ "setSecureSensorCapability:"
+ "useCaseClientIDs"
+ "v20@?0^v8i16"
+ "validation-category"
```
