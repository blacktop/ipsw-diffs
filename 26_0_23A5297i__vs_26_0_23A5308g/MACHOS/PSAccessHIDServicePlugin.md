## PSAccessHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/PSAccessHIDServicePlugin.plugin/PSAccessHIDServicePlugin`

```diff

-13.0.36.0.0
-  __TEXT.__text: 0x7718
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_stubs: 0x1340
+13.0.39.0.0
+  __TEXT.__text: 0x79d0
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0x1360
   __TEXT.__objc_methlist: 0xbfc
   __TEXT.__objc_classname: 0x2e6
-  __TEXT.__objc_methname: 0x2058
+  __TEXT.__objc_methname: 0x206d
   __TEXT.__objc_methtype: 0xd7b
-  __TEXT.__cstring: 0x5de
-  __TEXT.__const: 0xf5
-  __TEXT.__gcc_except_tab: 0x1e4
-  __TEXT.__oslogstring: 0x64e
+  __TEXT.__cstring: 0x5f9
+  __TEXT.__const: 0x10d
+  __TEXT.__gcc_except_tab: 0x200
+  __TEXT.__oslogstring: 0x772
   __TEXT.__unwind_info: 0x2f8
-  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__auth_got: 0x2f8
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0x370
-  __DATA_CONST.__cfstring: 0x740
+  __DATA_CONST.__cfstring: 0x780
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x17a8
-  __DATA.__objc_selrefs: 0x838
+  __DATA.__objc_selrefs: 0x840
   __DATA.__objc_ivar: 0xfc
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35CBE531-82F3-3D21-8AE7-B5FBDE1E8126
+  UUID: 84086258-67D1-35F0-B05E-F85E35DF1E34
   Functions: 263
-  Symbols:   131
-  CStrings:  693
+  Symbols:   134
+  CStrings:  697
 
Symbols:
+ _IOObjectCopyClass
+ _objc_release_x26
+ _objc_release_x27
Functions:
~ sub_1708 : 908 -> 1308
~ sub_1a94 -> sub_1c24 : 420 -> 488
~ sub_215c -> sub_2330 : 288 -> 292
~ sub_227c -> sub_2454 : 336 -> 356
~ sub_23cc -> sub_25b8 : 196 -> 200
~ sub_2490 -> sub_2680 : 380 -> 368
~ sub_26a4 -> sub_2888 : 140 -> 200
~ sub_2730 -> sub_2950 : 216 -> 276
~ sub_2880 -> sub_2adc : 216 -> 220
~ sub_2958 -> sub_2bb8 : 220 -> 236
~ sub_2b08 -> sub_2d78 : 700 -> 716
~ sub_2dc4 -> sub_3044 : 208 -> 224
~ sub_2e94 -> sub_3124 : 236 -> 252
~ sub_2f88 -> sub_3228 : 192 -> 252
~ sub_30f8 -> sub_33d4 : 136 -> 196
~ sub_3180 -> sub_3498 : 304 -> 320
~ sub_4988 -> sub_4cb0 : 232 -> 104
~ sub_79a4 -> sub_7c4c : 192 -> 208
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
