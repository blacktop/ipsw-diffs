## DualSenseHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/DualSenseHIDServicePlugin.plugin/DualSenseHIDServicePlugin`

```diff

-13.0.36.0.0
-  __TEXT.__text: 0xb394
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0x1720
+13.0.39.0.0
+  __TEXT.__text: 0xb64c
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0x1740
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xd54
-  __TEXT.__cstring: 0x7bd
+  __TEXT.__cstring: 0x7d8
   __TEXT.__objc_classname: 0x2ed
-  __TEXT.__objc_methname: 0x2571
+  __TEXT.__objc_methname: 0x2586
   __TEXT.__objc_methtype: 0x131c
-  __TEXT.__const: 0x560
-  __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__oslogstring: 0xb5b
+  __TEXT.__const: 0x570
+  __TEXT.__gcc_except_tab: 0x218
+  __TEXT.__oslogstring: 0xc7f
   __TEXT.__unwind_info: 0x328
-  __DATA_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__auth_got: 0x2f8
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x408
-  __DATA_CONST.__cfstring: 0xd40
+  __DATA_CONST.__cfstring: 0xd80
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x1d68
-  __DATA.__objc_selrefs: 0x8f0
+  __DATA.__objc_selrefs: 0x8f8
   __DATA.__objc_ivar: 0x17c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5C8D27FC-1420-3889-8FD9-47DDD63B00CD
+  UUID: E94BCCEE-E11D-32DD-BECF-B6FD94794565
   Functions: 317
-  Symbols:   131
-  CStrings:  895
+  Symbols:   132
+  CStrings:  899
 
Symbols:
+ _IOObjectCopyClass
Functions:
~ sub_28b0 : 908 -> 1308
~ sub_2c3c -> sub_2dcc : 420 -> 488
~ sub_3304 -> sub_34d8 : 288 -> 292
~ sub_3424 -> sub_35fc : 336 -> 356
~ sub_3574 -> sub_3760 : 196 -> 200
~ sub_3638 -> sub_3828 : 380 -> 368
~ sub_384c -> sub_3a30 : 140 -> 200
~ sub_38d8 -> sub_3af8 : 216 -> 276
~ sub_3a28 -> sub_3c84 : 216 -> 220
~ sub_3b00 -> sub_3d60 : 220 -> 236
~ sub_3cb0 -> sub_3f20 : 700 -> 716
~ sub_3f6c -> sub_41ec : 208 -> 224
~ sub_403c -> sub_42cc : 236 -> 252
~ sub_4130 -> sub_43d0 : 192 -> 252
~ sub_42a0 -> sub_457c : 136 -> 196
~ sub_4328 -> sub_4640 : 304 -> 320
~ sub_5b30 -> sub_5e58 : 232 -> 104
~ sub_b248 -> sub_b4f0 : 192 -> 208
CStrings:
+ "Initialize <%{public}@ %#010llx> {\nvendorID = %zu,\nproductID = %zu,\nversion = %zu,\nmanufacturer = '%{public}@',\nproduct = '%{public}@',\nserial = '%{private}@',\ntransport = '%{public}@',\n}"
+ "Manufacturer"
+ "VersionNumber"
+ "[%#010llx] Activate"
+ "[%#010llx] Cancel"
+ "[%#010llx] Creating HIDDevice."
+ "[%#010llx] Dealloc"
+ "[%#010llx] Opening HIDDevice"
+ "[%#010llx] SetCancelHandler"
+ "[%#010llx] SetDispatchQueue"
+ "[%#010llx] SetEventDispatcher"
+ "[%#010llx] clientNotification %@ added: %d"
+ "[%#010llx] creating battery device"
+ "[%#010llx] disconnectIfIdle disconnecting..."
+ "[%#010llx] eventMatching: %@ client: %@"
+ "[%#010llx] isIdle for %.2f seconds%@"
+ "[%#010llx] scheduleIdleTimer"
+ "[%#010llx] setProperty: %@ forKey: %@"
+ "[%#010llx] updateBatteryStats reporting battery level %d%%"
+ "[%#010llx] updateClientBattery reporting battery level %d%%"
+ "unsignedIntegerValue"
- "clientNotification %@ added: %d"
- "connectToBatteryServiceWithClient %@"
- "creating HIDDevice for service %#llx"
- "creating battery device"
- "disconnectIfIdle disconnecting..."
- "eventMatching: %@ client: %@"
- "initWithService: %d"
- "isIdle for %.2f seconds%@"
- "opening HIDDevice"
- "setCancelHandler %p"
- "setDispatchQueue %p"
- "setEventDispatcher %@"
- "setProperty: %@ forKey: %@"
- "updateBatteryStats reporting battery level %d%%"
- "updateClientBattery reporting battery level %d%%"

```
