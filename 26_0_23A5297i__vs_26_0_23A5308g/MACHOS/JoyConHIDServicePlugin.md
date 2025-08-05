## JoyConHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/JoyConHIDServicePlugin.plugin/JoyConHIDServicePlugin`

```diff

-13.0.36.0.0
-  __TEXT.__text: 0x15b3c
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_stubs: 0x19a0
+13.0.39.0.0
+  __TEXT.__text: 0x15df4
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_stubs: 0x19c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xdac
-  __TEXT.__cstring: 0xba9
+  __TEXT.__cstring: 0xbb7
   __TEXT.__objc_classname: 0x2ec
-  __TEXT.__objc_methname: 0x2611
+  __TEXT.__objc_methname: 0x2626
   __TEXT.__objc_methtype: 0x168e
-  __TEXT.__const: 0x1d4
-  __TEXT.__gcc_except_tab: 0x1c94
-  __TEXT.__oslogstring: 0x15c3
+  __TEXT.__const: 0x1dc
+  __TEXT.__gcc_except_tab: 0x1cb0
+  __TEXT.__oslogstring: 0x16e7
   __TEXT.__unwind_info: 0x938
-  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x700
-  __DATA_CONST.__cfstring: 0x1240
+  __DATA_CONST.__cfstring: 0x1260
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x1b60
-  __DATA.__objc_selrefs: 0x980
+  __DATA.__objc_selrefs: 0x988
   __DATA.__objc_ivar: 0x168
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9B725763-8A11-38E2-8197-B1A6E9A3C0DA
+  UUID: 39C1CE67-570A-3A77-929A-2D90FDCC8354
   Functions: 500
-  Symbols:   148
-  CStrings:  1051
+  Symbols:   149
+  CStrings:  1053
 
Symbols:
+ _IOObjectCopyClass
Functions:
~ sub_1730 : 908 -> 1308
~ sub_1abc -> sub_1c4c : 420 -> 488
~ sub_2184 -> sub_2358 : 288 -> 292
~ sub_22a4 -> sub_247c : 336 -> 356
~ sub_23f4 -> sub_25e0 : 196 -> 200
~ sub_24b8 -> sub_26a8 : 380 -> 368
~ sub_26cc -> sub_28b0 : 140 -> 200
~ sub_2758 -> sub_2978 : 216 -> 276
~ sub_28a8 -> sub_2b04 : 216 -> 220
~ sub_2980 -> sub_2be0 : 220 -> 236
~ sub_2b30 -> sub_2da0 : 700 -> 716
~ sub_2dec -> sub_306c : 208 -> 224
~ sub_2ebc -> sub_314c : 236 -> 252
~ sub_2fb0 -> sub_3250 : 192 -> 252
~ sub_3120 -> sub_33fc : 136 -> 196
~ sub_31a8 -> sub_34c0 : 304 -> 320
~ sub_49b0 -> sub_4cd8 : 232 -> 104
~ sub_1412c -> sub_143d4 : 192 -> 208
CStrings:
+ "Initialize <%{public}@ %#010llx> {\nvendorID = %zu,\nproductID = %zu,\nversion = %zu,\nmanufacturer = '%{public}@',\nproduct = '%{public}@',\nserial = '%{private}@',\ntransport = '%{public}@',\n}"
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
