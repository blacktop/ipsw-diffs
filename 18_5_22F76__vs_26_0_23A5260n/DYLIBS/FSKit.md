## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-531.120.18.0.2
-  __TEXT.__text: 0x3c95c
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x4324
-  __TEXT.__const: 0x370
-  __TEXT.__gcc_except_tab: 0xf00
-  __TEXT.__cstring: 0x3e7f
-  __TEXT.__oslogstring: 0x2cc5
+737.0.2.0.1
+  __TEXT.__text: 0x3fb70
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x49d4
+  __TEXT.__const: 0x390
+  __TEXT.__gcc_except_tab: 0xdd0
+  __TEXT.__cstring: 0x420f
+  __TEXT.__oslogstring: 0x2ec1
   __TEXT.__swift5_typeref: 0x1d1
   __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_reflstr: 0x16

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x11c8
+  __TEXT.__unwind_info: 0x12f0
   __TEXT.__eh_frame: 0x160
-  __TEXT.__objc_classname: 0x825
-  __TEXT.__objc_methname: 0x9376
-  __TEXT.__objc_methtype: 0x325e
-  __TEXT.__objc_stubs: 0x5400
-  __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0x12f8
-  __DATA_CONST.__objc_classlist: 0x208
+  __TEXT.__objc_classname: 0x8e7
+  __TEXT.__objc_methname: 0x99e0
+  __TEXT.__objc_methtype: 0x32db
+  __TEXT.__objc_stubs: 0x56c0
+  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__const: 0x1358
+  __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22a8
-  __DATA_CONST.__objc_protorefs: 0xe8
-  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_selrefs: 0x2480
+  __DATA_CONST.__objc_protorefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x668
-  __AUTH_CONST.__const: 0x5a8
-  __AUTH_CONST.__cfstring: 0x1e80
-  __AUTH_CONST.__objc_const: 0x7018
+  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__const: 0x4e8
+  __AUTH_CONST.__cfstring: 0x22c0
+  __AUTH_CONST.__objc_const: 0x7e70
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1158
+  __AUTH.__objc_data: 0x1040
   __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x3f4
-  __DATA.__data: 0xf68
+  __DATA.__objc_ivar: 0x498
+  __DATA.__data: 0xf48
   __DATA.__bss: 0x320
-  __DATA_DIRTY.__objc_data: 0x438
+  __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x38
+  __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 522DF87F-AF99-365F-AD4E-A59340E8D924
-  Functions: 1820
-  Symbols:   5846
-  CStrings:  3069
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: F8A62C69-C660-3BF2-A3D8-C9DDBED76BB8
+  Functions: 1985
+  Symbols:   6330
+  CStrings:  3307
 
Symbols:
+ +[FSBlockDeviceResource getDeviceName:]
+ +[FSBlockDeviceResource getDeviceName:].cold.1
+ +[FSBlockDeviceResource getDeviceName:].cold.2
+ +[FSBlockDeviceResource getDeviceName:].cold.3
+ +[FSOpenSessionParameters supportsSecureCoding]
+ +[FSPathURLResource supportsSecureCoding]
+ +[FSPathURLResource(Private) resourceWithURL:]
+ +[FSPathURLResource(Private) secureResourceWithURL:readonly:]
+ +[FSServerEnumerateSharesParameters supportsSecureCoding]
+ +[FSServerInfo supportsSecureCoding]
+ +[FSServerSessionInfo supportsSecureCoding]
+ +[FSServerShareInfo supportsSecureCoding]
+ +[FSServerURLParameters supportsSecureCoding]
+ -[FSBlockDeviceBufferResource asynchronousMetadataFlushWithError:]
+ -[FSBlockDeviceBufferResource delayedMetadataWriteFrom:startingAt:length:error:]
+ -[FSBlockDeviceBufferResource metadataClear:withDelayedWrites:error:]
+ -[FSBlockDeviceBufferResource metadataFlushWithError:]
+ -[FSBlockDeviceBufferResource metadataPurge:error:]
+ -[FSBlockDeviceBufferResource metadataReadInto:startingAt:length:error:]
+ -[FSBlockDeviceBufferResource metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:error:]
+ -[FSBlockDeviceBufferResource metadataWriteFrom:startingAt:length:error:]
+ -[FSBlockDeviceResource getProgressURLKey]
+ -[FSBlockDeviceResource(Project) terminateLocked]
+ -[FSClient(Private) doneFSCKWithTask:]
+ -[FSClient(Private) doneFSCKWithTask:].cold.1
+ -[FSClient(Private) startFSCKWithDevice:volumes:error:]
+ -[FSClient(Private) startFSCKWithDevice:volumes:error:].cold.1
+ -[FSConnectShareTask .cxx_destruct]
+ -[FSConnectShareTask didCompleteWithVolume:]
+ -[FSConnectShareTask result]
+ -[FSConnectShareTask setResult:]
+ -[FSEnumeratedSharePacker packShareWithName:info:]
+ -[FSGenericURLResource initWithURL:]
+ -[FSGenericURLResource url]
+ -[FSItemAttributes hasMinimalRequiredAttributes]
+ -[FSItemAttributes hasMinimalRequiredAttributes].cold.1
+ -[FSMessageConnection(Private) localizedMessage:table:bundle:arguments:]
+ -[FSMessageConnection(Private) localizedMessage:table:bundle:arguments:].cold.1
+ -[FSModuleExtension(Project) fskitdIsClient:]
+ -[FSModuleExtension(Project) fskitdIsClient:].cold.1
+ -[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]
+ -[FSModuleHost(Project) addBundleToEnableModules:].cold.1
+ -[FSModuleHost(Project) isValidModuleIdentifier:withError:]
+ -[FSModuleHost(Project) removeBundleFromEnabledModules:].cold.1
+ -[FSModuleIdentity applicationGroup]
+ -[FSModuleVolume(Project) getAndRemoveItemForFH:].cold.1
+ -[FSMutableFileDataBuffer .cxx_destruct]
+ -[FSMutableFileDataBuffer proxyOfBuffer]
+ -[FSMutableFileDataBuffer setProxyOfBuffer:]
+ -[FSMutableFileDataBuffer(Project) initProxyFrom:]
+ -[FSOpenSessionParameters .cxx_destruct]
+ -[FSOpenSessionParameters authenticationInfo]
+ -[FSOpenSessionParameters classForCoder]
+ -[FSOpenSessionParameters copyWithZone:]
+ -[FSOpenSessionParameters encodeWithCoder:]
+ -[FSOpenSessionParameters initWithCoder:]
+ -[FSOpenSessionParameters openFlags]
+ -[FSOpenSessionParameters setAuthenticationInfo:]
+ -[FSOpenSessionParameters setOpenFlags:]
+ -[FSOpenSessionParameters setUiOption:]
+ -[FSOpenSessionParameters uiOption]
+ -[FSPathURLResource .cxx_destruct]
+ -[FSPathURLResource URL]
+ -[FSPathURLResource classForCoder]
+ -[FSPathURLResource encodeWithCoder:]
+ -[FSPathURLResource getResourceID]
+ -[FSPathURLResource initWithCoder:]
+ -[FSPathURLResource initWithURL:writable:]
+ -[FSPathURLResource isEqual:]
+ -[FSPathURLResource isWritable]
+ -[FSPathURLResource kind]
+ -[FSPathURLResource makeProxy]
+ -[FSPathURLResource setUrlWrapper:]
+ -[FSPathURLResource urlWrapper]
+ -[FSPathURLResource url]
+ -[FSPathURLResource(Private) initAsSecureURL:readOnly:]
+ -[FSPathURLResource(Private) initAsSecureURL:writable:]
+ -[FSPathURLResource(Private) initWithURL:readOnly:]
+ -[FSResource(Private) getProgressURLKey]
+ -[FSServerEnumerateSharesParameters .cxx_destruct]
+ -[FSServerEnumerateSharesParameters authenticationInfo]
+ -[FSServerEnumerateSharesParameters classForCoder]
+ -[FSServerEnumerateSharesParameters copyWithZone:]
+ -[FSServerEnumerateSharesParameters encodeWithCoder:]
+ -[FSServerEnumerateSharesParameters initWithCoder:]
+ -[FSServerEnumerateSharesParameters setAuthenticationInfo:]
+ -[FSServerInfo .cxx_destruct]
+ -[FSServerInfo authenticationInfo]
+ -[FSServerInfo classForCoder]
+ -[FSServerInfo copyWithZone:]
+ -[FSServerInfo displayName]
+ -[FSServerInfo encodeWithCoder:]
+ -[FSServerInfo flags]
+ -[FSServerInfo initWithCoder:]
+ -[FSServerInfo machineType]
+ -[FSServerInfo proxyServerName]
+ -[FSServerInfo proxyServerRealm]
+ -[FSServerInfo serverOS]
+ -[FSServerInfo setAuthenticationInfo:]
+ -[FSServerInfo setDisplayName:]
+ -[FSServerInfo setFlags:]
+ -[FSServerInfo setMachineType:]
+ -[FSServerInfo setProxyServerName:]
+ -[FSServerInfo setProxyServerRealm:]
+ -[FSServerInfo setServerOS:]
+ -[FSServerInfo setSupportedMechTypes:]
+ -[FSServerInfo supportedMechTypes]
+ -[FSServerInfoTask .cxx_destruct]
+ -[FSServerInfoTask didCompleteWithServerInfo:]
+ -[FSServerInfoTask result]
+ -[FSServerInfoTask setResult:]
+ -[FSServerSessionInfo .cxx_destruct]
+ -[FSServerSessionInfo classForCoder]
+ -[FSServerSessionInfo connectedByUser]
+ -[FSServerSessionInfo copyWithZone:]
+ -[FSServerSessionInfo encodeWithCoder:]
+ -[FSServerSessionInfo howConnected]
+ -[FSServerSessionInfo initWithCoder:]
+ -[FSServerSessionInfo setConnectedByUser:]
+ -[FSServerSessionInfo setHowConnected:]
+ -[FSServerSessionInfoTask .cxx_destruct]
+ -[FSServerSessionInfoTask didCompleteWithServerSessionInfo:]
+ -[FSServerSessionInfoTask result]
+ -[FSServerSessionInfoTask setResult:]
+ -[FSServerShareInfo .cxx_destruct]
+ -[FSServerShareInfo additionalInfo]
+ -[FSServerShareInfo classForCoder]
+ -[FSServerShareInfo connectedByUser]
+ -[FSServerShareInfo copyWithZone:]
+ -[FSServerShareInfo displayName]
+ -[FSServerShareInfo encodeWithCoder:]
+ -[FSServerShareInfo hasPassword]
+ -[FSServerShareInfo howConnected]
+ -[FSServerShareInfo initWithCoder:]
+ -[FSServerShareInfo isAlreadyConnected]
+ -[FSServerShareInfo isHidden]
+ -[FSServerShareInfo isPrinterShare]
+ -[FSServerShareInfo setAdditionalInfo:]
+ -[FSServerShareInfo setAlreadyConnected:]
+ -[FSServerShareInfo setConnectedByUser:]
+ -[FSServerShareInfo setDisplayName:]
+ -[FSServerShareInfo setHasPassword:]
+ -[FSServerShareInfo setHidden:]
+ -[FSServerShareInfo setHowConnected:]
+ -[FSServerShareInfo setPrinterShare:]
+ -[FSServerURLParameters .cxx_destruct]
+ -[FSServerURLParameters classForCoder]
+ -[FSServerURLParameters copyWithZone:]
+ -[FSServerURLParameters encodeWithCoder:]
+ -[FSServerURLParameters extras]
+ -[FSServerURLParameters host]
+ -[FSServerURLParameters initWithCoder:]
+ -[FSServerURLParameters options]
+ -[FSServerURLParameters password]
+ -[FSServerURLParameters path]
+ -[FSServerURLParameters port]
+ -[FSServerURLParameters scheme]
+ -[FSServerURLParameters setExtras:]
+ -[FSServerURLParameters setHost:]
+ -[FSServerURLParameters setOptions:]
+ -[FSServerURLParameters setPassword:]
+ -[FSServerURLParameters setPath:]
+ -[FSServerURLParameters setPort:]
+ -[FSServerURLParameters setScheme:]
+ -[FSServerURLParameters setUser:]
+ -[FSServerURLParameters user]
+ -[FSTask cancellationHandler]
+ -[FSTask setCancellationHandler:]
+ -[FSTask(Private) localizedMessage:table:bundle:arguments:]
+ -[FSTask(Project) hasCancellationHandler]
+ -[FSTaskDescription setTaskHasCancellationHandler:]
+ -[FSTaskDescription taskHasCancellationHandler]
+ -[FSTaskDescription(Management) setTaskHasCancellationHandler:]
+ -[FSTaskMessageSTDIOWithProgress .cxx_destruct]
+ -[FSTaskMessageSTDIOWithProgress completed:replyHandler:]
+ -[FSTaskMessageSTDIOWithProgress completedError]
+ -[FSTaskMessageSTDIOWithProgress dealloc]
+ -[FSTaskMessageSTDIOWithProgress dispatch_group]
+ -[FSTaskMessageSTDIOWithProgress drawTwiddleBar]
+ -[FSTaskMessageSTDIOWithProgress fillProgressBar:]
+ -[FSTaskMessageSTDIOWithProgress hideProgressLocked]
+ -[FSTaskMessageSTDIOWithProgress hideProgress]
+ -[FSTaskMessageSTDIOWithProgress init]
+ -[FSTaskMessageSTDIOWithProgress logMessage:]
+ -[FSTaskMessageSTDIOWithProgress observeValueForKeyPath:ofObject:change:context:]
+ -[FSTaskMessageSTDIOWithProgress printAboveProgress:]
+ -[FSTaskMessageSTDIOWithProgress progressHasShown]
+ -[FSTaskMessageSTDIOWithProgress progressShowing]
+ -[FSTaskMessageSTDIOWithProgress progress]
+ -[FSTaskMessageSTDIOWithProgress prompt:replyHandler:]
+ -[FSTaskMessageSTDIOWithProgress promptTrueFalse:replyHandler:]
+ -[FSTaskMessageSTDIOWithProgress setCompletedError:]
+ -[FSTaskMessageSTDIOWithProgress setDispatch_group:]
+ -[FSTaskMessageSTDIOWithProgress setProgress:]
+ -[FSTaskMessageSTDIOWithProgress setProgressHasShown:]
+ -[FSTaskMessageSTDIOWithProgress setProgressShowing:]
+ -[FSTaskMessageSTDIOWithProgress setTwiddleState:]
+ -[FSTaskMessageSTDIOWithProgress showProgressLocked]
+ -[FSTaskMessageSTDIOWithProgress showProgress]
+ -[FSTaskMessageSTDIOWithProgress twiddleState]
+ -[FSTaskOptions(Private) initWithOptions:]
+ -[FSVolumeConnector getFreeSpaceInVolumeWithReplyHandler:]
+ -[FSVolumeConnector getIOItemAttributesSubsetData:replyHandler:]
+ -[FSVolumeConnector otherAttributeOf:named:requestID:replyHandler:].cold.3
+ -[FSVolumeConnector otherAttributeOf:named:requestID:replyHandler:].cold.4
+ -[FSVolumeConnector workQueue]
+ -[FSVolumeDescription copyWithZone:]
+ -[FSVolumeDescription hash]
+ -[FSWorkQueue concurrency]
+ -[FSWorkQueue didInitQueues]
+ -[FSWorkQueue domain]
+ -[FSWorkQueue initQueues]
+ -[FSWorkQueue setConcurrency:]
+ -[FSWorkQueue setDidInitQueues:]
+ -[FSWorkQueue setDomain:]
+ -[NSArray(FSKitAdditions) fs_all_of:]
+ -[NSArray(FSKitAdditions) fs_any_of:]
+ GCC_except_table101
+ GCC_except_table105
+ GCC_except_table15
+ GCC_except_table22
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table36
+ GCC_except_table55
+ GCC_except_table6
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table69
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table86
+ _FSKitCheckContainerStart
+ _FSKitCheckContainerStart.cold.1
+ _FSKitCheckContainerStart.cold.2
+ _FSKitCheckContainerStart.cold.3
+ _FSKitCheckDone
+ _FSKitCheckDone.cold.1
+ _FSKitCheckDone.cold.2
+ _FSKitCheckDone.cold.3
+ _FSKitCheckStart
+ _FSKitCheckStart.cold.1
+ _FSKitCheckUpdate
+ _FSKitCheckUpdate.cold.1
+ _FSModuleIdentityAttributeSupportedSchemes
+ _FSTaskStateCanceled
+ _NSProgressFileURLKey
+ _OBJC_CLASS_$_FSConnectShareTask
+ _OBJC_CLASS_$_FSEnumeratedSharePacker
+ _OBJC_CLASS_$_FSOpenSessionParameters
+ _OBJC_CLASS_$_FSServerEnumerateSharesParameters
+ _OBJC_CLASS_$_FSServerInfo
+ _OBJC_CLASS_$_FSServerInfoTask
+ _OBJC_CLASS_$_FSServerSessionInfo
+ _OBJC_CLASS_$_FSServerSessionInfoTask
+ _OBJC_CLASS_$_FSServerShareInfo
+ _OBJC_CLASS_$_FSServerURLParameters
+ _OBJC_CLASS_$_FSTaskMessageSTDIOWithProgress
+ _OBJC_IVAR_$_FSConnectShareTask._result
+ _OBJC_IVAR_$_FSGenericURLResource._url
+ _OBJC_IVAR_$_FSModuleIdentity._applicationGroup
+ _OBJC_IVAR_$_FSMutableFileDataBuffer._proxyOfBuffer
+ _OBJC_IVAR_$_FSOpenSessionParameters._authenticationInfo
+ _OBJC_IVAR_$_FSOpenSessionParameters._openFlags
+ _OBJC_IVAR_$_FSOpenSessionParameters._uiOption
+ _OBJC_IVAR_$_FSPathURLResource._url
+ _OBJC_IVAR_$_FSPathURLResource._urlWrapper
+ _OBJC_IVAR_$_FSPathURLResource._writable
+ _OBJC_IVAR_$_FSServerEnumerateSharesParameters._authenticationInfo
+ _OBJC_IVAR_$_FSServerInfo._authenticationInfo
+ _OBJC_IVAR_$_FSServerInfo._displayName
+ _OBJC_IVAR_$_FSServerInfo._flags
+ _OBJC_IVAR_$_FSServerInfo._machineType
+ _OBJC_IVAR_$_FSServerInfo._proxyServerName
+ _OBJC_IVAR_$_FSServerInfo._proxyServerRealm
+ _OBJC_IVAR_$_FSServerInfo._serverOS
+ _OBJC_IVAR_$_FSServerInfo._supportedMechTypes
+ _OBJC_IVAR_$_FSServerInfoTask._result
+ _OBJC_IVAR_$_FSServerSessionInfo._connectedByUser
+ _OBJC_IVAR_$_FSServerSessionInfo._howConnected
+ _OBJC_IVAR_$_FSServerSessionInfoTask._result
+ _OBJC_IVAR_$_FSServerShareInfo._additionalInfo
+ _OBJC_IVAR_$_FSServerShareInfo._alreadyConnected
+ _OBJC_IVAR_$_FSServerShareInfo._connectedByUser
+ _OBJC_IVAR_$_FSServerShareInfo._displayName
+ _OBJC_IVAR_$_FSServerShareInfo._hasPassword
+ _OBJC_IVAR_$_FSServerShareInfo._hidden
+ _OBJC_IVAR_$_FSServerShareInfo._howConnected
+ _OBJC_IVAR_$_FSServerShareInfo._printerShare
+ _OBJC_IVAR_$_FSServerURLParameters._extras
+ _OBJC_IVAR_$_FSServerURLParameters._host
+ _OBJC_IVAR_$_FSServerURLParameters._options
+ _OBJC_IVAR_$_FSServerURLParameters._password
+ _OBJC_IVAR_$_FSServerURLParameters._path
+ _OBJC_IVAR_$_FSServerURLParameters._port
+ _OBJC_IVAR_$_FSServerURLParameters._scheme
+ _OBJC_IVAR_$_FSServerURLParameters._user
+ _OBJC_IVAR_$_FSTask._cancellationHandler
+ _OBJC_IVAR_$_FSTaskDescription._taskHasCancellationHandler
+ _OBJC_IVAR_$_FSTaskMessageSTDIOWithProgress._completedError
+ _OBJC_IVAR_$_FSTaskMessageSTDIOWithProgress._dispatch_group
+ _OBJC_IVAR_$_FSTaskMessageSTDIOWithProgress._progress
+ _OBJC_IVAR_$_FSTaskMessageSTDIOWithProgress._progressHasShown
+ _OBJC_IVAR_$_FSTaskMessageSTDIOWithProgress._progressShowing
+ _OBJC_IVAR_$_FSTaskMessageSTDIOWithProgress._twiddleState
+ _OBJC_IVAR_$_FSTaskMessageSTDIOWithProgress.progress_buffer
+ _OBJC_IVAR_$_FSTaskMessageSTDIOWithProgress.screen_width
+ _OBJC_IVAR_$_FSVolumeConnector._workQueue
+ _OBJC_IVAR_$_FSWorkQueue._concurrency
+ _OBJC_IVAR_$_FSWorkQueue._didInitQueues
+ _OBJC_IVAR_$_FSWorkQueue._domain
+ _OBJC_METACLASS_$_FSConnectShareTask
+ _OBJC_METACLASS_$_FSEnumeratedSharePacker
+ _OBJC_METACLASS_$_FSOpenSessionParameters
+ _OBJC_METACLASS_$_FSServerEnumerateSharesParameters
+ _OBJC_METACLASS_$_FSServerInfo
+ _OBJC_METACLASS_$_FSServerInfoTask
+ _OBJC_METACLASS_$_FSServerSessionInfo
+ _OBJC_METACLASS_$_FSServerSessionInfoTask
+ _OBJC_METACLASS_$_FSServerShareInfo
+ _OBJC_METACLASS_$_FSServerURLParameters
+ _OBJC_METACLASS_$_FSTaskMessageSTDIOWithProgress
+ __MergedGlobals
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUUID_$_FSEntityIdentifier
+ __OBJC_$_CLASS_METHODS_FSGenericURLResource
+ __OBJC_$_CLASS_METHODS_FSOpenSessionParameters
+ __OBJC_$_CLASS_METHODS_FSPathURLResource(Private)
+ __OBJC_$_CLASS_METHODS_FSServerEnumerateSharesParameters
+ __OBJC_$_CLASS_METHODS_FSServerInfo
+ __OBJC_$_CLASS_METHODS_FSServerSessionInfo
+ __OBJC_$_CLASS_METHODS_FSServerShareInfo
+ __OBJC_$_CLASS_METHODS_FSServerURLParameters
+ __OBJC_$_CLASS_METHODS_FSTaskDescription(Management|Project)
+ __OBJC_$_CLASS_PROP_LIST_FSOpenSessionParameters
+ __OBJC_$_CLASS_PROP_LIST_FSServerEnumerateSharesParameters
+ __OBJC_$_CLASS_PROP_LIST_FSServerInfo
+ __OBJC_$_CLASS_PROP_LIST_FSServerSessionInfo
+ __OBJC_$_CLASS_PROP_LIST_FSServerShareInfo
+ __OBJC_$_CLASS_PROP_LIST_FSServerURLParameters
+ __OBJC_$_CLASS_PROP_LIST_FSServerURLResource
+ __OBJC_$_INSTANCE_METHODS_FSConnectShareTask
+ __OBJC_$_INSTANCE_METHODS_FSEnumeratedSharePacker
+ __OBJC_$_INSTANCE_METHODS_FSGenericURLResource
+ __OBJC_$_INSTANCE_METHODS_FSMutableFileDataBuffer(Project)
+ __OBJC_$_INSTANCE_METHODS_FSOpenSessionParameters
+ __OBJC_$_INSTANCE_METHODS_FSPathURLResource(Private)
+ __OBJC_$_INSTANCE_METHODS_FSServerEnumerateSharesParameters
+ __OBJC_$_INSTANCE_METHODS_FSServerInfo
+ __OBJC_$_INSTANCE_METHODS_FSServerInfoTask
+ __OBJC_$_INSTANCE_METHODS_FSServerSessionInfo
+ __OBJC_$_INSTANCE_METHODS_FSServerSessionInfoTask
+ __OBJC_$_INSTANCE_METHODS_FSServerShareInfo
+ __OBJC_$_INSTANCE_METHODS_FSServerURLParameters
+ __OBJC_$_INSTANCE_METHODS_FSTaskDescription(Management|Project)
+ __OBJC_$_INSTANCE_METHODS_FSTaskMessageSTDIOWithProgress
+ __OBJC_$_INSTANCE_METHODS_FSTaskOptions(Private|Project)
+ __OBJC_$_INSTANCE_VARIABLES_FSConnectShareTask
+ __OBJC_$_INSTANCE_VARIABLES_FSOpenSessionParameters
+ __OBJC_$_INSTANCE_VARIABLES_FSPathURLResource
+ __OBJC_$_INSTANCE_VARIABLES_FSServerEnumerateSharesParameters
+ __OBJC_$_INSTANCE_VARIABLES_FSServerInfo
+ __OBJC_$_INSTANCE_VARIABLES_FSServerInfoTask
+ __OBJC_$_INSTANCE_VARIABLES_FSServerSessionInfo
+ __OBJC_$_INSTANCE_VARIABLES_FSServerSessionInfoTask
+ __OBJC_$_INSTANCE_VARIABLES_FSServerShareInfo
+ __OBJC_$_INSTANCE_VARIABLES_FSServerURLParameters
+ __OBJC_$_INSTANCE_VARIABLES_FSTaskMessageSTDIOWithProgress
+ __OBJC_$_PROP_LIST_FSConnectShareTask
+ __OBJC_$_PROP_LIST_FSOpenSessionParameters
+ __OBJC_$_PROP_LIST_FSPathURLResource
+ __OBJC_$_PROP_LIST_FSServerEnumerateSharesParameters
+ __OBJC_$_PROP_LIST_FSServerInfo
+ __OBJC_$_PROP_LIST_FSServerInfoTask
+ __OBJC_$_PROP_LIST_FSServerSessionInfo
+ __OBJC_$_PROP_LIST_FSServerSessionInfoTask
+ __OBJC_$_PROP_LIST_FSServerShareInfo
+ __OBJC_$_PROP_LIST_FSServerURLParameters
+ __OBJC_$_PROP_LIST_FSTaskMessageSTDIOWithProgress
+ __OBJC_$_PROP_LIST_FSVolume
+ __OBJC_$_PROP_LIST_NSUUID_$_FSEntityIdentifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FSServerURLUnaryOperations
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FSServerURLUnaryOperations
+ __OBJC_$_PROTOCOL_REFS_FSServerURLUnaryOperations
+ __OBJC_CLASS_PROTOCOLS_$_FSItemTriple
+ __OBJC_CLASS_PROTOCOLS_$_FSOpenSessionParameters
+ __OBJC_CLASS_PROTOCOLS_$_FSServerEnumerateSharesParameters
+ __OBJC_CLASS_PROTOCOLS_$_FSServerInfo
+ __OBJC_CLASS_PROTOCOLS_$_FSServerSessionInfo
+ __OBJC_CLASS_PROTOCOLS_$_FSServerShareInfo
+ __OBJC_CLASS_PROTOCOLS_$_FSServerURLParameters
+ __OBJC_CLASS_PROTOCOLS_$_FSServerURLResource
+ __OBJC_CLASS_PROTOCOLS_$_FSTaskDescription(Management|Project)
+ __OBJC_CLASS_PROTOCOLS_$_FSTaskMessageSTDIOWithProgress
+ __OBJC_CLASS_RO_$_FSConnectShareTask
+ __OBJC_CLASS_RO_$_FSEnumeratedSharePacker
+ __OBJC_CLASS_RO_$_FSOpenSessionParameters
+ __OBJC_CLASS_RO_$_FSServerEnumerateSharesParameters
+ __OBJC_CLASS_RO_$_FSServerInfo
+ __OBJC_CLASS_RO_$_FSServerInfoTask
+ __OBJC_CLASS_RO_$_FSServerSessionInfo
+ __OBJC_CLASS_RO_$_FSServerSessionInfoTask
+ __OBJC_CLASS_RO_$_FSServerShareInfo
+ __OBJC_CLASS_RO_$_FSServerURLParameters
+ __OBJC_CLASS_RO_$_FSTaskMessageSTDIOWithProgress
+ __OBJC_LABEL_PROTOCOL_$_FSServerURLUnaryOperations
+ __OBJC_METACLASS_RO_$_FSConnectShareTask
+ __OBJC_METACLASS_RO_$_FSEnumeratedSharePacker
+ __OBJC_METACLASS_RO_$_FSOpenSessionParameters
+ __OBJC_METACLASS_RO_$_FSServerEnumerateSharesParameters
+ __OBJC_METACLASS_RO_$_FSServerInfo
+ __OBJC_METACLASS_RO_$_FSServerInfoTask
+ __OBJC_METACLASS_RO_$_FSServerSessionInfo
+ __OBJC_METACLASS_RO_$_FSServerSessionInfoTask
+ __OBJC_METACLASS_RO_$_FSServerShareInfo
+ __OBJC_METACLASS_RO_$_FSServerURLParameters
+ __OBJC_METACLASS_RO_$_FSTaskMessageSTDIOWithProgress
+ __OBJC_PROTOCOL_$_FSServerURLUnaryOperations
+ ___106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke.423
+ ___106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke_9
+ ___31-[FSBlockDeviceResource revoke]_block_invoke.77
+ ___31-[FSBlockDeviceResource revoke]_block_invoke.77.cold.1
+ ___38-[FSClient(Private) doneFSCKWithTask:]_block_invoke
+ ___38-[FSClient(Private) doneFSCKWithTask:]_block_invoke_2
+ ___39-[FSModuleConnector sendCloseResource:]_block_invoke.239
+ ___39-[FSModuleConnector sendCloseResource:]_block_invoke.239.cold.1
+ ___40-[FSMessageConnection(Private) connect:]_block_invoke.73
+ ___40-[FSMessageConnection(Private) connect:]_block_invoke.73.cold.1
+ ___40-[FSModuleConnector sendRevokeResource:]_block_invoke.234
+ ___40-[FSModuleConnector sendRevokeResource:]_block_invoke.234.cold.1
+ ___43-[FSBlockDeviceResource(Private) terminate]_block_invoke
+ ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.242
+ ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.242.cold.1
+ ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.242.cold.2
+ ___52-[FSVolumeConnector reclaim:requestID:replyHandler:]_block_invoke.403
+ ___55-[FSClient(Private) startFSCKWithDevice:volumes:error:]_block_invoke
+ ___55-[FSClient(Private) startFSCKWithDevice:volumes:error:]_block_invoke_2
+ ___55-[FSMessageConnection(Private) completed:replyHandler:]_block_invoke.75
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.262
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.267
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.267.cold.1
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.267.cold.2
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.269
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.272
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.cold.5
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke_2.270
+ ___57-[FSModuleConnector unloadResource:options:replyHandler:]_block_invoke.276
+ ___57-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke.414
+ ___58-[FSVolumeConnector getFreeSpaceInVolumeWithReplyHandler:]_block_invoke
+ ___58-[FSVolumeConnector getFreeSpaceInVolumeWithReplyHandler:]_block_invoke.cold.1
+ ___63-[FSVolumeConnector readSymbolicLinkOf:requestID:replyHandler:]_block_invoke.409
+ ___64-[FSVolumeConnector getIOItemAttributesSubsetData:replyHandler:]_block_invoke
+ ___64-[FSVolumeConnector getIOItemAttributesSubsetData:replyHandler:]_block_invoke.cold.1
+ ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke.395
+ ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke.399
+ ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke_2.400
+ ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke_4
+ ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke_4.cold.1
+ ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke.278
+ ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.281
+ ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.281.cold.1
+ ___67-[FSVolumeConnector getStandardItemAttributesForItem:replyHandler:]_block_invoke.cold.3
+ ___67-[FSVolumeConnector setFileAttributesOf:to:requestID:replyHandler:]_block_invoke.406
+ ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.249
+ ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.251
+ ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke_3
+ ___70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke.257
+ ___70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke.258
+ ___71-[FSVolumeConnector blockmapFile:range:flags:operationID:replyHandler:]_block_invoke.294
+ ___71-[FSVolumeConnector blockmapFile:range:flags:operationID:replyHandler:]_block_invoke.cold.2
+ ___71-[FSVolumeConnector endIO:range:status:flags:operationID:replyHandler:]_block_invoke.297
+ ___71-[FSVolumeConnector endIO:range:status:flags:operationID:replyHandler:]_block_invoke_2
+ ___72-[FSVolumeConnector writeTo:atOffset:fromBuffer:requestID:replyHandler:]_block_invoke.404
+ ___72-[FSVolumeConnector writeTo:atOffset:fromBuffer:requestID:replyHandler:]_block_invoke_2
+ ___72-[FSVolumeConnector writeTo:atOffset:fromBuffer:requestID:replyHandler:]_block_invoke_3
+ ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]_block_invoke
+ ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]_block_invoke.179
+ ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]_block_invoke_2
+ ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModuleInstances:]_block_invoke_2.181
+ ___73-[FSVolumeConnector makeLinkOf:named:inDirectory:requestID:replyHandler:]_block_invoke.412
+ ___73-[FSVolumeConnector makeLinkOf:named:inDirectory:requestID:replyHandler:]_block_invoke_5
+ ___73-[FSVolumeConnector readFrom:atOffset:intoBuffer:requestID:replyHandler:]_block_invoke.405
+ ___73-[FSVolumeConnector readFrom:atOffset:intoBuffer:requestID:replyHandler:]_block_invoke_2
+ ___75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke.392
+ ___75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke.393
+ ___76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke.390
+ ___76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke_4
+ ___76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke_5
+ ___76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke_6
+ ___76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke_6.cold.1
+ ___77-[FSVolumeConnector removeItem:from:named:usingFlags:requestID:replyHandler:]_block_invoke.402
+ ___77-[FSVolumeConnector removeItem:from:named:usingFlags:requestID:replyHandler:]_block_invoke_5
+ ___82-[FSVolumeConnector removeDirectory:from:named:usingFlags:requestID:replyHandler:]_block_invoke.401
+ ___82-[FSVolumeConnector removeDirectory:from:named:usingFlags:requestID:replyHandler:]_block_invoke_3
+ ___83+[FSBlockDeviceResource(Project) openWithBSDName:writable:auditToken:replyHandler:]_block_invoke.209
+ ___83+[FSBlockDeviceResource(Project) openWithBSDName:writable:auditToken:replyHandler:]_block_invoke.209.cold.1
+ ___84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke.410
+ ___84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke.411
+ ___96-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke.418
+ ___96-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke_5
+ ___block_descriptor_40_e8_32bs_e16_v16?0"NSData"8ls32l8
+ ___block_descriptor_48_e8_32bs_e16_v16?0"NSData"8ls32l8
+ ___block_descriptor_48_e8_32r40r_e28_v24?0"NSUUID"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e38_v24?0"FSItemAttributes"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e38_v24?0"FSItemAttributes"8"NSError"16ls40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40bs_e16_v16?0"NSData"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e16_v16?0"NSData"8ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e16_v16?0"NSData"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e16_v16?0"NSData"8ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?0Q8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e16_v16?0"NSData"8ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v24?0Q8"NSError"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e38_v24?0"FSItemAttributes"8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r_e20_v24?0Q8"NSError"16ls56l8r64l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e16_v16?0"NSData"8ls32l8s40l8s48l8s56l8s72l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e16_v16?0"NSData"8ls32l8s40l8s48l8s72l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e16_v16?0"NSData"8ls32l8s72l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e43_v32?0"FSItem"8"FSFileName"16"NSError"24ls72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s80l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s80l8s64l8s72l8
+ ___block_descriptor_92_e8_32s40s48s56s64s72bs80r_e16_v16?0"NSData"8ls32l8s40l8r80l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_92_e8_32s40s48s56s64s72bs80r_e5_v8?0ls32l8s40l8s48l8r80l8s56l8s64l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s88l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.236
+ ___block_literal_global.238
+ ___block_literal_global.241
+ ___block_literal_global.254
+ ___block_literal_global.260
+ ___block_literal_global.280
+ ___block_literal_global.304
+ ___block_literal_global.71
+ ___block_literal_global.77
+ ___stdoutp
+ ___updateTimer_block_invoke
+ ___updateTimer_block_invoke.cold.1
+ ___updateTimer_block_invoke.cold.2
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_FSKit
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_FSKit
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_FSKit
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_FSKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_FSKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_FSKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_FSKit
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_FSKit
+ _fcntl
+ _fflush
+ _firstVoidPointer
+ _fstat
+ _gInterval
+ _gProgress
+ _gProgressVal
+ _gStartDate
+ _gTimer
+ _locking_printf
+ _locking_vprintf
+ _memset
+ _objc_msgSend$_updateProviderListForFilteredFSModuleInstances:
+ _objc_msgSend$accessTime
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$allocSize
+ _objc_msgSend$bsdName
+ _objc_msgSend$capacity
+ _objc_msgSend$changeTime
+ _objc_msgSend$date
+ _objc_msgSend$didCompleteWithError:
+ _objc_msgSend$doneFSCKWithTask:
+ _objc_msgSend$doneFSCKWithTask:replyHandler:
+ _objc_msgSend$enableOpenUnlinkEmulation
+ _objc_msgSend$fileID
+ _objc_msgSend$fillProgressBar:
+ _objc_msgSend$fractionCompleted
+ _objc_msgSend$getDeviceName:
+ _objc_msgSend$getFreeSpaceInVolumeWithReplyHandler:
+ _objc_msgSend$getIOItemAttributesSubsetData:replyHandler:
+ _objc_msgSend$getProgressURLKey
+ _objc_msgSend$hasCancellationHandler
+ _objc_msgSend$hasMinimalRequiredAttributes
+ _objc_msgSend$hideProgressLocked
+ _objc_msgSend$initAsSecureURL:readOnly:
+ _objc_msgSend$initAsSecureURL:writable:
+ _objc_msgSend$initQueues
+ _objc_msgSend$initWithURL:readOnly:
+ _objc_msgSend$initWithURL:writable:
+ _objc_msgSend$isFileURL
+ _objc_msgSend$isIndeterminate
+ _objc_msgSend$isValid:
+ _objc_msgSend$isValidModuleIdentifier:withError:
+ _objc_msgSend$modifyTime
+ _objc_msgSend$mp
+ _objc_msgSend$precomposedStringWithCanonicalMapping
+ _objc_msgSend$printAboveProgress:
+ _objc_msgSend$proxyResourceForBSDName:
+ _objc_msgSend$publish
+ _objc_msgSend$removeObserver:forKeyPath:context:
+ _objc_msgSend$setProgress:
+ _objc_msgSend$setTaskHasCancellationHandler:
+ _objc_msgSend$setUserInfoObject:forKey:
+ _objc_msgSend$showProgressLocked
+ _objc_msgSend$size
+ _objc_msgSend$startFSCKWithDevice:volumes:error:
+ _objc_msgSend$startFSCKWithDevice:volumes:replyHandler:
+ _objc_msgSend$taskHasCancellationHandler
+ _objc_msgSend$terminateLocked
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$unpublish
+ _objc_msgSend$vma
+ _printf
+ _putchar
+ _snprintf
+ _strerror
+ _strncpy
+ _symbolic _____yxq_GSg s6ResultOsRi_zRi0_zrlE
+ _updateTimer
+ _vprintf
- +[FSBlockDeviceResource(Private) proxyResourceForBSDName:writable:]
- +[FSClient installedExtensionsWithError:]
- +[FSGenericURLResource(Private) secureResourceWithURL:readonly:]
- +[FSKitConstants(project) FSTaskProgressXPCProtocol]
- +[FSTaskProgress(Project) constructFromListener:description:replyHandler:]
- +[FSTaskProgressConnector newForProgress:description:]
- +[FSVolume(FSKit_private) volumeIdentifierDescription:]
- +[NSError(FSKitAdditions) fskit_errorWithPOSIXCode:itemURL:debugDescription:]
- -[FSBlockDeviceBufferResource delayedMetadataWriteFrom:startingAt:length:]
- -[FSBlockDeviceBufferResource metadataClear:wait:]
- -[FSBlockDeviceBufferResource metadataFlush]
- -[FSBlockDeviceBufferResource metadataPurge:]
- -[FSBlockDeviceBufferResource metadataReadInto:startingAt:length:]
- -[FSBlockDeviceBufferResource metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:]
- -[FSBlockDeviceBufferResource metadataWriteFrom:startingAt:length:]
- -[FSBlockDeviceBufferResource metadataWriteFrom:startingAt:length:completionHandler:]
- -[FSBlockDeviceResource encodeWithCoder:].cold.1
- -[FSBlockDeviceResource(Private) metadataWriteFrom:startingAt:length:completionHandler:]
- -[FSBlockDeviceResource(Private) synchronousReadInto:startingAt:length:reply:]
- -[FSBlockDeviceResource(Private) synchronousReadInto:startingAt:length:replyHandler:]
- -[FSClient(Private) getFSProgressForTask:replyHandler:]
- -[FSClient(Private) loadResource:shortName:options:synchronousReply:]
- -[FSClient(Private) probeResource:usingBundle:reply:]
- -[FSClient(Private) validateVolumeName:usingBundle:volumeID:reply:]
- -[FSFileHandle initWithBase64:]
- -[FSGenericURLResource initWithURL:readonly:]
- -[FSGenericURLResource setUrlWrapper:]
- -[FSGenericURLResource urlWrapper]
- -[FSGenericURLResource(Private) initAsSecureURL:readonly:]
- -[FSGenericURLResource(Private) initWithURL:]
- -[FSMessageConnection completed:reply:]
- -[FSMessageConnection(Project) localizedMessage:table:bundle:arguments:]
- -[FSMessageReceiverDelegateWrapper completed:reply:]
- -[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]
- -[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:].cold.1
- -[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]
- -[FSModuleConnector getProgressPortForTask:replyHandler:]
- -[FSModuleExtension fskitdIsClient:]
- -[FSModuleExtension fskitdIsClient:].cold.1
- -[FSModuleHost(Project) _updateProviderListForFilteredFSModileInstances:]
- -[FSModuleHost(Project) configurationForDefaultInstanceOf:]
- -[FSModuleHost(Project) configurationForDefaultInstanceOfBundle:]
- -[FSModuleHost(Project) isValidModuleIdentifier:WithError:]
- -[FSModuleHost(Project) setupSyncronously]
- -[FSModuleTask connector]
- -[FSModuleTask setConnector:]
- -[FSTaskOptions(Project) initWithOptions:]
- -[FSTaskOptionsBundle enumerateOptionsWithBlock:]
- -[FSTaskProgress .cxx_destruct]
- -[FSTaskProgress dealloc]
- -[FSTaskProgress initWithProgress:description:]
- -[FSTaskProgress initialDescription]
- -[FSTaskProgress ourConn]
- -[FSTaskProgress progress]
- -[FSTaskProgress setOurConn:]
- -[FSTaskProgressConnector .cxx_destruct]
- -[FSTaskProgressConnector dealloc]
- -[FSTaskProgressConnector endpoint]
- -[FSTaskProgressConnector getProgress:]
- -[FSTaskProgressConnector initWithProgress:description:]
- -[FSTaskProgressConnector listener:shouldAcceptNewConnection:]
- -[FSTaskProgressConnector listener]
- -[FSTaskProgressConnector pendingReplyBlocks]
- -[FSTaskProgressConnector progress]
- -[FSTaskProgressConnector setListener:]
- -[FSTaskProgressConnector setPendingReplyBlocks:]
- -[FSTaskProgressConnector setProgress:]
- -[FSTaskProgressConnector setTaskDesc:]
- -[FSTaskProgressConnector taskDesc]
- -[FSVolume dealloc]
- -[FSVolume renameWorkQueue]
- -[FSVolume setRenameWorkQueue:]
- -[FSVolumeConnector getFreeSpaceInVolume]
- -[FSWorkQueue initQueueWithDomain:concurrency:].cold.1
- -[NSError(FSKitAdditions) fskit_isFSKitError:]
- -[NSUUID(FSEntityIdentifier) fs_entityIdentifier]
- -[NSUUID(FSEntityIdentifier_private) containerIdentifier]
- GCC_except_table103
- GCC_except_table106
- GCC_except_table108
- GCC_except_table115
- GCC_except_table13
- GCC_except_table24
- GCC_except_table31
- GCC_except_table37
- GCC_except_table53
- GCC_except_table54
- GCC_except_table58
- GCC_except_table66
- GCC_except_table68
- GCC_except_table71
- GCC_except_table8
- GCC_except_table85
- GCC_except_table88
- GCC_except_table91
- GCC_except_table94
- GCC_except_table95
- GCC_except_table97
- _FSActivateOptionSyntaxKey
- _FSCheckOptionSyntaxKey
- _FSFormatOptionSyntaxKey
- _FSKitLoc
- _FSKitLocalizedErrorStringForKeyLiteral
- _FSKitLocv
- _FSKitLocvImpl
- _FSKitLocvImpl.cold.1
- _OBJC_CLASS_$_FSTaskProgress
- _OBJC_CLASS_$_FSTaskProgressConnector
- _OBJC_IVAR_$_FSGenericURLResource._URL
- _OBJC_IVAR_$_FSGenericURLResource._urlWrapper
- _OBJC_IVAR_$_FSModuleTask._connector
- _OBJC_IVAR_$_FSTaskProgress._initialDescription
- _OBJC_IVAR_$_FSTaskProgress._ourConn
- _OBJC_IVAR_$_FSTaskProgress._progress
- _OBJC_IVAR_$_FSTaskProgressConnector._endpoint
- _OBJC_IVAR_$_FSTaskProgressConnector._listener
- _OBJC_IVAR_$_FSTaskProgressConnector._pendingReplyBlocks
- _OBJC_IVAR_$_FSTaskProgressConnector._progress
- _OBJC_IVAR_$_FSTaskProgressConnector._taskDesc
- _OBJC_IVAR_$_FSVolume._renameWorkQueue
- _OBJC_METACLASS_$_FSTaskProgress
- _OBJC_METACLASS_$_FSTaskProgressConnector
- _OUTLINED_FUNCTION_17
- __OBJC_$_CLASS_METHODS_FSGenericURLResource(Private)
- __OBJC_$_CLASS_METHODS_FSTaskDescription(Project)
- __OBJC_$_CLASS_METHODS_FSTaskProgress(Project)
- __OBJC_$_CLASS_METHODS_FSTaskProgressConnector
- __OBJC_$_CLASS_METHODS_FSVolume(FSKit_private)
- __OBJC_$_INSTANCE_METHODS_FSGenericURLResource(Private)
- __OBJC_$_INSTANCE_METHODS_FSMutableFileDataBuffer
- __OBJC_$_INSTANCE_METHODS_FSTaskDescription(Project)
- __OBJC_$_INSTANCE_METHODS_FSTaskOptions(Project)
- __OBJC_$_INSTANCE_METHODS_FSTaskProgress
- __OBJC_$_INSTANCE_METHODS_FSTaskProgressConnector
- __OBJC_$_INSTANCE_METHODS_NSUUID(FSEntityIdentifier|FSEntityIdentifier_private)
- __OBJC_$_INSTANCE_VARIABLES_FSTaskProgress
- __OBJC_$_INSTANCE_VARIABLES_FSTaskProgressConnector
- __OBJC_$_PROP_LIST_FSTaskProgress
- __OBJC_$_PROP_LIST_FSTaskProgressConnector
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_FSTaskProgressXPC
- __OBJC_$_PROTOCOL_METHOD_TYPES_FSTaskProgressXPC
- __OBJC_$_PROTOCOL_REFS_FSTaskProgressXPC
- __OBJC_CLASS_PROTOCOLS_$_FSTaskDescription(Project)
- __OBJC_CLASS_PROTOCOLS_$_FSTaskProgressConnector
- __OBJC_CLASS_RO_$_FSTaskProgress
- __OBJC_CLASS_RO_$_FSTaskProgressConnector
- __OBJC_LABEL_PROTOCOL_$_FSTaskProgressXPC
- __OBJC_METACLASS_RO_$_FSTaskProgress
- __OBJC_METACLASS_RO_$_FSTaskProgressConnector
- __OBJC_PROTOCOL_$_FSTaskProgressXPC
- __OBJC_PROTOCOL_REFERENCE_$_FSTaskProgressXPC
- ___106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke.407
- ___31-[FSBlockDeviceResource revoke]_block_invoke.71
- ___31-[FSBlockDeviceResource revoke]_block_invoke.71.cold.1
- ___39-[FSMessageConnection completed:reply:]_block_invoke
- ___39-[FSModuleConnector sendCloseResource:]_block_invoke.232
- ___39-[FSModuleConnector sendCloseResource:]_block_invoke.232.cold.1
- ___40-[FSMessageConnection(Private) connect:]_block_invoke.74
- ___40-[FSMessageConnection(Private) connect:]_block_invoke.74.cold.1
- ___40-[FSModuleConnector sendRevokeResource:]_block_invoke.227
- ___40-[FSModuleConnector sendRevokeResource:]_block_invoke.227.cold.1
- ___41+[FSClient installedExtensionsWithError:]_block_invoke
- ___44-[FSMessageReceiverDelegateWrapper didStart]_block_invoke_2
- ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.235
- ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.235.cold.1
- ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.235.cold.2
- ___52-[FSMessageReceiverDelegateWrapper completed:reply:]_block_invoke
- ___55-[FSClient(Private) getFSProgressForTask:replyHandler:]_block_invoke
- ___55-[FSClient(Private) getFSProgressForTask:replyHandler:]_block_invoke_2
- ___55-[FSClient(Private) getFSProgressForTask:replyHandler:]_block_invoke_3
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.268
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.273
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.273.cold.1
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.273.cold.2
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.275
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.278
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke_2.276
- ___56-[FSMessageReceiver listener:shouldAcceptNewConnection:]_block_invoke_3
- ___57-[FSModuleConnector unloadResource:options:replyHandler:]_block_invoke.282
- ___57-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke.398
- ___63-[FSVolumeConnector readSymbolicLinkOf:requestID:replyHandler:]_block_invoke.394
- ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke.384
- ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke.388
- ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke_2.389
- ___64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke_3.cold.1
- ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke.284
- ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.287
- ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.287.cold.1
- ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.252
- ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.254
- ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke_2.255
- ___70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke.264
- ___70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke_2.265
- ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModileInstances:]_block_invoke
- ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModileInstances:]_block_invoke.179
- ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModileInstances:]_block_invoke_2
- ___73-[FSModuleHost(Project) _updateProviderListForFilteredFSModileInstances:]_block_invoke_2.181
- ___73-[FSVolumeConnector makeLinkOf:named:inDirectory:requestID:replyHandler:]_block_invoke.396
- ___74+[FSTaskProgress(Project) constructFromListener:description:replyHandler:]_block_invoke
- ___74+[FSTaskProgress(Project) constructFromListener:description:replyHandler:]_block_invoke.26
- ___74+[FSTaskProgress(Project) constructFromListener:description:replyHandler:]_block_invoke.27
- ___74+[FSTaskProgress(Project) constructFromListener:description:replyHandler:]_block_invoke_2
- ___74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke
- ___74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.243
- ___74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.243.cold.1
- ___74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.244
- ___74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke_2
- ___74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke_2.245
- ___75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke
- ___75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke.258
- ___75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke.258.cold.1
- ___75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke_2
- ___75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke_2.259
- ___75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke_3
- ___75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke.381
- ___76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke.379
- ___76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke_3.cold.1
- ___77-[FSVolumeConnector removeItem:from:named:usingFlags:requestID:replyHandler:]_block_invoke.391
- ___82-[FSVolumeConnector removeDirectory:from:named:usingFlags:requestID:replyHandler:]_block_invoke.390
- ___83+[FSBlockDeviceResource(Project) openWithBSDName:writable:auditToken:replyHandler:]_block_invoke.200
- ___83+[FSBlockDeviceResource(Project) openWithBSDName:writable:auditToken:replyHandler:]_block_invoke.200.cold.1
- ___84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke.395
- ___96-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke.402
- ___block_descriptor_108_e8_32s40s48s56s64s72s80s88bs96r_e5_v8?0ls32l8s40l8r96l8s48l8s56l8s88l8s64l8s72l8s80l8
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s104l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_40_e8_32bs_e36_v24?0"FSTaskProgress"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e65_v32?0"NSXPCListenerEndpoint"8"FSTaskDescription"16"NSError"24ls32l8
- ___block_descriptor_48_e8_32bs40w_e38_v24?0"FSItemAttributes"8"NSError"16ls32l8w40l8
- ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
- ___block_descriptor_48_e8_32s40bs_e20_v24?0Q8"NSError"16ls40l8s32l8
- ___block_descriptor_56_e8_32bs40r48r_e17_v16?0"NSError"8ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32bs40r_e17_v16?0"NSError"8lr40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56bs_e16_v16?0"NSData"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48bs56r_e20_v24?0Q8"NSError"16ls48l8r56l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56bs64w_e38_v24?0"FSItemAttributes"8"NSError"16ls56l8w64l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e16_v16?0"NSData"8ls32l8s40l8s64l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e16_v16?0"NSData"8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e16_v16?0"NSData"8ls32l8s40l8s48l8s56l8s64l8s80l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e16_v16?0"NSData"8ls32l8s40l8s48l8s56l8s80l8s64l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e16_v16?0"NSData"8ls32l8s40l8s48l8s80l8s56l8s64l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e43_v32?0"FSItem"8"FSFileName"16"NSError"24ls80l8s32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_92_e8_32s40s48s56s64s72bs80r_e16_v16?0"NSData"8ls32l8s40l8r80l8s48l8s56l8s72l8s64l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s88l8s80l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s88l8s72l8s80l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s88l8s64l8s72l8s80l8
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.234
- ___block_literal_global.248
- ___block_literal_global.257
- ___block_literal_global.261
- ___block_literal_global.267
- ___block_literal_global.286
- ___block_literal_global.30
- ___block_literal_global.316
- ___block_literal_global.32
- ___block_literal_global.7
- ___block_literal_global.72
- ___block_literal_global.82
- ___block_literal_global.84
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_FSKit
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_FSKit
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_FSKit
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_FSKit
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_FSKit
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_FSKit
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_FSKit
- _objc_msgSend$FSTaskProgressXPCProtocol
- _objc_msgSend$_updateProviderListForFilteredFSModileInstances:
- _objc_msgSend$checkResource:options:connection:taskID:progress:replyHandler:
- _objc_msgSend$checkResource:options:connection:taskID:replyHandler:
- _objc_msgSend$completed:reply:
- _objc_msgSend$connector
- _objc_msgSend$constructFromListener:description:replyHandler:
- _objc_msgSend$formatResource:options:connection:taskID:progress:replyHandler:
- _objc_msgSend$formatResource:options:connection:taskID:replyHandler:
- _objc_msgSend$fs_containerIdentifier
- _objc_msgSend$getFreeSpaceInVolume
- _objc_msgSend$getProgress:
- _objc_msgSend$getProgressPortForTask:replyHandler:
- _objc_msgSend$initAsSecureURL:readonly:
- _objc_msgSend$initWithBase64Encoding:
- _objc_msgSend$initWithProgress:description:
- _objc_msgSend$initWithURL:readonly:
- _objc_msgSend$isValidModuleIdentifier:WithError:
- _objc_msgSend$loadResource:shortName:options:synchronousReplyHandler:
- _objc_msgSend$newForProgress:description:
- _objc_msgSend$setConnector:
- _objc_msgSend$setOurConn:
- _objc_msgSend$setPausingHandler:
- _objc_msgSend$synchronousReadInto:startingAt:length:replyHandler:
- _objc_msgSend$taskDescription
- _objc_msgSend$taskProgress
- _objc_msgSend$validateVolumeName:usingBundle:volumeID:replyHandler:
- _objc_msgSend$writeMetaAsync:buffer:offset:length:
- _objc_retain_x9
- _swift_bridgeObjectRetain
- _swift_unknownObjectRelease
- _symbolic _____yxq_GSg s6ResultOsRi_zrlE
CStrings:
+ "\n"
+ "!"
+ "\""
+ "%02d%%"
+ "%s"
+ "%s: After %f seconds, changing rate to 1s"
+ "%s: After %f seconds, changing rate to 500ms"
+ "%s: Blockmap didn’t return an error, and it didn’t pack any extents. We treat this as an error (EINVAL)."
+ "%s: Can't start check on (%@/%@) error (%@)"
+ "%s: Can't start check, invalid arguments"
+ "%s: Can't start check, previous check task (%@) is running"
+ "%s: Can't update the progress, check task didn't start"
+ "%s: Check task (%@) is done"
+ "%s: Check task UUID (%@) finished"
+ "%s: Check task didn't start"
+ "%s: Format task UUID (%@) finished"
+ "%s: Reported attributes are incomplete"
+ "%s: Started check task (%@)"
+ "%s: Trying to remove nil filehandle"
+ "%s: fskitd encountered issues trying to make the task (%@) done of (%s), error (%@)"
+ "%s: instance is nil, can't add it to bundle"
+ "%s: instance is nil, can't remove it from bundle"
+ "%s: publishing progress (%@)"
+ "%s: returning error (%@)"
+ "%s: returning taskID (%@) error (%@)"
+ "%s: volume doesn't support access check operations."
+ "%s:%@:%d:UTF8String returned NULL"
+ "*"
+ "-[FSClient(Private) doneFSCKWithTask:]"
+ "-[FSClient(Private) startFSCKWithDevice:volumes:error:]"
+ "-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke"
+ "-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke_2"
+ "-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke"
+ "-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke_2"
+ "-[FSModuleExtension(Project) fskitdIsClient:]"
+ "-[FSModuleHost(Project) addBundleToEnableModules:]"
+ "-[FSModuleHost(Project) removeBundleFromEnabledModules:]"
+ "-[FSModuleVolume(Project) getAndRemoveItemForFH:]"
+ "-[FSVolumeConnector getFreeSpaceInVolumeWithReplyHandler:]_block_invoke"
+ "-[FSVolumeConnector getIOItemAttributesSubsetData:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke_4"
+ "-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke_6"
+ "/tmp/%@"
+ "@\"FSServerInfo\""
+ "@\"FSServerSessionInfo\""
+ "@\"FSVolume\""
+ "@\"LiveFSSharedMutableBuffer\""
+ "@\"NSNumber\""
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"NSProgress\"48@0:8@\"FSServerInfoTask\"16@\"FSServerURLResource\"24@\"FSTaskOptions\"32^@40"
+ "@\"NSProgress\"48@0:8@\"FSServerSessionInfoTask\"16@\"FSServerURLResource\"24@\"FSTaskOptions\"32^@40"
+ "@\"NSProgress\"48@0:8@\"FSTask\"16@\"FSServerURLResource\"24@\"FSTaskOptions\"32^@40"
+ "@\"NSProgress\"56@0:8@\"FSConnectShareTask\"16@\"FSServerURLResource\"24@\"NSString\"32@\"FSTaskOptions\"40^@48"
+ "@48@0:8@16@24@32^@40"
+ "@56@0:8@16@24@32@40^@48"
+ "A"
+ "Application-Group"
+ "B24@0:8@?16"
+ "Completed with error: %s\n"
+ "FAddInf"
+ "FConHow"
+ "FConUsr"
+ "FIsConn"
+ "FSConnectShareTask"
+ "FSEnumeratedSharePacker"
+ "FSExtra"
+ "FSFlags"
+ "FSHasPw"
+ "FSHiddn"
+ "FSHost"
+ "FSKitCheckContainerStart"
+ "FSKitCheckDone"
+ "FSKitCheckStart"
+ "FSKitCheckUpdate"
+ "FSMachT"
+ "FSOpenSessionParameters"
+ "FSOptns"
+ "FSPassw"
+ "FSPath"
+ "FSPathURLResource:%@"
+ "FSPort"
+ "FSPrntr"
+ "FSSAInf"
+ "FSSDisn"
+ "FSSOpnf"
+ "FSSPxSN"
+ "FSSPxSR"
+ "FSSUIOp"
+ "FSSchem"
+ "FSServerEnumerateSharesParameters"
+ "FSServerInfo"
+ "FSServerInfoTask"
+ "FSServerSessionInfo"
+ "FSServerSessionInfoTask"
+ "FSServerShareInfo"
+ "FSServerURLParameters"
+ "FSServerURLUnaryOperations"
+ "FSSrvOS"
+ "FSSupMT"
+ "FSSupportedSchemes"
+ "FSTask.canc"
+ "FSTaskCanceled"
+ "FSTaskMessageSTDIOWithProgress"
+ "FSUser"
+ "Got device path %@ for fd: %d"
+ "Management"
+ "Message %@ not found in bundle"
+ "Received invalid fd: %d"
+ "T@\"FSServerInfo\",&,V_result"
+ "T@\"FSServerSessionInfo\",&,V_result"
+ "T@\"FSVolume\",&,V_result"
+ "T@\"FSWorkQueue\",R,V_workQueue"
+ "T@\"LiveFSSharedMutableBuffer\",&,V_proxyOfBuffer"
+ "T@\"NSDictionary\",C,V_additionalInfo"
+ "T@\"NSDictionary\",C,V_authenticationInfo"
+ "T@\"NSDictionary\",C,V_extras"
+ "T@\"NSError\",C,V_completedError"
+ "T@\"NSNumber\",C,V_port"
+ "T@\"NSObject<OS_dispatch_group>\",&,V_dispatch_group"
+ "T@\"NSProgress\",&,N"
+ "T@\"NSString\",&,V_domain"
+ "T@\"NSString\",C,V_connectedByUser"
+ "T@\"NSString\",C,V_displayName"
+ "T@\"NSString\",C,V_host"
+ "T@\"NSString\",C,V_machineType"
+ "T@\"NSString\",C,V_options"
+ "T@\"NSString\",C,V_password"
+ "T@\"NSString\",C,V_path"
+ "T@\"NSString\",C,V_proxyServerName"
+ "T@\"NSString\",C,V_proxyServerRealm"
+ "T@\"NSString\",C,V_scheme"
+ "T@\"NSString\",C,V_serverOS"
+ "T@\"NSString\",C,V_supportedMechTypes"
+ "T@\"NSString\",C,V_user"
+ "T@\"NSString\",R,V_applicationGroup"
+ "T@\"NSURL\",R,C,V_url"
+ "T@\"NSURL\",R,GgetProgressURLKey"
+ "T@\"NSXPCConnection\",R"
+ "T@?,C,V_cancellationHandler"
+ "TB,GisAlreadyConnected,V_alreadyConnected"
+ "TB,GisHidden,V_hidden"
+ "TB,GisPrinterShare,V_printerShare"
+ "TB,V_didInitQueues"
+ "TB,V_hasPassword"
+ "TB,V_progressHasShown"
+ "TB,V_progressShowing"
+ "TB,V_taskHasCancellationHandler"
+ "TQ,V_flags"
+ "TQ,V_openFlags"
+ "Testing: just set hasCancellation to %d, we see %d"
+ "Ti,V_concurrency"
+ "Ti,V_twiddleState"
+ "Tq,V_howConnected"
+ "Tq,V_uiOption"
+ "Unable to get device path from fd %d: %s"
+ "_additionalInfo"
+ "_alreadyConnected"
+ "_applicationGroup"
+ "_authenticationInfo"
+ "_cancellationHandler"
+ "_concurrency"
+ "_connectedByUser"
+ "_didInitQueues"
+ "_dispatch_group"
+ "_displayName"
+ "_domain"
+ "_flags"
+ "_hasPassword"
+ "_hidden"
+ "_host"
+ "_howConnected"
+ "_machineType"
+ "_openFlags"
+ "_password"
+ "_path"
+ "_port"
+ "_printerShare"
+ "_progressHasShown"
+ "_progressShowing"
+ "_proxyOfBuffer"
+ "_proxyServerName"
+ "_proxyServerRealm"
+ "_scheme"
+ "_serverOS"
+ "_supportedMechTypes"
+ "_taskHasCancellationHandler"
+ "_twiddleState"
+ "_uiOption"
+ "_updateProviderListForFilteredFSModuleInstances:"
+ "_user"
+ "_workQueue"
+ "addObserver:forKeyPath:options:context:"
+ "additionalInfo"
+ "alreadyConnected"
+ "applicationGroup"
+ "attributes mask is 0x%llx, expected 0x%llx"
+ "authenticationInfo"
+ "cancellationHandler"
+ "capacity"
+ "closeSession:replyHandler:"
+ "composeURL:replyHandler:"
+ "concurrency"
+ "connectedByUser"
+ "connector.%@"
+ "date"
+ "didCompleteWithServerInfo:"
+ "didCompleteWithServerSessionInfo:"
+ "didCompleteWithVolume:"
+ "didInitQueues"
+ "dispatch_group"
+ "displayName"
+ "doneFSCKWithTask:"
+ "doneFSCKWithTask:replyHandler:"
+ "drawTwiddleBar"
+ "enableOpenUnlinkEmulation"
+ "error creating fdWrapper for fd %d(%{public}@), maybe error: %d"
+ "fd/"
+ "fillProgressBar:"
+ "formatWithOptions: encountered on connect error!"
+ "fractionCompleted"
+ "fs_all_of:"
+ "fs_any_of:"
+ "getDeviceName:"
+ "getFreeSpaceInVolumeWithReplyHandler:"
+ "getIOItemAttributesSubsetData:replyHandler:"
+ "getProgressURLKey"
+ "hasCancellationHandler"
+ "hasMinimalRequiredAttributes"
+ "hasPassword"
+ "hidden"
+ "hideProgress"
+ "hideProgressLocked"
+ "host"
+ "howConnected"
+ "i24@0:8r*16"
+ "initAsSecureURL:readOnly:"
+ "initAsSecureURL:writable:"
+ "initProxyFrom:"
+ "initQueues"
+ "initWithURL:readOnly:"
+ "initWithURL:writable:"
+ "isAlreadyConnected"
+ "isFileURL"
+ "isHidden"
+ "isIndeterminate"
+ "isPrinterShare"
+ "isValidModuleIdentifier:withError:"
+ "machineType"
+ "mp"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "openFlags"
+ "packShareWithName:info:"
+ "parseURL:replyHandler:"
+ "password"
+ "port"
+ "precomposedStringWithCanonicalMapping"
+ "printAboveProgress:"
+ "printerShare"
+ "progressHasShown"
+ "progressShowing"
+ "progressURLKey"
+ "progress_buffer"
+ "proxyOfBuffer"
+ "proxyServerName"
+ "proxyServerRealm"
+ "publish"
+ "r"
+ "removeObserver:forKeyPath:context:"
+ "scheme"
+ "screen_width"
+ "serverOS"
+ "setAdditionalInfo:"
+ "setAlreadyConnected:"
+ "setAuthenticationInfo:"
+ "setConcurrency:"
+ "setConnectedByUser:"
+ "setDidInitQueues:"
+ "setDispatch_group:"
+ "setDisplayName:"
+ "setDomain:"
+ "setHasPassword:"
+ "setHidden:"
+ "setHost:"
+ "setHowConnected:"
+ "setMachineType:"
+ "setOpenFlags:"
+ "setOptions:"
+ "setPassword:"
+ "setPath:"
+ "setPort:"
+ "setPrinterShare:"
+ "setProgressHasShown:"
+ "setProgressShowing:"
+ "setProxyOfBuffer:"
+ "setProxyServerName:"
+ "setProxyServerRealm:"
+ "setResult:"
+ "setScheme:"
+ "setServerOS:"
+ "setSupportedMechTypes:"
+ "setTaskHasCancellationHandler:"
+ "setTwiddleState:"
+ "setUiOption:"
+ "setUser:"
+ "setUserInfoObject:forKey:"
+ "showProgress"
+ "showProgressLocked"
+ "startConnectingShareWithTask:server:share:options:error:"
+ "startEnumeratingSharesWithTask:url:options:error:"
+ "startFSCKWithDevice:volumes:error:"
+ "startFSCKWithDevice:volumes:replyHandler:"
+ "startOpeningSessionWithTask:url:options:error:"
+ "startServerInfoFetchWithTask:url:options:error:"
+ "supportedMechTypes"
+ "taskHasCancellationHandler"
+ "terminateLocked"
+ "timeIntervalSinceDate:"
+ "twiddleState"
+ "uiOption"
+ "unpublish"
+ "updateTimer_block_invoke"
+ "user"
+ "v20@0:8f16"
+ "v32@0:8@\"FSServerURLParameters\"16@?<v@?@\"NSURL\"@\"NSError\">24"
+ "v32@0:8@\"FSServerURLResource\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"FSServerURLParameters\"@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSUUID\"@\"NSError\">32"
+ "v48@0:8@\"FSTaskOptionsBundle\"16@\"FSMessageConnection\"24@\"NSUUID\"32@?<v@?@\"FSTaskDescription\"@\"NSError\">40"
+ "v48@0:8@16@24@32^v40"
+ "v56@0:8@\"FSFileHandle\"16@\"FSFileName\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"FSFileHandle\"16Q24@\"FSMutableFileDataBuffer\"32Q40@?<v@?iQ@\"NSData\">48"
+ "v56@0:8@\"FSFileHandle\"16Q24@\"NSData\"32Q40@?<v@?iQ@\"NSData\"@\"NSData\">48"
+ "v68@0:8@\"FSFileHandle\"16{_NSRange=QQ}24i40Q44Q52@?<v@?i@\"NSData\">60"
+ "vma"
+ "workQueue"
+ "|%s|\r"
+ "|/-\\"
- "%s given listener %@, connection %@"
- "%s got listener %@"
- "%s got listener %@ endpoint %@"
- "%s: delegate has checkResource:options:connection:taskID:replyHandler: method, try that"
- "-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]"
- "-[FSModuleExtension fskitdIsClient:]"
- "-[FSTaskProgressConnector initWithProgress:description:]"
- "-[FSTaskProgressConnector listener:shouldAcceptNewConnection:]"
- "-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke_3"
- "-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke_3"
- "@\"FSTaskProgressConnector\""
- "@\"NSMutableSet\""
- "@\"NSProgress\"24@0:8@?<v@?@\"NSError\">16"
- "@24@0:8^@16"
- "@36@0:8i16@20@28"
- "@40@0:8^v16q24Q32"
- "@56@0:8^v16q24Q32r^{?=qQ}40q48"
- "FSEntityIdentifier_private"
- "FSKit_private"
- "FSModule %{public}@ check: did NOT call reply()"
- "FSModule %{public}@ formatResource: did NOT call reply()"
- "FSTaskProgress"
- "FSTaskProgressConnector"
- "FSTaskProgressXPC"
- "FSTaskProgressXPCProtocol"
- "Localized key '%@' missing from table '%@' (bundlePath:%@)"
- "Progress from getProgress %u units of %u, isFinished %d"
- "T@\"FSEntityIdentifier\",R,C"
- "T@\"FSFileName\",C"
- "T@\"FSTaskDescription\",C,V_taskDesc"
- "T@\"FSTaskDescription\",R,C,V_initialDescription"
- "T@\"FSTaskProgressConnector\",&,V_connector"
- "T@\"FSVolumeIdentifier\",&"
- "T@\"NSMutableSet\",&,V_pendingReplyBlocks"
- "T@\"NSObject<OS_dispatch_queue>\",&,N"
- "T@\"NSProgress\",&,V_progress"
- "T@\"NSProgress\",R,&,V_progress"
- "T@\"NSURL\",R,C,V_URL"
- "T@\"NSXPCConnection\",&,V_ourConn"
- "T@\"NSXPCListener\",&,V_listener"
- "T@\"NSXPCListenerEndpoint\",R,&,V_endpoint"
- "_URL"
- "_connector"
- "_initialDescription"
- "_ourConn"
- "_pendingReplyBlocks"
- "_renameWorkQueue"
- "_taskDesc"
- "_updateProviderListForFilteredFSModileInstances:"
- "browseServerResource:replyHandler:"
- "check: encountered connect error!"
- "checkResource:options:connection:taskID:progress:replyHandler:"
- "checkResource:options:connection:taskID:replyHandler:"
- "checkVolume:options:auditToken:connection:replyHandler:"
- "checkVolume:options:connection:replyHandler:"
- "com.apple.fskit.rename.queue"
- "completed:reply:"
- "configurationForDefaultInstanceOf:"
- "configurationForDefaultInstanceOfBundle:"
- "connector"
- "constructFromListener:description:replyHandler:"
- "containerIdentifier"
- "delayedMetadataWriteFrom:startingAt:length:"
- "enumerateOptionsWithBlock:"
- "error creating fdWrapper for fd %d, maybe error: %d"
- "formatResource: encountered on connect error!"
- "formatResource:options:connection:taskID:progress:replyHandler:"
- "formatResource:options:connection:taskID:reply"
- "formatResource:options:connection:taskID:replyHandler:"
- "fs_entityIdentifier"
- "fskit_errorWithPOSIXCode:itemURL:debugDescription:"
- "fskit_isFSKitError:"
- "getFSProgressForTask:replyHandler:"
- "getFreeSpaceInVolume"
- "getProgress returned error %@"
- "getProgress returned success"
- "getProgress returning progress with %u of %u units done"
- "getProgress:"
- "getProgressPortForTask:replyHandler:"
- "initAsSecureURL:readonly:"
- "initWithBase64:"
- "initWithBase64Encoding:"
- "initWithProgress:description:"
- "initWithURL:readonly:"
- "initialDescription"
- "installedExtensionsWithError:"
- "isValidModuleIdentifier:WithError:"
- "loadResource:shortName:options:synchronousReply:"
- "metadataClear:wait:"
- "metadataFlush"
- "metadataPurge:"
- "metadataReadInto:startingAt:length:"
- "metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:"
- "metadataWriteFrom:startingAt:length:"
- "metadataWriteFrom:startingAt:length:completionHandler:"
- "newForProgress:description:"
- "normnal blockReply just did fire, passed rv %@"
- "ourConn"
- "pendingReplyBlocks"
- "probeResource:usingBundle:reply:"
- "probeServerAddress:replyHandler:"
- "proxyResourceForBSDName:writable:"
- "remote proxy blockReply about to fire"
- "remote proxy object error %@"
- "renameWorkQueue"
- "setConnector:"
- "setListener:"
- "setOurConn:"
- "setPausingHandler:"
- "setPendingReplyBlocks:"
- "setRenameWorkQueue:"
- "setTaskDesc:"
- "setupSyncronously"
- "synchronousReadInto:startingAt:length:reply:"
- "synchronousReadInto:startingAt:length:replyHandler:"
- "taskDesc"
- "v24@?0@\"FSTaskProgress\"8@\"NSError\"16"
- "v32@0:8@\"FSServerURLResource\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSXPCListenerEndpoint\"@\"FSTaskDescription\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">24"
- "v32@?0@\"NSXPCListenerEndpoint\"8@\"FSTaskDescription\"16@\"NSError\"24"
- "v48@0:8@\"FSTaskOptionsBundle\"16@\"FSMessageConnection\"24@\"NSUUID\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"FSTaskOptionsBundle\"24@\"FSMessageConnection\"32@?<v@?@\"NSUUID\"@\"NSError\">40"
- "v56@0:8@\"FSFileHandle\"16@\"FSFileName\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSData\">48"
- "v56@0:8@\"FSFileHandle\"16Q24@\"FSMutableFileDataBuffer\"32Q40@?<v@?iQ>48"
- "v56@0:8@\"FSFileHandle\"16Q24@\"NSData\"32Q40@?<v@?iQ@\"NSData\">48"
- "v56@0:8@\"FSResource\"16@\"FSTaskOptionsBundle\"24@\"FSMessageConnection\"32@\"NSUUID\"40@?<v@?@\"NSError\">48"
- "v68@0:8@\"FSFileHandle\"16{_NSRange=QQ}24i40Q44Q52@?<v@?i>60"
- "v80@0:8@\"NSString\"16@\"FSTaskOptionsBundle\"24{?=[8I]}32@\"FSMessageConnection\"64@?<v@?@\"NSUUID\"@\"NSError\">72"
- "v80@0:8@16@24{?=[8I]}32@64@?72"
- "validateVolumeName:usingBundle:volumeID:reply:"
- "volumeIdentifierDescription:"
- "writeMetaAsync:buffer:offset:length:"

```
