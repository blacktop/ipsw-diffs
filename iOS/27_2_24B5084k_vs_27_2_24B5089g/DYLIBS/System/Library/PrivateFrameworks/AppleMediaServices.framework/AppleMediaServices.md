## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-10.1.11.2.1
-  __TEXT.__text: 0x86c764
+10.1.13.2.1
+  __TEXT.__text: 0x8706c4
   __TEXT.__lazy_helpers: 0x42f4
-  __TEXT.__objc_methlist: 0x25484
-  __TEXT.__const: 0x63fd0
+  __TEXT.__objc_methlist: 0x25544
+  __TEXT.__const: 0x64140
   __TEXT.__dlopen_cstrs: 0x990
-  __TEXT.__cstring: 0x30bd2
-  __TEXT.__swift5_typeref: 0x907f
-  __TEXT.__swift5_reflstr: 0x671e
+  __TEXT.__cstring: 0x30e0c
+  __TEXT.__swift5_typeref: 0x90bf
+  __TEXT.__swift5_reflstr: 0x681e
   __TEXT.__swift5_assocty: 0x13b0
-  __TEXT.__constg_swiftt: 0x7b08
+  __TEXT.__constg_swiftt: 0x7b68
   __TEXT.__swift5_builtin: 0x53c
-  __TEXT.__swift5_fieldmd: 0x7c44
-  __TEXT.__swift5_proto: 0x17b4
-  __TEXT.__swift5_types: 0x8f4
-  __TEXT.__swift_as_entry: 0xafc
-  __TEXT.__swift_as_ret: 0xda8
-  __TEXT.__swift_as_cont: 0x1a9c
-  __TEXT.__swift5_capture: 0x779c
+  __TEXT.__swift5_fieldmd: 0x7d60
+  __TEXT.__swift5_proto: 0x17d0
+  __TEXT.__swift5_types: 0x8fc
+  __TEXT.__swift_as_entry: 0xb00
+  __TEXT.__swift_as_ret: 0xdb4
+  __TEXT.__swift_as_cont: 0x1aa8
+  __TEXT.__swift5_capture: 0x7810
   __TEXT.__swift5_mpenum: 0xd4
   __TEXT.__swift5_protos: 0x15c
-  __TEXT.__oslogstring: 0x38416
-  __TEXT.__gcc_except_tab: 0x54ec
+  __TEXT.__oslogstring: 0x385a8
+  __TEXT.__gcc_except_tab: 0x547c
   __TEXT.__ustring: 0x204
-  __TEXT.__unwind_info: 0x1a9e8
-  __TEXT.__eh_frame: 0x2005c
+  __TEXT.__unwind_info: 0x1a640
+  __TEXT.__eh_frame: 0x201b4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd838
+  __DATA_CONST.__const: 0xd868
   __DATA_CONST.__objc_classlist: 0x16c0
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x4e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10648
+  __DATA_CONST.__objc_selrefs: 0x106d0
   __DATA_CONST.__objc_protorefs: 0x278
   __DATA_CONST.__objc_superrefs: 0xd28
   __DATA_CONST.__objc_arraydata: 0x5f8
-  __DATA_CONST.__got: 0x1b38
-  __AUTH_CONST.__const: 0x3c560
-  __AUTH_CONST.__cfstring: 0x24300
-  __AUTH_CONST.__objc_const: 0x41f28
+  __DATA_CONST.__got: 0x1b40
+  __AUTH_CONST.__const: 0x3c780
+  __AUTH_CONST.__cfstring: 0x24340
+  __AUTH_CONST.__objc_const: 0x42050
   __AUTH_CONST.__lazy_load_got: 0x638
   __AUTH_CONST.__objc_intobj: 0xd20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0x27a8
-  __AUTH.__objc_data: 0xb9e8
-  __AUTH.__data: 0x3858
-  __DATA.__objc_ivar: 0x1a5c
-  __DATA.__data: 0x91bc
-  __DATA.__common: 0xb74
+  __AUTH_CONST.__auth_got: 0x27c0
+  __AUTH.__objc_data: 0xb290
+  __AUTH.__data: 0x3530
+  __DATA.__objc_ivar: 0x1a78
+  __DATA.__data: 0x91b0
+  __DATA.__common: 0xb6c
   __DATA_DIRTY.__objc_ivar: 0x72c
-  __DATA_DIRTY.__objc_data: 0x5660
-  __DATA_DIRTY.__data: 0x2c30
+  __DATA_DIRTY.__objc_data: 0x5db8
+  __DATA_DIRTY.__data: 0x2fc8
   __DATA_DIRTY.__bss: 0x62e0
-  __DATA_DIRTY.__common: 0xa0
+  __DATA_DIRTY.__common: 0xa8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 35700
-  Symbols:   33929
-  CStrings:  9825
+  Functions: 35824
+  Symbols:   33975
+  CStrings:  9845
 
Symbols:
+ +[AMSDefaults cardEnrollmentWarmWindowCount]
+ +[AMSDefaults cardEnrollmentWarmWindowStart]
+ +[AMSDefaults setCardEnrollmentWarmWindowCount:]
+ +[AMSDefaults setCardEnrollmentWarmWindowStart:]
+ +[AMSProcessInfo _bundleInfoStringForKey:bundleIdentifier:record:]
+ -[AMSProcessInfo _bundleFactsLocked]
+ -[AMSProcessInfo _resolveBundleURLLocked]
+ -[AMSProcessInfo _resolveBundleVersionLocked]
+ -[AMSProcessInfo _resolveClientVersionLocked]
+ -[AMSProcessInfo _resolveCodablePropertiesLocked]
+ -[AMSProcessInfo _resolveDescriptionPropertiesLocked]
+ -[AMSProcessInfo _resolveEqualityPropertiesLocked]
+ -[AMSProcessInfo _resolveExecutableNameLocked]
+ -[AMSProcessInfo _resolveLocalizedNameLocked]
+ -[AMSProcessInfoBundleFacts _resolvedStringValue:generator:]
+ -[AMSProcessInfoBundleFacts _resolvedURLValue:generator:]
+ -[AMSProcessInfoBundleFacts initWithBundleURLGenerator:executableNameGenerator:localizedNameGenerator:bundleVersionGenerator:clientVersionGenerator:]
+ _AKCredentialCollectionIsLoud
+ _OBJC_IVAR_$_AMSProcessInfo._bundleFacts
+ _OBJC_IVAR_$_AMSProcessInfo._resolvesFromBundleFacts
+ _OBJC_IVAR_$_AMSProcessInfoBundleFacts._bundleURLGenerator
+ _OBJC_IVAR_$_AMSProcessInfoBundleFacts._bundleVersionGenerator
+ _OBJC_IVAR_$_AMSProcessInfoBundleFacts._clientVersionGenerator
+ _OBJC_IVAR_$_AMSProcessInfoBundleFacts._executableNameGenerator
+ _OBJC_IVAR_$_AMSProcessInfoBundleFacts._localizedNameGenerator
+ _OBJC_IVAR_$_AMSProcessInfoBundleFacts._lock
+ ___58+[AMSProcessInfo _launchServicesBundleFactsForIdentifier:]_block_invoke_3
+ ___58+[AMSProcessInfo _launchServicesBundleFactsForIdentifier:]_block_invoke_4
+ ___58+[AMSProcessInfo _launchServicesBundleFactsForIdentifier:]_block_invoke_5
+ ___block_descriptor_40_e8_32s_e12_"NSURL"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e15_"NSString"8?0ls32l8
+ ___block_descriptor_64_e8_32s40s48s_e53_v24?0"AMSMetricsFigaroBagConfguration"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls32l8u56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___swift_memcpy343_8
+ ___swift_memcpy695_8
+ _associated conformance 18AppleMediaServices19SelfieConfigurationV17FaceIDCalibrationV10CodingKeys33_5876F864F6DA530D109B30F5992255AFLLOSHAASQ
+ _associated conformance 18AppleMediaServices19SelfieConfigurationV17FaceIDCalibrationV10CodingKeys33_5876F864F6DA530D109B30F5992255AFLLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 18AppleMediaServices19SelfieConfigurationV17FaceIDCalibrationV10CodingKeys33_5876F864F6DA530D109B30F5992255AFLLOs0H3KeyAAs28CustomDebugStringConvertible
+ _objc_msgSend$_bundleFactsLocked
+ _objc_msgSend$_bundleInfoStringForKey:bundleIdentifier:record:
+ _objc_msgSend$_resolveBundleURLLocked
+ _objc_msgSend$_resolveBundleVersionLocked
+ _objc_msgSend$_resolveClientVersionLocked
+ _objc_msgSend$_resolveCodablePropertiesLocked
+ _objc_msgSend$_resolveDescriptionPropertiesLocked
+ _objc_msgSend$_resolveEqualityPropertiesLocked
+ _objc_msgSend$_resolveExecutableNameLocked
+ _objc_msgSend$_resolveLocalizedNameLocked
+ _objc_msgSend$_resolvedStringValue:generator:
+ _objc_msgSend$_resolvedURLValue:generator:
+ _objc_msgSend$initWithBundleURLGenerator:executableNameGenerator:localizedNameGenerator:bundleVersionGenerator:clientVersionGenerator:
+ _symbolic _____ 18AppleMediaServices19SelfieConfigurationV17FaceIDCalibrationV
+ _symbolic _____ 18AppleMediaServices19SelfieConfigurationV17FaceIDCalibrationV10CodingKeys33_5876F864F6DA530D109B30F5992255AFLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 18AppleMediaServices19SelfieConfigurationV17FaceIDCalibrationV10CodingKeys33_5876F864F6DA530D109B30F5992255AFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 18AppleMediaServices19SelfieConfigurationV17FaceIDCalibrationV10CodingKeys33_5876F864F6DA530D109B30F5992255AFLLO
+ _type_layout_string 18AppleMediaServices19SelfieConfigurationV17FaceIDCalibrationV
- -[AMSProcessInfo _ensureAllPropertiesResolved]
- -[AMSProcessInfo _resolveRecordPropertiesIfNeededLocked]
- _OBJC_IVAR_$_AMSProcessInfo._recordPropertiesResolved
- ___block_descriptor_48_e8_32s40bs_e24_24?0^{__CFString=}8#16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e15_"NSBundle"8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s_e53_v24?0"AMSMetricsFigaroBagConfguration"8"NSError"16ls32l8s40l8
- ___block_descriptor_64_e8_32s40bs_e5_v8?0ls32l8u48l8s40l8
- ___swift_memcpy295_8
- ___swift_memcpy599_8
- _objc_msgSend$_ensureAllPropertiesResolved
- _objc_msgSend$_resolveRecordPropertiesIfNeededLocked
CStrings:
+ " bytes); dropping"
+ "%{public}@: [%{public}@] Cannot schedule flush for container %{public}@ with style %{public}ld (no flush interval available)"
+ "%{public}@: [%{public}@] Cannot schedule flush for container %{public}@ with style %{public}ld because one is already scheduled and pending; it may be one deferred until the app becomes active."
+ "%{public}@: [%{public}@] Cannot schedule flush for container %{public}@ with style %{public}ld because the style is currently not allowed."
+ "%{public}@: [%{public}@] Flush scheduled for container %{public}@. (style: %{public}ld, time: %{public}.3f)"
+ "%{public}@: [%{public}@] Not scheduling flush for container %{public}@ because we failed to get Figaro bag configuration: %{public}@"
+ "%{public}@: [%{public}@] Replacing a deferred flush for container %{public}@ that has not run yet; the app has not become active since it was deferred."
+ "%{public}@: [%{public}@] Scheduled flush for container %{public}@ with flush style %{public}ld unable to run while app is inactive, it will be run when app becomes active again."
+ "%{public}@authResults credential source AKCredentialCollectionIsLoud = %{public}@"
+ "2`"
+ "@\"NSString\"8@?0"
+ "@\"NSURL\"8@?0"
+ "AMSCardEnrollmentWarmWindowCount"
+ "AMSCardEnrollmentWarmWindowStart"
+ "CardEnrollmentCacheWarming"
+ "Diagnostic attachment too large ("
+ "Failed to write diagnostic attachment. Error: "
+ "Passcode Engagement not available: Feature flag turned off"
+ "PasscodeEngagement"
+ "Rejected unsafe diagnostic filename: "
+ "centerBinPitchMaximum"
+ "centerBinPitchMinimum"
+ "correctionSeedFrameCount"
+ "faceIDCalibration"
+ "pitchCorrectionAlpha"
+ "pitchRangeComputeMax"
+ "pitchRangeComputeMin"
+ "pitchRangeForCorrectionMinimum"
- "%{public}@: [%{public}@] Cannot schedule flush with style %{public}ld (no flush interval available)"
- "%{public}@: [%{public}@] Cannot schedule flush with style %{public}ld because one has already been scheduled and is pending."
- "%{public}@: [%{public}@] Cannot schedule flush with style %{public}ld because the style is currently not allowed."
- "%{public}@: [%{public}@] Flush scheduled. (style: %{public}ld, time: %{public}.3f)"
- "%{public}@: [%{public}@] Not scheduling flush because we failed to get Figaro bag configuration: %{public}@"
- "%{public}@: [%{public}@] Scheduled flush for container %@{public}@ with flush style %{public}ld unable to run while app is inactive, it will be run when app becomes active again."
- "@\"NSBundle\"8@?0"
- "@24@?0^{__CFString=}8#16"
```
