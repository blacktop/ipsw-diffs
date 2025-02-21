## CoreUARP

> `/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x82340
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x8178
-  __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x6ccd
-  __TEXT.__oslogstring: 0x5bca
+1207.100.54.502.1
+  __TEXT.__text: 0x84970
+  __TEXT.__auth_stubs: 0x9e0
+  __TEXT.__objc_methlist: 0x88cc
+  __TEXT.__const: 0x230
+  __TEXT.__cstring: 0x6fc1
+  __TEXT.__oslogstring: 0x5e78
   __TEXT.__gcc_except_tab: 0x810
   __TEXT.__dlopen_cstrs: 0x10e
-  __TEXT.__unwind_info: 0x2420
-  __TEXT.__objc_classname: 0x17fe
-  __TEXT.__objc_methname: 0xd757
-  __TEXT.__objc_methtype: 0x39b7
-  __TEXT.__objc_stubs: 0x9420
-  __DATA_CONST.__got: 0x718
-  __DATA_CONST.__const: 0x1e00
-  __DATA_CONST.__objc_classlist: 0x648
+  __TEXT.__unwind_info: 0x24b8
+  __TEXT.__objc_classname: 0x18a7
+  __TEXT.__objc_methname: 0xdb0e
+  __TEXT.__objc_methtype: 0x3a45
+  __TEXT.__objc_stubs: 0x95c0
+  __DATA_CONST.__got: 0x738
+  __DATA_CONST.__const: 0x1e60
+  __DATA_CONST.__objc_classlist: 0x680
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2eb0
+  __DATA_CONST.__objc_selrefs: 0x3018
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x638
-  __AUTH_CONST.__auth_got: 0x498
+  __DATA_CONST.__objc_superrefs: 0x670
+  __AUTH_CONST.__auth_got: 0x500
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x6d20
-  __AUTH_CONST.__objc_const: 0x11a30
-  __AUTH_CONST.__objc_intobj: 0xc60
-  __AUTH.__objc_data: 0x2030
-  __DATA.__objc_ivar: 0xb64
+  __AUTH_CONST.__cfstring: 0x6ea0
+  __AUTH_CONST.__objc_const: 0x117d0
+  __AUTH_CONST.__objc_intobj: 0xc90
+  __AUTH.__objc_data: 0x2120
+  __DATA.__objc_ivar: 0xb90
   __DATA.__data: 0x40d
   __DATA.__bss: 0x1a5b
-  __DATA_DIRTY.__objc_data: 0x1ea0
+  __DATA_DIRTY.__objc_data: 0x1fe0
   __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 3712
-  Symbols:   4737
-  CStrings:  4676
+  Functions: 3779
+  Symbols:   4853
+  CStrings:  4766
 
Symbols:
+ _OBJC_CLASS_$_UARPAccessoryHardwareIPv4
+ _OBJC_CLASS_$_UARPAccessoryHardwareIPv6
+ _OBJC_CLASS_$_UARPAccessoryHardwareSerial
+ _OBJC_CLASS_$_UARPIPDevice
+ _OBJC_CLASS_$_UARPSuperBinaryPlist
+ _OBJC_CLASS_$_UARPSupportedAccessoryAirTag
+ _OBJC_CLASS_$_UARPSupportedAccessoryIP
+ _OBJC_METACLASS_$_UARPAccessoryHardwareIPv4
+ _OBJC_METACLASS_$_UARPAccessoryHardwareIPv6
+ _OBJC_METACLASS_$_UARPAccessoryHardwareSerial
+ _OBJC_METACLASS_$_UARPIPDevice
+ _OBJC_METACLASS_$_UARPSuperBinaryPlist
+ _OBJC_METACLASS_$_UARPSupportedAccessoryAirTag
+ _OBJC_METACLASS_$_UARPSupportedAccessoryIP
+ ___error
+ __dispatch_source_type_read
+ _close
+ _connect
+ _dispatch_source_get_data
+ _dispatch_source_set_cancel_handler
+ _inet_pton
+ _kUARPStringMetadataDevicePayloadOrderedIndex
+ _kUARPStringMetadataDeviceTlvFlashSectionLength
+ _kUARPStringMobileAssetAssetsKey
+ _kUARPStringMobileAssetDeploymentCountryListKey
+ _kUARPStringMobileAssetDeploymentDeploymentLimitKey
+ _kUARPStringMobileAssetDeploymentGoLiveDateKey
+ _kUARPStringMobileAssetDeploymentRampPeriodKey
+ _kUARPStringPersonalizationOptionUIDMode
+ _kUARPSupportedAccessoryKeyTransportIP
+ _kUARPSupportedAccessoryKeyTransportSerial
+ _malloc_type_malloc
+ _objc_retainAutoreleasedReturnValue
+ _recv
+ _send
+ _setsockopt
+ _socket
+ _strerror
CStrings:
+ "\x05\x16"
+ "%s: Failed receive UARP message, closing socket"
+ "%s: Failed to connect"
+ "%s: Failed to connect on socket: %s"
+ "%s: Failed to create dispatch_source_t"
+ "%s: Failed to initialize deployment limits with error %@"
+ "%s: Failed to initialize recvSource"
+ "%s: Failed to initialize socket"
+ "%s: Failed to receive UARP Message Header on connected socket: %s"
+ "%s: Failed to receive UARP Message Payload on connected socket: %s"
+ "%s: Failed to send UARP Message on connected socket"
+ "%s: Failed to set socket option SO_NOSIGPIPE for socket: %s"
+ "%s: Failed to set socket option SO_RCVTIMEO for socket: %s"
+ "%s: Generating Read Sandbox Extension Token for %@ "
+ "%s: UARP Message Payload length exceeds maximum (%u bytes)"
+ "%s: failed to consume sandbox token"
+ "+[UARPSandboxExtension readTokenStringWithURL:]"
+ "-[UARPDeploymentRule initWithConfig:]"
+ "-[UARPIPDevice connect]"
+ "-[UARPIPDevice initRecvSource]"
+ "-[UARPIPDevice initRecvSource]_block_invoke"
+ "-[UARPIPDevice initWithIPAddress:port:delegate:]"
+ "-[UARPIPDevice recvUARPMsg]"
+ "-[UARPIPDevice sendData:]_block_invoke"
+ "@\"<UARPIPDeviceDelegate>\""
+ "@32@0:8@16o^@24"
+ "@36@0:8@16S24@28"
+ "@40@0:8@16S24C28@32"
+ "Assets"
+ "B28@0:8@16S24"
+ "CrystalSeedUpdate"
+ "Flash Section Length"
+ "IPv4"
+ "IPv6"
+ "Invalid Deployment Rule: Deployment Limit %lu for %@ with Go Live Date %@ is invalid, must be strictly increasing"
+ "Invalid Deployment Rule: Deployment Limit already set on Go Live Date %@ for %@"
+ "Invalid Deployment Rule: Deployment already scheduled for full deployment for %@"
+ "Payload Ordered Index"
+ "Serial"
+ "T@\"NSMutableDictionary\",C,V_deploymentLimits"
+ "T@\"NSString\",C,V_currentISOCountryCode"
+ "TB,V_isFullyDeployedDeploymentLimits"
+ "UARPAccessoryHardwareIPv4"
+ "UARPAccessoryHardwareIPv6"
+ "UARPAccessoryHardwareSerial"
+ "UARPIPDevice"
+ "UARPSuperBinaryPlist"
+ "UARPSupportedAccessoryAirTag"
+ "UARPSupportedAccessoryIP"
+ "UID_MODE"
+ "^{sockaddr=CC[14c]}"
+ "_deploymentLimits"
+ "_isFullyDeployedDeploymentLimits"
+ "_recvSource"
+ "_sbDict"
+ "_socketAddress"
+ "_socketAddressFamily"
+ "_socketAddressLength"
+ "_socketFileDescriptor"
+ "addDeploymentLimit:withGoLiveDate:error:"
+ "com.apple.app-sandbox.read"
+ "connect"
+ "currentISOCountryCode"
+ "deploymentLimits"
+ "findByMobileAssetAppleModelNumber:"
+ "https://basejumper.apple.com"
+ "initRecvSource"
+ "initSocketWithIPv4Address:port:"
+ "initSocketWithIPv6Address:port:"
+ "initWithIPAddress:port:delegate:"
+ "initWithIPAddress:port:family:delegate:"
+ "initWithIPv4Dictionary:"
+ "initWithIPv6Dictionary:"
+ "initWithSerialDictionary:"
+ "isFullyDeployedDeploymentLimits"
+ "lastObject"
+ "mergePlist:"
+ "ota disabled"
+ "q24@0:8@16"
+ "readTokenStringWithURL:"
+ "receivedData:device:"
+ "recvUARPMsg"
+ "replaceBytesInRange:withBytes:"
+ "sendData:"
+ "setCurrentISOCountryCode:"
+ "setDeploymentLimits:"
+ "setIsFullyDeployedDeploymentLimits:"
+ "sortedArrayUsingSelector:"
+ "uarpCreateFileHandleForWritingToURL:error:"
+ "uarpIPDevice"
+ "v40@0:8@16@24^@32"
+ "validateDeploymentLimits:"
- "%s: failed to cosume sandbox token"
- "CrystalD"

```
