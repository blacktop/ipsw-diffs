## ShazamCore

> `/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore`

```diff

-426.4.31.0.0
-  __TEXT.__text: 0x16ffc
+426.4.35.1.0
+  __TEXT.__text: 0x16c2c
   __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_methlist: 0x146c
+  __TEXT.__objc_methlist: 0x1334
   __TEXT.__const: 0x1454
-  __TEXT.__gcc_except_tab: 0x1e8
-  __TEXT.__oslogstring: 0x813
-  __TEXT.__cstring: 0x10d2
+  __TEXT.__gcc_except_tab: 0x198
+  __TEXT.__oslogstring: 0x8c3
+  __TEXT.__cstring: 0x1102
   __TEXT.__swift5_typeref: 0x3b2
   __TEXT.__swift5_capture: 0x5c
   __TEXT.__swift_as_entry: 0x14

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x54
-  __TEXT.__unwind_info: 0x958
+  __TEXT.__unwind_info: 0x8c0
   __TEXT.__eh_frame: 0x688
-  __TEXT.__objc_classname: 0x351
-  __TEXT.__objc_methname: 0x39e8
-  __TEXT.__objc_methtype: 0x76c
-  __TEXT.__objc_stubs: 0x2580
+  __TEXT.__objc_classname: 0x34e
+  __TEXT.__objc_methname: 0x32e3
+  __TEXT.__objc_methtype: 0x75c
+  __TEXT.__objc_stubs: 0x2400
   __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__const: 0x6b8
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xda0
+  __DATA_CONST.__objc_selrefs: 0xcc8
   __DATA_CONST.__objc_superrefs: 0xe0
   __AUTH_CONST.__auth_got: 0x678
-  __AUTH_CONST.__const: 0xd88
-  __AUTH_CONST.__cfstring: 0x1260
-  __AUTH_CONST.__objc_const: 0x2bd0
+  __AUTH_CONST.__const: 0xbe8
+  __AUTH_CONST.__cfstring: 0x12a0
+  __AUTH_CONST.__objc_const: 0x2930
   __AUTH.__objc_data: 0x9d0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_ivar: 0x10c
   __DATA.__data: 0x550
   __DATA.__bss: 0x2500
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5F0EE09C-C202-3057-8B84-CD303D2B8196
-  Functions: 783
-  Symbols:   2000
-  CStrings:  1111
+  UUID: 712F25BD-90E8-3A88-B9E8-36009867F758
+  Functions: 746
+  Symbols:   1882
+  CStrings:  1064
 
Symbols:
+ -[SHRematchBagConfiguration amsPromise]
+ -[SHRematchBagConfiguration initWithPromise:]
+ -[SHRematchBagConfiguration setAmsPromise:]
+ -[SHRematchBagConfiguration setConfiguration:]
+ -[SHRemoteConfiguration rematchBagConfigurationWithPromise]
+ _OBJC_IVAR_$_SHRematchBagConfiguration._amsPromise
+ ___45-[SHRematchBagConfiguration initWithPromise:]_block_invoke
+ ___45-[SHRematchBagConfiguration initWithPromise:]_block_invoke.2
+ ___53-[SHRemoteConfiguration campaignTokenWithCompletion:]_block_invoke.65
+ ___69-[SHRemoteConfiguration announcementsBagConfigurationWithCompletion:]_block_invoke.76
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e50_v24?0"SHDefaultConfigurationValues"8"NSError"16ls40l8s32l8
+ _objc_msgSend$addErrorBlock:
+ _objc_msgSend$setAmsPromise:
+ _objc_msgSend$setConfiguration:
- -[SHRemoteConfiguration announcementsBagValue]
- -[SHRemoteConfiguration cacheValuesBagValue]
- -[SHRemoteConfiguration campaignTokenBagValue]
- -[SHRemoteConfiguration defaultValuesBagValue]
- -[SHRemoteConfiguration endpointsBagValue]
- -[SHRemoteConfiguration externalHostBagValue]
- -[SHRemoteConfiguration featureFlagsBagValue]
- -[SHRemoteConfiguration hapticsEndpointsBagValue]
- -[SHRemoteConfiguration internalHostBagValue]
- -[SHRemoteConfiguration languageTagBagValue]
- -[SHRemoteConfiguration musicalFeaturesBagConfigurationValue]
- -[SHRemoteConfiguration populateRemoteConfiguration]
- -[SHRemoteConfiguration recorderConfigurationBagValue]
- -[SHRemoteConfiguration rematchBagConfigurationValue]
- -[SHRemoteConfiguration setAnnouncementsBagValue:]
- -[SHRemoteConfiguration setCacheValuesBagValue:]
- -[SHRemoteConfiguration setCampaignTokenBagValue:]
- -[SHRemoteConfiguration setDefaultValuesBagValue:]
- -[SHRemoteConfiguration setEndpointsBagValue:]
- -[SHRemoteConfiguration setExternalHostBagValue:]
- -[SHRemoteConfiguration setFeatureFlagsBagValue:]
- -[SHRemoteConfiguration setHapticsEndpointsBagValue:]
- -[SHRemoteConfiguration setInternalHostBagValue:]
- -[SHRemoteConfiguration setLanguageTagBagValue:]
- -[SHRemoteConfiguration setMusicalFeaturesBagConfigurationValue:]
- -[SHRemoteConfiguration setRecorderConfigurationBagValue:]
- -[SHRemoteConfiguration setRematchBagConfigurationValue:]
- -[SHRemoteConfiguration setShazamAMPConfigurationAPIEndpointsBagValue:]
- -[SHRemoteConfiguration setShazamOfferAPIHostsBagValue:]
- -[SHRemoteConfiguration shazamAMPConfigurationAPIEndpointsBagValue]
- -[SHRemoteConfiguration shazamOfferAPIHostsBagValue]
- GCC_except_table19
- GCC_except_table24
- GCC_except_table29
- GCC_except_table50
- _OBJC_IVAR_$_SHRemoteConfiguration._announcementsBagValue
- _OBJC_IVAR_$_SHRemoteConfiguration._cacheValuesBagValue
- _OBJC_IVAR_$_SHRemoteConfiguration._campaignTokenBagValue
- _OBJC_IVAR_$_SHRemoteConfiguration._defaultValuesBagValue
- _OBJC_IVAR_$_SHRemoteConfiguration._endpointsBagValue
- _OBJC_IVAR_$_SHRemoteConfiguration._externalHostBagValue
- _OBJC_IVAR_$_SHRemoteConfiguration._featureFlagsBagValue
- _OBJC_IVAR_$_SHRemoteConfiguration._hapticsEndpointsBagValue
- _OBJC_IVAR_$_SHRemoteConfiguration._internalHostBagValue
- _OBJC_IVAR_$_SHRemoteConfiguration._languageTagBagValue
- _OBJC_IVAR_$_SHRemoteConfiguration._musicalFeaturesBagConfigurationValue
- _OBJC_IVAR_$_SHRemoteConfiguration._recorderConfigurationBagValue
- _OBJC_IVAR_$_SHRemoteConfiguration._rematchBagConfigurationValue
- _OBJC_IVAR_$_SHRemoteConfiguration._shazamAMPConfigurationAPIEndpointsBagValue
- _OBJC_IVAR_$_SHRemoteConfiguration._shazamOfferAPIHostsBagValue
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_10
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_11
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_12
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_13
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_2
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_3
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_4
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_5
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_6
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_7
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_8
- ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_9
- ___53-[SHRemoteConfiguration campaignTokenWithCompletion:]_block_invoke.91
- ___69-[SHRemoteConfiguration announcementsBagConfigurationWithCompletion:]_block_invoke.102
- ___block_descriptor_32_e23_v28?08B16"NSError"20l
- ___block_descriptor_48_e8_32bs40w_e23_v28?08B16"NSError"20ls32l8w40l8
- ___block_descriptor_48_e8_32bs40w_e23_v28?08B16"NSError"20lw40l8s32l8
- ___block_descriptor_48_e8_32bs40w_e50_v24?0"SHDefaultConfigurationValues"8"NSError"16ls32l8w40l8
- ___block_literal_global.58
- ___block_literal_global.60
- ___block_literal_global.62
- ___block_literal_global.64
- ___block_literal_global.66
- ___block_literal_global.68
- ___block_literal_global.70
- ___block_literal_global.72
- ___block_literal_global.74
- ___block_literal_global.76
- ___block_literal_global.78
- ___block_literal_global.80
- ___block_literal_global.82
- _objc_msgSend$announcementsBagValue
- _objc_msgSend$cacheValuesBagValue
- _objc_msgSend$campaignTokenBagValue
- _objc_msgSend$defaultValuesBagValue
- _objc_msgSend$endpointsBagValue
- _objc_msgSend$externalHostBagValue
- _objc_msgSend$featureFlagsBagValue
- _objc_msgSend$hapticsEndpointsBagValue
- _objc_msgSend$internalHostBagValue
- _objc_msgSend$languageTagBagValue
- _objc_msgSend$musicalFeaturesBagConfigurationValue
- _objc_msgSend$recorderConfigurationBagValue
- _objc_msgSend$rematchBagConfigurationValue
- _objc_msgSend$shazamAMPConfigurationAPIEndpointsBagValue
- _objc_msgSend$shazamOfferAPIHostsBagValue
CStrings:
+ "Failed to load rematch bag configuration: %@"
+ "Musical features bag not yet loaded for client %@"
+ "Rematch bag configuration loaded successfully"
+ "Rematch bag not loaded yet for '%@', defaulting to disabled"
+ "Rematch for '%@' is %@"
+ "T@\"AMSPromise\",&,N,V_amsPromise"
+ "T@\"NSDictionary\",&,N,V_configuration"
+ "addErrorBlock:"
+ "disabled"
+ "enabled"
+ "rematchBagConfigurationWithPromise"
+ "setAmsPromise:"
+ "setConfiguration:"
+ "v16@?0@\"NSError\"8"
- "@\"AMSBagValue\""
- "Populating remote configuration..."
- "T@\"AMSBagValue\",&,N,V_announcementsBagValue"
- "T@\"AMSBagValue\",&,N,V_cacheValuesBagValue"
- "T@\"AMSBagValue\",&,N,V_campaignTokenBagValue"
- "T@\"AMSBagValue\",&,N,V_defaultValuesBagValue"
- "T@\"AMSBagValue\",&,N,V_endpointsBagValue"
- "T@\"AMSBagValue\",&,N,V_externalHostBagValue"
- "T@\"AMSBagValue\",&,N,V_featureFlagsBagValue"
- "T@\"AMSBagValue\",&,N,V_hapticsEndpointsBagValue"
- "T@\"AMSBagValue\",&,N,V_internalHostBagValue"
- "T@\"AMSBagValue\",&,N,V_languageTagBagValue"
- "T@\"AMSBagValue\",&,N,V_musicalFeaturesBagConfigurationValue"
- "T@\"AMSBagValue\",&,N,V_recorderConfigurationBagValue"
- "T@\"AMSBagValue\",&,N,V_rematchBagConfigurationValue"
- "T@\"AMSBagValue\",&,N,V_shazamAMPConfigurationAPIEndpointsBagValue"
- "T@\"AMSBagValue\",&,N,V_shazamOfferAPIHostsBagValue"
- "_announcementsBagValue"
- "_cacheValuesBagValue"
- "_campaignTokenBagValue"
- "_defaultValuesBagValue"
- "_endpointsBagValue"
- "_externalHostBagValue"
- "_featureFlagsBagValue"
- "_hapticsEndpointsBagValue"
- "_internalHostBagValue"
- "_languageTagBagValue"
- "_musicalFeaturesBagConfigurationValue"
- "_recorderConfigurationBagValue"
- "_rematchBagConfigurationValue"
- "_shazamAMPConfigurationAPIEndpointsBagValue"
- "_shazamOfferAPIHostsBagValue"
- "announcementsBagValue"
- "cacheValuesBagValue"
- "campaignTokenBagValue"
- "defaultValuesBagValue"
- "endpointsBagValue"
- "externalHostBagValue"
- "featureFlagsBagValue"
- "hapticsEndpointsBagValue"
- "internalHostBagValue"
- "languageTagBagValue"
- "musicalFeaturesBagConfigurationValue"
- "populateRemoteConfiguration"
- "recorderConfigurationBagValue"
- "rematchBagConfigurationValue"
- "setAnnouncementsBagValue:"
- "setCacheValuesBagValue:"
- "setCampaignTokenBagValue:"
- "setDefaultValuesBagValue:"
- "setEndpointsBagValue:"
- "setExternalHostBagValue:"
- "setFeatureFlagsBagValue:"
- "setHapticsEndpointsBagValue:"
- "setInternalHostBagValue:"
- "setLanguageTagBagValue:"
- "setMusicalFeaturesBagConfigurationValue:"
- "setRecorderConfigurationBagValue:"
- "setRematchBagConfigurationValue:"
- "setShazamAMPConfigurationAPIEndpointsBagValue:"
- "setShazamOfferAPIHostsBagValue:"
- "shazamAMPConfigurationAPIEndpointsBagValue"
- "shazamOfferAPIHostsBagValue"

```
