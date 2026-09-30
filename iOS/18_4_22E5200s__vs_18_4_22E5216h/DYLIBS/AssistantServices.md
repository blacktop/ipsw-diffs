## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3404.68.6.1.1
-  __TEXT.__text: 0x1ab2a0
+3404.77.1.0.0
+  __TEXT.__text: 0x1acad0
   __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_methlist: 0x1db34
+  __TEXT.__objc_methlist: 0x1dbf4
   __TEXT.__const: 0x458
-  __TEXT.__dlopen_cstrs: 0x484
-  __TEXT.__gcc_except_tab: 0x2ae4
-  __TEXT.__cstring: 0x3d014
-  __TEXT.__oslogstring: 0x10c1b
+  __TEXT.__dlopen_cstrs: 0x4e2
+  __TEXT.__gcc_except_tab: 0x2b60
+  __TEXT.__cstring: 0x3d3b2
+  __TEXT.__oslogstring: 0x10f67
   __TEXT.__ustring: 0x2ac
-  __TEXT.__unwind_info: 0x7cf0
+  __TEXT.__unwind_info: 0x7d40
   __TEXT.__objc_classname: 0x4f0c
-  __TEXT.__objc_methname: 0x3af4f
-  __TEXT.__objc_methtype: 0xaa95
-  __TEXT.__objc_stubs: 0x246a0
+  __TEXT.__objc_methname: 0x3b18a
+  __TEXT.__objc_methtype: 0xaaf0
+  __TEXT.__objc_stubs: 0x24820
   __DATA_CONST.__got: 0x1648
-  __DATA_CONST.__const: 0x8450
+  __DATA_CONST.__const: 0x8478
   __DATA_CONST.__objc_classlist: 0xdd8
   __DATA_CONST.__objc_catlist: 0x290
   __DATA_CONST.__objc_protolist: 0x558
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc2b8
+  __DATA_CONST.__objc_selrefs: 0xc330
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xdf0
-  __DATA_CONST.__objc_arraydata: 0x2068
+  __DATA_CONST.__objc_arraydata: 0x2090
   __AUTH_CONST.__auth_got: 0xab8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3a20
-  __AUTH_CONST.__cfstring: 0x27000
-  __AUTH_CONST.__objc_const: 0x33578
+  __AUTH_CONST.__const: 0x3aa0
+  __AUTH_CONST.__cfstring: 0x270a0
+  __AUTH_CONST.__objc_const: 0x33638
   __AUTH_CONST.__objc_intobj: 0x2328
   __AUTH_CONST.__objc_dictobj: 0xb90
-  __AUTH_CONST.__objc_arrayobj: 0x5a0
+  __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x7918
-  __AUTH.__data: 0x2b0
-  __DATA.__objc_ivar: 0x254c
+  __AUTH.__data: 0x2b8
+  __DATA.__objc_ivar: 0x255c
   __DATA.__data: 0x4178
-  __DATA.__bss: 0x1310
+  __DATA.__bss: 0x1360
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1158
   __DATA_DIRTY.__common: 0xf8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11734
-  Symbols:   14018
-  CStrings:  19195
+  Functions: 11764
+  Symbols:   14049
+  CStrings:  19251
 
Symbols:
+ _AFDeviceSupportsVisualIntelligence
+ _AFIsAppleIntelligenceEnabled
+ _AFIsDeviceGreymatterEligible
+ _AFIsPersistentSiriAvailable
+ _AFVisualIntelligenceEnabled
+ _kAFBackedUpVisualIntelligenceCameraControlEnabled
+ _kAFSiriCapabilitiesDidChangeNotification
- _kAFSiriCapabilitiesDidChangNotification
CStrings:
+ "%@ {sharedUserId = %@, loggableSharedUserId = %@, companionDeviceInfo = %@, personalRequestsEnabled = %@, companionLinkReady = %@, homeUserId = %@, iCloudAltDSID = %@, isDeviceOwner = %@}"
+ "%s #AppleIntelligence optIn status: %d"
+ "%s #SAEStatus available from cache:%d"
+ "%s #SAEStatus enabled from cache:%d"
+ "%s #preferences Setting Visual Intelligence Camera Control %@"
+ "%s #visualIntelligenceStatus from cache:%d"
+ "%s #visualIntelligenceStatus:%d"
+ "%s %p Skipping timeouts and interstitials for testing"
+ "%s Error in getLoggableIdentiferForUserWithiCloudAltDSID:%@"
+ "%s Failed to determine GM eligibility with status code: %d"
+ "%s Loading GMS availability via deprecated SPI"
+ "%s Loading GMS availability via locale based SPI"
+ "%s Locale is nil, returning unavailable"
+ "%s SAE available status: %@"
+ "%s SAE enabled status: %@"
+ "%s deviceSupportsVisualIntelligence = %d, isDeviceCapable = %d, isDeviceEligible = %d, deviceSupported = %d, isDeviceRestricted = %d"
+ "%s visualIntelligenceEnabled = %d, deviceSupportsVisualIntelligence = %d, appleIntelligenceAvailable = %d"
+ "%s visualIntelligenceRestricted = %d,"
+ "+[AFSystemAssistantExperienceStatusManager isVisualIntelligenceEnabled]"
+ "+[AFSystemAssistantExperienceStatusManager saeAvailable]"
+ "-[AFMultiUserConnection getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:]"
+ "-[AFMultiUserConnection getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:]_block_invoke_2"
+ "/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures"
+ "@68@0:8@16@24@32B40B44@48@56B64"
+ "AFDeviceSupportsVisualIntelligence"
+ "AFIsAppleIntelligenceEnabled"
+ "AFIsDeviceGreymatterEligible_block_invoke"
+ "AFSharedUserInfo::isDeviceOwner"
+ "AFSystemAssistantExperienceStatusManager.m"
+ "AFVisualIntelligenceCameraRestricted"
+ "AFVisualIntelligenceEnabled"
+ "CSFGMOptIn"
+ "HomePodNoTTSPerfTestEnabled"
+ "TB,R,N,V_isDeviceOwner"
+ "TB,V_saeAvailable"
+ "TB,V_visualIntelligenceEnabled"
+ "Visual Intelligence Camera Control Enabled"
+ "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSString\">40"
+ "_AFPreferencesSetVisualIntelligenceCameraControlEnabled"
+ "_isDeviceOwner"
+ "_saeAvailable"
+ "_visualIntelligenceEnabled"
+ "checkGMAvailabilityWithUseCaseIdentifiers"
+ "currentWithUseCaseIdentifiers:language:"
+ "getIsDeviceOwner"
+ "getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:"
+ "initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:"
+ "isDeviceOwner"
+ "isHomePodNoTTSPerfTestEnabled"
+ "isOptedIn"
+ "isPersistentSiriEnabled"
+ "isVisualIntelligenceEnabled"
+ "persistent_siri"
+ "saeAvailable"
+ "setIsDeviceOwner:"
+ "setSaeAvailable:"
+ "setVisualIntelligenceCameraControlEnabled:"
+ "setVisualIntelligenceEnabled:"
+ "visualIntelligenceCameraControlEnabled"
+ "visualIntelligenceEnabled"
+ "{_mutationFlags=\"isDirty\"b1\"hasSharedUserId\"b1\"hasLoggableSharedUserId\"b1\"hasCompanionDeviceInfo\"b1\"hasPersonalRequestsEnabled\"b1\"hasCompanionLinkReady\"b1\"hasHomeUserId\"b1\"hasICloudAltDSID\"b1\"hasIsDeviceOwner\"b1}"
- "%@ {sharedUserId = %@, loggableSharedUserId = %@, companionDeviceInfo = %@, personalRequestsEnabled = %@, companionLinkReady = %@, homeUserId = %@, iCloudAltDSID = %@}"
- "%s #SAEStatus from cache:%d"
- "%s SAE status: %@"
- "@64@0:8@16@24@32B40B44@48@56"
- "initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:"
- "{_mutationFlags=\"isDirty\"b1\"hasSharedUserId\"b1\"hasLoggableSharedUserId\"b1\"hasCompanionDeviceInfo\"b1\"hasPersonalRequestsEnabled\"b1\"hasCompanionLinkReady\"b1\"hasHomeUserId\"b1\"hasICloudAltDSID\"b1}"

```
