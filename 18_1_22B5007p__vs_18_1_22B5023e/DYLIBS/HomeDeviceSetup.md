## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-257.0.13.0.0
-  __TEXT.__text: 0x55374
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x2374
+257.10.3.0.0
+  __TEXT.__text: 0x55fe8
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x23b4
   __TEXT.__const: 0x270
-  __TEXT.__cstring: 0x16995
-  __TEXT.__oslogstring: 0x3a7
+  __TEXT.__cstring: 0x16de6
+  __TEXT.__oslogstring: 0x3ba
   __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0xce0
-  __TEXT.__objc_classname: 0x2c3
-  __TEXT.__objc_methname: 0xb2e4
+  __TEXT.__unwind_info: 0xcf8
+  __TEXT.__objc_classname: 0x2c4
+  __TEXT.__objc_methname: 0xb4b5
   __TEXT.__objc_methtype: 0x11ff
-  __TEXT.__objc_stubs: 0x6c40
-  __DATA_CONST.__got: 0x348
-  __DATA_CONST.__const: 0x12f8
+  __TEXT.__objc_stubs: 0x6da0
+  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__const: 0x1300
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2218
+  __DATA_CONST.__objc_selrefs: 0x2268
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0x210
-  __AUTH_CONST.__auth_got: 0x548
+  __DATA_CONST.__objc_arraydata: 0x220
+  __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__const: 0x6a0
-  __AUTH_CONST.__cfstring: 0x4560
-  __AUTH_CONST.__objc_const: 0x7690
+  __AUTH_CONST.__cfstring: 0x4640
+  __AUTH_CONST.__objc_const: 0x77b0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0x398
+  __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH.__objc_data: 0x4b0
   __AUTH.__data: 0x290
-  __DATA.__objc_ivar: 0x8dc
+  __DATA.__objc_ivar: 0x900
   __DATA.__data: 0xa28
   __DATA.__common: 0x10
   __DATA.__bss: 0x528

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1306
-  Symbols:   1605
-  CStrings:  4760
+  Functions: 1313
+  Symbols:   1621
+  CStrings:  4807
 
Symbols:
+ _CFDictionaryCreateMutable
+ _CFDictionarySetValue
+ _CFStringCreateWithCString
+ _WiFiNetworkCopyPassword
+ _WiFiNetworkCreate
+ _kCFAllocatorDefault
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kDefaultsKey_SSIDFetchTimeout
CStrings:
+ "\x114C!\x11!232\x11\x13\x11\x1111a\xb51Q3A\xe1!!\xb1\x81a!sAQ\x13\x11r\x14\x13/\x0f\x03"
+ "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]"
+ "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke"
+ "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2"
+ "-[HDSSetupSession _runPreflightSSIDCheck]"
+ "-[HDSSetupSession createWiFiConfigurationForSetup:password:]"
+ "-[HDSSetupSession passwordForSSID:]"
+ "HIDDEN_NETWORK"
+ "HKStereoPair-AccountMismatch, Skipping stereo counterpart for account mismatch: '%!{(MISSING)mask}' vs '%!{(MISSING)mask}'\n"
+ "HKStereoPair-AlreadyStereoPaired, skipping\n"
+ "HKStereoPair-NoAccount, Existing potential HomePod does not have a loggedInAccount\n"
+ "HKStereoPair-NoLogin, Existing potential HomePod does not have a remoteLoginHandler\n"
+ "HKStereoPair-NoMediaSystemSupport, Skipping stereo counterpart that doesn't support MediaSystem\n"
+ "HKStereoPair-NoUsername, Existing potential HomePod does not have an iTunes username\n"
+ "HKStereoPair-VersionMismatch, Skipping stereo counterpart for supportedStereoPairVersions mismatch: '%!l(MISSING)d' vs '%!l(MISSING)d'\n"
+ "HomeKitPRSSIDFetch"
+ "HomeKitPrimarySSIDFetch empty result, falling back to regular wifi setup\n"
+ "HomeKitPrimarySSIDFetch error %!@(MISSING)\n"
+ "HomeKitPrimarySSIDFetch fetchWiFiInfosWithTimeout complete, duration %!f(MISSING) seconds\n"
+ "HomeKitPrimarySSIDFetch fetched SSID %!@(MISSING)\n"
+ "HomeKitPrimarySSIDFetch no selected Home, Skipping\n"
+ "HomeKitPrimarySSIDFetch result %!@(MISSING)\n"
+ "HomeKitPrimarySSIDFetch start\n"
+ "Preflight SSID Check hasn't succeeded yet (%!d(MISSING))\n"
+ "Preflight SSID Check start\n"
+ "Preflight SSID Check succeeded\n"
+ "PreflightSSID"
+ "SCAN_DIRECTED"
+ "SSID"
+ "SSID_STR"
+ "_didSetupWithPRSSID"
+ "_homeKitPrimarySSIDFetchState"
+ "_homeKitSSIDFetchDuration"
+ "_homeKitSSIDFetchStart"
+ "_preferredWiFiConfig"
+ "_preflightSSIDCheckState"
+ "_primaryResidentPassword"
+ "_primaryResidentSSID"
+ "_runHomeKitPrimarySSIDFetch"
+ "_runPreflightSSIDCheck"
+ "_selectedHomeHasPrimaryResident"
+ "_selectedHomeHasPrimaryResident = %!@(MISSING)\n"
+ "cStringUsingEncoding:"
+ "createWiFiConfigurationForSetup finish\n"
+ "createWiFiConfigurationForSetup:password:"
+ "fetchWiFiInfosWithTimeout:completion:"
+ "passwordForSSID WiFi Info %!@(MISSING)\n"
+ "passwordForSSID:"
+ "primarySSIDFetchMs"
+ "primary_resident_wifi"
+ "residentDevices"
+ "residentWiFiSetup"
+ "setPreferredWiFiConfiguration:"
+ "ssidfetchTimeout"
+ "timeoutForSSIDFetch"
- "\x1143!\x11!232\x11\x13\x11\x1111a\xb51Q3A\xe1!!\xb1\x81a!sAQ\x11R\x14\x13/\x0f\x03"
- "Existing potential HomePod does not have a loggedInAccount\n"
- "Existing potential HomePod does not have a remoteLoginHandler\n"
- "Existing potential HomePod does not have an iTunes username\n"
- "Skipping stereo counterpart for account mismatch: '%!{(MISSING)mask}' vs '%!{(MISSING)mask}'\n"
- "Skipping stereo counterpart for supportedStereoPairVersions mismatch: '%!l(MISSING)d' vs '%!l(MISSING)d'\n"
- "Skipping stereo counterpart that doesn't support MediaSystem\n"
- "_runRecognizeVoiceCheckVoiceProfileResponse kAFErrorCloudKitSyncDisabled hit, setting rmv to succeeded \n"

```
