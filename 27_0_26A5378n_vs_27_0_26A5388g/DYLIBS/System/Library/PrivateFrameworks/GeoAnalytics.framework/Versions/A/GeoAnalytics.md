## GeoAnalytics

> `/System/Library/PrivateFrameworks/GeoAnalytics.framework/Versions/A/GeoAnalytics`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2075.20.6.12.3
-  __TEXT.__text: 0x97dbc
-  __TEXT.__objc_methlist: 0x22bc
-  __TEXT.__const: 0x72c
+2075.20.6.12.8
+  __TEXT.__text: 0x99758
+  __TEXT.__objc_methlist: 0x2444
+  __TEXT.__const: 0x704
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__swift5_typeref: 0x4e
   __TEXT.__swift5_capture: 0x24

   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__gcc_except_tab: 0xa04
-  __TEXT.__cstring: 0xe136
-  __TEXT.__oslogstring: 0xdd8
-  __TEXT.__unwind_info: 0xfb0
+  __TEXT.__gcc_except_tab: 0x5b0
+  __TEXT.__cstring: 0xe180
+  __TEXT.__oslogstring: 0xe61
+  __TEXT.__unwind_info: 0x1048
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x5e40
-  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ec0
+  __DATA_CONST.__objc_selrefs: 0x3f60
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0xe20
-  __DATA_CONST.__got: 0x678
-  __AUTH_CONST.__const: 0x3788
-  __AUTH_CONST.__cfstring: 0x13ba0
-  __AUTH_CONST.__objc_const: 0x2890
+  __DATA_CONST.__got: 0x688
+  __AUTH_CONST.__const: 0x37a8
+  __AUTH_CONST.__cfstring: 0x13c00
+  __AUTH_CONST.__objc_const: 0x2d98
   __AUTH_CONST.__objc_intobj: 0x1c68
   __AUTH_CONST.__objc_dictobj: 0x4b0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x2e8
-  __AUTH_CONST.__auth_got: 0x3b8
-  __AUTH.__objc_data: 0x50
+  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x40
-  __DATA.__objc_ivar: 0x1a8
-  __DATA.__data: 0x310
-  __DATA.__bss: 0x70
+  __DATA.__objc_ivar: 0x1c4
+  __DATA.__data: 0x490
+  __DATA.__bss: 0x80
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1469
-  Symbols:   4661
-  CStrings:  2690
+  Functions: 1528
+  Symbols:   4793
+  CStrings:  2698
 
Symbols:
+ -[GEOAPFinderSession .cxx_destruct]
+ -[GEOAPFinderSession _clearTimer]
+ -[GEOAPFinderSession _handleExpiration]
+ -[GEOAPFinderSession _isValidSession:]
+ -[GEOAPFinderSession _updateSessionData]
+ -[GEOAPFinderSession currentSessionID]
+ -[GEOAPFinderSession dealloc]
+ -[GEOAPFinderSession finderSessionDataChanged]
+ -[GEOAPFinderSession initWithMonitor:]
+ -[GEOAPFinderSession initWithMonitor:timeProvider:sessionDataProvider:]
+ -[GEOAPFinderSession isValidSession:]
+ -[GEOAPFinderSessionDataProvider .cxx_destruct]
+ -[GEOAPFinderSessionDataProvider deregisterForChange:]
+ -[GEOAPFinderSessionDataProvider finderSessionData]
+ -[GEOAPFinderSessionDataProvider registerForChange:onQueue:]
+ -[GEOAPFinderSessionDataProvider sessionDuration]
+ -[GEOAPFinderSessionDataProvider valueChangedForGEOConfigKey:]
+ -[GEOAPFinderSessionTimeProvider dateNow]
+ -[GEOAPFinderSessionTimeProvider now]
+ -[GEOAPStateFactory actionButtonDetails]
+ -[GEOAPStateFactory applicationIdentifierShort]
+ -[GEOAPStateFactory carPlay]
+ -[GEOAPStateFactory curatedCollection]
+ -[GEOAPStateFactory deviceConnection]
+ -[GEOAPStateFactory deviceIdentifierHardwareClass]
+ -[GEOAPStateFactory deviceLocale]
+ -[GEOAPStateFactory deviceSettings_DailySettings]
+ -[GEOAPStateFactory deviceSettings_Long]
+ -[GEOAPStateFactory deviceSettings_Short]
+ -[GEOAPStateFactory extension]
+ -[GEOAPStateFactory lookAroundSummary]
+ -[GEOAPStateFactory lookAroundView]
+ -[GEOAPStateFactory mapLaunch]
+ -[GEOAPStateFactory mapRestore]
+ -[GEOAPStateFactory mapSettingsShort]
+ -[GEOAPStateFactory mapSettings]
+ -[GEOAPStateFactory mapUI]
+ -[GEOAPStateFactory mapViewLocation]
+ -[GEOAPStateFactory mapView]
+ -[GEOAPStateFactory mapsServer]
+ -[GEOAPStateFactory mapsUser]
+ -[GEOAPStateFactory market]
+ -[GEOAPStateFactory muninResourceLog]
+ -[GEOAPStateFactory pairedDeviceLong]
+ -[GEOAPStateFactory pairedDevice]
+ -[GEOAPStateFactory photoSubmissionDetails]
+ -[GEOAPStateFactory ratingPhotoSubmissionDetails]
+ -[GEOAPStateFactory ratingSubmissionDetails]
+ -[GEOAPStateFactory route]
+ -[GEOAPStateFactory suggestions]
+ -[GEOAPStateFactory tapEvent]
+ -[GEOAPStateFactory tileSet]
+ -[GEOAPStateFactory ugc]
+ GCC_except_table1070
+ GCC_except_table1095
+ GCC_except_table1097
+ GCC_except_table1115
+ GCC_except_table1119
+ GCC_except_table1121
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table129
+ GCC_except_table131
+ GCC_except_table1334
+ GCC_except_table1372
+ GCC_except_table166
+ GCC_except_table167
+ GCC_except_table36
+ GCC_except_table4
+ GCC_except_table56
+ GCC_except_table561
+ GCC_except_table565
+ GCC_except_table567
+ GCC_except_table570
+ GCC_except_table573
+ GCC_except_table576
+ GCC_except_table580
+ GCC_except_table581
+ GCC_except_table583
+ GCC_except_table592
+ GCC_except_table595
+ GCC_except_table598
+ GCC_except_table646
+ GCC_except_table652
+ GCC_except_table653
+ GCC_except_table662
+ GCC_except_table90
+ GCC_except_table94
+ GCC_except_table961
+ GCC_except_table966
+ GCC_except_table968
+ GEOGetGEOAPFinderSessionAnalyticsLog.log
+ GEOGetGEOAPFinderSessionAnalyticsLog.onceToken
+ OBJC_IVAR_$_GEOAPFinderSession._monitor
+ OBJC_IVAR_$_GEOAPFinderSession._q
+ OBJC_IVAR_$_GEOAPFinderSession._sessionData
+ OBJC_IVAR_$_GEOAPFinderSession._sessionDataProvider
+ OBJC_IVAR_$_GEOAPFinderSession._timeProvider
+ OBJC_IVAR_$_GEOAPFinderSession._timer
+ OBJC_IVAR_$_GEOAPFinderSessionDataProvider._delegate
+ OBJC_IVAR_$_GEOAPStateFactory._runningInMaps
+ _GEOGetGEOAPFinderSessionAnalyticsLog
+ _GeoUserSessionConfig_ACSNFinderSessionData
+ _OBJC_CLASS_$_GEOAPFinderSession
+ _OBJC_CLASS_$_GEOAPFinderSessionDataProvider
+ _OBJC_CLASS_$_GEOAPFinderSessionTimeProvider
+ _OBJC_CLASS_$_GEOAPSessionData
+ _OBJC_METACLASS_$_GEOAPFinderSession
+ _OBJC_METACLASS_$_GEOAPFinderSessionDataProvider
+ _OBJC_METACLASS_$_GEOAPFinderSessionTimeProvider
+ __71-[GEOAPFinderSession initWithMonitor:timeProvider:sessionDataProvider:]_block_invoke
+ __GEOConfigAddDelegateListenerForKey
+ __OBJC_$_INSTANCE_METHODS_GEOAPFinderSession
+ __OBJC_$_INSTANCE_METHODS_GEOAPFinderSessionDataProvider
+ __OBJC_$_INSTANCE_METHODS_GEOAPFinderSessionTimeProvider
+ __OBJC_$_INSTANCE_VARIABLES_GEOAPFinderSession
+ __OBJC_$_INSTANCE_VARIABLES_GEOAPFinderSessionDataProvider
+ __OBJC_$_PROP_LIST_GEOAPFinderSession
+ __OBJC_$_PROP_LIST_GEOAPFinderSessionDataProvider
+ __OBJC_$_PROP_LIST_GEOAPFinderSessionDataProviding
+ __OBJC_$_PROP_LIST_GEOAPFinderSessionTimeProvider
+ __OBJC_$_PROP_LIST_GEOAPTimeProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GEOAPFinderSessionDataDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GEOAPFinderSessionDataProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GEOAPTimeProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GEOConfigChangeListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GEOAPFinderSessionDataDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GEOAPFinderSessionDataProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GEOAPTimeProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GEOConfigChangeListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_GEOAPFinderSessionDataDelegate
+ __OBJC_$_PROTOCOL_REFS_GEOAPFinderSessionDataProviding
+ __OBJC_$_PROTOCOL_REFS_GEOAPTimeProviding
+ __OBJC_$_PROTOCOL_REFS_GEOConfigChangeListenerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_GEOAPFinderSession
+ __OBJC_CLASS_PROTOCOLS_$_GEOAPFinderSessionDataProvider
+ __OBJC_CLASS_PROTOCOLS_$_GEOAPFinderSessionTimeProvider
+ __OBJC_CLASS_RO_$_GEOAPFinderSession
+ __OBJC_CLASS_RO_$_GEOAPFinderSessionDataProvider
+ __OBJC_CLASS_RO_$_GEOAPFinderSessionTimeProvider
+ __OBJC_LABEL_PROTOCOL_$_GEOAPFinderSessionDataDelegate
+ __OBJC_LABEL_PROTOCOL_$_GEOAPFinderSessionDataProviding
+ __OBJC_LABEL_PROTOCOL_$_GEOAPTimeProviding
+ __OBJC_LABEL_PROTOCOL_$_GEOConfigChangeListenerDelegate
+ __OBJC_METACLASS_RO_$_GEOAPFinderSession
+ __OBJC_METACLASS_RO_$_GEOAPFinderSessionDataProvider
+ __OBJC_METACLASS_RO_$_GEOAPFinderSessionTimeProvider
+ __OBJC_PROTOCOL_$_GEOAPFinderSessionDataDelegate
+ __OBJC_PROTOCOL_$_GEOAPFinderSessionDataProviding
+ __OBJC_PROTOCOL_$_GEOAPTimeProviding
+ __OBJC_PROTOCOL_$_GEOConfigChangeListenerDelegate
+ ___37-[GEOAPFinderSession isValidSession:]_block_invoke
+ ___38-[GEOAPFinderSession currentSessionID]_block_invoke
+ ___71-[GEOAPFinderSession initWithMonitor:timeProvider:sessionDataProvider:]_block_invoke
+ ___GEOGetGEOAPFinderSessionAnalyticsLog_block_invoke
+ _createStateWithType
+ _dispatch_assert_queue$V2
+ _objc_msgSend$_clearTimer
+ _objc_msgSend$_handleExpiration
+ _objc_msgSend$_isValidSession:
+ _objc_msgSend$_updateSessionData
+ _objc_msgSend$bestReferenceTime
+ _objc_msgSend$createTime
+ _objc_msgSend$deregisterForChange:
+ _objc_msgSend$finderSessionData
+ _objc_msgSend$finderSessionDataChanged
+ _objc_msgSend$hasRotated
+ _objc_msgSend$initWithMonitor:timeProvider:sessionDataProvider:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$now
+ _objc_msgSend$registerForChange:onQueue:
+ _objc_msgSend$session:didExpireAt:
+ _objc_msgSend$sessionDuration
+ _objc_storeWeak
- GCC_except_table1011
- GCC_except_table1036
- GCC_except_table1038
- GCC_except_table1056
- GCC_except_table1060
- GCC_except_table1062
- GCC_except_table1275
- GCC_except_table1313
- GCC_except_table134
- GCC_except_table135
- GCC_except_table24
- GCC_except_table31
- GCC_except_table500
- GCC_except_table506
- GCC_except_table508
- GCC_except_table511
- GCC_except_table514
- GCC_except_table517
- GCC_except_table521
- GCC_except_table522
- GCC_except_table524
- GCC_except_table533
- GCC_except_table536
- GCC_except_table539
- GCC_except_table58
- GCC_except_table587
- GCC_except_table593
- GCC_except_table594
- GCC_except_table603
- GCC_except_table62
- GCC_except_table7
- GCC_except_table89
- GCC_except_table902
- GCC_except_table907
- GCC_except_table909
- GCC_except_table91
- GCC_except_table97
- GCC_except_table99
- OBJC_IVAR_$_GEOAPStateFactory._isolationQueue
- __ZN6gloria6TileId10FromLatLngERKdS2_RKh
- __ZNK6gloria6TileId16GetEncodedTileIdEv
- __ZNK6gloria6TileId6ToBBOXEv
CStrings:
+ "GEOAPFinderSession"
+ "TAP_DICTATION_ADD_STOP"
+ "TAP_SATELLITE_MODE_OFF"
+ "TAP_SATELLITE_MODE_ON"
+ "com.apple.geoapfindersession"
+ "session has expired"
+ "unexpected state : _sessionData has already rotated"
+ "unexpected state : should have _sessionData"
+ "updating timer state"
- "com.apple.GeoServices.Analytics.StateFactory"
```
