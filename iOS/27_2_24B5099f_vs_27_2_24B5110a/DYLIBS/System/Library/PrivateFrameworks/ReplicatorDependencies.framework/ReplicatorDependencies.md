## ReplicatorDependencies

> `/System/Library/PrivateFrameworks/ReplicatorDependencies.framework/ReplicatorDependencies`

```diff

-176.2.5.0.0
-  __TEXT.__text: 0x28ca0
+176.2.6.0.0
+  __TEXT.__text: 0x28f04
   __TEXT.__objc_methlist: 0x314
-  __TEXT.__const: 0x1ce4
+  __TEXT.__const: 0x1d14
   __TEXT.__swift5_typeref: 0xbbe
-  __TEXT.__swift5_reflstr: 0x898
+  __TEXT.__swift5_reflstr: 0x8a8
   __TEXT.__swift5_assocty: 0x180
   __TEXT.__constg_swiftt: 0x111c
   __TEXT.__swift5_fieldmd: 0xa5c
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_proto: 0x130
   __TEXT.__swift5_types: 0xac
-  __TEXT.__oslogstring: 0x11e1
+  __TEXT.__oslogstring: 0x1311
   __TEXT.__cstring: 0x5e1
   __TEXT.__swift5_capture: 0x4e0
   __TEXT.__swift_as_entry: 0x28

   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x2210
-  __AUTH_CONST.__objc_const: 0x12c8
+  __AUTH_CONST.__objc_const: 0x12a8
   __AUTH_CONST.__auth_got: 0xba0
   __DATA.__data: 0x260
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x3f0
-  __DATA_DIRTY.__data: 0x1328
+  __DATA_DIRTY.__data: 0x1318
   __DATA_DIRTY.__bss: 0x900
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
Functions:
~ sub_29ed7b298 -> sub_29ff8f298 : 760 -> 764
~ sub_29ed7e9b8 -> sub_29ff929bc : 1508 -> 1520
~ sub_29ed7f984 -> sub_29ff93994 : 152 -> 192
~ sub_29ed83504 -> sub_29ff9753c : 152 -> 192
~ sub_29ed8359c -> sub_29ff975fc : 8 -> 16
~ sub_29ed911c4 -> sub_29ffa522c : 216 -> 224
~ sub_29ed92ab8 -> sub_29ffa6b28 : 48 -> 112
~ sub_29ed93848 -> sub_29ffa78f8 : 1488 -> 1628
~ sub_29ed93e64 -> sub_29ffa7fa0 : 1748 -> 1852
~ sub_29ed94538 -> sub_29ffa86dc : 2492 -> 2620
~ sub_29ed94ef4 -> sub_29ffa9118 : 772 -> 844
~ sub_29ed951f8 -> sub_29ffa9464 : 1880 -> 1996
~ sub_29ed959ec -> sub_29ffa9ccc : 692 -> 768
~ sub_29ed95ca0 -> sub_29ffa9fcc : 4428 -> 4728
~ sub_29ed96e44 -> sub_29ffab29c : 100 -> 92
~ sub_29ed96ea8 -> sub_29ffab2f8 : 112 -> 104
~ sub_29ed97134 -> sub_29ffab57c : 52 -> 116
~ sub_29ed97178 -> sub_29ffab600 : 2704 -> 2452
~ sub_29ed97c08 -> sub_29ffabf94 : 2732 -> 2472
~ sub_29ed98fa0 -> sub_29ffad228 : 36 -> 28
~ sub_29ed9a708 -> sub_29ffae988 : 3160 -> 3092
~ sub_29eda1510 -> sub_29ffb574c : 380 -> 420
CStrings:
+ "%{public}llu:%{private}s: Cannot create NWConnection from nw_connection_t"
+ "%{public}llu:%{private}s: Connection cancelled"
+ "%{public}llu:%{private}s: Connection failed and entered waiting state: %{public}s"
+ "%{public}llu:%{private}s: Connection failed with no reported error"
+ "%{public}llu:%{private}s: Connection failed: %{public}s"
+ "%{public}llu:%{private}s: Connection ready"
+ "%{public}llu:%{private}s: Connection state changed; state: %{public}s"
+ "%{public}llu:%{private}s: Connection state changed; state: %{public}s; error: %{public}s"
+ "%{public}llu:%{private}s: Failed to send file %{public}s error: %{public}s"
+ "%{public}llu:%{private}s: Failed to send message data: %{public}s"
+ "%{public}llu:%{private}s: New outgoing connection created to %{public}s"
+ "%{public}llu:%{private}s: Ready to receive %{public}u bytes"
+ "%{public}llu:%{private}s: Received %{public}ld bytes"
+ "%{public}llu:%{private}s: Received error: %{public}s"
+ "%{public}llu:%{private}s: Received nil data"
+ "%{public}llu:%{private}s: Sending file %{public}s; maximumLength: %{public}ld"
+ "%{public}llu:%{private}s: Sent %{public}ld bytes"
+ "%{public}llu:%{private}s: Sent file %{public}s; maximumLength: %{public}ld; totalBytesSent: %{public}ld"
+ "%{public}llu:%{private}s: Starting connection"
+ "%{public}s: %{public}s %{private}s will be used for connection: %{public}s"
+ "%{public}s: Browser found device with ID: %{private}s; name: %{private}s; isMeDevice: %{bool,public}d"
+ "%{public}s: Monitor found remote device with ID %{private}s but it is not the 'me' device"
+ "%{public}s: Monitor found remote device with ID: %{private}s"
+ "%{public}s: Received new connection: %{public}s: DeviceID: %{private}s"
+ "%{public}s: Unable to get DeviceID from connection: %{public}s: Using uuidString %{private}s instead"
+ "Fetched IDS device: %{private}s; isCloudPaired: %{bool,public}d"
+ "Finding active paired device in devices: %{private}s"
+ "IDS PairedDevice is %{private}s"
+ "Updating paired device from %{private}s to %{private}s"
+ "[?:%{private}s]: Creating %{public}s connection for %{public}s"
- "%{public}s: %{public}s %{public}s will be used for connection: %{public}s"
- "%{public}s: Browser found device with ID: %{public}s; name: %{public}s; isMeDevice: %{bool,public}d"
- "%{public}s: Cannot create NWConnection from nw_connection_t"
- "%{public}s: Connection cancelled"
- "%{public}s: Connection failed and entered waiting state: %{public}s"
- "%{public}s: Connection failed with no reported error"
- "%{public}s: Connection failed: %{public}s"
- "%{public}s: Connection ready"
- "%{public}s: Connection state changed; state: %{public}s"
- "%{public}s: Connection state changed; state: %{public}s; error: %{public}s"
- "%{public}s: Failed to send file %{public}s error: %{public}s"
- "%{public}s: Failed to send message data: %{public}s"
- "%{public}s: Monitor found remote device with ID %{public}s but it is not the 'me' device"
- "%{public}s: Monitor found remote device with ID: %{public}s"
- "%{public}s: New outgoing connection created to %{public}s; deviceID: %{public}s"
- "%{public}s: Ready to receive %u bytes"
- "%{public}s: Received %{public}ld bytes"
- "%{public}s: Received error: %{public}s"
- "%{public}s: Received new connection: %{public}s: DeviceID: %{public}s"
- "%{public}s: Received nil data"
- "%{public}s: Sending file %{public}s; maximumLength: %{public}ld"
- "%{public}s: Sent %ld bytes"
- "%{public}s: Sent file %{public}s; maximumLength: %{public}ld; totalBytesSent: %{public}ld"
- "%{public}s: Starting connection"
- "%{public}s: Unable to get DeviceID from connection: %{public}s: Using uuidString %{public}s instead"
- "Fetched IDS device: %{public}s; isCloudPaired: %{bool,public}d"
- "Finding active paired device in devices: %{public}s"
- "IDS PairedDevice is %{public}s"
- "Updating paired device from %{public}s to %{public}s"
- "[?:%s]: Creating %s connection for %{public}s"
```
