## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-515.17.3.2.0
-  __TEXT.__text: 0x68ffc
+515.22.0.0.0
+  __TEXT.__text: 0x686e4
   __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x89c8
-  __TEXT.__const: 0x562
+  __TEXT.__objc_methlist: 0x89a0
+  __TEXT.__const: 0x552
   __TEXT.__cstring: 0x4f26
-  __TEXT.__oslogstring: 0x2e7b
+  __TEXT.__oslogstring: 0x2e6b
   __TEXT.__gcc_except_tab: 0x968
   __TEXT.__constg_swiftt: 0x1f8
   __TEXT.__swift5_typeref: 0x12f

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_fieldmd: 0x7c
-  __TEXT.__unwind_info: 0x1f38
+  __TEXT.__unwind_info: 0x1f30
   __TEXT.__objc_classname: 0x127b
-  __TEXT.__objc_methname: 0x11fcb
-  __TEXT.__objc_methtype: 0x2d49
-  __TEXT.__objc_stubs: 0xaf60
-  __DATA_CONST.__got: 0x7f0
+  __TEXT.__objc_methname: 0x1203b
+  __TEXT.__objc_methtype: 0x2d59
+  __TEXT.__objc_stubs: 0xb080
+  __DATA_CONST.__got: 0x7e8
   __DATA_CONST.__const: 0x1e00
   __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bf8
+  __DATA_CONST.__objc_selrefs: 0x3c30
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x2e8
   __AUTH_CONST.__auth_got: 0x628
-  __AUTH_CONST.__const: 0xae8
-  __AUTH_CONST.__cfstring: 0x4c00
-  __AUTH_CONST.__objc_const: 0x1ec78
+  __AUTH_CONST.__const: 0xac8
+  __AUTH_CONST.__cfstring: 0x4bc0
+  __AUTH_CONST.__objc_const: 0x1ec48
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x1ce0
   __AUTH.__data: 0x230
-  __DATA.__objc_ivar: 0x924
+  __DATA.__objc_ivar: 0x920
   __DATA.__data: 0x1fa0
   __DATA.__bss: 0x550
   __DATA.__common: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3F6A9224-A71B-3B26-9540-5955F30470C3
-  Functions: 3019
-  Symbols:   11250
-  CStrings:  5045
+  UUID: 5FAEE42C-3A2D-323F-B4E7-84AA162BF81D
+  Functions: 3018
+  Symbols:   11252
+  CStrings:  5049
 
Symbols:
+ +[CPAccNavUpdate _encodeNumber:forParameter:withEncoder:accNavType:]
+ +[CPAccNavUpdate _encodeNumber:forParameter:withEncoder:accNavType:].cold.1
+ +[CPAccNavUpdate _encodeNumber:forParameter:withEncoder:accNavType:].cold.2
+ -[CPNavigationManager vehicleStateManager:didUpdateRouteSharingUserEnabled:].cold.2
+ GCC_except_table93
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.347
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.348
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.350
+ ___47-[CPMapTemplate startNavigationSessionForTrip:]_block_invoke.38
+ ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke.359
+ ___50-[CPMapTemplate handleActionForControlIdentifier:]_block_invoke.51
+ ___51-[CPMapTemplate clientWaypointReceivedFromVehicle:]_block_invoke.146
+ ___51-[CPMapTemplate clientWaypointReceivedFromVehicle:]_block_invoke.147
+ ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.333
+ ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.333.cold.1
+ ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.339
+ ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.339.cold.1
+ ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.340
+ ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.340.cold.1
+ ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.312
+ ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.312.cold.1
+ ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.316
+ ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.321
+ ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.321.cold.1
+ ___58-[CPNavigationManager handleSharedDestination:completion:]_block_invoke.248
+ ___65-[CPNavigationManager initWithIdentifier:delegate:sessionStatus:]_block_invoke.201
+ ___block_literal_global.276
+ ___block_literal_global.279
+ ___block_literal_global.281
+ ___block_literal_global.284
+ ___block_literal_global.291
+ ___block_literal_global.293
+ ___block_literal_global.315
+ ___block_literal_global.323
+ ___block_literal_global.335
+ ___block_literal_global.342
+ ___block_literal_global.365
+ ___block_literal_global.63
+ _objc_msgSend$_encodeNumber:forParameter:withEncoder:accNavType:
+ _objc_msgSend$charValue
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$encodeInt:forKey:
+ _objc_msgSend$intValue
+ _objc_msgSend$longLongValue
+ _objc_msgSend$shortValue
+ _objc_msgSend$unsignedCharValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$unsignedShortValue
- -[CPNavigationManager cancelRerouting]
- -[CPNavigationManager sharingConsentChanged:]
- -[CPTrip sendsNavigationMetadata]
- -[CPTrip setSendsNavigationMetadata:]
- GCC_except_table96
- _$s7CarPlay17RouteSharingStateC11userEnabledSbvs
- _$sSo21CPVehicleStateManagerC7CarPlayE31didUpdateUserRouteSharingStatusyyF
- _$sSo21CPVehicleStateManagerC7CarPlayE31didUpdateUserRouteSharingStatusyyFTo
- _$sSo26CRBridgeRouteSharingStatusVSQSCSQ2eeoiySbx_xtFZTW
- _$sSo26CRBridgeRouteSharingStatusVSYSCSY8rawValue03RawF0QzvgTW
- _OBJC_CLASS_$_NSDistributedNotificationCenter
- _OBJC_IVAR_$_CPTrip._sendsNavigationMetadata
- ___38-[CPNavigationManager cancelRerouting]_block_invoke
- ___39-[CPNavigationManager _setupConnection]_block_invoke.358
- ___39-[CPNavigationManager _setupConnection]_block_invoke.359
- ___39-[CPNavigationManager _setupConnection]_block_invoke.361
- ___47-[CPMapTemplate startNavigationSessionForTrip:]_block_invoke.32
- ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke.370
- ___50-[CPMapTemplate handleActionForControlIdentifier:]_block_invoke.45
- ___51-[CPMapTemplate clientWaypointReceivedFromVehicle:]_block_invoke.140
- ___51-[CPMapTemplate clientWaypointReceivedFromVehicle:]_block_invoke.141
- ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.344
- ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.344.cold.1
- ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.350
- ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.350.cold.1
- ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.351
- ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.351.cold.1
- ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.323
- ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.323.cold.1
- ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.327
- ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.332
- ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.332.cold.1
- ___58-[CPNavigationManager handleSharedDestination:completion:]_block_invoke.257
- ___65-[CPNavigationManager initWithIdentifier:delegate:sessionStatus:]_block_invoke.210
- ___block_literal_global.285
- ___block_literal_global.290
- ___block_literal_global.292
- ___block_literal_global.297
- ___block_literal_global.299
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.306
- ___block_literal_global.326
- ___block_literal_global.334
- ___block_literal_global.346
- ___block_literal_global.364
- ___block_literal_global.376
- ___block_literal_global.57
- _objc_msgSend$didUpdateUserRouteSharingStatus
- _objc_msgSend$setUserEnabled:
CStrings:
+ "%s attempting to decode object of unknown type %@ primaryKey=%d accNavType=%ld"
+ "%s attempting to encode nil value of type %@ primaryKey=%d accNavType=%ld"
+ "%s attempting to encode value of unknown type %@ primaryKey=%d accNavType=%ld"
+ "%s: Dismissing Routesharing Popup"
+ "+[CPAccNavUpdate _decodeNumberForParameter:fromDecoder:accNavType:]"
+ "+[CPAccNavUpdate _encodeNumber:forParameter:withEncoder:accNavType:]"
+ "_encodeNumber:forParameter:withEncoder:accNavType:"
+ "charValue"
+ "encodeInt32:forKey:"
+ "encodeInt64:forKey:"
+ "encodeInt:forKey:"
+ "intValue"
+ "longLongValue"
+ "mapTemplateShouldProvideRouteSharing returned %@"
+ "shortValue"
+ "unsignedCharValue"
+ "unsignedLongLongValue"
+ "unsignedShortValue"
+ "v48@0:8@16@24@32q40"
- "%s failed: routeSharing.receivedAllValues=%{bool}d"
- "%s userEnabled=%{bool}d userRouteSharingStatus=%s"
- "CRPairedVehiclesDidChangeNotification"
- "CRRouteSharingConsentDidChangeNotificationName"
- "cancelRerouting"
- "cancelRerouting guidanceState: %{public}@"
- "cancelRerouting: setting guidance state to active"
- "cancelRerouting: state was rerouting, setting to active"
- "didSet userEnabled: %{bool}d routeSharing=%s"
- "didUpdateUserRouteSharingStatus"
- "didUpdateUserRouteSharingStatus()"
- "setUserEnabled:"
- "sharingConsentChanged:"

```
