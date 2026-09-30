## HearingModeSettingsUI

> `/System/Library/PrivateFrameworks/HearingModeSettingsUI.framework/HearingModeSettingsUI`

```diff

-30.54.2.1.1
-  __TEXT.__text: 0x4468c
-  __TEXT.__auth_stubs: 0x19b0
-  __TEXT.__objc_methlist: 0x1960
-  __TEXT.__const: 0x17c4
-  __TEXT.__cstring: 0x63e1
+30.58.1.0.0
+  __TEXT.__text: 0x45400
+  __TEXT.__auth_stubs: 0x19a0
+  __TEXT.__objc_methlist: 0x1958
+  __TEXT.__const: 0x17b4
+  __TEXT.__cstring: 0x6681
   __TEXT.__gcc_except_tab: 0xbc
   __TEXT.__ustring: 0xce
-  __TEXT.__oslogstring: 0xd4a
+  __TEXT.__oslogstring: 0xdfa
   __TEXT.__constg_swiftt: 0xd24
-  __TEXT.__swift5_typeref: 0x105a
+  __TEXT.__swift5_typeref: 0x1014
   __TEXT.__swift5_reflstr: 0x84c
   __TEXT.__swift5_fieldmd: 0x63c
   __TEXT.__swift5_types: 0xa4

   __TEXT.__swift_as_ret: 0x4
   __TEXT.__unwind_info: 0x1098
   __TEXT.__eh_frame: 0x228
-  __TEXT.__objc_classname: 0x32d
-  __TEXT.__objc_methname: 0x443c
+  __TEXT.__objc_classname: 0x312
+  __TEXT.__objc_methname: 0x4406
   __TEXT.__objc_methtype: 0xd20
-  __TEXT.__objc_stubs: 0x2320
-  __DATA_CONST.__got: 0x5d0
-  __DATA_CONST.__const: 0x318
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__objc_stubs: 0x2300
+  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__const: 0x320
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1450
+  __DATA_CONST.__objc_selrefs: 0x1448
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0xce8
-  __AUTH_CONST.__const: 0xe20
+  __AUTH_CONST.__auth_got: 0xce0
+  __AUTH_CONST.__const: 0xe78
   __AUTH_CONST.__cfstring: 0x19e0
-  __AUTH_CONST.__objc_const: 0x4620
+  __AUTH_CONST.__objc_const: 0x4590
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH.__objc_data: 0x1908
+  __AUTH.__objc_data: 0x18b8
   __AUTH.__data: 0x490
   __DATA.__objc_ivar: 0xa4
-  __DATA.__data: 0xd10
+  __DATA.__data: 0xd00
   __DATA.__bss: 0x1fd8
   __DATA.__common: 0x1c8
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 637A4A80-9F7A-360E-AC95-DBC8511942B6
-  Functions: 1495
-  Symbols:   1707
-  CStrings:  1740
+  UUID: 8C652E1D-A7EB-34B7-B0B4-DEB3F14935C5
+  Functions: 1502
+  Symbols:   1699
+  CStrings:  1753
 
Symbols:
+ ___frequencyToHearingDecibelLevelMapFromAudiogram_block_invoke.633
+ ___swift_memcpy0_1
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_HearingModeSettingsUI
+ _block_copy_helper.33
+ _block_descriptor.35
+ _block_destroy_helper.34
+ _objc_msgSend$shouldShowHearingProtection
- +[HMHearingProtectionService shouldShowHearingProtectionForDevice:]
- _OBJC_CLASS_$_HMHearingProtectionService
- _OBJC_METACLASS_$_HMHearingProtectionService
- __OBJC_$_CLASS_METHODS_HMHearingProtectionService
- __OBJC_CLASS_RO_$_HMHearingProtectionService
- __OBJC_METACLASS_RO_$_HMHearingProtectionService
- ___frequencyToHearingDecibelLevelMapFromAudiogram_block_invoke.630
- _block_copy_helper.29
- _block_descriptor.31
- _block_destroy_helper.30
- _objc_msgSend$activeHearingProtectionAvailableForAddress:
- _objc_msgSend$shouldShowHearingProtectionForDevice:
- _swift_unknownObjectRelease_n
- _symbolic SS_So8NSObjectCSgt
- _symbolic _____ySSSo8NSObjectCSgG s18_DictionaryStorageC
- _symbolic _____ySS_So8NSObjectCSgtG s23_ContiguousArrayStorageC
CStrings:
+ " and proper storage in their case are necessary for hearing protection to work as expected. You will not receive the hearing protection benefits if the battery is not charged. After one year of use, check the ear tips for any damage and replace if needed."
+ "$__lazy_storage_$_passiveAttenuationV2"
+ "%s: for %s, HP status: %hhu, HP capability: %hhd"
+ "%s: for %s, shouldShow: %{bool}d"
+ "11 dB"
+ "15 dB"
+ "18 dB"
+ "23 dB"
+ "@\"<_TtP21HearingModeSettingsUI25HearingFlowControllerType_>\""
+ "Device Information"
+ "Hearing Aid: Return Empty Specifiers, No Hearing Health Fature to show for device %@"
+ "HearingModeUIService decoratedSpecifiers for %s: HP: %hhu HA:%hhu  HT:%hhu VS:%s BTSC:%s"
+ "HearingModeUIService listener triggered for %s: HP: %hhu  HA:%hhu  HT:%hhu BTSC:%s"
+ "High Frequency (H)"
+ "Low Frequency (L)"
+ "Medium Frequency (M)"
+ "Passive Attenuation"
+ "Proper Maintenance & Care"
+ "Single Number Rating (SNR)"
+ "The passive attenuation values above only apply in Off listening mode or when there is no battery charge. Hearing Protection is off in each of these two cases, or when Loud Sound Reduction is Off (Transparency & Adaptive modes)."
+ "Total Attenuation"
+ "featureCapable: for %@ showHearingAid %s, showHearingProtection %s, showHearingTest %s"
+ "passiveAttenuationV2"
+ "shouldShowHearingProtection"
+ "shouldShowHearingProtection()"
+ "specifiers: for %@ showHearingAid %s, showHearingProtection %s, showHearingTest %s"
+ "updatedSpecifiersMap adding identifier: %s"
- " and proper storage in their case are necessary for hearing protection to work as expected. You will not receive the hearing protection benefits if the battery is not charged."
- "$__lazy_storage_$_properFitPlaceCard"
- "DEVICE INFORMATION"
- "HMHearingProtectionService"
- "Hearing Aid: Return Empty Specifiers, No Hearing Health Fature to show"
- "Hearing Protection: Feature NOT Enabled"
- "Hearing Protection: Should Show Feature: %s for Device: %@, Device Support: Device: %s, Location Support: %s"
- "HearingModeUIService decoratedSpecifiers: HP: %hhu  HA:%hhu  HT:%hhu VS:%s BTSC:%s"
- "HearingModeUIService listener triggered: HP: %hhu  HA:%hhu  HT:%hhu BTSC:%s"
- "HearingProtection"
- "PASSIVE ATTENUATION"
- "PROPER MAINTENANCE & CARE"
- "TOTAL ATTENUATION"
- "activeHearingProtectionAvailableForAddress:"
- "shouldShowHearingProtectionForDevice:"

```
