## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-484.3.0.0.0
-  __TEXT.__text: 0xeccd0
+487.2.1.0.0
+  __TEXT.__text: 0xedde4
   __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x1728c
+  __TEXT.__objc_methlist: 0x1745c
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__cstring: 0x6cfd
+  __TEXT.__cstring: 0x6d21
   __TEXT.__oslogstring: 0x344a
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x3a20
-  __TEXT.__objc_classname: 0x3af9
-  __TEXT.__objc_methname: 0x1ba3c
-  __TEXT.__objc_methtype: 0x4314
-  __TEXT.__objc_stubs: 0x11d20
+  __TEXT.__unwind_info: 0x3a60
+  __TEXT.__objc_classname: 0x3b29
+  __TEXT.__objc_methname: 0x1bb35
+  __TEXT.__objc_methtype: 0x4387
+  __TEXT.__objc_stubs: 0x11dc0
   __DATA_CONST.__got: 0xb80
-  __DATA_CONST.__const: 0x21f8
-  __DATA_CONST.__objc_classlist: 0xc08
-  __DATA_CONST.__objc_nlclslist: 0x8d0
+  __DATA_CONST.__const: 0x2200
+  __DATA_CONST.__objc_classlist: 0xc10
+  __DATA_CONST.__objc_nlclslist: 0x8d8
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x670
+  __DATA_CONST.__objc_protolist: 0x678
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c50
-  __DATA_CONST.__objc_protorefs: 0x610
-  __DATA_CONST.__objc_superrefs: 0x1078
-  __DATA_CONST.__objc_arraydata: 0xab98
+  __DATA_CONST.__objc_selrefs: 0x6c88
+  __DATA_CONST.__objc_protorefs: 0x618
+  __DATA_CONST.__objc_superrefs: 0x1088
+  __DATA_CONST.__objc_arraydata: 0xade8
   __AUTH_CONST.__auth_got: 0x340
   __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0xc3c0
-  __AUTH_CONST.__objc_const: 0x4bb38
+  __AUTH_CONST.__cfstring: 0xc400
+  __AUTH_CONST.__objc_const: 0x4c198
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x510
-  __AUTH_CONST.__objc_dictobj: 0x5910
+  __AUTH_CONST.__objc_dictobj: 0x5af0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x1ef0
+  __AUTH.__objc_data: 0x1bd0
   __DATA.__objc_ivar: 0x5a8
-  __DATA.__data: 0x4d60
-  __DATA.__bss: 0x378
-  __DATA_DIRTY.__objc_data: 0x5960
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA.__data: 0x4dc0
+  __DATA.__bss: 0x300
+  __DATA_DIRTY.__objc_data: 0x5cd0
+  __DATA_DIRTY.__bss: 0x158
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E3ED3CF5-4089-37C3-B640-79D41165B1C5
-  Functions: 7150
-  Symbols:   23491
-  CStrings:  8863
+  UUID: F97FC00C-C416-3EC4-9ABF-AD9BC20E80C8
+  Functions: 7182
+  Symbols:   23590
+  CStrings:  8879
 
Symbols:
+ +[CAFTemperatureLevel indexBy]
+ +[CAFTemperatureLevel load]
+ +[CAFTemperatureLevel observerProtocol]
+ +[CAFTemperatureLevel serviceIdentifier]
+ -[CAFClimate temperatureLevelServices]
+ -[CAFClimate temperatureLevelsIndexed]
+ -[CAFClimate temperatureLevels]
+ -[CAFTemperatureLevel _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFTemperatureLevel addObserver:]
+ -[CAFTemperatureLevel hasOn]
+ -[CAFTemperatureLevel heatingCoolingLevelCharacteristic]
+ -[CAFTemperatureLevel heatingCoolingLevelDisabled]
+ -[CAFTemperatureLevel heatingCoolingLevelInvalid]
+ -[CAFTemperatureLevel heatingCoolingLevelRange]
+ -[CAFTemperatureLevel heatingCoolingLevelRestricted]
+ -[CAFTemperatureLevel heatingCoolingLevel]
+ -[CAFTemperatureLevel name]
+ -[CAFTemperatureLevel onCharacteristic]
+ -[CAFTemperatureLevel onDisabled]
+ -[CAFTemperatureLevel onInvalid]
+ -[CAFTemperatureLevel onRestricted]
+ -[CAFTemperatureLevel on]
+ -[CAFTemperatureLevel registerObserver:]
+ -[CAFTemperatureLevel registeredForHeatingCoolingLevel]
+ -[CAFTemperatureLevel registeredForOn]
+ -[CAFTemperatureLevel registeredForVehicleLayoutKey]
+ -[CAFTemperatureLevel removeObserver:]
+ -[CAFTemperatureLevel setHeatingCoolingLevel:]
+ -[CAFTemperatureLevel setOn:]
+ -[CAFTemperatureLevel unregisterObserver:]
+ -[CAFTemperatureLevel vehicleLayoutKeyCharacteristic]
+ -[CAFTemperatureLevel vehicleLayoutKey]
+ _CAFServiceTypeTemperatureLevel
+ _OBJC_CLASS_$_CAFTemperatureLevel
+ _OBJC_METACLASS_$_CAFTemperatureLevel
+ __OBJC_$_CLASS_METHODS_CAFTemperatureLevel
+ __OBJC_$_INSTANCE_METHODS_CAFTemperatureLevel
+ __OBJC_$_PROP_LIST_CAFTemperatureLevel
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFTemperatureLevelObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFTemperatureLevelObserver
+ __OBJC_$_PROTOCOL_REFS_CAFTemperatureLevelObserver
+ __OBJC_CLASS_PROTOCOLS_$_CAFTemperatureLevel
+ __OBJC_CLASS_RO_$_CAFTemperatureLevel
+ __OBJC_LABEL_PROTOCOL_$_CAFTemperatureLevelObserver
+ __OBJC_METACLASS_RO_$_CAFTemperatureLevel
+ __OBJC_PROTOCOL_$_CAFTemperatureLevelObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFTemperatureLevelObserver
+ ___block_literal_global.663
+ ___block_literal_global.665
+ _objc_msgSend$temperatureLevelService:didUpdateHeatingCoolingLevel:
+ _objc_msgSend$temperatureLevelService:didUpdateName:
+ _objc_msgSend$temperatureLevelService:didUpdateOn:
+ _objc_msgSend$temperatureLevelService:didUpdateVehicleLayoutKey:
+ _objc_msgSend$temperatureLevelServices
- ___block_literal_global.657
- ___block_literal_global.659
CStrings:
+ "0x0000000011000015"
+ "CAFTemperatureLevel"
+ "CAFTemperatureLevelObserver"
+ "TemperatureLevel"
+ "temperatureLevelService:didUpdateHeatingCoolingLevel:"
+ "temperatureLevelService:didUpdateName:"
+ "temperatureLevelService:didUpdateOn:"
+ "temperatureLevelService:didUpdateVehicleLayoutKey:"
+ "temperatureLevelServices"
+ "temperatureLevels"
+ "temperatureLevelsIndexed"
+ "v28@0:8@\"CAFTemperatureLevel\"16B24"
+ "v28@0:8@\"CAFTemperatureLevel\"16i24"
+ "v32@0:8@\"CAFTemperatureLevel\"16@\"NSString\"24"

```
