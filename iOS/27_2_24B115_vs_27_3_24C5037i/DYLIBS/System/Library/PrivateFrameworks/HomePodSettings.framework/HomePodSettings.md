## HomePodSettings

> `/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings`

```diff

-346.10.26.0.0
-  __TEXT.__text: 0x6b88c
-  __TEXT.__objc_methlist: 0x1f94
-  __TEXT.__const: 0x5250
-  __TEXT.__cstring: 0x2d41
+346.20.14.0.0
+  __TEXT.__text: 0x6d7a8
+  __TEXT.__objc_methlist: 0x1ffc
+  __TEXT.__const: 0x5430
+  __TEXT.__cstring: 0x2e91
   __TEXT.__oslogstring: 0x1119
   __TEXT.__ustring: 0x4
-  __TEXT.__gcc_except_tab: 0x1b0
-  __TEXT.__constg_swiftt: 0x175c
-  __TEXT.__swift5_typeref: 0x1b7b
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_types: 0x170
+  __TEXT.__gcc_except_tab: 0x1c0
+  __TEXT.__constg_swiftt: 0x177c
+  __TEXT.__swift5_typeref: 0x1c0b
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_reflstr: 0xdf0
+  __TEXT.__swift5_fieldmd: 0x1618
+  __TEXT.__swift5_assocty: 0x3b8
+  __TEXT.__swift5_proto: 0x384
+  __TEXT.__swift5_types: 0x174
   __TEXT.__swift5_capture: 0xb08
-  __TEXT.__swift5_reflstr: 0xdc0
-  __TEXT.__swift5_assocty: 0x388
-  __TEXT.__swift5_fieldmd: 0x15fc
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_proto: 0x36c
   __TEXT.__swift_as_entry: 0x198
   __TEXT.__swift_as_ret: 0x170
   __TEXT.__swift_as_cont: 0x3cc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x32a8
-  __TEXT.__eh_frame: 0x4928
+  __TEXT.__unwind_info: 0x3368
+  __TEXT.__eh_frame: 0x4970
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xaa0
+  __DATA_CONST.__const: 0xaf8
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb30
+  __DATA_CONST.__objc_selrefs: 0xb90
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x4a8
-  __AUTH_CONST.__const: 0x3a78
-  __AUTH_CONST.__cfstring: 0x1360
-  __AUTH_CONST.__objc_const: 0x64b0
+  __DATA_CONST.__got: 0x4b8
+  __AUTH_CONST.__const: 0x3aa0
+  __AUTH_CONST.__cfstring: 0x13c0
+  __AUTH_CONST.__objc_const: 0x64c0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xfc0
+  __AUTH_CONST.__auth_got: 0xfe8
   __AUTH.__objc_data: 0x1e20
   __AUTH.__data: 0xd68
   __DATA.__objc_ivar: 0xc8
-  __DATA.__data: 0x1b58
+  __DATA.__data: 0x1bb8
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4059
-  Symbols:   2286
-  CStrings:  414
+  Functions: 4117
+  Symbols:   2304
+  CStrings:  419
 
Symbols:
+ +[HPSFeatureStatus isHomePodSiriRestrictionsEnabled]
+ +[HPSHomeKitSettingHelper compatibleReadResult:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper compatibleReadResults:forClientKeyPaths:]
+ +[HPSHomeKitSettingHelper compatibleReadSetting:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper compatibleWriteSetting:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper fixUpAppleIntelligenceReportDuration:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper fixUpAssistantEnabled:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper fixUpAutoAdjustSiriVolumeEnabled:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper fixUpDisplayMediaVisualizerDefaultColor:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper fixUpDisplayMediaVisualizerVisualization:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper fixUpHoldDuration:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper fixUpIgnoreRepeat:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper fixUpSiriEnabled:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper fixUpSpeakingRate:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper fixUpTapAssistanceSelection:forClientKeyPath:]
+ +[HPSHomeKitSettingHelper fixUpTimeoutInterval:forClientKeyPath:]
+ GCC_except_table53
+ GCC_except_table58
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table73
+ GCC_except_table76
+ GCC_except_table95
+ _HPSKeyPathSiriEnabled
+ __OBJC_$_CLASS_METHODS_HPSHomeKitSettingHelper(HomePodSettings)
+ ___67+[HPSHomeKitSettingHelper compatibleReadResults:forClientKeyPaths:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e32_v24?0"HPSSetting"8"NSError"16lr40l8s32l8
+ ___block_descriptor_64_e8_32s40s48r_e26_v32?0"HPSResult"8Q16^B24ls32l8r48l8s40l8
+ _associated conformance So10HPSKeyPathaSHSCSQ
+ _associated conformance So10HPSKeyPathas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So10HPSKeyPathas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _swift_bridgeObjectRetain_n
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic Say_____G So10HPSKeyPatha
+ _symbolic So10HPSSettingCm
+ _symbolic _____ So10HPSKeyPatha
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So10HPSKeyPatha
+ _symbolic _____y_____SayABGG s18_DictionaryStorageC So10HPSKeyPatha
+ _symbolic _____y_____SbG s17_NativeDictionaryV So10HPSKeyPatha
+ _type_layout_string So10HPSKeyPatha
- +[HPSHomeKitSettingHelper compatibleReadResult:]
- +[HPSHomeKitSettingHelper compatibleReadResults:]
- +[HPSHomeKitSettingHelper compatibleReadSetting:]
- +[HPSHomeKitSettingHelper compatibleWriteSetting:]
- +[HPSHomeKitSettingHelper fixUpAppleIntelligenceReportDuration:]
- +[HPSHomeKitSettingHelper fixUpAutoAdjustSiriVolumeEnabled:]
- +[HPSHomeKitSettingHelper fixUpDisplayMediaVisualizerDefaultColor:]
- +[HPSHomeKitSettingHelper fixUpDisplayMediaVisualizerVisualization:]
- +[HPSHomeKitSettingHelper fixUpHoldDuration:]
- +[HPSHomeKitSettingHelper fixUpIgnoreRepeat:]
- +[HPSHomeKitSettingHelper fixUpSpeakingRate:]
- +[HPSHomeKitSettingHelper fixUpTapAssistanceSelection:]
- +[HPSHomeKitSettingHelper fixUpTimeoutInterval:]
- GCC_except_table51
- GCC_except_table56
- GCC_except_table65
- GCC_except_table68
- GCC_except_table71
- GCC_except_table74
- GCC_except_table93
- __OBJC_$_CLASS_METHODS_HPSHomeKitSettingHelper
- ___49+[HPSHomeKitSettingHelper compatibleReadResults:]_block_invoke
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
- ___block_descriptor_40_e8_32r_e32_v24?0"HPSSetting"8"NSError"16lr32l8
- ___block_descriptor_56_e8_32s40r_e26_v32?0"HPSResult"8Q16^B24lr40l8s32l8
CStrings:
+ " should not be a "
+ "+[HPSHomeKitSettingHelper compatibleReadSetting:forClientKeyPath:]"
+ "+[HPSHomeKitSettingHelper compatibleWriteSetting:forClientKeyPath:]"
+ "HomePodSiriRestrictions"
+ "fixUpAppleIntelligenceReportDuration:forClientKeyPath:"
+ "fixUpAssistantEnabled:forClientKeyPath:"
+ "fixUpAutoAdjustSiriVolumeEnabled:forClientKeyPath:"
+ "fixUpDisplayMediaVisualizerDefaultColor:forClientKeyPath:"
+ "fixUpDisplayMediaVisualizerVisualization:forClientKeyPath:"
+ "fixUpHoldDuration:forClientKeyPath:"
+ "fixUpIgnoreRepeat:forClientKeyPath:"
+ "fixUpSiriEnabled:forClientKeyPath:"
+ "fixUpSpeakingRate:forClientKeyPath:"
+ "fixUpTapAssistanceSelection:forClientKeyPath:"
+ "fixUpTimeoutInterval:forClientKeyPath:"
+ "root.siri.siriEnabled"
- "+[HPSHomeKitSettingHelper compatibleReadSetting:]"
- "+[HPSHomeKitSettingHelper compatibleWriteSetting:]"
- "fixUpAppleIntelligenceReportDuration:"
- "fixUpAutoAdjustSiriVolumeEnabled:"
- "fixUpDisplayMediaVisualizerDefaultColor:"
- "fixUpDisplayMediaVisualizerVisualization:"
- "fixUpHoldDuration:"
- "fixUpIgnoreRepeat:"
- "fixUpSpeakingRate:"
- "fixUpTapAssistanceSelection:"
- "fixUpTimeoutInterval:"
```
