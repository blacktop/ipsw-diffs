## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-552.7.1.0.0
-  __TEXT.__text: 0x109d00
-  __TEXT.__objc_methlist: 0x19694
+553.9.3.0.0
+  __TEXT.__text: 0xff354
+  __TEXT.__objc_methlist: 0x19ca4
   __TEXT.__const: 0x1b8
   __TEXT.__gcc_except_tab: 0x53c
   __TEXT.__oslogstring: 0x3e3a
-  __TEXT.__cstring: 0x80cb
+  __TEXT.__cstring: 0x8277
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x6740
+  __TEXT.__unwind_info: 0x6878
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x27f0
-  __DATA_CONST.__objc_classlist: 0xe08
+  __DATA_CONST.__const: 0x28a8
+  __DATA_CONST.__objc_classlist: 0xe48
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x630
+  __DATA_CONST.__objc_protolist: 0x660
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7fa8
-  __DATA_CONST.__objc_protorefs: 0x5d0
-  __DATA_CONST.__objc_superrefs: 0x810
-  __DATA_CONST.__objc_arraydata: 0xc578
-  __DATA_CONST.__got: 0xf40
+  __DATA_CONST.__objc_selrefs: 0x8150
+  __DATA_CONST.__objc_protorefs: 0x5f0
+  __DATA_CONST.__objc_superrefs: 0x830
+  __DATA_CONST.__objc_arraydata: 0xc8e8
+  __DATA_CONST.__got: 0xf80
   __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0xe220
-  __AUTH_CONST.__objc_const: 0x51288
+  __AUTH_CONST.__cfstring: 0xe560
+  __AUTH_CONST.__objc_const: 0x547d0
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__objc_dictobj: 0x6860
-  __AUTH_CONST.__objc_intobj: 0x690
+  __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
+  __AUTH_CONST.__objc_dictobj: 0x6b80
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x6a4
-  __DATA.__data: 0x4a60
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x6d0
+  __DATA.__data: 0x4ca0
   __DATA_DIRTY.__objc_data: 0x8930
   __DATA_DIRTY.__bss: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7890
-  Symbols:   13385
-  CStrings:  2217
+  Functions: 7997
+  Symbols:   13613
+  CStrings:  2245
 
Symbols:
+ +[CAFApps accessoryIdentifier]
+ +[CAFApps observerProtocol]
+ +[CAFContacts observerProtocol]
+ +[CAFContacts serviceIdentifier]
+ +[CAFIncomingCallPresentationCharacteristic primaryCharacteristicFormat]
+ +[CAFIncomingCallPresentationCharacteristic secondaryCharacteristicFormats]
+ +[CAFMessageAIProcessingCharacteristic primaryCharacteristicFormat]
+ +[CAFMessageAIProcessingCharacteristic secondaryCharacteristicFormats]
+ +[CAFMessageHandlingCharacteristic primaryCharacteristicFormat]
+ +[CAFMessageHandlingCharacteristic secondaryCharacteristicFormats]
+ +[CAFMessages observerProtocol]
+ +[CAFMessages serviceIdentifier]
+ +[CAFPhone observerProtocol]
+ +[CAFPhone serviceIdentifier]
+ +[CAFSyncContactsCharacteristic primaryCharacteristicFormat]
+ +[CAFSyncContactsCharacteristic secondaryCharacteristicFormats]
+ -[CAFAccessory carManager]
+ -[CAFApps addObserver:]
+ -[CAFApps contactsService]
+ -[CAFApps contacts]
+ -[CAFApps messagesService]
+ -[CAFApps messages]
+ -[CAFApps phoneService]
+ -[CAFApps phone]
+ -[CAFApps registerObserver:]
+ -[CAFApps removeObserver:]
+ -[CAFApps unregisterObserver:]
+ -[CAFAutomakerSetting(Localization) localizedUserVisibleLabel]
+ -[CAFCar(Accessories) apps]
+ -[CAFCharacteristic carManager]
+ -[CAFContacts _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFContacts addObserver:]
+ -[CAFContacts hasSyncContacts]
+ -[CAFContacts name]
+ -[CAFContacts registerObserver:]
+ -[CAFContacts registeredForSyncContacts]
+ -[CAFContacts removeObserver:]
+ -[CAFContacts setSyncContacts:]
+ -[CAFContacts syncContactsCharacteristic]
+ -[CAFContacts syncContacts]
+ -[CAFContacts unregisterObserver:]
+ -[CAFControl carManager]
+ -[CAFDimensionManager vehicleEnergyUnit]
+ -[CAFIncomingCallPresentationCharacteristic formattedValue]
+ -[CAFIncomingCallPresentationCharacteristic incomingCallPresentationValue]
+ -[CAFIncomingCallPresentationCharacteristic setIncomingCallPresentationValue:]
+ -[CAFMessageAIProcessingCharacteristic formattedValue]
+ -[CAFMessageAIProcessingCharacteristic messageAIProcessingValue]
+ -[CAFMessageAIProcessingCharacteristic setMessageAIProcessingValue:]
+ -[CAFMessageHandlingCharacteristic formattedValue]
+ -[CAFMessageHandlingCharacteristic messageHandlingValue]
+ -[CAFMessageHandlingCharacteristic setMessageHandlingValue:]
+ -[CAFMessages _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFMessages addObserver:]
+ -[CAFMessages hasInterimBluetoothGroupMessaging]
+ -[CAFMessages hasMessageAIProcessing]
+ -[CAFMessages hasMessageHandling]
+ -[CAFMessages interimBluetoothGroupMessagingCharacteristic]
+ -[CAFMessages interimBluetoothGroupMessaging]
+ -[CAFMessages messageAIProcessingCharacteristic]
+ -[CAFMessages messageAIProcessing]
+ -[CAFMessages messageHandlingCharacteristic]
+ -[CAFMessages messageHandling]
+ -[CAFMessages name]
+ -[CAFMessages registerObserver:]
+ -[CAFMessages registeredForInterimBluetoothGroupMessaging]
+ -[CAFMessages registeredForMessageAIProcessing]
+ -[CAFMessages registeredForMessageHandling]
+ -[CAFMessages removeObserver:]
+ -[CAFMessages setMessageAIProcessing:]
+ -[CAFMessages setMessageHandling:]
+ -[CAFMessages unregisterObserver:]
+ -[CAFPhone _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFPhone addObserver:]
+ -[CAFPhone hasIncomingCallPresentation]
+ -[CAFPhone incomingCallPresentationCharacteristic]
+ -[CAFPhone incomingCallPresentation]
+ -[CAFPhone name]
+ -[CAFPhone registerObserver:]
+ -[CAFPhone registeredForIncomingCallPresentation]
+ -[CAFPhone removeObserver:]
+ -[CAFPhone unregisterObserver:]
+ -[CAFPresetEntry hidden]
+ -[CAFPresetEntry initWithDisabled:hidden:imageIdentifier:symbolName:userVisibleDescription:userVisibleLabel:]
+ -[CAFProminenceInformation(Localization) localizedUserVisibleLabel]
+ -[CAFRecirculation currentIndexCharacteristic]
+ -[CAFRecirculation currentIndexDisabled]
+ -[CAFRecirculation currentIndexInvalid]
+ -[CAFRecirculation currentIndexRange]
+ -[CAFRecirculation currentIndexRestricted]
+ -[CAFRecirculation currentIndex]
+ -[CAFRecirculation hasCurrentIndex]
+ -[CAFRecirculation hasModes]
+ -[CAFRecirculation hasOn]
+ -[CAFRecirculation modesCharacteristic]
+ -[CAFRecirculation modes]
+ -[CAFRecirculation registeredForCurrentIndex]
+ -[CAFRecirculation registeredForRecirculationModes]
+ -[CAFRecirculation setCurrentIndex:]
+ -[CAFService accessoryIdentifier]
+ -[CAFService carManager]
+ -[CAFSyncContactsCharacteristic formattedValue]
+ -[CAFSyncContactsCharacteristic setSyncContactsValue:]
+ -[CAFSyncContactsCharacteristic syncContactsValue]
+ GCC_except_table18
+ GCC_except_table21
+ GCC_except_table33
+ _CAFAccessoryTypeApps
+ _CAFCharacteristicTypeIncomingCallPresentation
+ _CAFCharacteristicTypeInterimBluetoothGroupMessaging
+ _CAFCharacteristicTypeMessageAIProcessing
+ _CAFCharacteristicTypeMessageHandling
+ _CAFCharacteristicTypeRecirculationModes
+ _CAFCharacteristicTypeSyncContacts
+ _CAFServiceTypeContacts
+ _CAFServiceTypeMessages
+ _CAFServiceTypePhone
+ _CARPKeyPresetEntryHidden
+ _NSStringFromIncomingCallPresentation
+ _NSStringFromMessageAIProcessing
+ _NSStringFromMessageHandling
+ _NSStringFromSyncContacts
+ _OBJC_CLASS_$_CAFApps
+ _OBJC_CLASS_$_CAFContacts
+ _OBJC_CLASS_$_CAFIncomingCallPresentationCharacteristic
+ _OBJC_CLASS_$_CAFMessageAIProcessingCharacteristic
+ _OBJC_CLASS_$_CAFMessageHandlingCharacteristic
+ _OBJC_CLASS_$_CAFMessages
+ _OBJC_CLASS_$_CAFPhone
+ _OBJC_CLASS_$_CAFSyncContactsCharacteristic
+ _OBJC_IVAR_$_CAFAccessory._carManager
+ _OBJC_IVAR_$_CAFCharacteristic._accessory
+ _OBJC_IVAR_$_CAFCharacteristic._car
+ _OBJC_IVAR_$_CAFCharacteristic._carManager
+ _OBJC_IVAR_$_CAFControl._accessory
+ _OBJC_IVAR_$_CAFControl._car
+ _OBJC_IVAR_$_CAFControl._carManager
+ _OBJC_IVAR_$_CAFPresetEntry._hidden
+ _OBJC_IVAR_$_CAFService._accessoryIdentifier
+ _OBJC_IVAR_$_CAFService._car
+ _OBJC_IVAR_$_CAFService._carManager
+ _OBJC_METACLASS_$_CAFApps
+ _OBJC_METACLASS_$_CAFContacts
+ _OBJC_METACLASS_$_CAFIncomingCallPresentationCharacteristic
+ _OBJC_METACLASS_$_CAFMessageAIProcessingCharacteristic
+ _OBJC_METACLASS_$_CAFMessageHandlingCharacteristic
+ _OBJC_METACLASS_$_CAFMessages
+ _OBJC_METACLASS_$_CAFPhone
+ _OBJC_METACLASS_$_CAFSyncContactsCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFApps
+ __OBJC_$_CLASS_METHODS_CAFContacts
+ __OBJC_$_CLASS_METHODS_CAFIncomingCallPresentationCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFMessageAIProcessingCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFMessageHandlingCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFMessages
+ __OBJC_$_CLASS_METHODS_CAFPhone
+ __OBJC_$_CLASS_METHODS_CAFSyncContactsCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFApps
+ __OBJC_$_INSTANCE_METHODS_CAFAutomakerSetting(Localization)
+ __OBJC_$_INSTANCE_METHODS_CAFCar(CAFNowPlaying|Accessories)
+ __OBJC_$_INSTANCE_METHODS_CAFContacts
+ __OBJC_$_INSTANCE_METHODS_CAFIncomingCallPresentationCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFMessageAIProcessingCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFMessageHandlingCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFMessages
+ __OBJC_$_INSTANCE_METHODS_CAFPhone
+ __OBJC_$_INSTANCE_METHODS_CAFProminenceInformation(Localization)
+ __OBJC_$_INSTANCE_METHODS_CAFSyncContactsCharacteristic
+ __OBJC_$_PROP_LIST_CAFApps
+ __OBJC_$_PROP_LIST_CAFContacts
+ __OBJC_$_PROP_LIST_CAFIncomingCallPresentationCharacteristic
+ __OBJC_$_PROP_LIST_CAFMessageAIProcessingCharacteristic
+ __OBJC_$_PROP_LIST_CAFMessageHandlingCharacteristic
+ __OBJC_$_PROP_LIST_CAFMessages
+ __OBJC_$_PROP_LIST_CAFPhone
+ __OBJC_$_PROP_LIST_CAFPositioned_Internal
+ __OBJC_$_PROP_LIST_CAFPositioned_Private
+ __OBJC_$_PROP_LIST_CAFSyncContactsCharacteristic
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFContactsObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFMessagesObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFPhoneObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFPositioned_Internal
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFPositioned_Private
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFContactsObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFMessagesObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFPhoneObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFPositioned_Internal
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFPositioned_Private
+ __OBJC_$_PROTOCOL_REFS_CAFAppsObserver
+ __OBJC_$_PROTOCOL_REFS_CAFContactsObserver
+ __OBJC_$_PROTOCOL_REFS_CAFMessagesObserver
+ __OBJC_$_PROTOCOL_REFS_CAFPhoneObserver
+ __OBJC_$_PROTOCOL_REFS_CAFPositioned_Internal
+ __OBJC_$_PROTOCOL_REFS_CAFPositioned_Private
+ __OBJC_CLASS_PROTOCOLS_$_CAFBooleanSetting
+ __OBJC_CLASS_PROTOCOLS_$_CAFButtonSetting
+ __OBJC_CLASS_PROTOCOLS_$_CAFDeepLinkSetting
+ __OBJC_CLASS_PROTOCOLS_$_CAFFloatSetting
+ __OBJC_CLASS_PROTOCOLS_$_CAFIntegerSetting
+ __OBJC_CLASS_PROTOCOLS_$_CAFMultipleSelectImageSetting
+ __OBJC_CLASS_PROTOCOLS_$_CAFMultipleSelectSetting
+ __OBJC_CLASS_PROTOCOLS_$_CAFSingleSelectImageSetting
+ __OBJC_CLASS_PROTOCOLS_$_CAFSingleSelectSetting
+ __OBJC_CLASS_PROTOCOLS_$_CAFStaticSetting
+ __OBJC_CLASS_RO_$_CAFApps
+ __OBJC_CLASS_RO_$_CAFContacts
+ __OBJC_CLASS_RO_$_CAFIncomingCallPresentationCharacteristic
+ __OBJC_CLASS_RO_$_CAFMessageAIProcessingCharacteristic
+ __OBJC_CLASS_RO_$_CAFMessageHandlingCharacteristic
+ __OBJC_CLASS_RO_$_CAFMessages
+ __OBJC_CLASS_RO_$_CAFPhone
+ __OBJC_CLASS_RO_$_CAFSyncContactsCharacteristic
+ __OBJC_LABEL_PROTOCOL_$_CAFAppsObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFContactsObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFMessagesObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFPhoneObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFPositioned_Internal
+ __OBJC_LABEL_PROTOCOL_$_CAFPositioned_Private
+ __OBJC_METACLASS_RO_$_CAFApps
+ __OBJC_METACLASS_RO_$_CAFContacts
+ __OBJC_METACLASS_RO_$_CAFIncomingCallPresentationCharacteristic
+ __OBJC_METACLASS_RO_$_CAFMessageAIProcessingCharacteristic
+ __OBJC_METACLASS_RO_$_CAFMessageHandlingCharacteristic
+ __OBJC_METACLASS_RO_$_CAFMessages
+ __OBJC_METACLASS_RO_$_CAFPhone
+ __OBJC_METACLASS_RO_$_CAFSyncContactsCharacteristic
+ __OBJC_PROTOCOL_$_CAFAppsObserver
+ __OBJC_PROTOCOL_$_CAFContactsObserver
+ __OBJC_PROTOCOL_$_CAFMessagesObserver
+ __OBJC_PROTOCOL_$_CAFPhoneObserver
+ __OBJC_PROTOCOL_$_CAFPositioned_Internal
+ __OBJC_PROTOCOL_$_CAFPositioned_Private
+ __OBJC_PROTOCOL_REFERENCE_$_CAFAppsObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFContactsObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFMessagesObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFPhoneObserver
- -[CAFPresetEntry initWithDisabled:imageIdentifier:symbolName:userVisibleDescription:userVisibleLabel:]
- GCC_except_table22
- GCC_except_table37
- __OBJC_$_INSTANCE_METHODS_CAFAutomakerSetting
- __OBJC_$_INSTANCE_METHODS_CAFCar(Accessories|CAFNowPlaying)
- __OBJC_$_INSTANCE_METHODS_CAFProminenceInformation
- __OBJC_$_PROP_LIST_CAFAutomakerSetting
- __OBJC_$_PROP_LIST_CAFProminenceInformation
CStrings:
+ "#!"
+ "0x0000000001A00001"
+ "0x0000000026000001"
+ "0x0000000026000002"
+ "0x0000000026000003"
+ "0x0000000031000033"
+ "0x0000000053000001"
+ "0x0000000053000002"
+ "0x0000000053000003"
+ "0x0000000053000004"
+ "0x0000000053000005"
+ "4"
+ "<%@: %p { %@: %d, %@: %d, %@: %@, %@: %@, %@: %@, %@: %@ }>"
+ "Apps"
+ "Authorized"
+ "BalanceAndFade"
+ "Contacts"
+ "Denied"
+ "IncomingCallPresentation"
+ "InterimBluetoothGroupMessaging"
+ "Localizable"
+ "MessageAIProcessing"
+ "MessageHandling"
+ "Messages"
+ "Phone"
+ "RecirculationModes"
+ "SyncContacts"
+ "VisibleSystem"
+ "hidden"
+ "\x82A"
- "<%@: %p { %@: %d, %@: %@, %@: %@, %@: %@, %@: %@ }>"
- "\x81"
```
