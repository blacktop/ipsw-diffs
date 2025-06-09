## MobileStoreDemoKit

> `/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit`

```diff

-1445.122.3.0.0
-  __TEXT.__text: 0x2f098
+1604.0.0.0.0
+  __TEXT.__text: 0x2fbd8
   __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x2414
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x1078
-  __TEXT.__oslogstring: 0x3681
-  __TEXT.__cstring: 0x6e6b
-  __TEXT.__unwind_info: 0xb58
+  __TEXT.__objc_methlist: 0x24f4
+  __TEXT.__const: 0xe0
+  __TEXT.__gcc_except_tab: 0x1114
+  __TEXT.__oslogstring: 0x36dd
+  __TEXT.__cstring: 0x70aa
+  __TEXT.__unwind_info: 0xba8
   __TEXT.__objc_classname: 0x3cf
-  __TEXT.__objc_methname: 0x609d
-  __TEXT.__objc_methtype: 0xc3d
-  __TEXT.__objc_stubs: 0x4400
+  __TEXT.__objc_methname: 0x6349
+  __TEXT.__objc_methtype: 0xcec
+  __TEXT.__objc_stubs: 0x4580
   __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x5d8
+  __DATA_CONST.__const: 0x618
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1880
+  __DATA_CONST.__objc_selrefs: 0x18f8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x340
   __AUTH_CONST.__auth_got: 0x610
   __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x4ca0
-  __AUTH_CONST.__objc_const: 0x3810
+  __AUTH_CONST.__cfstring: 0x4d60
+  __AUTH_CONST.__objc_const: 0x38b8
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0x23c
+  __DATA.__objc_ivar: 0x248
   __DATA.__data: 0x9e0
   __DATA.__bss: 0xe0
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B4B3513-B309-3D62-9AAB-C0AFE495070B
-  Functions: 1142
-  Symbols:   3875
-  CStrings:  3028
+  UUID: 6CE0A331-7DF7-3626-8D64-50A29558B3A6
+  Functions: 1164
+  Symbols:   3917
+  CStrings:  3071
 
Symbols:
+ -[MSDKManagedDevice isStoreOpen:withError:]
+ -[MSDKManagedDevice isStoreOpen:withError:].cold.1
+ -[MSDKManagedDevice isStoreOpen:withError:].cold.2
+ -[MSDKManagedDevice nextStoreCloseDate:withError:]
+ -[MSDKManagedDevice nextStoreCloseDate:withError:].cold.1
+ -[MSDKManagedDevice nextStoreCloseDate:withError:].cold.2
+ -[MSDKManagedDevice nextStoreCloseDate:withError:].cold.3
+ -[MSDKManagedDevice nextStoreOpenDate:withError:]
+ -[MSDKManagedDevice nextStoreOpenDate:withError:].cold.1
+ -[MSDKManagedDevice nextStoreOpenDate:withError:].cold.2
+ -[MSDKManagedDevice nextStoreOpenDate:withError:].cold.3
+ -[MSDKManagedDevice preferencesFileExists]
+ -[MSDKManagedDevice readPreferencesFileObjectForKey:]
+ -[MSDKManagedDevice(FeatureFlag) isScreenDarkHoursEnabled]
+ -[MSDKPeerDemoAXSettings liveTranscription]
+ -[MSDKPeerDemoAXSettings setLiveTranscription:]
+ -[MSDKPeerDemoDevice batteryCharging]
+ -[MSDKPeerDemoDevice externalPowerSourceConnected]
+ -[MSDKPeerDemoDevice setBatteryCharging:]
+ -[MSDKPeerDemoDevice setExternalPowerSourceConnected:]
+ -[MSDKPeerDemoDeviceManager enableMuseBuddyResetOnPeer:value:withCompletion:]
+ -[MSDKPeerDemoDeviceManager enableMuseBuddyResetOnPeer:value:withCompletion:].cold.1
+ -[MSDKPeerDemoDeviceManager getIconImagesOfVisibleAppsOnPeer:height:width:scale:withCompletion:]
+ -[MSDKPeerDemoDeviceManager getIconImagesOfVisibleAppsOnPeer:height:width:scale:withCompletion:].cold.1
+ -[MSDKPeerDemoDeviceManager setLanguageAndRegionOnPeer:languageCode:regionCode:withCompletion:]
+ -[MSDKPeerDemoDeviceManager setLanguageAndRegionOnPeer:languageCode:regionCode:withCompletion:].cold.1
+ GCC_except_table101
+ GCC_except_table105
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table54
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table83
+ GCC_except_table85
+ GCC_except_table87
+ GCC_except_table89
+ GCC_except_table91
+ GCC_except_table95
+ GCC_except_table97
+ _OBJC_IVAR_$_MSDKPeerDemoAXSettings._liveTranscription
+ _OBJC_IVAR_$_MSDKPeerDemoDevice._batteryCharging
+ _OBJC_IVAR_$_MSDKPeerDemoDevice._externalPowerSourceConnected
+ ___53-[MSDKManagedDevice handleContentUpdateStatus:event:]_block_invoke.195
+ ___56-[MSDKPeerDemoDeviceManager _setUpXPCConnectionIfNeeded]_block_invoke.157
+ ___56-[MSDKPeerDemoDeviceManager _setUpXPCConnectionIfNeeded]_block_invoke.157.cold.1
+ ___77-[MSDKPeerDemoDeviceManager enableMuseBuddyResetOnPeer:value:withCompletion:]_block_invoke
+ ___95-[MSDKPeerDemoDeviceManager setLanguageAndRegionOnPeer:languageCode:regionCode:withCompletion:]_block_invoke
+ ___96-[MSDKPeerDemoDeviceManager getIconImagesOfVisibleAppsOnPeer:height:width:scale:withCompletion:]_block_invoke
+ ___96-[MSDKPeerDemoDeviceManager getIconImagesOfVisibleAppsOnPeer:height:width:scale:withCompletion:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ _kMSDKPeerDemoAXSettingsPropertyLiveTranscription
+ _kMSDKPeerDemoDevicePropertyBatteryCharging
+ _kMSDKPeerDemoDevicePropertyExternalPowerSourceConnected
+ _objc_msgSend$batteryCharging
+ _objc_msgSend$enableMuseBuddyResetOnPeer:value:withCompletion:
+ _objc_msgSend$externalPowerSourceConnected
+ _objc_msgSend$getIconImagesOfVisibleAppsOnPeerOfID:height:width:scale:withCompletion:
+ _objc_msgSend$isStoreOpen:withError:
+ _objc_msgSend$liveTranscription
+ _objc_msgSend$nextStoreCloseDate:withError:
+ _objc_msgSend$nextStoreOpenDate:withError:
+ _objc_msgSend$setBatteryCharging:
+ _objc_msgSend$setExternalPowerSourceConnected:
+ _objc_msgSend$setLanguageAndRegionOnPeer:languageCode:regionCode:withCompletion:
+ _objc_msgSend$setLiveTranscription:
- -[MSDKManagedDevice isStoreOpen:].cold.1
- -[MSDKManagedDevice isStoreOpen:].cold.2
- -[MSDKManagedDevice nextStoreCloseDate:].cold.1
- -[MSDKManagedDevice nextStoreCloseDate:].cold.2
- -[MSDKManagedDevice nextStoreCloseDate:].cold.3
- -[MSDKManagedDevice nextStoreOpenDate:].cold.1
- -[MSDKManagedDevice nextStoreOpenDate:].cold.2
- -[MSDKManagedDevice nextStoreOpenDate:].cold.3
- GCC_except_table133
- GCC_except_table135
- GCC_except_table55
- GCC_except_table60
- GCC_except_table68
- GCC_except_table77
- GCC_except_table78
- GCC_except_table80
- GCC_except_table84
- GCC_except_table86
- GCC_except_table88
- GCC_except_table90
- GCC_except_table92
- GCC_except_table94
- GCC_except_table98
- ___53-[MSDKManagedDevice handleContentUpdateStatus:event:]_block_invoke.194
- ___56-[MSDKPeerDemoDeviceManager _setUpXPCConnectionIfNeeded]_block_invoke.149
- ___56-[MSDKPeerDemoDeviceManager _setUpXPCConnectionIfNeeded]_block_invoke.149.cold.1
CStrings:
+ "%s: called - value: %{bool}d"
+ "%s: called:  languageCode: %{public}@ - regionCode: %{public}@"
+ "-[MSDKManagedDevice isStoreOpen:withError:]"
+ "-[MSDKManagedDevice nextStoreCloseDate:withError:]"
+ "-[MSDKManagedDevice nextStoreOpenDate:withError:]"
+ "-[MSDKPeerDemoDeviceManager enableMuseBuddyResetOnPeer:value:withCompletion:]"
+ "-[MSDKPeerDemoDeviceManager getIconImagesOfVisibleAppsOnPeer:height:width:scale:withCompletion:]"
+ "-[MSDKPeerDemoDeviceManager setLanguageAndRegionOnPeer:languageCode:regionCode:withCompletion:]"
+ "<%@[%p]: Identifier=%@ DeviceName=%@ PairingMode=%d Authenticated=%d IsInBubble=%d ProductType=%@ SerialNumber=%@ OSVersion=%@ BatteryCapacity=%lu BatteryCharging=%d ExternalPowerSourceConnected=%d WiFiNetworkName=%@ WiFiSignalStrength=%ld iCloudAccountName=%@ ActiveEnvironment=%@ MainVolume=%f EnvironmentVolume=%f PhoneCallVolume=%f AudioVideoVolume=%f ContentFrozen=%d AirPlayAssistedReady=%d ThermalMitigationNeeded=%d BuddyInProgress=%d IpAddresses=%@ ProtocolVersion=%lu>"
+ "<%@[%p]: PointerControl=%lu GazeAccessibility=%lu StaticFoveation=%lu HandChirality=%lu DwellControll=%lu VoiceOver=%lu ClosedCaptions=%lu AssistiveTouch=%lu AudioDescriptions=%lu VoiceOverTutorial=%lu LiveTranscription=%lu>"
+ "DisableScreenDarkHours"
+ "Library/Preferences/com.apple.osanalytics.internal.plist"
+ "Media/ManagedPurchases"
+ "TB,N,V_batteryCharging"
+ "TB,N,V_externalPowerSourceConnected"
+ "TQ,N,V_liveTranscription"
+ "_batteryCharging"
+ "_externalPowerSourceConnected"
+ "_liveTranscription"
+ "batteryCharging"
+ "enableMuseBuddyResetOnPeer:value:withCompletion:"
+ "externalPowerSourceConnected"
+ "getIconImagesOfVisibleAppsOnPeer:height:width:scale:withCompletion:"
+ "getIconImagesOfVisibleAppsOnPeerOfID:height:width:scale:withCompletion:"
+ "isScreenDarkHoursEnabled"
+ "isStoreOpen:withError:"
+ "liveTranscription"
+ "nextStoreCloseDate:withError:"
+ "nextStoreOpenDate:withError:"
+ "readPreferencesFileObjectForKey:"
+ "setBatteryCharging:"
+ "setExternalPowerSourceConnected:"
+ "setLanguageAndRegionOnPeer:languageCode:regionCode:withCompletion:"
+ "setLiveTranscription:"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v44@0:8@\"NSString\"16f24f28f32@?<v@?@\"NSDictionary\"@\"NSError\">36"
+ "v44@0:8@16f24f28f32@?36"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
- "-[MSDKManagedDevice isStoreOpen:]"
- "-[MSDKManagedDevice nextStoreCloseDate:]"
- "-[MSDKManagedDevice nextStoreOpenDate:]"
- "<%@[%p]: Identifier=%@ DeviceName=%@ PairingMode=%d Authenticated=%d IsInBubble=%d ProductType=%@ SerialNumber=%@ OSVersion=%@ BatteryCapacity=%lu WiFiNetworkName=%@ WiFiSignalStrength=%ld iCloudAccountName=%@ ActiveEnvironment=%@ MainVolume=%f EnvironmentVolume=%f PhoneCallVolume=%f AudioVideoVolume=%f ContentFrozen=%d AirPlayAssistedReady=%d ThermalMitigationNeeded=%d BuddyInProgress=%d IpAddresses=%@ ProtocolVersion=%lu>"
- "<%@[%p]: PointerControl=%lu GazeAccessibility=%lu StaticFoveation=%lu HandChirality=%lu DwellControll=%lu VoiceOver=%lu ClosedCaptions=%lu AssistiveTouch=%lu AudioDescriptions=%lu VoiceOverTutorial=%lu>"

```
