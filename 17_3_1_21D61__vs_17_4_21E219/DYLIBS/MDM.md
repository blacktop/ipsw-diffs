## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-3.26.4.1.0
-  __TEXT.__text: 0x3af34
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x2138
+3.26.5.12.0
+  __TEXT.__text: 0x3fa34
+  __TEXT.__auth_stubs: 0xc00
+  __TEXT.__objc_methlist: 0x2a18
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0xa4c
-  __TEXT.__cstring: 0x3c33
-  __TEXT.__oslogstring: 0x42f8
+  __TEXT.__gcc_except_tab: 0xca0
+  __TEXT.__cstring: 0x3fb0
+  __TEXT.__oslogstring: 0x4660
   __TEXT.__dlopen_cstrs: 0x55
-  __TEXT.__unwind_info: 0xb68
-  __TEXT.__objc_classname: 0x37c
-  __TEXT.__objc_methname: 0xa04c
-  __TEXT.__objc_methtype: 0x10b8
-  __TEXT.__objc_stubs: 0x8800
-  __DATA_CONST.__got: 0x988
-  __DATA_CONST.__const: 0x1568
-  __DATA_CONST.__objc_classlist: 0xd0
+  __TEXT.__unwind_info: 0xd7c
+  __TEXT.__objc_classname: 0x5ad
+  __TEXT.__objc_methname: 0xb5f7
+  __TEXT.__objc_methtype: 0x14ac
+  __TEXT.__objc_stubs: 0x9300
+  __DATA_CONST.__got: 0x9b8
+  __DATA_CONST.__const: 0x1738
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3758
-  __DATA_CONST.__objc_selrefs: 0x2480
+  __DATA_CONST.__objc_const: 0x4708
+  __DATA_CONST.__objc_selrefs: 0x2788
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x5e0
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__objc_const: 0xa30
-  __AUTH_CONST.__cfstring: 0x4320
+  __AUTH_CONST.__objc_const: 0x12a0
+  __AUTH_CONST.__cfstring: 0x47a0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH_CONST.__auth_got: 0x5b8
-  __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x560
-  __DATA.__objc_superrefs: 0x50
-  __DATA.__objc_ivar: 0x1a0
-  __DATA.__data: 0x5a0
-  __DATA.__bss: 0x198
+  __AUTH_CONST.__auth_got: 0x610
+  __AUTH.__objc_data: 0xbe0
+  __DATA.__objc_ivar: 0x208
+  __DATA.__data: 0x660
+  __DATA.__bss: 0x1a8
   __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
   - /System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices
   - /System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement
+  - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel
+  - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /System/Library/PrivateFrameworks/StoreServices.framework/StoreServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 956
-  Symbols:   4397
-  CStrings:  2618
+  Functions: 1148
+  Symbols:   5074
+  CStrings:  2880
 
Symbols:
+ +[MDMDeclarativeManagementCommand _isSupervised]
+ +[MDMRequestBase requestType]
+ +[MDMRequestBase requiredAccessRights]
+ +[MDMRequestClasses classForRequestType:]
+ +[MDMRequestClearRestrictionsPasswordCommand requestType]
+ +[MDMRequestClearRestrictionsPasswordCommand request]
+ +[MDMRequestClearRestrictionsPasswordCommand requiredAccessRights]
+ +[MDMRequestDeviceEraseCommand requestType]
+ +[MDMRequestDeviceEraseCommand requestWithPreserveDataPlan:disallowProximitySetup:PIN:obliterationBehavior:returnToService:]
+ +[MDMRequestDeviceEraseCommand requiredAccessRights]
+ +[MDMRequestDeviceEraseCommand_ReturnToService allowedCommandKeys]
+ +[MDMRequestDeviceEraseCommand_ReturnToService buildRequiredOnlyWithEnabled:]
+ +[MDMRequestDeviceEraseCommand_ReturnToService buildWithEnabled:wiFiProfileData:mdmProfileData:]
+ +[MDMRequestDeviceLocationCommand requestType]
+ +[MDMRequestDeviceLocationCommand request]
+ +[MDMRequestDeviceLocationCommand requiredAccessRights]
+ +[MDMRequestDeviceLockCommand requestType]
+ +[MDMRequestDeviceLockCommand requestWithMessage:phoneNumber:PIN:]
+ +[MDMRequestDeviceLockCommand requiredAccessRights]
+ +[MDMRequestDeviceRestartCommand requestType]
+ +[MDMRequestDeviceRestartCommand requestWithRebuildKernelCache:kextPaths:notifyUser:]
+ +[MDMRequestDeviceRestartCommand requiredAccessRights]
+ +[MDMRequestDeviceShutDownCommand requestType]
+ +[MDMRequestDeviceShutDownCommand request]
+ +[MDMRequestDeviceShutDownCommand requiredAccessRights]
+ +[MDMRequestDisableMDMLostModeCommand requestType]
+ +[MDMRequestDisableMDMLostModeCommand request]
+ +[MDMRequestDisableMDMLostModeCommand requiredAccessRights]
+ +[MDMRequestEnableMDMLostModeCommand requestType]
+ +[MDMRequestEnableMDMLostModeCommand requestWithMessage:phoneNumber:footnote:]
+ +[MDMRequestEnableMDMLostModeCommand requiredAccessRights]
+ +[MDMRequestLogOutUserCommand requestType]
+ +[MDMRequestLogOutUserCommand request]
+ +[MDMRequestLogOutUserCommand requiredAccessRights]
+ +[MDMRequestPlayLostModeSoundCommand requestType]
+ +[MDMRequestPlayLostModeSoundCommand request]
+ +[MDMRequestPlayLostModeSoundCommand requiredAccessRights]
+ +[MDMRequestSecurityInformationCommand requestType]
+ +[MDMRequestSecurityInformationCommand request]
+ +[MDMRequestSecurityInformationCommand requiredAccessRights]
+ +[MDMRequestUserListCommand requestType]
+ +[MDMRequestUserListCommand request]
+ +[MDMRequestUserListCommand requiredAccessRights]
+ -[MDMLostDeviceLocationManager .cxx_destruct]
+ -[MDMLostDeviceLocationManager _cleanupAfterResponseFromLocationManagerOrTimeout]
+ -[MDMLostDeviceLocationManager _updateLostModeFileForOriginator:]
+ -[MDMLostDeviceLocationManager clearLastLocationRequestedDate]
+ -[MDMLostDeviceLocationManager completionBlock]
+ -[MDMLostDeviceLocationManager getCurrentLocationForOriginator:completion:]
+ -[MDMLostDeviceLocationManager init]
+ -[MDMLostDeviceLocationManager lastLocationRequestedDateMessage]
+ -[MDMLostDeviceLocationManager locationManager:didFailWithError:]
+ -[MDMLostDeviceLocationManager locationManager:didUpdateLocations:]
+ -[MDMLostDeviceLocationManager locationManager]
+ -[MDMLostDeviceLocationManager originator]
+ -[MDMLostDeviceLocationManager queue]
+ -[MDMLostDeviceLocationManager setCompletionBlock:]
+ -[MDMLostDeviceLocationManager setLocationManager:]
+ -[MDMLostDeviceLocationManager setOriginator:]
+ -[MDMLostDeviceLocationManager setTimeoutTimerDispatchSource:]
+ -[MDMLostDeviceLocationManager timeoutTimerDispatchSource]
+ -[MDMParser _appAttributesWithRequestedAttributes:]
+ -[MDMParser _appManagementFlagsWithRequestedFlags:]
+ -[MDMParser _isChlorineEligible]
+ -[MDMParser _isPurchaseMethodAllowed:onUserEnrollment:]
+ -[MDMParser _setAppAnalyticsEnabled:]
+ -[MDMParser _setDiagnosticSubmissionEnabled:]
+ -[MDMParser didInitiateSwitchUser]
+ -[MDMParser originator]
+ -[MDMParser willTerminateProcess:]
+ -[MDMRequestBase .cxx_destruct]
+ -[MDMRequestBase _notAuthorizedError]
+ -[MDMRequestBase _validateAccessRights:requiredAccessRights:error:]
+ -[MDMRequestBase accessRights]
+ -[MDMRequestBase channelType]
+ -[MDMRequestBase delegate]
+ -[MDMRequestBase isRequestAllowedWithError:]
+ -[MDMRequestBase isUserEnrollment]
+ -[MDMRequestBase processRequest:completionHandler:]
+ -[MDMRequestBase setAccessRights:]
+ -[MDMRequestBase setChannelType:]
+ -[MDMRequestBase setDelegate:]
+ -[MDMRequestBase setIsUserEnrollment:]
+ -[MDMRequestBase shouldBlockUserSwitch]
+ -[MDMRequestClearRestrictionsPasswordCommand copyWithZone:]
+ -[MDMRequestClearRestrictionsPasswordCommand loadFromDictionary:serializationType:error:]
+ -[MDMRequestClearRestrictionsPasswordCommand serializeWithType:]
+ -[MDMRequestClearRestrictionsPasswordCommand(Handler) processRequest:completionHandler:]
+ -[MDMRequestDeviceEraseCommand .cxx_destruct]
+ -[MDMRequestDeviceEraseCommand commandDisallowProximitySetup]
+ -[MDMRequestDeviceEraseCommand commandObliterationBehavior]
+ -[MDMRequestDeviceEraseCommand commandPIN]
+ -[MDMRequestDeviceEraseCommand commandPreserveDataPlan]
+ -[MDMRequestDeviceEraseCommand commandReturnToService]
+ -[MDMRequestDeviceEraseCommand copyWithZone:]
+ -[MDMRequestDeviceEraseCommand loadFromDictionary:serializationType:error:]
+ -[MDMRequestDeviceEraseCommand serializeWithType:]
+ -[MDMRequestDeviceEraseCommand setCommandDisallowProximitySetup:]
+ -[MDMRequestDeviceEraseCommand setCommandObliterationBehavior:]
+ -[MDMRequestDeviceEraseCommand setCommandPIN:]
+ -[MDMRequestDeviceEraseCommand setCommandPreserveDataPlan:]
+ -[MDMRequestDeviceEraseCommand setCommandReturnToService:]
+ -[MDMRequestDeviceEraseCommand(Handler) _eraseDeviceActivationLockIsOnError]
+ -[MDMRequestDeviceEraseCommand(Handler) _eraseDeviceFailedToEraseErrorWithUnderlayingError:]
+ -[MDMRequestDeviceEraseCommand(Handler) _eraseDeviceInvalidMDMProfileErrorWithUnderlayingError:]
+ -[MDMRequestDeviceEraseCommand(Handler) _eraseDeviceInvalidWiFiProfileErrorWithUnderlayingError:]
+ -[MDMRequestDeviceEraseCommand(Handler) _eraseDeviceMissingMDMProfileError]
+ -[MDMRequestDeviceEraseCommand(Handler) _eraseDeviceNotSupporttedError]
+ -[MDMRequestDeviceEraseCommand(Handler) _eraseDeviceNotSupporttedOnSharedIPadError]
+ -[MDMRequestDeviceEraseCommand(Handler) _eraseDeviceNotTeslaEnrolledError]
+ -[MDMRequestDeviceEraseCommand(Handler) _eraseDeviceProvisionallyEnrolledError]
+ -[MDMRequestDeviceEraseCommand(Handler) processRequest:completionHandler:]
+ -[MDMRequestDeviceEraseCommand_ReturnToService .cxx_destruct]
+ -[MDMRequestDeviceEraseCommand_ReturnToService commandEnabled]
+ -[MDMRequestDeviceEraseCommand_ReturnToService commandMDMProfileData]
+ -[MDMRequestDeviceEraseCommand_ReturnToService commandWiFiProfileData]
+ -[MDMRequestDeviceEraseCommand_ReturnToService copyWithZone:]
+ -[MDMRequestDeviceEraseCommand_ReturnToService loadFromDictionary:serializationType:error:]
+ -[MDMRequestDeviceEraseCommand_ReturnToService serializeWithType:]
+ -[MDMRequestDeviceEraseCommand_ReturnToService setCommandEnabled:]
+ -[MDMRequestDeviceEraseCommand_ReturnToService setCommandMDMProfileData:]
+ -[MDMRequestDeviceEraseCommand_ReturnToService setCommandWiFiProfileData:]
+ -[MDMRequestDeviceLocationCommand copyWithZone:]
+ -[MDMRequestDeviceLocationCommand loadFromDictionary:serializationType:error:]
+ -[MDMRequestDeviceLocationCommand serializeWithType:]
+ -[MDMRequestDeviceLocationCommand(Handler) processRequest:completionHandler:]
+ -[MDMRequestDeviceLockCommand .cxx_destruct]
+ -[MDMRequestDeviceLockCommand commandMessage]
+ -[MDMRequestDeviceLockCommand commandPIN]
+ -[MDMRequestDeviceLockCommand commandPhoneNumber]
+ -[MDMRequestDeviceLockCommand copyWithZone:]
+ -[MDMRequestDeviceLockCommand loadFromDictionary:serializationType:error:]
+ -[MDMRequestDeviceLockCommand serializeWithType:]
+ -[MDMRequestDeviceLockCommand setCommandMessage:]
+ -[MDMRequestDeviceLockCommand setCommandPIN:]
+ -[MDMRequestDeviceLockCommand setCommandPhoneNumber:]
+ -[MDMRequestDeviceLockCommand(Handler) processRequest:completionHandler:]
+ -[MDMRequestDeviceRestartCommand .cxx_destruct]
+ -[MDMRequestDeviceRestartCommand commandKextPaths]
+ -[MDMRequestDeviceRestartCommand commandNotifyUser]
+ -[MDMRequestDeviceRestartCommand commandRebuildKernelCache]
+ -[MDMRequestDeviceRestartCommand copyWithZone:]
+ -[MDMRequestDeviceRestartCommand loadFromDictionary:serializationType:error:]
+ -[MDMRequestDeviceRestartCommand serializeWithType:]
+ -[MDMRequestDeviceRestartCommand setCommandKextPaths:]
+ -[MDMRequestDeviceRestartCommand setCommandNotifyUser:]
+ -[MDMRequestDeviceRestartCommand setCommandRebuildKernelCache:]
+ -[MDMRequestDeviceRestartCommand(Handler) processRequest:completionHandler:]
+ -[MDMRequestDeviceShutDownCommand copyWithZone:]
+ -[MDMRequestDeviceShutDownCommand loadFromDictionary:serializationType:error:]
+ -[MDMRequestDeviceShutDownCommand serializeWithType:]
+ -[MDMRequestDeviceShutDownCommand(Handler) processRequest:completionHandler:]
+ -[MDMRequestDisableMDMLostModeCommand copyWithZone:]
+ -[MDMRequestDisableMDMLostModeCommand loadFromDictionary:serializationType:error:]
+ -[MDMRequestDisableMDMLostModeCommand serializeWithType:]
+ -[MDMRequestDisableMDMLostModeCommand(Handler) processRequest:completionHandler:]
+ -[MDMRequestEnableMDMLostModeCommand .cxx_destruct]
+ -[MDMRequestEnableMDMLostModeCommand commandFootnote]
+ -[MDMRequestEnableMDMLostModeCommand commandMessage]
+ -[MDMRequestEnableMDMLostModeCommand commandPhoneNumber]
+ -[MDMRequestEnableMDMLostModeCommand copyWithZone:]
+ -[MDMRequestEnableMDMLostModeCommand loadFromDictionary:serializationType:error:]
+ -[MDMRequestEnableMDMLostModeCommand serializeWithType:]
+ -[MDMRequestEnableMDMLostModeCommand setCommandFootnote:]
+ -[MDMRequestEnableMDMLostModeCommand setCommandMessage:]
+ -[MDMRequestEnableMDMLostModeCommand setCommandPhoneNumber:]
+ -[MDMRequestEnableMDMLostModeCommand(Handler) processRequest:completionHandler:]
+ -[MDMRequestLogOutUserCommand copyWithZone:]
+ -[MDMRequestLogOutUserCommand loadFromDictionary:serializationType:error:]
+ -[MDMRequestLogOutUserCommand serializeWithType:]
+ -[MDMRequestLogOutUserCommand(Handler) processRequest:completionHandler:]
+ -[MDMRequestLogOutUserCommand(Handler) shouldBlockUserSwitch]
+ -[MDMRequestPlayLostModeSoundCommand copyWithZone:]
+ -[MDMRequestPlayLostModeSoundCommand loadFromDictionary:serializationType:error:]
+ -[MDMRequestPlayLostModeSoundCommand serializeWithType:]
+ -[MDMRequestPlayLostModeSoundCommand(Handler) processRequest:completionHandler:]
+ -[MDMRequestSecurityInformationCommand copyWithZone:]
+ -[MDMRequestSecurityInformationCommand loadFromDictionary:serializationType:error:]
+ -[MDMRequestSecurityInformationCommand serializeWithType:]
+ -[MDMRequestSecurityInformationCommand(Handler) processRequest:completionHandler:]
+ -[MDMRequestUserListCommand copyWithZone:]
+ -[MDMRequestUserListCommand loadFromDictionary:serializationType:error:]
+ -[MDMRequestUserListCommand serializeWithType:]
+ -[MDMRequestUserListCommand(Handler) processRequest:completionHandler:]
+ -[MDMWallpaperUtilities _updateWallpaperConfiguraitonWithUUID:updates:completionHandler:]
+ -[MDMWallpaperUtilities _updateWallpaperConfiguraitonWithUUID:updates:retryCount:completionHandler:]
+ GCC_except_table15
+ GCC_except_table170
+ GCC_except_table188
+ GCC_except_table197
+ GCC_except_table208
+ GCC_except_table212
+ GCC_except_table222
+ GCC_except_table226
+ GCC_except_table242
+ GCC_except_table6
+ GCC_except_table67
+ _DMCLocationErrorDomain
+ _DMCSystemLostModeRequestPath
+ _MDMRequestDeviceEraseCommand_ObliterationBehavior_always
+ _MDMRequestDeviceEraseCommand_ObliterationBehavior_default
+ _MDMRequestDeviceEraseCommand_ObliterationBehavior_doNotObliterate
+ _MDMRequestDeviceEraseCommand_ObliterationBehavior_obliterateWithWarning
+ _NSCocoaErrorDomain
+ _NSFileProtectionKey
+ _NSFileProtectionNone
+ _NSURLIsExcludedFromBackupKey
+ _OBJC_CLASS_$_CLEmergencyEnablementAssertion
+ _OBJC_CLASS_$_CLLocationManager
+ _OBJC_CLASS_$_DMCDateFormatterFactory
+ _OBJC_CLASS_$_DMCReturnToServiceHelper
+ _OBJC_CLASS_$_FBSShutdownOptions
+ _OBJC_CLASS_$_FBSSystemService
+ _OBJC_CLASS_$_FMDLostModeInfo
+ _OBJC_CLASS_$_MCDeviceCapabilities
+ _OBJC_CLASS_$_MDMLostDeviceLocationManager
+ _OBJC_CLASS_$_MDMRequestBase
+ _OBJC_CLASS_$_MDMRequestClasses
+ _OBJC_CLASS_$_MDMRequestClearRestrictionsPasswordCommand
+ _OBJC_CLASS_$_MDMRequestDeviceEraseCommand
+ _OBJC_CLASS_$_MDMRequestDeviceEraseCommand_ReturnToService
+ _OBJC_CLASS_$_MDMRequestDeviceLocationCommand
+ _OBJC_CLASS_$_MDMRequestDeviceLockCommand
+ _OBJC_CLASS_$_MDMRequestDeviceRestartCommand
+ _OBJC_CLASS_$_MDMRequestDeviceShutDownCommand
+ _OBJC_CLASS_$_MDMRequestDisableMDMLostModeCommand
+ _OBJC_CLASS_$_MDMRequestEnableMDMLostModeCommand
+ _OBJC_CLASS_$_MDMRequestLogOutUserCommand
+ _OBJC_CLASS_$_MDMRequestPlayLostModeSoundCommand
+ _OBJC_CLASS_$_MDMRequestSecurityInformationCommand
+ _OBJC_CLASS_$_MDMRequestUserListCommand
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSFileCoordinator
+ _OBJC_CLASS_$_RMModelPayloadBase
+ _OBJC_CLASS_$_STManagementState
+ _OBJC_CLASS_$_UMUserManager
+ _OBJC_IVAR_$_MDMLostDeviceLocationManager._completionBlock
+ _OBJC_IVAR_$_MDMLostDeviceLocationManager._locationManager
+ _OBJC_IVAR_$_MDMLostDeviceLocationManager._originator
+ _OBJC_IVAR_$_MDMLostDeviceLocationManager._queue
+ _OBJC_IVAR_$_MDMLostDeviceLocationManager._timeoutTimerDispatchSource
+ _OBJC_IVAR_$_MDMRequestBase._accessRights
+ _OBJC_IVAR_$_MDMRequestBase._channelType
+ _OBJC_IVAR_$_MDMRequestBase._delegate
+ _OBJC_IVAR_$_MDMRequestBase._isUserEnrollment
+ _OBJC_IVAR_$_MDMRequestDeviceEraseCommand._commandDisallowProximitySetup
+ _OBJC_IVAR_$_MDMRequestDeviceEraseCommand._commandObliterationBehavior
+ _OBJC_IVAR_$_MDMRequestDeviceEraseCommand._commandPIN
+ _OBJC_IVAR_$_MDMRequestDeviceEraseCommand._commandPreserveDataPlan
+ _OBJC_IVAR_$_MDMRequestDeviceEraseCommand._commandReturnToService
+ _OBJC_IVAR_$_MDMRequestDeviceEraseCommand_ReturnToService._commandEnabled
+ _OBJC_IVAR_$_MDMRequestDeviceEraseCommand_ReturnToService._commandMDMProfileData
+ _OBJC_IVAR_$_MDMRequestDeviceEraseCommand_ReturnToService._commandWiFiProfileData
+ _OBJC_IVAR_$_MDMRequestDeviceLockCommand._commandMessage
+ _OBJC_IVAR_$_MDMRequestDeviceLockCommand._commandPIN
+ _OBJC_IVAR_$_MDMRequestDeviceLockCommand._commandPhoneNumber
+ _OBJC_IVAR_$_MDMRequestDeviceRestartCommand._commandKextPaths
+ _OBJC_IVAR_$_MDMRequestDeviceRestartCommand._commandNotifyUser
+ _OBJC_IVAR_$_MDMRequestDeviceRestartCommand._commandRebuildKernelCache
+ _OBJC_IVAR_$_MDMRequestEnableMDMLostModeCommand._commandFootnote
+ _OBJC_IVAR_$_MDMRequestEnableMDMLostModeCommand._commandMessage
+ _OBJC_IVAR_$_MDMRequestEnableMDMLostModeCommand._commandPhoneNumber
+ _OBJC_METACLASS_$_MDMLostDeviceLocationManager
+ _OBJC_METACLASS_$_MDMRequestBase
+ _OBJC_METACLASS_$_MDMRequestClasses
+ _OBJC_METACLASS_$_MDMRequestClearRestrictionsPasswordCommand
+ _OBJC_METACLASS_$_MDMRequestDeviceEraseCommand
+ _OBJC_METACLASS_$_MDMRequestDeviceEraseCommand_ReturnToService
+ _OBJC_METACLASS_$_MDMRequestDeviceLocationCommand
+ _OBJC_METACLASS_$_MDMRequestDeviceLockCommand
+ _OBJC_METACLASS_$_MDMRequestDeviceRestartCommand
+ _OBJC_METACLASS_$_MDMRequestDeviceShutDownCommand
+ _OBJC_METACLASS_$_MDMRequestDisableMDMLostModeCommand
+ _OBJC_METACLASS_$_MDMRequestEnableMDMLostModeCommand
+ _OBJC_METACLASS_$_MDMRequestLogOutUserCommand
+ _OBJC_METACLASS_$_MDMRequestPlayLostModeSoundCommand
+ _OBJC_METACLASS_$_MDMRequestSecurityInformationCommand
+ _OBJC_METACLASS_$_MDMRequestUserListCommand
+ _OBJC_METACLASS_$_RMModelPayloadBase
+ _SBLockDevice
+ _SBSSpringBoardServerPort
+ __OBJC_$_CLASS_METHODS_MDMRequestBase
+ __OBJC_$_CLASS_METHODS_MDMRequestClasses
+ __OBJC_$_CLASS_METHODS_MDMRequestClearRestrictionsPasswordCommand(Handler)
+ __OBJC_$_CLASS_METHODS_MDMRequestDeviceEraseCommand(Handler)
+ __OBJC_$_CLASS_METHODS_MDMRequestDeviceEraseCommand_ReturnToService
+ __OBJC_$_CLASS_METHODS_MDMRequestDeviceLocationCommand(Handler)
+ __OBJC_$_CLASS_METHODS_MDMRequestDeviceLockCommand(Handler)
+ __OBJC_$_CLASS_METHODS_MDMRequestDeviceRestartCommand(Handler)
+ __OBJC_$_CLASS_METHODS_MDMRequestDeviceShutDownCommand(Handler)
+ __OBJC_$_CLASS_METHODS_MDMRequestDisableMDMLostModeCommand(Handler)
+ __OBJC_$_CLASS_METHODS_MDMRequestEnableMDMLostModeCommand(Handler)
+ __OBJC_$_CLASS_METHODS_MDMRequestLogOutUserCommand(Handler)
+ __OBJC_$_CLASS_METHODS_MDMRequestPlayLostModeSoundCommand(Handler)
+ __OBJC_$_CLASS_METHODS_MDMRequestSecurityInformationCommand(Handler)
+ __OBJC_$_CLASS_METHODS_MDMRequestUserListCommand(Handler)
+ __OBJC_$_CLASS_PROP_LIST_MDMRequestBase
+ __OBJC_$_CLASS_PROP_LIST_MDMRequestDeviceEraseCommand_ReturnToService
+ __OBJC_$_INSTANCE_METHODS_MDMLostDeviceLocationManager
+ __OBJC_$_INSTANCE_METHODS_MDMRequestBase
+ __OBJC_$_INSTANCE_METHODS_MDMRequestClearRestrictionsPasswordCommand(Handler)
+ __OBJC_$_INSTANCE_METHODS_MDMRequestDeviceEraseCommand(Handler)
+ __OBJC_$_INSTANCE_METHODS_MDMRequestDeviceEraseCommand_ReturnToService
+ __OBJC_$_INSTANCE_METHODS_MDMRequestDeviceLocationCommand(Handler)
+ __OBJC_$_INSTANCE_METHODS_MDMRequestDeviceLockCommand(Handler)
+ __OBJC_$_INSTANCE_METHODS_MDMRequestDeviceRestartCommand(Handler)
+ __OBJC_$_INSTANCE_METHODS_MDMRequestDeviceShutDownCommand(Handler)
+ __OBJC_$_INSTANCE_METHODS_MDMRequestDisableMDMLostModeCommand(Handler)
+ __OBJC_$_INSTANCE_METHODS_MDMRequestEnableMDMLostModeCommand(Handler)
+ __OBJC_$_INSTANCE_METHODS_MDMRequestLogOutUserCommand(Handler)
+ __OBJC_$_INSTANCE_METHODS_MDMRequestPlayLostModeSoundCommand(Handler)
+ __OBJC_$_INSTANCE_METHODS_MDMRequestSecurityInformationCommand(Handler)
+ __OBJC_$_INSTANCE_METHODS_MDMRequestUserListCommand(Handler)
+ __OBJC_$_INSTANCE_VARIABLES_MDMLostDeviceLocationManager
+ __OBJC_$_INSTANCE_VARIABLES_MDMRequestBase
+ __OBJC_$_INSTANCE_VARIABLES_MDMRequestDeviceEraseCommand
+ __OBJC_$_INSTANCE_VARIABLES_MDMRequestDeviceEraseCommand_ReturnToService
+ __OBJC_$_INSTANCE_VARIABLES_MDMRequestDeviceLockCommand
+ __OBJC_$_INSTANCE_VARIABLES_MDMRequestDeviceRestartCommand
+ __OBJC_$_INSTANCE_VARIABLES_MDMRequestEnableMDMLostModeCommand
+ __OBJC_$_PROP_LIST_MDMLostDeviceLocationManager
+ __OBJC_$_PROP_LIST_MDMRequestBase
+ __OBJC_$_PROP_LIST_MDMRequestDeviceEraseCommand
+ __OBJC_$_PROP_LIST_MDMRequestDeviceEraseCommand_ReturnToService
+ __OBJC_$_PROP_LIST_MDMRequestDeviceLockCommand
+ __OBJC_$_PROP_LIST_MDMRequestDeviceRestartCommand
+ __OBJC_$_PROP_LIST_MDMRequestEnableMDMLostModeCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MDMRequestHandlerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CLLocationManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CLLocationManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MDMRequestHandlerProtocol
+ __OBJC_$_PROTOCOL_REFS_CLLocationManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_MDMRequestHandlerProtocol
+ __OBJC_CLASS_PROTOCOLS_$_MDMLostDeviceLocationManager
+ __OBJC_CLASS_PROTOCOLS_$_MDMParser
+ __OBJC_CLASS_RO_$_MDMLostDeviceLocationManager
+ __OBJC_CLASS_RO_$_MDMRequestBase
+ __OBJC_CLASS_RO_$_MDMRequestClasses
+ __OBJC_CLASS_RO_$_MDMRequestClearRestrictionsPasswordCommand
+ __OBJC_CLASS_RO_$_MDMRequestDeviceEraseCommand
+ __OBJC_CLASS_RO_$_MDMRequestDeviceEraseCommand_ReturnToService
+ __OBJC_CLASS_RO_$_MDMRequestDeviceLocationCommand
+ __OBJC_CLASS_RO_$_MDMRequestDeviceLockCommand
+ __OBJC_CLASS_RO_$_MDMRequestDeviceRestartCommand
+ __OBJC_CLASS_RO_$_MDMRequestDeviceShutDownCommand
+ __OBJC_CLASS_RO_$_MDMRequestDisableMDMLostModeCommand
+ __OBJC_CLASS_RO_$_MDMRequestEnableMDMLostModeCommand
+ __OBJC_CLASS_RO_$_MDMRequestLogOutUserCommand
+ __OBJC_CLASS_RO_$_MDMRequestPlayLostModeSoundCommand
+ __OBJC_CLASS_RO_$_MDMRequestSecurityInformationCommand
+ __OBJC_CLASS_RO_$_MDMRequestUserListCommand
+ __OBJC_LABEL_PROTOCOL_$_CLLocationManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_MDMRequestHandlerProtocol
+ __OBJC_METACLASS_RO_$_MDMLostDeviceLocationManager
+ __OBJC_METACLASS_RO_$_MDMRequestBase
+ __OBJC_METACLASS_RO_$_MDMRequestClasses
+ __OBJC_METACLASS_RO_$_MDMRequestClearRestrictionsPasswordCommand
+ __OBJC_METACLASS_RO_$_MDMRequestDeviceEraseCommand
+ __OBJC_METACLASS_RO_$_MDMRequestDeviceEraseCommand_ReturnToService
+ __OBJC_METACLASS_RO_$_MDMRequestDeviceLocationCommand
+ __OBJC_METACLASS_RO_$_MDMRequestDeviceLockCommand
+ __OBJC_METACLASS_RO_$_MDMRequestDeviceRestartCommand
+ __OBJC_METACLASS_RO_$_MDMRequestDeviceShutDownCommand
+ __OBJC_METACLASS_RO_$_MDMRequestDisableMDMLostModeCommand
+ __OBJC_METACLASS_RO_$_MDMRequestEnableMDMLostModeCommand
+ __OBJC_METACLASS_RO_$_MDMRequestLogOutUserCommand
+ __OBJC_METACLASS_RO_$_MDMRequestPlayLostModeSoundCommand
+ __OBJC_METACLASS_RO_$_MDMRequestSecurityInformationCommand
+ __OBJC_METACLASS_RO_$_MDMRequestUserListCommand
+ __OBJC_PROTOCOL_$_CLLocationManagerDelegate
+ __OBJC_PROTOCOL_$_MDMRequestHandlerProtocol
+ ___100-[MDMWallpaperUtilities _updateWallpaperConfiguraitonWithUUID:updates:retryCount:completionHandler:]_block_invoke
+ ___100-[MDMWallpaperUtilities _updateWallpaperConfiguraitonWithUUID:updates:retryCount:completionHandler:]_block_invoke.8
+ ___110-[MDMWallpaperUtilities _setWallpaper:forConfigurationWithUUID:setLockScreen:setHomeScreen:completionHandler:]_block_invoke_2
+ ___34-[MDMServerCore _pollingSucceeded]_block_invoke
+ ___41+[MDMRequestClasses classForRequestType:]_block_invoke
+ ___50-[MDMRequestDeviceEraseCommand serializeWithType:]_block_invoke
+ ___50-[MDMServerCore connection:didReceivePublicToken:]_block_invoke.223
+ ___50-[MDMServerCore connection:didReceivePublicToken:]_block_invoke_2.225
+ ___50-[MDMServicerCore blockAppInstallsWithCompletion:]_block_invoke.101
+ ___52-[MDMRequestDeviceRestartCommand serializeWithType:]_block_invoke
+ ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1414
+ ___55-[MDMServerCore _executeBlockWhenPushTokenIsAvailable:]_block_invoke.212
+ ___61-[MDMServerCore requestInstallOfAppsInRestoreWithCompletion:]_block_invoke.190
+ ___62-[MDMLostDeviceLocationManager clearLastLocationRequestedDate]_block_invoke
+ ___62-[MDMServerCore _executionQueueRemoveMDMProfileWithAssertion:]_block_invoke.238
+ ___63-[MDMServerCore connection:didReceiveMessageForTopic:userInfo:]_block_invoke.229
+ ___63-[MDMServerCore connection:didReceiveMessageForTopic:userInfo:]_block_invoke.231
+ ___64-[MDMLostDeviceLocationManager lastLocationRequestedDateMessage]_block_invoke
+ ___65-[MDMLostDeviceLocationManager _updateLostModeFileForOriginator:]_block_invoke
+ ___68-[MDMParser _processRequest:accessRights:assertion:completionBlock:]_block_invoke.913
+ ___68-[MDMParser _processRequest:accessRights:assertion:completionBlock:]_block_invoke_2
+ ___73-[MDMRequestLogOutUserCommand(Handler) processRequest:completionHandler:]_block_invoke
+ ___74-[MDMRequestDeviceEraseCommand(Handler) processRequest:completionHandler:]_block_invoke
+ ___75-[MDMLostDeviceLocationManager getCurrentLocationForOriginator:completion:]_block_invoke
+ ___75-[MDMLostDeviceLocationManager getCurrentLocationForOriginator:completion:]_block_invoke_2
+ ___77-[MDMRequestDeviceLocationCommand(Handler) processRequest:completionHandler:]_block_invoke
+ ___77-[MDMRequestDeviceRestartCommand loadFromDictionary:serializationType:error:]_block_invoke
+ ___80-[MDMRequestEnableMDMLostModeCommand(Handler) processRequest:completionHandler:]_block_invoke
+ ___80-[MDMRequestPlayLostModeSoundCommand(Handler) processRequest:completionHandler:]_block_invoke
+ ___81-[MDMRequestDisableMDMLostModeCommand(Handler) processRequest:completionHandler:]_block_invoke
+ ___89-[MDMWallpaperUtilities _updateWallpaperConfiguraitonWithUUID:updates:completionHandler:]_block_invoke
+ ___89-[MDMWallpaperUtilities _updateWallpaperConfiguraitonWithUUID:updates:completionHandler:]_block_invoke.13
+ ___89-[MDMWallpaperUtilities _updateWallpaperConfiguraitonWithUUID:updates:completionHandler:]_block_invoke.14
+ ___block_descriptor_32_e12_B24?08^16l
+ ___block_descriptor_32_e8_16?08l
+ ___block_descriptor_34_e42_"NSDictionary"16?0"RMModelPayloadBase"8l
+ ___block_descriptor_40_e8_32bs_e32_v24?0"CLLocation"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e22_v16?0"NSDictionary"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e15_v16?0"NSURL"8lr40l8s32l8
+ ___block_descriptor_56_e8_32bs40r48r_e17_v16?0"NSError"8lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32r40r48r_e15_v16?0"NSURL"8lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e15_v16?0"NSURL"8lr40l8s32l8r48l8
+ ___block_descriptor_57_e8_32s40bs48bs_e22_v16?0"NSDictionary"8ls40l8s32l8s48l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e17_v16?0"NSError"8lr48l8r56l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.1024
+ ___block_literal_global.1041
+ ___block_literal_global.1122
+ ___block_literal_global.1131
+ ___block_literal_global.1294
+ ___block_literal_global.1296
+ ___block_literal_global.1328
+ ___block_literal_global.1333
+ ___block_literal_global.1405
+ ___block_literal_global.24
+ ___block_literal_global.241
+ ___block_literal_global.295
+ ___block_literal_global.876
+ ___block_literal_global.878
+ ___block_literal_global.880
+ ___block_literal_global.882
+ ___block_literal_global.884
+ ___block_literal_global.886
+ ___block_literal_global.893
+ ___block_literal_global.980
+ __dispatch_source_type_timer
+ _classForRequestType:.onceToken
+ _classForRequestType:.requestClassByRequestType
+ _dispatch_activate
+ _dispatch_assert_queue$V2
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _kCLLocationAccuracyBest
+ _kInstalledApplicationListKeyDistributorIdentifier
+ _kMCDMDAppPropertyKeyDistributorIdentifier
+ _kMCMDMLostModeLastLocationRequestDateKey
+ _objc_msgSend$_appAttributesWithRequestedAttributes:
+ _objc_msgSend$_appManagementFlagsWithRequestedFlags:
+ _objc_msgSend$_cleanupAfterResponseFromLocationManagerOrTimeout
+ _objc_msgSend$_isChlorineEligible
+ _objc_msgSend$_isPurchaseMethodAllowed:onUserEnrollment:
+ _objc_msgSend$_isSupervised
+ _objc_msgSend$_setAppAnalyticsEnabled:
+ _objc_msgSend$_setDiagnosticSubmissionEnabled:
+ _objc_msgSend$_updateLostModeFileForOriginator:
+ _objc_msgSend$_updateWallpaperConfiguraitonWithUUID:updates:completionHandler:
+ _objc_msgSend$_updateWallpaperConfiguraitonWithUUID:updates:retryCount:completionHandler:
+ _objc_msgSend$_validateAccessRights:requiredAccessRights:error:
+ _objc_msgSend$accessRights
+ _objc_msgSend$allowedCommandKeys
+ _objc_msgSend$bundlePath
+ _objc_msgSend$classForRequestType:
+ _objc_msgSend$clearRestrictionsPasscodeWithError:
+ _objc_msgSend$commandDisallowProximitySetup
+ _objc_msgSend$commandEnabled
+ _objc_msgSend$commandFootnote
+ _objc_msgSend$commandKextPaths
+ _objc_msgSend$commandMDMProfileData
+ _objc_msgSend$commandMessage
+ _objc_msgSend$commandNotifyUser
+ _objc_msgSend$commandObliterationBehavior
+ _objc_msgSend$commandPIN
+ _objc_msgSend$commandPhoneNumber
+ _objc_msgSend$commandPreserveDataPlan
+ _objc_msgSend$commandRebuildKernelCache
+ _objc_msgSend$commandReturnToService
+ _objc_msgSend$commandWiFiProfileData
+ _objc_msgSend$completionBlock
+ _objc_msgSend$coordinateReadingItemAtURL:options:error:byAccessor:
+ _objc_msgSend$coordinateWritingItemAtURL:options:error:byAccessor:
+ _objc_msgSend$currentDevice
+ _objc_msgSend$currentPasscodeIsCompliantWithGlobalRestrictionsOutError:
+ _objc_msgSend$currentPasscodeIsCompliantWithProfileRestrictionsOutError:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$delegate
+ _objc_msgSend$dictionaryWithContentsOfURL:
+ _objc_msgSend$didInitiateSwitchUser
+ _objc_msgSend$disableManagedLostModeWithLocatedMessage:completion:
+ _objc_msgSend$distributorIdentifier
+ _objc_msgSend$enableLostModeWithInfo:
+ _objc_msgSend$enableManagedLostModeWithInfo:completion:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$forceAppInstallUnremovability
+ _objc_msgSend$forceAppRemovalOnUnenroll
+ _objc_msgSend$forceMediaCommandSupport
+ _objc_msgSend$getCurrentLocationForOriginator:completion:
+ _objc_msgSend$initWithEffectiveBundlePath:delegate:onQueue:
+ _objc_msgSend$initWithURL:data:identity:pinnedCertificates:pinningRevocationCheckRequired:signMessage:isCheckin:isCheckout:isShortTransaction:rmAccountID:
+ _objc_msgSend$isMultiUser
+ _objc_msgSend$isRequestAllowedWithError:
+ _objc_msgSend$isSubclassOfClass:
+ _objc_msgSend$isVisionDevice
+ _objc_msgSend$isoDateFormatter
+ _objc_msgSend$lastLocationRequestedDateMessage
+ _objc_msgSend$lastObject
+ _objc_msgSend$load:serializationType:error:
+ _objc_msgSend$loadArrayFromDictionary:usingKey:forKeyPath:validator:isRequired:defaultValue:error:
+ _objc_msgSend$loadBooleanFromDictionary:usingKey:forKeyPath:isRequired:defaultValue:error:
+ _objc_msgSend$loadDataFromDictionary:usingKey:forKeyPath:isRequired:defaultValue:serializationType:error:
+ _objc_msgSend$loadDictionaryFromDictionary:usingKey:forKeyPath:classType:isRequired:defaultValue:serializationType:error:
+ _objc_msgSend$loadStringFromDictionary:usingKey:forKeyPath:isRequired:defaultValue:error:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$locationManager
+ _objc_msgSend$newAssertionForBundle:withReason:
+ _objc_msgSend$originator
+ _objc_msgSend$playSoundWithOptions:completion:
+ _objc_msgSend$preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:error:
+ _objc_msgSend$processRequest:completionHandler:
+ _objc_msgSend$queue
+ _objc_msgSend$requestLocation
+ _objc_msgSend$requestType
+ _objc_msgSend$requiredAccessRights
+ _objc_msgSend$serializeArrayIntoDictionary:usingKey:value:itemSerializer:isRequired:defaultValue:
+ _objc_msgSend$serializeBooleanIntoDictionary:usingKey:value:isRequired:defaultValue:
+ _objc_msgSend$serializeDataIntoDictionary:usingKey:value:isRequired:defaultValue:serializationType:
+ _objc_msgSend$serializeDictionaryIntoDictionary:usingKey:value:dictSerializer:isRequired:defaultValue:
+ _objc_msgSend$serializeStringIntoDictionary:usingKey:value:isRequired:defaultValue:
+ _objc_msgSend$serializeWithType:
+ _objc_msgSend$setAccessRights:
+ _objc_msgSend$setAuthorizationStatusByType:forBundle:
+ _objc_msgSend$setChannelType:
+ _objc_msgSend$setCommandDisallowProximitySetup:
+ _objc_msgSend$setCommandEnabled:
+ _objc_msgSend$setCommandFootnote:
+ _objc_msgSend$setCommandKextPaths:
+ _objc_msgSend$setCommandMDMProfileData:
+ _objc_msgSend$setCommandMessage:
+ _objc_msgSend$setCommandNotifyUser:
+ _objc_msgSend$setCommandObliterationBehavior:
+ _objc_msgSend$setCommandPIN:
+ _objc_msgSend$setCommandPhoneNumber:
+ _objc_msgSend$setCommandPreserveDataPlan:
+ _objc_msgSend$setCommandRebuildKernelCache:
+ _objc_msgSend$setCommandReturnToService:
+ _objc_msgSend$setCommandWiFiProfileData:
+ _objc_msgSend$setCompletionBlock:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setDesiredAccuracy:
+ _objc_msgSend$setDisableSlideToUnlock:
+ _objc_msgSend$setFootnoteText:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setLocationManager:
+ _objc_msgSend$setLostModeEnabled:
+ _objc_msgSend$setRebootType:
+ _objc_msgSend$setResourceValues:error:
+ _objc_msgSend$setTimeStyle:
+ _objc_msgSend$setTimeoutTimerDispatchSource:
+ _objc_msgSend$sharedService
+ _objc_msgSend$shouldBlockUserSwitch
+ _objc_msgSend$shutdownWithOptions:
+ _objc_msgSend$stopUpdatingLocation
+ _objc_msgSend$switchToLoginUserWithCompletionHandler:
+ _objc_msgSend$timeoutTimerDispatchSource
+ _objc_msgSend$userValueForSetting:
+ _objc_msgSend$willTerminateProcess:
+ _objc_msgSend$writeToURL:atomically:
+ _objc_msgSend$writeToURL:options:error:
+ _os_eligibility_get_domain_answer
- -[MDMParser _clearRestrictionsPasswordRequest:completionBlock:]
- -[MDMParser _deviceLocation:]
- -[MDMParser _deviceLock:]
- -[MDMParser _deviceNotInMDMLostModeError]
- -[MDMParser _disableLostMode:assertion:completionBlock:]
- -[MDMParser _enableLostMode:assertion:completionBlock:]
- -[MDMParser _eraseDevice:]
- -[MDMParser _eraseDeviceActivationLockIsOnError]
- -[MDMParser _eraseDeviceFailedToEraseErrorWithUnderlayingError:]
- -[MDMParser _eraseDeviceInvalidMDMProfileErrorWithUnderlayingError:]
- -[MDMParser _eraseDeviceInvalidWiFiProfileErrorWithUnderlayingError:]
- -[MDMParser _eraseDeviceMissingMDMProfileError]
- -[MDMParser _eraseDeviceNotSupporttedError]
- -[MDMParser _eraseDeviceNotSupporttedOnSharedIPadError]
- -[MDMParser _eraseDeviceNotTeslaEnrolledError]
- -[MDMParser _eraseDeviceProvisionallyEnrolledError]
- -[MDMParser _logOutUser:]
- -[MDMParser _playLostModeSound:assertion:completionBlock:]
- -[MDMParser _restartDevice:]
- -[MDMParser _securityInfo:]
- -[MDMParser _shutDownDevice:]
- -[MDMParser _userList:]
- GCC_except_table190
- GCC_except_table196
- GCC_except_table207
- GCC_except_table211
- GCC_except_table221
- GCC_except_table225
- GCC_except_table241
- GCC_except_table45
- _OBJC_CLASS_$_DMCObliterationShelter
- _OBJC_CLASS_$_DMFClearRestrictionsPasswordRequest
- _OBJC_CLASS_$_DMFDisableLostModeRequest
- _OBJC_CLASS_$_DMFEnableLostModeRequest
- _OBJC_CLASS_$_DMFFetchLocationRequest
- _OBJC_CLASS_$_DMFFetchSecurityInformationRequest
- _OBJC_CLASS_$_DMFFetchUsersRequest
- _OBJC_CLASS_$_DMFLockDeviceRequest
- _OBJC_CLASS_$_DMFLogOutUserRequest
- _OBJC_CLASS_$_DMFPlayLostModeSoundRequest
- _OBJC_CLASS_$_DMFRestartDeviceRequest
- _OBJC_CLASS_$_DMFShutDownDeviceRequest
- ___110-[MDMWallpaperUtilities _setWallpaper:forConfigurationWithUUID:setLockScreen:setHomeScreen:completionHandler:]_block_invoke.11
- ___110-[MDMWallpaperUtilities _setWallpaper:forConfigurationWithUUID:setLockScreen:setHomeScreen:completionHandler:]_block_invoke.12
- ___26-[MDMParser _eraseDevice:]_block_invoke
- ___50-[MDMServerCore connection:didReceivePublicToken:]_block_invoke.222
- ___50-[MDMServerCore connection:didReceivePublicToken:]_block_invoke_2.223
- ___50-[MDMServicerCore blockAppInstallsWithCompletion:]_block_invoke.100
- ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1507
- ___55-[MDMParser _enableLostMode:assertion:completionBlock:]_block_invoke
- ___55-[MDMServerCore _executeBlockWhenPushTokenIsAvailable:]_block_invoke.211
- ___56-[MDMParser _disableLostMode:assertion:completionBlock:]_block_invoke
- ___58-[MDMParser _playLostModeSound:assertion:completionBlock:]_block_invoke
- ___58-[MDMParser _playLostModeSound:assertion:completionBlock:]_block_invoke_2
- ___61-[MDMServerCore requestInstallOfAppsInRestoreWithCompletion:]_block_invoke.189
- ___62-[MDMServerCore _executionQueueRemoveMDMProfileWithAssertion:]_block_invoke.237
- ___63-[MDMParser _clearRestrictionsPasswordRequest:completionBlock:]_block_invoke
- ___63-[MDMServerCore connection:didReceiveMessageForTopic:userInfo:]_block_invoke.228
- ___63-[MDMServerCore connection:didReceiveMessageForTopic:userInfo:]_block_invoke.230
- ___block_descriptor_56_e8_32s40s48bs_e22_v16?0"NSDictionary"8ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e20_v24?08"NSError"16ls32l8s40l8s56l8s48l8
- ___block_descriptor_65_e8_32s40s48bs56bs_e22_v16?0"NSDictionary"8ls48l8s32l8s56l8s40l8
- ___block_literal_global.1074
- ___block_literal_global.1118
- ___block_literal_global.1135
- ___block_literal_global.1214
- ___block_literal_global.1223
- ___block_literal_global.1387
- ___block_literal_global.1389
- ___block_literal_global.1421
- ___block_literal_global.1426
- ___block_literal_global.1498
- ___block_literal_global.240
- ___block_literal_global.294
- ___block_literal_global.911
- ___block_literal_global.913
- ___block_literal_global.915
- ___block_literal_global.917
- ___block_literal_global.919
- ___block_literal_global.921
- ___block_literal_global.927
- _kCCCloudConfigurationUICompleteKey
- _kCCCloudConfigurationWasAppliedKey
- _objc_msgSend$_clearRestrictionsPasswordRequest:completionBlock:
- _objc_msgSend$_deviceLocation:
- _objc_msgSend$_deviceLock:
- _objc_msgSend$_deviceNotInMDMLostModeError
- _objc_msgSend$_disableLostMode:assertion:completionBlock:
- _objc_msgSend$_enableLostMode:assertion:completionBlock:
- _objc_msgSend$_eraseDevice:
- _objc_msgSend$_logOutUser:
- _objc_msgSend$_playLostModeSound:assertion:completionBlock:
- _objc_msgSend$_restartDevice:
- _objc_msgSend$_securityInfo:
- _objc_msgSend$_shutDownDevice:
- _objc_msgSend$_userList:
- _objc_msgSend$dmc_valueOfClass:forKey:
- _objc_msgSend$initWithURL:data:identity:pinnedCertificates:pinningRevocationCheckRequired:signMessage:isCheckin:isShortTransaction:rmAccountID:
- _objc_msgSend$isCurrentUser
- _objc_msgSend$localeIdentifier
- _objc_msgSend$location
- _objc_msgSend$passcodeIsCompliantWithGlobalRestrictions
- _objc_msgSend$passcodeIsCompliantWithProfileRestrictions
- _objc_msgSend$passcodeIsSet
- _objc_msgSend$passcodeLockGracePeriod
- _objc_msgSend$passcodeLockGracePeriodEnforced
- _objc_msgSend$preferredLanguages
- _objc_msgSend$preserveWithError:
- _objc_msgSend$securityInformation
- _objc_msgSend$setCloudConfigurationDetails:
- _objc_msgSend$setFootnote:
- _objc_msgSend$setLanguageStrings:
- _objc_msgSend$setLocaleString:
- _objc_msgSend$setMdmProfileData:
- _objc_msgSend$setWifiProfileData:
- _objc_msgSend$users
CStrings:
+ "\x05"
+ "#24@0:8@16"
+ "@\"<MDMRequestHandlerProtocol>\""
+ "@\"CLLocationManager\""
+ "@\"MDMRequestDeviceEraseCommand_ReturnToService\""
+ "@\"NSDictionary\"16@?0@\"RMModelPayloadBase\"8"
+ "@\"NSObject<OS_dispatch_source>\""
+ "@16@?0@8"
+ "@20@0:8s16"
+ "@24@0:8^{_NSZone=}16"
+ "Always"
+ "B24@0:8@\"CLLocationManager\"16"
+ "B24@0:8i16B20"
+ "B24@?0@8^@16"
+ "B36@0:8@16s24^@28"
+ "B40@0:8Q16Q24^@32"
+ "CLLocationManagerDelegate"
+ "Could not disable lost mode: %{public}@"
+ "Could not play sound in MDM Lost Mode: Device is not in lost mode."
+ "Could not read device last located time interval for update: %@"
+ "Could not read device last located time interval: %@"
+ "Could not read device last location requested file: %@"
+ "Could not remove device last located file: %@"
+ "Could not write device last located time interval"
+ "Could not write device last located time interval URL resourve values: %@"
+ "Device is not in lost mode. Reporting success regardless."
+ "Device last located on %{public}@. Creating localized message."
+ "Device was located while in lost mode. Alerting user with message “%{public}@”"
+ "Disabling lost mode..."
+ "DistributorIdentifier"
+ "DoNotObliterate"
+ "Eligibility check failed with error code: %d"
+ "Failed to update wallpaper. Retry count %ld"
+ "Failed to write image to url: %{public}@, error: %{public}@"
+ "Handler"
+ "KextPaths"
+ "Location Manager failed: error=%{public}@"
+ "Location Manager returned a location, but we can't report it because we can't record that fact. Throwing location information away."
+ "Location Manager returned a location."
+ "Location Manager timed out"
+ "MDMDLDLMServiceQueue"
+ "MDMDLostDeviceLocationManager getCurrentLocationForOriginator:completion:"
+ "MDMLostDeviceLocationManager"
+ "MDMNotifications"
+ "MDMRequestBase"
+ "MDMRequestClasses"
+ "MDMRequestClearRestrictionsPasswordCommand"
+ "MDMRequestDeviceEraseCommand"
+ "MDMRequestDeviceEraseCommand_ReturnToService"
+ "MDMRequestDeviceLocationCommand"
+ "MDMRequestDeviceLockCommand"
+ "MDMRequestDeviceRestartCommand"
+ "MDMRequestDeviceShutDownCommand"
+ "MDMRequestDisableMDMLostModeCommand"
+ "MDMRequestEnableMDMLostModeCommand"
+ "MDMRequestHandlerProtocol"
+ "MDMRequestLogOutUserCommand"
+ "MDMRequestPlayLostModeSoundCommand"
+ "MDMRequestSecurityInformationCommand"
+ "MDMRequestUserListCommand"
+ "MDM_ERROR_COULD_NOT_LOG_OUT_USER"
+ "MDM_ERROR_NO_USER_LOGGED_IN"
+ "Malformed command %{public}@."
+ "NotifyUser"
+ "ObliterateWithWarning"
+ "ObliterationBehavior"
+ "PIN"
+ "RebuildKernelCache"
+ "Retry setting wallpaper..."
+ "T@\"<MDMRequestHandlerProtocol>\",W,V_delegate"
+ "T@\"CLLocationManager\",&,N,V_locationManager"
+ "T@\"MDMRequestDeviceEraseCommand_ReturnToService\",C,N,V_commandReturnToService"
+ "T@\"NSArray\",C,N,V_commandKextPaths"
+ "T@\"NSData\",C,N,V_commandMDMProfileData"
+ "T@\"NSData\",C,N,V_commandWiFiProfileData"
+ "T@\"NSNumber\",C,N,V_commandDisallowProximitySetup"
+ "T@\"NSNumber\",C,N,V_commandEnabled"
+ "T@\"NSNumber\",C,N,V_commandNotifyUser"
+ "T@\"NSNumber\",C,N,V_commandPreserveDataPlan"
+ "T@\"NSNumber\",C,N,V_commandRebuildKernelCache"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_timeoutTimerDispatchSource"
+ "T@\"NSSet\",R,C"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_commandFootnote"
+ "T@\"NSString\",C,N,V_commandMessage"
+ "T@\"NSString\",C,N,V_commandObliterationBehavior"
+ "T@\"NSString\",C,N,V_commandPIN"
+ "T@\"NSString\",C,N,V_commandPhoneNumber"
+ "T@\"NSString\",C,N,V_originator"
+ "T@?,C,N,V_completionBlock"
+ "TQ,N,V_accessRights"
+ "The location of this device was sent to %@ at %@ on %@."
+ "Unexpected payload keys: %@"
+ "_accessRights"
+ "_appAttributesWithRequestedAttributes:"
+ "_appManagementFlagsWithRequestedFlags:"
+ "_cleanupAfterResponseFromLocationManagerOrTimeout"
+ "_commandDisallowProximitySetup"
+ "_commandEnabled"
+ "_commandFootnote"
+ "_commandKextPaths"
+ "_commandMDMProfileData"
+ "_commandMessage"
+ "_commandNotifyUser"
+ "_commandObliterationBehavior"
+ "_commandPIN"
+ "_commandPhoneNumber"
+ "_commandPreserveDataPlan"
+ "_commandRebuildKernelCache"
+ "_commandReturnToService"
+ "_commandWiFiProfileData"
+ "_delegate"
+ "_isChlorineEligible"
+ "_isPurchaseMethodAllowed:onUserEnrollment:"
+ "_isSupervised"
+ "_locationManager"
+ "_setAppAnalyticsEnabled:"
+ "_setDiagnosticSubmissionEnabled:"
+ "_timeoutTimerDispatchSource"
+ "_updateLostModeFileForOriginator:"
+ "_updateWallpaperConfiguraitonWithUUID:updates:completionHandler:"
+ "_updateWallpaperConfiguraitonWithUUID:updates:retryCount:completionHandler:"
+ "_validateAccessRights:requiredAccessRights:error:"
+ "accessRights"
+ "allowedCommandKeys"
+ "buildRequiredOnlyWithEnabled:"
+ "buildWithEnabled:wiFiProfileData:mdmProfileData:"
+ "bundlePath"
+ "classForRequestType:"
+ "clearLastLocationRequestedDate"
+ "clearRestrictionsPasscodeWithError:"
+ "commandDisallowProximitySetup"
+ "commandEnabled"
+ "commandFootnote"
+ "commandKextPaths"
+ "commandMDMProfileData"
+ "commandMessage"
+ "commandNotifyUser"
+ "commandObliterationBehavior"
+ "commandPIN"
+ "commandPhoneNumber"
+ "commandPreserveDataPlan"
+ "commandRebuildKernelCache"
+ "commandReturnToService"
+ "commandWiFiProfileData"
+ "completionBlock"
+ "coordinateReadingItemAtURL:options:error:byAccessor:"
+ "coordinateWritingItemAtURL:options:error:byAccessor:"
+ "copyWithZone:"
+ "currentDevice"
+ "currentPasscodeIsCompliantWithGlobalRestrictionsOutError:"
+ "currentPasscodeIsCompliantWithProfileRestrictionsOutError:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "delegate"
+ "dictionaryWithContentsOfURL:"
+ "didInitiateSwitchUser"
+ "disableManagedLostModeWithLocatedMessage:completion:"
+ "distributorIdentifier"
+ "enableLostModeWithInfo:"
+ "enableManagedLostModeWithInfo:completion:"
+ "fileURLWithPath:isDirectory:"
+ "forceAppInstallUnremovability"
+ "forceAppRemovalOnUnenroll"
+ "forceMediaCommandSupport"
+ "getCurrentLocationForOriginator:completion:"
+ "initWithEffectiveBundlePath:delegate:onQueue:"
+ "initWithURL:data:identity:pinnedCertificates:pinningRevocationCheckRequired:signMessage:isCheckin:isCheckout:isShortTransaction:rmAccountID:"
+ "isChlorineEligible: %llu"
+ "isMultiUser"
+ "isRequestAllowedWithError:"
+ "isSubclassOfClass:"
+ "isVisionDevice"
+ "isoDateFormatter"
+ "lastLocationRequestedDateMessage"
+ "lastObject"
+ "load:serializationType:error:"
+ "loadArrayFromDictionary:usingKey:forKeyPath:validator:isRequired:defaultValue:error:"
+ "loadBooleanFromDictionary:usingKey:forKeyPath:isRequired:defaultValue:error:"
+ "loadDataFromDictionary:usingKey:forKeyPath:isRequired:defaultValue:serializationType:error:"
+ "loadDictionaryFromDictionary:usingKey:forKeyPath:classType:isRequired:defaultValue:serializationType:error:"
+ "loadFromDictionary:serializationType:error:"
+ "loadStringFromDictionary:usingKey:forKeyPath:isRequired:defaultValue:error:"
+ "localizedStringForKey:value:table:"
+ "locationManager"
+ "locationManager:didChangeAuthorizationStatus:"
+ "locationManager:didDetermineState:forRegion:"
+ "locationManager:didEnterRegion:"
+ "locationManager:didExitRegion:"
+ "locationManager:didFailRangingBeaconsForConstraint:error:"
+ "locationManager:didFailWithError:"
+ "locationManager:didFinishDeferredUpdatesWithError:"
+ "locationManager:didRangeBeacons:inRegion:"
+ "locationManager:didRangeBeacons:satisfyingConstraint:"
+ "locationManager:didStartMonitoringForRegion:"
+ "locationManager:didUpdateHeading:"
+ "locationManager:didUpdateLocations:"
+ "locationManager:didUpdateToLocation:fromLocation:"
+ "locationManager:didVisit:"
+ "locationManager:monitoringDidFailForRegion:withError:"
+ "locationManager:rangingBeaconsDidFailForRegion:withError:"
+ "locationManagerDidChangeAuthorization:"
+ "locationManagerDidPauseLocationUpdates:"
+ "locationManagerDidResumeLocationUpdates:"
+ "locationManagerShouldDisplayHeadingCalibration:"
+ "mdmd restart device"
+ "mdmd shut down device"
+ "newAssertionForBundle:withReason:"
+ "originator"
+ "playSoundWithOptions:completion:"
+ "preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:error:"
+ "processRequest:completionHandler:"
+ "requestLocation"
+ "requestType"
+ "requestWithMessage:phoneNumber:PIN:"
+ "requestWithMessage:phoneNumber:footnote:"
+ "requestWithPreserveDataPlan:disallowProximitySetup:PIN:obliterationBehavior:returnToService:"
+ "requestWithRebuildKernelCache:kextPaths:notifyUser:"
+ "requiredAccessRights"
+ "serializeArrayIntoDictionary:usingKey:value:itemSerializer:isRequired:defaultValue:"
+ "serializeBooleanIntoDictionary:usingKey:value:isRequired:defaultValue:"
+ "serializeDataIntoDictionary:usingKey:value:isRequired:defaultValue:serializationType:"
+ "serializeDictionaryIntoDictionary:usingKey:value:dictSerializer:isRequired:defaultValue:"
+ "serializeStringIntoDictionary:usingKey:value:isRequired:defaultValue:"
+ "serializeWithType:"
+ "setAccessRights:"
+ "setAuthorizationStatusByType:forBundle:"
+ "setCommandDisallowProximitySetup:"
+ "setCommandEnabled:"
+ "setCommandFootnote:"
+ "setCommandKextPaths:"
+ "setCommandMDMProfileData:"
+ "setCommandMessage:"
+ "setCommandNotifyUser:"
+ "setCommandObliterationBehavior:"
+ "setCommandPIN:"
+ "setCommandPhoneNumber:"
+ "setCommandPreserveDataPlan:"
+ "setCommandRebuildKernelCache:"
+ "setCommandReturnToService:"
+ "setCommandWiFiProfileData:"
+ "setCompletionBlock:"
+ "setDateStyle:"
+ "setDesiredAccuracy:"
+ "setDisableSlideToUnlock:"
+ "setFootnoteText:"
+ "setLocale:"
+ "setLocationManager:"
+ "setLostModeEnabled:"
+ "setRebootType:"
+ "setResourceValues:error:"
+ "setTimeStyle:"
+ "setTimeoutTimerDispatchSource:"
+ "sharedService"
+ "shouldBlockUserSwitch"
+ "shutdownWithOptions:"
+ "stopUpdatingLocation"
+ "switchToLoginUserWithCompletionHandler:"
+ "timeoutTimerDispatchSource"
+ "userValueForSetting:"
+ "v16@?0@\"NSURL\"8"
+ "v24@0:8@\"CLLocationManager\"16"
+ "v24@?0@\"CLLocation\"8@\"NSError\"16"
+ "v28@0:8@\"CLLocationManager\"16i24"
+ "v28@0:8@16i24"
+ "v32@0:8@\"CLLocationManager\"16@\"CLHeading\"24"
+ "v32@0:8@\"CLLocationManager\"16@\"CLRegion\"24"
+ "v32@0:8@\"CLLocationManager\"16@\"CLVisit\"24"
+ "v32@0:8@\"CLLocationManager\"16@\"NSArray\"24"
+ "v32@0:8@\"CLLocationManager\"16@\"NSError\"24"
+ "v40@0:8@\"CLLocationManager\"16@\"CLBeaconIdentityConstraint\"24@\"NSError\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"CLBeaconRegion\"24@\"NSError\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"CLLocation\"24@\"CLLocation\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"CLRegion\"24@\"NSError\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"NSArray\"24@\"CLBeaconIdentityConstraint\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"NSArray\"24@\"CLBeaconRegion\"32"
+ "v40@0:8@\"CLLocationManager\"16q24@\"CLRegion\"32"
+ "v40@0:8@16q24@32"
+ "v48@0:8@16@24Q32@?40"
+ "willTerminateProcess:"
+ "writeToURL:atomically:"
+ "writeToURL:options:error:"
- "Could not play sound in MDM Lost Mode: %{public}@"
- "Could not to disable MDM Lost Mode: %{public}@"
- "Doing RRTS on non-ADE enrolled device, need to preserve the cloud config"
- "Failed to retrieve security information with error: %{public}@"
- "Failed to write image to url: %{public}@"
- "_clearRestrictionsPasswordRequest:completionBlock:"
- "_deviceLocation:"
- "_deviceLock:"
- "_deviceNotInMDMLostModeError"
- "_disableLostMode:assertion:completionBlock:"
- "_enableLostMode:assertion:completionBlock:"
- "_eraseDevice:"
- "_logOutUser:"
- "_playLostModeSound:assertion:completionBlock:"
- "_restartDevice:"
- "_securityInfo:"
- "_shutDownDevice:"
- "_userList:"
- "dmc_valueOfClass:forKey:"
- "initWithURL:data:identity:pinnedCertificates:pinningRevocationCheckRequired:signMessage:isCheckin:isShortTransaction:rmAccountID:"
- "isCurrentUser"
- "localeIdentifier"
- "location"
- "passcodeIsCompliantWithGlobalRestrictions"
- "passcodeIsCompliantWithProfileRestrictions"
- "passcodeIsSet"
- "passcodeLockGracePeriod"
- "passcodeLockGracePeriodEnforced"
- "preferredLanguages"
- "preserveWithError:"
- "securityInformation"
- "setCloudConfigurationDetails:"
- "setFootnote:"
- "setLanguageStrings:"
- "setLocaleString:"
- "setMdmProfileData:"
- "setWifiProfileData:"
- "users"

```
