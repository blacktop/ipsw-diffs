## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-487.3.1.0.0
-  __TEXT.__text: 0xedde4
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x1745c
+488.11.0.0.0
+  __TEXT.__text: 0xec528
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_methlist: 0x170d4
   __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__cstring: 0x6d21
-  __TEXT.__oslogstring: 0x344a
+  __TEXT.__gcc_except_tab: 0x670
+  __TEXT.__cstring: 0x6c95
+  __TEXT.__oslogstring: 0x33ff
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x3a60
-  __TEXT.__objc_classname: 0x3b29
-  __TEXT.__objc_methname: 0x1bb35
-  __TEXT.__objc_methtype: 0x4387
-  __TEXT.__objc_stubs: 0x11dc0
-  __DATA_CONST.__got: 0xb80
+  __TEXT.__unwind_info: 0x39e8
+  __TEXT.__objc_classname: 0x3a68
+  __TEXT.__objc_methname: 0x1b888
+  __TEXT.__objc_methtype: 0x42db
+  __TEXT.__objc_stubs: 0x11bc0
+  __DATA_CONST.__got: 0xb58
   __DATA_CONST.__const: 0x2200
-  __DATA_CONST.__objc_classlist: 0xc10
-  __DATA_CONST.__objc_nlclslist: 0x8d8
+  __DATA_CONST.__objc_classlist: 0xbe0
+  __DATA_CONST.__objc_nlclslist: 0x8b8
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x678
+  __DATA_CONST.__objc_protolist: 0x670
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c88
-  __DATA_CONST.__objc_protorefs: 0x618
-  __DATA_CONST.__objc_superrefs: 0x1088
-  __DATA_CONST.__objc_arraydata: 0xade8
-  __AUTH_CONST.__auth_got: 0x340
+  __DATA_CONST.__objc_selrefs: 0x6bd0
+  __DATA_CONST.__objc_protorefs: 0x610
+  __DATA_CONST.__objc_superrefs: 0x1050
+  __DATA_CONST.__objc_arraydata: 0xa838
+  __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0xc400
-  __AUTH_CONST.__objc_const: 0x4c198
+  __AUTH_CONST.__cfstring: 0xc300
+  __AUTH_CONST.__objc_const: 0x4b648
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__objc_intobj: 0x510
-  __AUTH_CONST.__objc_dictobj: 0x5af0
   __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x1bd0
-  __DATA.__objc_ivar: 0x5a8
-  __DATA.__data: 0x4dc0
+  __AUTH_CONST.__objc_dictobj: 0x5a28
+  __AUTH.__objc_data: 0x1b30
+  __DATA.__objc_ivar: 0x5a0
+  __DATA.__data: 0x4d60
   __DATA.__bss: 0x300
-  __DATA_DIRTY.__objc_data: 0x5cd0
+  __DATA_DIRTY.__objc_data: 0x5b90
   __DATA_DIRTY.__bss: 0x158
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E1B01B4C-E5C5-3EF2-9AD6-886ABBC22F8D
-  Functions: 7182
-  Symbols:   23590
-  CStrings:  8879
+  UUID: FE1F1C0B-481F-3FD3-A0D1-BBE3147A5062
+  Functions: 7125
+  Symbols:   23401
+  CStrings:  8826
 
Symbols:
+ -[CAFPositionManager _queue_positionedServices]
+ -[CAFPositionManager _queue_stateForPositionedServices:]
+ -[CAFPositionManager _queue_stateForPositionedServices:].cold.1
+ -[CAFService characteristicTrackingLock]
+ -[CAFService controlTrackingLock]
+ -[CAFService setCharacteristicTrackingLock:]
+ -[CAFService setControlTrackingLock:]
+ GCC_except_table10
+ GCC_except_table26
+ GCC_except_table6
+ _OBJC_IVAR_$_CAFService._characteristicTrackingLock
+ _OBJC_IVAR_$_CAFService._controlTrackingLock
+ ___39-[CAFPositionManager vehicleLayoutKeys]_block_invoke
+ ___41-[CAFPositionManager accessoryIsTracked:]_block_invoke
+ ___43-[CAFPositionManager vehicleLayoutKeysFor:]_block_invoke
+ ___50-[CAFPositionManager servicesForVehicleLayoutKey:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_literal_global.1479
+ ___block_literal_global.1481
+ ___block_literal_global.657
+ ___block_literal_global.659
+ _dispatch_assert_queue$V2
+ _objc_msgSend$_queue_positionedServices
+ _objc_msgSend$_queue_stateForPositionedServices:
- +[CAFImageInfoCharacteristic load]
- +[CAFImageInfoCharacteristic primaryCharacteristicFormat]
- +[CAFImageInfoCharacteristic secondaryCharacteristicFormats]
- +[CAFImageInfoList imageInfoListWithArray:]
- +[CAFImageInfoList imageInfoListWithImageInfos:]
- +[CAFImageInfoListCharacteristic load]
- +[CAFImageInfoListCharacteristic primaryCharacteristicFormat]
- +[CAFImageInfoListCharacteristic secondaryCharacteristicFormats]
- +[CAFSettingsSubcategoryCharacteristic load]
- +[CAFSettingsSubcategoryCharacteristic primaryCharacteristicFormat]
- +[CAFSettingsSubcategoryCharacteristic secondaryCharacteristicFormats]
- +[CAFSplitImageViewConfiguration load]
- +[CAFSplitImageViewConfiguration observerProtocol]
- +[CAFSplitImageViewConfiguration serviceIdentifier]
- -[CAFAutomakerSetting hasSettingImageInfo]
- -[CAFAutomakerSetting hasSubcategory]
- -[CAFAutomakerSetting registeredForSettingImageInfo]
- -[CAFAutomakerSetting registeredForSettingsSubcategory]
- -[CAFAutomakerSetting settingImageInfoCharacteristic]
- -[CAFAutomakerSetting settingImageInfo]
- -[CAFAutomakerSetting subcategoryCharacteristic]
- -[CAFAutomakerSetting subcategory]
- -[CAFAutomakerSettings splitImageViewConfigurationService]
- -[CAFAutomakerSettings splitImageViewConfiguration]
- -[CAFImageInfo .cxx_destruct]
- -[CAFImageInfo description]
- -[CAFImageInfo dictionaryRepresentation]
- -[CAFImageInfo initWithDictionary:]
- -[CAFImageInfo name]
- -[CAFImageInfo text]
- -[CAFImageInfoCharacteristic formattedValue]
- -[CAFImageInfoCharacteristic imageInfoValue]
- -[CAFImageInfoCharacteristic setImageInfoValue:]
- -[CAFImageInfoList .cxx_destruct]
- -[CAFImageInfoList countByEnumeratingWithState:objects:count:]
- -[CAFImageInfoList formattedValue]
- -[CAFImageInfoList imageInfos]
- -[CAFImageInfoList initWithArray:]
- -[CAFImageInfoList initWithImageInfos:]
- -[CAFImageInfoList objectAtIndex:]
- -[CAFImageInfoList objectAtIndexedSubscript:]
- -[CAFImageInfoList parseError]
- -[CAFImageInfoListCharacteristic formattedValue]
- -[CAFImageInfoListCharacteristic imageInfoListValue]
- -[CAFImageInfoListCharacteristic setImageInfoListValue:]
- -[CAFPositionManager _positionedServices]
- -[CAFPositionManager _queue_currentState]
- -[CAFPositionManager _queue_positionServicesState]
- -[CAFPositionManager _stateForPositionedServices:]
- -[CAFPositionManager _stateForPositionedServices:].cold.1
- -[CAFPositionManager servicesFor:row:column:]
- -[CAFSettingsSubcategoryCharacteristic formattedValue]
- -[CAFSettingsSubcategoryCharacteristic setSettingsSubcategoryValue:]
- -[CAFSettingsSubcategoryCharacteristic settingsSubcategoryValue]
- -[CAFSplitImageViewConfiguration _characteristicDidUpdate:fromGroupUpdate:]
- -[CAFSplitImageViewConfiguration addObserver:]
- -[CAFSplitImageViewConfiguration hasSettingImageInfo]
- -[CAFSplitImageViewConfiguration name]
- -[CAFSplitImageViewConfiguration onCharacteristic]
- -[CAFSplitImageViewConfiguration on]
- -[CAFSplitImageViewConfiguration registerObserver:]
- -[CAFSplitImageViewConfiguration registeredForOn]
- -[CAFSplitImageViewConfiguration registeredForSettingImageInfo]
- -[CAFSplitImageViewConfiguration removeObserver:]
- -[CAFSplitImageViewConfiguration settingImageInfoCharacteristic]
- -[CAFSplitImageViewConfiguration settingImageInfo]
- -[CAFSplitImageViewConfiguration unregisterObserver:]
- GCC_except_table18
- GCC_except_table21
- _CAFCharacteristicTypeSettingImageInfo
- _CAFCharacteristicTypeSettingsSubcategory
- _CAFServiceTypeSplitImageViewConfiguration
- _CARPKeyImageInfoName
- _CARPKeyImageInfoText
- _NSStringFromSettingsSubcategory
- _OBJC_CLASS_$_CAFImageInfo
- _OBJC_CLASS_$_CAFImageInfoCharacteristic
- _OBJC_CLASS_$_CAFImageInfoList
- _OBJC_CLASS_$_CAFImageInfoListCharacteristic
- _OBJC_CLASS_$_CAFSettingsSubcategoryCharacteristic
- _OBJC_CLASS_$_CAFSplitImageViewConfiguration
- _OBJC_IVAR_$_CAFImageInfo._name
- _OBJC_IVAR_$_CAFImageInfo._text
- _OBJC_IVAR_$_CAFImageInfoList._imageInfos
- _OBJC_IVAR_$_CAFImageInfoList._parseError
- _OBJC_METACLASS_$_CAFImageInfo
- _OBJC_METACLASS_$_CAFImageInfoCharacteristic
- _OBJC_METACLASS_$_CAFImageInfoList
- _OBJC_METACLASS_$_CAFImageInfoListCharacteristic
- _OBJC_METACLASS_$_CAFSettingsSubcategoryCharacteristic
- _OBJC_METACLASS_$_CAFSplitImageViewConfiguration
- __OBJC_$_CLASS_METHODS_CAFImageInfoCharacteristic
- __OBJC_$_CLASS_METHODS_CAFImageInfoList
- __OBJC_$_CLASS_METHODS_CAFImageInfoListCharacteristic
- __OBJC_$_CLASS_METHODS_CAFSettingsSubcategoryCharacteristic
- __OBJC_$_CLASS_METHODS_CAFSplitImageViewConfiguration
- __OBJC_$_INSTANCE_METHODS_CAFImageInfo
- __OBJC_$_INSTANCE_METHODS_CAFImageInfoCharacteristic
- __OBJC_$_INSTANCE_METHODS_CAFImageInfoList
- __OBJC_$_INSTANCE_METHODS_CAFImageInfoListCharacteristic
- __OBJC_$_INSTANCE_METHODS_CAFSettingsSubcategoryCharacteristic
- __OBJC_$_INSTANCE_METHODS_CAFSplitImageViewConfiguration
- __OBJC_$_INSTANCE_VARIABLES_CAFImageInfo
- __OBJC_$_INSTANCE_VARIABLES_CAFImageInfoList
- __OBJC_$_PROP_LIST_CAFImageInfo
- __OBJC_$_PROP_LIST_CAFImageInfoCharacteristic
- __OBJC_$_PROP_LIST_CAFImageInfoList
- __OBJC_$_PROP_LIST_CAFImageInfoListCharacteristic
- __OBJC_$_PROP_LIST_CAFSettingsSubcategoryCharacteristic
- __OBJC_$_PROP_LIST_CAFSplitImageViewConfiguration
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFSplitImageViewConfigurationObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_CAFSplitImageViewConfigurationObserver
- __OBJC_$_PROTOCOL_REFS_CAFSplitImageViewConfigurationObserver
- __OBJC_CLASS_PROTOCOLS_$_CAFImageInfoList
- __OBJC_CLASS_RO_$_CAFImageInfo
- __OBJC_CLASS_RO_$_CAFImageInfoCharacteristic
- __OBJC_CLASS_RO_$_CAFImageInfoList
- __OBJC_CLASS_RO_$_CAFImageInfoListCharacteristic
- __OBJC_CLASS_RO_$_CAFSettingsSubcategoryCharacteristic
- __OBJC_CLASS_RO_$_CAFSplitImageViewConfiguration
- __OBJC_LABEL_PROTOCOL_$_CAFSplitImageViewConfigurationObserver
- __OBJC_METACLASS_RO_$_CAFImageInfo
- __OBJC_METACLASS_RO_$_CAFImageInfoCharacteristic
- __OBJC_METACLASS_RO_$_CAFImageInfoList
- __OBJC_METACLASS_RO_$_CAFImageInfoListCharacteristic
- __OBJC_METACLASS_RO_$_CAFSettingsSubcategoryCharacteristic
- __OBJC_METACLASS_RO_$_CAFSplitImageViewConfiguration
- __OBJC_PROTOCOL_$_CAFSplitImageViewConfigurationObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFSplitImageViewConfigurationObserver
- ___34-[CAFImageInfoList initWithArray:]_block_invoke
- ___34-[CAFImageInfoList initWithArray:]_block_invoke.cold.1
- ___block_literal_global.1491
- ___block_literal_global.1493
- ___block_literal_global.663
- ___block_literal_global.665
- _objc_msgSend$_positionedServices
- _objc_msgSend$_queue_positionServicesState
- _objc_msgSend$_stateForPositionedServices:
- _objc_msgSend$automakerSettingService:didUpdateSettingImageInfo:
- _objc_msgSend$automakerSettingService:didUpdateSubcategory:
- _objc_msgSend$imageInfoListValue
- _objc_msgSend$imageInfoListWithArray:
- _objc_msgSend$imageInfoValue
- _objc_msgSend$imageInfos
- _objc_msgSend$initWithImageInfos:
- _objc_msgSend$settingImageInfo
- _objc_msgSend$settingImageInfoCharacteristic
- _objc_msgSend$settingsSubcategoryValue
- _objc_msgSend$splitImageViewConfigurationService
- _objc_msgSend$splitImageViewConfigurationService:didUpdateOn:
- _objc_msgSend$splitImageViewConfigurationService:didUpdateSettingImageInfo:
- _objc_msgSend$subcategory
- _objc_msgSend$subcategoryCharacteristic
CStrings:
+ "-[CAFPositionManager _queue_stateForPositionedServices:]"
+ "T{os_unfair_lock_s=I},N,V_characteristicTrackingLock"
+ "T{os_unfair_lock_s=I},N,V_controlTrackingLock"
+ "_characteristicTrackingLock"
+ "_controlTrackingLock"
+ "_queue_positionedServices"
+ "_queue_stateForPositionedServices:"
+ "characteristicTrackingLock"
+ "controlTrackingLock"
+ "fetchResourcesWithReply:"
+ "setCharacteristicTrackingLock:"
+ "setControlTrackingLock:"
+ "\x81"
- "%{public}@: Error parsing dictionary from ImageInfoList array - %{public}@"
- "-[CAFPositionManager _stateForPositionedServices:]"
- "0x0000000016000021"
- "0x0000000036000030"
- "0x0000000036000034"
- "@40@0:8#16Q24Q32"
- "CAFImageInfo"
- "CAFImageInfoCharacteristic"
- "CAFImageInfoList"
- "CAFImageInfoListCharacteristic"
- "CAFSettingsSubcategoryCharacteristic"
- "CAFSplitImageViewConfiguration"
- "CAFSplitImageViewConfigurationObserver"
- "ImageInfo"
- "ImageInfoList"
- "SettingImageInfo"
- "SettingsSubcategory"
- "SplitImageViewConfiguration"
- "T@\"CAFImageInfo\",C,N"
- "T@\"CAFImageInfo\",R,N"
- "T@\"CAFImageInfoCharacteristic\",R,N"
- "T@\"CAFImageInfoList\",C,N"
- "T@\"CAFSettingsSubcategoryCharacteristic\",R,N"
- "T@\"CAFSplitImageViewConfiguration\",R,N"
- "T@\"NSArray\",R,N,V_imageInfos"
- "_imageInfos"
- "_queue_currentState"
- "_queue_positionServicesState"
- "_stateForPositionedServices:"
- "automakerSettingService:didUpdateSettingImageInfo:"
- "automakerSettingService:didUpdateSubcategory:"
- "fetchVariantsWithReply:"
- "hasSettingImageInfo"
- "hasSubcategory"
- "imageInfoListValue"
- "imageInfoListWithArray:"
- "imageInfoListWithImageInfos:"
- "imageInfoValue"
- "imageInfos"
- "initWithImageInfos:"
- "registeredForSettingImageInfo"
- "registeredForSettingsSubcategory"
- "servicesFor:row:column:"
- "setImageInfoListValue:"
- "setImageInfoValue:"
- "setSettingsSubcategoryValue:"
- "settingImageInfo"
- "settingImageInfoCharacteristic"
- "settingsSubcategoryValue"
- "splitImageViewConfiguration"
- "splitImageViewConfigurationService"
- "splitImageViewConfigurationService:didUpdateOn:"
- "splitImageViewConfigurationService:didUpdateSettingImageInfo:"
- "subcategory"
- "subcategoryCharacteristic"
- "v28@0:8@\"CAFSplitImageViewConfiguration\"16B24"
- "v32@0:8@\"CAFAutomakerSetting\"16@\"CAFImageInfo\"24"
- "v32@0:8@\"CAFSplitImageViewConfiguration\"16@\"CAFImageInfo\"24"

```
