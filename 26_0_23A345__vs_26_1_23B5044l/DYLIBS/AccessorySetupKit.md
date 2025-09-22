## AccessorySetupKit

> `/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`

```diff

-320.40.0.0.0
-  __TEXT.__text: 0x19860
+321.4.1.0.0
+  __TEXT.__text: 0x1b734
   __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_methlist: 0x1a40
-  __TEXT.__const: 0x436
-  __TEXT.__cstring: 0x31e7
+  __TEXT.__objc_methlist: 0x1c50
+  __TEXT.__const: 0x462
+  __TEXT.__cstring: 0x341a
   __TEXT.__gcc_except_tab: 0x3e4
   __TEXT.__ustring: 0x44
-  __TEXT.__swift5_typeref: 0x291
-  __TEXT.__oslogstring: 0x24b
-  __TEXT.__constg_swiftt: 0x224
-  __TEXT.__swift5_reflstr: 0xb1
-  __TEXT.__swift5_fieldmd: 0xb4
+  __TEXT.__constg_swiftt: 0x264
+  __TEXT.__swift5_typeref: 0x295
+  __TEXT.__swift5_reflstr: 0x109
+  __TEXT.__swift5_fieldmd: 0xcc
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x618
-  __TEXT.__objc_classname: 0x2dd
-  __TEXT.__objc_methname: 0x4f34
-  __TEXT.__objc_methtype: 0x1147
-  __TEXT.__objc_stubs: 0x3280
-  __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0x5a0
-  __DATA_CONST.__objc_classlist: 0xa0
+  __TEXT.__oslogstring: 0x24b
+  __TEXT.__swift5_capture: 0xc0
+  __TEXT.__unwind_info: 0x690
+  __TEXT.__objc_classname: 0x30c
+  __TEXT.__objc_methname: 0x521d
+  __TEXT.__objc_methtype: 0x11d7
+  __TEXT.__objc_stubs: 0x3460
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__const: 0x578
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14e8
+  __DATA_CONST.__objc_selrefs: 0x1590
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x660
-  __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x11a0
-  __AUTH_CONST.__objc_const: 0x2670
+  __AUTH_CONST.__const: 0x410
+  __AUTH_CONST.__cfstring: 0x1240
+  __AUTH_CONST.__objc_const: 0x2920
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x8a8
-  __AUTH.__data: 0x60
-  __DATA.__objc_ivar: 0x180
-  __DATA.__data: 0x860
+  __AUTH.__objc_data: 0x998
+  __AUTH.__data: 0x68
+  __DATA.__objc_ivar: 0x194
+  __DATA.__data: 0x880
   __DATA.__bss: 0x4a0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 192099AE-E003-3735-BB20-9FAFF8688B4E
-  Functions: 643
-  Symbols:   2187
-  CStrings:  1539
+  UUID: 1C28E97C-F4B7-353E-B8E3-AC0BD589ACE1
+  Functions: 699
+  Symbols:   2323
+  CStrings:  1592
 
Symbols:
+ +[ASDiscoveredAccessory supportsSecureCoding]
+ +[ASDiscoveredDisplayItem supportsSecureCoding]
+ -[ASAccessory setWifiAwarePairedDeviceID:]
+ -[ASAccessorySession _finishDiscovery:]
+ -[ASAccessorySession _updatePickerWithDiscoveredDisplayItems:completionHandler:]
+ -[ASAccessorySession finishPickerDiscovery:]
+ -[ASAccessorySession updatePickerShowingDiscoveredDisplayItems:completionHandler:]
+ -[ASDiscoveredAccessory .cxx_destruct]
+ -[ASDiscoveredAccessory bluetoothAdvertisementData]
+ -[ASDiscoveredAccessory bluetoothRSSI]
+ -[ASDiscoveredAccessory copyWithZone:]
+ -[ASDiscoveredAccessory descriptionWithLevel:]
+ -[ASDiscoveredAccessory description]
+ -[ASDiscoveredAccessory encodeWithCoder:]
+ -[ASDiscoveredAccessory encodeWithXPCObject:]
+ -[ASDiscoveredAccessory initWithCoder:]
+ -[ASDiscoveredAccessory initWithCoder:].cold.1
+ -[ASDiscoveredAccessory initWithDADevice:bundleID:]
+ -[ASDiscoveredAccessory initWithXPCObject:error:]
+ -[ASDiscoveredAccessory initWithXPCObject:error:].cold.1
+ -[ASDiscoveredAccessory isEqual:]
+ -[ASDiscoveredAccessory setBluetoothAdvertisementData:]
+ -[ASDiscoveredAccessory setBluetoothRSSI:]
+ -[ASDiscoveredDisplayItem .cxx_destruct]
+ -[ASDiscoveredDisplayItem accessory]
+ -[ASDiscoveredDisplayItem copyWithZone:]
+ -[ASDiscoveredDisplayItem descriptionWithLevel:]
+ -[ASDiscoveredDisplayItem encodeWithCoder:]
+ -[ASDiscoveredDisplayItem encodeWithXPCObject:]
+ -[ASDiscoveredDisplayItem initWithCoder:]
+ -[ASDiscoveredDisplayItem initWithCoder:].cold.1
+ -[ASDiscoveredDisplayItem initWithName:productImage:accessory:]
+ -[ASDiscoveredDisplayItem initWithXPCObject:error:]
+ -[ASDiscoveredDisplayItem initWithXPCObject:error:].cold.1
+ -[ASDiscoveredDisplayItem isEqual:]
+ -[ASDiscoveredDisplayItem setAccessory:]
+ -[ASPickerDisplayItem setName:]
+ -[ASPickerDisplayItem setProductImage:]
+ -[ASPickerDisplaySettings options]
+ -[ASPickerDisplaySettings setOptions:]
+ GCC_except_table68
+ GCC_except_table71
+ _ASPickerDisplaySettingsDiscoveryTimeoutUnbounded
+ _OBJC_CLASS_$_ASDiscoveredAccessory
+ _OBJC_CLASS_$_ASDiscoveredDisplayItem
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSSet
+ _OBJC_IVAR_$_ASAccessorySession._discoveredAccessories
+ _OBJC_IVAR_$_ASDiscoveredAccessory._bluetoothAdvertisementData
+ _OBJC_IVAR_$_ASDiscoveredAccessory._bluetoothRSSI
+ _OBJC_IVAR_$_ASDiscoveredDisplayItem._accessory
+ _OBJC_IVAR_$_ASPickerDisplaySettings._options
+ _OBJC_METACLASS_$_ASDiscoveredAccessory
+ _OBJC_METACLASS_$_ASDiscoveredDisplayItem
+ __OBJC_$_CLASS_METHODS_ASDiscoveredAccessory
+ __OBJC_$_CLASS_METHODS_ASDiscoveredDisplayItem
+ __OBJC_$_CLASS_PROP_LIST_ASDiscoveredAccessory
+ __OBJC_$_INSTANCE_METHODS_ASDiscoveredAccessory
+ __OBJC_$_INSTANCE_METHODS_ASDiscoveredDisplayItem
+ __OBJC_$_INSTANCE_VARIABLES_ASDiscoveredAccessory
+ __OBJC_$_INSTANCE_VARIABLES_ASDiscoveredDisplayItem
+ __OBJC_$_PROP_LIST_ASDiscoveredAccessory
+ __OBJC_$_PROP_LIST_ASDiscoveredDisplayItem
+ __OBJC_CLASS_PROTOCOLS_$_ASDiscoveredAccessory
+ __OBJC_CLASS_RO_$_ASDiscoveredAccessory
+ __OBJC_CLASS_RO_$_ASDiscoveredDisplayItem
+ __OBJC_METACLASS_RO_$_ASDiscoveredAccessory
+ __OBJC_METACLASS_RO_$_ASDiscoveredDisplayItem
+ __PROTOCOLS__TtC17AccessorySetupKit17ASUIClientWrapper.37
+ ___44-[ASAccessorySession finishPickerDiscovery:]_block_invoke
+ ___44-[ASAccessorySession finishPickerDiscovery:]_block_invoke.cold.1
+ ___44-[ASAccessorySession finishPickerDiscovery:]_block_invoke.cold.2
+ ___82-[ASAccessorySession updatePickerShowingDiscoveredDisplayItems:completionHandler:]_block_invoke
+ ___82-[ASAccessorySession updatePickerShowingDiscoveredDisplayItems:completionHandler:]_block_invoke.cold.1
+ ___82-[ASAccessorySession updatePickerShowingDiscoveredDisplayItems:completionHandler:]_block_invoke.cold.2
+ ___82-[ASAccessorySession updatePickerShowingDiscoveredDisplayItems:completionHandler:]_block_invoke.cold.3
+ _block_copy_helper.71
+ _block_copy_helper.77
+ _block_copy_helper.81
+ _block_copy_helper.88
+ _block_descriptor.73
+ _block_descriptor.79
+ _block_descriptor.83
+ _block_descriptor.90
+ _block_destroy_helper.72
+ _block_destroy_helper.78
+ _block_destroy_helper.82
+ _block_destroy_helper.89
+ _objc_msgSend$_finishDiscovery:
+ _objc_msgSend$_updatePickerWithDiscoveredDisplayItems:completionHandler:
+ _objc_msgSend$accessory
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$bluetoothAdvertisementData
+ _objc_msgSend$bluetoothRSSI
+ _objc_msgSend$finishDiscoveryWith:
+ _objc_msgSend$intValue
+ _objc_msgSend$options
+ _objc_msgSend$setBluetoothAdvertisementData:
+ _objc_msgSend$setBluetoothRSSI:
+ _objc_msgSend$setDescriptor:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_msgSend$updatePickerWith:completionHandler:
+ _symbolic Sb
- GCC_except_table63
- GCC_except_table66
- __PROTOCOLS__TtC17AccessorySetupKit17ASUIClientWrapper.31
- ___67-[ASAccessorySession _showPickerForDisplayItems:completionHandler:]_block_invoke_4
- ___block_descriptor_48_e8_32r40r_e36_v32?0"ASPickerDisplayItem"8Q16^B24lr32l8r40l8
- _block_copy_helper.55
- _block_copy_helper.58
- _block_copy_helper.64
- _block_copy_helper.75
- _block_descriptor.57
- _block_descriptor.60
- _block_descriptor.66
- _block_descriptor.77
- _block_destroy_helper.56
- _block_destroy_helper.59
- _block_destroy_helper.65
- _block_destroy_helper.76
CStrings:
+ "%s can only be called if ASAccessorySession.pickerDisplaySettings.filterDiscoveryResultsInApp is true"
+ "-[ASAccessorySession finishPickerDiscovery:]_block_invoke"
+ "-[ASAccessorySession updatePickerShowingDiscoveredDisplayItems:completionHandler:]_block_invoke"
+ "@\"ASDiscoveredAccessory\""
+ "@\"NSDictionary\""
+ "@\"NSNumber\""
+ "ASDiscoveredAccessory"
+ "ASDiscoveredDisplayItem"
+ "ASMigrationDisplayItem must provide either peripheralIdentifier, hotspotSSID, or wifiAwarePairedDeviceID with wifiAwareServiceName in the ASDiscoveryDescriptor."
+ "ASMigrationDisplayItem's wifiAwarePairedDeviceID and wifiAwareServiceName in the descriptor cannot be used. 'WiFi' support not declared in Info.plist's NSAccessorySetupKitSupports."
+ "T@\"ASDiscoveredAccessory\",C,N,V_accessory"
+ "T@\"NSDictionary\",C,N,V_bluetoothAdvertisementData"
+ "T@\"NSNumber\",C,N,V_bluetoothRSSI"
+ "T@\"NSString\",C,N,V_name"
+ "T@\"UIImage\",C,N,V_productImage"
+ "TQ,N,V_options"
+ "Unbounded"
+ "_bluetoothAdvertisementData"
+ "_bluetoothRSSI"
+ "_discoveredAccessories"
+ "_finishDiscovery:"
+ "_options"
+ "_updatePickerWithDiscoveredDisplayItems:completionHandler:"
+ "accessory [%@]"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "bluetoothAdvertisementData"
+ "bluetoothRSSI"
+ "btAdv"
+ "btAdvData %@"
+ "btRSSI"
+ "btRSSI %@"
+ "dsAc"
+ "endDiscoveryInPicker"
+ "finishDiscoveryWith:"
+ "finishPickerDiscovery:"
+ "initWithName:productImage:accessory:"
+ "intValue"
+ "integerValue"
+ "options"
+ "pSOp"
+ "setBluetoothAdvertisementData:"
+ "setBluetoothRSSI:"
+ "setOptions:"
+ "setProductImage:"
+ "setWithArray:"
+ "showPermissionPromptCalled"
+ "showPickerWithOverrideBundleID:shouldRetrieveDisplayItems:needsBluetooth:needsWiFi:needsDeviceOTANameBroadcast:discoveryTimeout:filterInApp:"
+ "unarchivedObjectOfClasses:fromData:error:"
+ "updatePickerShowingDiscoveredDisplayItems:completionHandler:"
+ "updatePickerWith:"
+ "updatePickerWith:completionHandler:"
+ "v24@0:8@\"NSArray<__ASDiscoveredDisplayItem__>\"16"
+ "v72@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64"
+ "v72@0:8@16@24@32@40@48@56@64"
- "ASMigrationDisplayItem must provide either peripheralIdentifier or hotspotSSID."
- "Migration allowed to migrate Bluetooth accessories"
- "Migration not allowed since accessories are already authorized"
- "T@\"NSString\",R,C,N,V_name"
- "T@\"UIImage\",R,C,N,V_productImage"
- "TQ,R,N,V_wifiAwarePairedDeviceID"
- "showPickerWithOverrideBundleID:shouldRetrieveDisplayItems:needsBluetooth:needsWiFi:needsDeviceOTANameBroadcast:discoveryTimeout:"
- "v64@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56"

```
