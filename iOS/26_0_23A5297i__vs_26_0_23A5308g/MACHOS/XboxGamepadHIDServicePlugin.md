## XboxGamepadHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/XboxGamepadHIDServicePlugin.plugin/XboxGamepadHIDServicePlugin`

```diff

-13.0.36.0.0
-  __TEXT.__text: 0x7c40
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0x1400
+13.0.39.0.0
+  __TEXT.__text: 0x7ef8
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_stubs: 0x1420
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xd04
   __TEXT.__objc_classname: 0x392
-  __TEXT.__objc_methname: 0x2106
+  __TEXT.__objc_methname: 0x211b
   __TEXT.__objc_methtype: 0xc85
-  __TEXT.__cstring: 0x4fe
-  __TEXT.__const: 0xfc
-  __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__oslogstring: 0x494
+  __TEXT.__cstring: 0x519
+  __TEXT.__const: 0x10c
+  __TEXT.__gcc_except_tab: 0x1d8
+  __TEXT.__oslogstring: 0x5b8
   __TEXT.__unwind_info: 0x2f0
-  __DATA_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__auth_got: 0x308
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x320
-  __DATA_CONST.__cfstring: 0x760
+  __DATA_CONST.__cfstring: 0x7a0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x2570
-  __DATA.__objc_selrefs: 0x858
+  __DATA.__objc_selrefs: 0x860
   __DATA.__objc_ivar: 0xfc
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ADF245F4-98A9-3A41-8A6C-13484C53B037
+  UUID: C24A6187-0350-3A2C-800B-2D1A65A6E430
   Functions: 277
-  Symbols:   133
-  CStrings:  696
+  Symbols:   136
+  CStrings:  700
 
Symbols:
+ _IOObjectCopyClass
+ _objc_release_x26
+ _objc_release_x27
Functions:
~ sub_3ab0 : 908 -> 1308
~ sub_3e3c -> sub_3fcc : 420 -> 488
~ sub_4504 -> sub_46d8 : 288 -> 292
~ sub_4624 -> sub_47fc : 336 -> 356
~ sub_4774 -> sub_4960 : 196 -> 200
~ sub_4838 -> sub_4a28 : 380 -> 368
~ sub_4a4c -> sub_4c30 : 140 -> 200
~ sub_4ad8 -> sub_4cf8 : 216 -> 276
~ sub_4c28 -> sub_4e84 : 216 -> 220
~ sub_4d00 -> sub_4f60 : 220 -> 236
~ sub_4eb0 -> sub_5120 : 700 -> 716
~ sub_516c -> sub_53ec : 208 -> 224
~ sub_523c -> sub_54cc : 236 -> 252
~ sub_5330 -> sub_55d0 : 192 -> 252
~ sub_54a0 -> sub_577c : 136 -> 196
~ sub_5528 -> sub_5840 : 304 -> 320
~ sub_6d30 -> sub_7058 : 232 -> 104
~ sub_858c -> sub_8834 : 192 -> 208
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
