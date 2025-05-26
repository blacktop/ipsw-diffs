## GPUToolsTransport

> `/System/Library/PrivateFrameworks/GPUToolsTransport.framework/GPUToolsTransport`

```diff

-240.9.0.0.0
-  __TEXT.__text: 0x2a410
-  __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_methlist: 0x4af4
+270.12.0.0.0
+  __TEXT.__text: 0x2cdf4
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__objc_methlist: 0x4cb4
   __TEXT.__const: 0x208
-  __TEXT.__cstring: 0x2027
-  __TEXT.__oslogstring: 0x6b5
-  __TEXT.__unwind_info: 0xb00
-  __TEXT.__objc_classname: 0x103e
-  __TEXT.__objc_methname: 0x7541
-  __TEXT.__objc_methtype: 0x17da
-  __TEXT.__objc_stubs: 0x2960
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0xaf8
-  __DATA_CONST.__objc_classlist: 0x4a8
-  __DATA_CONST.__objc_protolist: 0x148
+  __TEXT.__cstring: 0x24fb
+  __TEXT.__oslogstring: 0x76a
+  __TEXT.__unwind_info: 0xb48
+  __TEXT.__objc_classname: 0x1091
+  __TEXT.__objc_methname: 0x7777
+  __TEXT.__objc_methtype: 0x1853
+  __TEXT.__objc_stubs: 0x2aa0
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0xa88
+  __DATA_CONST.__objc_classlist: 0x4b8
+  __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x98d0
-  __DATA_CONST.__objc_selrefs: 0x1970
+  __DATA_CONST.__objc_const: 0x9b70
+  __DATA_CONST.__objc_selrefs: 0x19f0
+  __DATA_CONST.__objc_protorefs: 0x98
+  __DATA_CONST.__objc_classrefs: 0x470
+  __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__cfstring: 0x29e0
+  __AUTH_CONST.__objc_const: 0x4260
+  __AUTH_CONST.__cfstring: 0x2e60
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_const: 0x41d0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__auth_got: 0x4e0
-  __AUTH.__objc_data: 0x2e90
-  __DATA.__objc_protorefs: 0x88
-  __DATA.__objc_classrefs: 0x470
-  __DATA.__objc_superrefs: 0x450
-  __DATA.__objc_ivar: 0x778
-  __DATA.__data: 0xf7c
+  __AUTH_CONST.__auth_got: 0x4f0
+  __AUTH.__objc_data: 0x2f30
+  __DATA.__objc_ivar: 0x7a0
+  __DATA.__data: 0xfdc
   __DATA.__common: 0x18
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1621
-  Symbols:   5791
-  CStrings:  2294
+  Functions: 1656
+  Symbols:   5903
+  CStrings:  2365
 
Symbols:
+ -[GTBulkDataServiceXPCProxy respondsToSelector:]
+ -[GTDeviceProperties reality]
+ -[GTDeviceProperties setReality:]
+ -[GTFileWriterService initWithConnectionProvider:deviceUDID:urlAccessProvider:]
+ -[GTFileWriterSessionUncompressed _closeCurrentFileDescriptor:]
+ -[GTLocalXPCConnection dispatchMessage:replyConnection:]
+ -[GTLoopbackServiceXPCProxy respondsToSelector:]
+ -[GTMTLReplayServiceXPCDispatcher initWithService:properties:bulkDataService:bulkDataServiceProperties:]
+ -[GTProcessInfo description]
+ -[GTProcessService description]
+ -[GTRelayedXPCConnection .cxx_destruct]
+ -[GTRelayedXPCConnection _setRoutingPropertiesForMessage:]
+ -[GTRelayedXPCConnection activateWithMessageHandler:andErrorHandler:]
+ -[GTRelayedXPCConnection cancel]
+ -[GTRelayedXPCConnection connection]
+ -[GTRelayedXPCConnection deregisterDispatcher:]
+ -[GTRelayedXPCConnection dispatchMessage:replyConnection:]
+ -[GTRelayedXPCConnection error]
+ -[GTRelayedXPCConnection initWithConnection:]
+ -[GTRelayedXPCConnection initWithConnection:relayPort:relayPid:]
+ -[GTRelayedXPCConnection registerDispatcher:]
+ -[GTRelayedXPCConnection registerDispatcher:forPort:]
+ -[GTRelayedXPCConnection sendMessage:]
+ -[GTRelayedXPCConnection sendMessage:replyHandler:]
+ -[GTRelayedXPCConnection sendMessageAndWaitForDelivery:]
+ -[GTRelayedXPCConnection sendMessageWithReplySync:error:]
+ -[GTRelayedXPCConnection setError:]
+ -[GTRelayedXPCConnection setHandleDeviceLocally]
+ -[GTRelayedXPCConnection updateRelayPort:pid:]
+ -[GTServiceConnection dispatchMessage:replyConnection:]
+ -[GTServiceProperties description]
+ -[GTSimulatorDeviceBrowserXPCProxy .cxx_destruct]
+ -[GTSimulatorDeviceBrowserXPCProxy deviceProperties:error:]
+ -[GTSimulatorDeviceBrowserXPCProxy initWithConnection:remoteProperties:]
+ -[GTSimulatorDeviceBrowserXPCProxy isSimulatorDevice:]
+ -[GTSimulatorDeviceBrowserXPCProxy respondsToSelector:]
+ -[GTURLAccessProvider _sharesFileSystemWith:remoteConnection:]
+ -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:].cold.3
+ -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:].cold.4
+ -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:].cold.5
+ -[GTURLAccessProvider initWithServiceProvider:connectionProvider:serviceVendor:]
+ -[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:].cold.3
+ -[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:].cold.4
+ -[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:].cold.5
+ -[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:].cold.6
+ -[GTUnsupportedFenumInfo asError]
+ -[GTUnsupportedFenumInfo customRecoverySuggestion]
+ -[GTUnsupportedFenumInfo initWithFenum:category:customMessage:customRecoverySuggestion:]
+ _GTCaptureErrorDomain
+ _NSLocalizedFailureReasonErrorKey
+ _OBJC_CLASS_$_GTRelayedXPCConnection
+ _OBJC_CLASS_$_GTSimulatorDeviceBrowserXPCProxy
+ _OBJC_IVAR_$_GTBulkDataServiceXPCProxy._ignoreMethods
+ _OBJC_IVAR_$_GTDeviceProperties._Reality
+ _OBJC_IVAR_$_GTFileWriterService._connectionProvider
+ _OBJC_IVAR_$_GTLoopbackServiceXPCProxy._ignoreMethods
+ _OBJC_IVAR_$_GTRelayedXPCConnection._connection
+ _OBJC_IVAR_$_GTRelayedXPCConnection._handleDeviceLocally
+ _OBJC_IVAR_$_GTRelayedXPCConnection._relayPid
+ _OBJC_IVAR_$_GTRelayedXPCConnection._relayPort
+ _OBJC_IVAR_$_GTSimulatorDeviceBrowserXPCProxy._connection
+ _OBJC_IVAR_$_GTSimulatorDeviceBrowserXPCProxy._ignoreMethods
+ _OBJC_IVAR_$_GTURLAccessProvider._connectionProvider
+ _OBJC_IVAR_$_GTURLAccessProvider._serviceProvider
+ _OBJC_IVAR_$_GTURLAccessProvider._serviceVendor
+ _OBJC_IVAR_$_GTUnsupportedFenumInfo._customRecoverySuggestion
+ _OBJC_METACLASS_$_GTRelayedXPCConnection
+ _OBJC_METACLASS_$_GTSimulatorDeviceBrowserXPCProxy
+ _OUTLINED_FUNCTION_5
+ _PrettifyFenumString
+ __OBJC_$_INSTANCE_METHODS_GTRelayedXPCConnection
+ __OBJC_$_INSTANCE_METHODS_GTSimulatorDeviceBrowserXPCProxy
+ __OBJC_$_INSTANCE_VARIABLES_GTRelayedXPCConnection
+ __OBJC_$_INSTANCE_VARIABLES_GTSimulatorDeviceBrowserXPCProxy
+ __OBJC_$_PROP_LIST_GTRelayedXPCConnection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GTSimulatorDeviceBrowser
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GTSimulatorDeviceBrowser
+ __OBJC_CLASS_PROTOCOLS_$_GTRelayedXPCConnection
+ __OBJC_CLASS_PROTOCOLS_$_GTSimulatorDeviceBrowserXPCProxy
+ __OBJC_CLASS_RO_$_GTRelayedXPCConnection
+ __OBJC_CLASS_RO_$_GTSimulatorDeviceBrowserXPCProxy
+ __OBJC_LABEL_PROTOCOL_$_GTSimulatorDeviceBrowser
+ __OBJC_METACLASS_RO_$_GTRelayedXPCConnection
+ __OBJC_METACLASS_RO_$_GTSimulatorDeviceBrowserXPCProxy
+ __OBJC_PROTOCOL_$_GTSimulatorDeviceBrowser
+ __OBJC_PROTOCOL_REFERENCE_$_GTBulkDataService
+ __OBJC_PROTOCOL_REFERENCE_$_GTSimulatorDeviceBrowser
+ ___113-[GTFileWriterService beginTransferSessionWithFileEntries:basePath:toDevice:options:sessionID:completionHandler:]_block_invoke.346
+ ___56-[GTLocalXPCConnection dispatchMessage:replyConnection:]_block_invoke
+ ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke.39
+ ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke.39.cold.1
+ ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke_2
+ ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke_2.cold.1
+ ___92-[GTFileWriterService initiateTransfer:basePath:fromDevice:toURL:options:completionHandler:]_block_invoke.cold.2
+ ___92-[GTFileWriterService initiateTransfer:basePath:fromDevice:toURL:options:completionHandler:]_block_invoke.cold.3
+ ___block_descriptor_56_8_32s40s48bs_e15_v16?0"NSURL"8ls32l8s40l8s48l8
+ ___block_descriptor_56_8_32s40s48s_e25_v16?0"GTReplayRequest"8ls32l8s40l8s48l8
+ ___block_descriptor_64_8_32s40s48s56w_e5_v8?0ls32l8s40l8s48l8w56l8
+ ___block_descriptor_72_8_32s40s48s56s_e26_v16?0"GTReplayResponse"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_96_8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ _fsync
+ _gt_xpc_dictionary_create_reply
+ _objc_msgSend$_closeCurrentFileDescriptor:
+ _objc_msgSend$_sharesFileSystemWith:remoteConnection:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$getSimulatorDeviceBrowserService:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$initWithConnection:relayPort:relayPid:
+ _objc_msgSend$isSimulatorDevice:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:options:range:
+ _objc_msgSend$substringFromIndex:
+ _objc_retain_x9
- -[GTFileWriterService _finishSession:error:].cold.1
- -[GTFileWriterService initWithRemoteConnectionProvider:deviceUDID:urlAccessProvider:]
- -[GTFileWriterSessionUncompressed _closeCurrentFileDescriptor]
- -[GTLocalXPCConnection dispatchMessage:]
- -[GTMTLReplayServiceXPCDispatcher initWithService:properties:bulkDataService:bulkDataServiceProperties:URLAccesService:]
- -[GTServiceConnection dispatchMessage:]
- -[GTURLAccessProvider initWithDeviceUDID:remoteConnectionProvider:]
- -[GTUnsupportedFenumInfo initWithFenum:category:customMessage:]
- -[GTUnsupportedFenumInfo reason]
- -[GTXPCDispatcher dispatchMessage:replyConnection:].cold.2
- _OBJC_IVAR_$_GTFileWriterService._remoteConnectionProvider
- _OBJC_IVAR_$_GTMTLReplayServiceXPCDispatcher._URLAccessService
- _OBJC_IVAR_$_GTURLAccessProvider._remoteConnectionProvider
- _OBJC_IVAR_$_GTURLAccessProvider._urlProviderQueue
- ___113-[GTFileWriterService beginTransferSessionWithFileEntries:basePath:toDevice:options:sessionID:completionHandler:]_block_invoke.323
- ___40-[GTLocalXPCConnection dispatchMessage:]_block_invoke
- ___62-[GTReplayProfileReplyStream dispatchMessage:replyConnection:]_block_invoke.cold.3
- ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke.30
- ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke.30.cold.1
- ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke.32
- ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke.32.cold.1
- ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke.cold.1
- ___79-[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:]_block_invoke.60
- ___79-[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:]_block_invoke.cold.1
- ___79-[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:]_block_invoke.cold.2
- ___92-[GTFileWriterService initiateTransfer:basePath:fromDevice:toURL:options:completionHandler:]_block_invoke.316
- ___92-[GTFileWriterService initiateTransfer:basePath:fromDevice:toURL:options:completionHandler:]_block_invoke.316.cold.1
- ___block_descriptor_48_8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_8_32s40s48s56w_e25_v16?0"GTReplayRequest"8ls32l8w56l8s40l8s48l8
- ___block_descriptor_64_8_32s40s48s_e26_v16?0"GTReplayResponse"8ls32l8s40l8s48l8
- ___block_descriptor_65_8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_8_32s40s48s56w64w_e5_v8?0ls32l8s40l8s48l8w56l8w64l8
- ___block_descriptor_88_8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s80l8s64l8s72l8
- ___block_descriptor_96_8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s80l8s40l8s48l8s56l8s64l8s72l8
- _objc_msgSend$_closeCurrentFileDescriptor
- _objc_msgSend$dispatchMessage:
CStrings:
+ "\x06"
+ "\n\n%@"
+ " "
+ "%@[%@%@]"
+ "&\x15"
+ "+"
+ "-"
+ "<%@: processName=%@ arguments=%@ environment=%@ bundleIdentifier=%@ processIdentifier=%d ppid=%d>"
+ "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu>"
+ "<%@: serviceProperties=%@ processInfo=%@>"
+ "@\"<GTConnectionProvider>\""
+ "@\"GTDeviceProperties\"32@0:8@\"NSString\"16^@24"
+ "@\"GTServiceVendor\""
+ "@36@0:8@16Q24i32"
+ "@48@0:8@16@24@32@40"
+ "B24@0:8@\"NSString\"16"
+ "B32@0:8@16@24"
+ "Capturing %@ is not supported."
+ "Capturing disabled. Unsupported API usage."
+ "Failed to close file"
+ "Failed to find URL access provider"
+ "Failed to find remote file writer service for device %@"
+ "Failed to flush file"
+ "Failed to transfer archive, %@"
+ "File should exist locally at %@ but can't be found on disk"
+ "File transfer failed in %@: %@"
+ "GTRelayedXPCConnection"
+ "GTReplayService"
+ "GTSimulatorDeviceBrowser"
+ "GTSimulatorDeviceBrowserXPCProxy"
+ "Initiate transfer basePath:%@ device:%@ toURL:%@ chunkSize:%lu compression:%s"
+ "Invalid device UDID passed to beginTransferSessionWithFileEntries"
+ "Invalid device UDID passed to copyIdentifier"
+ "Invalid device UDID passed to initiateTransfer"
+ "Invalid device UDID passed to startTransfer"
+ "Invalid path passed to beginTransferSessionWithFileEntries"
+ "Invalid path passed to initiateTransfer"
+ "Invalid path passed to startTransfer"
+ "Invalid processInfo argument passed to registerService"
+ "Invalid protocol name"
+ "Invalid sandbox ID"
+ "Invalid serviceProperties argument passed to registerService"
+ "Missing file writer service for device: %@"
+ "Missing remote connection for %@"
+ "Profiler Raw URL"
+ "Reality"
+ "T@\"NSObject<OS_xpc_object>\",&,N,V_connection"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_Reality"
+ "T@\"NSString\",R,N,V_customRecoverySuggestion"
+ "To enable capturing, disable calls to unsupported APIs and relaunch your application."
+ "Transfer session %llu completed successfully"
+ "Transfer session %llu failed with error \"%@\""
+ "Unsupported method: %@"
+ "_Reality"
+ "_closeCurrentFileDescriptor:"
+ "_connectionProvider"
+ "_customRecoverySuggestion"
+ "_handleDeviceLocally"
+ "_relayPid"
+ "_relayPort"
+ "_remoteDeviceRelayPid"
+ "_remoteDeviceRelayPort"
+ "_serviceVendor"
+ "_sharesFileSystemWith:remoteConnection:"
+ "asError"
+ "com.apple.gputools.capture"
+ "com.apple.gputools.serviceprovider"
+ "customRecoverySuggestion"
+ "dataWithBytes:length:"
+ "deviceProperties:error:"
+ "fileExistsAtPath:"
+ "getSimulatorDeviceBrowserService:"
+ "hasPrefix:"
+ "initWithConnection:relayPort:relayPid:"
+ "initWithConnectionProvider:deviceUDID:urlAccessProvider:"
+ "initWithFenum:category:customMessage:customRecoverySuggestion:"
+ "initWithService:properties:bulkDataService:bulkDataServiceProperties:"
+ "initWithServiceProvider:connectionProvider:serviceVendor:"
+ "isSimulatorDevice:"
+ "kDYFE"
+ "loading GPU trace"
+ "objectForKey:"
+ "rangeOfString:"
+ "reality"
+ "setHandleDeviceLocally"
+ "setReality:"
+ "stringByReplacingOccurrencesOfString:withString:options:range:"
+ "substringFromIndex:"
+ "updateRelayPort:pid:"
+ "v28@0:8Q16i24"
- "%\x15"
- "%@ API is not yet supported on this platform."
- "@\"<GTRemoteConnectionProvider>\""
- "@56@0:8@16@24@32@40@48"
- "Download Data handle:%llu"
- "Initiate transfer basePath:%@ device:%@ chunkSize:%lu compression:%s"
- "No remote connection"
- "Received data length:%lu"
- "T@\"<GTXPCConnection>\",&,N,V_connection"
- "Transfer session complete"
- "Unsupported selector: %s"
- "_URLAccessService"
- "_closeCurrentFileDescriptor"
- "_remoteConnectionProvider"
- "_urlProviderQueue"
- "com.apple.gputools.urlProvider"
- "dispatchMessage:"
- "finishSession %llu"
- "initWithDeviceUDID:remoteConnectionProvider:"
- "initWithFenum:category:customMessage:"
- "initWithRemoteConnectionProvider:deviceUDID:urlAccessProvider:"
- "initWithService:properties:bulkDataService:bulkDataServiceProperties:URLAccesService:"
- "path: %s"
- "reason"

```
