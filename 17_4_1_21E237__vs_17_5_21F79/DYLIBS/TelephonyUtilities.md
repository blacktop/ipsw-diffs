## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1431.500.151.2.13
-  __TEXT.__text: 0x119d1c
-  __TEXT.__auth_stubs: 0x1790
-  __TEXT.__objc_methlist: 0x1235c
-  __TEXT.__cstring: 0x1008d
-  __TEXT.__oslogstring: 0xdb3a
+1431.600.72.2.2
+  __TEXT.__text: 0x11aa80
+  __TEXT.__auth_stubs: 0x17b0
+  __TEXT.__objc_methlist: 0x1240c
+  __TEXT.__cstring: 0x100cd
+  __TEXT.__oslogstring: 0xdc01
   __TEXT.__const: 0x276
-  __TEXT.__gcc_except_tab: 0x1238
+  __TEXT.__gcc_except_tab: 0x124c
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x788
   __TEXT.__swift5_typeref: 0x1ee

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x4694
+  __TEXT.__unwind_info: 0x465c
   __TEXT.__eh_frame: 0xf8
   __TEXT.__objc_classname: 0x20d4
-  __TEXT.__objc_methname: 0x30a9f
+  __TEXT.__objc_methname: 0x30c77
   __TEXT.__objc_methtype: 0x6c88
-  __TEXT.__objc_stubs: 0x1ba20
-  __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__const: 0x2e98
+  __TEXT.__objc_stubs: 0x1bc00
+  __DATA_CONST.__got: 0x300
+  __DATA_CONST.__const: 0x2ec8
   __DATA_CONST.__objc_classlist: 0x660
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x3d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1fbf0
-  __DATA_CONST.__objc_selrefs: 0x8f18
+  __DATA_CONST.__objc_const: 0x1fc30
+  __DATA_CONST.__objc_selrefs: 0x8f88
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_classrefs: 0x7f8
   __DATA_CONST.__objc_superrefs: 0x580
   __DATA_CONST.__objc_arraydata: 0x120
-  __AUTH_CONST.__cfstring: 0xe2e0
+  __AUTH_CONST.__cfstring: 0xe320
   __AUTH_CONST.__objc_const: 0x5e70
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__const: 0x1e18
+  __AUTH_CONST.__const: 0x1e58
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0xbd8
+  __AUTH_CONST.__auth_got: 0xbe8
   __AUTH.__objc_data: 0x1d10
-  __AUTH.__data: 0x2d0
-  __DATA.__objc_ivar: 0x1338
-  __DATA.__data: 0x3268
-  __DATA.__bss: 0x5a0
-  __DATA.__common: 0x10
+  __AUTH.__data: 0x2c8
+  __DATA.__objc_ivar: 0x1344
+  __DATA.__data: 0x33a0
+  __DATA.__bss: 0x4d0
+  __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x22b0
-  __DATA_DIRTY.__bss: 0x228
+  __DATA_DIRTY.__bss: 0x200
+  - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7773
-  Symbols:   24332
-  CStrings:  11502
+  Functions: 7791
+  Symbols:   24399
+  CStrings:  11525
 
Symbols:
+ +[TUCallCapabilities isSimultaneousVoiceAndDataSupportedForSIMWithUUID:]
+ +[TUConversationLink featureFlags]
+ -[TUCall channelImageURL]
+ -[TUCall setChannelImageURL:]
+ -[TUCall supportsSimultaneousVoiceAndData]
+ -[TUCallCenter initWithQueue:wantsCallNotifications:]
+ -[TUCallCenter initWithQueue:wantsCallNotifications:featureFlags:]
+ -[TUCallNotificationManager initWithNotificationCenter:wantsCallNotifications:]
+ -[TUCallNotificationManager wantsCallNotifications]
+ -[TUCallServicesInterface initWithQueue:callCenter:wantsCallNotifications:]
+ -[TUConversationLink allInvitedMembersInContactsChecking:]
+ -[TUConversationLink displayName]
+ -[TUConversationLink fetchedResults]
+ -[TUConversationLink generateDisplayName]
+ -[TUFeatureFlags groupFaceTimeBlockEnabled]
+ -[TUFeatureFlags linkNamesEnabled]
+ -[TUFeatureFlags reportInitiatorEnabled]
+ -[TUProxyCall channelImageURL]
+ -[TUProxyCall setChannelImageURL:]
+ -[TUVideoDeviceController _postIsCinematicFramingAvailable:]
+ -[TUVideoDeviceController provider:dockKitTrackingDidChange:]
+ -[TUVideoDeviceControllerProvider centerStageAvailableChangedNotification:]
+ GCC_except_table124
+ GCC_except_table130
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table156
+ GCC_except_table194
+ GCC_except_table215
+ GCC_except_table220
+ GCC_except_table63
+ GCC_except_table66
+ _AVControlCenterModulesNotificationCenterStageUnavailableReasonsKey
+ _NSClassFromString
+ _OBJC_IVAR_$_TUCall._channelImageURL
+ _OBJC_IVAR_$_TUCallNotificationManager._wantsCallNotifications
+ _OBJC_IVAR_$_TUProxyCall._channelImageURL
+ _TUAudioRouteBluetoothProductIdentifierB465
+ __BSSafeCast
+ __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.303
+ __OBJC_$_PROP_LIST_TUFeatureFlags.307
+ __OBJC_$_PROP_LIST_TUVideoDeviceControllerProvider.242
+ ___34+[TUConversationLink featureFlags]_block_invoke
+ ___36-[TUConversationLink fetchedResults]_block_invoke
+ ___58-[TUConversationLink allInvitedMembersInContactsChecking:]_block_invoke
+ ___66-[TUCallCenter initWithQueue:wantsCallNotifications:featureFlags:]_block_invoke
+ ___68-[TUDynamicCallDisplayContext _initializeAsynchronousStateWithCall:]_block_invoke.39
+ ___68-[TUDynamicCallDisplayContext _initializeAsynchronousStateWithCall:]_block_invoke.49
+ ___68-[TUDynamicCallDisplayContext _initializeAsynchronousStateWithCall:]_block_invoke.49.cold.1
+ ___68-[TUDynamicCallDisplayContext _initializeAsynchronousStateWithCall:]_block_invoke_2.40
+ ___68-[TUDynamicCallDisplayContext _initializeAsynchronousStateWithCall:]_block_invoke_2.50
+ ___75-[TUCallServicesInterface initWithQueue:callCenter:wantsCallNotifications:]_block_invoke
+ ___block_descriptor_40_e8_32r_e55_v32?0"TUHandle"8"TUContactsDataProviderResult"16^B24lr32l8
+ ___block_literal_global.1499
+ ___block_literal_global.1505
+ ___block_literal_global.234
+ ___block_literal_global.267
+ ___block_literal_global.272
+ _featureFlags.flags
+ _featureFlags.onceToken
+ _fetchedResults._IMPreferredAccountForService
+ _fetchedResults._pred_IMPreferredAccountForServiceIMCore
+ _init._AVControlCenterVideoEffectsUnavailableReasonsDidChangeNotification
+ _objc_msgSend$_postIsCinematicFramingAvailable:
+ _objc_msgSend$aliases
+ _objc_msgSend$allInvitedMembersInContactsChecking:
+ _objc_msgSend$blockUntilConnected
+ _objc_msgSend$channelImageURL
+ _objc_msgSend$fetchedResults
+ _objc_msgSend$generateDisplayName
+ _objc_msgSend$initWithNotificationCenter:wantsCallNotifications:
+ _objc_msgSend$initWithQueue:callCenter:wantsCallNotifications:
+ _objc_msgSend$initWithQueue:wantsCallNotifications:
+ _objc_msgSend$initWithQueue:wantsCallNotifications:featureFlags:
+ _objc_msgSend$isSimultaneousVoiceAndDataSupportedForSIMWithUUID:
+ _objc_msgSend$languageCode
+ _objc_msgSend$linkNamesEnabled
+ _objc_msgSend$provider:dockKitTrackingDidChange:
+ _objc_msgSend$regionCode
+ _objc_msgSend$wantsCallNotifications
- -[TUCall postNotificationsAfterUpdatesInBlock:]
- -[TUCallCenter initWithQueue:featureFlags:]
- -[TUFeatureFlags callEndedUIBlockAndReportEnabled]
- -[TUFeatureFlags contactBlockAndReportEnabled]
- -[TUFeatureFlags faceTimeCallSpamReportAndBlockEnabled]
- -[TUFeatureFlags faceTimeCallSpamReportEnabled]
- -[TUFeatureFlags faceTimeGroupCallSpamReportEnabled]
- GCC_except_table123
- GCC_except_table129
- GCC_except_table132
- GCC_except_table138
- GCC_except_table141
- GCC_except_table144
- GCC_except_table155
- GCC_except_table193
- GCC_except_table214
- GCC_except_table219
- GCC_except_table55
- GCC_except_table65
- __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.309
- __OBJC_$_PROP_LIST_TUFeatureFlags.313
- __OBJC_$_PROP_LIST_TUVideoDeviceControllerProvider.236
- ___43-[TUCallCenter initWithQueue:featureFlags:]_block_invoke
- ___52-[TUCallServicesInterface initWithQueue:callCenter:]_block_invoke
- ___68-[TUDynamicCallDisplayContext _initializeAsynchronousStateWithCall:]_block_invoke.38
- ___68-[TUDynamicCallDisplayContext _initializeAsynchronousStateWithCall:]_block_invoke.48
- ___68-[TUDynamicCallDisplayContext _initializeAsynchronousStateWithCall:]_block_invoke.48.cold.1
- ___68-[TUDynamicCallDisplayContext _initializeAsynchronousStateWithCall:]_block_invoke_2.39
- ___68-[TUDynamicCallDisplayContext _initializeAsynchronousStateWithCall:]_block_invoke_2.49
- ___block_literal_global.1489
- ___block_literal_global.1495
- ___block_literal_global.231
- ___block_literal_global.258
- ___block_literal_global.263
- _objc_msgSend$initWithQueue:callCenter:
- _objc_msgSend$initWithQueue:featureFlags:
CStrings:
+ "%@-%@"
+ "AVControlCenterVideoEffectsUnavailableReasonsDidChangeNotification"
+ "DockKit tracking changed to %d"
+ "NSNumber"
+ "ShowsLinkNames"
+ "T@\"NSURL\",&,N,V_channelImageURL"
+ "TB,R,N,V_wantsCallNotifications"
+ "TUIsIDSAvailableForFaceTime supportsDisplayingFaceTimeVideoCalls: %@ IDSServiceAvailabilityController: %@ isFaceTimeServiceAvailable: %@"
+ "_channelImageURL"
+ "_postIsCinematicFramingAvailable:"
+ "_wantsCallNotifications"
+ "aliases"
+ "allInvitedMembersInContactsChecking:"
+ "blockUntilConnected"
+ "centerStageAvailableChangedNotification:"
+ "channelImageURL"
+ "currentLanguageIdentifier = %@"
+ "fetchedResults"
+ "generateDisplayName"
+ "groupFaceTimeBlock"
+ "groupFaceTimeBlockEnabled"
+ "initWithNotificationCenter:wantsCallNotifications:"
+ "initWithQueue:callCenter:wantsCallNotifications:"
+ "initWithQueue:wantsCallNotifications:"
+ "initWithQueue:wantsCallNotifications:featureFlags:"
+ "isSimultaneousVoiceAndDataSupportedForSIMWithUUID:"
+ "languageCode"
+ "linkNamesEnabled"
+ "provider:dockKitTrackingDidChange:"
+ "regionCode"
+ "reportInitiator"
+ "reportInitiatorEnabled"
+ "setChannelImageURL:"
+ "v32@?0@\"TUHandle\"8@\"TUContactsDataProviderResult\"16^B24"
+ "wantsCallNotifications"
+ "\x887G4"
+ "\x8e\x12&AB1"
+ "\xf0\xf0\x91"
- "callEndedUIBlockAndReport"
- "callEndedUIBlockAndReportEnabled"
- "contactBlockAndReport"
- "contactBlockAndReportEnabled"
- "faceTimeCallSpamReport"
- "faceTimeCallSpamReportAndBlock"
- "faceTimeCallSpamReportAndBlockEnabled"
- "faceTimeCallSpamReportEnabled"
- "faceTimeGroupCallSpamReport"
- "faceTimeGroupCallSpamReportEnabled"
- "initWithQueue:featureFlags:"
- "postNotificationsAfterUpdatesInBlock:"
- "\x877G4"
- "\x8e\x12%AB1"
- "\xf0\xf0\x81"

```
