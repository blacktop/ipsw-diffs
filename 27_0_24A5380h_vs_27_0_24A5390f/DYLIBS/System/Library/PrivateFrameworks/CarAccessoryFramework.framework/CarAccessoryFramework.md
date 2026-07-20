## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_catlist`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA.__objc_ivar`
- `__DATA_DIRTY.__objc_data`

```diff

-537.3.0.0.0
-  __TEXT.__text: 0x10bed4
-  __TEXT.__objc_methlist: 0x18e9c
+540.1.0.0.0
+  __TEXT.__text: 0x10cc10
+  __TEXT.__objc_methlist: 0x1901c
   __TEXT.__const: 0x1b8
   __TEXT.__gcc_except_tab: 0x53c
-  __TEXT.__oslogstring: 0x3cb5
-  __TEXT.__cstring: 0x7e6f
+  __TEXT.__oslogstring: 0x3d35
+  __TEXT.__cstring: 0x7ef1
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x3bb0
+  __TEXT.__unwind_info: 0x3bd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x26f8
-  __DATA_CONST.__objc_classlist: 0xdc0
+  __DATA_CONST.__const: 0x2738
+  __DATA_CONST.__objc_classlist: 0xdd0
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x618
+  __DATA_CONST.__objc_protolist: 0x620
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d18
-  __DATA_CONST.__objc_protorefs: 0x5b8
-  __DATA_CONST.__objc_superrefs: 0x7e8
-  __DATA_CONST.__objc_arraydata: 0xc168
-  __DATA_CONST.__got: 0xf00
+  __DATA_CONST.__objc_selrefs: 0x7da0
+  __DATA_CONST.__objc_protorefs: 0x5c0
+  __DATA_CONST.__objc_superrefs: 0x7f0
+  __DATA_CONST.__objc_arraydata: 0xc218
+  __DATA_CONST.__got: 0xf10
   __AUTH_CONST.__const: 0xac0
-  __AUTH_CONST.__cfstring: 0xde00
-  __AUTH_CONST.__objc_const: 0x4fbe8
+  __AUTH_CONST.__cfstring: 0xdf20
+  __AUTH_CONST.__objc_const: 0x50188
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__objc_intobj: 0x690
-  __AUTH_CONST.__objc_dictobj: 0x6630
   __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__objc_intobj: 0x690
   __AUTH_CONST.__objc_doubleobj: 0x30
+  __AUTH_CONST.__objc_dictobj: 0x66d0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50
+  __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x684
-  __DATA.__data: 0x4940
+  __DATA.__data: 0x49a0
   __DATA.__bss: 0x3d0
   __DATA_DIRTY.__objc_data: 0x8930
   __DATA_DIRTY.__bss: 0x128

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7734
-  Symbols:   15823
-  CStrings:  2178
+  Functions: 7764
+  Symbols:   15883
+  CStrings:  2188
 
Symbols:
+ +[CAFChargingSchedule observerProtocol]
+ +[CAFChargingSchedule serviceIdentifier]
+ +[CAFCurrentOwnerCharacteristic primaryCharacteristicFormat]
+ +[CAFCurrentOwnerCharacteristic secondaryCharacteristicFormats]
+ -[CAFCharging chargingScheduleService]
+ -[CAFCharging chargingSchedule]
+ -[CAFChargingSchedule _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFChargingSchedule addObserver:]
+ -[CAFChargingSchedule name]
+ -[CAFChargingSchedule registerObserver:]
+ -[CAFChargingSchedule registeredForTimeToStart]
+ -[CAFChargingSchedule removeObserver:]
+ -[CAFChargingSchedule timeToStartCharacteristic]
+ -[CAFChargingSchedule timeToStartInvalid]
+ -[CAFChargingSchedule timeToStartMeasurementRange]
+ -[CAFChargingSchedule timeToStartRange]
+ -[CAFChargingSchedule timeToStart]
+ -[CAFChargingSchedule unregisterObserver:]
+ -[CAFCurrentOwnerCharacteristic currentOwnerValue]
+ -[CAFCurrentOwnerCharacteristic formattedValue]
+ -[CAFCurrentOwnerCharacteristic setCurrentOwnerValue:]
+ -[CAFInteriorAmbientLights currentOwnerCharacteristic]
+ -[CAFInteriorAmbientLights currentOwner]
+ -[CAFInteriorAmbientLights hasCurrentOwner]
+ -[CAFInteriorAmbientLights registeredForCurrentOwner]
+ -[CAFInteriorAmbientLights setCurrentOwner:]
+ _CAFCharacteristicTypeCurrentOwner
+ _CAFCharacteristicTypeTimeToStart
+ _CAFServiceTypeChargingSchedule
+ _NSStringFromCurrentOwner
+ _OBJC_CLASS_$_CAFChargingSchedule
+ _OBJC_CLASS_$_CAFCurrentOwnerCharacteristic
+ _OBJC_METACLASS_$_CAFChargingSchedule
+ _OBJC_METACLASS_$_CAFCurrentOwnerCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFChargingSchedule
+ __OBJC_$_CLASS_METHODS_CAFCurrentOwnerCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFCar(CAFNowPlaying|Accessories)
+ __OBJC_$_INSTANCE_METHODS_CAFChargingSchedule
+ __OBJC_$_INSTANCE_METHODS_CAFCurrentOwnerCharacteristic
+ __OBJC_$_PROP_LIST_CAFChargingSchedule
+ __OBJC_$_PROP_LIST_CAFCurrentOwnerCharacteristic
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFChargingScheduleObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFChargingScheduleObserver
+ __OBJC_$_PROTOCOL_REFS_CAFChargingScheduleObserver
+ __OBJC_CLASS_RO_$_CAFChargingSchedule
+ __OBJC_CLASS_RO_$_CAFCurrentOwnerCharacteristic
+ __OBJC_LABEL_PROTOCOL_$_CAFChargingScheduleObserver
+ __OBJC_METACLASS_RO_$_CAFChargingSchedule
+ __OBJC_METACLASS_RO_$_CAFCurrentOwnerCharacteristic
+ __OBJC_PROTOCOL_$_CAFChargingScheduleObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFChargingScheduleObserver
+ _objc_msgSend$chargingScheduleService
+ _objc_msgSend$chargingScheduleService:didUpdateTimeToStart:
+ _objc_msgSend$currentOwner
+ _objc_msgSend$currentOwnerCharacteristic
+ _objc_msgSend$currentOwnerValue
+ _objc_msgSend$interiorAmbientLightsService:didUpdateCurrentOwner:
+ _objc_msgSend$setCurrentOwnerValue:
+ _objc_msgSend$timeToStart
+ _objc_msgSend$timeToStartCharacteristic
+ _objc_msgSend$timeToStartRange
- __OBJC_$_INSTANCE_METHODS_CAFCar(Accessories|CAFNowPlaying)
CStrings:
+ "%{public}@ echo timeout after %.3fs: no confirming update received; discarding pending write, reverting to last confirmed value"
+ "0x000000001900000B"
+ "0x000000003600006E"
+ "0x000000004000000E"
+ "Accessory"
+ "ChargingSchedule"
+ "Controller"
+ "CurrentOwner"
+ "Scheduled"
+ "TimeToStart"
```
