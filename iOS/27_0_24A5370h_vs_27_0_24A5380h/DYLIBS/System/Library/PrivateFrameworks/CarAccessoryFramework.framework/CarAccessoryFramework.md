## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-  __TEXT.__text: 0x10a3cc
-  __TEXT.__objc_methlist: 0x18c44
+  __TEXT.__text: 0x10bed4
+  __TEXT.__objc_methlist: 0x18e9c
   __TEXT.__const: 0x1b8
   __TEXT.__gcc_except_tab: 0x53c
-  __TEXT.__oslogstring: 0x3c7c
-  __TEXT.__cstring: 0x7e43
+  __TEXT.__oslogstring: 0x3cb5
+  __TEXT.__cstring: 0x7e6f
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x3b60
+  __TEXT.__unwind_info: 0x3bb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x26c8
-  __DATA_CONST.__objc_classlist: 0xdb8
+  __DATA_CONST.__const: 0x26f8
+  __DATA_CONST.__objc_classlist: 0xdc0
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x610
+  __DATA_CONST.__objc_protolist: 0x618
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7cc8
-  __DATA_CONST.__objc_protorefs: 0x5b0
-  __DATA_CONST.__objc_superrefs: 0x7e0
-  __DATA_CONST.__objc_arraydata: 0xbc98
-  __DATA_CONST.__got: 0xef8
+  __DATA_CONST.__objc_selrefs: 0x7d18
+  __DATA_CONST.__objc_protorefs: 0x5b8
+  __DATA_CONST.__objc_superrefs: 0x7e8
+  __DATA_CONST.__objc_arraydata: 0xc168
+  __DATA_CONST.__got: 0xf00
   __AUTH_CONST.__const: 0xac0
-  __AUTH_CONST.__cfstring: 0xddc0
-  __AUTH_CONST.__objc_const: 0x4f528
+  __AUTH_CONST.__cfstring: 0xde00
+  __AUTH_CONST.__objc_const: 0x4fbe8
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x690
-  __AUTH_CONST.__objc_dictobj: 0x64a0
+  __AUTH_CONST.__objc_dictobj: 0x6630
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x2da0
-  __DATA.__objc_ivar: 0x680
-  __DATA.__data: 0x48e0
-  __DATA.__bss: 0x3e0
-  __DATA_DIRTY.__objc_data: 0x5b90
-  __DATA_DIRTY.__bss: 0x118
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x684
+  __DATA.__data: 0x4940
+  __DATA.__bss: 0x3d0
+  __DATA_DIRTY.__objc_data: 0x8930
+  __DATA_DIRTY.__bss: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7693
-  Symbols:   25547
-  CStrings:  3945
+  Functions: 7734
+  Symbols:   25662
+  CStrings:  3950
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
Symbols:
+ +[CAFButtonActionStatusItem observerProtocol]
+ +[CAFButtonActionStatusItem serviceIdentifier]
+ -[CAFASCTree nightModeByDisplayID]
+ -[CAFBluetoothStatus buttonActionCharacteristic]
+ -[CAFBluetoothStatus buttonAction]
+ -[CAFBluetoothStatus hasButtonAction]
+ -[CAFBluetoothStatus registeredForButtonAction]
+ -[CAFBluetoothStatus setButtonAction:]
+ -[CAFButtonActionStatusItem _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFButtonActionStatusItem addObserver:]
+ -[CAFButtonActionStatusItem buttonActionCharacteristic]
+ -[CAFButtonActionStatusItem buttonAction]
+ -[CAFButtonActionStatusItem name]
+ -[CAFButtonActionStatusItem registerObserver:]
+ -[CAFButtonActionStatusItem registeredForButtonAction]
+ -[CAFButtonActionStatusItem removeObserver:]
+ -[CAFButtonActionStatusItem setButtonAction:]
+ -[CAFButtonActionStatusItem unregisterObserver:]
+ -[CAFCellularStatus buttonActionCharacteristic]
+ -[CAFCellularStatus buttonAction]
+ -[CAFCellularStatus hasButtonAction]
+ -[CAFCellularStatus registeredForButtonAction]
+ -[CAFCellularStatus setButtonAction:]
+ -[CAFCurrentUserStatus buttonActionCharacteristic]
+ -[CAFCurrentUserStatus buttonAction]
+ -[CAFCurrentUserStatus hasButtonAction]
+ -[CAFCurrentUserStatus registeredForButtonAction]
+ -[CAFCurrentUserStatus setButtonAction:]
+ -[CAFStatusIndicators buttonActionStatusItemServices]
+ -[CAFStatusIndicators buttonActionStatusItems]
+ -[CAFWiFiStatus buttonActionCharacteristic]
+ -[CAFWiFiStatus buttonAction]
+ -[CAFWiFiStatus hasButtonAction]
+ -[CAFWiFiStatus registeredForButtonAction]
+ -[CAFWiFiStatus setButtonAction:]
+ -[CAFWirelessChargerStatus buttonActionCharacteristic]
+ -[CAFWirelessChargerStatus buttonAction]
+ -[CAFWirelessChargerStatus hasButtonAction]
+ -[CAFWirelessChargerStatus registeredForButtonAction]
+ -[CAFWirelessChargerStatus setButtonAction:]
+ _CAFServiceTypeButtonActionStatusItem
+ _OBJC_CLASS_$_CAFButtonActionStatusItem
+ _OBJC_IVAR_$_CAFASCTree._nightModeByDisplayID
+ _OBJC_METACLASS_$_CAFButtonActionStatusItem
+ __OBJC_$_CLASS_METHODS_CAFButtonActionStatusItem
+ __OBJC_$_INSTANCE_METHODS_CAFButtonActionStatusItem
+ __OBJC_$_PROP_LIST_CAFButtonActionStatusItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFButtonActionStatusItemObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFButtonActionStatusItemObserver
+ __OBJC_$_PROTOCOL_REFS_CAFButtonActionStatusItemObserver
+ __OBJC_CLASS_RO_$_CAFButtonActionStatusItem
+ __OBJC_LABEL_PROTOCOL_$_CAFButtonActionStatusItemObserver
+ __OBJC_METACLASS_RO_$_CAFButtonActionStatusItem
+ __OBJC_PROTOCOL_$_CAFButtonActionStatusItemObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFButtonActionStatusItemObserver
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e15_v32?08Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
+ _objc_msgSend$bluetoothStatusService:didUpdateButtonAction:
+ _objc_msgSend$buttonActionStatusItemService:didUpdateButtonAction:
+ _objc_msgSend$buttonActionStatusItemServices
+ _objc_msgSend$cellularStatusService:didUpdateButtonAction:
+ _objc_msgSend$currentUserStatusService:didUpdateButtonAction:
+ _objc_msgSend$wiFiStatusService:didUpdateButtonAction:
+ _objc_msgSend$wirelessChargerStatusService:didUpdateButtonAction:
CStrings:
+ "0x0000000016100009"
+ "ButtonActionStatusItem"
+ "[NightModeSeed] parsed displayID=%{public}@ nightMode=%@"

```
