## BatteryCenter

> `/System/Library/PrivateFrameworks/BatteryCenter.framework/Versions/A/BatteryCenter`

```diff

-301.0.0.0.0
-  __TEXT.__text: 0x4d14
+301.4.2.0.0
+  __TEXT.__text: 0x4e08
   __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x4a0
+  __TEXT.__objc_methlist: 0x614
   __TEXT.__const: 0x198
-  __TEXT.__gcc_except_tab: 0x100
+  __TEXT.__gcc_except_tab: 0xf4
   __TEXT.__oslogstring: 0x40a
   __TEXT.__cstring: 0x7e5
-  __TEXT.__unwind_info: 0x188
+  __TEXT.__unwind_info: 0x198
   __TEXT.__objc_classname: 0xaf
   __TEXT.__objc_methname: 0x11ad
   __TEXT.__objc_methtype: 0x2f6

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x418
+  __DATA_CONST.__objc_selrefs: 0x4a8
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x1b0
   __AUTH_CONST.__cfstring: 0xb60
-  __AUTH_CONST.__objc_const: 0xfe8
+  __AUTH_CONST.__objc_const: 0xd48
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x7c
   __DATA.__data: 0x1e8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5BDDFC9B-6CAD-3992-88E7-B2AEC832A174
-  Functions: 123
-  Symbols:   442
+  UUID: 7437F578-5C83-39A2-B64C-4E6497D2D087
+  Functions: 128
+  Symbols:   447
   CStrings:  494
 
Symbols:
+ +[BCBatteryDeviceController _sharedPowerSourceController].cold.1
+ -[_BCPowerSourceController _identifierFromPowerSourceDescription:].cold.1
+ -[_BCPowerSourceController addBatteryDeviceObserver:queue:].cold.1
+ -[_BCPowerSourceController addBatteryDeviceObserver:queue:].cold.2
+ BCRegisterUserNotificationsLogging.cold.1

```
