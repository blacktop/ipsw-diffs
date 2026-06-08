## DeviceSharingServices

> `/System/Library/PrivateFrameworks/DeviceSharingServices.framework/DeviceSharingServices`

```diff

-38.60.2.0.0
-  __TEXT.__text: 0x236b8
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x624
-  __TEXT.__const: 0x382c
-  __TEXT.__cstring: 0x10e3
+40.0.0.0.0
+  __TEXT.__text: 0x23338
+  __TEXT.__objc_methlist: 0x634
+  __TEXT.__const: 0x380c
+  __TEXT.__cstring: 0x1144
   __TEXT.__oslogstring: 0xca1
-  __TEXT.__swift5_typeref: 0x9a9
+  __TEXT.__swift5_typeref: 0x9ad
   __TEXT.__constg_swiftt: 0xa00
-  __TEXT.__swift5_reflstr: 0x9fc
-  __TEXT.__swift5_fieldmd: 0x8a8
+  __TEXT.__swift5_reflstr: 0xa1c
+  __TEXT.__swift5_fieldmd: 0x8c0
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x120
   __TEXT.__swift5_proto: 0x328

   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_capture: 0x64
   __TEXT.__swift_as_entry: 0x5c
+  __TEXT.__swift_as_cont: 0xa0
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0xdb8
-  __TEXT.__eh_frame: 0x1aa0
-  __TEXT.__objc_classname: 0x358
-  __TEXT.__objc_methname: 0x1058
-  __TEXT.__objc_methtype: 0x266
-  __TEXT.__objc_stubs: 0x820
-  __DATA_CONST.__got: 0x238
+  __TEXT.__unwind_info: 0xd90
+  __TEXT.__eh_frame: 0x19e8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x428
+  __DATA_CONST.__objc_selrefs: 0x430
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x7d8
+  __DATA_CONST.__got: 0x238
   __AUTH_CONST.__const: 0x1868
   __AUTH_CONST.__cfstring: 0xbc0
-  __AUTH_CONST.__objc_const: 0x1210
+  __AUTH_CONST.__objc_const: 0x1220
+  __AUTH_CONST.__auth_got: 0x8c8
   __AUTH.__objc_data: 0x318
   __AUTH.__data: 0x218
   __DATA.__objc_ivar: 0x68
-  __DATA.__data: 0x9b0
+  __DATA.__data: 0x9b8
   __DATA.__bss: 0x5ed0
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x118

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 96EFA06B-71E0-3B6B-807C-7A223EEF5E3B
-  Functions: 1110
-  Symbols:   985
-  CStrings:  570
+  UUID: 733997C9-C28A-3309-B65E-81B9FD077B97
+  Functions: 1105
+  Symbols:   1036
+  CStrings:  309
 
Symbols:
+ +[DSSFeatureFlags isGuestModeCallingEnabled]
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.3
+ ___swift_memcpy17_8
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_DeviceSharingServices
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x28
+ _swift_release_n
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _symbolic SO3key______5valuet 21DeviceSharingServices14ObserversTableV11Observation33_FB91759BF284DF87C2A5A79FFF11CF42LLV
+ _symbolic SbSg
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_DeviceSharingServices
- _symbolic SO3key______5valuetSg 21DeviceSharingServices14ObserversTableV11Observation33_FB91759BF284DF87C2A5A79FFF11CF42LLV
CStrings:
+ " - applicationLibraryData: ["
+ "Copresence"
+ "GuestModeCallingEnabled"
+ "], guestModeCallingEnabled: "
+ "guestModeCallingEnabled"
- "#16@0:8"
- "$defaultActor"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16Q24"
- "@36@0:8q16@24B32"
- "@40@0:8:16@24@32"
- "@52@0:8@16@24@32@40B48"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "DSSAdditions"
- "DSSConstants"
- "DSSFeatureFlags"
- "DSSGuestPreferences"
- "DSSGuestUser"
- "DSSGuestUserModeNotificationRequest"
- "DSSGuestUserRemoteUnlockDevice"
- "DSSMutableGuestUser"
- "DSSSharingModeService"
- "I"
- "NSCoding"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "SBSRemoteAlertHandleObserver"
- "T#,R"
- "T@\"NSDate\",&,D,N"
- "T@\"NSDate\",R,N,V_lastSwitchTime"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_modelIdentifier"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_productVersion"
- "T@\"NSString\",R,N,V_reason"
- "T@\"NSString\",R,N,V_uniqueIdentifier"
- "T@\"NSUUID\",&,D,N"
- "T@\"NSUUID\",R,N,V_managedAssetsProfileUUID"
- "T@\"NSUUID\",R,N,V_uuid"
- "TB,D,N"
- "TB,D,N,GisTemporaryUser"
- "TB,R"
- "TB,R,N"
- "TB,R,N,GisTemporaryUser,V_temporaryUser"
- "TB,R,N,V_hasSeenGuestSafetyNotice"
- "TB,R,N,V_isPaired"
- "TQ,R"
- "TQ,R,N,V_notificationType"
- "Td,R,N"
- "URLForResource:withExtension:"
- "UUID"
- "UUIDString"
- "Version2 - applicationLibraryData: ["
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC21DeviceSharingServices11Application"
- "_TtC21DeviceSharingServices18ApplicationLibrary"
- "_TtC21DeviceSharingServices23AirPlayReceiverSettings"
- "_TtC21DeviceSharingServices23LiveActivityCoordinator"
- "_TtC21DeviceSharingServices26AirPlayReceiverCoordinator"
- "_TtC21DeviceSharingServices33GuestUserHandoverSetupCoordinator"
- "_TtC21DeviceSharingServicesP33_DCC69EBB8BA68A324D11B2F382DAF43C25RemoteAlertHandleObserver"
- "_TtCE21DeviceSharingServicesCSo8NSBundleP33_573015E15F19123B471575E1B451A46829deviceSharingServicesSentinel"
- "_applications"
- "_assetEnrolled"
- "_axOpened"
- "_clipOnsPresent"
- "_hasSeenGuestSafetyNotice"
- "_isPaired"
- "_lastSwitchTime"
- "_managedAssetsProfileUUID"
- "_mode"
- "_modelIdentifier"
- "_name"
- "_notificationType"
- "_numAppsOpened"
- "_openedApps"
- "_productVersion"
- "_reason"
- "_sessionIdentifier"
- "_sharingModeStartTime"
- "_smEnabled"
- "_soundIDEnded"
- "_soundIDStarted"
- "_store"
- "_synced"
- "_tccShown"
- "_temporaryUser"
- "_uniqueIdentifier"
- "_uuid"
- "activateWithContext:"
- "airPlayReceiverSettingsManager"
- "allocWithZone:"
- "autorelease"
- "boolValue"
- "bundleForClass:"
- "class"
- "code"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "count"
- "currentHandler"
- "d16@0:8"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "doesNotRecognizeSelector:"
- "domain"
- "dss_copyRetryable:"
- "dss_errorWithCode:"
- "dss_errorWithCode:userInfo:retryable:"
- "dss_isRetryable"
- "emitAXOpened"
- "emitAXOpened:"
- "emitGuestBeganInitialEnrollment:"
- "emitGuestReEnrolled:"
- "emitOpenedApps:"
- "emitScreenMirroring"
- "emitScreenMirroring:"
- "emitSessionEnded:"
- "emitSessionStarted:withOpenedApps:"
- "emitTCCShown:"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "failWithError:"
- "handleFailureInFunction:file:lineNumber:description:"
- "hash"
- "i"
- "identityForApplicationJobLabel:"
- "init"
- "initWithCoder:"
- "initWithDomain:code:userInfo:"
- "initWithReason:withType:"
- "initWithSceneProvidingProcess:configurationIdentifier:"
- "initWithTimeIntervalSince1970:"
- "initWithUniqueIdentifier:name:modelIdentifier:productVersion:isPaired:"
- "invalidate"
- "isActiveContinuation"
- "isBYOEEnabled"
- "isEqual:"
- "isGuestUserHandoverEnabled"
- "isKindOfClass:"
- "isLiveActivityActive"
- "isMemberOfClass:"
- "isMigrationEnabled"
- "isProxy"
- "isTemporaryUser"
- "isV2Enabled"
- "listeningForAlternateBonjourBrowsing"
- "localizedTitle"
- "lookupHandlesForDefinition:"
- "maximumAutoLockTimeoutDuration"
- "mutableCopy"
- "mutableCopyWithZone:"
- "new"
- "newGuestUser"
- "newHandleWithDefinition:configurationContext:"
- "now"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observers"
- "onRemoteAlertHandleDidDeactivate"
- "openApplication:withOptions:completion:"
- "optionsWithDictionary:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "playEndSound"
- "playStartSound"
- "previousAirPlayReceiverState"
- "proxCardState"
- "reason"
- "registerObserver:"
- "release"
- "remoteAlertHandle"
- "remoteAlertHandle:didInvalidateWithError:"
- "remoteAlertHandleDidActivate:"
- "remoteAlertHandleDidDeactivate:"
- "remoteAlertHandleObserver"
- "removeObjectForKey:"
- "resetCAMetrics"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "serviceWithDefaultShellEndpoint"
- "setHasSeenGuestSafetyNotice:"
- "setLastSwitchTime:"
- "setListeningForAlternateBonjourBrowsing:"
- "setManagedAssetsProfileUUID:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setSynced:"
- "setTemporaryUser:"
- "setUserInfo:"
- "setUuid:"
- "sharedInstance"
- "sharingModeDidEnd:"
- "sharingModeDidStart:withOpenedApps:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supportsSecureCoding"
- "timeIntervalSinceDate:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"SBSRemoteAlertHandle\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@?0@\"BSProcessHandle\"8@\"NSError\"16"
- "v32@0:8@\"SBSRemoteAlertHandle\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8Q16@24"
- "zone"

```
