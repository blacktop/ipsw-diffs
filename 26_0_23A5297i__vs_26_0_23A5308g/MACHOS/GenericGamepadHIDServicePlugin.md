## GenericGamepadHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/GenericGamepadHIDServicePlugin.plugin/GenericGamepadHIDServicePlugin`

```diff

-13.0.36.0.0
-  __TEXT.__text: 0xdc40
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_stubs: 0x1d00
+13.0.39.0.0
+  __TEXT.__text: 0xdef8
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_stubs: 0x1d20
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xcec
-  __TEXT.__cstring: 0xe52
+  __TEXT.__cstring: 0xe6d
   __TEXT.__objc_classname: 0x362
-  __TEXT.__objc_methname: 0x267b
+  __TEXT.__objc_methname: 0x2690
   __TEXT.__objc_methtype: 0xe0b
-  __TEXT.__const: 0x115
-  __TEXT.__gcc_except_tab: 0x5ac
-  __TEXT.__oslogstring: 0x7a6
+  __TEXT.__const: 0x11d
+  __TEXT.__gcc_except_tab: 0x5c8
+  __TEXT.__oslogstring: 0x8ca
   __TEXT.__unwind_info: 0x3d0
-  __DATA_CONST.__auth_got: 0x390
+  __DATA_CONST.__auth_got: 0x398
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0x830
-  __DATA_CONST.__cfstring: 0xbc0
+  __DATA_CONST.__cfstring: 0xc00
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x1988
-  __DATA.__objc_selrefs: 0xa80
+  __DATA.__objc_selrefs: 0xa88
   __DATA.__objc_ivar: 0x130
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x900

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 820DE7D0-0B49-3589-9DD8-5EEC82494603
+  UUID: 5901499D-0B52-3E21-A03B-A5790AF7D698
   Functions: 348
-  Symbols:   178
-  CStrings:  892
+  Symbols:   179
+  CStrings:  896
 
Symbols:
+ _IOObjectCopyClass
Functions:
~ sub_17d0 : 908 -> 1308
~ sub_1b5c -> sub_1cec : 420 -> 488
~ sub_2224 -> sub_23f8 : 288 -> 292
~ sub_2344 -> sub_251c : 336 -> 356
~ sub_2494 -> sub_2680 : 196 -> 200
~ sub_2558 -> sub_2748 : 380 -> 368
~ sub_276c -> sub_2950 : 140 -> 200
~ sub_27f8 -> sub_2a18 : 216 -> 276
~ sub_2948 -> sub_2ba4 : 216 -> 220
~ sub_2a20 -> sub_2c80 : 220 -> 236
~ sub_2c40 -> sub_2eb0 : 700 -> 716
~ sub_2efc -> sub_317c : 208 -> 224
~ sub_2fcc -> sub_325c : 236 -> 252
~ sub_30c0 -> sub_3360 : 192 -> 252
~ sub_3230 -> sub_350c : 136 -> 196
~ sub_32b8 -> sub_35d0 : 304 -> 320
~ sub_4ac0 -> sub_4de8 : 232 -> 104
~ sub_cd90 -> sub_d038 : 192 -> 208
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
