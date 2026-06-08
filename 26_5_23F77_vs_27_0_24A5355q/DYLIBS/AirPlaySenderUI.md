## AirPlaySenderUI

> `/System/Library/PrivateFrameworks/AirPlaySenderUI.framework/AirPlaySenderUI`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0x10dc
-  __TEXT.__auth_stubs: 0x170
+980.58.1.11.1
+  __TEXT.__text: 0xfe8
   __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x33f
+  __TEXT.__cstring: 0x345
   __TEXT.__unwind_info: 0xc8
-  __TEXT.__objc_classname: 0xb6
-  __TEXT.__objc_methname: 0x4f6
-  __TEXT.__objc_methtype: 0xda
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0x50
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
-  __AUTH_CONST.__auth_got: 0xc0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x240
   __AUTH_CONST.__objc_const: 0x520
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x70

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CE700B29-E1E8-3358-AD9E-6CDF191403A6
+  UUID: FEA3BFDC-4817-30E0-9E59-1477A80B74B5
   Functions: 46
-  Symbols:   213
-  CStrings:  130
+  Symbols:   212
+  CStrings:  48
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ -[APUIAirPlaySetupConfigurationWiFi copyWithZone:] : 176 -> 164
~ -[APUIAirPlaySetupConfigurationWiFi description] : 408 -> 376
~ -[APUIAirPlaySetupConfigurationDiscoveryBroker copyWithZone:] : 140 -> 132
~ -[APUIAirPlaySetupConfigurationDiscoveryBroker description] : 232 -> 212
~ -[APUIAirPlaySetupConfigurationReceiver copyWithZone:] : 160 -> 152
~ -[APUIAirPlaySetupConfigurationReceiver description] : 256 -> 240
~ -[APUIAirPlaySetupConfiguration urlString] : 1000 -> 884
~ -[APUIAirPlaySetupConfiguration description] : 180 -> 164
~ +[APUIAirPlaySetupFlowLauncher launchAirPlayAutomaticSetupFlowWithConfiguration:] : 356 -> 344
~ +[APUIAirPlaySetupFlowLauncher launchAirPlaySetupFlowWithUserInfo:] : 276 -> 272
CStrings:
- ".cxx_destruct"
- "@\"APUIAirPlaySetupConfigurationDiscoveryBroker\""
- "@\"APUIAirPlaySetupConfigurationReceiver\""
- "@\"APUIAirPlaySetupConfigurationWiFi\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8^{_NSZone=}16"
- "APUIAirPlaySetupConfiguration"
- "APUIAirPlaySetupConfigurationDiscoveryBroker"
- "APUIAirPlaySetupConfigurationReceiver"
- "APUIAirPlaySetupConfigurationWiFi"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "ID"
- "SSID"
- "T@\"APUIAirPlaySetupConfigurationDiscoveryBroker\",C,N,V_broker"
- "T@\"APUIAirPlaySetupConfigurationReceiver\",C,N,V_receiver"
- "T@\"APUIAirPlaySetupConfigurationWiFi\",C,N,V_wifi"
- "T@\"NSString\",C,N,V_ID"
- "T@\"NSString\",C,N,V_SSID"
- "T@\"NSString\",C,N,V_authString"
- "T@\"NSString\",C,N,V_authToken"
- "T@\"NSString\",C,N,V_captivePortalBypassToken"
- "T@\"NSString\",C,N,V_passphrase"
- "TB,N,V_routeToReceiverAfterSetup"
- "URLWithString:"
- "_ID"
- "_SSID"
- "_authString"
- "_authToken"
- "_broker"
- "_captivePortalBypassToken"
- "_passphrase"
- "_receiver"
- "_routeToReceiverAfterSetup"
- "_wifi"
- "activateWithContext:"
- "addObject:"
- "allocWithZone:"
- "array"
- "authString"
- "authToken"
- "broker"
- "captivePortalBypassToken"
- "copyWithZone:"
- "defaultWorkspace"
- "description"
- "init"
- "initWithServiceName:viewControllerClassName:"
- "launchAirPlayAutomaticSetupFlowWithConfiguration:"
- "launchAirPlayManualSetupFlowForDiscoveryBroker:"
- "launchAirPlaySetupFlowWithUserInfo:"
- "newHandleWithDefinition:configurationContext:"
- "openSensitiveURL:withOptions:"
- "passphrase"
- "queryItemWithName:value:"
- "receiver"
- "routeToReceiverAfterSetup"
- "setAuthString:"
- "setAuthToken:"
- "setBroker:"
- "setCaptivePortalBypassToken:"
- "setHost:"
- "setID:"
- "setPassphrase:"
- "setQueryItems:"
- "setReason:"
- "setReceiver:"
- "setRouteToReceiverAfterSetup:"
- "setSSID:"
- "setScheme:"
- "setUserInfo:"
- "setWifi:"
- "string"
- "stringWithFormat:"
- "urlString"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "wifi"

```
