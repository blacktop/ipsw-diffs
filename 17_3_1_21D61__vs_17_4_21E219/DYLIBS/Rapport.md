## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-530.1.1.0.0
-  __TEXT.__text: 0x6ff00
-  __TEXT.__auth_stubs: 0x1120
-  __TEXT.__objc_methlist: 0x7130
-  __TEXT.__const: 0x1c35
-  __TEXT.__cstring: 0x11bb5
-  __TEXT.__gcc_except_tab: 0xf58
+542.1.0.0.0
+  __TEXT.__text: 0x76590
+  __TEXT.__auth_stubs: 0x1130
+  __TEXT.__objc_methlist: 0x7850
+  __TEXT.__const: 0x1cbf
+  __TEXT.__cstring: 0x12cf9
+  __TEXT.__gcc_except_tab: 0xfd8
   __TEXT.__oslogstring: 0x588
-  __TEXT.__unwind_info: 0x17d8
-  __TEXT.__objc_classname: 0x8ef
-  __TEXT.__objc_methname: 0xebf0
-  __TEXT.__objc_methtype: 0x2633
-  __TEXT.__objc_stubs: 0x7f40
+  __TEXT.__unwind_info: 0x1970
+  __TEXT.__objc_classname: 0x9ad
+  __TEXT.__objc_methname: 0xf4f0
+  __TEXT.__objc_methtype: 0x27be
+  __TEXT.__objc_stubs: 0x83a0
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x2168
-  __DATA_CONST.__objc_classlist: 0x210
+  __DATA_CONST.__const: 0x2280
+  __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe020
-  __DATA_CONST.__objc_selrefs: 0x3230
+  __DATA_CONST.__objc_const: 0xed38
+  __DATA_CONST.__objc_selrefs: 0x33e8
+  __DATA_CONST.__objc_protorefs: 0xa0
+  __DATA_CONST.__objc_classrefs: 0x268
+  __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__objc_const: 0x360
-  __AUTH_CONST.__cfstring: 0x45a0
+  __AUTH_CONST.__objc_const: 0x5a0
+  __AUTH_CONST.__cfstring: 0x4740
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x8a0
-  __DATA.__objc_protorefs: 0x90
-  __DATA.__objc_classrefs: 0x250
-  __DATA.__objc_superrefs: 0x198
-  __DATA.__objc_ivar: 0xf98
-  __DATA.__data: 0x1718
+  __AUTH_CONST.__auth_got: 0x8a8
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x1074
+  __DATA.__data: 0x1928
   __DATA.__bss: 0x118
   __DATA.__common: 0x0
-  __DATA_DIRTY.__const: 0x340
+  __DATA_DIRTY.__const: 0x360
   __DATA_DIRTY.__objc_const: 0x17e0
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x1a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99AD67E8-63EF-3842-B6CA-6EBADDE81109
-  Functions: 2961
-  Symbols:   9321
-  CStrings:  6191
+  UUID: B37A8868-7104-3214-A4BF-E8AEBD583606
+  Functions: 3142
+  Symbols:   9843
+  CStrings:  6407
 
Symbols:
+ +[RPNearbyInvitationDevice supportsSecureCoding]
+ +[RPNearbyInvitationDiscovery supportsSecureCoding]
+ +[RPNearbyInvitationServer supportsSecureCoding]
+ +[RPNearbyInvitationSession supportsSecureCoding]
+ -[RPClient removeSessionPairedIdentity:completion:]
+ -[RPCompanionLinkClient encodeSensitiveProperties]
+ -[RPCompanionLinkClient setEncodeSensitiveProperties:]
+ -[RPConnection _configureForSessionPairing:]
+ -[RPConnection bleConnectionPSM]
+ -[RPConnection setBleConnectionPSM:]
+ -[RPEndpoint encodeSensitiveProperties]
+ -[RPEndpoint encodedBLETargetData]
+ -[RPEndpoint setEncodeSensitiveProperties:]
+ -[RPEndpoint setEncodedBLETargetData:]
+ -[RPEndpoint updateWithEndpoint:]
+ -[RPFileTransferResumeStateItem sourceFileItemUsable:]
+ -[RPFileTransferSession _reportDataTransferred]
+ -[RPFileTransferSession _startProgressReportTimer]
+ -[RPFileTransferSession _stopProgressReportTimer]
+ -[RPFileTransferSession largeFileBufferBytes]
+ -[RPFileTransferSession maxLargeFileTasks]
+ -[RPFileTransferSession maxSmallFileTasks]
+ -[RPFileTransferSession progressHandlerTimeInterval]
+ -[RPFileTransferSession setLargeFileBufferBytes:]
+ -[RPFileTransferSession setMaxLargeFileTasks:]
+ -[RPFileTransferSession setMaxSmallFileTasks:]
+ -[RPFileTransferSession setProgressHandlerTimeInterval:]
+ -[RPNearbyInvitationDevice descriptionWithLevel:]
+ -[RPNearbyInvitationDevice description]
+ -[RPNearbyInvitationDevice deviceColor]
+ -[RPNearbyInvitationDevice encodeWithCoder:]
+ -[RPNearbyInvitationDevice inBubble]
+ -[RPNearbyInvitationDevice initWithCoder:]
+ -[RPNearbyInvitationDevice isEqualToDevice:]
+ -[RPNearbyInvitationDevice setInBubble:]
+ -[RPNearbyInvitationDevice setWasTriggered:]
+ -[RPNearbyInvitationDevice updateWithEndpoint:]
+ -[RPNearbyInvitationDevice updateWithSFDevice:]
+ -[RPNearbyInvitationDevice wasTriggered]
+ -[RPNearbyInvitationDiscovery .cxx_destruct]
+ -[RPNearbyInvitationDiscovery _activateWithCompletion:reactivate:]
+ -[RPNearbyInvitationDiscovery _ensureXPCStarted]
+ -[RPNearbyInvitationDiscovery _interrupted]
+ -[RPNearbyInvitationDiscovery _invalidated]
+ -[RPNearbyInvitationDiscovery activateWithCompletion:]
+ -[RPNearbyInvitationDiscovery description]
+ -[RPNearbyInvitationDiscovery deviceChangedHandler]
+ -[RPNearbyInvitationDiscovery deviceFoundHandler]
+ -[RPNearbyInvitationDiscovery deviceLostHandler]
+ -[RPNearbyInvitationDiscovery discoveredDevices]
+ -[RPNearbyInvitationDiscovery discoveryFlags]
+ -[RPNearbyInvitationDiscovery dispatchQueue]
+ -[RPNearbyInvitationDiscovery encodeWithCoder:]
+ -[RPNearbyInvitationDiscovery initWithCoder:]
+ -[RPNearbyInvitationDiscovery init]
+ -[RPNearbyInvitationDiscovery interruptionHandler]
+ -[RPNearbyInvitationDiscovery invalidate]
+ -[RPNearbyInvitationDiscovery invalidationHandler]
+ -[RPNearbyInvitationDiscovery nearbyInvitationChangedDevice:changes:]
+ -[RPNearbyInvitationDiscovery nearbyInvitationFoundDevice:]
+ -[RPNearbyInvitationDiscovery nearbyInvitationLostDevice:]
+ -[RPNearbyInvitationDiscovery setDeviceChangedHandler:]
+ -[RPNearbyInvitationDiscovery setDeviceFoundHandler:]
+ -[RPNearbyInvitationDiscovery setDeviceLostHandler:]
+ -[RPNearbyInvitationDiscovery setDiscoveryFlags:]
+ -[RPNearbyInvitationDiscovery setDispatchQueue:]
+ -[RPNearbyInvitationDiscovery setInterruptionHandler:]
+ -[RPNearbyInvitationDiscovery setInvalidationHandler:]
+ -[RPNearbyInvitationDiscovery shouldReportDevice:]
+ -[RPNearbyInvitationServer .cxx_destruct]
+ -[RPNearbyInvitationServer _activateWithCompletion:reactivate:]
+ -[RPNearbyInvitationServer _ensureXPCStarted]
+ -[RPNearbyInvitationServer _interrupted]
+ -[RPNearbyInvitationServer _invalidated]
+ -[RPNearbyInvitationServer activateWithCompletion:]
+ -[RPNearbyInvitationServer description]
+ -[RPNearbyInvitationServer dispatchQueue]
+ -[RPNearbyInvitationServer encodeWithCoder:]
+ -[RPNearbyInvitationServer initWithCoder:]
+ -[RPNearbyInvitationServer init]
+ -[RPNearbyInvitationServer interruptionHandler]
+ -[RPNearbyInvitationServer invalidate]
+ -[RPNearbyInvitationServer invalidationHandler]
+ -[RPNearbyInvitationServer nearbyInvitationReceivedEventID:event:options:sessionID:]
+ -[RPNearbyInvitationServer nearbyInvitationReceivedRequestID:request:options:responseHandler:sessionID:]
+ -[RPNearbyInvitationServer nearbyInvitationSessionEndedWithID:]
+ -[RPNearbyInvitationServer nearbyInvitationStartServerSessionID:device:completion:]
+ -[RPNearbyInvitationServer serviceType]
+ -[RPNearbyInvitationServer sessionEndedHandler]
+ -[RPNearbyInvitationServer sessionStartHandler]
+ -[RPNearbyInvitationServer setDispatchQueue:]
+ -[RPNearbyInvitationServer setInterruptionHandler:]
+ -[RPNearbyInvitationServer setInvalidationHandler:]
+ -[RPNearbyInvitationServer setServiceType:]
+ -[RPNearbyInvitationServer setSessionEndedHandler:]
+ -[RPNearbyInvitationServer setSessionStartHandler:]
+ -[RPNearbyInvitationSession .cxx_destruct]
+ -[RPNearbyInvitationSession _activateWithCompletion:reactivate:]
+ -[RPNearbyInvitationSession _ensureXPCStarted]
+ -[RPNearbyInvitationSession _interrupted]
+ -[RPNearbyInvitationSession _invalidated]
+ -[RPNearbyInvitationSession _sendRequestID:request:destinationID:options:responseHandler:]
+ -[RPNearbyInvitationSession activateWithCompletion:]
+ -[RPNearbyInvitationSession daemonDevice]
+ -[RPNearbyInvitationSession deregisterEventID:]
+ -[RPNearbyInvitationSession deregisterRequestID:]
+ -[RPNearbyInvitationSession description]
+ -[RPNearbyInvitationSession destinationDevice]
+ -[RPNearbyInvitationSession dispatchQueue]
+ -[RPNearbyInvitationSession encodeWithCoder:]
+ -[RPNearbyInvitationSession errorHandler]
+ -[RPNearbyInvitationSession failedToConnect]
+ -[RPNearbyInvitationSession initWithCoder:]
+ -[RPNearbyInvitationSession init]
+ -[RPNearbyInvitationSession interruptionHandler]
+ -[RPNearbyInvitationSession invalidate]
+ -[RPNearbyInvitationSession invalidationHandler]
+ -[RPNearbyInvitationSession nearbyInvitationReceivedEventID:event:options:sessionID:]
+ -[RPNearbyInvitationSession nearbyInvitationReceivedRequestID:request:options:responseHandler:sessionID:]
+ -[RPNearbyInvitationSession nearbyInvitationSessionError:]
+ -[RPNearbyInvitationSession registerEventID:options:handler:]
+ -[RPNearbyInvitationSession registerRequestID:options:handler:]
+ -[RPNearbyInvitationSession sendEventID:event:destinationID:options:completion:]
+ -[RPNearbyInvitationSession sendEventID:event:options:completion:]
+ -[RPNearbyInvitationSession sendRequestID:request:destinationID:options:responseHandler:]
+ -[RPNearbyInvitationSession sendRequestID:request:options:responseHandler:]
+ -[RPNearbyInvitationSession server]
+ -[RPNearbyInvitationSession serviceType]
+ -[RPNearbyInvitationSession sessionID]
+ -[RPNearbyInvitationSession setDaemonDevice:]
+ -[RPNearbyInvitationSession setDestinationDevice:]
+ -[RPNearbyInvitationSession setDispatchQueue:]
+ -[RPNearbyInvitationSession setErrorHandler:]
+ -[RPNearbyInvitationSession setFailedToConnect:]
+ -[RPNearbyInvitationSession setInterruptionHandler:]
+ -[RPNearbyInvitationSession setInvalidationHandler:]
+ -[RPNearbyInvitationSession setServer:]
+ -[RPNearbyInvitationSession setServiceType:]
+ -[RPNearbyInvitationSession setSessionID:]
+ -[RPNearbyInvitationSession setWaitingToConnect:]
+ -[RPNearbyInvitationSession setXpcCnx:]
+ -[RPNearbyInvitationSession waitingToConnect]
+ -[RPNearbyInvitationSession xpcCnx]
+ -[RPServer advertiseDeviceName]
+ -[RPServer setAdvertiseDeviceName:]
+ GCC_except_table112
+ GCC_except_table133
+ GCC_except_table150
+ GCC_except_table155
+ GCC_except_table160
+ GCC_except_table176
+ GCC_except_table18
+ GCC_except_table190
+ GCC_except_table195
+ GCC_except_table197
+ GCC_except_table21
+ GCC_except_table210
+ GCC_except_table68
+ GCC_except_table70
+ _OBJC_CLASS_$_CUPairingIdentity
+ _OBJC_CLASS_$_RPNearbyInvitationDevice
+ _OBJC_CLASS_$_RPNearbyInvitationDiscovery
+ _OBJC_CLASS_$_RPNearbyInvitationServer
+ _OBJC_CLASS_$_RPNearbyInvitationSession
+ _OBJC_IVAR_$_RPCompanionLinkClient._encodeSensitiveProperties
+ _OBJC_IVAR_$_RPConnection._bleConnectionPSM
+ _OBJC_IVAR_$_RPEndpoint._encodeSensitiveProperties
+ _OBJC_IVAR_$_RPEndpoint._encodedBLETargetData
+ _OBJC_IVAR_$_RPFileTransferSession._largeFileBufferBytes
+ _OBJC_IVAR_$_RPFileTransferSession._maxLargeFileTasks
+ _OBJC_IVAR_$_RPFileTransferSession._maxSmallFileTasks
+ _OBJC_IVAR_$_RPFileTransferSession._progressCurrentBytes
+ _OBJC_IVAR_$_RPFileTransferSession._progressCurrentFiles
+ _OBJC_IVAR_$_RPFileTransferSession._progressDirty
+ _OBJC_IVAR_$_RPFileTransferSession._progressHandlerTimeInterval
+ _OBJC_IVAR_$_RPFileTransferSession._progressTimer
+ _OBJC_IVAR_$_RPFileTransferSession._progressTotalBytes
+ _OBJC_IVAR_$_RPFileTransferSession._progressTotalFiles
+ _OBJC_IVAR_$_RPNearbyInvitationDevice._deviceColor
+ _OBJC_IVAR_$_RPNearbyInvitationDevice._inBubble
+ _OBJC_IVAR_$_RPNearbyInvitationDevice._wasTriggered
+ _OBJC_IVAR_$_RPNearbyInvitationDiscovery._activateCalled
+ _OBJC_IVAR_$_RPNearbyInvitationDiscovery._deviceChangedHandler
+ _OBJC_IVAR_$_RPNearbyInvitationDiscovery._deviceFoundHandler
+ _OBJC_IVAR_$_RPNearbyInvitationDiscovery._deviceLostHandler
+ _OBJC_IVAR_$_RPNearbyInvitationDiscovery._discoveredDevices
+ _OBJC_IVAR_$_RPNearbyInvitationDiscovery._discoveryFlags
+ _OBJC_IVAR_$_RPNearbyInvitationDiscovery._dispatchQueue
+ _OBJC_IVAR_$_RPNearbyInvitationDiscovery._interruptionHandler
+ _OBJC_IVAR_$_RPNearbyInvitationDiscovery._invalidateCalled
+ _OBJC_IVAR_$_RPNearbyInvitationDiscovery._invalidateDone
+ _OBJC_IVAR_$_RPNearbyInvitationDiscovery._invalidationHandler
+ _OBJC_IVAR_$_RPNearbyInvitationDiscovery._xpcCnx
+ _OBJC_IVAR_$_RPNearbyInvitationServer._activateCalled
+ _OBJC_IVAR_$_RPNearbyInvitationServer._dispatchQueue
+ _OBJC_IVAR_$_RPNearbyInvitationServer._interruptionHandler
+ _OBJC_IVAR_$_RPNearbyInvitationServer._invalidateCalled
+ _OBJC_IVAR_$_RPNearbyInvitationServer._invalidateDone
+ _OBJC_IVAR_$_RPNearbyInvitationServer._invalidationHandler
+ _OBJC_IVAR_$_RPNearbyInvitationServer._serviceType
+ _OBJC_IVAR_$_RPNearbyInvitationServer._sessionEndedHandler
+ _OBJC_IVAR_$_RPNearbyInvitationServer._sessionStartHandler
+ _OBJC_IVAR_$_RPNearbyInvitationServer._sessions
+ _OBJC_IVAR_$_RPNearbyInvitationServer._xpcCnx
+ _OBJC_IVAR_$_RPNearbyInvitationSession._activateCalled
+ _OBJC_IVAR_$_RPNearbyInvitationSession._daemonDevice
+ _OBJC_IVAR_$_RPNearbyInvitationSession._destinationDevice
+ _OBJC_IVAR_$_RPNearbyInvitationSession._dispatchQueue
+ _OBJC_IVAR_$_RPNearbyInvitationSession._errorHandler
+ _OBJC_IVAR_$_RPNearbyInvitationSession._eventRegistrations
+ _OBJC_IVAR_$_RPNearbyInvitationSession._failedToConnect
+ _OBJC_IVAR_$_RPNearbyInvitationSession._interruptionHandler
+ _OBJC_IVAR_$_RPNearbyInvitationSession._invalidateCalled
+ _OBJC_IVAR_$_RPNearbyInvitationSession._invalidateDone
+ _OBJC_IVAR_$_RPNearbyInvitationSession._invalidationHandler
+ _OBJC_IVAR_$_RPNearbyInvitationSession._requestRegistrations
+ _OBJC_IVAR_$_RPNearbyInvitationSession._server
+ _OBJC_IVAR_$_RPNearbyInvitationSession._serviceType
+ _OBJC_IVAR_$_RPNearbyInvitationSession._sessionID
+ _OBJC_IVAR_$_RPNearbyInvitationSession._waitingToConnect
+ _OBJC_IVAR_$_RPNearbyInvitationSession._xpcCnx
+ _OBJC_IVAR_$_RPServer._advertiseDeviceName
+ _OBJC_METACLASS_$_RPNearbyInvitationDevice
+ _OBJC_METACLASS_$_RPNearbyInvitationDiscovery
+ _OBJC_METACLASS_$_RPNearbyInvitationServer
+ _OBJC_METACLASS_$_RPNearbyInvitationSession
+ _RPOptionSenderAccountAltDSID
+ __OBJC_$_CLASS_METHODS_RPNearbyInvitationDevice
+ __OBJC_$_CLASS_METHODS_RPNearbyInvitationDiscovery
+ __OBJC_$_CLASS_METHODS_RPNearbyInvitationServer
+ __OBJC_$_CLASS_METHODS_RPNearbyInvitationSession
+ __OBJC_$_CLASS_PROP_LIST_RPNearbyInvitationDevice
+ __OBJC_$_CLASS_PROP_LIST_RPNearbyInvitationDiscovery
+ __OBJC_$_CLASS_PROP_LIST_RPNearbyInvitationServer
+ __OBJC_$_CLASS_PROP_LIST_RPNearbyInvitationSession
+ __OBJC_$_INSTANCE_METHODS_RPNearbyInvitationDevice
+ __OBJC_$_INSTANCE_METHODS_RPNearbyInvitationDiscovery
+ __OBJC_$_INSTANCE_METHODS_RPNearbyInvitationServer
+ __OBJC_$_INSTANCE_METHODS_RPNearbyInvitationSession
+ __OBJC_$_INSTANCE_VARIABLES_RPNearbyInvitationDevice
+ __OBJC_$_INSTANCE_VARIABLES_RPNearbyInvitationDiscovery
+ __OBJC_$_INSTANCE_VARIABLES_RPNearbyInvitationServer
+ __OBJC_$_INSTANCE_VARIABLES_RPNearbyInvitationSession
+ __OBJC_$_PROP_LIST_RPNearbyInvitationDevice
+ __OBJC_$_PROP_LIST_RPNearbyInvitationDiscovery
+ __OBJC_$_PROP_LIST_RPNearbyInvitationServer
+ __OBJC_$_PROP_LIST_RPNearbyInvitationSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_RPNearbyInvitationXPCClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RPNearbyInvitationXPCDaemonInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RPNearbyInvitationXPCClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RPNearbyInvitationXPCDaemonInterface
+ __OBJC_$_PROTOCOL_REFS_RPNearbyInvitationXPCClientInterface
+ __OBJC_$_PROTOCOL_REFS_RPNearbyInvitationXPCDaemonInterface
+ __OBJC_CLASS_PROTOCOLS_$_RPNearbyInvitationDevice
+ __OBJC_CLASS_PROTOCOLS_$_RPNearbyInvitationDiscovery
+ __OBJC_CLASS_PROTOCOLS_$_RPNearbyInvitationServer
+ __OBJC_CLASS_PROTOCOLS_$_RPNearbyInvitationSession
+ __OBJC_CLASS_RO_$_RPNearbyInvitationDevice
+ __OBJC_CLASS_RO_$_RPNearbyInvitationDiscovery
+ __OBJC_CLASS_RO_$_RPNearbyInvitationServer
+ __OBJC_CLASS_RO_$_RPNearbyInvitationSession
+ __OBJC_LABEL_PROTOCOL_$_RPNearbyInvitationXPCClientInterface
+ __OBJC_LABEL_PROTOCOL_$_RPNearbyInvitationXPCDaemonInterface
+ __OBJC_METACLASS_RO_$_RPNearbyInvitationDevice
+ __OBJC_METACLASS_RO_$_RPNearbyInvitationDiscovery
+ __OBJC_METACLASS_RO_$_RPNearbyInvitationServer
+ __OBJC_METACLASS_RO_$_RPNearbyInvitationSession
+ __OBJC_PROTOCOL_$_RPNearbyInvitationXPCClientInterface
+ __OBJC_PROTOCOL_$_RPNearbyInvitationXPCDaemonInterface
+ __OBJC_PROTOCOL_REFERENCE_$_RPNearbyInvitationXPCClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_RPNearbyInvitationXPCDaemonInterface
+ ___38-[RPNearbyInvitationServer invalidate]_block_invoke
+ ___38-[RPNearbyInvitationServer invalidate]_block_invoke_2
+ ___39-[RPNearbyInvitationSession invalidate]_block_invoke
+ ___41-[RPNearbyInvitationDiscovery invalidate]_block_invoke
+ ___44-[RPConnection _configureForSessionPairing:]_block_invoke
+ ___44-[RPConnection _configureForSessionPairing:]_block_invoke_2
+ ___44-[RPConnection _configureForSessionPairing:]_block_invoke_3
+ ___45-[RPNearbyInvitationServer _ensureXPCStarted]_block_invoke
+ ___45-[RPNearbyInvitationServer _ensureXPCStarted]_block_invoke_2
+ ___46-[RPNearbyInvitationSession _ensureXPCStarted]_block_invoke
+ ___46-[RPNearbyInvitationSession _ensureXPCStarted]_block_invoke_2
+ ___47-[RPNearbyInvitationSession deregisterEventID:]_block_invoke
+ ___48-[RPFileTransferSession _smallFilesSendTaskRun:]_block_invoke.425
+ ___48-[RPFileTransferSession _smallFilesSendTaskRun:]_block_invoke_2.428
+ ___48-[RPFileTransferSession _smallFilesSendTaskRun:]_block_invoke_3
+ ___48-[RPNearbyInvitationDiscovery _ensureXPCStarted]_block_invoke
+ ___48-[RPNearbyInvitationDiscovery _ensureXPCStarted]_block_invoke_2
+ ___49-[RPFileTransferSession _largeFileSendTaskStart:]_block_invoke_3
+ ___49-[RPNearbyInvitationSession deregisterRequestID:]_block_invoke
+ ___50-[RPFileTransferSession _startProgressReportTimer]_block_invoke
+ ___51-[RPClient removeSessionPairedIdentity:completion:]_block_invoke
+ ___51-[RPClient removeSessionPairedIdentity:completion:]_block_invoke_2
+ ___51-[RPNearbyInvitationServer activateWithCompletion:]_block_invoke
+ ___52-[RPNearbyInvitationSession activateWithCompletion:]_block_invoke
+ ___54-[RPNearbyInvitationDiscovery activateWithCompletion:]_block_invoke
+ ___58-[RPNearbyInvitationSession nearbyInvitationSessionError:]_block_invoke
+ ___61-[RPNearbyInvitationSession registerEventID:options:handler:]_block_invoke
+ ___63-[RPNearbyInvitationServer _activateWithCompletion:reactivate:]_block_invoke
+ ___63-[RPNearbyInvitationServer _activateWithCompletion:reactivate:]_block_invoke_2
+ ___63-[RPNearbyInvitationSession registerRequestID:options:handler:]_block_invoke
+ ___64-[RPNearbyInvitationSession _activateWithCompletion:reactivate:]_block_invoke
+ ___64-[RPNearbyInvitationSession _activateWithCompletion:reactivate:]_block_invoke_2
+ ___66-[RPNearbyInvitationDiscovery _activateWithCompletion:reactivate:]_block_invoke
+ ___66-[RPNearbyInvitationDiscovery _activateWithCompletion:reactivate:]_block_invoke_2
+ ___80-[RPNearbyInvitationSession sendEventID:event:destinationID:options:completion:]_block_invoke
+ ___80-[RPNearbyInvitationSession sendEventID:event:destinationID:options:completion:]_block_invoke_2
+ ___81-[RPFileTransferSession _largeFileReceiveTaskRun:data:sendFlags:responseHandler:]_block_invoke_8
+ ___89-[RPNearbyInvitationSession sendRequestID:request:destinationID:options:responseHandler:]_block_invoke
+ ___90-[RPNearbyInvitationSession _sendRequestID:request:destinationID:options:responseHandler:]_block_invoke
+ ___90-[RPNearbyInvitationSession _sendRequestID:request:destinationID:options:responseHandler:]_block_invoke_2
+ ___block_descriptor_32_e52_v32?0"NSNumber"8"RPNearbyInvitationSession"16^B24l
+ ___block_descriptor_48_e8_32s40s_e29_B32?0"CUPairedPeer"8Q16^24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e31_"CUPairingIdentity"24?0Q8^16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e43_"CUPairedPeer"32?0"CUPairedPeer"8Q16^24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_61_e8_32s40s48s_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_69_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_77_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_literal_global.1274
+ ___block_literal_global.137
+ ___block_literal_global.272
+ __unnamed_array_storage.356
+ __unnamed_array_storage.379
+ __unnamed_array_storage.380
+ _gLogCategory_RPNearbyInvitationDiscovery
+ _gLogCategory_RPNearbyInvitationServer
+ _gLogCategory_RPNearbyInvitationSession
+ _objc_msgSend$_configureForSessionPairing:
+ _objc_msgSend$_reportDataTransferred
+ _objc_msgSend$_startProgressReportTimer
+ _objc_msgSend$_stopProgressReportTimer
+ _objc_msgSend$addSessionPairedIdentity:
+ _objc_msgSend$bleTargetData
+ _objc_msgSend$deviceClassCode
+ _objc_msgSend$deviceModelCode
+ _objc_msgSend$identitiesOfType:error:
+ _objc_msgSend$initWithPairedPeer:type:
+ _objc_msgSend$largeFileBufferBytes
+ _objc_msgSend$maxLargeFileTasks
+ _objc_msgSend$maxSmallFileTasks
+ _objc_msgSend$nearbyInvitationActivateDiscovery:completion:
+ _objc_msgSend$nearbyInvitationActivateServer:completion:
+ _objc_msgSend$nearbyInvitationActivateSession:completion:
+ _objc_msgSend$nearbyInvitationInvalidateClientSession
+ _objc_msgSend$nearbyInvitationInvalidateSessionID:
+ _objc_msgSend$nearbyInvitationReceivedEventID:event:options:sessionID:
+ _objc_msgSend$nearbyInvitationReceivedRequestID:request:options:responseHandler:sessionID:
+ _objc_msgSend$nearbyInvitationSendEventID:event:options:completion:
+ _objc_msgSend$nearbyInvitationSendRequestID:request:options:responseHandler:
+ _objc_msgSend$progressHandlerTimeInterval
+ _objc_msgSend$removeSessionPairedIdentity:completion:
+ _objc_msgSend$sessionPairingIdentifier
+ _objc_msgSend$setAltIRK:
+ _objc_msgSend$setCopyIdentityHandler:
+ _objc_msgSend$setFindPeerHandler:
+ _objc_msgSend$setLargeFileBufferBytes:
+ _objc_msgSend$setMaxLargeFileTasks:
+ _objc_msgSend$setMaxSmallFileTasks:
+ _objc_msgSend$setProgressHandlerTimeInterval:
+ _objc_msgSend$setPublicKey:
+ _objc_msgSend$setSavePeerHandler:
+ _objc_msgSend$setSecretKey:
+ _objc_msgSend$sourceFileItemUsable:
+ _objc_retain_x10
- -[RPFileTransferResumeStateItem sourceFileItemUsable]
- GCC_except_table105
- GCC_except_table126
- GCC_except_table142
- GCC_except_table147
- GCC_except_table152
- GCC_except_table167
- GCC_except_table180
- GCC_except_table185
- GCC_except_table187
- GCC_except_table200
- GCC_except_table63
- _OBJC_IVAR_$_RPFileTransferSession._prefLargeFileBufferBytes
- _OBJC_IVAR_$_RPFileTransferSession._prefLargeFileMaxTasks
- _OBJC_IVAR_$_RPFileTransferSession._prefSmallFilesMaxTasks
- ___48-[RPFileTransferSession _smallFilesSendTaskRun:]_block_invoke.412
- ___48-[RPFileTransferSession _smallFilesSendTaskRun:]_block_invoke_2.415
- ___block_descriptor_48_e8_32s40s_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8
- ___block_descriptor_53_e8_32s40s_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8
- ___block_descriptor_61_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_69_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_literal_global.1255
- ___block_literal_global.136
- ___block_literal_global.271
- __unnamed_array_storage.343
- __unnamed_array_storage.366
- __unnamed_array_storage.367
- _objc_msgSend$sourceFileItemUsable
CStrings:
+ "\x05\x13\x14A\x13("
+ "\x11\x11\x1a"
+ "\x11\x15\x12"
+ "\x14\x13!\x15\x122\x14\x11\x91\xf0\xc1\x133\x16"
+ "\x18"
+ " %@"
+ " color=%d"
+ "### Failed to get self identity: %@\n."
+ "### Interrupted"
+ "### No registration found for incoming event '%@'"
+ "### Null session ID, dropping received event `%@`\n"
+ "### Null session ID, dropping received request `%@`\n"
+ ", AdvName %s"
+ ", LBuf: %llu"
+ ", Label %@"
+ ", MaxLargeTasks: %u"
+ ", MaxSmallTasks: %u"
+ ", PVAuth %s"
+ "-[RPConnection _configureForSessionPairing:]_block_invoke"
+ "-[RPConnection _configureForSessionPairing:]_block_invoke_2"
+ "-[RPConnection _configureForSessionPairing:]_block_invoke_3"
+ "-[RPFileTransferResumeStateItem outputFileItemUsable:]"
+ "-[RPFileTransferResumeStateItem sourceFileItemUsable:]"
+ "-[RPFileTransferSession _reportDataTransferred]"
+ "-[RPFileTransferSession setLargeFileBufferBytes:]"
+ "-[RPFileTransferSession setMaxLargeFileTasks:]"
+ "-[RPFileTransferSession setMaxSmallFileTasks:]"
+ "-[RPNearbyInvitationDiscovery _activateWithCompletion:reactivate:]"
+ "-[RPNearbyInvitationDiscovery _activateWithCompletion:reactivate:]_block_invoke"
+ "-[RPNearbyInvitationDiscovery _activateWithCompletion:reactivate:]_block_invoke_2"
+ "-[RPNearbyInvitationDiscovery _ensureXPCStarted]"
+ "-[RPNearbyInvitationDiscovery _interrupted]"
+ "-[RPNearbyInvitationDiscovery _invalidated]"
+ "-[RPNearbyInvitationDiscovery invalidate]_block_invoke"
+ "-[RPNearbyInvitationServer _activateWithCompletion:reactivate:]"
+ "-[RPNearbyInvitationServer _activateWithCompletion:reactivate:]_block_invoke"
+ "-[RPNearbyInvitationServer _activateWithCompletion:reactivate:]_block_invoke_2"
+ "-[RPNearbyInvitationServer _ensureXPCStarted]"
+ "-[RPNearbyInvitationServer _interrupted]"
+ "-[RPNearbyInvitationServer _invalidated]"
+ "-[RPNearbyInvitationServer invalidate]_block_invoke"
+ "-[RPNearbyInvitationServer nearbyInvitationReceivedEventID:event:options:sessionID:]"
+ "-[RPNearbyInvitationServer nearbyInvitationReceivedRequestID:request:options:responseHandler:sessionID:]"
+ "-[RPNearbyInvitationSession _activateWithCompletion:reactivate:]"
+ "-[RPNearbyInvitationSession _activateWithCompletion:reactivate:]_block_invoke"
+ "-[RPNearbyInvitationSession _activateWithCompletion:reactivate:]_block_invoke_2"
+ "-[RPNearbyInvitationSession _ensureXPCStarted]"
+ "-[RPNearbyInvitationSession _interrupted]"
+ "-[RPNearbyInvitationSession _invalidated]"
+ "-[RPNearbyInvitationSession _sendRequestID:request:destinationID:options:responseHandler:]_block_invoke"
+ "-[RPNearbyInvitationSession _sendRequestID:request:destinationID:options:responseHandler:]_block_invoke_2"
+ "-[RPNearbyInvitationSession deregisterEventID:]_block_invoke"
+ "-[RPNearbyInvitationSession deregisterRequestID:]_block_invoke"
+ "-[RPNearbyInvitationSession invalidate]_block_invoke"
+ "-[RPNearbyInvitationSession nearbyInvitationReceivedEventID:event:options:sessionID:]"
+ "-[RPNearbyInvitationSession registerEventID:options:handler:]_block_invoke"
+ "-[RPNearbyInvitationSession registerRequestID:options:handler:]_block_invoke"
+ "-[RPNearbyInvitationSession sendEventID:event:destinationID:options:completion:]_block_invoke"
+ "-[RPNearbyInvitationSession sendEventID:event:destinationID:options:completion:]_block_invoke_2"
+ "-[RPNearbyInvitationSession sendRequestID:request:destinationID:options:responseHandler:]"
+ "542.1"
+ "@\"CUPairedPeer\"32@?0@\"CUPairedPeer\"8Q16^@24"
+ "@\"CUPairingIdentity\"24@?0Q8^@16"
+ "@\"RPNearbyInvitationDevice\""
+ "@\"RPNearbyInvitationServer\""
+ "AudioAccessory1,1"
+ "AudioAccessory5,1"
+ "AudioAccessory6,1"
+ "B32@?0@\"CUPairedPeer\"8Q16^@24"
+ "DataTransferred"
+ "Find paired peer handler for peer %@ options %lu\n"
+ "FindNearbyPencil"
+ "Ignoring RPFileTransferResumeStateItem: failed transfer: '%s'"
+ "Ignoring RPFileTransferResumeStateItem: file modification time not matching: '%s'"
+ "Ignoring RPFileTransferResumeStateItem: file not present: '%s'"
+ "Ignoring RPFileTransferResumeStateItem: file size = %ld bytes, expected %ld bytes: '%s'"
+ "Ignoring RPFileTransferResumeStateItem: no file offset: '%s'"
+ "Ignoring RPFileTransferResumeStateItem: stat() failed: '%s'"
+ "LargeFileBufferBytes: %llu -> %llu\n"
+ "LargeFileMaxTasks: %llu -> %llu\n"
+ "PairSetup completed client.\n"
+ "RPFileTransferResumeStateItem: output file is resumable: '%s'"
+ "RPFileTransferResumeStateItem: source file is resumable: '%s'"
+ "RPNearbyInvitationDevice"
+ "RPNearbyInvitationDiscovery"
+ "RPNearbyInvitationDiscovery %{ptr}"
+ "RPNearbyInvitationServer"
+ "RPNearbyInvitationServer %{ptr}"
+ "RPNearbyInvitationSession"
+ "RPNearbyInvitationSession %{ptr} "
+ "RPNearbyInvitationXPCClientInterface"
+ "RPNearbyInvitationXPCDaemonInterface"
+ "Requested password type: %s auth type: %s\n"
+ "S16@0:8"
+ "SafetyAlerts"
+ "Save paired peer handler for peer %@ options %lu\n"
+ "SharingVisionProDiscovery"
+ "SharingVisionProStateChange"
+ "SmallFileMaxTasks: %llu -> %llu\n"
+ "T@\"NSData\",C,N,V_encodedBLETargetData"
+ "T@\"NSString\",?,R,C"
+ "T@\"RPNearbyInvitationDevice\",&,N,V_daemonDevice"
+ "T@\"RPNearbyInvitationDevice\",&,N,V_destinationDevice"
+ "T@\"RPNearbyInvitationServer\",&,N,V_server"
+ "TB,N,V_advertiseDeviceName"
+ "TB,N,V_encodeSensitiveProperties"
+ "TB,N,V_failedToConnect"
+ "TB,N,V_inBubble"
+ "TB,N,V_waitingToConnect"
+ "TB,N,V_wasTriggered"
+ "TC,R,N,V_deviceColor"
+ "TQ,N,V_largeFileBufferBytes"
+ "TQ,N,V_maxLargeFileTasks"
+ "TQ,N,V_maxSmallFileTasks"
+ "TS,N,V_bleConnectionPSM"
+ "Td,N,V_progressHandlerTimeInterval"
+ "Temporary identity of the peer was not found."
+ "_advertiseDeviceName"
+ "_bleConnectionPSM"
+ "_configureForSessionPairing:"
+ "_disFl"
+ "_encodeSensitiveProperties"
+ "_encodedBLETargetData"
+ "_failedToConnect"
+ "_inBubble"
+ "_largeFileBufferBytes"
+ "_maxLargeFileTasks"
+ "_maxSmallFileTasks"
+ "_progressCurrentBytes"
+ "_progressCurrentFiles"
+ "_progressDirty"
+ "_progressHandlerTimeInterval"
+ "_progressTimer"
+ "_progressTotalBytes"
+ "_progressTotalFiles"
+ "_reportDataTransferred"
+ "_startProgressReportTimer"
+ "_stopProgressReportTimer"
+ "_waitingToConnect"
+ "_wasTriggered"
+ "addSessionPairedIdentity:"
+ "advertiseDeviceName"
+ "bleConnectionPSM"
+ "bleTD"
+ "cc"
+ "com.apple.rapport.NearbyInvitation"
+ "devName"
+ "deviceClassCode"
+ "deviceModelCode"
+ "encodeSensitiveProperties"
+ "encodedBLETargetData"
+ "esp"
+ "failedToConnect"
+ "identitiesOfType:error:"
+ "inBubble"
+ "lFlBufB"
+ "lFlMxTs"
+ "largeFileBufferBytes"
+ "maxLargeFileTasks"
+ "maxSmallFileTasks"
+ "nearbyInvitationActivateDiscovery:completion:"
+ "nearbyInvitationActivateServer:completion:"
+ "nearbyInvitationActivateSession:completion:"
+ "nearbyInvitationChangedDevice:changes:"
+ "nearbyInvitationFoundDevice:"
+ "nearbyInvitationInvalidateClientSession"
+ "nearbyInvitationInvalidateSessionID:"
+ "nearbyInvitationLostDevice:"
+ "nearbyInvitationReceivedEventID:event:options:sessionID:"
+ "nearbyInvitationReceivedRequestID:request:options:responseHandler:sessionID:"
+ "nearbyInvitationSendEventID:event:options:completion:"
+ "nearbyInvitationSendRequestID:request:options:responseHandler:"
+ "nearbyInvitationSessionEndedWithID:"
+ "nearbyInvitationSessionError:"
+ "nearbyInvitationStartServerSessionID:device:completion:"
+ "progressHandlerTimeInterval"
+ "removeSessionPairedIdentity:completion:"
+ "sFlMxTs"
+ "senderAccountAltDSID"
+ "sessionPairingIdentifier"
+ "setAdvertiseDeviceName:"
+ "setAltIRK:"
+ "setBleConnectionPSM:"
+ "setCopyIdentityHandler:"
+ "setEncodeSensitiveProperties:"
+ "setEncodedBLETargetData:"
+ "setFailedToConnect:"
+ "setFindPeerHandler:"
+ "setInBubble:"
+ "setLargeFileBufferBytes:"
+ "setMaxLargeFileTasks:"
+ "setMaxSmallFileTasks:"
+ "setProgressHandlerTimeInterval:"
+ "setPublicKey:"
+ "setSavePeerHandler:"
+ "setSecretKey:"
+ "setWaitingToConnect:"
+ "setWasTriggered:"
+ "sourceFileItemUsable:"
+ "v20@0:8S16"
+ "v24@0:8@\"RPNearbyInvitationDevice\"16"
+ "v28@0:8@\"RPNearbyInvitationDevice\"16I24"
+ "v32@0:8@\"RPNearbyInvitationDiscovery\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"RPNearbyInvitationServer\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"RPNearbyInvitationSession\"16@?<v@?@\"NSError\">24"
+ "v32@?0@\"NSNumber\"8@\"RPNearbyInvitationSession\"16^B24"
+ "v40@0:8@\"NSNumber\"16@\"RPNearbyInvitationDevice\"24@?<v@?@\"NSError\">32"
+ "waitingToConnect"
+ "wasTriggered"
- "\x05\x13\x14A\x13'"
- "\x14\x13!\x15\x122\x14\x11\xf0\xf0!\x1c"
- "530.1.1"
- "LargeFileBufferBytes: %u -> %llu\n"
- "LargeFileMaxTasks: %u -> %llu\n"
- "PairSetup completed client\n"
- "SmallFilesMaxTasks: %u -> %llu\n"
- "_prefLargeFileBufferBytes"
- "_prefLargeFileMaxTasks"
- "_prefSmallFilesMaxTasks"
- "sourceFileItemUsable"

```
