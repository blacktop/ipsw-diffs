## RemoteHID

> `/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID`

```diff

 224.40.2.0.0
-  __TEXT.__text: 0xab68
+  __TEXT.__text: 0xab30
   __TEXT.__objc_methlist: 0x550
   __TEXT.__const: 0x260
   __TEXT.__gcc_except_tab: 0x5f4
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ -[HIDRemoteEndpoint getDevice:] : 124 -> 120
~ -[HIDRemoteEndpoint addDevice:] : 212 -> 208
~ -[HIDRemoteEndpoint _removeDeviceID:] : 352 -> 348
~ -[HIDRemoteEndpoint removeAllDevices] : 276 -> 272
~ -[HIDRemoteEndpoint logRemovedDevice:] : 148 -> 144
~ -[HIDRemoteEndpoint copyState] : 328 -> 324
~ -[HIDRemoteEndpoint devices] : 76 -> 72
~ -[HIDRemoteDeviceServer endpoints] : 76 -> 72
~ -[HIDRemoteDeviceServer getEndpoint:] : 124 -> 120
~ -[HIDRemoteDeviceServer connectEndpoint:] : 192 -> 188
~ -[HIDRemoteDeviceServer _disconnectEndpointID:] : 216 -> 212
~ -[HIDRemoteDeviceServer disconnectAll] : 144 -> 140
~ -[HIDRemoteDeviceServer getRefreshCountForEndpoint:deviceID:] : 344 -> 340
~ -[HIDRemoteDeviceServer setRefreshCountForEndpoint:deviceID:count:] : 384 -> 380
```
