## TrustedAccessory

> `/System/Library/PrivateFrameworks/TrustedAccessory.framework/Versions/A/TrustedAccessory`

```diff

-145.60.1.0.0
-  __TEXT.__text: 0xa9e4
+147.100.3.0.0
+  __TEXT.__text: 0xbbe0
   __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x4bc
+  __TEXT.__objc_methlist: 0x618
   __TEXT.__const: 0xd8
   __TEXT.__cstring: 0xa7b
   __TEXT.__oslogstring: 0xbb7
-  __TEXT.__gcc_except_tab: 0x250
-  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__gcc_except_tab: 0x294
+  __TEXT.__unwind_info: 0x2a0
   __TEXT.__objc_classname: 0xe7
   __TEXT.__objc_methname: 0xc6c
   __TEXT.__objc_methtype: 0x38f

   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x330
+  __DATA_CONST.__objc_selrefs: 0x3d0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x200
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0x1438
+  __AUTH_CONST.__objc_const: 0x11d0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x64

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A692228A-A4BE-30FF-9EEA-0AD49066D33D
-  Functions: 113
-  Symbols:   419
+  UUID: 84DDD153-8C57-3FC8-83DD-A1DCCF905E04
+  Functions: 240
+  Symbols:   573
   CStrings:  385
 
Symbols:
+ +[TADevice deviceWithUID:error:].cold.1
+ +[TADevice deviceWithUID:error:].cold.2
+ +[TADeviceManager initialize].cold.1
+ -[TADevice authorizeWithCredentialSet:error:].cold.1
+ -[TADevice authorizeWithCredentialSet:error:].cold.2
+ -[TADevice authorizeWithTicket:error:].cold.1
+ -[TADevice authorizeWithTicket:error:].cold.2
+ -[TADevice authorizeWithTicket:error:].cold.3
+ -[TADevice generateAuthorizationNonceWithError:].cold.1
+ -[TADevice generateAuthorizationNonceWithError:].cold.2
+ -[TADevice getNumberProperty:].cold.1
+ -[TADevice getStringProperty:].cold.1
+ -[TADevice getStringProperty:].cold.2
+ -[TADevice getStringProperty:].cold.3
+ -[TADevice init].cold.1
+ -[TADevice init].cold.2
+ -[TADevice isConnected:error:].cold.1
+ -[TADevice isConnected:error:].cold.2
+ -[TADevice isConnected:error:].cold.3
+ -[TADevice pairWithError:].cold.1
+ -[TADevice pairWithError:].cold.2
+ -[TADevice pairWithError:].cold.3
+ -[TADevice pairWithError:].cold.4
+ -[TADevice pairWithError:].cold.5
+ -[TADevice pairWithError:].cold.6
+ -[TADevice pairWithError:].cold.7
+ -[TADevice pairWithError:].cold.8
+ -[TADevice pairingState:error:].cold.1
+ -[TADevice pairingState:error:].cold.2
+ -[TADevice pairingState:error:].cold.3
+ -[TADeviceManager availablePairingSlotsWithError:].cold.1
+ -[TADeviceManager availablePairingSlotsWithError:].cold.2
+ -[TADeviceManager cancelOperation:].cold.1
+ -[TADeviceManager cancelOperation:].cold.2
+ -[TADeviceManager connectedDevicesWithFilter:].cold.1
+ -[TADeviceManager connectedDevicesWithFilter:].cold.10
+ -[TADeviceManager connectedDevicesWithFilter:].cold.11
+ -[TADeviceManager connectedDevicesWithFilter:].cold.12
+ -[TADeviceManager connectedDevicesWithFilter:].cold.13
+ -[TADeviceManager connectedDevicesWithFilter:].cold.14
+ -[TADeviceManager connectedDevicesWithFilter:].cold.15
+ -[TADeviceManager connectedDevicesWithFilter:].cold.16
+ -[TADeviceManager connectedDevicesWithFilter:].cold.2
+ -[TADeviceManager connectedDevicesWithFilter:].cold.3
+ -[TADeviceManager connectedDevicesWithFilter:].cold.4
+ -[TADeviceManager connectedDevicesWithFilter:].cold.5
+ -[TADeviceManager connectedDevicesWithFilter:].cold.6
+ -[TADeviceManager connectedDevicesWithFilter:].cold.7
+ -[TADeviceManager connectedDevicesWithFilter:].cold.8
+ -[TADeviceManager connectedDevicesWithFilter:].cold.9
+ -[TADeviceManager createSecureIntentOperationWithError:].cold.1
+ -[TADeviceManager init].cold.1
+ -[TADeviceManager init].cold.2
+ -[TADeviceManager operationFinished:].cold.1
+ -[TADeviceManager pairedDevices].cold.1
+ -[TADeviceManager pairedDevices].cold.2
+ -[TADeviceManager pairedDevices].cold.3
+ -[TADeviceManager pairedDevices].cold.4
+ -[TADeviceManager pairedDevices].cold.5
+ -[TADeviceManager pairedDevices].cold.6
+ -[TADeviceManager pairedDevices].cold.7
+ -[TADeviceManager startOperation:withData:].cold.1
+ -[TADeviceManager startOperation:withData:].cold.2
+ -[TADeviceManager startOperation:withData:].cold.3
+ -[TAManagerProxy init].cold.1
+ -[TAManagerProxy init].cold.2
+ -[TAManagerProxy prepareCommand:version:inValue:inData:inSize:command:].cold.1
+ -[TAManagerProxy prepareCommand:version:inValue:inData:inSize:command:].cold.2
+ -[TAManagerProxy prepareCommand:version:inValue:inData:inSize:command:].cold.3
+ -[TAManagerProxy prepareCommand:version:inValue:inData:inSize:command:].cold.4
+ -[TAManagerProxy prepareCommand:version:inValue:inData:inSize:command:].cold.5
+ -[TAManagerProxyBridge initializeConnection].cold.1
+ -[TAManagerProxyBridge initializeConnection].cold.2
+ -[TAManagerProxyBridge performCommand:method:version:inValue:inData:inSize:outData:outSize:].cold.1
+ -[TAManagerProxyBridge performCommand:method:version:inValue:inData:inSize:outData:outSize:].cold.2
+ -[TAManagerProxyBridge performCommand:method:version:inValue:inData:inSize:outData:outSize:].cold.3
+ -[TAManagerProxyDirect initializeConnection].cold.1
+ -[TAManagerProxyDirect initializeConnection].cold.2
+ -[TAManagerProxyDirect initializeConnection].cold.3
+ -[TAManagerProxyDirect initializeConnection].cold.4
+ -[TAManagerProxyDirect initializeConnection].cold.5
+ -[TAManagerProxyDirect performCommand:method:version:inValue:inData:inSize:outData:outSize:].cold.1
+ -[TAManagerProxyDirect performCommand:method:version:inValue:inData:inSize:outData:outSize:].cold.2
+ -[TAManagerProxyDirect performCommand:method:version:inValue:inData:inSize:outData:outSize:].cold.3
+ -[TAOperation cancelWithError:].cold.1
+ -[TAOperation cancelWithError:].cold.2
+ -[TAOperation initWithDeviceManager:].cold.1
+ -[TASecureIntentInfo initWithDevice:].cold.1
+ -[TASecureIntentOperation notification:withData:].cold.1
+ -[TASecureIntentOperation notification:withData:].cold.2
+ -[TASecureIntentOperation notification:withData:].cold.3
+ -[TASecureIntentOperation notification:withData:].cold.4
+ -[TASecureIntentOperation notification:withData:].cold.5
+ -[TASecureIntentOperation notification:withData:].cold.6
+ -[TASecureIntentOperation startWithError:].cold.1
+ -[TASecureIntentOperation startWithError:].cold.2
+ -[TASecureIntentOperation startWithError:].cold.3
+ GCC_except_table37
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __44-[TAManagerProxyDirect initializeConnection]_block_invoke.cold.1
+ __44-[TAManagerProxyDirect initializeConnection]_block_invoke.cold.2
+ __92-[TAManagerProxyBridge performCommand:method:version:inValue:inData:inSize:outData:outSize:]_block_invoke.139.cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/TrustedAccessory/TrustedAccessory/TADevice.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/TrustedAccessory/TrustedAccessory/TADeviceManager.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/TrustedAccessory/TrustedAccessory/TAManagerProxy.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/TrustedAccessory/TrustedAccessory/TAOperation.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrustedAccessory/TrustedAccessory/TADevice.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrustedAccessory/TrustedAccessory/TADeviceManager.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrustedAccessory/TrustedAccessory/TAManagerProxy.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrustedAccessory/TrustedAccessory/TAOperation.m"

```
