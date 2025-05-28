## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-217.51.1.0.0
-  __TEXT.__text: 0x53438
+217.60.6.0.0
+  __TEXT.__text: 0x5392c
   __TEXT.__auth_stubs: 0xa60
   __TEXT.__objc_methlist: 0x2294
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x15acf
+  __TEXT.__cstring: 0x15e4e
   __TEXT.__gcc_except_tab: 0x114
   __TEXT.__oslogstring: 0x3a7
-  __TEXT.__unwind_info: 0xca8
-  __TEXT.__objc_classname: 0x291
-  __TEXT.__objc_methname: 0xa4ae
+  __TEXT.__unwind_info: 0xcac
+  __TEXT.__objc_classname: 0x293
+  __TEXT.__objc_methname: 0xa4f4
   __TEXT.__objc_methtype: 0xf8c
   __TEXT.__objc_stubs: 0x6a20
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x12c0
+  __DATA_CONST.__const: 0x12e8
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6368
+  __DATA_CONST.__objc_const: 0x6408
   __DATA_CONST.__objc_selrefs: 0x2150
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x240
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x210
-  __AUTH_CONST.__cfstring: 0x40a0
+  __AUTH_CONST.__cfstring: 0x44c0
   __AUTH_CONST.__objc_const: 0x780
   __AUTH_CONST.__const: 0x680
   __AUTH_CONST.__objc_arrayobj: 0x30

   __AUTH_CONST.__auth_got: 0x540
   __AUTH.__objc_data: 0x4b0
   __AUTH.__data: 0x288
-  __DATA.__objc_ivar: 0x878
+  __DATA.__objc_ivar: 0x88c
   __DATA.__data: 0x968
   __DATA.__common: 0x10
   __DATA.__bss: 0x510

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   Functions: 1278
-  Symbols:   4800
-  CStrings:  4528
+  Symbols:   4806
+  CStrings:  4573
 
Symbols:
+ -[HDSDeviceOperationHomeKitSetup _completeWithError:errorLabel:]
+ _OBJC_IVAR_$_HDSSetupSession._wifiCCA
+ _OBJC_IVAR_$_HDSSetupSession._wifiChannel
+ _OBJC_IVAR_$_HDSSetupSession._wifiOUI
+ _OBJC_IVAR_$_HDSSetupSession._wifiRSSI
+ _OBJC_IVAR_$_HDSSetupSession._wifiSecurityString
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke.1363
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1497
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1498
+ ___block_descriptor_40_e8_32s_e30_v24?0"NSError"8"NSString"16ls32l8
+ ___block_literal_global.1365
+ ___block_literal_global.2913
+ ___block_literal_global.2917
+ ___block_literal_global.2921
+ ___block_literal_global.2925
+ ___block_literal_global.2929
+ ___block_literal_global.2945
+ ___block_literal_global.2949
+ ___block_literal_global.2962
+ ___block_literal_global.2966
+ ___block_literal_global.2970
+ ___block_literal_global.2974
+ ___block_literal_global.3003
+ ___block_literal_global.3007
+ ___block_literal_global.3013
+ ___block_literal_global.3018
+ ___block_literal_global.3022
+ ___block_literal_global.3027
+ ___block_literal_global.3042
+ ___block_literal_global.3046
+ ___block_literal_global.3141
+ ___block_literal_global.756
+ ___block_literal_global.760
+ ___block_literal_global.767
+ ___block_literal_global.776
+ __unnamed_array_storage.1106
+ __unnamed_array_storage.1107
+ __unnamed_array_storage.1129
+ __unnamed_array_storage.1130
+ __unnamed_array_storage.1140
+ __unnamed_array_storage.1141
+ __unnamed_array_storage.1194
+ __unnamed_array_storage.1195
+ __unnamed_array_storage.1441
+ __unnamed_array_storage.1909
+ __unnamed_array_storage.1910
+ __unnamed_array_storage.1960
+ __unnamed_array_storage.1961
+ __unnamed_array_storage.831
+ __unnamed_array_storage.853
+ __unnamed_array_storage.854
+ _objc_msgSend$_completeWithError:errorLabel:
- -[HDSDeviceOperationHomeKitSetup _completeWithError:]
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke.1345
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1478
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1479
- ___block_literal_global.1347
- ___block_literal_global.2886
- ___block_literal_global.2890
- ___block_literal_global.2894
- ___block_literal_global.2898
- ___block_literal_global.2902
- ___block_literal_global.2918
- ___block_literal_global.2922
- ___block_literal_global.2935
- ___block_literal_global.2939
- ___block_literal_global.2943
- ___block_literal_global.2947
- ___block_literal_global.2964
- ___block_literal_global.2976
- ___block_literal_global.2980
- ___block_literal_global.2986
- ___block_literal_global.2995
- ___block_literal_global.3000
- ___block_literal_global.3015
- ___block_literal_global.3019
- ___block_literal_global.3114
- ___block_literal_global.672
- ___block_literal_global.676
- ___block_literal_global.683
- ___block_literal_global.692
- __unnamed_array_storage.1085
- __unnamed_array_storage.1086
- __unnamed_array_storage.1108
- __unnamed_array_storage.1109
- __unnamed_array_storage.1119
- __unnamed_array_storage.1120
- __unnamed_array_storage.1173
- __unnamed_array_storage.1174
- __unnamed_array_storage.1423
- __unnamed_array_storage.1887
- __unnamed_array_storage.1888
- __unnamed_array_storage.1938
- __unnamed_array_storage.1939
- __unnamed_array_storage.810
- __unnamed_array_storage.811
- __unnamed_array_storage.833
- _objc_msgSend$_completeWithError:
CStrings:
+ "\x1143!\x11!232\x11\x13\x11\x1111\xf0%1Q3A\xe1!!\x81\x81a!sAQ\x11R\x13\x13/\x0f\x01"
+ "-[HDSDeviceOperationHomeKitSetup _completeWithError:errorLabel:]"
+ "Force-Failure"
+ "HDS-HK-AddAccessory"
+ "HDS-HK-AddAppData"
+ "HDS-HK-AddHome"
+ "HDS-HK-AddRoomWithName"
+ "HDS-HK-AppData-NoHKAccessory"
+ "HDS-HK-AssignRoom"
+ "HDS-HK-DeviceSetup-NoHKAccessory"
+ "HDS-HK-KeychainNotEnabled"
+ "HDS-HK-NoAccessory"
+ "HDS-HK-NoAudioDestination"
+ "HDS-HK-NoRoomName"
+ "HDS-HK-NoTR"
+ "HDS-HK-NotHomeOwner"
+ "HDS-HK-NotOwner"
+ "HDS-HK-Odeon"
+ "HDS-HK-Odeon-NoAudioDestinationController"
+ "HDS-HK-PR-CreateAccessFail"
+ "HDS-HK-PR-UpdateAccessControlFailed"
+ "HDS-HK-RequiresConfigurationReset"
+ "HDS-HK-RoomSelection"
+ "HDS-HK-StereoPair"
+ "HDS-HK-StereoPair-NoMediaSystem"
+ "HDS-HK-StereoPair-Preflights"
+ "HDS-HK-TimeOut"
+ "HDS-HK-ULH-CreateAccessFail"
+ "HDS-HK-ULH-UpdateAccessControlFailed"
+ "NoAccessory"
+ "NoLabel"
+ "None"
+ "WiFi OUI not found\n"
+ "WiFi RSSI not found\n"
+ "WiFi Security String not found\n"
+ "WiFi cca not found\n"
+ "WiFi channel not found\n"
+ "_completeWithError:errorLabel:"
+ "_wifiCCA"
+ "_wifiChannel"
+ "_wifiOUI"
+ "_wifiRSSI"
+ "_wifiSecurityString"
+ "cca"
+ "iTunes Auth Failed, skipping since HomePod is possible Dalaman\n"
+ "oui"
+ "rssi"
+ "securityStr"
+ "v24@?0@\"NSError\"8@\"NSString\"16"
- "\x1143!\x11!232\x11\x13\x11\x1111\xf0%1Q3A\xe1!!\x81\x81a!sAr\x13\x13/\x0f\x01"
- "-[HDSDeviceOperationHomeKitSetup _completeWithError:]"
- "_completeWithError:"

```
