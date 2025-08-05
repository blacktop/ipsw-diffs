## PSVR2HIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/PSVR2HIDServicePlugin.plugin/PSVR2HIDServicePlugin`

```diff

-13.0.36.0.0
-  __TEXT.__text: 0xa2e0
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_stubs: 0x12e0
+13.0.39.0.0
+  __TEXT.__text: 0xa598
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_stubs: 0x1300
   __TEXT.__objc_methlist: 0xd34
   __TEXT.__objc_classname: 0x2f2
-  __TEXT.__objc_methname: 0x2084
+  __TEXT.__objc_methname: 0x2099
   __TEXT.__objc_methtype: 0xd2b
-  __TEXT.__cstring: 0x4ff
-  __TEXT.__const: 0xd5
-  __TEXT.__gcc_except_tab: 0x208
-  __TEXT.__oslogstring: 0xb9d
+  __TEXT.__cstring: 0x51a
+  __TEXT.__const: 0xe5
+  __TEXT.__gcc_except_tab: 0x224
+  __TEXT.__oslogstring: 0xca3
   __TEXT.__unwind_info: 0x328
-  __DATA_CONST.__auth_got: 0x438
+  __DATA_CONST.__auth_got: 0x448
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x2a8
-  __DATA_CONST.__cfstring: 0x700
+  __DATA_CONST.__cfstring: 0x740
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x1d10
-  __DATA.__objc_selrefs: 0x830
+  __DATA.__objc_selrefs: 0x838
   __DATA.__objc_ivar: 0x168
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5374742F-F02F-3B96-BB3F-3F8308C7AAF9
+  UUID: AB4BB723-0362-3FC3-8B4F-4F0F3980B261
   Functions: 308
-  Symbols:   178
-  CStrings:  746
+  Symbols:   180
+  CStrings:  748
 
Symbols:
+ _IOObjectCopyClass
+ _objc_release_x26
Functions:
~ sub_17a8 : 908 -> 1308
~ sub_1b34 -> sub_1cc4 : 420 -> 488
~ sub_21fc -> sub_23d0 : 288 -> 292
~ sub_231c -> sub_24f4 : 336 -> 356
~ sub_246c -> sub_2658 : 196 -> 200
~ sub_2530 -> sub_2720 : 380 -> 368
~ sub_2744 -> sub_2928 : 140 -> 200
~ sub_27d0 -> sub_29f0 : 216 -> 276
~ sub_2920 -> sub_2b7c : 216 -> 220
~ sub_29f8 -> sub_2c58 : 220 -> 236
~ sub_2ba8 -> sub_2e18 : 700 -> 716
~ sub_2e64 -> sub_30e4 : 208 -> 224
~ sub_2f34 -> sub_31c4 : 236 -> 252
~ sub_3028 -> sub_32c8 : 192 -> 252
~ sub_3198 -> sub_3474 : 136 -> 196
~ sub_3220 -> sub_3538 : 304 -> 320
~ sub_4a28 -> sub_4d50 : 232 -> 104
~ sub_9f18 -> sub_a1c0 : 192 -> 208
CStrings:
+ "Initialize <%{public}@ %#010llx> {\nvendorID = %zu,\nproductID = %zu,\nversion = %zu,\nmanufacturer = '%{public}@',\nproduct = '%{public}@',\nserial = '%{private}@',\ntransport = '%{public}@',\n}"
+ "Manufacturer"
+ "VersionNumber"
+ "[%#010llx] Creating HIDDevice."
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
- "updateBatteryStats reporting battery level %d%%"
- "updateClientBattery reporting battery level %d%%"

```
