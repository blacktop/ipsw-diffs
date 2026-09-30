## LunaHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/LunaHIDServicePlugin.plugin/LunaHIDServicePlugin`

```diff

-13.0.36.0.0
-  __TEXT.__text: 0x5cdc
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_stubs: 0x1220
+13.0.39.0.0
+  __TEXT.__text: 0x5f94
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_stubs: 0x1240
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xba4
-  __TEXT.__cstring: 0x4ae
+  __TEXT.__cstring: 0x4c9
   __TEXT.__objc_classname: 0x2e2
-  __TEXT.__objc_methname: 0x1f20
+  __TEXT.__objc_methname: 0x1f35
   __TEXT.__objc_methtype: 0xc67
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__oslogstring: 0x35d
+  __TEXT.__const: 0xd0
+  __TEXT.__gcc_except_tab: 0x188
+  __TEXT.__oslogstring: 0x481
   __TEXT.__unwind_info: 0x260
-  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__auth_got: 0x2d0
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x2a8
-  __DATA_CONST.__cfstring: 0x6c0
+  __DATA_CONST.__cfstring: 0x700
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x1760
-  __DATA.__objc_selrefs: 0x7f0
+  __DATA.__objc_selrefs: 0x7f8
   __DATA.__objc_ivar: 0xf4
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CD8DDF74-EFB4-3206-A74C-DE659E109C7F
+  UUID: 5B80EF56-BEA3-3DF4-8909-9BCC4CFD0D7B
   Functions: 235
-  Symbols:   124
-  CStrings:  655
+  Symbols:   127
+  CStrings:  659
 
Symbols:
+ _IOObjectCopyClass
+ _objc_release_x26
+ _objc_release_x27
Functions:
~ sub_2e50 : 908 -> 1308
~ sub_31dc -> sub_336c : 420 -> 488
~ sub_38a4 -> sub_3a78 : 288 -> 292
~ sub_39c4 -> sub_3b9c : 336 -> 356
~ sub_3b14 -> sub_3d00 : 196 -> 200
~ sub_3bd8 -> sub_3dc8 : 380 -> 368
~ sub_3dec -> sub_3fd0 : 140 -> 200
~ sub_3e78 -> sub_4098 : 216 -> 276
~ sub_3fc8 -> sub_4224 : 216 -> 220
~ sub_40a0 -> sub_4300 : 220 -> 236
~ sub_4250 -> sub_44c0 : 700 -> 716
~ sub_450c -> sub_478c : 208 -> 224
~ sub_45dc -> sub_486c : 236 -> 252
~ sub_46d0 -> sub_4970 : 192 -> 252
~ sub_4840 -> sub_4b1c : 136 -> 196
~ sub_48c8 -> sub_4be0 : 304 -> 320
~ sub_60d0 -> sub_63f8 : 232 -> 104
~ sub_6808 -> sub_6ab0 : 192 -> 208
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
