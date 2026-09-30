## XboxOneHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/XboxOneHIDServicePlugin.plugin/XboxOneHIDServicePlugin`

```diff

-13.0.36.0.0
-  __TEXT.__text: 0x6be4
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0x13a0
+13.0.39.0.0
+  __TEXT.__text: 0x6e9c
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_stubs: 0x13c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xc1c
   __TEXT.__objc_classname: 0x2e5
-  __TEXT.__objc_methname: 0x2072
+  __TEXT.__objc_methname: 0x2087
   __TEXT.__objc_methtype: 0xcbb
-  __TEXT.__cstring: 0x508
-  __TEXT.__const: 0xf4
-  __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__oslogstring: 0x52b
+  __TEXT.__cstring: 0x523
+  __TEXT.__const: 0x104
+  __TEXT.__gcc_except_tab: 0x188
+  __TEXT.__oslogstring: 0x64f
   __TEXT.__unwind_info: 0x280
-  __DATA_CONST.__auth_got: 0x2c0
+  __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0x2a8
-  __DATA_CONST.__cfstring: 0x7c0
+  __DATA_CONST.__cfstring: 0x800
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA.__objc_const: 0x1868
-  __DATA.__objc_selrefs: 0x828
+  __DATA.__objc_selrefs: 0x830
   __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 88585BAB-29DE-3D20-A31F-A056D1363CAE
+  UUID: 955846C3-475C-3C3C-A349-2D53CAB22674
   Functions: 246
-  Symbols:   127
-  CStrings:  701
+  Symbols:   130
+  CStrings:  705
 
Symbols:
+ _IOObjectCopyClass
+ _objc_release_x26
+ _objc_release_x27
Functions:
~ sub_3e04 : 908 -> 1308
~ sub_4190 -> sub_4320 : 420 -> 488
~ sub_4858 -> sub_4a2c : 288 -> 292
~ sub_4978 -> sub_4b50 : 336 -> 356
~ sub_4ac8 -> sub_4cb4 : 196 -> 200
~ sub_4b8c -> sub_4d7c : 380 -> 368
~ sub_4da0 -> sub_4f84 : 140 -> 200
~ sub_4e2c -> sub_504c : 216 -> 276
~ sub_4f7c -> sub_51d8 : 216 -> 220
~ sub_5054 -> sub_52b4 : 220 -> 236
~ sub_5204 -> sub_5474 : 700 -> 716
~ sub_54c0 -> sub_5740 : 208 -> 224
~ sub_5590 -> sub_5820 : 236 -> 252
~ sub_5684 -> sub_5924 : 192 -> 252
~ sub_57f4 -> sub_5ad0 : 136 -> 196
~ sub_587c -> sub_5b94 : 304 -> 320
~ sub_7084 -> sub_73ac : 232 -> 104
~ sub_77b0 -> sub_7a58 : 192 -> 208
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
