## com.apple.accessoryd.matching

> `/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA.__const`
- `__DATA.__objc_classlist`
- `__DATA.__objc_catlist`
- `__DATA.__objc_protolist`
- `__DATA.__objc_const`
- `__DATA.__objc_protorefs`
- `__DATA.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__objc_arraydata`
- `__DATA.__objc_arrayobj`
- `__DATA.__objc_intobj`
- `__DATA.__data`
- `__DATA.__objc_dictobj`
- `__DATA.__auth_ptr`

```diff

-1219.42.3.0.0
-  __TEXT.__text: 0x373bc
+1219.60.10.0.0
+  __TEXT.__text: 0x3743c
   __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_stubs: 0x50c0
+  __TEXT.__objc_stubs: 0x5100
   __TEXT.__objc_methlist: 0x23ac
-  __TEXT.__cstring: 0x505b
-  __TEXT.__objc_methname: 0x6ed9
+  __TEXT.__cstring: 0x5064
+  __TEXT.__objc_methname: 0x6ee3
   __TEXT.__objc_classname: 0x27f
   __TEXT.__objc_methtype: 0xaeb
-  __TEXT.__const: 0x228
-  __TEXT.__oslogstring: 0x3f71
+  __TEXT.__const: 0x230
+  __TEXT.__oslogstring: 0x3fb6
   __TEXT.__gcc_except_tab: 0x404
   __TEXT.__ustring: 0x18
   __TEXT.__unwind_info: 0xf18
   __DATA.__const: 0x1150
-  __DATA.__cfstring: 0x3a80
+  __DATA.__cfstring: 0x3aa0
   __DATA.__objc_classlist: 0xb0
   __DATA.__objc_catlist: 0x10
   __DATA.__objc_protolist: 0x48
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x3cb0
-  __DATA.__objc_selrefs: 0x1a30
+  __DATA.__objc_selrefs: 0x1a38
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_superrefs: 0xa8
   __DATA.__objc_ivar: 0x38c

   __DATA.__data: 0x39e
   __DATA.__objc_dictobj: 0x28
   __DATA.__auth_got: 0x810
-  __DATA.__got: 0x388
+  __DATA.__got: 0x390
   __DATA.__auth_ptr: 0x18
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 1494
-  Symbols:   3087
-  CStrings:  2513
+  Symbols:   3090
+  CStrings:  2515
 
Symbols:
+ _BluetoothAvailabilityChangedNotification
+ _BluetoothPowerChangedNotification
+ _objc_msgSend$available
+ _objc_msgSend$name
- _BluetoothStateChangedNotification
Functions:
~ ___24-[BluetoothSetting init]_block_invoke : 292 -> 300
~ -[BluetoothSetting btSettingChanged:] : 692 -> 812
CStrings:
+ "Registered for BluetoothAvailability/PowerChangedNotification"
+ "Unregistered for BluetoothAvailability/PowerChangedNotification: bluetoothEnabled = %d"
+ "available"
+ "btSettingChanged: %{public}@ bluetoothEnabled = %d -> %d"
+ "btSettingChanged: bluetoothd not available, keep bluetoothEnabled = %d (initComplete %d)"
+ "catch-up"
- "Registered for BluetoothStateChangedNotification: bluetoothEnabled = %d"
- "Unregistered for BluetoothStateChangedNotification: bluetoothEnabled = %d"
- "btSettingChanged: bluetoothEnabled = %d -> %d"
- "btSettingChanged: powerState = %d"
```
