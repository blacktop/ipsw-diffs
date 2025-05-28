## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

```diff

-367.0.9.0.0
-  __TEXT.__text: 0x460bc
+367.10.21.0.0
+  __TEXT.__text: 0x465f8
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x5440
-  __TEXT.__const: 0x3a0
-  __TEXT.__cstring: 0x24d1
-  __TEXT.__oslogstring: 0x3b8d
+  __TEXT.__objc_methlist: 0x5450
+  __TEXT.__const: 0x3c0
+  __TEXT.__cstring: 0x24f1
+  __TEXT.__oslogstring: 0x3c43
   __TEXT.__gcc_except_tab: 0x3cc
-  __TEXT.__unwind_info: 0xff0
+  __TEXT.__unwind_info: 0x1000
   __TEXT.__objc_classname: 0xd09
-  __TEXT.__objc_methname: 0xfa9e
+  __TEXT.__objc_methname: 0xfab8
   __TEXT.__objc_methtype: 0x294d
-  __TEXT.__objc_stubs: 0xb9e0
+  __TEXT.__objc_stubs: 0xba00
   __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x990
+  __DATA_CONST.__const: 0x970
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xa4c0
-  __DATA_CONST.__objc_selrefs: 0x3930
+  __DATA_CONST.__objc_selrefs: 0x3938
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__cfstring: 0x28a0
+  __AUTH_CONST.__cfstring: 0x28e0
   __AUTH_CONST.__objc_const: 0x1d38
-  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__const: 0x480
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_intobj: 0xd8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1927
-  Symbols:   7149
-  CStrings:  3857
+  Functions: 1933
+  Symbols:   7160
+  CStrings:  3865
 
Symbols:
+ -[TVRUICoreDevice hash]
+ -[TVRUIDevicePickerViewController _updateDevicesWithSuggestionsAndReload].cold.1
+ -[TVRUIDevicePickerViewController _updateDevicesWithSuggestionsAndReload].cold.2
+ -[TVRUIDevicePickerViewController _updateDevicesWithSuggestionsAndReload].cold.3
+ -[TVRUINetworkObserver _wifiStateUpdatedWithOldState:newState:]
+ -[TVRUINetworkObserver setWifiStateUpdatedHandler:]
+ -[TVRUINetworkObserver wifiStateUpdatedHandler]
+ -[TVRUIRemoteViewController wifiStateDidUpdate:]
+ -[TVRUITitleView _updateDeviceNameAutomationIdentifier:]
+ _OBJC_IVAR_$_TVRUINetworkObserver._wifiStateUpdatedHandler
+ ___46-[TVRUIRemoteViewController _showFindingAlert]_block_invoke.185
+ ___58-[TVRUIRemoteViewController _setupNetworkObserverIfNeeded]_block_invoke.158
+ ___63-[TVRUINetworkObserver _wifiStateUpdatedWithOldState:newState:]_block_invoke
+ ___63-[TVRUINetworkObserver _wifiStateUpdatedWithOldState:newState:]_block_invoke.22
+ ___block_literal_global.62
+ _objc_msgSend$_updateDeviceNameAutomationIdentifier:
+ _objc_msgSend$_wifiStateUpdatedWithOldState:newState:
+ _objc_msgSend$setHitTestInsets:
+ _objc_msgSend$setWifiStateUpdatedHandler:
+ _objc_msgSend$wifiStateDidUpdate:
+ _objc_msgSend$wifiStateUpdatedHandler
- -[TVRUINetworkObserver _updateNetworkReachability:]
- -[TVRUINetworkObserver _wifiStateUpdatedWithOldState:andNewState:]
- -[TVRUINetworkObserver reachabilityDidUpdate]
- -[TVRUINetworkObserver setReachabilityDidUpdate:]
- -[TVRUIRemoteViewController networkReachabilityDidUpdate:]
- _OBJC_IVAR_$_TVRUINetworkObserver._reachabilityDidUpdate
- ___46-[TVRUIRemoteViewController _showFindingAlert]_block_invoke_2
- ___51-[TVRUINetworkObserver _updateNetworkReachability:]_block_invoke
- ___58-[TVRUIRemoteViewController _setupNetworkObserverIfNeeded]_block_invoke.157
- ___66-[TVRUINetworkObserver _wifiStateUpdatedWithOldState:andNewState:]_block_invoke
- ___block_descriptor_32_e23_v16?0"UIAlertAction"8l
- ___block_literal_global.182
- ___block_literal_global.55
- _objc_msgSend$_updateNetworkReachability:
- _objc_msgSend$_wifiStateUpdatedWithOldState:andNewState:
- _objc_msgSend$networkReachabilityDidUpdate:
- _objc_msgSend$reachabilityDidUpdate
- _objc_msgSend$setReachabilityDidUpdate:
CStrings:
+ "Adding connected device: %@"
+ "Adding suggested device: %@"
+ "Network observer reported reachability update, state=%ld, reachable=%d"
+ "T@?,C,N,V_wifiStateUpdatedHandler"
+ "User requested to continue looking for the remote. Restarting finding session"
+ "User requested to stop finding remote"
+ "_updateDeviceNameAutomationIdentifier:"
+ "_wifiStateUpdatedHandler"
+ "_wifiStateUpdatedWithOldState:newState:"
+ "deviceTable"
+ "devices: %@"
+ "selectedDevice=\"%@\""
+ "setHitTestInsets:"
+ "setWifiStateUpdatedHandler:"
+ "suggested devices: %@"
+ "wifiStateDidUpdate:"
+ "wifiStateUpdatedHandler"
- "Network observer reported reachability update, reachable=%d"
- "Network reachability changed to %@"
- "T@?,C,N,V_reachabilityDidUpdate"
- "_reachabilityDidUpdate"
- "_updateNetworkReachability:"
- "_wifiStateUpdatedWithOldState:andNewState:"
- "networkReachabilityDidUpdate:"
- "reachabilityDidUpdate"
- "setReachabilityDidUpdate:"

```
