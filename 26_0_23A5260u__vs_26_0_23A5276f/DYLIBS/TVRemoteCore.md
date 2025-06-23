## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-548.0.1.0.0
-  __TEXT.__text: 0x5f608
-  __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_methlist: 0x82cc
-  __TEXT.__const: 0x200
-  __TEXT.__gcc_except_tab: 0xc4c
-  __TEXT.__cstring: 0x4e87
-  __TEXT.__oslogstring: 0x6ae0
-  __TEXT.__unwind_info: 0x1600
-  __TEXT.__objc_classname: 0xcef
-  __TEXT.__objc_methname: 0xf58d
-  __TEXT.__objc_methtype: 0x2954
-  __TEXT.__objc_stubs: 0x98a0
-  __DATA_CONST.__got: 0x558
-  __DATA_CONST.__const: 0x1610
-  __DATA_CONST.__objc_classlist: 0x370
+548.0.4.0.0
+  __TEXT.__text: 0x62858
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_methlist: 0x856c
+  __TEXT.__const: 0x230
+  __TEXT.__gcc_except_tab: 0xd6c
+  __TEXT.__cstring: 0x4fcb
+  __TEXT.__oslogstring: 0x6d2c
+  __TEXT.__unwind_info: 0x16f0
+  __TEXT.__objc_classname: 0xd39
+  __TEXT.__objc_methname: 0xf74d
+  __TEXT.__objc_methtype: 0x29d8
+  __TEXT.__objc_stubs: 0x9940
+  __DATA_CONST.__got: 0x568
+  __DATA_CONST.__const: 0x1798
+  __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xe8
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ae0
+  __DATA_CONST.__objc_selrefs: 0x3b20
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x2d0
+  __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x5a8
-  __AUTH_CONST.__const: 0x4f8
-  __AUTH_CONST.__cfstring: 0x6b80
-  __AUTH_CONST.__objc_const: 0xcae0
-  __AUTH_CONST.__objc_intobj: 0x1b0
+  __AUTH_CONST.__auth_got: 0x5b8
+  __AUTH_CONST.__const: 0x518
+  __AUTH_CONST.__cfstring: 0x6c60
+  __AUTH_CONST.__objc_const: 0xcf80
+  __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x2120
-  __DATA.__objc_ivar: 0x878
-  __DATA.__data: 0xaf0
+  __AUTH_CONST.__objc_doubleobj: 0x40
+  __AUTH.__objc_data: 0x21c0
+  __DATA.__objc_ivar: 0x8a8
+  __DATA.__data: 0xb50
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x78

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C9DADF4C-8CA8-3483-952C-2C6A02972E10
-  Functions: 2719
-  Symbols:   8837
-  CStrings:  5571
+  UUID: C694CB3E-0487-3001-BC80-22712AB3ECF1
+  Functions: 2788
+  Symbols:   9043
+  CStrings:  5626
 
Symbols:
+ -[TVRCMediaControlSession .cxx_destruct]
+ -[TVRCMediaControlSession _activateWithCompletion:]
+ -[TVRCMediaControlSession _activateWithCompletion:].cold.1
+ -[TVRCMediaControlSession _handleMediaControlEvent:]
+ -[TVRCMediaControlSession _invalidate]
+ -[TVRCMediaControlSession activateWithCompletion:]
+ -[TVRCMediaControlSession init]
+ -[TVRCMediaControlSession invalidate]
+ -[TVRCMediaControlSession mediaCaptionSettingGetFromDestinationID:completion:]
+ -[TVRCMediaControlSession mediaCaptionSettingSet:destinationID:completion:]
+ -[TVRCMediaControlSession mediaCommand:destinationID:completion:]
+ -[TVRCMediaControlSession mediaControlFlagsChangedHandler]
+ -[TVRCMediaControlSession mediaControlFlags]
+ -[TVRCMediaControlSession mediaGetVolumeFromDestinationID:completion:]
+ -[TVRCMediaControlSession mediaSetVolume:destinationID:completion:]
+ -[TVRCMediaControlSession mediaSkipBySeconds:destinationID:completion:]
+ -[TVRCMediaControlSession messenger]
+ -[TVRCMediaControlSession setMediaControlFlagsChangedHandler:]
+ -[TVRCMediaControlSession setMessenger:]
+ -[TVRCMediaEventsManager .cxx_destruct]
+ -[TVRCMediaEventsManager _captionSettingForButtonEvent:]
+ -[TVRCMediaEventsManager _commandForMediaButtonEvent:]
+ -[TVRCMediaEventsManager _refreshCaptionState]
+ -[TVRCMediaEventsManager _setupMediaCommands:]
+ -[TVRCMediaEventsManager activateWithCompletionHandler:]
+ -[TVRCMediaEventsManager currentSetting]
+ -[TVRCMediaEventsManager eventHandler]
+ -[TVRCMediaEventsManager initWithCompanionLinkClient:supportsDirectCaptionQueries:eventHandler:]
+ -[TVRCMediaEventsManager invalidate]
+ -[TVRCMediaEventsManager mediaCommands]
+ -[TVRCMediaEventsManager mediaSession]
+ -[TVRCMediaEventsManager sendMediaEvent:]
+ -[TVRCMediaEventsManager setCurrentSetting:]
+ -[TVRCMediaEventsManager setEventHandler:]
+ -[TVRCMediaEventsManager setMediaCommands:]
+ -[TVRCMediaEventsManager setMediaSession:]
+ -[TVRCMediaEventsManager setSupportsDirectCaptionQueries:]
+ -[TVRCMediaEventsManager setVolumeCommands:]
+ -[TVRCMediaEventsManager supportedCaptionEvents]
+ -[TVRCMediaEventsManager supportedMediaCommands]
+ -[TVRCMediaEventsManager supportsDirectCaptionQueries]
+ -[TVRCMediaEventsManager volumeCommands]
+ -[TVRCMediaEventsManager volumeSupported]
+ -[TVRCRPCompanionLinkClientWrapper _setupLegacyMediaEventsManager]
+ -[TVRCRPCompanionLinkClientWrapper _setupMediaEventsManager]
+ -[TVRCRapportMediaEventsManager activateWithCompletionHandler:]
+ GCC_except_table109
+ GCC_except_table115
+ GCC_except_table130
+ GCC_except_table7
+ GCC_except_table82
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table96
+ _CFDictionaryGetDouble
+ _CFDictionaryGetInt64
+ _OBJC_CLASS_$_TVRCMediaControlSession
+ _OBJC_CLASS_$_TVRCMediaEventsManager
+ _OBJC_IVAR_$_TVRCMediaControlSession._dispatchQueue
+ _OBJC_IVAR_$_TVRCMediaControlSession._invalidateCalled
+ _OBJC_IVAR_$_TVRCMediaControlSession._mediaControlFlags
+ _OBJC_IVAR_$_TVRCMediaControlSession._mediaControlFlagsChangedHandler
+ _OBJC_IVAR_$_TVRCMediaControlSession._messenger
+ _OBJC_IVAR_$_TVRCMediaControlSession._registeredMediaControlInterest
+ _OBJC_IVAR_$_TVRCMediaEventsManager._currentSetting
+ _OBJC_IVAR_$_TVRCMediaEventsManager._eventHandler
+ _OBJC_IVAR_$_TVRCMediaEventsManager._mediaCommands
+ _OBJC_IVAR_$_TVRCMediaEventsManager._mediaSession
+ _OBJC_IVAR_$_TVRCMediaEventsManager._supportsDirectCaptionQueries
+ _OBJC_IVAR_$_TVRCMediaEventsManager._volumeCommands
+ _OBJC_METACLASS_$_TVRCMediaControlSession
+ _OBJC_METACLASS_$_TVRCMediaEventsManager
+ _TVRCFetchMediaControlStatus
+ _TVRCMediaControlCommandID
+ _TVRCMediaControlStatus
+ _TVRCMessageKeyMediaCaptionSetting
+ _TVRCMessageKeyMediaControlCommand
+ _TVRCMessageKeyMediaControlFlags
+ _TVRCMessageKeySkipSeconds
+ _TVRCMessageKeyVolume
+ __OBJC_$_INSTANCE_METHODS_TVRCMediaControlSession
+ __OBJC_$_INSTANCE_METHODS_TVRCMediaEventsManager
+ __OBJC_$_INSTANCE_VARIABLES_TVRCMediaControlSession
+ __OBJC_$_INSTANCE_VARIABLES_TVRCMediaEventsManager
+ __OBJC_$_PROP_LIST_TVRCMediaControlSession
+ __OBJC_$_PROP_LIST_TVRCMediaEventsManager
+ __OBJC_$_PROP_LIST_TVRCMediaEventsManaging
+ __OBJC_$_PROTOCOL_CLASS_METHODS_TVRCMediaEventsManaging
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TVRCMediaEventsManaging
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TVRCMediaEventsManaging
+ __OBJC_$_PROTOCOL_REFS_TVRCMediaEventsManaging
+ __OBJC_CLASS_PROTOCOLS_$_TVRCMediaEventsManager
+ __OBJC_CLASS_PROTOCOLS_$_TVRCRapportMediaEventsManager
+ __OBJC_CLASS_RO_$_TVRCMediaControlSession
+ __OBJC_CLASS_RO_$_TVRCMediaEventsManager
+ __OBJC_LABEL_PROTOCOL_$_TVRCMediaEventsManaging
+ __OBJC_METACLASS_RO_$_TVRCMediaControlSession
+ __OBJC_METACLASS_RO_$_TVRCMediaEventsManager
+ __OBJC_PROTOCOL_$_TVRCMediaEventsManaging
+ ___37-[TVRCMediaControlSession invalidate]_block_invoke
+ ___41-[TVRCMediaEventsManager sendMediaEvent:]_block_invoke
+ ___41-[TVRCMediaEventsManager sendMediaEvent:]_block_invoke.6
+ ___41-[TVRCMediaEventsManager sendMediaEvent:]_block_invoke.6.cold.1
+ ___41-[TVRCMediaEventsManager sendMediaEvent:]_block_invoke.7
+ ___41-[TVRCMediaEventsManager sendMediaEvent:]_block_invoke.7.cold.1
+ ___41-[TVRCMediaEventsManager sendMediaEvent:]_block_invoke.cold.1
+ ___46-[TVRCMediaEventsManager _refreshCaptionState]_block_invoke
+ ___46-[TVRCMediaEventsManager _refreshCaptionState]_block_invoke.cold.1
+ ___48-[TVRCRapportMediaEventsManager sendMediaEvent:]_block_invoke.6
+ ___48-[TVRCRapportMediaEventsManager sendMediaEvent:]_block_invoke.6.cold.1
+ ___50-[TVRCMediaControlSession activateWithCompletion:]_block_invoke
+ ___51-[TVRCMediaControlSession _activateWithCompletion:]_block_invoke
+ ___51-[TVRCMediaControlSession _activateWithCompletion:]_block_invoke_2
+ ___51-[TVRCMediaControlSession _activateWithCompletion:]_block_invoke_2.cold.1
+ ___56-[TVRCMediaEventsManager activateWithCompletionHandler:]_block_invoke
+ ___56-[TVRCMediaEventsManager activateWithCompletionHandler:]_block_invoke.cold.1
+ ___60-[TVRCRPCompanionLinkClientWrapper _launchApplicationOrURL:]_block_invoke.156
+ ___60-[TVRCRPCompanionLinkClientWrapper _launchApplicationOrURL:]_block_invoke.156.cold.1
+ ___60-[TVRCRPCompanionLinkClientWrapper _setupMediaEventsManager]_block_invoke
+ ___60-[TVRCRPCompanionLinkClientWrapper _setupMediaEventsManager]_block_invoke.123
+ ___60-[TVRCRPCompanionLinkClientWrapper _setupMediaEventsManager]_block_invoke.123.cold.1
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.149
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.149.cold.1
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.150
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.150.cold.1
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.151
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.151.cold.1
+ ___63-[TVRCRapportMediaEventsManager activateWithCompletionHandler:]_block_invoke
+ ___63-[TVRCRapportMediaEventsManager activateWithCompletionHandler:]_block_invoke.cold.1
+ ___65-[TVRCMediaControlSession mediaCommand:destinationID:completion:]_block_invoke
+ ___66-[TVRCRPCompanionLinkClientWrapper _setupLegacyMediaEventsManager]_block_invoke
+ ___66-[TVRCRPCompanionLinkClientWrapper _setupLegacyMediaEventsManager]_block_invoke.125
+ ___66-[TVRCRPCompanionLinkClientWrapper _setupLegacyMediaEventsManager]_block_invoke.125.cold.1
+ ___67-[TVRCMediaControlSession mediaSetVolume:destinationID:completion:]_block_invoke
+ ___70-[TVRCMediaControlSession mediaGetVolumeFromDestinationID:completion:]_block_invoke
+ ___71-[TVRCMediaControlSession mediaSkipBySeconds:destinationID:completion:]_block_invoke
+ ___75-[TVRCMediaControlSession mediaCaptionSettingSet:destinationID:completion:]_block_invoke
+ ___78-[TVRCMediaControlSession mediaCaptionSettingGetFromDestinationID:completion:]_block_invoke
+ ___96-[TVRCMediaEventsManager initWithCompanionLinkClient:supportsDirectCaptionQueries:eventHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8
+ ___block_descriptor_48_e8_32bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8ls32l8s40l8w48l8
+ ___block_literal_global.127
+ ___block_literal_global.141
+ _objc_msgSend$_handleMediaControlEvent:
+ _objc_msgSend$_setupLegacyMediaEventsManager
+ _objc_msgSend$_setupMediaEventsManager
+ _objc_msgSend$activateWithCompletionHandler:
+ _objc_msgSend$messenger
- GCC_except_table110
- GCC_except_table120
- GCC_except_table6
- GCC_except_table83
- GCC_except_table91
- GCC_except_table99
- ___103-[TVRCRapportMediaEventsManager initWithCompanionLinkClient:supportsDirectCaptionQueries:eventHandler:]_block_invoke.3
- ___103-[TVRCRapportMediaEventsManager initWithCompanionLinkClient:supportsDirectCaptionQueries:eventHandler:]_block_invoke.3.cold.1
- ___48-[TVRCRapportMediaEventsManager sendMediaEvent:]_block_invoke.8
- ___48-[TVRCRapportMediaEventsManager sendMediaEvent:]_block_invoke.8.cold.1
- ___60-[TVRCRPCompanionLinkClientWrapper _launchApplicationOrURL:]_block_invoke.152
- ___60-[TVRCRPCompanionLinkClientWrapper _launchApplicationOrURL:]_block_invoke.152.cold.1
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.145
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.145.cold.1
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.146
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.146.cold.1
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.147
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.147.cold.1
- ___65-[TVRCRPCompanionLinkClientWrapper _setupFeatureServicesIfNeeded]_block_invoke.123
- ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8ls32l8w40l8
- ___block_literal_global.137
CStrings:
+ "### Activate failed: %{public}@\n"
+ "-[TVRCMediaEventsManager _commandForMediaButtonEvent:]"
+ "-[TVRCMediaEventsManager _refreshCaptionState]"
+ "-[TVRCMediaEventsManager _setupMediaCommands:]"
+ "@\"<TVRCMediaEventsManaging>\""
+ "@\"TVRCMediaControlSession\""
+ "@36@0:8@\"RPCompanionLinkClient\"16B24@?<v@?>28"
+ "Activated"
+ "FetchMediaControlStatus"
+ "FetchMediaControlStatus failed: %{public}@"
+ "Found the same device over a different link. Creating a new device impl"
+ "Invalidate: Interest %s\n"
+ "MediaCaptionSetting"
+ "MediaControl event: %llu, %d"
+ "MediaControlCommand"
+ "MediaControlFlags"
+ "MediaControlFlagsVolume available for <%{public}@>"
+ "MediaControlFlagsVolume not available for companionLinkClient <%{public}@>"
+ "MediaControlStatus"
+ "MessageKeySkipSeconds"
+ "MessageKeyVolume"
+ "No media caption setting"
+ "No volume"
+ "Received request response for FetchMediaControlStatus, response %{public}@, error %{public}@"
+ "Setting up TVRCMediaEventsManager"
+ "Setting up legacy TVRCRapportMediaEventsManager"
+ "T@\"<TVRCMediaEventsManaging>\",&,N,V_mediaManager"
+ "T@\"TVRCMediaControlSession\",&,N,V_mediaSession"
+ "T@?,C,N,V_mediaControlFlagsChangedHandler"
+ "TQ,R,N,V_mediaControlFlags"
+ "TVRCMediaControlSession"
+ "TVRCMediaEventsManager"
+ "TVRCMediaEventsManager eventHandlerCalled"
+ "TVRCMediaEventsManager is not supported on the device - %@"
+ "TVRCMediaEventsManager timed out waiting for volume:%d or siri:%d settings, meaning it is unsupported"
+ "TVRCMediaEventsManager volume control is: %@"
+ "TVRCMediaEventsManaging"
+ "TVRCRapportMediaEventsManager eventHandlerCalled"
+ "TVRCRapportMediaEventsManager is not supported - %@"
+ "TVRCRapportMediaEventsManager volume control is: %@"
+ "_handleMediaControlEvent:"
+ "_invalidateCalled"
+ "_mediaControlFlags"
+ "_mediaControlFlagsChangedHandler"
+ "_registeredMediaControlInterest"
+ "_setupLegacyMediaEventsManager"
+ "_setupMediaEventsManager"
+ "activateWithCompletionHandler:"
+ "mediaControlFlagsChangedHandler"
+ "mediaGetVolumeFromDestinationID:completion:"
+ "mediaSetVolume:destinationID:completion:"
+ "new"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v36@0:8i16@20@?28"
+ "v40@0:8d16@24@?32"
- "@\"TVRCRapportMediaEventsManager\""
- "Found the same device over a different link. Creating a new dveice impl"
- "Setting up _TVRCRapportMediaEventsManager"
- "T@\"TVRCRapportMediaEventsManager\",&,N,V_mediaManager"
- "_TVRCRapportMediaEventsManager eventHandlerCalled"
- "_TVRCRapportMediaEventsManager timed out waiting for volume:%d or siri:%d settings, meaning it is unsupported"
- "_TVRCRapportMediaEventsManager volume control is %@"

```
