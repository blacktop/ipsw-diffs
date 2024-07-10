## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/Versions/A/TVRemoteCore`

```diff

-443.0.16.0.0
-  __TEXT.__text: 0x562c0
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x66b4
-  __TEXT.__const: 0x1f0
-  __TEXT.__gcc_except_tab: 0x9e8
-  __TEXT.__cstring: 0x450b
-  __TEXT.__oslogstring: 0x579d
-  __TEXT.__unwind_info: 0x1358
-  __TEXT.__objc_classname: 0xbef
-  __TEXT.__objc_methname: 0xda43
-  __TEXT.__objc_methtype: 0x2689
-  __TEXT.__objc_stubs: 0x83a0
-  __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x6e0
-  __DATA_CONST.__objc_classlist: 0x320
+443.0.25.0.0
+  __TEXT.__text: 0x5a9c0
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_methlist: 0x6abc
+  __TEXT.__const: 0x200
+  __TEXT.__gcc_except_tab: 0xac8
+  __TEXT.__cstring: 0x46c2
+  __TEXT.__oslogstring: 0x5d38
+  __TEXT.__unwind_info: 0x1470
+  __TEXT.__objc_classname: 0xc50
+  __TEXT.__objc_methname: 0xe423
+  __TEXT.__objc_methtype: 0x271b
+  __TEXT.__objc_stubs: 0x8ae0
+  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__const: 0x6f0
+  __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xd8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f20
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x288
+  __DATA_CONST.__objc_selrefs: 0x3140
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0x400
-  __AUTH_CONST.__const: 0x1158
-  __AUTH_CONST.__cfstring: 0x61c0
-  __AUTH_CONST.__objc_const: 0xd258
+  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__const: 0x12e8
+  __AUTH_CONST.__cfstring: 0x6440
+  __AUTH_CONST.__objc_const: 0xd9c0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x1f40
-  __DATA.__objc_ivar: 0x794
-  __DATA.__data: 0xa30
+  __AUTH.__objc_data: 0x2030
+  __DATA.__objc_ivar: 0x7f0
+  __DATA.__data: 0xa90
   __DATA.__bss: 0x158
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2443
-  Symbols:   5402
-  CStrings:  883
+  Functions: 2553
+  Symbols:   5656
+  CStrings:  905
 
Symbols:
+ +[TVRCRottenTomatoesReview rottenTomatoesReviewWithDictionary:]
+ +[TVRCRottenTomatoesReview supportsSecureCoding]
+ +[TVRCTimedMetadata _timedMetadataWithIdentifier:rawData:expectsTimedMetadata:]
+ +[TVRCTimedMetadata supportsSecureCoding]
+ +[TVRCTimedMetadata timedMetadataWithIdentifier:rawData:]
+ +[TVRCTimedMetadata timedMetadataWithIdentifier:rawData:expectsTimedMetadata:]
+ -[TVRCDeviceQuery startWithCompletionHandler:]
+ -[TVRCHMHomeObserver accessory:service:didUpdateValueForCharacteristic:]
+ -[TVRCHMServiceWrapper _readValueForCharacteristic:completionHandler:]
+ -[TVRCHMServiceWrapper _readValueForCharacteristic:completionHandler:].cold.1
+ -[TVRCHMServiceWrapper _sendMuteKey]
+ -[TVRCHMServiceWrapper _serviceActiveStateChanged:]
+ -[TVRCHMServiceWrapper _togglePowerButton]
+ -[TVRCHMServiceWrapper _updateMuteState]
+ -[TVRCHMServiceWrapper _updatePowerState]
+ -[TVRCHMServiceWrapper _writeRequestForCharacteristic:withValue:]
+ -[TVRCHMServiceWrapper currentActiveState]
+ -[TVRCHMServiceWrapper isTVAwake]
+ -[TVRCHMServiceWrapper muteCharacteristic]
+ -[TVRCHMServiceWrapper muteEnabled]
+ -[TVRCHMServiceWrapper setCurrentActiveState:]
+ -[TVRCHMServiceWrapper setMuteCharacteristic:]
+ -[TVRCHMServiceWrapper setMuteEnabled:]
+ -[TVRCHMServiceWrapper supportsMute]
+ -[TVRCHMServiceWrapper supportsPowerButton]
+ -[TVRCMediaInfo releaseDate]
+ -[TVRCMediaInfo rottenTomatoesReview]
+ -[TVRCMediaInfo setReleaseDate:]
+ -[TVRCMediaInfo setRottenTomatoesReview:]
+ -[TVRCNowPlayingMetadata imageURLTemplate]
+ -[TVRCNowPlayingMetadata releaseDate]
+ -[TVRCNowPlayingMetadata rottenTomatoesReview]
+ -[TVRCNowPlayingMetadata setImageURLTemplate:]
+ -[TVRCNowPlayingMetadata setReleaseDate:]
+ -[TVRCNowPlayingMetadata setRottenTomatoesReview:]
+ -[TVRCRottenTomatoesReview .cxx_destruct]
+ -[TVRCRottenTomatoesReview audienceScore]
+ -[TVRCRottenTomatoesReview averageRating]
+ -[TVRCRottenTomatoesReview consensus]
+ -[TVRCRottenTomatoesReview copyWithZone:]
+ -[TVRCRottenTomatoesReview encodeWithCoder:]
+ -[TVRCRottenTomatoesReview freshnessLevel]
+ -[TVRCRottenTomatoesReview freshness]
+ -[TVRCRottenTomatoesReview initWithCoder:]
+ -[TVRCRottenTomatoesReview isEqual:]
+ -[TVRCRottenTomatoesReview isEqualToRottenTomatoesReview:]
+ -[TVRCRottenTomatoesReview numberOfFreshReviews]
+ -[TVRCRottenTomatoesReview numberOfRottenReviews]
+ -[TVRCRottenTomatoesReview percentage]
+ -[TVRCRottenTomatoesReview setAudienceScore:]
+ -[TVRCRottenTomatoesReview setAverageRating:]
+ -[TVRCRottenTomatoesReview setConsensus:]
+ -[TVRCRottenTomatoesReview setFreshness:]
+ -[TVRCRottenTomatoesReview setNumberOfFreshReviews:]
+ -[TVRCRottenTomatoesReview setNumberOfRottenReviews:]
+ -[TVRCRottenTomatoesReview setPercentage:]
+ -[TVRCTimedMetadata .cxx_destruct]
+ -[TVRCTimedMetadata copyWithZone:]
+ -[TVRCTimedMetadata encodeWithCoder:]
+ -[TVRCTimedMetadata expectsTimedMetadata]
+ -[TVRCTimedMetadata hasExpectsTimedMetadata]
+ -[TVRCTimedMetadata identifier]
+ -[TVRCTimedMetadata initWithCoder:]
+ -[TVRCTimedMetadata initWithIdentifier:rawData:expectsTimedMetadata:]
+ -[TVRCTimedMetadata isEqual:]
+ -[TVRCTimedMetadata isEqualToTimedMetadata:]
+ -[TVRCTimedMetadata rawData]
+ -[TVRCTimedMetadata setExpectsTimedMetadata:]
+ -[TVRCTimedMetadata setHasExpectsTimedMetadata:]
+ -[TVRCTimedMetadata setIdentifier:]
+ -[TVRCTimedMetadata setRawData:]
+ -[TVRCTimedMetadataManager .cxx_destruct]
+ -[TVRCTimedMetadataManager connection]
+ -[TVRCTimedMetadataManager currentTimedMetadata]
+ -[TVRCTimedMetadataManager proxy]
+ -[TVRCTimedMetadataManager updateTimedMetadata:]
+ -[TVRCXPCClient _cancelRetryTimer]
+ -[TVRCXPCClient _invalidateConnection]
+ -[TVRCXPCClient _startDeviceQueryRetryTimerWithEventHander:]
+ -[TVRCXPCClient beginDeviceQueryWithResponse:]
+ -[TVRCXPCClient deviceQueryRetryTimerFired]
+ -[TVRCXPCClient deviceQueryRetryTimer]
+ -[TVRCXPCClient setDeviceQueryRetryTimer:]
+ -[TVRCXPCClient setDeviceQueryRetryTimerFired:]
+ GCC_except_table20
+ GCC_except_table22
+ GCC_except_table26
+ GCC_except_table28
+ GCC_except_table54
+ OBJC_IVAR_$_TVRCHMServiceWrapper._currentActiveState
+ OBJC_IVAR_$_TVRCHMServiceWrapper._muteCharacteristic
+ OBJC_IVAR_$_TVRCHMServiceWrapper._muteEnabled
+ OBJC_IVAR_$_TVRCMediaInfo._releaseDate
+ OBJC_IVAR_$_TVRCMediaInfo._rottenTomatoesReview
+ OBJC_IVAR_$_TVRCNowPlayingMetadata._imageURLTemplate
+ OBJC_IVAR_$_TVRCNowPlayingMetadata._releaseDate
+ OBJC_IVAR_$_TVRCNowPlayingMetadata._rottenTomatoesReview
+ OBJC_IVAR_$_TVRCRottenTomatoesReview._audienceScore
+ OBJC_IVAR_$_TVRCRottenTomatoesReview._averageRating
+ OBJC_IVAR_$_TVRCRottenTomatoesReview._consensus
+ OBJC_IVAR_$_TVRCRottenTomatoesReview._freshness
+ OBJC_IVAR_$_TVRCRottenTomatoesReview._numberOfFreshReviews
+ OBJC_IVAR_$_TVRCRottenTomatoesReview._numberOfRottenReviews
+ OBJC_IVAR_$_TVRCRottenTomatoesReview._percentage
+ OBJC_IVAR_$_TVRCTimedMetadata._expectsTimedMetadata
+ OBJC_IVAR_$_TVRCTimedMetadata._hasExpectsTimedMetadata
+ OBJC_IVAR_$_TVRCTimedMetadata._identifier
+ OBJC_IVAR_$_TVRCTimedMetadata._rawData
+ OBJC_IVAR_$_TVRCTimedMetadataManager._connection
+ OBJC_IVAR_$_TVRCTimedMetadataManager._currentTimedMetadata
+ OBJC_IVAR_$_TVRCXPCClient._deviceQueryRetryTimer
+ OBJC_IVAR_$_TVRCXPCClient._deviceQueryRetryTimerFired
+ _HMCharacteristicTypeMute
+ _HMCharacteristicTypeVolume
+ _OBJC_CLASS_$_TVRCRottenTomatoesReview
+ _OBJC_CLASS_$_TVRCTimedMetadata
+ _OBJC_CLASS_$_TVRCTimedMetadataManager
+ _OBJC_METACLASS_$_TVRCRottenTomatoesReview
+ _OBJC_METACLASS_$_TVRCTimedMetadata
+ _OBJC_METACLASS_$_TVRCTimedMetadataManager
+ _TVRCMatchPointServiceActiveStateChangedNotification
+ _TVRCMatchPointServiceActiveStateKey
+ __33-[TVRCTimedMetadataManager proxy]_block_invoke.cold.1
+ __36-[TVRCHMServiceWrapper _sendMuteKey]_block_invoke.cold.1
+ __38-[TVRCTimedMetadataManager connection]_block_invoke.46
+ __38-[TVRCTimedMetadataManager connection]_block_invoke.46.cold.1
+ __38-[TVRCTimedMetadataManager connection]_block_invoke.cold.1
+ __40-[TVRCHMServiceWrapper _updateMuteState]_block_invoke.cold.1
+ __41-[TVRCHMServiceWrapper _updatePowerState]_block_invoke.cold.1
+ __41-[TVRCXPCClient _setupConnectionIfNeeded]_block_invoke.33
+ __41-[TVRCXPCClient _setupConnectionIfNeeded]_block_invoke.34
+ __41-[TVRCXPCClient _setupConnectionIfNeeded]_block_invoke.34.cold.1
+ __42-[TVRCHMServiceWrapper _togglePowerButton]_block_invoke.cold.1
+ __46-[TVRCXPCClient beginDeviceQueryWithResponse:]_block_invoke.10
+ __53-[TVRCHMHomeObserver _readCharacteristic:completion:]_block_invoke.24
+ __53-[TVRCHMServiceWrapper _writeValue:toCharacteristic:]_block_invoke.36
+ __54-[TVRCHMServiceWrapper _setCharacteristicsForService:]_block_invoke.cold.1
+ __57-[TVRCHMServiceWrapper _checkVolumeServicesForAccessory:]_block_invoke.cold.1
+ __63+[TVRCRottenTomatoesReview rottenTomatoesReviewWithDictionary:]_block_invoke.304
+ __70-[TVRCHMServiceWrapper _readValueForCharacteristic:completionHandler:]_block_invoke.40
+ __70-[TVRCHMServiceWrapper _readValueForCharacteristic:completionHandler:]_block_invoke.40.cold.1
+ __OBJC_$_CLASS_METHODS_TVRCRottenTomatoesReview
+ __OBJC_$_CLASS_METHODS_TVRCTimedMetadata
+ __OBJC_$_CLASS_PROP_LIST_TVRCRottenTomatoesReview
+ __OBJC_$_CLASS_PROP_LIST_TVRCTimedMetadata
+ __OBJC_$_INSTANCE_METHODS_TVRCRottenTomatoesReview
+ __OBJC_$_INSTANCE_METHODS_TVRCTimedMetadata
+ __OBJC_$_INSTANCE_METHODS_TVRCTimedMetadataManager
+ __OBJC_$_INSTANCE_VARIABLES_TVRCRottenTomatoesReview
+ __OBJC_$_INSTANCE_VARIABLES_TVRCTimedMetadata
+ __OBJC_$_INSTANCE_VARIABLES_TVRCTimedMetadataManager
+ __OBJC_$_PROP_LIST_TVRCRottenTomatoesReview
+ __OBJC_$_PROP_LIST_TVRCTimedMetadata
+ __OBJC_$_PROP_LIST_TVRCTimedMetadataManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TVRCTimedMetadataUpdating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TVRCTimedMetadataUpdating
+ __OBJC_$_PROTOCOL_REFS_TVRCTimedMetadataUpdating
+ __OBJC_CLASS_PROTOCOLS_$_TVRCRottenTomatoesReview
+ __OBJC_CLASS_PROTOCOLS_$_TVRCTimedMetadata
+ __OBJC_CLASS_PROTOCOLS_$_TVRCTimedMetadataManager
+ __OBJC_CLASS_RO_$_TVRCRottenTomatoesReview
+ __OBJC_CLASS_RO_$_TVRCTimedMetadata
+ __OBJC_CLASS_RO_$_TVRCTimedMetadataManager
+ __OBJC_LABEL_PROTOCOL_$_TVRCTimedMetadataUpdating
+ __OBJC_METACLASS_RO_$_TVRCRottenTomatoesReview
+ __OBJC_METACLASS_RO_$_TVRCTimedMetadata
+ __OBJC_METACLASS_RO_$_TVRCTimedMetadataManager
+ __OBJC_PROTOCOL_$_TVRCTimedMetadataUpdating
+ __OBJC_PROTOCOL_REFERENCE_$_TVRCTimedMetadataUpdating
+ ___33-[TVRCTimedMetadataManager proxy]_block_invoke
+ ___36-[TVRCHMServiceWrapper _sendMuteKey]_block_invoke
+ ___38-[TVRCTimedMetadataManager connection]_block_invoke
+ ___40-[TVRCHMServiceWrapper _updateMuteState]_block_invoke
+ ___41-[TVRCHMServiceWrapper _updatePowerState]_block_invoke
+ ___42-[TVRCHMServiceWrapper _togglePowerButton]_block_invoke
+ ___46-[TVRCXPCClient beginDeviceQueryWithResponse:]_block_invoke
+ ___54-[TVRCHMServiceWrapper _setCharacteristicsForService:]_block_invoke
+ ___57-[TVRCHMServiceWrapper _checkVolumeServicesForAccessory:]_block_invoke
+ ___60-[TVRCXPCClient _startDeviceQueryRetryTimerWithEventHander:]_block_invoke
+ ___63+[TVRCRottenTomatoesReview rottenTomatoesReviewWithDictionary:]_block_invoke
+ ___70-[TVRCHMServiceWrapper _readValueForCharacteristic:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8l
+ ___block_descriptor_40_e8_32s_e28_"NSNumber"16?0"NSString"8l
+ ___block_descriptor_40_e8_32s_e28_"NSString"16?0"NSString"8l
+ ___block_descriptor_41_e8_32w_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32bs40w_e8_v12?0B8l
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32w_e17_v16?0"NSError"8l
+ __block_literal_global.49
+ __dispatch_source_type_timer
+ _dispatch_activate
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _objc_msgSend$_cancelRetryTimer
+ _objc_msgSend$_invalidateConnection
+ _objc_msgSend$_sendMuteKey
+ _objc_msgSend$_startDeviceQueryRetryTimerWithEventHander:
+ _objc_msgSend$_timedMetadataWithIdentifier:rawData:expectsTimedMetadata:
+ _objc_msgSend$_togglePowerButton
+ _objc_msgSend$_updateMuteState
+ _objc_msgSend$_updatePowerState
+ _objc_msgSend$activate
+ _objc_msgSend$activeCharacteristic
+ _objc_msgSend$audienceScore
+ _objc_msgSend$averageRating
+ _objc_msgSend$beginDeviceQueryWithResponse:
+ _objc_msgSend$characteristic
+ _objc_msgSend$connection
+ _objc_msgSend$consensus
+ _objc_msgSend$currentActiveState
+ _objc_msgSend$deviceQueryRetryTimerFired
+ _objc_msgSend$enableNotification:completionHandler:
+ _objc_msgSend$freshness
+ _objc_msgSend$hasExpectsTimedMetadata
+ _objc_msgSend$initWithIdentifier:rawData:expectsTimedMetadata:
+ _objc_msgSend$isEqualToDate:
+ _objc_msgSend$isEqualToRottenTomatoesReview:
+ _objc_msgSend$isEqualToTimedMetadata:
+ _objc_msgSend$isTVAwake
+ _objc_msgSend$muteCharacteristic
+ _objc_msgSend$muteEnabled
+ _objc_msgSend$numberOfFreshReviews
+ _objc_msgSend$numberOfRottenReviews
+ _objc_msgSend$percentage
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$proxy
+ _objc_msgSend$rawData
+ _objc_msgSend$readValueWithCompletionHandler:
+ _objc_msgSend$releaseDate
+ _objc_msgSend$request
+ _objc_msgSend$rottenTomatoesReview
+ _objc_msgSend$rottenTomatoesReviewWithDictionary:
+ _objc_msgSend$scanDouble:
+ _objc_msgSend$setAudienceScore:
+ _objc_msgSend$setAverageRating:
+ _objc_msgSend$setConsensus:
+ _objc_msgSend$setCurrentActiveState:
+ _objc_msgSend$setDeviceQueryRetryTimerFired:
+ _objc_msgSend$setFreshness:
+ _objc_msgSend$setHasExpectsTimedMetadata:
+ _objc_msgSend$setMuteEnabled:
+ _objc_msgSend$setNumberOfFreshReviews:
+ _objc_msgSend$setNumberOfRottenReviews:
+ _objc_msgSend$setPercentage:
+ _objc_msgSend$setRawData:
+ _objc_msgSend$setReleaseDate:
+ _objc_msgSend$setRottenTomatoesReview:
+ _objc_msgSend$startWithCompletionHandler:
+ _objc_msgSend$supportsMute
+ _objc_msgSend$supportsPowerButton
+ _objc_msgSend$updateTimedMetadata:
+ _objc_msgSend$writeValue:completionHandler:
- -[TVRCXPCClient beginDeviceQuery]
- GCC_except_table46
- _HMCharacteristicTypeVolumeControlType
- __41-[TVRCXPCClient _setupConnectionIfNeeded]_block_invoke.29
- __41-[TVRCXPCClient _setupConnectionIfNeeded]_block_invoke.30
- __41-[TVRCXPCClient _setupConnectionIfNeeded]_block_invoke.30.cold.1
- __53-[TVRCHMHomeObserver _readCharacteristic:completion:]_block_invoke.17
- __53-[TVRCHMServiceWrapper _writeValue:toCharacteristic:]_block_invoke.30
- __block_literal_global.33
- _objc_msgSend$beginDeviceQuery
CStrings:
+ "@\"NSNumber\"16@?0@\"NSString\"8"
+ "@\"NSString\"16@?0@\"NSString\"8"
+ "CertifiedFresh"
+ "Rotten"
+ "TVRCMatchPointServiceActiveStateChangedNotification"
+ "TVRCMatchPointServiceActiveStateKey"
+ "audienceScore"
+ "averageRating"
+ "consensus"
+ "freshness"
+ "hasExpectsTimedMetadata"
+ "numFreshReviews"
+ "numRottenReviews"
+ "numberOfFreshReviews"
+ "numberOfRottenReviews"
+ "percentage"
+ "rawData"
+ "releaseDate"
+ "rottenTomatoesReview"
+ "rottenTomatoesReviews"
+ "tomatometerFreshness"
+ "tomatometerPercentage"
+ "tv-remote"
- "wlk"

```
