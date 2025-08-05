## DualShock4HIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/DualShock4HIDServicePlugin.plugin/DualShock4HIDServicePlugin`

```diff

-13.0.36.0.0
-  __TEXT.__text: 0x9480
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_stubs: 0x15c0
+13.0.39.0.0
+  __TEXT.__text: 0x9738
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_stubs: 0x15e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xc94
   __TEXT.__objc_classname: 0x2ed
-  __TEXT.__objc_methname: 0x238c
+  __TEXT.__objc_methname: 0x23a1
   __TEXT.__objc_methtype: 0xeef
-  __TEXT.__cstring: 0x72c
-  __TEXT.__const: 0x520
-  __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__oslogstring: 0x864
+  __TEXT.__cstring: 0x747
+  __TEXT.__const: 0x530
+  __TEXT.__gcc_except_tab: 0x1a4
+  __TEXT.__oslogstring: 0x988
   __TEXT.__unwind_info: 0x2f0
-  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__auth_got: 0x2e8
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x368
-  __DATA_CONST.__cfstring: 0xbe0
+  __DATA_CONST.__cfstring: 0xc20
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x1bb8
-  __DATA.__objc_selrefs: 0x8a0
+  __DATA.__objc_selrefs: 0x8a8
   __DATA.__objc_ivar: 0x168
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 359AF27A-9768-378C-9FBB-42273D46CB42
+  UUID: 9FB5D31B-8699-3F73-B062-3DE0C42D8349
   Functions: 290
-  Symbols:   129
-  CStrings:  827
+  Symbols:   130
+  CStrings:  831
 
Symbols:
+ _IOObjectCopyClass
Functions:
~ sub_5d90 : 908 -> 1308
~ sub_611c -> sub_62ac : 420 -> 488
~ sub_67e4 -> sub_69b8 : 288 -> 292
~ sub_6904 -> sub_6adc : 336 -> 356
~ sub_6a54 -> sub_6c40 : 196 -> 200
~ sub_6b18 -> sub_6d08 : 380 -> 368
~ sub_6d2c -> sub_6f10 : 140 -> 200
~ sub_6db8 -> sub_6fd8 : 216 -> 276
~ sub_6f08 -> sub_7164 : 216 -> 220
~ sub_6fe0 -> sub_7240 : 220 -> 236
~ sub_7190 -> sub_7400 : 700 -> 716
~ sub_744c -> sub_76cc : 208 -> 224
~ sub_751c -> sub_77ac : 236 -> 252
~ sub_7610 -> sub_78b0 : 192 -> 252
~ sub_7780 -> sub_7a5c : 136 -> 196
~ sub_7808 -> sub_7b20 : 304 -> 320
~ sub_9010 -> sub_9338 : 232 -> 104
~ sub_9fac -> sub_a254 : 192 -> 208
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
