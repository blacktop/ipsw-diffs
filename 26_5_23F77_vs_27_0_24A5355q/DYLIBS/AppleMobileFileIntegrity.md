## AppleMobileFileIntegrity

> `/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity`

```diff

-1045.120.5.0.0
-  __TEXT.__text: 0xb12c
-  __TEXT.__auth_stubs: 0x790
-  __TEXT.__objc_methlist: 0x2f4
-  __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x15f5
-  __TEXT.__oslogstring: 0xbf0
-  __TEXT.__gcc_except_tab: 0x2c8
-  __TEXT.__unwind_info: 0x328
-  __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0x9c2
-  __TEXT.__objc_methtype: 0x352
-  __TEXT.__objc_stubs: 0xa40
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x828
-  __DATA_CONST.__objc_classlist: 0x30
+1166.0.0.0.0
+  __TEXT.__text: 0xb6f0
+  __TEXT.__lazy_helpers: 0x54
+  __TEXT.__objc_methlist: 0x48c
+  __TEXT.__const: 0x1d0
+  __TEXT.__cstring: 0x1853
+  __TEXT.__oslogstring: 0xdd2
+  __TEXT.__gcc_except_tab: 0x384
+  __TEXT.__unwind_info: 0x3b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x8c8
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x300
+  __DATA_CONST.__objc_selrefs: 0x428
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x3d8
-  __AUTH_CONST.__const: 0x268
-  __AUTH_CONST.__cfstring: 0x720
-  __AUTH_CONST.__objc_const: 0x658
-  __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__got: 0x1c8
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__cfstring: 0x760
+  __AUTH_CONST.__objc_const: 0x908
+  __AUTH_CONST.__lazy_load_got: 0x8
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x6c
+  __DATA.__data: 0xc4
   __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6B182011-1E99-3AEC-8E2B-CF2A2A357564
-  Functions: 258
-  Symbols:   881
-  CStrings:  497
+  UUID: B9123383-80C6-3CAC-8B07-FCFCA89C8E3D
+  Functions: 292
+  Symbols:   1027
+  CStrings:  350
 
Symbols:
+ -[AMFIDeveloperModeSettingVisibilityManager .cxx_destruct]
+ -[AMFIDeveloperModeSettingVisibilityManager callbackQueue]
+ -[AMFIDeveloperModeSettingVisibilityManager changeBlock]
+ -[AMFIDeveloperModeSettingVisibilityManager computeCurrentVisibility]
+ -[AMFIDeveloperModeSettingVisibilityManager dealloc]
+ -[AMFIDeveloperModeSettingVisibilityManager developerModeChangedToken]
+ -[AMFIDeveloperModeSettingVisibilityManager handlePairableHostBecameUnavailableWithIdentifier:]
+ -[AMFIDeveloperModeSettingVisibilityManager handlePairableHostDiscovered:]
+ -[AMFIDeveloperModeSettingVisibilityManager init]
+ -[AMFIDeveloperModeSettingVisibilityManager invalidate]
+ -[AMFIDeveloperModeSettingVisibilityManager invalidated]
+ -[AMFIDeveloperModeSettingVisibilityManager monitorQueue]
+ -[AMFIDeveloperModeSettingVisibilityManager monitoringStarted]
+ -[AMFIDeveloperModeSettingVisibilityManager pairableHostBrowser]
+ -[AMFIDeveloperModeSettingVisibilityManager pairableHosts]
+ -[AMFIDeveloperModeSettingVisibilityManager profileInstalledToken]
+ -[AMFIDeveloperModeSettingVisibilityManager profileRemovedToken]
+ -[AMFIDeveloperModeSettingVisibilityManager recomputeVisibility]
+ -[AMFIDeveloperModeSettingVisibilityManager setCallbackQueue:]
+ -[AMFIDeveloperModeSettingVisibilityManager setChangeBlock:]
+ -[AMFIDeveloperModeSettingVisibilityManager setDeveloperModeChangedToken:]
+ -[AMFIDeveloperModeSettingVisibilityManager setInvalidated:]
+ -[AMFIDeveloperModeSettingVisibilityManager setMonitorQueue:]
+ -[AMFIDeveloperModeSettingVisibilityManager setMonitoringStarted:]
+ -[AMFIDeveloperModeSettingVisibilityManager setPairableHostBrowser:]
+ -[AMFIDeveloperModeSettingVisibilityManager setPairableHosts:]
+ -[AMFIDeveloperModeSettingVisibilityManager setProfileInstalledToken:]
+ -[AMFIDeveloperModeSettingVisibilityManager setProfileRemovedToken:]
+ -[AMFIDeveloperModeSettingVisibilityManager setSettingsShouldBeVisibleInternal:]
+ -[AMFIDeveloperModeSettingVisibilityManager settingsShouldBeVisibleInternal]
+ -[AMFIDeveloperModeSettingVisibilityManager settingsShouldBeVisible]
+ -[AMFIDeveloperModeSettingVisibilityManager startMonitoringVisibilityChangesOnQueue:withBlock:]
+ -[AMFIDeveloperModeSettingVisibilityManager visibilityDidChange:]
+ -[AMFIPathValidator_ios computedCdHash:withLength:]
+ GCC_except_table13
+ GCC_except_table9
+ _OBJC_CLASS_$_AMFIDeveloperModeSettingVisibilityManager
+ _OBJC_CLASS_$_RPPairableHostBrowser
+ _OBJC_CLASS_$_RPPairableHostBrowser$lazyGOT
+ _OBJC_CLASS_$_RPPairableHostBrowser$lazyGOT$loadHelper_x22
+ _OBJC_IVAR_$_AMFIDeveloperModeSettingVisibilityManager._callbackQueue
+ _OBJC_IVAR_$_AMFIDeveloperModeSettingVisibilityManager._changeBlock
+ _OBJC_IVAR_$_AMFIDeveloperModeSettingVisibilityManager._developerModeChangedToken
+ _OBJC_IVAR_$_AMFIDeveloperModeSettingVisibilityManager._invalidated
+ _OBJC_IVAR_$_AMFIDeveloperModeSettingVisibilityManager._monitorQueue
+ _OBJC_IVAR_$_AMFIDeveloperModeSettingVisibilityManager._monitoringStarted
+ _OBJC_IVAR_$_AMFIDeveloperModeSettingVisibilityManager._pairableHostBrowser
+ _OBJC_IVAR_$_AMFIDeveloperModeSettingVisibilityManager._pairableHosts
+ _OBJC_IVAR_$_AMFIDeveloperModeSettingVisibilityManager._profileInstalledToken
+ _OBJC_IVAR_$_AMFIDeveloperModeSettingVisibilityManager._profileRemovedToken
+ _OBJC_IVAR_$_AMFIDeveloperModeSettingVisibilityManager._settingsShouldBeVisibleInternal
+ _OBJC_METACLASS_$_AMFIDeveloperModeSettingVisibilityManager
+ __OBJC_$_INSTANCE_METHODS_AMFIDeveloperModeSettingVisibilityManager
+ __OBJC_$_INSTANCE_VARIABLES_AMFIDeveloperModeSettingVisibilityManager
+ __OBJC_$_PROP_LIST_AMFIDeveloperModeSettingVisibilityManager
+ __OBJC_CLASS_RO_$_AMFIDeveloperModeSettingVisibilityManager
+ __OBJC_METACLASS_RO_$_AMFIDeveloperModeSettingVisibilityManager
+ ___31-[AMFIConnection setDemoState:]_block_invoke.45
+ ___34-[AMFIConnection setManagedState:]_block_invoke.46
+ ___36-[AMFIConnection removeManagedState]_block_invoke.47
+ ___37-[AMFIConnection setSupervisedState:]_block_invoke.44
+ ___38-[AMFIConnection stageProfileForUuid:]_block_invoke.38
+ ___39-[AMFIConnection commitProfileForUuid:]_block_invoke.41
+ ___39-[AMFIConnection getSEPStateWithError:]_block_invoke.34
+ ___39-[AMFIConnection removeTrustforTeamID:]_block_invoke.43
+ ___44-[AMFIConnection getStagedProfileWithError:]_block_invoke.39
+ ___63-[AMFIConnection setTrustForTeamID:withSignature:withSignType:]_block_invoke.42
+ ___65-[AMFIDeveloperModeSettingVisibilityManager visibilityDidChange:]_block_invoke
+ ___66-[AMFIConnection signTeamID:withSignType:withLAContext:withError:]_block_invoke.36
+ ___74-[AMFIDeveloperModeSettingVisibilityManager handlePairableHostDiscovered:]_block_invoke
+ ___95-[AMFIDeveloperModeSettingVisibilityManager startMonitoringVisibilityChangesOnQueue:withBlock:]_block_invoke
+ ___95-[AMFIDeveloperModeSettingVisibilityManager startMonitoringVisibilityChangesOnQueue:withBlock:]_block_invoke_2
+ ___95-[AMFIDeveloperModeSettingVisibilityManager startMonitoringVisibilityChangesOnQueue:withBlock:]_block_invoke_3
+ ___95-[AMFIDeveloperModeSettingVisibilityManager startMonitoringVisibilityChangesOnQueue:withBlock:]_block_invoke_4
+ ___block_descriptor_40_e8_32s_e8_v12?0i8ls32l8
+ ___block_descriptor_40_e8_32w_e24_v16?0"RPPairableHost"8lw32l8
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40w48w_e5_v8?0lw40l8w48l8s32l8
+ ___block_descriptor_tmp.58
+ ___block_descriptor_tmp.60
+ ___block_descriptor_tmp.66
+ ___block_descriptor_tmp.70
+ __dyld_lazy_load
+ _amfi_interface_authorize_local_signing_with_length
+ _lazyLoadFlag$RemotePairingDevice
+ _memcpy
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$available
+ _objc_msgSend$callbackQueue
+ _objc_msgSend$cancel
+ _objc_msgSend$changeBlock
+ _objc_msgSend$computeCurrentVisibility
+ _objc_msgSend$developerModeChangedToken
+ _objc_msgSend$handlePairableHostBecameUnavailableWithIdentifier:
+ _objc_msgSend$handlePairableHostDiscovered:
+ _objc_msgSend$identifier
+ _objc_msgSend$invalidated
+ _objc_msgSend$monitorQueue
+ _objc_msgSend$pairableHostBrowser
+ _objc_msgSend$pairableHosts
+ _objc_msgSend$profileInstalledToken
+ _objc_msgSend$profileRemovedToken
+ _objc_msgSend$recomputeVisibility
+ _objc_msgSend$registerChangeHandlerOnTargetQueue:handler:
+ _objc_msgSend$registerHostDiscoveredHandlerOnQueue:handler:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$setCallbackQueue:
+ _objc_msgSend$setChangeBlock:
+ _objc_msgSend$setDeveloperModeChangedToken:
+ _objc_msgSend$setInvalidated:
+ _objc_msgSend$setMonitoringStarted:
+ _objc_msgSend$setPairableHostBrowser:
+ _objc_msgSend$setProfileInstalledToken:
+ _objc_msgSend$setProfileRemovedToken:
+ _objc_msgSend$setSettingsShouldBeVisibleInternal:
+ _objc_msgSend$settingsShouldBeVisibleInternal
+ _objc_msgSend$startBrowsing
+ _objc_msgSend$visibilityDidChange:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_setProperty_nonatomic_copy
+ _objc_sync_enter
+ _objc_sync_exit
- -[AMFIPathValidator_ios computedCdHash:]
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- ___31-[AMFIConnection setDemoState:]_block_invoke.46
- ___34-[AMFIConnection setManagedState:]_block_invoke.47
- ___36-[AMFIConnection removeManagedState]_block_invoke.48
- ___37-[AMFIConnection setSupervisedState:]_block_invoke.45
- ___38-[AMFIConnection stageProfileForUuid:]_block_invoke.39
- ___39-[AMFIConnection commitProfileForUuid:]_block_invoke.42
- ___39-[AMFIConnection getSEPStateWithError:]_block_invoke.35
- ___39-[AMFIConnection removeTrustforTeamID:]_block_invoke.44
- ___44-[AMFIConnection getStagedProfileWithError:]_block_invoke.40
- ___63-[AMFIConnection setTrustForTeamID:withSignature:withSignType:]_block_invoke.43
- ___66-[AMFIConnection signTeamID:withSignType:withLAContext:withError:]_block_invoke.37
- ___block_descriptor_tmp.55
- ___block_descriptor_tmp.59
- ___block_descriptor_tmp.62
- ___block_descriptor_tmp.68
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%"
+ "-[AMFIDeveloperModeSettingVisibilityManager computeCurrentVisibility]"
+ "-[AMFIDeveloperModeSettingVisibilityManager handlePairableHostBecameUnavailableWithIdentifier:]"
+ "-[AMFIDeveloperModeSettingVisibilityManager handlePairableHostDiscovered:]"
+ "-[AMFIDeveloperModeSettingVisibilityManager invalidate]"
+ "-[AMFIDeveloperModeSettingVisibilityManager startMonitoringVisibilityChangesOnQueue:withBlock:]"
+ "MISProvisioningProfileInstalled"
+ "MISProvisioningProfileRemoved"
+ "[%s] Discovered nearby pairable host: %@"
+ "[%s] Invalidated"
+ "[%s] Nearby discovered pairable host disappeared: %@"
+ "[%s] Not monitoring for pairable hosts since RemotePairingDevice is not loaded."
+ "[%s] Reporting developer mode settings not visible"
+ "[%s] Reporting developer mode settings visible because AMFIShouldShowDeveloperModeSettings returned true"
+ "[%s] Reporting developer mode settings visible because nearby pairable hosts were found"
+ "[%s] Started monitoring for visibility changes"
+ "cdhash-full"
+ "com.apple.amfi.developer_mode_visibility_monitor"
+ "security.mac.amfi.developer_mode_status.changed"
+ "v12@?0i8"
+ "v16@?0@\"RPPairableHost\"8"
- ".cxx_destruct"
- "@\"NSData\""
- "@\"NSError\""
- "@\"NSMutableArray\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@28@0:8@16i24"
- "@28@0:8i16@20"
- "@32@0:8@16Q24"
- "@32@0:8q16@24"
- "@36@0:8@16@24I32"
- "@36@0:8@16@24i32"
- "@36@0:8@16Q24i32"
- "@44@0:8@16I24@28^@36"
- "AMFIConnection"
- "AMFIError"
- "AMFIFMKLog"
- "AMFIPathValidator_ios"
- "AMFIProtocol"
- "B"
- "B16@0:8"
- "B24@0:8[20C]16"
- "B24@0:8^@16"
- "I"
- "I16@0:8"
- "LWCRTypeErrorContext"
- "Q"
- "T@\"NSData\",R,N"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSString\",R,N"
- "TB,R,N,V_areEntitlementsValidated"
- "TB,R,N,V_isValid"
- "TI,R,N,V_signerType"
- "UTF8String"
- "ValidationMetrics"
- "_areEntitlementsValidated"
- "_bootargs"
- "_cdhash"
- "_error"
- "_flags"
- "_isValid"
- "_offset"
- "_profileAuxSig"
- "_profileData"
- "_profileID"
- "_signerType"
- "_url"
- "_validated"
- "addObject:"
- "appendFormat:"
- "appendString:"
- "areEntitlementsValidated"
- "auxiliarySignatureWithTeamID:"
- "bytes"
- "cStringUsingEncoding:"
- "code"
- "commitProfileForUuid:"
- "commitProfileForUuid:withReply:"
- "computedCdHash:"
- "connection"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "defaultManager"
- "dictionaryWithObjects:forKeys:count:"
- "dispatchMetrics:"
- "domain"
- "enumerateKeysAndObjectsUsingBlock:"
- "error"
- "errorWithDomain:code:userInfo:"
- "fileExistsAtPath:"
- "generic"
- "getBytes:length:"
- "getSEPStateWithError:"
- "getSEPStateWithReply:"
- "getStagedProfileWithError:"
- "getStagedProfileWithReply:"
- "i"
- "i16@0:8"
- "init"
- "initWithAMFIErrorCode:withURL:"
- "initWithData:encoding:"
- "initWithDomain:code:userInfo:"
- "initWithMISError:withURL:"
- "initWithMachServiceName:options:"
- "initWithURL:"
- "initWithURL:withFileOffset:"
- "initWithURL:withFileOffset:withFlags:"
- "initWithURL:withFileOffsetAsNumber:withFlags:"
- "initWithURL:withFlags:"
- "initiateDataMigration"
- "initiateDataMigrationWithReply:"
- "initiateDeveloperModeDaemons"
- "initiateDeveloperModeDaemonsWithReply:"
- "intValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqualToString:"
- "isSignerType"
- "isValid"
- "keyContext"
- "length"
- "longLongValue"
- "newConnection"
- "null"
- "numberWithBool:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "path"
- "popKey"
- "profileAuxSig"
- "profileData"
- "profileID"
- "pushKey:"
- "removeLastObject"
- "removeManagedState"
- "removeManagedStateWithReply:"
- "removeTrustforTeamID:"
- "removeTrustforTeamID:withReply:"
- "resume"
- "sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:withSigningYear:withExecutableFormat:withHasRestrictedEntitlements:"
- "setDemoState:"
- "setDemoState:withReply:"
- "setError:"
- "setManagedState:"
- "setManagedState:withReply:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "setSupervisedState:"
- "setSupervisedState:withReply:"
- "setTrustForTeamID:withSignature:withSignType:"
- "setTrustForTeamID:withSignature:withSignType:withReply:"
- "signTeamID:withSignType:withLAContext:withError:"
- "signTeamID:withSignType:withLAContext:withReply:"
- "signerType"
- "stageProfileForUuid:"
- "stageProfileForUuid:withReply:"
- "stringWithString:"
- "stringWithUTF8String:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "synthesizeError"
- "teamIDSupportsAuxiliarySignature:"
- "teamIDWithProfileUUID:"
- "unsignedLongLongValue"
- "v16@0:8"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "v24@0:8@?<v@?{?=III{?=C{?=I[32C]}}}@\"NSError\">16"
- "v28@0:8I16@?20"
- "v28@0:8I16@?<v@?@\"NSError\">20"
- "v32@0:8@\"LAContext\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v44@0:8@\"NSString\"16@\"NSData\"24I32@?<v@?@\"NSError\">36"
- "v44@0:8@\"NSString\"16I24@\"LAContext\"28@?<v@?@\"NSData\"@\"NSError\">36"
- "v44@0:8@16@24I32@?36"
- "v44@0:8@16I24@28@?36"
- "v88@0:8@16@24@32@40@48@56B64@68@76B84"
- "validateWithError:"
- "{?=III{?=C{?=I[32C]}}}24@0:8^@16"

```
