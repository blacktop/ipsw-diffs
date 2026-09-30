## ConnectivityModule

> `/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule`

```diff

-598.0.0.0.0
-  __TEXT.__text: 0xfe2c
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x192c
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x194
-  __TEXT.__cstring: 0x121d
-  __TEXT.__oslogstring: 0x843
-  __TEXT.__unwind_info: 0x678
-  __TEXT.__objc_classname: 0x5a9
-  __TEXT.__objc_methname: 0x5be2
-  __TEXT.__objc_methtype: 0x1290
-  __TEXT.__objc_stubs: 0x3840
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x588
-  __DATA_CONST.__objc_classlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x98
+599.2.0.0.0
+  __TEXT.__text: 0xec10
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0x170c
+  __TEXT.__const: 0xf8
+  __TEXT.__gcc_except_tab: 0x154
+  __TEXT.__cstring: 0xfab
+  __TEXT.__oslogstring: 0x6c7
+  __TEXT.__unwind_info: 0x5e0
+  __TEXT.__objc_classname: 0x566
+  __TEXT.__objc_methname: 0x5a09
+  __TEXT.__objc_methtype: 0x1272
+  __TEXT.__objc_stubs: 0x37a0
+  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__const: 0x4c8
+  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11f0
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_selrefs: 0x11c0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x2e8
-  __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x1140
-  __AUTH_CONST.__objc_const: 0x4138
+  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0xf60
+  __AUTH_CONST.__objc_const: 0x3f08
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x198
-  __DATA.__data: 0x720
-  __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__bss: 0x40
+  __DATA.__objc_ivar: 0x17c
+  __DATA.__data: 0x780
+  __DATA_DIRTY.__objc_data: 0x410
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 592
-  Symbols:   230
-  CStrings:  1297
+  Functions: 542
+  Symbols:   218
+  CStrings:  1253
 
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_CCUIBluetoothModuleViewController
- _OBJC_CLASS_$_NSHashTable
- _OBJC_CLASS_$_WFControlCenterStateMonitor
- _OBJC_METACLASS_$_CCUIConnectivityBluetoothViewController
- _OBJC_METACLASS_$_CCUIConnectivityBluetoothDefaults
- _BluetoothStateChangedNotification
- _OBJC_CLASS_$_CCUIConnectivityBluetoothViewController
- _OBJC_CLASS_$_CCUIConnectivityBluetoothDefaults
- _OBJC_CLASS_$_CCUIBluetoothMenuModuleViewController
- _OBJC_CLASS_$_WFPersonalHotspotStateMonitor
- _OBJC_CLASS_$_NEVPNConnectivityManager
- _OBJC_CLASS_$_BluetoothManager
- _BluetoothConnectionStatusChangedNotification
- _OBJC_METACLASS_$_CCUIConnectivityManager
- _dispatch_get_global_queue
CStrings:
+ "ccui_safelyBeginAppearanceTransition:animated:"
+ "viewForInteraction"
+ "@\"CCUIBluetoothModuleViewController\""
+ "clickPresentationInteractionManagers"
+ "presentingMenuViewController"
+ "templateViewForExpandedConnectivityModule"
+ "setAlwaysExpanded:"
+ "T@\"NSString\",R,N"
+ "bluetoothModuleViewController"
+ "T@\"CCUIControlTemplateView\",R,N"
+ "buttonViewForCollapsedConnectivityModule"
+ "setPresentingMenuViewController:"
+ "_addViewControllers:forwardingAppearanceMethods:"
+ "TB,N,GisAvailable,V_available"
+ "accessibilityIdentifier"
+ "T@\"CCUIRoundButton\",R,N"
+ "setBluetoothModuleViewController:"
+ "@\"NSMutableSet\""
+ "T@\"CCUIBluetoothModuleViewController\",&,N,V_bluetoothModuleViewController"
+ "CCUIConnectivityStateUpdating"
+ "CCUIConnectivityModuleViewProviding"
+ "@\"CCUIRoundButton\"16@0:8"
+ "T@\"NSMutableSet\",&,N,V_clickPresentationInteractionManagers"
+ "_clickPresentationInteractionManagers"
+ "ccui_safelyEndAppearanceTransition"
+ "\x12/\x06"
+ "_bluetoothModuleViewController"
+ "setClickPresentationInteractionManagers:"
+ "TB,N,V_presentingMenuViewController"
+ "@\"CCUIControlTemplateView\"16@0:8"
- "CCUIConnectivityManager"
- "com.apple.ControlCenter.Bluetooth"
- "_vpnViewControllersObservingStateChanges"
- "busy"
- "removeObserver:name:object:"
- "v24@?0q8q16"
- "v12@?0i8"
- "CONTROL_CENTER_STATUS_BLUETOOTH_DEVICES"
- "_bluetoothStateDidChange:"
- "T@\"CCUIConnectivityManager\",R,N"
- "CONTROL_CENTER_BLUETOOTH_BEHAVIOR_ALERT_TITLE"
- "_bluetoothConnectionStatusDidChange:"
- "@20@0:8i16"
- "com.apple.control-center.BluetoothModule"
- "_bluetoothButtonViewController"
- "i20@0:8i16"
- "@\"BluetoothManager\""
- "T@\"NSHashTable\",&,N,V_wifiViewControllersObservingStateChanges"
- "_vpnConnectivityManager"
- "bluetoothButtonViewController"
- "removeObject:"
- "setBluetoothButtonViewController:"
- "CCUIConnectivityBluetoothViewController"
- "_updateConnectedDeviceNames"
- "T@\"NEVPNConnectivityManager\",R,N,V_vpnConnectivityManager"
- "setVpnViewControllersObservingStateChanges:"
- "CONTROL_CENTER_BLUETOOTH_BEHAVIOR_ALERT_MESSAGE"
- "v32@?0@\"CCUIConnectivityButtonViewController\"8Q16^B24"
- "_addButtonViewControllers:forwardingAppearanceMethods:"
- "_connectedDeviceNames"
- "_wifiStateMonitor"
- "@\"NEVPNConnectivityManager\""
- "@\"NSHashTable\""
- "CONTROL_CENTER_STATUS_BLUETOOTH_NAME"
- "bluetooth"
- "bluetooth.slash"
- "_wifiViewControllersObservingStateChanges"
- "CONTROL_CENTER_STATUS_BLUETOOTH_OFF"
- "B20@0:8i16"
- "bluetoothStateActionWithCompletion:"
- "[Bluetooth (Connectivity)] Toggle Bluetooth state from %!{(MISSING)public}@"
- "T@\"WFPersonalHotspotStateMonitor\",R,N,V_hotspotStateMonitor"
- "CCUIConnectivityBluetoothDefaults"
- "vpnViewControllersObservingStateChanges"
- "wifiViewControllersObservingStateChanges"
- "initWithDelegate:"
- "v24@0:8@\"NEVPNConnectivityManager\"16"
- "enumerateObjectsUsingBlock:"
- "_hotspotStateMonitor"
- "connectivityManagerDidChange:"
- "[Bluetooth (Connectivity)] Bluetooth connection status changed"
- "[Bluetooth (Connectivity)] Bluetooth state updated to %!{(MISSING)public}@ [ inoperative: %!d(MISSING) enabled: %!d(MISSING) subtitle: %!{(MISSING)private}@ ]"
- "CONTROL_CENTER_STATUS_MESSAGE_BLUETOOTH_CONNECTIONS_DISABLED"
- "setHandler:"
- "i16@0:8"
- "\x12/\x05"
- "bluetoothState"
- "[Bluetooth (Connectivity)] Toggled Bluetooth state from %!{(MISSING)public}@ to %!{(MISSING)public}@"
- "CONTROL_CENTER_STATUS_MESSAGE_BLUETOOTH_CONNECTIONS_ENABLED"
- "_glyphImageForState:"
- "CONTROL_CENTER_STATUS_BLUETOOTH_ON"
- "T@\"WFControlCenterStateMonitor\",R,N,V_wifiStateMonitor"
- "T@\"NSHashTable\",&,N,V_vpnViewControllersObservingStateChanges"
- "CONTROL_CENTER_STATUS_BLUETOOTH_BUSY"
- "setWifiViewControllersObservingStateChanges:"
- "TB,GisAvailable,V_available"
- "T@\"CCUIConnectivityButtonViewController\",&,N,V_bluetoothButtonViewController"
- "\x05"
- "[Bluetooth (Connectivity)] Bluetooth state changed"
- "NEVPNConnectivityManagerDelegate"
- "weakObjectsHashTable"
- "CONTROL_CENTER_STATUS_BLUETOOTH_DISCONNECTED"
- "_bluetoothManager"
- "connectedDeviceNamesThatMayBeDenylisted"

```
