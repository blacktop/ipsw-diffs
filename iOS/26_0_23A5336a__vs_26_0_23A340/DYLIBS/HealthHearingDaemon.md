## HealthHearingDaemon

> `/System/Library/PrivateFrameworks/HealthHearingDaemon.framework/HealthHearingDaemon`

```diff

 6106.1.2.11.0
-  __TEXT.__text: 0x216c0
+  __TEXT.__text: 0x21b08
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_methlist: 0x1ac4
+  __TEXT.__objc_methlist: 0x1af4
   __TEXT.__const: 0x3f2
-  __TEXT.__cstring: 0x22d2
+  __TEXT.__cstring: 0x2302
   __TEXT.__oslogstring: 0x2a2b
   __TEXT.__gcc_except_tab: 0x284
   __TEXT.__constg_swiftt: 0xd8

   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x788
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x6bb
-  __TEXT.__objc_methname: 0x7029
+  __TEXT.__objc_classname: 0x6d0
+  __TEXT.__objc_methname: 0x7116
   __TEXT.__objc_methtype: 0x11a4
-  __TEXT.__objc_stubs: 0x4a40
-  __DATA_CONST.__got: 0x4e0
+  __TEXT.__objc_stubs: 0x4aa0
+  __DATA_CONST.__got: 0x4e8
   __DATA_CONST.__const: 0x650
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17a0
+  __DATA_CONST.__objc_selrefs: 0x17b8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x668
+  __DATA_CONST.__objc_arraydata: 0x690
   __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0x310
-  __AUTH_CONST.__cfstring: 0x1d00
-  __AUTH_CONST.__objc_const: 0x3018
-  __AUTH_CONST.__objc_intobj: 0xd50
-  __AUTH_CONST.__objc_arrayobj: 0x138
+  __AUTH_CONST.__cfstring: 0x1d20
+  __AUTH_CONST.__objc_const: 0x3058
+  __AUTH_CONST.__objc_intobj: 0xdc8
+  __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x1a8
+  __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x910
   __DATA.__bss: 0x300
   __DATA_DIRTY.__objc_data: 0x918

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F1834B12-584E-3005-A4B0-60C87AEDE23C
-  Functions: 682
-  Symbols:   2681
-  CStrings:  1837
+  UUID: 0277E03B-BF1D-3164-87EA-56B8980B7C80
+  Functions: 686
+  Symbols:   2695
+  CStrings:  1845
 
Symbols:
+ +[HDFeatureAvailabilityManager(Hearing) hearingProtectionPPEFeatureAvailabilityManagerWithProfile:]
+ +[HKCountrySet(HearingProtectionPPE) localAvailabilityForHearingProtectionPPE]
+ +[HKCountrySet(HearingProtectionPPE) localAvailabilityForHearingProtectionPPE].cold.1
+ +[HKFeatureAvailabilityRequirementSet(Hearing) hearingProtectionPPERequirementSet]
+ _HKFeatureIdentifierHearingProtectionPPE
+ _OBJC_IVAR_$_HDHearingProfileExtension._hearingProtectionPPEBackgroundFeatureDeliveryManager
+ _OBJC_IVAR_$_HDHearingProfileExtension._hearingProtectionPPEFeatureAvailabilityManager
+ __OBJC_$_CLASS_METHODS_HKCountrySet(HearingAidV2|HearingProtectionPPE|HearingProtection|HearingTest|HearingAid)
+ _objc_msgSend$hearingProtectionPPEFeatureAvailabilityManagerWithProfile:
+ _objc_msgSend$hearingProtectionPPERequirementSet
+ _objc_msgSend$localAvailabilityForHearingProtectionPPE
- __OBJC_$_CLASS_METHODS_HKCountrySet(HearingAidV2|HearingProtection|HearingTest|HearingAid)
Functions:
+ +[HKCountrySet(HearingProtectionPPE) localAvailabilityForHearingProtectionPPE]
~ +[HKFeatureAvailabilityRequirements(Hearing) hearingFeatureHardwareRequirementsForFeatureIdentifier:] : 376 -> 432
+ +[HKFeatureAvailabilityRequirementSet(Hearing) hearingProtectionPPERequirementSet]
+ +[HDFeatureAvailabilityManager(Hearing) hearingTestFeatureAvailabilityManagerWithProfile:]
~ -[HDHearingProfileExtension initWithProfile:] : 720 -> 788
~ -[HDHearingProfileExtension featureAvailabilityExtensionForFeatureIdentifier:] : 204 -> 236
~ -[HDHearingProfileExtension .cxx_destruct] : 176 -> 200
+ +[HKCountrySet(HearingProtectionPPE) localAvailabilityForHearingProtectionPPE].cold.1
CStrings:
+ "\r"
+ "HKCountrySet+HearingProtectionPPE.m"
+ "HearingProtectionPPE"
+ "_hearingProtectionPPEBackgroundFeatureDeliveryManager"
+ "_hearingProtectionPPEFeatureAvailabilityManager"
+ "hearingProtectionPPEFeatureAvailabilityManagerWithProfile:"
+ "hearingProtectionPPERequirementSet"
+ "localAvailabilityForHearingProtectionPPE"
- "\v"

```
