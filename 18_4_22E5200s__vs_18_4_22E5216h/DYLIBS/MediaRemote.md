## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4024.510.28.1.0
-  __TEXT.__text: 0x2c1230
+4024.510.36.1.0
+  __TEXT.__text: 0x2c23c8
   __TEXT.__auth_stubs: 0x1620
-  __TEXT.__objc_methlist: 0x293d0
+  __TEXT.__objc_methlist: 0x293c0
   __TEXT.__const: 0x570
-  __TEXT.__cstring: 0x2a88b
-  __TEXT.__oslogstring: 0xd2a3
-  __TEXT.__gcc_except_tab: 0x62a8
+  __TEXT.__cstring: 0x2a798
+  __TEXT.__oslogstring: 0xd28d
+  __TEXT.__gcc_except_tab: 0x6348
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0xa970
-  __TEXT.__objc_classname: 0x4a08
-  __TEXT.__objc_methname: 0x48d94
-  __TEXT.__objc_methtype: 0x8a76
-  __TEXT.__objc_stubs: 0x26140
-  __DATA_CONST.__got: 0x1298
-  __DATA_CONST.__const: 0xa4a8
-  __DATA_CONST.__objc_classlist: 0x1110
+  __TEXT.__unwind_info: 0xa990
+  __TEXT.__objc_classname: 0x4a18
+  __TEXT.__objc_methname: 0x48f42
+  __TEXT.__objc_methtype: 0x8a97
+  __TEXT.__objc_stubs: 0x26280
+  __DATA_CONST.__got: 0x12a0
+  __DATA_CONST.__const: 0xa528
+  __DATA_CONST.__objc_classlist: 0x1118
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe370
+  __DATA_CONST.__objc_selrefs: 0xe350
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xf58
   __DATA_CONST.__objc_arraydata: 0x228
   __AUTH_CONST.__auth_got: 0xb20
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x31a0
-  __AUTH_CONST.__cfstring: 0x205a0
-  __AUTH_CONST.__objc_const: 0x42d80
+  __AUTH_CONST.__const: 0x31e0
+  __AUTH_CONST.__cfstring: 0x20460
+  __AUTH_CONST.__objc_const: 0x42e80
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x7850
+  __AUTH.__objc_data: 0x78a0
   __AUTH.__data: 0x160
-  __DATA.__objc_ivar: 0x3008
+  __DATA.__objc_ivar: 0x3020
   __DATA.__data: 0x1a90
-  __DATA.__bss: 0x8c0
+  __DATA.__bss: 0x8b0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3250
   __DATA_DIRTY.__data: 0x1b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 19480
-  Symbols:   23301
-  CStrings:  19055
+  Functions: 19482
+  Symbols:   23304
+  CStrings:  19054
 
Symbols:
+ _MRMediaRemotePlaybackSessionIsMigrationPossible
+ _NSDebugDescriptionErrorKey
- _MRMediaRemotePlaybackSessionMigrate
- _MRMediaRemotePlaybackSessionMigrateForOrigin
- _MRMediaRemotePlaybackSessionMigrateWithRequest
- _MRMediaRemotePlaybackSessionRequestSupportedType
- _MRMediaRemotePlaybackSessionRequestSupportedTypeForOrigin
- _MRPlaybackSessionMigrateCopyCorrespondingPlayerPath
- _MRPlaybackSessionMigrateCopyCurrentTypes
- _MRPlaybackSessionMigrateCopySupportedTypeMatch
- _MRPlaybackSessionMigrateCopySupportedTypes
CStrings:
+ "\x01\x15"
+ "%{public}@"
+ "05ac:110"
+ "@\"MRCommandInfo\""
+ "@32@0:8@?16@?24"
+ "AudioAccessory1,"
+ "AudioAccessory5,"
+ "AudioAccessory6,"
+ "CurrentTypes.insersect(SupportedTypes) is empty currentTypes=%@ supportedTypes=%@"
+ "Destination.setPlaybackSession.options[supportedTypes] is empty"
+ "Failed to find symbol with model: %{public}@ variant options: %lu error: %{public}@ symbol:%{public}@"
+ "Failed to resolve destination player path"
+ "Failed to resolve player path, but did not receive an error: sourcePlayerPath=%@"
+ "Failed to resolve source player path"
+ "OneShotQHO"
+ "Partially resolved player path mising bundleID: destinationPlayerPath=%@"
+ "Partially resolved player path mising origin: destinationPlayerPath=%@"
+ "Source.setPlaybackSession.options[currentTypes] is empty"
+ "T@\"MRCommandInfo\",R,N,V_destinationSetPlaybackSessionCommandInfo"
+ "T@\"NSError\",R,C,N,V_error"
+ "T@\"NSString\",&,N,V_delegateAccountDataType"
+ "T@\"NSString\",R,C,N,V_playbackSessionType"
+ "T@?,C,N,V_activeRouteIDsChangedCallback"
+ "T@?,C,N,V_isLocalDeviceAirPlayActiveCallback"
+ "[MRActiveRoutesObserver] LocalDeviceAirPlayActive -> %u"
+ "_MRPSMRecipe"
+ "_activeRouteIDsChangedCallback"
+ "_destinationSetPlaybackSessionCommandInfo"
+ "_handleActiveDeviceInfoDidChange:"
+ "_isLocalDeviceAirPlayActiveCallback"
+ "_localDeviceAirPlayActive"
+ "_onWorkerQueue_reevaluateAPA"
+ "_onWorkerQueue_reevaluateASE"
+ "_reevaluateAPA"
+ "_reevaluateASE"
+ "activeRouteIDsChangedCallback"
+ "addHomePodWithModelIdentifier:"
+ "destinationSetPlaybackSessionCommandInfo"
+ "failed to get device info for source"
+ "failed to get supported commands for destination"
+ "failed to get supported commands for source"
+ "groupSessionDelayedInitializationEnabled"
+ "homePodHomeTheaterCompositionWithHomePodModelIdentifier:"
+ "homePodStereoPairCompositionWithModelIdentifier:"
+ "initWithActiveRouteIDsChangedCallback:isLocalDeviceAirplayActiveChangedCallback:"
+ "isHomePodMiniDevice"
+ "isLocalDeviceAirPlayActive"
+ "isLocalDeviceAirPlayActiveCallback"
+ "legacySetPlaybackSessionWithSessionType:"
+ "msv_compactDescription"
+ "notPossibleWithError:"
+ "oneShotSetPlaybackSessionWithCommandInfo:"
+ "outputDevicesForUID:"
+ "setActiveRouteIDsChangedCallback:"
+ "setIsLocalDeviceAirPlayActive:"
+ "setIsLocalDeviceAirPlayActiveCallback:"
+ "symbolNameForType:fillVariant:"
+ "symbolNameForType:fillVariant:otherVariantOptions:"
+ "v32@?0@\"MRPlayerPath\"8@\"MRPlayerPath\"16@\"NSError\"24"
+ "v32@?0@\"MRPlayerPath\"8@\"MRPlayerPath\"16@\"_MRPSMRecipe\"24"
+ "void _MRPSMDetermineRecipe(MRPlayerPath *__strong, MROrigin *__strong, __strong dispatch_queue_t, void (^__strong)(MRPlayerPath *__strong, MRPlayerPath *__strong, _MRPSMRecipe *__strong))"
- "%@ options do not match. source=%@ currentType=%@ destination=%@ supportedTypes=%@"
- "76,4384"
- "AllowAllClientUIConnections"
- "AudioAccessory6"
- "ConnectedClientAuditTokens"
- "ConnectedClientPIDs"
- "DefaultSupportedCommands"
- "ExpectedClientAuditTokens"
- "ExpectedClientPIDs"
- "Failed to find symbol with model: %{public}@ variant options: %lu error: %{public}@"
- "GroupSessionASEAssertionEnabled"
- "JSONClientUIDs"
- "LastBootUUID"
- "LastPlayingDate"
- "LocalPlaybackState"
- "MRNowPlayingPlayerPathRef MRPlaybackSessionMigrateCopyCorrespondingPlayerPath(MRNowPlayingPlayerPathRef, MROriginRef)"
- "Non resolved playerPath"
- "PersonalDeviceState"
- "RecentGroupSessionParticipantsPepper"
- "ShouldInitializeGenericBonjourService"
- "ShouldInitializeTVBonjourService"
- "SupportedCommands do not allow migration because %@"
- "T@\"NSData\",&,N,V_delegateAccountDataType"
- "T@\"NSDictionary\",&,N"
- "UseDebugAVRouteWithoutVolumeControl"
- "[ConcreteOutputContext] Ignoring request to attempt logical device recovery because APSync API is enabled."
- "_onWorkerQueue_reevaluate"
- "_reevaluate"
- "allowAllClientUIConnections"
- "connectedClientAuditTokens"
- "defaultSupportedCommandsData"
- "defaultSupportedCommandsDataForClient:"
- "destination %@ does not support %@ (source currentTypes = %@)"
- "destinationPlayerPath %@ was resolved to %@"
- "expectedClientAuditTokens"
- "groupSessionASEAssertionEnabled"
- "isB520Device"
- "isHomeTheaterB520Device"
- "jsonClientUIDs"
- "lastBootUUID"
- "personalDeviceState"
- "recentGroupSessionParticipantsPepper"
- "setConnectedClientAuditTokens:"
- "setExpectedClientAuditTokens:"
- "setInteger:forKey:"
- "setLastBootUUID:"
- "setLocalLastPlayingDate:"
- "setLocalPlaybackState:"
- "setPersonalDeviceState:"
- "shouldInitializeGenericBonjourService"
- "shouldInitializeTelevisionBonjourService"
- "source %@ does not support %@ (destination supportedTypes = %@)"
- "sourcePlayerPath %@ was resolved to %@. Likely there is no now playing app?"
- "stringForKey:"
- "symbolForType:fillVariant:"
- "symbolForType:fillVariant:otherVariantOptions:"
- "updateDefaultSupportedCommandsData:forClient:"
- "useAPSyncAPI"
- "useDebugAVRouteWithoutVolumeControl"
- "v40@?0@\"MRPlayerPath\"8@\"MRPlayerPath\"16@\"NSString\"24@\"NSError\"32"
- "v40@?0^v8^v16^{__CFString=}24^{__CFError=}32"
- "void _MRMediaRemotePlaybackSessionRequestSupportedType(MRPlayerPath *__strong, MRPlayerPath *__strong, __strong dispatch_queue_t, void (^__strong)(NSString *__strong, NSError *__strong))"

```
