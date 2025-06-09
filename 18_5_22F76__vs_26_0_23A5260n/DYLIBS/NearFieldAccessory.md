## NearFieldAccessory

> `/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory`

```diff

-355.4.0.0.0
-  __TEXT.__text: 0xda94
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0x8e8
-  __TEXT.__const: 0x38
+360.33.0.0.0
+  __TEXT.__text: 0xde68
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_methlist: 0x908
+  __TEXT.__const: 0x98
   __TEXT.__cstring: 0x975
-  __TEXT.__oslogstring: 0x75e
-  __TEXT.__unwind_info: 0x2a0
+  __TEXT.__oslogstring: 0x7af
+  __TEXT.__unwind_info: 0x2b0
   __TEXT.__objc_classname: 0x16a
-  __TEXT.__objc_methname: 0xead
-  __TEXT.__objc_methtype: 0x6f5
-  __TEXT.__objc_stubs: 0xda0
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x4c0
+  __TEXT.__objc_methname: 0xf2f
+  __TEXT.__objc_methtype: 0x70b
+  __TEXT.__objc_stubs: 0xe60
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0x4e8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x580
+  __DATA_CONST.__objc_selrefs: 0x5b0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x210
+  __AUTH_CONST.__auth_got: 0x220
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x540
-  __AUTH_CONST.__objc_const: 0xe60
+  __AUTH_CONST.__objc_const: 0xe80
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_ivar: 0x70
   __DATA.__data: 0x480
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 103B4BEA-D494-32B8-A149-4E389F08E81E
-  Functions: 190
-  Symbols:   757
-  CStrings:  507
+  UUID: E7D9F855-D695-3D5D-98B9-364B36E331CD
+  Functions: 195
+  Symbols:   105
+  CStrings:  518
 
Symbols:
+ _OBJC_CLASS_$_NFTimer
+ __os_log_default
+ __os_log_fault_impl
+ _class_getName
- +[NFACTag supportsSecureCoding]
- +[NFAccessoryHardwareManager sharedHardwareManager]
- +[NFAccessoryReaderSession supportsSecureCoding]
- +[NFHardwareManagerAccessoryInterface interface]
- +[NFReaderSessionAccessoryCallbacks interface]
- +[NFReaderSessionAccessoryInterface interface]
- -[NFACTag .cxx_destruct]
- -[NFACTag IDm]
- -[NFACTag PMm]
- -[NFACTag SystemCode]
- -[NFACTag UID]
- -[NFACTag allSystemCodes]
- -[NFACTag applicationDataCoding]
- -[NFACTag applicationData]
- -[NFACTag asDictionary]
- -[NFACTag atqa]
- -[NFACTag description]
- -[NFACTag encodeWithCoder:]
- -[NFACTag historicalBytes]
- -[NFACTag initWithCoder:]
- -[NFACTag initWithInternalTag:]
- -[NFACTag isSilent]
- -[NFACTag ndefAvailability]
- -[NFACTag ndefContainerSize]
- -[NFACTag ndefMessageSize]
- -[NFACTag pupi]
- -[NFACTag sak]
- -[NFACTag selectedAID]
- -[NFACTag silentType]
- -[NFACTag tagID]
- -[NFACTag technology]
- -[NFACTag type]
- -[NFAccessoryHardwareManager .cxx_destruct]
- -[NFAccessoryHardwareManager _cleanupSessions]
- -[NFAccessoryHardwareManager _connectIfNeeded]
- -[NFAccessoryHardwareManager clearMultiTagState]
- -[NFAccessoryHardwareManager connect]
- -[NFAccessoryHardwareManager dealloc]
- -[NFAccessoryHardwareManager didInterruptXPCConnection:]
- -[NFAccessoryHardwareManager didInvalidateXPCConnection:]
- -[NFAccessoryHardwareManager disconnect]
- -[NFAccessoryHardwareManager enableLPCD:]
- -[NFAccessoryHardwareManager enableMultiTag:]
- -[NFAccessoryHardwareManager getDieId:]
- -[NFAccessoryHardwareManager getHwSupport:error:]
- -[NFAccessoryHardwareManager getInfo]
- -[NFAccessoryHardwareManager getLastDetectedTags:]
- -[NFAccessoryHardwareManager getMultiTagState:]
- -[NFAccessoryHardwareManager getPowerCounters:]
- -[NFAccessoryHardwareManager getRfSettings:]
- -[NFAccessoryHardwareManager init]
- -[NFAccessoryHardwareManager pushSignedRF:]
- -[NFAccessoryHardwareManager remoteObjectProxyWithErrorHandler:]
- -[NFAccessoryHardwareManager sessionDidEnd:]
- -[NFAccessoryHardwareManager shutdownAndLeaveHWEnabled:]
- -[NFAccessoryHardwareManager startReaderSession:]
- -[NFAccessoryHardwareManager synchronousRemoteObjectProxyWithErrorHandler:]
- -[NFAccessoryHardwareManager triggerDelayedWake:]
- -[NFAccessoryHardwareManager updateHWSupport:]
- -[NFAccessoryReaderSession .cxx_destruct]
- -[NFAccessoryReaderSession checkNdefSupport:andWrite:error:]
- -[NFAccessoryReaderSession checkPresence:]
- -[NFAccessoryReaderSession connectTag:error:]
- -[NFAccessoryReaderSession delegate]
- -[NFAccessoryReaderSession didDetectTags:]
- -[NFAccessoryReaderSession didEndUnexpectedly]
- -[NFAccessoryReaderSession didTerminate:]
- -[NFAccessoryReaderSession disconnectTag:]
- -[NFAccessoryReaderSession encodeWithCoder:]
- -[NFAccessoryReaderSession endSessionWithCompletion:]
- -[NFAccessoryReaderSession readNDEF:]
- -[NFAccessoryReaderSession readTypeIdentifier:]
- -[NFAccessoryReaderSession sendAccessoryProtocolCommand:outError:]
- -[NFAccessoryReaderSession sendAuthProtocolCommand:error:]
- -[NFAccessoryReaderSession setDelegate:]
- -[NFAccessoryReaderSession setTagDataRate:]
- -[NFAccessoryReaderSession startLpcdPolling:]
- -[NFAccessoryReaderSession startPolling:]
- -[NFAccessoryReaderSession startPollingForTechnology:error:]
- -[NFAccessoryReaderSession stopPolling:]
- -[NFAccessoryReaderSession transceive:error:]
- -[NFAccessoryReaderSession(InternalTest) enableContinuousWave:withFrequencySweep:]
- -[NFAccessorySession .cxx_destruct]
- -[NFAccessorySession _didEndSession]
- -[NFAccessorySession _didStartSession:]
- -[NFAccessorySession _endProxySession]
- -[NFAccessorySession callbackQueue]
- -[NFAccessorySession dealloc]
- -[NFAccessorySession didEndUnexpectedly]
- -[NFAccessorySession didEnd]
- -[NFAccessorySession didStartSession:]
- -[NFAccessorySession didStartSessionWithoutQueue:]
- -[NFAccessorySession endSessionWithCompletion:]
- -[NFAccessorySession init]
- -[NFAccessorySession isActive]
- -[NFAccessorySession isFirstInQueue]
- -[NFAccessorySession proxy]
- -[NFAccessorySession remoteObjectProxyWithErrorHandler:]
- -[NFAccessorySession resume]
- -[NFAccessorySession setDidEndCallback:]
- -[NFAccessorySession setDidStartCallback:]
- -[NFAccessorySession setIsFirstInQueue:]
- -[NFAccessorySession setProxy:]
- -[NFAccessorySession state]
- -[NFAccessorySession synchronousRemoteObjectProxyWithErrorHandler:]
- <redacted>
- _OBJC_CLASS_$_NFHardwareManagerAccessoryCallbacks
- _OBJC_CLASS_$_NFHardwareManagerAccessoryInterface
- _OBJC_CLASS_$_NFReaderSessionAccessoryCallbacks
- _OBJC_CLASS_$_NFReaderSessionAccessoryInterface
- _OBJC_IVAR_$_NFACTag._allSystemCodes
- _OBJC_IVAR_$_NFACTag._appData
- _OBJC_IVAR_$_NFACTag._atqa
- _OBJC_IVAR_$_NFACTag._description
- _OBJC_IVAR_$_NFACTag._historicalBytes
- _OBJC_IVAR_$_NFACTag._ndefAvailability
- _OBJC_IVAR_$_NFACTag._ndefContainerSize
- _OBJC_IVAR_$_NFACTag._ndefMessageSize
- _OBJC_IVAR_$_NFACTag._pmm
- _OBJC_IVAR_$_NFACTag._sak
- _OBJC_IVAR_$_NFACTag._silentType
- _OBJC_IVAR_$_NFACTag._tagID
- _OBJC_IVAR_$_NFACTag._technology
- _OBJC_IVAR_$_NFACTag._type
- _OBJC_IVAR_$_NFACTag._uid
- _OBJC_IVAR_$_NFAccessoryHardwareManager._connection
- _OBJC_IVAR_$_NFAccessoryHardwareManager._hwSupport
- _OBJC_IVAR_$_NFAccessoryHardwareManager._refCount
- _OBJC_IVAR_$_NFAccessoryHardwareManager._sessions
- _OBJC_IVAR_$_NFAccessoryReaderSession._delegate
- _OBJC_IVAR_$_NFAccessorySession._callbackQueue
- _OBJC_IVAR_$_NFAccessorySession._didEndCallback
- _OBJC_IVAR_$_NFAccessorySession._didStartCallback
- _OBJC_IVAR_$_NFAccessorySession._isCallbackQueueSuspended
- _OBJC_IVAR_$_NFAccessorySession._isFirstInQueue
- _OBJC_IVAR_$_NFAccessorySession._proxy
- _OBJC_IVAR_$_NFAccessorySession._state
- _OBJC_METACLASS_$_NFHardwareManagerAccessoryCallbacks
- _OBJC_METACLASS_$_NFHardwareManagerAccessoryInterface
- _OBJC_METACLASS_$_NFReaderSessionAccessoryCallbacks
- _OBJC_METACLASS_$_NFReaderSessionAccessoryInterface
- __MergedGlobals
- __OBJC_$_CLASS_METHODS_NFACTag
- __OBJC_$_CLASS_METHODS_NFAccessoryHardwareManager
- __OBJC_$_CLASS_METHODS_NFAccessoryReaderSession
- __OBJC_$_CLASS_PROP_LIST_NFACTag
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
- __OBJC_$_INSTANCE_METHODS_NFACTag
- __OBJC_$_INSTANCE_METHODS_NFAccessoryHardwareManager
- __OBJC_$_INSTANCE_METHODS_NFAccessoryReaderSession(InternalTest)
- __OBJC_$_INSTANCE_METHODS_NFAccessorySession
- __OBJC_$_INSTANCE_VARIABLES_NFACTag
- __OBJC_$_INSTANCE_VARIABLES_NFAccessoryHardwareManager
- __OBJC_$_INSTANCE_VARIABLES_NFAccessoryReaderSession
- __OBJC_$_INSTANCE_VARIABLES_NFAccessorySession
- __OBJC_$_PROP_LIST_NFACTag
- __OBJC_$_PROP_LIST_NFACTag.237
- __OBJC_$_PROP_LIST_NFAccessoryHardwareManager
- __OBJC_$_PROP_LIST_NFAccessoryReaderSession
- __OBJC_$_PROP_LIST_NFAccessorySession
- __OBJC_$_PROP_LIST_NSObject
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFACTag
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFAccessorySession
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFHardwareManagerAccessoryCallbacks
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFHardwareManagerAccessoryInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFReaderSessionAccessoryCallbacks
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFReaderSessionAccessoryInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFSessionAccessoryCallbackInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFSessionAccessoryInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCConnectionDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_NFACTag
- __OBJC_$_PROTOCOL_METHOD_TYPES_NFAccessorySession
- __OBJC_$_PROTOCOL_METHOD_TYPES_NFHardwareManagerAccessoryCallbacks
- __OBJC_$_PROTOCOL_METHOD_TYPES_NFHardwareManagerAccessoryInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_NFReaderSessionAccessoryCallbacks
- __OBJC_$_PROTOCOL_METHOD_TYPES_NFReaderSessionAccessoryInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_NFSessionAccessoryCallbackInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_NFSessionAccessoryInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCConnectionDelegate
- __OBJC_$_PROTOCOL_REFS_NFACTag
- __OBJC_$_PROTOCOL_REFS_NFAccessorySession
- __OBJC_$_PROTOCOL_REFS_NFHardwareManagerAccessoryCallbacks
- __OBJC_$_PROTOCOL_REFS_NFHardwareManagerAccessoryInterface
- __OBJC_$_PROTOCOL_REFS_NFReaderSessionAccessoryCallbacks
- __OBJC_$_PROTOCOL_REFS_NFReaderSessionAccessoryInterface
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding
- __OBJC_$_PROTOCOL_REFS_NSXPCConnectionDelegate
- __OBJC_CLASS_PROTOCOLS_$_NFACTag
- __OBJC_CLASS_PROTOCOLS_$_NFAccessoryHardwareManager
- __OBJC_CLASS_PROTOCOLS_$_NFAccessoryReaderSession
- __OBJC_CLASS_PROTOCOLS_$_NFAccessorySession
- __OBJC_CLASS_RO_$_NFACTag
- __OBJC_CLASS_RO_$_NFAccessoryHardwareManager
- __OBJC_CLASS_RO_$_NFAccessoryReaderSession
- __OBJC_CLASS_RO_$_NFAccessorySession
- __OBJC_CLASS_RO_$_NFHardwareManagerAccessoryCallbacks
- __OBJC_CLASS_RO_$_NFHardwareManagerAccessoryInterface
- __OBJC_CLASS_RO_$_NFReaderSessionAccessoryCallbacks
- __OBJC_CLASS_RO_$_NFReaderSessionAccessoryInterface
- __OBJC_LABEL_PROTOCOL_$_NFACTag
- __OBJC_LABEL_PROTOCOL_$_NFAccessorySession
- __OBJC_LABEL_PROTOCOL_$_NFHardwareManagerAccessoryCallbacks
- __OBJC_LABEL_PROTOCOL_$_NFHardwareManagerAccessoryInterface
- __OBJC_LABEL_PROTOCOL_$_NFReaderSessionAccessoryCallbacks
- __OBJC_LABEL_PROTOCOL_$_NFReaderSessionAccessoryInterface
- __OBJC_LABEL_PROTOCOL_$_NFSessionAccessoryCallbackInterface
- __OBJC_LABEL_PROTOCOL_$_NFSessionAccessoryInterface
- __OBJC_LABEL_PROTOCOL_$_NSCoding
- __OBJC_LABEL_PROTOCOL_$_NSObject
- __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
- __OBJC_LABEL_PROTOCOL_$_NSXPCConnectionDelegate
- __OBJC_METACLASS_RO_$_NFACTag
- __OBJC_METACLASS_RO_$_NFAccessoryHardwareManager
- __OBJC_METACLASS_RO_$_NFAccessoryReaderSession
- __OBJC_METACLASS_RO_$_NFAccessorySession
- __OBJC_METACLASS_RO_$_NFHardwareManagerAccessoryCallbacks
- __OBJC_METACLASS_RO_$_NFHardwareManagerAccessoryInterface
- __OBJC_METACLASS_RO_$_NFReaderSessionAccessoryCallbacks
- __OBJC_METACLASS_RO_$_NFReaderSessionAccessoryInterface
- __OBJC_PROTOCOL_$_NFACTag
- __OBJC_PROTOCOL_$_NFAccessorySession
- __OBJC_PROTOCOL_$_NFHardwareManagerAccessoryCallbacks
- __OBJC_PROTOCOL_$_NFHardwareManagerAccessoryInterface
- __OBJC_PROTOCOL_$_NFReaderSessionAccessoryCallbacks
- __OBJC_PROTOCOL_$_NFReaderSessionAccessoryInterface
- __OBJC_PROTOCOL_$_NFSessionAccessoryCallbackInterface
- __OBJC_PROTOCOL_$_NFSessionAccessoryInterface
- __OBJC_PROTOCOL_$_NSCoding
- __OBJC_PROTOCOL_$_NSObject
- __OBJC_PROTOCOL_$_NSSecureCoding
- __OBJC_PROTOCOL_$_NSXPCConnectionDelegate
- __OBJC_PROTOCOL_REFERENCE_$_NFHardwareManagerAccessoryCallbacks
- __OBJC_PROTOCOL_REFERENCE_$_NFHardwareManagerAccessoryInterface
- __OBJC_PROTOCOL_REFERENCE_$_NFReaderSessionAccessoryCallbacks
- __OBJC_PROTOCOL_REFERENCE_$_NFReaderSessionAccessoryInterface
- ___37-[NFAccessoryHardwareManager getInfo]_block_invoke
- ___37-[NFAccessoryHardwareManager getInfo]_block_invoke.98
- ___37-[NFAccessoryReaderSession readNDEF:]_block_invoke
- ___37-[NFAccessoryReaderSession readNDEF:]_block_invoke.22
- ___38-[NFAccessorySession _endProxySession]_block_invoke
- ___38-[NFAccessorySession _endProxySession]_block_invoke.14
- ___38-[NFAccessorySession didStartSession:]_block_invoke
- ___39-[NFAccessoryHardwareManager getDieId:]_block_invoke
- ___39-[NFAccessoryHardwareManager getDieId:]_block_invoke.92
- ___40-[NFAccessoryReaderSession stopPolling:]_block_invoke
- ___40-[NFAccessoryReaderSession stopPolling:]_block_invoke.16
- ___40-[NFAccessorySession setDidEndCallback:]_block_invoke
- ___41-[NFAccessoryHardwareManager enableLPCD:]_block_invoke
- ___41-[NFAccessoryHardwareManager enableLPCD:]_block_invoke.100
- ___41-[NFAccessoryReaderSession startPolling:]_block_invoke
- ___41-[NFAccessoryReaderSession startPolling:]_block_invoke.14
- ___42-[NFAccessoryReaderSession checkPresence:]_block_invoke
- ___42-[NFAccessoryReaderSession checkPresence:]_block_invoke.20
- ___42-[NFAccessoryReaderSession didDetectTags:]_block_invoke
- ___42-[NFAccessoryReaderSession disconnectTag:]_block_invoke
- ___42-[NFAccessoryReaderSession disconnectTag:]_block_invoke.19
- ___42-[NFAccessorySession setDidStartCallback:]_block_invoke
- ___43-[NFAccessoryHardwareManager pushSignedRF:]_block_invoke
- ___43-[NFAccessoryHardwareManager pushSignedRF:]_block_invoke.110
- ___43-[NFAccessoryReaderSession setTagDataRate:]_block_invoke
- ___43-[NFAccessoryReaderSession setTagDataRate:]_block_invoke.30
- ___44-[NFAccessoryHardwareManager getRfSettings:]_block_invoke
- ___44-[NFAccessoryHardwareManager getRfSettings:]_block_invoke.97
- ___45-[NFAccessoryHardwareManager enableMultiTag:]_block_invoke
- ___45-[NFAccessoryHardwareManager enableMultiTag:]_block_invoke.101
- ___45-[NFAccessoryReaderSession connectTag:error:]_block_invoke
- ___45-[NFAccessoryReaderSession connectTag:error:]_block_invoke.18
- ___45-[NFAccessoryReaderSession startLpcdPolling:]_block_invoke
- ___45-[NFAccessoryReaderSession startLpcdPolling:]_block_invoke.13
- ___45-[NFAccessoryReaderSession transceive:error:]_block_invoke
- ___45-[NFAccessoryReaderSession transceive:error:]_block_invoke.26
- ___46-[NFAccessoryHardwareManager _cleanupSessions]_block_invoke
- ___46-[NFAccessoryHardwareManager _connectIfNeeded]_block_invoke
- ___46-[NFAccessoryHardwareManager _connectIfNeeded]_block_invoke.56
- ___46-[NFAccessoryHardwareManager _connectIfNeeded]_block_invoke.58
- ___46-[NFAccessoryHardwareManager _connectIfNeeded]_block_invoke_2
- ___46-[NFAccessoryHardwareManager _connectIfNeeded]_block_invoke_2.60
- ___46-[NFAccessoryHardwareManager updateHWSupport:]_block_invoke
- ___46-[NFAccessoryHardwareManager updateHWSupport:]_block_invoke.128
- ___46-[NFAccessoryHardwareManager updateHWSupport:]_block_invoke.129
- ___46-[NFAccessoryReaderSession didEndUnexpectedly]_block_invoke
- ___47-[NFAccessoryHardwareManager getMultiTagState:]_block_invoke
- ___47-[NFAccessoryHardwareManager getMultiTagState:]_block_invoke.106
- ___47-[NFAccessoryHardwareManager getPowerCounters:]_block_invoke
- ___47-[NFAccessoryHardwareManager getPowerCounters:]_block_invoke.95
- ___47-[NFAccessoryReaderSession readTypeIdentifier:]_block_invoke
- ___47-[NFAccessoryReaderSession readTypeIdentifier:]_block_invoke.29
- ___47-[NFAccessorySession endSessionWithCompletion:]_block_invoke
- ___48+[NFHardwareManagerAccessoryInterface interface]_block_invoke
- ___48-[NFAccessoryHardwareManager clearMultiTagState]_block_invoke
- ___48-[NFAccessoryHardwareManager clearMultiTagState]_block_invoke.108
- ___49-[NFAccessoryHardwareManager startReaderSession:]_block_invoke
- ___49-[NFAccessoryHardwareManager startReaderSession:]_block_invoke.89
- ___49-[NFAccessoryHardwareManager startReaderSession:]_block_invoke_2
- ___49-[NFAccessoryHardwareManager triggerDelayedWake:]_block_invoke
- ___49-[NFAccessoryHardwareManager triggerDelayedWake:]_block_invoke.109
- ___50-[NFAccessoryHardwareManager getLastDetectedTags:]_block_invoke
- ___50-[NFAccessoryHardwareManager getLastDetectedTags:]_block_invoke.102
- ___51+[NFAccessoryHardwareManager sharedHardwareManager]_block_invoke
- ___56-[NFAccessoryHardwareManager didInterruptXPCConnection:]_block_invoke
- ___56-[NFAccessoryHardwareManager shutdownAndLeaveHWEnabled:]_block_invoke
- ___56-[NFAccessoryHardwareManager shutdownAndLeaveHWEnabled:]_block_invoke.111
- ___56-[NFAccessorySession remoteObjectProxyWithErrorHandler:]_block_invoke
- ___60-[NFAccessoryReaderSession checkNdefSupport:andWrite:error:]_block_invoke
- ___60-[NFAccessoryReaderSession checkNdefSupport:andWrite:error:]_block_invoke.24
- ___60-[NFAccessoryReaderSession startPollingForTechnology:error:]_block_invoke
- ___60-[NFAccessoryReaderSession startPollingForTechnology:error:]_block_invoke.15
- ___64-[NFAccessoryHardwareManager remoteObjectProxyWithErrorHandler:]_block_invoke
- ___66-[NFAccessoryReaderSession sendAccessoryProtocolCommand:outError:]_block_invoke
- ___66-[NFAccessoryReaderSession sendAccessoryProtocolCommand:outError:]_block_invoke.28
- ___67-[NFAccessorySession synchronousRemoteObjectProxyWithErrorHandler:]_block_invoke
- ___75-[NFAccessoryHardwareManager synchronousRemoteObjectProxyWithErrorHandler:]_block_invoke
- ___82-[NFAccessoryReaderSession(InternalTest) enableContinuousWave:withFrequencySweep:]_block_invoke
- ___82-[NFAccessoryReaderSession(InternalTest) enableContinuousWave:withFrequencySweep:]_block_invoke.2
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___block_descriptor_32_e12_v24?08^B16l
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_40_8_32bs_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_8_32r_e17_v16?0"NSError"8lr32l8
- ___block_descriptor_40_8_32s_e5_v8?0ls32l8
- ___block_descriptor_40_8_32s_e8_v12?0I8ls32l8
- ___block_descriptor_40_8_32s_e8_v16?08ls32l8
- ___block_descriptor_40_8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_8_32r40r_e17_v16?0"NSError"8lr32l8r40l8
- ___block_descriptor_48_8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
- ___block_descriptor_48_8_32r40r_e28_v24?0"NSData"8"NSError"16lr32l8r40l8
- ___block_descriptor_48_8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
- ___block_descriptor_48_8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_48_8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_48_8_32s_e5_v8?0ls32l8
- ___block_descriptor_56_8_32r40r48r_e23_v24?0B8B12"NSError"16lr32l8r40l8r48l8
- ___block_descriptor_56_8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
- ___block_descriptor_56_8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
- ___block_descriptor_56_8_32s40r_e34_v24?0"NSDictionary"8"NSError"16ls32l8r40l8
- ___block_descriptor_56_8_32s40r_e65_v24?0"NSObject<NFReaderSessionAccessoryInterface>"8"NSError"16ls32l8r40l8
- ___block_descriptor_64_8_32s40r48r_e17_v16?0"NSError"8lr40l8s32l8r48l8
- ___block_descriptor_64_8_32s40r48r_e28_v24?0"NSData"8"NSError"16ls32l8r40l8r48l8
- ___block_descriptor_64_8_32s40r48r_e29_v24?0"NSArray"8"NSError"16ls32l8r40l8r48l8
- ___block_descriptor_64_8_32s40r48r_e34_v24?0"NSError"8"NSDictionary"16ls32l8r40l8r48l8
- ___block_descriptor_72_8_32s40r48r56r_e17_v16?0"NSError"8lr40l8s32l8r48l8r56l8
- ___block_literal_global
- ___block_literal_global.3
- ___block_literal_global.73
- _objc_msgSend$NF_asHexString
- _objc_msgSend$PMm
- _objc_msgSend$UID
- _objc_msgSend$_cleanupSessions
- _objc_msgSend$_connectIfNeeded
- _objc_msgSend$_didEndSession
- _objc_msgSend$_didStartSession:
- _objc_msgSend$_endProxySession
- _objc_msgSend$_setQueue:
- _objc_msgSend$addObject:
- _objc_msgSend$asDictionary
- _objc_msgSend$atqa
- _objc_msgSend$bytes
- _objc_msgSend$checkNdefSupport:
- _objc_msgSend$checkPresence:
- _objc_msgSend$clearMultiTagState:
- _objc_msgSend$coder:decodeArrayOfClass:forKey:
- _objc_msgSend$connect
- _objc_msgSend$connectTag:callback:
- _objc_msgSend$copy
- _objc_msgSend$count
- _objc_msgSend$countByEnumeratingWithState:objects:count:
- _objc_msgSend$decodeInt32ForKey:
- _objc_msgSend$decodeIntForKey:
- _objc_msgSend$decodeIntegerForKey:
- _objc_msgSend$decodeObjectOfClass:forKey:
- _objc_msgSend$delegate
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$didEndUnexpectedly
- _objc_msgSend$didStartSession:
- _objc_msgSend$didStartSessionWithoutQueue:
- _objc_msgSend$disconnectTag:
- _objc_msgSend$enableContinuousWave:withFrequencySweep:callback:
- _objc_msgSend$enableLPCD:callback:
- _objc_msgSend$enableMultiTag:callback:
- _objc_msgSend$encodeInt32:forKey:
- _objc_msgSend$encodeInt:forKey:
- _objc_msgSend$encodeInteger:forKey:
- _objc_msgSend$encodeObject:forKey:
- _objc_msgSend$endSession:
- _objc_msgSend$endSessionWithCompletion:
- _objc_msgSend$enumerateObjectsUsingBlock:
- _objc_msgSend$getDieId:
- _objc_msgSend$getInfo:
- _objc_msgSend$getLastDetectedTags:
- _objc_msgSend$getMultiTagState:
- _objc_msgSend$getPowerCounters:
- _objc_msgSend$getRfSettings:
- _objc_msgSend$historicalBytes
- _objc_msgSend$initWithDictionary:
- _objc_msgSend$initWithDomain:code:userInfo:
- _objc_msgSend$initWithFormat:
- _objc_msgSend$initWithInternalTag:
- _objc_msgSend$initWithMachServiceName:options:
- _objc_msgSend$initWithObjects:
- _objc_msgSend$interfaceWithProtocol:
- _objc_msgSend$invalidate
- _objc_msgSend$isHWSupported:
- _objc_msgSend$ndefAvailability
- _objc_msgSend$ndefContainerSize
- _objc_msgSend$ndefMessageSize
- _objc_msgSend$numberWithUnsignedChar:
- _objc_msgSend$numberWithUnsignedInt:
- _objc_msgSend$numberWithUnsignedLong:
- _objc_msgSend$processInfo
- _objc_msgSend$processName
- _objc_msgSend$proxy
- _objc_msgSend$pushSignedRF:callback:
- _objc_msgSend$queueReaderSession:callback:
- _objc_msgSend$readRawNdef:
- _objc_msgSend$readTypeIdentifier:
- _objc_msgSend$readerSession:didDetectTags:
- _objc_msgSend$readerSessionDidEndUnexpectedly:
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
- _objc_msgSend$removeAllObjects
- _objc_msgSend$removeObject:
- _objc_msgSend$resume
- _objc_msgSend$sak
- _objc_msgSend$sendAccessoryProtocolCommand:outError:
- _objc_msgSend$sessionDidEnd:
- _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
- _objc_msgSend$setClientName:
- _objc_msgSend$setDelegate:
- _objc_msgSend$setDidEndCallback:
- _objc_msgSend$setDidStartCallback:
- _objc_msgSend$setExportedInterface:
- _objc_msgSend$setExportedObject:
- _objc_msgSend$setInterface:forSelector:argumentIndex:ofReply:
- _objc_msgSend$setInterruptionHandler:
- _objc_msgSend$setInvalidationHandler:
- _objc_msgSend$setIsFirstInQueue:
- _objc_msgSend$setObject:forKeyedSubscript:
- _objc_msgSend$setProxy:
- _objc_msgSend$setRemoteObjectInterface:
- _objc_msgSend$setTagDataRate:callback:
- _objc_msgSend$shutdownAndLeaveHWEnabled:callback:
- _objc_msgSend$silentType
- _objc_msgSend$startPollingForTechnology:lpcd:callback:
- _objc_msgSend$stopPolling:
- _objc_msgSend$stringWithUTF8String:
- _objc_msgSend$subdataWithRange:
- _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- _objc_msgSend$tagID
- _objc_msgSend$technology
- _objc_msgSend$transceive:callback:
- _objc_msgSend$transceiveAccessoryCommand:callback:
- _objc_msgSend$triggerDelayedWake:callback:
- _objc_msgSend$type
- _objc_msgSend$updateHWSupport:
CStrings:
+ "%s is still active after %lf seconds"
+ "@\"NFTimer\""
+ "_sessionTimeout"
+ "_setSessionTimeLimit:"
+ "com.apple.nfcd.accessorySession.activeTimer"
+ "didTimeout"
+ "initSleepTimerWithCallback:queue:"
+ "readerSessionDidTimeout:"
+ "startTimer:"
+ "stopTimer"
+ "v24@0:8d16"

```
