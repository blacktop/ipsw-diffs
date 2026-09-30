## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

-61.0.0.0.0
-  __TEXT.__text: 0x3e21c
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_stubs: 0x4680
-  __TEXT.__objc_methlist: 0x1bf0
-  __TEXT.__cstring: 0x1bf4
-  __TEXT.__objc_methname: 0x48df
-  __TEXT.__objc_classname: 0x3e7
-  __TEXT.__objc_methtype: 0xf59
+63.100.22.0.0
+  __TEXT.__text: 0x53080
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_stubs: 0x5620
+  __TEXT.__objc_methlist: 0x2bf4
+  __TEXT.__cstring: 0x20e6
+  __TEXT.__objc_methname: 0x5922
+  __TEXT.__objc_classname: 0x49e
+  __TEXT.__objc_methtype: 0x10f0
   __TEXT.__const: 0x1631
-  __TEXT.__oslogstring: 0x440c
-  __TEXT.__gcc_except_tab: 0xb78
+  __TEXT.__oslogstring: 0x57af
+  __TEXT.__gcc_except_tab: 0x11d0
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0xbb0
-  __DATA_CONST.__auth_got: 0x5b0
-  __DATA_CONST.__got: 0x290
+  __TEXT.__unwind_info: 0x1218
+  __DATA_CONST.__auth_got: 0x6c8
+  __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x56e8
-  __DATA_CONST.__cfstring: 0x1c80
-  __DATA_CONST.__objc_classlist: 0xf8
+  __DATA_CONST.__const: 0x6fe8
+  __DATA_CONST.__cfstring: 0x23e0
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_intobj: 0x1188
-  __DATA_CONST.__objc_arraydata: 0x280
-  __DATA_CONST.__objc_arrayobj: 0x258
-  __DATA.__objc_const: 0x63f0
-  __DATA.__objc_selrefs: 0x1338
-  __DATA.__objc_ivar: 0x204
-  __DATA.__objc_data: 0x9b0
-  __DATA.__data: 0x5a8
-  __DATA.__bss: 0xc8
+  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_intobj: 0x1578
+  __DATA_CONST.__objc_doubleobj: 0x10
+  __DATA_CONST.__objc_arraydata: 0x408
+  __DATA_CONST.__objc_arrayobj: 0x468
+  __DATA_CONST.__objc_dictobj: 0x50
+  __DATA.__objc_const: 0x7010
+  __DATA.__objc_selrefs: 0x1958
+  __DATA.__objc_ivar: 0x2c4
+  __DATA.__objc_data: 0xaf0
+  __DATA.__data: 0x6c8
+  __DATA.__bss: 0xe0
   __DATA.__common: 0x10
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
+  - /System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
+  - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1456
-  Symbols:   271
-  CStrings:  1811
+  Functions: 2367
+  Symbols:   317
+  CStrings:  2223
 
Symbols:
+ _CBAssignedL2CAPPSMForSoftwareUpdate
+ _CFPreferencesSetValue
+ _IOIteratorNext
+ _IORegistryEntryGetProperty
+ _IORegistryEntrySetCFProperties
+ _IOServiceGetMatchingServices
+ _NSDataWithHex
+ _OBJC_CLASS_$_CBAdvertiser
+ _OBJC_CLASS_$_CBController
+ _OBJC_CLASS_$_CBControllerLowPowerModeParams
+ _OBJC_CLASS_$_CBReadRequest
+ _OBJC_CLASS_$_CBServer
+ _OBJC_CLASS_$_CBWriteRequest
+ _OBJC_CLASS_$_MIBUNWClientController
+ _OBJC_CLASS_$_MIBURaptorQPacketConsumer
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _PLResetPowerlog
+ _archive_entry_pathname
+ _archive_entry_set_pathname
+ _archive_entry_size
+ _archive_error_string
+ _archive_read_append_filter
+ _archive_read_close
+ _archive_read_data_block
+ _archive_read_free
+ _archive_read_new
+ _archive_read_next_header
+ _archive_read_open_filename
+ _archive_read_set_format
+ _archive_write_close
+ _archive_write_data_block
+ _archive_write_disk_new
+ _archive_write_disk_set_options
+ _archive_write_disk_set_standard_lookup
+ _archive_write_finish_entry
+ _archive_write_free
+ _archive_write_header
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _kCFPreferencesCurrentUser
+ _launch_set_service_enabled
+ _nw_interface_get_subtype
+ _nw_path_monitor_set_queue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
+ _posix_spawn
+ _posix_spawnattr_destroy
+ _posix_spawnattr_init
+ _strerror
- _SMJobSetEnabled
- _container_system_group_path_for_identifier
- _kSMDomainUserLaunchd
CStrings:
+ "\x05"
+ "\x0f\x06"
+ "\x11\x12\x16"
+ "\x15"
+ "%{public}@: cannot find io registry entry for IOPMUPrimary"
+ "%{public}@: cannot set properties for IOPMUBootLPMCtrl"
+ "%{public}@: device will shutdown in low power mode now."
+ "/tmp/su/"
+ "/tmp/su/assets/"
+ "/usr/local/bin/"
+ "/usr/local/bin/python3"
+ "/usr/local/bin/suServer.py"
+ "?"
+ "@\"<MIBUBTConnectionDelegate>\""
+ "@\"<MIBUBTControllerDelegate>\""
+ "@\"CBAdvertiser\""
+ "@\"CBConnection\""
+ "@\"CBServer\""
+ "@\"MIBUBTConnection\""
+ "@\"MIBUBTController\""
+ "@\"MIBUNWClientController\""
+ "@\"MIBURaptorQPacketConsumer\""
+ "@\"NSTask\""
+ "@32@0:8@16Q24"
+ "@36@0:8@16B24^@28"
+ "Advertisement payload cannot be nil"
+ "All BT payload received: %ld/%hu"
+ "AppleDialogSPMIPMU"
+ "Archive write failed with error: %s"
+ "Asset download timed out after %ds"
+ "AssetPath"
+ "Assets"
+ "Attempting to connect to WiFi (attempt %lu)..."
+ "Awaiting Incoming BT Request..."
+ "B32@0:8@\"NSDictionary\"16^@24"
+ "B40@0:8@16@24^@32"
+ "BT Link Authenticated!"
+ "BatterySOC"
+ "Bluetooth advertisement activated"
+ "Bluetooth advertiser invalidated"
+ "Bluetooth connection accept: %{public}@"
+ "Bluetooth connection dropped: %{public}@"
+ "Bluetooth connection error: %{public}@"
+ "Bluetooth connection established: %{public}@"
+ "Bluetooth controller already running, ignore advertise of payload: %{public}@"
+ "Bluetooth server invalidated"
+ "Bluetooth server listening on 0x%hx"
+ "Bluetooth state changed: %s"
+ "Catalog does not have Assets key"
+ "Cleaning up in-box update main controller..."
+ "Cleaning up shipping update main controller..."
+ "Command %ld is not allowed in current state, rejecting"
+ "Connection not authenticated, rejecting command %ld"
+ "Current connection already dropped; rejecting command %ld"
+ "Data copy failed with error: %s"
+ "Deserialize authenticate command"
+ "Device already activated"
+ "DownloadServerBaseURLOverride"
+ "Downloaded asset file does not exist at path: %{public}@"
+ "EnablePipelineMode"
+ "Extracting asset files..."
+ "Extracting file %{public}@"
+ "Extraction failed with error: %s"
+ "FFFFFFFFFFFFFFFFFFFF"
+ "Failed ss update serialization; payload missing %{public}@ key"
+ "Failed to activate bluetooth advertiser; error: %{public}@"
+ "Failed to activate bluetooth server with error: %{public}@"
+ "Failed to copy file %{public}@ to %{public}@.  Error %{public}@"
+ "Failed to create directory: %{public}@; error: %{public}@"
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
+ "Failed to disable daemon, err: %d"
+ "Failed to download update asset"
+ "Failed to extract OS update assets."
+ "Failed to extract update asset"
+ "Failed to extract update asset relative path from %{public}@"
+ "Failed to extract update brain asset relative path from %{public}@"
+ "Failed to find asset relative path from %{public}@"
+ "Failed to open %s"
+ "Failed to put device to LPM mode."
+ "Failed to put device to low power mode."
+ "Failed to read data block with %s; ret: %d"
+ "Failed to read from BT connection: %{public}@"
+ "Failed to receive OS update assets."
+ "Failed to scan for SSID: %{public}@ with error:%{public}@ (%lu tries remaining)"
+ "Failed to send data over bluetooth; error: %{public}@"
+ "Failed to set device to LPM; empty scan payload"
+ "Failed to set read format with error: %s"
+ "Failed to setup OS update assets."
+ "Failed to setup asset file"
+ "Failed to setup local file server."
+ "Failed to start multicast download, no RQ basic parameters"
+ "Failed to start multicast download, no RQ extended parameters"
+ "Failed to start multicast download, no RQ payload"
+ "Failed to start multicast download, no group address"
+ "Failed to start multicast download, no group port"
+ "Failed to start multicast download, no host port"
+ "Failed to start multicast download, no interface name"
+ "Failed to start multicast download, no service name"
+ "Failed to write data block with %s; ret: %d"
+ "File Server Console: %{public}@"
+ "Finished assembling asset over multicast"
+ "Finished receiving asset over multicast"
+ "GroupAddress"
+ "GroupPort"
+ "Handling setLPMWithPaylod: xpc call"
+ "Handling shutdownWithReply: xpc call"
+ "Handling start SS update command..."
+ "Handling status authenticate command..."
+ "HostPort"
+ "IOPMUBootLPMCtrl"
+ "IOPMUPrimary"
+ "IORegistryEntryGetProperty returned %d"
+ "IOServiceGetMatchingServices returned %d"
+ "IdleTimeoutTask"
+ "Ignoring bluetooth connection error"
+ "InterfaceName"
+ "LPMScanPayload"
+ "Loaded advertisement material: %{public}@"
+ "MIBUBTConnection"
+ "MIBUBTConnectionDelegate"
+ "MIBUBTController"
+ "MIBUBTControllerDelegate"
+ "MIBUNWClientControllerDelegate"
+ "MIBUShipUpdateMainController"
+ "MIBUShippingUpdateOperation"
+ "Operation"
+ "Operation is succesful. Putting device to low power mode."
+ "OperationDetails"
+ "Overriding Software Update Asset Path to %{public}@"
+ "Overriding Software Update XML Path to %{public}@"
+ "Overriding Update Brain Asset Path to %{public}@"
+ "Overriding Update Brain XML Path to %{public}@"
+ "Phase"
+ "PoweredOff"
+ "PoweredOn"
+ "RQBasicParameters"
+ "RQExtendedParameters"
+ "RQThreshold"
+ "Reached the end of file"
+ "Read request timed out after %ds"
+ "Reading BT payload: %ld/%hu"
+ "Received Command %ld over BT"
+ "Received data over BT: %{public}@"
+ "Reseting BT controller"
+ "Resetting"
+ "Restricted"
+ "Retrying SU scan on internal builds: %lu/%u"
+ "S24@0:8@16"
+ "Sending response over BT..."
+ "Serializing SSUpdate command"
+ "Serializing authenticate command"
+ "Server spawn result: %d; (error: %s); PID = %d"
+ "ServiceName"
+ "Set LPM returned error: %{public}@"
+ "Setting Mobile Asset Base URL Override..."
+ "Setting device to LPM mode with scan payload: %{public}@"
+ "Setting device to LPM mode; scanWindow = 0x%X; scanInterval = 0x%X"
+ "Setting up asset file..."
+ "SoftwareUpdate Brain XML Path does not exist at path %{public}@"
+ "SoftwareUpdate XML Path does not exist at path %{public}@"
+ "SoftwareUpdateAssetPath"
+ "SoftwareUpdateBrainAssetPath"
+ "SoftwareUpdateBrainXMLPath"
+ "SoftwareUpdateBrainXMLPath = %{public}@; SoftwareUpdateBrainAssetPath = %{public}@; SoftwareUpdateXMLPath = %{public}@; SoftwareUpdateAssetPath = %{public}@"
+ "SoftwareUpdateXMLPath"
+ "Started assembling asset file."
+ "Started receiving asset over multicast"
+ "Starting BT controller"
+ "Starting in-box update main controller ..."
+ "Starting local file server..."
+ "Starting shipping update main controller ..."
+ "StatusServerHostAddress"
+ "StatusServerPortNumber"
+ "Successfully extracted asset files!"
+ "T@\"<MIBUBTConnectionDelegate>\",&,N,V_delegate"
+ "T@\"<MIBUBTControllerDelegate>\",&,N,V_delegate"
+ "T@\"CBAdvertiser\",&,N,V_advertiser"
+ "T@\"CBConnection\",&,N,V_connection"
+ "T@\"CBServer\",&,N,V_server"
+ "T@\"MIBUBTConnection\",&,N,V_connection"
+ "T@\"MIBUBTController\",&,N,V_btController"
+ "T@\"MIBUNWClientController\",&,N,V_multicastClient"
+ "T@\"MIBURaptorQPacketConsumer\",&,N,V_packetConsumer"
+ "T@\"NSData\",&,N,V_advertisementPayload"
+ "T@\"NSNumber\",&,N,V_rqBasicParameters"
+ "T@\"NSNumber\",&,N,V_rqExtendedParameters"
+ "T@\"NSNumber\",&,N,V_rqThreshold"
+ "T@\"NSNumber\",&,N,V_tcpPingInterval"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_idleTimeoutTaskQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_networkMonitorQueue"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_downloadSem"
+ "T@\"NSString\",&,N,V_groupAddress"
+ "T@\"NSString\",&,N,V_groupPort"
+ "T@\"NSString\",&,N,V_hostPort"
+ "T@\"NSString\",&,N,V_interfaceName"
+ "T@\"NSString\",&,N,V_serviceName"
+ "T@\"NSString\",&,N,V_tcpAddress"
+ "T@\"NSString\",&,N,V_tcpPort"
+ "T@\"NSTask\",&,N,V_serverTask"
+ "TB,N,V_authenticated"
+ "TB,V_running"
+ "TCPAddress"
+ "TCPPingInterval"
+ "TCPPort"
+ "TCPUnicastAddress"
+ "TCPUnicastPort"
+ "TQ,V_retryCount"
+ "Terminating BT controller"
+ "Timed out in state %d, putting device to low power mode."
+ "Truncating payload data to %{public}@"
+ "Unauthorized"
+ "Unknown"
+ "Unsupported"
+ "Use wifi password: %{public}@"
+ "UseSrNmForDeviceKey"
+ "Using device serial number %{public}@ as device key"
+ "WiFiPassword"
+ "Write header failed with error: %s, retrying"
+ "Write request timed out after %ds"
+ "__RelativePath"
+ "_advertisementPayload"
+ "_advertiser"
+ "_assetRelativePathFromCatalog:"
+ "_associateFromScanResult:password:error:"
+ "_authenticated"
+ "_beginUpdate"
+ "_btController"
+ "_cleanUp"
+ "_connectToWiFi"
+ "_deserializeAuthenticate"
+ "_deserializeSSUpdate"
+ "_didReceivePipeOutput:"
+ "_downloadAssetFile"
+ "_downloadSem"
+ "_endUpdate:"
+ "_extractAssetFile"
+ "_groupAddress"
+ "_groupPort"
+ "_handleAuthenticate:"
+ "_handleStartSSUpdate:"
+ "_hostPort"
+ "_idleTimeoutTaskQueue"
+ "_interfaceName"
+ "_loadAdvertisementPayload"
+ "_multicastClient"
+ "_networkMonitorQueue"
+ "_overrideSUAssetBaseURL"
+ "_packetConsumer"
+ "_retryCount"
+ "_rqBasicParameters"
+ "_rqExtendedParameters"
+ "_rqThreshold"
+ "_scan"
+ "_scanForSSID:skipEAP:error:"
+ "_serializeAuthenticate"
+ "_serializeSSUpdate"
+ "_server"
+ "_serverTask"
+ "_serviceName"
+ "_setupAssetFile"
+ "_startCBServer"
+ "_startConnectionReadLoop"
+ "_startLocalFileServer"
+ "_tcpAddress"
+ "_tcpPingInterval"
+ "_tcpPort"
+ "_terminateLocalFileServer"
+ "activateWithCompletion:"
+ "adjustData:toLength:"
+ "advertisementPayload"
+ "advertiser"
+ "asset.tar"
+ "assetPath"
+ "assets"
+ "authenticated"
+ "availableData"
+ "bleListenPSM"
+ "bluetoothState"
+ "brain.xml"
+ "brain.zip"
+ "btController"
+ "cStringUsingEncoding:"
+ "checkOutWithError:"
+ "clientControllerDidFinishAssembly:"
+ "clientControllerDidFinishReceive:"
+ "clientControllerDidStartAssembly:"
+ "clientControllerDidStartReceive:"
+ "com.apple.MobileAsset"
+ "com.apple.mibu_bt_connection_queue"
+ "com.apple.mobileinboxupdate.wifi_monitor_queue"
+ "command rejected"
+ "command timed out"
+ "copyItemAtPath:toPath:error:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "devicePingPayload"
+ "didConnect:"
+ "didDisconnect:"
+ "download"
+ "downloadSem"
+ "enablePipelineMode"
+ "expectedAPDULength:"
+ "extract"
+ "findServicePmuPrimary"
+ "groupAddress"
+ "groupPort"
+ "hostPort"
+ "http://localhost:8080"
+ "idleTimeoutTaskQueue"
+ "imgIdx"
+ "increaseLengthBy:"
+ "initWithBasicParameters:extendedParameters:threshold:outputFile:"
+ "initWithPacketConsumer:hostPort:tcpAddress:tcpPort:groupAddress:groupPort:interfaceName:serviceName:controllerDelegate:"
+ "lpm0"
+ "lpm1"
+ "lpm2"
+ "lpm3"
+ "multicastClient"
+ "networkMonitorQueue"
+ "object"
+ "packetConsumer"
+ "pathWithComponents:"
+ "readWithCBReadRequest:"
+ "reset:"
+ "retryCount"
+ "rqBasicParameters"
+ "rqExtendedParameters"
+ "rqThreshold"
+ "scanInterval"
+ "scanWindow"
+ "server"
+ "serverTask"
+ "serviceName"
+ "setAcceptHandler:"
+ "setActionType:"
+ "setAdvertisementPayload:"
+ "setAdvertiser:"
+ "setAuthenticated:"
+ "setBleListenPSM:"
+ "setBluetoothStateChangedHandler:"
+ "setBtController:"
+ "setCompletion:"
+ "setConfigFlags:"
+ "setDarkBoot:"
+ "setDataArray:"
+ "setDataBlob:"
+ "setDataMask:"
+ "setDownloadSem:"
+ "setErrorHandler:"
+ "setGpioAssertionTime:"
+ "setGroupAddress:"
+ "setGroupPort:"
+ "setHostPort:"
+ "setIdleTimeoutTaskQueue:"
+ "setInterfaceName:"
+ "setInvalidationHandler:"
+ "setLowPowerModeWithParams:params:completion:"
+ "setMaxLength:"
+ "setMulticastClient:"
+ "setNetworkMonitorQueue:"
+ "setNextScanDelay:"
+ "setPacketConsumer:"
+ "setPacketLength:"
+ "setPassword:"
+ "setPingInterval:"
+ "setRetryCount:"
+ "setRqBasicParameters:"
+ "setRqExtendedParameters:"
+ "setRqThreshold:"
+ "setRssiThresholdValue:"
+ "setRunning:"
+ "setScanDelayStart:"
+ "setScanDuration:"
+ "setScanInterval:"
+ "setScanWindow:"
+ "setServer:"
+ "setServerTask:"
+ "setServiceName:"
+ "setSoftwareUpdateActionType:"
+ "setSoftwareUpdateDataArray:"
+ "setSource:"
+ "setTcpAddress:"
+ "setTcpPingInterval:"
+ "setTcpPort:"
+ "setToLPMWithOptions:error:"
+ "setToLPMWithOptions:reply:"
+ "shutdownInLPM"
+ "shutdownWithReply:"
+ "softwareUpdateAssetPath"
+ "softwareUpdateBrainAssetPath"
+ "softwareUpdateBrainXMLPath"
+ "softwareUpdateXMLPath"
+ "startWithAdv:error:"
+ "statusServerHostAddress"
+ "statusServerPortNumber"
+ "stop"
+ "stopping multicast client..."
+ "stringByDeletingLastPathComponent"
+ "tcpAddress"
+ "tcpPingInterval"
+ "tcpPort"
+ "tcpUnicastAddress"
+ "tcpUnicastPort"
+ "thermalPressureLevel"
+ "update.aea"
+ "update.xml"
+ "updateIOPMUBootLPMCtrl"
+ "useSrNmForDeviceKey"
+ "v24@0:8@\"MIBUBTConnection\"16"
+ "v24@0:8@\"MIBUNWClientController\"16"
+ "v24@?0@\"CBConnection\"8@?<v@?@\"NSError\">16"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "waitForDataInBackgroundAndNotify"
+ "wifiPassword"
+ "writeWithCBWriteRequest:"
- "Cleaning up main controller..."
- "Device is iPad, disable daemon"
- "Failed to locate power log path, error: %llu"
- "Failed to scan for SSID: %{public}@ with error:%{public}@"
- "Power log: %{public}@ removed: %{bool}d with error: %{public}@"
- "Removing power log from device ..."
- "SMJobSetEnabled returned error: %{public}@"
- "Starting main controller ..."
- "_associateFromScanResult:error:"
- "_scanForSSID:error:"
- "_thermalPressureLevel"
- "contentsOfDirectoryAtPath:error:"
- "stringByAppendingPathComponent:"
- "systemgroup.com.apple.powerlog"

```
