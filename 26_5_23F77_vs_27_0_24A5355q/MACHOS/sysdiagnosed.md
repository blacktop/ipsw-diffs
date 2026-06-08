## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

```diff

-1527.120.2.0.0
-  __TEXT.__text: 0x6a45c
-  __TEXT.__auth_stubs: 0x16c0
-  __TEXT.__objc_stubs: 0x94a0
-  __TEXT.__objc_methlist: 0x3eec
-  __TEXT.__const: 0x1d4
-  __TEXT.__cstring: 0x10b67
-  __TEXT.__objc_classname: 0x395
-  __TEXT.__objc_methtype: 0x1752
-  __TEXT.__gcc_except_tab: 0x1110
-  __TEXT.__objc_methname: 0xa757
-  __TEXT.__oslogstring: 0x8d8c
+1587.0.0.0.0
+  __TEXT.__text: 0x610c0
+  __TEXT.__auth_stubs: 0x16d0
+  __TEXT.__objc_stubs: 0x9320
+  __TEXT.__objc_methlist: 0x3f04
+  __TEXT.__const: 0x1cc
+  __TEXT.__cstring: 0x10c32
+  __TEXT.__objc_classname: 0x38b
+  __TEXT.__objc_methtype: 0x17f5
+  __TEXT.__gcc_except_tab: 0xd9c
+  __TEXT.__objc_methname: 0xa5c5
+  __TEXT.__oslogstring: 0x80fa
   __TEXT.__ustring: 0x4e8
-  __TEXT.__unwind_info: 0x1308
-  __DATA_CONST.__auth_got: 0xb70
-  __DATA_CONST.__got: 0x3c0
-  __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x1430
-  __DATA_CONST.__cfstring: 0x11500
+  __TEXT.__unwind_info: 0x1190
+  __DATA_CONST.__const: 0x1408
+  __DATA_CONST.__cfstring: 0x115e0
   __DATA_CONST.__objc_classlist: 0x130
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0xe48
-  __DATA_CONST.__objc_arrayobj: 0x13b0
+  __DATA_CONST.__objc_arraydata: 0xea8
+  __DATA_CONST.__objc_arrayobj: 0x1410
   __DATA_CONST.__objc_intobj: 0x300
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x5220
-  __DATA.__objc_selrefs: 0x29f0
-  __DATA.__objc_ivar: 0x470
+  __DATA_CONST.__auth_got: 0xb78
+  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__auth_ptr: 0x60
+  __DATA.__objc_const: 0x5388
+  __DATA.__objc_selrefs: 0x29b8
+  __DATA.__objc_ivar: 0x474
   __DATA.__objc_data: 0xbe0
-  __DATA.__data: 0x2d0
+  __DATA.__data: 0x3a0
   __DATA.__bss: 0x280
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 12DB7223-EC79-3FE4-A3A5-FE13A02D71A7
-  Functions: 1795
-  Symbols:   498
-  CStrings:  7525
+  UUID: BA1962B2-2071-3984-A299-8A7E99BA4898
+  Functions: 1767
+  Symbols:   502
+  CStrings:  7506
 
Symbols:
+ _CONTAINER_PERSONA_ALL_AVAILABLE
+ _OSLogConstructSourceDirectory
+ _container_query_iterate_results_sync
+ _container_query_set_identifiers
+ _container_query_set_persona_unique_string
+ _kCFBooleanTrue
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
- _BTLocalDeviceDumpExposureNotificationDatabase
- _BTLocalDeviceGetDefault
- _IOIteratorNext
- _IOObjectRelease
- _IORegistryEntryCreateIterator
- _IORegistryEntryGetName
- _container_create_or_lookup_path_for_current_user
- _objc_terminate
CStrings:
+ "\t%s"
+ "#\""
+ "%s%@"
+ "%s%s: config not found for '%@', returning default result"
+ "%s%s: found %lu configs (>1). Configs found for:"
+ "%s.%@: "
+ "%sAlready remote initiated. Failing to startRemoteInitiatedFlow"
+ "%sConnection to '%s' terminated with error: %s"
+ "%sConnection to '%s' terminated with event type: %s"
+ "%sFailed response from remote, error: %@"
+ "%sFailed to create CSSessionConfig object"
+ "%sFailed to get receiveFileSema for '%{public}s' for signaling host output dir"
+ "%sFailed to get receiveFileSema for '%{public}s' for waiting host output dir"
+ "%sFailed to trigger co-sysdiagnose for %@"
+ "%sFailing to trigger co-sysdiagnose: device is not usable"
+ "%sFailing to trigger co-sysdiagnose: failed to create remote xpc connection"
+ "%sForcing remote to not act as host"
+ "%sForwarding to remote device: %s"
+ "%sReceived response: %@ from remote for request: %@"
+ "%sRemote sysdiagnose wasn't triggered or is done transferring. Skipping waiting"
+ "%sStarting remote initiated flow"
+ "%sTimed out waiting for host to set output directory"
+ "%sTimed out waiting for remote co-sysdiagnose"
+ "%sTimed out waiting on proxies for %lus, canceling connections"
+ "%sTimed out waiting on proxies. Skipping remaining"
+ "%sTriggering co-sysdiagnose"
+ "%sTriggering co-sysdiagnoses"
+ "%sUnknown response type received: %d"
+ "%sWaiting for co-sysdiagnoses..."
+ "%snil device passed into _initWithDevice"
+ "%snil diagnosticID passed to %s - returning default result"
+ "%sself.connection is nil - connection has been cancelled. Skipping waiting"
+ "%stimeout target requested. Using %lus"
+ "%stimeout target requested. noTimeout is set - using DISPATCH_TIME_FOREVER"
+ "--dump-to-file"
+ "--mobile"
+ "--outdir"
+ "-z"
+ "/private/var/db/accessoryupdater/assetcache/mobileasset/UARPCacheRegistry.plist"
+ "/private/var/db/spindump/UUIDToBinaryLocations"
+ "/private/var/mobile/Library/Preferences/com.apple.osanalytics.addaily.plist"
+ "/private/var/mobile/tmp/com.apple.audiomxd/"
+ "/private/var/preferences/Logging/Subsystems"
+ "/usr/appleinternal/bin/CiderCLI"
+ "/usr/local/bin/iftool"
+ "/usr/local/bin/triagectl"
+ "<TMPOUTPUTDIR>/node-serial-logs.txt"
+ "@\"<CSProxyFactoryProtocol>\""
+ "@\"<CSSessionConfigFactoryProtocol>\""
+ "@\"CSSessionConfig\"16@0:8"
+ "@\"NSArray\"24@0:8@\"NSString\"16"
+ "@32@0:8@16d24"
+ "@40@0:8@16d24@32"
+ "Allowing remote invocation because DeviceSupportsUntrustedRemoteSysdiagnose"
+ "Allowing remote invocation because on compute controller"
+ "Allowing remote invocation because on compute node"
+ "Allowing remote invocation because we are on a darwinOS iOS VM"
+ "Allowing remote invocation because we are on a stress rack device"
+ "Allowing remote invocation because we are on an Apple Display"
+ "AppManagedFeatures"
+ "Automatic co-sysdiagnose is not possible"
+ "Automatic co-sysdiagnose is possible"
+ "B16@?0^{container_object_s=}8"
+ "CSProxyFactory"
+ "CSProxyFactoryProtocol"
+ "CSSessionConfigFactory"
+ "CSSessionConfigFactoryProtocol"
+ "Can't act as remote device. Rejecting request for message: %@"
+ "CiderCLISerialize"
+ "Collecting all trusted, adding all uuids"
+ "Conn started"
+ "Couldn't create transfer object. Skipping file transfer"
+ "Current config prevents accepting RemoteXPC requests. Cancelling conn"
+ "Deduced msg type: Request, triggering local sysdiagnose"
+ "Did not receive any file transfer object. Got xpc response: %s"
+ "Failed to allocate uuidStr in %s"
+ "Failed to fetch device for UDID '%s'. Not appending remote UUID"
+ "Failed to fetch uuidStr for device with UDID '%s'. Not appending remote UUID"
+ "Failed to get path basename. Not sending file to remote"
+ "Failed to parse device uuid for '%s'"
+ "Failed to start remote initiated flow. Cancelling connection for message: %@"
+ "Failed to write remote archive %@ because host dir is not set"
+ "Failing to move tarball: invalid fd! src: %d, dst: %d"
+ "File transfer failed to \"%s\" with error %d:%s"
+ "File transfer failed with error %d:%s"
+ "File transfer succeeded"
+ "File transfer succeeded to \"%s\""
+ "Found remote UUID. New tarball name: %@"
+ "Got result %d for compute controller check"
+ "Got result %d for compute node check"
+ "Initiating remote connection"
+ "IntelligenceFlow"
+ "IsComputeController"
+ "IsComputeNode"
+ "LoggingPreferences"
+ "MiscBreadcrumbs"
+ "NOT SELF ENDSWITH[c] '.vrdump'"
+ "NVRAM is not supported on this system. Returning NO for %s"
+ "NetworkRelay"
+ "No srcPath sent from remote"
+ "OSAnalytics"
+ "Prioritized device '%{public}s' for uuid '%{public}s'"
+ "Received canceling, ending browsing"
+ "Remote server initialized"
+ "Returning default value of NO for RSD invocation"
+ "Sorted devices:"
+ "Starting server with trust: %d"
+ "T@\"<CSProxyFactoryProtocol>\",&,N,V_proxyFactory"
+ "T@\"<CSSessionConfigFactoryProtocol>\",&,N,V_sessionConfigFactory"
+ "T@\"NSObject<OS_os_log>\",&,V_logHandle"
+ "TASK_TYPE_APP_MANAGED_FEATURES"
+ "TASK_TYPE_LSD_IDENTIFIERS"
+ "Td,N,V_outputDirTimeout"
+ "Timed out waiting to send file to host"
+ "Tr*,V_logPrefix"
+ "Transferring %@ to host"
+ "Trying to fetch service (%{public}s) for unconnected device (%{public}s)"
+ "Trying to prioritize an empty device list!"
+ "UARPKitFirmwareSubscriptionDatabase"
+ "UDID not found in xpc dict for name: %@ - assuming legacy client and not appending remote UUID"
+ "Unexpected type (%{public}s); cancelling conn"
+ "Unknown message type. Mismatched os versions."
+ "_logHandle"
+ "_logPrefix"
+ "_outputDirTimeout"
+ "_proxyFactory"
+ "_resolveHomeTildePath:"
+ "_sessionConfigFactory"
+ "bmc-triage"
+ "com.apple.sysdiagnose.co-sysdiagnose"
+ "countDisplays"
+ "createSessionConfig"
+ "getProxies found total: %lu"
+ "got nil device from from browsing SPI with canceling == false"
+ "initWithProxyFactory:"
+ "initWithProxyFactory:outputDirTimeout:"
+ "initWithProxyFactory:outputDirTimeout:sessionConfigFactory:"
+ "launch-services"
+ "logHandle"
+ "logPrefix"
+ "logs/AppManagedFeatures"
+ "logs/BMC"
+ "logs/CiderCLI"
+ "logs/IntelligenceFlow"
+ "nil"
+ "nil UUID str given to %s, returning NULL for remote device"
+ "outputDirTimeout"
+ "proxyFactory"
+ "query"
+ "r*"
+ "r*16@0:8"
+ "remote_device_copy_device_with_uuid failed for UUID '%@' (uuid_t '%s'). Returning NULL"
+ "reset"
+ "resolvePathsToMobileContainer:"
+ "sds"
+ "serialize"
+ "sessionConfigFactory"
+ "setLogHandle:"
+ "setLogPrefix:"
+ "setOutputDirTimeout:"
+ "setProxyFactory:"
+ "setSessionConfigFactory:"
+ "sharedFactory"
+ "sysdiagnose-logs"
+ "tailspindb"
+ "timed out (%lus) waiting for browsing to finish"
+ "triagectl-output.txt"
+ "uuid_parse failed to parse '%@' and returned %lu. Returning NULL for remote device"
+ "v24@0:8r*16"
- " not"
- "#$"
- "+[CSProxy description]"
- "+[CSProxy isHost]"
- "--pid"
- "-[CSProxy transferFileToHost:]"
- "/usr/local/bin/aidreport"
- "/usr/local/bin/stsp_tool"
- "0x10"
- "0xbb"
- "0xbc"
- "0xe0"
- "0xe1"
- "0xe7"
- "0xff00,0x000b"
- "619"
- ": \n"
- "@24@0:8q16"
- "CSBridgeProxy"
- "CSCoordinator: %@"
- "CSCoordinator: %s: config not found for '%@', returning default result"
- "CSCoordinator: %s: found %lu configs (>1). Configs found for:"
- "CSCoordinator: Already remote initiated. Failing to startRemoteInitiatedFlow"
- "CSCoordinator: Failed to allocate CSSessionConfig object"
- "CSCoordinator: Failed to trigger co-sysdiagnose for %@"
- "CSCoordinator: Not transferring file to host in transferFileToHostIfNecessary, because we are already remote initiated"
- "CSCoordinator: Not triggering co-sysdiagnoses"
- "CSCoordinator: On host, so file transfer not necessary. Skipping transfer"
- "CSCoordinator: Starting remote initiated flow with initiatedByRemoteHost: %d"
- "CSCoordinator: Timed out waiting for host to set output directory"
- "CSCoordinator: Timed out waiting on proxies for %lus, canceling connections"
- "CSCoordinator: Timed out waiting on proxies. Skipping remaining"
- "CSCoordinator: Transferring file from remote to host: %@"
- "CSCoordinator: Triggering co-sysdiagnoses"
- "CSCoordinator: Waiting for co-sysdiagnoses..."
- "CSCoordinator: forced to return no for isHost"
- "CSCoordinator: nil diagnosticID passed to %s - returning default result"
- "CSDisplayProxy"
- "CSDisplayProxy: Automatic co-sysdiagnose is%s possible"
- "CSDisplayProxy: Finished browsing. Found %lu devices (%lu usable) of type %s"
- "CSDisplayProxy: Found device %{public}s"
- "CSDisplayProxy: Found valid display with uuid %@, but already manually requested from client - skipping"
- "CSDisplayProxy: On iOS, but not an iPhone or iPad. Returning no proxies"
- "CSDisplayProxy: Received canceling, ending browsing"
- "CSDisplayProxy: getProxies found total: %lu"
- "CSDisplayProxy: got nil device from from browsing SPI with canceling == false"
- "CSDisplayProxy: timed out (%lus) waiting for browsing to finish"
- "CSDisplayProxy: timeout target requested. Using %lus"
- "CSRemoteXPCProxy: \t%s"
- "CSRemoteXPCProxy: %{public}s: conn started"
- "CSRemoteXPCProxy: %{public}s: current config prevents accepting RemoteXPC requests. Cancelling conn"
- "CSRemoteXPCProxy: %{public}s: initiating remote connection"
- "CSRemoteXPCProxy: %{public}s: remote server initialized."
- "CSRemoteXPCProxy: %{public}s: unexpected type (%{public}s); cancelling conn"
- "CSRemoteXPCProxy: Allowing remote invocation because DeviceSupportsUntrustedRemoteSysdiagnose"
- "CSRemoteXPCProxy: Allowing remote invocation because on compute module B"
- "CSRemoteXPCProxy: Allowing remote invocation because on compute module C"
- "CSRemoteXPCProxy: Allowing remote invocation because we are on a darwinOS iOS VM"
- "CSRemoteXPCProxy: Allowing remote invocation because we are on a stress rack device"
- "CSRemoteXPCProxy: Allowing remote invocation because we are on an Apple Display"
- "CSRemoteXPCProxy: Can't act as remote device. Rejecting request for message: %@"
- "CSRemoteXPCProxy: Collecting all trusted, adding all uuids"
- "CSRemoteXPCProxy: Connection to '%s' terminated with error: %s"
- "CSRemoteXPCProxy: Connection to '%s' terminated with event type: %s"
- "CSRemoteXPCProxy: Couldn't create transfer object. Skipping file transfer"
- "CSRemoteXPCProxy: Deduced msg type: Request, triggering local sysdiagnose"
- "CSRemoteXPCProxy: Did not receive any file transfer object. Got xpc response: %s"
- "CSRemoteXPCProxy: Didn't create connection to host - stopping file transfer"
- "CSRemoteXPCProxy: Failed response from remote, error: %@"
- "CSRemoteXPCProxy: Failed to allocate uuidStr in %s"
- "CSRemoteXPCProxy: Failed to fetch device for UDID '%s'. Not appending remote UUID"
- "CSRemoteXPCProxy: Failed to fetch uuidStr for device with UDID '%s'. Not appending remote UUID"
- "CSRemoteXPCProxy: Failed to get path basename. Not sending file to remote"
- "CSRemoteXPCProxy: Failed to parse device uuid for '%s'"
- "CSRemoteXPCProxy: Failed to start remote initiated flow. Cancelling connection for message: %@"
- "CSRemoteXPCProxy: Failed to write remote archive %@ because host dir is not set"
- "CSRemoteXPCProxy: Failing to trigger co-sysdiagnose: device is not usable"
- "CSRemoteXPCProxy: Failing to trigger co-sysdiagnose: failed to create remote xpc connection"
- "CSRemoteXPCProxy: File transfer failed to \"%s\" with error %d:%s"
- "CSRemoteXPCProxy: File transfer failed with error %d:%s"
- "CSRemoteXPCProxy: File transfer succeeded"
- "CSRemoteXPCProxy: File transfer succeeded to \"%s\""
- "CSRemoteXPCProxy: Forcing remote to not act as host"
- "CSRemoteXPCProxy: Forwarding to remote device: %s"
- "CSRemoteXPCProxy: Found remote UUID. New tarball name: %@"
- "CSRemoteXPCProxy: NVRAM is not supported on this system. Returning NO for %s"
- "CSRemoteXPCProxy: No srcPath sent from remote"
- "CSRemoteXPCProxy: Prioritized device '%{public}s' for uuid '%{public}s'"
- "CSRemoteXPCProxy: Received response: %@ from remote for request: %@"
- "CSRemoteXPCProxy: Remote sysdiagnose wasn't triggered or is done transferring. Skipping waiting"
- "CSRemoteXPCProxy: Returning default value of NO for RSD invocation"
- "CSRemoteXPCProxy: Sorted devices:"
- "CSRemoteXPCProxy: Timed out waiting for remote co-sysdiagnose"
- "CSRemoteXPCProxy: Timed out waiting to send file to host"
- "CSRemoteXPCProxy: Transferring %@ to host"
- "CSRemoteXPCProxy: Triggering co-sysdiagnose"
- "CSRemoteXPCProxy: Trying to fetch service (%{public}s) for unconnected device (%{public}s)"
- "CSRemoteXPCProxy: Trying to prioritize an empty device list!"
- "CSRemoteXPCProxy: UDID not found in xpc dict for name: %@ - assuming legacy client and not appending remote UUID"
- "CSRemoteXPCProxy: Unknown message type. Mismatched os versions."
- "CSRemoteXPCProxy: Unknown response type received: %d"
- "CSRemoteXPCProxy: getProxies found total: %lu"
- "CSRemoteXPCProxy: got nil device from from browsing SPI with canceling == false"
- "CSRemoteXPCProxy: nil UUID str given to %s, returning NULL for remote device"
- "CSRemoteXPCProxy: nil device passed into _initWithDevice"
- "CSRemoteXPCProxy: remote_device_copy_device_with_uuid failed for UUID '%@' (uuid_t '%s'). Returning NULL"
- "CSRemoteXPCProxy: self.connection is nil - connection has been cancelled. Skipping waiting"
- "CSRemoteXPCProxy: timed out (%lus) waiting for browsing to finish"
- "CSRemoteXPCProxy: timeout target requested. Using %lus"
- "CSRemoteXPCProxy: timeout target requested. noTimeout is set - using DISPATCH_TIME_FOREVER"
- "CSRemoteXPCProxy: uuid_parse failed to parse '%@' and returned %lu. Returning NULL for remote device"
- "Collecting ExposureNotification DB"
- "Could not dump ExposureNotification db from bluetoothd with error %d"
- "Did not get any URL to collect from ExposureNotification API"
- "DisplayProxyHost"
- "DisplayProxyRemote"
- "ExposureNotification"
- "ExposureNotification db still collecting; waiting for it to become available."
- "ExposureNotification enumeration error for URL %@ : %@"
- "Failed to get default local device from bluetoothd with error %d"
- "Found collected ExposureNotification db."
- "Got result %d for isComputeModuleB check"
- "Got result %d for isComputeModuleC check"
- "IODeviceTree:/"
- "IOObjectRetain: %{mach.errno}d"
- "IORegistryEntryGetName: %d"
- "No ExposureNotification db available to collect."
- "Not triggering exposure notification logs, as self.shouldGatherBTLogs is set to NO"
- "Not triggering exposure notifications since bluetooth is missing"
- "Not waiting for exposure notification logs, as self.shouldGatherBTLogs is set to NO"
- "Querying bluetooth if ExposureNotification is supported, and collect db if so."
- "Received ExposureNotification db after wait."
- "RemoteXPCProxyHost"
- "RemoteXPCProxyRemote"
- "Stsp"
- "Stsp.txt"
- "T@\"NSObject<OS_dispatch_group>\",&,N,V_exposureNotificationGroup"
- "T@\"NSObject<OS_os_log>\",&,V_logSubsystem"
- "T@\"NSURL\",&,N,V_exposureNotificationDBURL"
- "TB,V_initiatedByRemoteHost"
- "TB,V_waitingToCaptureExposureNotificationLogs"
- "Timed out waiting for ExposureNotification db collection."
- "_exposureNotificationDBURL"
- "_exposureNotificationGroup"
- "_initiatedByRemoteHost"
- "_logSubsystem"
- "_waitingToCaptureExposureNotificationLogs"
- "assertion failure: \"[proxies count] <= 1\" -> %llu"
- "assertion failure: \"name\" -> %llu"
- "assetInfo"
- "bridge"
- "browseDevices:"
- "clearHistory unsupported on this config. Manual override: %{BOOL}d"
- "exposureNotificationDBURL"
- "exposureNotificationGroup"
- "failed to create IORegistryEntryCreateIterator: %d"
- "failed to find ioreg path: %{public}s"
- "getAIDReportContainers"
- "getExposureNotificationContainer"
- "getMediaContainer"
- "getSPIContainers"
- "getStspContainer"
- "hidreport"
- "hidreport.log"
- "iPad"
- "iPhone"
- "isHost"
- "logSubsystem"
- "lowercaseString"
- "manta-b"
- "manta-c"
- "markExposureNotificationLogsDone:"
- "resolvePathToMobileContainer:"
- "setExposureNotificationDBURL:"
- "setExposureNotificationGroup:"
- "setInitiatedByRemoteHost:"
- "setLogSubsystem:"
- "setWaitingToCaptureExposureNotificationLogs:"
- "shouldGatherCoSysdiagnoses"
- "startBTSessionAndTriggerExposureNotificationLogs:"
- "transferFileToHost:"
- "transferFileToHostIfNecessary:forDiagnosticID:"
- "triggerExposureNotificationLogs"
- "trusted"
- "untrusted"
- "v16@?0@\"OS_remote_device\"8"
- "waitForExposureNotificationLogsIfAvailable:"
- "waitingToCaptureExposureNotificationLogs"

```
