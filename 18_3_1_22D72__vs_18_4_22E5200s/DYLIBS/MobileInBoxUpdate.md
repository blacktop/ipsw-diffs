## MobileInBoxUpdate

> `/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate`

```diff

-61.0.0.0.0
-  __TEXT.__text: 0x21fec
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0xf7c
+63.100.13.502.1
+  __TEXT.__text: 0x26aa0
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_methlist: 0x1264
   __TEXT.__const: 0x1631
-  __TEXT.__cstring: 0xcc6
-  __TEXT.__oslogstring: 0x1969
-  __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__unwind_info: 0x608
+  __TEXT.__cstring: 0xef4
+  __TEXT.__oslogstring: 0x1c2e
+  __TEXT.__gcc_except_tab: 0x1c4
+  __TEXT.__unwind_info: 0x798
   __TEXT.__objc_classname: 0x1f5
-  __TEXT.__objc_methname: 0x238b
-  __TEXT.__objc_methtype: 0x52c
-  __TEXT.__objc_stubs: 0x23e0
+  __TEXT.__objc_methname: 0x256e
+  __TEXT.__objc_methtype: 0x58f
+  __TEXT.__objc_stubs: 0x24c0
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x16a8
+  __DATA_CONST.__const: 0x1710
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa50
+  __DATA_CONST.__objc_selrefs: 0xbd0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__objc_arraydata: 0x148
-  __AUTH_CONST.__auth_got: 0x420
+  __DATA_CONST.__objc_arraydata: 0x1a0
+  __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x19e0
-  __AUTH_CONST.__cfstring: 0xfa0
-  __AUTH_CONST.__objc_const: 0x2570
-  __AUTH_CONST.__objc_intobj: 0xc60
-  __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH_CONST.__const: 0x1f20
+  __AUTH_CONST.__cfstring: 0x12c0
+  __AUTH_CONST.__objc_const: 0x2210
+  __AUTH_CONST.__objc_intobj: 0xe70
+  __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x690
   __DATA.__objc_ivar: 0x168

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/NearField.framework/NearField

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 792
-  Symbols:   1460
-  CStrings:  901
+  Functions: 998
+  Symbols:   1712
+  CStrings:  971
 
Symbols:
+ _MIBUDeviceNFCInactivityTimeoutKey
+ _kMIBUClientLPMOptionScanPayload
+ _kMIBUNFCCommandGroupAddressKey
+ _kMIBUNFCCommandGroupPortKey
+ _kMIBUNFCCommandHostPortKey
+ _kMIBUNFCCommandInterfaceNameKey
+ _kMIBUNFCCommandRQBasicParametersKey
+ _kMIBUNFCCommandRQExtendedParametersKey
+ _kMIBUNFCCommandRQThresholdKey
+ _kMIBUNFCCommandServiceNameKey
+ _kMIBUNFCCommandTCPAddressKey
+ _kMIBUNFCCommandTCPPingIntervalKey
+ _kMIBUNFCCommandTCPPortKey
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke"
+ "-[MIBUClient shutdown:]_block_invoke"
+ "@32@0:8@16Q24"
+ "AssetPath"
+ "Configuring NFC with options %@"
+ "Deserialize authenticate command"
+ "EnablePipelineMode"
+ "Failed ss update serialization; payload missing %{public}@ key"
+ "Failed to deserialize SSUpdate command"
+ "Failed to deserialize authenticate command"
+ "Failed to deserialize basic param from command"
+ "Failed to deserialize extended param from command"
+ "Failed to deserialize group address from command"
+ "Failed to deserialize group port from command"
+ "Failed to deserialize host port from command"
+ "Failed to deserialize interface name from command"
+ "Failed to deserialize payload size from command"
+ "Failed to deserialize service name from command"
+ "Failed to deserialize ssUpdate command"
+ "GroupAddress"
+ "GroupPort"
+ "HostPort"
+ "InactivityTimeout can not be nil"
+ "InterfaceName"
+ "LPMScanPayload"
+ "RQBasicParameters"
+ "RQExtendedParameters"
+ "RQThreshold"
+ "S24@0:8@16"
+ "Serializing SSUpdate command"
+ "Serializing authenticate command"
+ "ServiceName"
+ "SoftwareUpdateAssetPath"
+ "SoftwareUpdateBrainAssetPath"
+ "SoftwareUpdateBrainXMLPath"
+ "SoftwareUpdateXMLPath"
+ "StatusServerHostAddress"
+ "StatusServerPortNumber"
+ "TCPAddress"
+ "TCPPingInterval"
+ "TCPPort"
+ "TCPUnicastAddress"
+ "TCPUnicastPort"
+ "UseSrNmForDeviceKey"
+ "_deserializeAuthenticate"
+ "_deserializeSSUpdate"
+ "_serializeAuthenticate"
+ "_serializeSSUpdate"
+ "adjustData:toLength:"
+ "assetPath"
+ "configureNFC:error:"
+ "enablePipelineMode"
+ "expectedAPDULength:"
+ "increaseLengthBy:"
+ "setLowPowerModeWithOptions:completion:"
+ "setToLPMWithOptions:reply:"
+ "shutdown: is only supported on internal builds"
+ "shutdownWithReply:"
+ "softwareUpdateAssetPath"
+ "softwareUpdateBrainAssetPath"
+ "softwareUpdateBrainXMLPath"
+ "softwareUpdateXMLPath"
+ "statusServerHostAddress"
+ "statusServerPortNumber"
+ "tcpUnicastAddress"
+ "tcpUnicastPort"
+ "useSrNmForDeviceKey"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@16@?24"
+ "v32@0:8@16^@24"

```
