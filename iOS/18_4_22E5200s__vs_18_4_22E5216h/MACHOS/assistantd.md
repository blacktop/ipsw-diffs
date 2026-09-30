## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3404.68.6.1.1
-  __TEXT.__text: 0x36b5c8
+3404.77.1.0.0
+  __TEXT.__text: 0x36c174
   __TEXT.__auth_stubs: 0x34b0
-  __TEXT.__objc_stubs: 0x45220
-  __TEXT.__objc_methlist: 0x22418
+  __TEXT.__objc_stubs: 0x45240
+  __TEXT.__objc_methlist: 0x22468
   __TEXT.__const: 0x109a0
   __TEXT.__dlopen_cstrs: 0xafa
-  __TEXT.__gcc_except_tab: 0x482c
-  __TEXT.__cstring: 0x51403
-  __TEXT.__oslogstring: 0x3f434
-  __TEXT.__objc_classname: 0x518b
-  __TEXT.__objc_methname: 0x5cff7
-  __TEXT.__objc_methtype: 0xf19e
+  __TEXT.__gcc_except_tab: 0x487c
+  __TEXT.__cstring: 0x51683
+  __TEXT.__oslogstring: 0x3f60e
+  __TEXT.__objc_classname: 0x518d
+  __TEXT.__objc_methname: 0x5d0d8
+  __TEXT.__objc_methtype: 0xf1e2
   __TEXT.__ustring: 0x2b0
-  __TEXT.__unwind_info: 0xa380
+  __TEXT.__unwind_info: 0xa388
   __TEXT.__eh_frame: 0xe68
   __DATA_CONST.__auth_got: 0x1a68
-  __DATA_CONST.__got: 0x3b20
+  __DATA_CONST.__got: 0x3b28
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x14c68
-  __DATA_CONST.__cfstring: 0x127e0
+  __DATA_CONST.__const: 0x14c88
+  __DATA_CONST.__cfstring: 0x128e0
   __DATA_CONST.__objc_classlist: 0xd10
   __DATA_CONST.__objc_catlist: 0x630
   __DATA_CONST.__objc_protolist: 0x6e8

   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x33560
-  __DATA.__objc_selrefs: 0x147d8
-  __DATA.__objc_ivar: 0x2580
+  __DATA.__objc_const: 0x335b8
+  __DATA.__objc_selrefs: 0x147f8
+  __DATA.__objc_ivar: 0x2588
   __DATA.__objc_data: 0x82a0
   __DATA.__data: 0x60f0
-  __DATA.__bss: 0xe00
+  __DATA.__bss: 0xe10
   __DATA.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14298
-  Symbols:   2888
-  CStrings:  27085
+  Functions: 14302
+  Symbols:   2889
+  CStrings:  27117
 
Symbols:
+ _SADeviceRestrictionEYES_FREEValue
+ _kAFSiriCapabilitiesDidChangeNotification
- _kAFSiriCapabilitiesDidChangNotification
CStrings:
+ "#EyesFree Remove EyesFree Restriction"
+ "#eyesFree Add EyesFree Restriction"
+ "%s Asset manager is deallocated."
+ "%s Failed to generate loggable identifier due to error: %@"
+ "%s Loading GMS availability via deprecated SPI"
+ "%s Loading GMS availability via locale based SPI"
+ "%s No user found with iCloudAltDSID: %{private}@ sharedUserID:%{private}@"
+ "%s Received GMS availability notifification %@"
+ "%s Should download assets is %@, capabilities: %@"
+ "%s Skipping tvOS dependency check for sync enablement on VisionOS, macOS and watchOS devices"
+ "%s Updated GMS capabilities to %@"
+ "%s Updated systemAssistantExperienceCapabilites capabilities to %@"
+ "%s deviceIsLocked=%d AFHasUnlockedSinceBoot=%d ADVoiceDialingDisabledWhileLocked=%d deviceIsShowingLockScreen=%d ADControlCenterDisabledWhileLocked=%d _isInStarkMode=%d _isInCarDNDMode=%d _isWatchAuthenticated=%d _isheadphonesAuthenticated=%d _isHeadGestureRecognitionAvailable=%d _isEyesFree=%d"
+ "%s optedOut: %d, fullUodCapable: %d, deviceHasAtvOrHomepodInHome: %d, deviceHasPairedWatch: %d, syncDisabledViaTrial: %d"
+ "*o+2$Tf?6M_mo"
+ "-[ADCommandCenter _setIsEyesFree:]"
+ "-[ADMultiUserService getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:]_block_invoke"
+ "-[ADSiriCapabilitiesService shouldDownloadAssetsForSiriSystemAssistantExperience:]"
+ "-[ADSiriCapabilitiesService siriSystemAssistantExperienceEnabled:]"
+ "-[ADSiriCapabilitiesStore updateSystemAssistantExperienceCapabilites:localeIdentifier:]"
+ "95"
+ "HandleGMSAvailabilityNotification"
+ "MobileAssistantDaemons-3404.77.1"
+ "SiriSystemAssistantExperienceCapabilitiesForGMSAvailability"
+ "T@\"ADAssetManager\",R,W,N,V_assetManager"
+ "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSString\">40"
+ "_isEyesFree"
+ "_setIsEyesFree:"
+ "appletv"
+ "assetManager"
+ "audioaccessory"
+ "com.apple.assistant"
+ "currentWithUseCaseIdentifiers:language:"
+ "disableForceLocationUpdates"
+ "getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:"
+ "initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:"
+ "mac"
+ "setMeDeviceUseFindMyLocate:"
- "%s Skipping tvOS dependency check for sync enablement on VisionOS and macOS devices"
- "%s deviceIsLocked=%d AFHasUnlockedSinceBoot=%d ADVoiceDialingDisabledWhileLocked=%d deviceIsShowingLockScreen=%d ADControlCenterDisabledWhileLocked=%d _isInStarkMode=%d _isInCarDNDMode=%d _isWatchAuthenticated=%d _isheadphonesAuthenticated=%d _isHeadGestureRecognitionAvailable=%d"
- "%s optedOut: %d, fullUodCapable: %d, deviceHasAtvOrHomepodInHome: %d, deviceHasPairedWatch: %d, assistantSyncDisabledViaConfig: %d"
- "11"
- "MobileAssistantDaemons-3404.68.6.1.1"
- "initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:"
- "isOkayToHaveAsset"

```
