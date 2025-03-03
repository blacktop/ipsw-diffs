## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-277.30.2.0.0
-  __TEXT.__text: 0x5ca70
-  __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_methlist: 0x24fc
+277.40.32.0.0
+  __TEXT.__text: 0x656d0
+  __TEXT.__auth_stubs: 0xfe0
+  __TEXT.__objc_methlist: 0x2d5c
   __TEXT.__const: 0x3a2
-  __TEXT.__cstring: 0x17d44
-  __TEXT.__oslogstring: 0x54d
-  __TEXT.__gcc_except_tab: 0x14c
+  __TEXT.__cstring: 0x18584
+  __TEXT.__oslogstring: 0x57d
+  __TEXT.__gcc_except_tab: 0x154
   __TEXT.__constg_swiftt: 0xe0
   __TEXT.__swift5_typeref: 0xcb
   __TEXT.__swift5_reflstr: 0x8b

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_capture: 0x88
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0xee0
-  __TEXT.__eh_frame: 0x480
-  __TEXT.__objc_classname: 0x2b1
-  __TEXT.__objc_methname: 0xb6ef
-  __TEXT.__objc_methtype: 0x1106
-  __TEXT.__objc_stubs: 0x70c0
-  __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x1460
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x24
+  __TEXT.__unwind_info: 0x1528
+  __TEXT.__eh_frame: 0x490
+  __TEXT.__objc_classname: 0x2b4
+  __TEXT.__objc_methname: 0xba81
+  __TEXT.__objc_methtype: 0x111e
+  __TEXT.__objc_stubs: 0x7300
+  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__const: 0x14c0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2360
+  __DATA_CONST.__objc_selrefs: 0x27e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x230
-  __AUTH_CONST.__auth_got: 0x7e8
+  __AUTH_CONST.__auth_got: 0x800
   __AUTH_CONST.__auth_ptr: 0x98
   __AUTH_CONST.__const: 0x848
-  __AUTH_CONST.__cfstring: 0x4780
-  __AUTH_CONST.__objc_const: 0x7688
+  __AUTH_CONST.__cfstring: 0x4d40
+  __AUTH_CONST.__objc_const: 0x69f0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH.__objc_data: 0x688
   __AUTH.__data: 0x2d8
-  __DATA.__objc_ivar: 0x900
+  __DATA.__objc_ivar: 0x944
   __DATA.__data: 0xac0
   __DATA.__common: 0x40
   __DATA.__bss: 0x690

   - /usr/lib/libutil.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1442
-  Symbols:   1728
-  CStrings:  4909
+  Functions: 2574
+  Symbols:   2962
+  CStrings:  5031
 
Symbols:
+ _CFDictionaryCreateMutable
+ _CFDictionarySetValue
+ _WiFiNetworkCopyPassword
+ _WiFiNetworkCreate
+ __swift_FORCE_LOAD_$_swiftCompression
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _kCFAllocatorDefault
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kDefaultsKey_FailBonjour
+ _objc_retainAutoreleasedReturnValue
- _objc_release_x3
- _swift_arrayDestroy
CStrings:
+ "\x1141\x13!\x11!23!\x12\x11\x13\x11\x1111a\xb51Q3A\xe1!!\xb1\x81a!sAQ\x11\"\x11\x82\x14\x13/\x0f\x05"
+ "%@-%@"
+ "-[HDSDeviceOperationHomeKitSetup performReadinessCheck:completion:]_block_invoke"
+ "-[HDSDeviceOperationHomeKitSetup performReadinessCheck:completion:]_block_invoke_2"
+ "-[HDSDeviceOperationHomeKitSetup performReadinessCheck:completion:]_block_invoke_3"
+ "-[HDSDeviceOperationHomeKitSetup sendPeerAccessoryHintForStereoPair]"
+ "-[HDSSetupSession _homeKitUpdateiCloudSwitchState:]_block_invoke_3"
+ "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]"
+ "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke"
+ "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2"
+ "-[HDSSetupSession _runPreflightSSIDCheck]"
+ "-[HDSSetupSession _runSetSessionID]"
+ "-[HDSSetupSession _runStereoPairUserInput]_block_invoke"
+ "-[HDSSetupSession _runStereoPairUserInput]_block_invoke_2"
+ "-[HDSSetupSession _runTVAudioUserInput]_block_invoke_3"
+ "-[HDSSetupSession _runWiFiSetup]_block_invoke_2"
+ "-[HDSSetupSession _runWiFiSetup]_block_invoke_3"
+ "-[HDSSetupSession createWiFiConfigurationForSetup:password:]"
+ "-[HDSSetupSession passwordForSSID:]"
+ "-[HDSSetupSession preflightCheckPhonesNetwork]"
+ "@\"HMMediaSystemBuilder\""
+ "APC"
+ "Activated"
+ "Adding Ready Accessory %@\n"
+ "CaptiveJoin"
+ "Default Enabled, force failing Bonjour test\n"
+ "DidUsePhones %s\n"
+ "Enable FF for HK Stereo Pair hint\n"
+ "HIDDEN_NETWORK"
+ "HomeKitPRSSIDFetch"
+ "HomeKitPrimarySSIDFetch empty result, falling back to regular wifi setup\n"
+ "HomeKitPrimarySSIDFetch error %@\n"
+ "HomeKitPrimarySSIDFetch fetchWiFiInfosWithTimeout complete, duration %f seconds\n"
+ "HomeKitPrimarySSIDFetch fetched SSID %@ | protected %s\n"
+ "HomeKitPrimarySSIDFetch no selected Home, Skipping\n"
+ "HomeKitPrimarySSIDFetch result %@\n"
+ "HomeKitPrimarySSIDFetch start\n"
+ "No iOS WiFi SSID"
+ "NoWiFIPassword"
+ "NoWiFiPassword"
+ "Odeon"
+ "PersonalContent"
+ "Phone SSID %@ | PR SSID %@\n"
+ "PreMisc"
+ "Preflight SSID Check hasn't succeeded yet (%d)\n"
+ "Preflight SSID Check start\n"
+ "Preflight SSID Check succeeded\n"
+ "Preflight iOS WiFi Info %@\n"
+ "Preflight iOS WiFi start\n"
+ "PreflightCDP"
+ "PreflightJS"
+ "PreflightSSID"
+ "PreflightSSIDCheck"
+ "PreflightiOSWiFi"
+ "Readiness finished, ready accessories %@\n"
+ "Role must be left or right and have a valid stereo counterpart acc: %@ | role: %@ | builder %@\n"
+ "SCAN_DIRECTED"
+ "SFSessionActivate-SysDrop"
+ "SFSessionActivation"
+ "SFSessionError-%@"
+ "SFSessionError-SysDrop"
+ "SFSessionInterruption-SysDrop"
+ "SPC"
+ "SSID"
+ "SSID_STR"
+ "SessionID"
+ "Set Session ID %@\n"
+ "ShareSettings"
+ "SiriEnablement"
+ "StereoPair"
+ "T@?,C,N,V_promptForWiFiSetupComplete"
+ "TRAuthiCloud"
+ "TRAuthiTunes"
+ "TVAudioUserInput kCUMultiStateTVAudioTVReadiness finished\n"
+ "TermsV1"
+ "Unactivated"
+ "User opted out of iTunes Auth, skipping\n"
+ "Using new builder, sending hint...\n"
+ "WEP"
+ "WPA"
+ "WPA2"
+ "WPA3"
+ "WiFi password missing, Failing.\n"
+ "WiFiDisabled"
+ "WiFiSetup resetting retries for CWS"
+ "WiFiSetupNoInternet"
+ "_appleTVReady"
+ "_builder"
+ "_currentStageLabel"
+ "_didSetupWithPRSSID"
+ "_homeKitPrimarySSIDFetchState"
+ "_homeKitSSIDFetchDuration"
+ "_homeKitSSIDFetchStart"
+ "_isVM"
+ "_prSSIDRetried"
+ "_preferredWiFiConfig"
+ "_primaryResidentPassword"
+ "_primaryResidentSSID"
+ "_primaryResidentSSIDProtected"
+ "_promptForWiFiSetupComplete"
+ "_runHomeKitPrimarySSIDFetch"
+ "_runPreflightSSIDCheck"
+ "_runSetSessionID"
+ "_selectedHomeHasPrimaryResident"
+ "_sessionIDState"
+ "_stereoPairReady"
+ "_wifiSetupType"
+ "addPeerAccessoryBeforeSetupSession:role:"
+ "b\x11\x12\x11\x121\x11)\xab!"
+ "createStereoPairBuilder:"
+ "createWiFiConfigurationForSetup finish\n"
+ "createWiFiConfigurationForSetup:password:"
+ "failBonjour"
+ "fetchPhonesSSID"
+ "fetchWiFiInfosWithTimeout:completion:"
+ "forceFailBonjour"
+ "hk_browser"
+ "initWithHome:setupSessionIdentifier:"
+ "initWithUUIDString:"
+ "open"
+ "passwordForSSID WiFi Info %@\n"
+ "passwordForSSID:"
+ "performReadinessCheck\n"
+ "performReadinessCheck:completion:"
+ "preflightCheckPhonesNetwork"
+ "primarySSIDFetchMs"
+ "primary_resident_wifi"
+ "promptForWiFiSetupComplete"
+ "requiresPassword"
+ "residentWiFiSetup"
+ "sendPeerAccessoryHintForStereoPair"
+ "setPreferredWiFiConfiguration:"
+ "setPromptForWiFiSetupComplete:"
+ "stereo_pair_hint"
+ "sysdrop_carry"
+ "wifiSetupType"
+ "wifiTypeForString:"
- "\x1141\x13!\x11!232\x11\x13\x11\x1111a\xb51Q3A\xe1!!\xb1\x81a!sAQ\x11b\x14\x13/\x0f\x04"
- "-[HDSDeviceOperationHomeKitSetup performReadinessCheck:]"
- "-[HDSDeviceOperationHomeKitSetup performReadinessCheck:]_block_invoke"
- "-[HDSSetupSession init]"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_skipWiFiSetup"
- "b\x11\x12\x11\x111\x11)\xab!"
- "invalid Collection: less than 'count' elements in collection"
- "performReadinessCheck:"
- "sessionID = %@\n"
- "sysdrop_external"

```
