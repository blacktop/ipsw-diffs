## Intents

> `/System/Library/Frameworks/Intents.framework/Intents`

```diff

-2504.0.0.0.0
-  __TEXT.__text: 0x4338b8
+2600.0.0.0.0
+  __TEXT.__text: 0x434bc8
   __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_methlist: 0x553d8
+  __TEXT.__objc_methlist: 0x55510
   __TEXT.__const: 0x19e0
   __TEXT.__gcc_except_tab: 0x17d4
   __TEXT.__oslogstring: 0x54bc
-  __TEXT.__cstring: 0x46b5a
+  __TEXT.__cstring: 0x46b6a
   __TEXT.__dlopen_cstrs: 0xc6c
   __TEXT.__ustring: 0x512
-  __TEXT.__unwind_info: 0x11224
-  __TEXT.__objc_classname: 0x12188
-  __TEXT.__objc_methname: 0x68846
-  __TEXT.__objc_methtype: 0xca4c
-  __TEXT.__objc_stubs: 0x33340
+  __TEXT.__unwind_info: 0x11370
+  __TEXT.__objc_classname: 0x12184
+  __TEXT.__objc_methname: 0x68cd8
+  __TEXT.__objc_methtype: 0xcad0
+  __TEXT.__objc_stubs: 0x333a0
   __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0xb1d8
   __DATA_CONST.__objc_classlist: 0x28f8
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x1938
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc8248
-  __DATA_CONST.__objc_selrefs: 0x14f60
+  __DATA_CONST.__objc_const: 0xc86f8
+  __DATA_CONST.__objc_selrefs: 0x14fa0
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_classrefs: 0x2670
   __DATA_CONST.__objc_superrefs: 0x1370
   __DATA_CONST.__objc_arraydata: 0xc298
   __AUTH_CONST.__objc_const: 0x2de38
-  __AUTH_CONST.__cfstring: 0x41dc0
+  __AUTH_CONST.__cfstring: 0x41de0
   __AUTH_CONST.__const: 0x16e0
   __AUTH_CONST.__objc_intobj: 0x828
   __AUTH_CONST.__objc_doubleobj: 0x20

   __AUTH_CONST.__objc_dictobj: 0x3a48
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0x818
-  __AUTH.__objc_data: 0x143e8
-  __DATA.__objc_ivar: 0x3c98
-  __DATA.__data: 0x13368
+  __AUTH.__objc_data: 0x14168
+  __DATA.__objc_ivar: 0x3cc0
+  __DATA.__data: 0x13388
   __DATA.__common: 0x0
-  __DATA.__bss: 0x7e0
+  __DATA.__bss: 0x7b0
   __DATA_DIRTY.__const: 0x61b
-  __DATA_DIRTY.__objc_data: 0x55c8
+  __DATA_DIRTY.__objc_data: 0x5848
   __DATA_DIRTY.__common: 0x8
-  __DATA_DIRTY.__bss: 0x260
+  __DATA_DIRTY.__bss: 0x270
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 30879
-  Symbols:   88121
-  CStrings:  28496
+  Functions: 30905
+  Symbols:   88184
+  CStrings:  28508
 
Symbols:
+ -[INPrivateAddMediaIntentData initWithPrivateMediaIntentData:audioSearchResults:internalSignals:pegasusMetaData:]
+ -[INPrivateAddMediaIntentData pegasusMetaData]
+ -[INPrivateMediaItemValueData initWithRecommendationId:assetInfo:sharedUserIdFromPlayableMusicAccount:punchoutURI:requiresSubscription:provider:isAvailable:isHardBan:bundleId:universalResourceLink:providerAppName:internalSignals:ampConfidenceScore:ampConfidenceLevel:pegasusMetaData:mediaSubItems:]
+ -[INPrivateMediaItemValueData pegasusMetaData]
+ -[INPrivatePlayMediaIntentData initWithAppSelectionEnabled:appInferred:audioSearchResults:privateMediaIntentData:appSelectionSignalsEnabled:appSelectionSignalsFrequencyDenominator:shouldSuppressCommonWholeHouseAudioRoutes:immediatelyStartPlayback:isAmbiguousPlay:isPersonalizedRequest:internalSignals:entityConfidenceSignalsEnabled:entityConfidenceSignalsFrequencyDenominatorInternal:entityConfidenceSignalsFrequencyDenominatorProd:entityConfidenceSignalsMaxItemsToDisambiguate:alternativeProviderBundleIdentifier:ampPAFDataSetID:pegasusMetaData:]
+ -[INPrivatePlayMediaIntentData pegasusMetaData]
+ -[INPrivateSearchForMediaIntentData initWithPrivateMediaIntentData:audioSearchResults:internalSignals:appInferred:pegasusMetaData:]
+ -[INPrivateSearchForMediaIntentData pegasusMetaData]
+ -[INPrivateUpdateMediaAffinityIntentData initWithPrivateMediaIntentData:internalSignals:pegasusMetaData:]
+ -[INPrivateUpdateMediaAffinityIntentData pegasusMetaData]
+ -[_INPBPrivateAddMediaIntentData hasPegasusMetaData]
+ -[_INPBPrivateAddMediaIntentData pegasusMetaData]
+ -[_INPBPrivateAddMediaIntentData setPegasusMetaData:]
+ -[_INPBPrivateMediaItemValueData hasPegasusMetaData]
+ -[_INPBPrivateMediaItemValueData pegasusMetaData]
+ -[_INPBPrivateMediaItemValueData setPegasusMetaData:]
+ -[_INPBPrivatePlayMediaIntentData hasPegasusMetaData]
+ -[_INPBPrivatePlayMediaIntentData pegasusMetaData]
+ -[_INPBPrivatePlayMediaIntentData setPegasusMetaData:]
+ -[_INPBPrivateSearchForMediaIntentData hasPegasusMetaData]
+ -[_INPBPrivateSearchForMediaIntentData pegasusMetaData]
+ -[_INPBPrivateSearchForMediaIntentData setPegasusMetaData:]
+ -[_INPBPrivateUpdateMediaAffinityIntentData hasPegasusMetaData]
+ -[_INPBPrivateUpdateMediaAffinityIntentData pegasusMetaData]
+ -[_INPBPrivateUpdateMediaAffinityIntentData setPegasusMetaData:]
+ GCC_except_table26924
+ GCC_except_table26927
+ GCC_except_table26928
+ GCC_except_table26929
+ GCC_except_table26930
+ GCC_except_table28624
+ GCC_except_table29670
+ GCC_except_table29671
+ GCC_except_table29675
+ GCC_except_table29676
+ GCC_except_table29677
+ GCC_except_table29678
+ GCC_except_table29679
+ GCC_except_table29684
+ GCC_except_table29686
+ GCC_except_table29687
+ GCC_except_table29688
+ GCC_except_table29689
+ GCC_except_table29692
+ GCC_except_table29881
+ _LinkServicesLibraryCore.frameworkLibrary.165612
+ _OBJC_IVAR_$_INPrivateAddMediaIntentData._pegasusMetaData
+ _OBJC_IVAR_$_INPrivateMediaItemValueData._pegasusMetaData
+ _OBJC_IVAR_$_INPrivatePlayMediaIntentData._pegasusMetaData
+ _OBJC_IVAR_$_INPrivateSearchForMediaIntentData._pegasusMetaData
+ _OBJC_IVAR_$_INPrivateUpdateMediaAffinityIntentData._pegasusMetaData
+ _OBJC_IVAR_$__INPBPrivateAddMediaIntentData._pegasusMetaData
+ _OBJC_IVAR_$__INPBPrivateMediaItemValueData._pegasusMetaData
+ _OBJC_IVAR_$__INPBPrivatePlayMediaIntentData._pegasusMetaData
+ _OBJC_IVAR_$__INPBPrivateSearchForMediaIntentData._pegasusMetaData
+ _OBJC_IVAR_$__INPBPrivateUpdateMediaAffinityIntentData._pegasusMetaData
+ __OBJC_$_PROP_LIST__INPBPrivateAddMediaIntentData.134
+ __OBJC_$_PROP_LIST__INPBPrivateMediaItemValueData.274
+ __OBJC_$_PROP_LIST__INPBPrivatePlayMediaIntentData.299
+ __OBJC_$_PROP_LIST__INPBPrivateSearchForMediaIntentData.149
+ __OBJC_$_PROP_LIST__INPBPrivateUpdateMediaAffinityIntentData.117
+ ___LinkServicesLibraryCore_block_invoke.165613
+ ___block_literal_global.157943
+ ___block_literal_global.4.157936
+ _audit_stringLinkServices.165618
+ _objc_msgSend$initWithAppSelectionEnabled:appInferred:audioSearchResults:privateMediaIntentData:appSelectionSignalsEnabled:appSelectionSignalsFrequencyDenominator:shouldSuppressCommonWholeHouseAudioRoutes:immediatelyStartPlayback:isAmbiguousPlay:isPersonalizedRequest:internalSignals:entityConfidenceSignalsEnabled:entityConfidenceSignalsFrequencyDenominatorInternal:entityConfidenceSignalsFrequencyDenominatorProd:entityConfidenceSignalsMaxItemsToDisambiguate:alternativeProviderBundleIdentifier:ampPAFDataSetID:pegasusMetaData:
+ _objc_msgSend$initWithPrivateMediaIntentData:audioSearchResults:internalSignals:appInferred:pegasusMetaData:
+ _objc_msgSend$initWithPrivateMediaIntentData:audioSearchResults:internalSignals:pegasusMetaData:
+ _objc_msgSend$initWithPrivateMediaIntentData:internalSignals:pegasusMetaData:
+ _objc_msgSend$initWithRecommendationId:assetInfo:sharedUserIdFromPlayableMusicAccount:punchoutURI:requiresSubscription:provider:isAvailable:isHardBan:bundleId:universalResourceLink:providerAppName:internalSignals:ampConfidenceScore:ampConfidenceLevel:pegasusMetaData:mediaSubItems:
+ _objc_msgSend$pegasusMetaData
+ _objc_msgSend$setPegasusMetaData:
- GCC_except_table26904
- GCC_except_table26907
- GCC_except_table26908
- GCC_except_table26909
- GCC_except_table26910
- GCC_except_table28599
- GCC_except_table29638
- GCC_except_table29645
- GCC_except_table29646
- GCC_except_table29650
- GCC_except_table29651
- GCC_except_table29652
- GCC_except_table29653
- GCC_except_table29654
- GCC_except_table29659
- GCC_except_table29661
- GCC_except_table29662
- GCC_except_table29664
- GCC_except_table29667
- GCC_except_table29856
- _LinkServicesLibraryCore.frameworkLibrary.165490
- __OBJC_$_PROP_LIST__INPBPrivateAddMediaIntentData.120
- __OBJC_$_PROP_LIST__INPBPrivateMediaItemValueData.260
- __OBJC_$_PROP_LIST__INPBPrivatePlayMediaIntentData.285
- __OBJC_$_PROP_LIST__INPBPrivateSearchForMediaIntentData.135
- __OBJC_$_PROP_LIST__INPBPrivateUpdateMediaAffinityIntentData.103
- ___LinkServicesLibraryCore_block_invoke.165491
- ___block_literal_global.157821
- ___block_literal_global.4.157814
- _audit_stringLinkServices.165496
- _objc_msgSend$initWithAppSelectionEnabled:appInferred:audioSearchResults:privateMediaIntentData:appSelectionSignalsEnabled:appSelectionSignalsFrequencyDenominator:shouldSuppressCommonWholeHouseAudioRoutes:immediatelyStartPlayback:isAmbiguousPlay:isPersonalizedRequest:internalSignals:entityConfidenceSignalsEnabled:entityConfidenceSignalsFrequencyDenominatorInternal:entityConfidenceSignalsFrequencyDenominatorProd:entityConfidenceSignalsMaxItemsToDisambiguate:alternativeProviderBundleIdentifier:ampPAFDataSetID:
- _objc_msgSend$initWithPrivateMediaIntentData:audioSearchResults:internalSignals:
- _objc_msgSend$initWithPrivateMediaIntentData:audioSearchResults:internalSignals:appInferred:
- _objc_msgSend$initWithPrivateMediaIntentData:internalSignals:
CStrings:
+ "\r\x12"
+ "\x0f\x03"
+ "@144@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112q120@128@136"
+ "@160@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152"
+ "T@\"NSData\",C,N,V_pegasusMetaData"
+ "T@\"NSData\",R,C,N,V_pegasusMetaData"
+ "_pegasusMetaData"
+ "hasPegasusMetaData"
+ "initWithAppSelectionEnabled:appInferred:audioSearchResults:privateMediaIntentData:appSelectionSignalsEnabled:appSelectionSignalsFrequencyDenominator:shouldSuppressCommonWholeHouseAudioRoutes:immediatelyStartPlayback:isAmbiguousPlay:isPersonalizedRequest:internalSignals:entityConfidenceSignalsEnabled:entityConfidenceSignalsFrequencyDenominatorInternal:entityConfidenceSignalsFrequencyDenominatorProd:entityConfidenceSignalsMaxItemsToDisambiguate:alternativeProviderBundleIdentifier:ampPAFDataSetID:pegasusMetaData:"
+ "initWithPrivateMediaIntentData:audioSearchResults:internalSignals:appInferred:pegasusMetaData:"
+ "initWithPrivateMediaIntentData:audioSearchResults:internalSignals:pegasusMetaData:"
+ "initWithPrivateMediaIntentData:internalSignals:pegasusMetaData:"
+ "initWithRecommendationId:assetInfo:sharedUserIdFromPlayableMusicAccount:punchoutURI:requiresSubscription:provider:isAvailable:isHardBan:bundleId:universalResourceLink:providerAppName:internalSignals:ampConfidenceScore:ampConfidenceLevel:pegasusMetaData:mediaSubItems:"
+ "pegasusMetaData"
+ "setPegasusMetaData:"
- "\r\x11"
- "\x0f\x02"
- "*"
- "E"

```
