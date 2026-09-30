## VoiceShortcutClient

> `/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient`

```diff

-4037.1.4.0.0
-  __TEXT.__text: 0x12de80
-  __TEXT.__auth_stubs: 0x35d0
-  __TEXT.__objc_methlist: 0xc43c
-  __TEXT.__const: 0xbbc8
+4040.0.4.0.0
+  __TEXT.__text: 0x132ef0
+  __TEXT.__auth_stubs: 0x3610
+  __TEXT.__objc_methlist: 0xc46c
+  __TEXT.__const: 0xc678
   __TEXT.__dlopen_cstrs: 0xdb4
-  __TEXT.__cstring: 0x17733
-  __TEXT.__swift5_typeref: 0x2caf
-  __TEXT.__swift5_reflstr: 0x11ca
-  __TEXT.__swift5_assocty: 0x360
-  __TEXT.__constg_swiftt: 0x2c58
-  __TEXT.__swift5_fieldmd: 0x2278
-  __TEXT.__swift5_builtin: 0x154
-  __TEXT.__swift5_proto: 0xa60
-  __TEXT.__swift5_types: 0x370
-  __TEXT.__swift5_capture: 0x448
-  __TEXT.__swift_as_entry: 0xcc
-  __TEXT.__swift_as_ret: 0xbc
-  __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__oslogstring: 0x395b
+  __TEXT.__cstring: 0x17899
+  __TEXT.__swift5_typeref: 0x2ee1
+  __TEXT.__swift5_reflstr: 0x127a
+  __TEXT.__swift5_assocty: 0x390
+  __TEXT.__constg_swiftt: 0x2ea0
+  __TEXT.__swift5_fieldmd: 0x242c
+  __TEXT.__swift5_builtin: 0x168
+  __TEXT.__swift5_proto: 0xb08
+  __TEXT.__swift5_types: 0x3a4
+  __TEXT.__swift5_capture: 0x444
+  __TEXT.__swift_as_entry: 0xc8
+  __TEXT.__swift_as_ret: 0xb4
+  __TEXT.__swift5_mpenum: 0x7c
+  __TEXT.__oslogstring: 0x3b0e
   __TEXT.__swift5_protos: 0x30
   __TEXT.__gcc_except_tab: 0x1be0
   __TEXT.__ustring: 0x14e
-  __TEXT.__unwind_info: 0x5df8
-  __TEXT.__eh_frame: 0x5100
+  __TEXT.__unwind_info: 0x5f50
+  __TEXT.__eh_frame: 0x5248
   __TEXT.__objc_classname: 0x230b
-  __TEXT.__objc_methname: 0x1bb61
+  __TEXT.__objc_methname: 0x1bbf5
   __TEXT.__objc_methtype: 0x482e
-  __TEXT.__objc_stubs: 0x11a20
-  __DATA_CONST.__got: 0x11a0
-  __DATA_CONST.__const: 0x3430
+  __TEXT.__objc_stubs: 0x11a80
+  __DATA_CONST.__got: 0x11a8
+  __DATA_CONST.__const: 0x3448
   __DATA_CONST.__objc_classlist: 0x930
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5ca0
+  __DATA_CONST.__objc_selrefs: 0x5cd0
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x790
   __DATA_CONST.__objc_arraydata: 0x1a10
-  __AUTH_CONST.__auth_got: 0x1b00
-  __AUTH_CONST.__const: 0x7c60
-  __AUTH_CONST.__cfstring: 0x186c0
-  __AUTH_CONST.__objc_const: 0x190a0
+  __AUTH_CONST.__auth_got: 0x1b20
+  __AUTH_CONST.__const: 0x81e0
+  __AUTH_CONST.__cfstring: 0x18880
+  __AUTH_CONST.__objc_const: 0x190c0
   __AUTH_CONST.__objc_intobj: 0x49b0
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH.__objc_data: 0x3a90
-  __AUTH.__data: 0x1a40
+  __AUTH.__data: 0x1aa0
   __DATA.__objc_ivar: 0xc78
-  __DATA.__data: 0x3758
-  __DATA.__bss: 0x143e8
+  __DATA.__data: 0x3968
+  __DATA.__bss: 0x158f0
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x21e8
-  __DATA_DIRTY.__data: 0x560
-  __DATA_DIRTY.__bss: 0x12c0
+  __DATA_DIRTY.__data: 0x570
+  __DATA_DIRTY.__bss: 0x12d0
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E2976B9B-6E0C-393A-834E-08D884C2FE68
-  Functions: 9153
-  Symbols:   18903
-  CStrings:  12580
+  UUID: FC74EF09-B677-30C3-BE06-A9493A3F5508
+  Functions: 9322
+  Symbols:   19018
+  CStrings:  12628
 
Symbols:
+ +[WFColor(Convenience) colorForName:]
+ +[WFColor(Convenience) tintedColorForName:]
+ -[VCVoiceShortcutClient(Spotlight) triggerFullContextualActionReindexWithCompletion:]
+ GCC_except_table1098
+ GCC_except_table1120
+ GCC_except_table1121
+ GCC_except_table1122
+ GCC_except_table1131
+ GCC_except_table1186
+ GCC_except_table1217
+ GCC_except_table1256
+ GCC_except_table1347
+ GCC_except_table1382
+ GCC_except_table1395
+ GCC_except_table1422
+ GCC_except_table1427
+ GCC_except_table1433
+ GCC_except_table1480
+ GCC_except_table1482
+ GCC_except_table1483
+ GCC_except_table1494
+ GCC_except_table1499
+ GCC_except_table1564
+ GCC_except_table1565
+ GCC_except_table1622
+ GCC_except_table1698
+ GCC_except_table1714
+ GCC_except_table1763
+ GCC_except_table1786
+ GCC_except_table1788
+ GCC_except_table1848
+ GCC_except_table1850
+ GCC_except_table1851
+ GCC_except_table1853
+ GCC_except_table1862
+ GCC_except_table1870
+ GCC_except_table1872
+ GCC_except_table1893
+ GCC_except_table2000
+ GCC_except_table2023
+ GCC_except_table2060
+ GCC_except_table2090
+ GCC_except_table2143
+ GCC_except_table2154
+ GCC_except_table2179
+ GCC_except_table2202
+ GCC_except_table2207
+ GCC_except_table2210
+ GCC_except_table2283
+ GCC_except_table2348
+ GCC_except_table2355
+ GCC_except_table2362
+ GCC_except_table2572
+ GCC_except_table2625
+ GCC_except_table2629
+ GCC_except_table2634
+ GCC_except_table2665
+ GCC_except_table2783
+ GCC_except_table2786
+ GCC_except_table2799
+ GCC_except_table2804
+ GCC_except_table2829
+ GCC_except_table3010
+ GCC_except_table3080
+ GCC_except_table3092
+ GCC_except_table3095
+ GCC_except_table3175
+ GCC_except_table3182
+ GCC_except_table3385
+ GCC_except_table3472
+ GCC_except_table3490
+ GCC_except_table3491
+ GCC_except_table3504
+ GCC_except_table3505
+ GCC_except_table3506
+ GCC_except_table3508
+ GCC_except_table3548
+ GCC_except_table3638
+ GCC_except_table3667
+ GCC_except_table3668
+ GCC_except_table3669
+ GCC_except_table3874
+ GCC_except_table3884
+ GCC_except_table3887
+ GCC_except_table3889
+ GCC_except_table3897
+ GCC_except_table4002
+ GCC_except_table4006
+ GCC_except_table4019
+ GCC_except_table4126
+ GCC_except_table4176
+ GCC_except_table4205
+ GCC_except_table4219
+ GCC_except_table4222
+ GCC_except_table4227
+ GCC_except_table4231
+ GCC_except_table4234
+ GCC_except_table4239
+ GCC_except_table4242
+ GCC_except_table4249
+ GCC_except_table4254
+ GCC_except_table4259
+ GCC_except_table4275
+ GCC_except_table4279
+ GCC_except_table4291
+ GCC_except_table4323
+ GCC_except_table659
+ GCC_except_table819
+ GCC_except_table953
+ _BiomeLibraryLibraryCore.frameworkLibrary.20389
+ _BiomeLibraryLibraryCore.frameworkLibrary.3428
+ _ContentKitLibrary.13346
+ _ContentKitLibrary.18979
+ _ContentKitLibraryCore.frameworkLibrary.13349
+ _ContentKitLibraryCore.frameworkLibrary.18990
+ _CoreTextLibraryCore.frameworkLibrary.12282
+ _IconServicesLibrary.16604
+ _IconServicesLibraryCore.frameworkLibrary.16613
+ _LinkPresentationLibraryCore.frameworkLibrary.13330
+ _UIKitLibrary.19501
+ _UIKitLibrary.sLib.12015
+ _UIKitLibrary.sOnce.12008
+ _UIKitLibraryCore.frameworkLibrary.19015
+ _UIKitLibraryCore.frameworkLibrary.19511
+ _VisionKitCoreLibraryCore.frameworkLibrary.14749
+ _WFLogCategoryControlMigration
+ __NSFullMethodName
+ __OBJC_$_INSTANCE_METHODS_VCVoiceShortcutClient(DaemonConfig|MenuBar|Sting|AppIntents|Spotlight|TopHitContextual|VoiceShortcuts|AutoShortcuts|Accessibility|Staccato|Automations|ContextualActions|ShareSheet|Suggestions)
+ ___85-[VCVoiceShortcutClient(Spotlight) triggerFullContextualActionReindexWithCompletion:]_block_invoke
+ ___BiomeLibraryLibraryCore_block_invoke.20390
+ ___BiomeLibraryLibraryCore_block_invoke.3429
+ ___Block_byref_object_copy_.10581
+ ___Block_byref_object_copy_.13171
+ ___Block_byref_object_copy_.14948
+ ___Block_byref_object_copy_.16083
+ ___Block_byref_object_copy_.18999
+ ___Block_byref_object_copy_.20929
+ ___Block_byref_object_copy_.2791
+ ___Block_byref_object_dispose_.10582
+ ___Block_byref_object_dispose_.13172
+ ___Block_byref_object_dispose_.14949
+ ___Block_byref_object_dispose_.16084
+ ___Block_byref_object_dispose_.19000
+ ___Block_byref_object_dispose_.20930
+ ___Block_byref_object_dispose_.2792
+ ___ContentKitLibraryCore_block_invoke.13350
+ ___ContentKitLibraryCore_block_invoke.18991
+ ___CoreTextLibraryCore_block_invoke.12283
+ ___IconServicesLibraryCore_block_invoke.16614
+ ___LinkPresentationLibraryCore_block_invoke.13331
+ ___UIKitLibraryCore_block_invoke.19016
+ ___UIKitLibraryCore_block_invoke.19512
+ ___UIKitLibrary_block_invoke.12013
+ ___VisionKitCoreLibraryCore_block_invoke.14750
+ ___block_literal_global.10604
+ ___block_literal_global.11012
+ ___block_literal_global.11042
+ ___block_literal_global.11659
+ ___block_literal_global.12009
+ ___block_literal_global.12423
+ ___block_literal_global.13432
+ ___block_literal_global.14494
+ ___block_literal_global.14793
+ ___block_literal_global.149.12410
+ ___block_literal_global.14971
+ ___block_literal_global.15329
+ ___block_literal_global.15449
+ ___block_literal_global.155.10575
+ ___block_literal_global.15772
+ ___block_literal_global.16087
+ ___block_literal_global.17534
+ ___block_literal_global.18169
+ ___block_literal_global.18231
+ ___block_literal_global.185.20934
+ ___block_literal_global.19009
+ ___block_literal_global.19059
+ ___block_literal_global.19070
+ ___block_literal_global.19327
+ ___block_literal_global.194.20927
+ ___block_literal_global.19588
+ ___block_literal_global.200.1972
+ ___block_literal_global.20069
+ ___block_literal_global.20257
+ ___block_literal_global.203.10568
+ ___block_literal_global.21080
+ ___block_literal_global.3593
+ ___block_literal_global.4283
+ ___block_literal_global.50.17815
+ ___block_literal_global.62.16088
+ ___block_literal_global.77.15320
+ ___getBiomeLibrarySymbolLoc_block_invoke.20380
+ ___getBiomeLibrarySymbolLoc_block_invoke.3424
+ ___getISImageDescriptorClass_block_invoke.16601
+ ___getLPLinkMetadataClass_block_invoke.13327
+ ___getVKCRemoveBackgroundRequestHandlerClass_block_invoke.14748
+ ___getWFContentItemClass_block_invoke.13324
+ ___getWFContentItemClass_block_invoke.19003
+ ___getWFControlMigrationLogObject_block_invoke
+ ___getWFStringContentItemClass_block_invoke.18978
+ ___getkISImageDescriptorHomeScreenSymbolLoc_block_invoke.16603
+ ___unnamed_13
+ ___unnamed_18
+ ___unnamed_20
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_VoiceShortcutClient
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_VoiceShortcutClient
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O10CodingKeys028_7E07E9B612B0F096B9217137183N3A34LLOSHAASQ
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O10CodingKeys028_7E07E9B612B0F096B9217137183N3A34LLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O10CodingKeys028_7E07E9B612B0F096B9217137183N3A34LLOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O18UseModelCodingKeys028_7E07E9B612B0F096B9217137183P3A34LLOs0K3KeyAAs23CustomStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O18UseModelCodingKeys028_7E07E9B612B0F096B9217137183P3A34LLOs0K3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O22WritingToolsCodingKeys028_7E07E9B612B0F096B9217137183P3A34LLOs0K3KeyAAs23CustomStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O22WritingToolsCodingKeys028_7E07E9B612B0F096B9217137183P3A34LLOs0K3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O24PhotosMemoriesCodingKeys028_7E07E9B612B0F096B9217137183P3A34LLOs0K3KeyAAs23CustomStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O24PhotosMemoriesCodingKeys028_7E07E9B612B0F096B9217137183P3A34LLOs0K3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O25ImagePlaygroundCodingKeys028_7E07E9B612B0F096B9217137183P3A34LLOs0K3KeyAAs23CustomStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O25ImagePlaygroundCodingKeys028_7E07E9B612B0F096B9217137183P3A34LLOs0K3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O34VisualIntelligenceCameraCodingKeys028_7E07E9B612B0F096B9217137183Q3A34LLOs0L3KeyAAs23CustomStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O34VisualIntelligenceCameraCodingKeys028_7E07E9B612B0F096B9217137183Q3A34LLOs0L3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0OSHAASQ
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD10CodingKeys028_7E07E9B612B0F096B9217137183N3A34LLOSHAASQ
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD10CodingKeys028_7E07E9B612B0F096B9217137183N3A34LLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD10CodingKeys028_7E07E9B612B0F096B9217137183N3A34LLOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 19VoiceShortcutClient21XPCRapportEventStreamV0E0V10CodingKeysOSHAASQ
+ _associated conformance 19VoiceShortcutClient21XPCRapportEventStreamV0E0V10CodingKeysOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 19VoiceShortcutClient21XPCRapportEventStreamV0E0V10CodingKeysOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 19VoiceShortcutClient21XPCRapportEventStreamV0E0V21XPCEventDecodingError33_FABCDDD4239CC45AE632E6ED748D6D13LLOSHAASQ
+ _associated conformance 19VoiceShortcutClient21XPCRapportEventStreamVAA08XPCEventF0AA0E0AaDP_AA0G0
+ _audit_stringBiomeLibrary.20394
+ _audit_stringBiomeLibrary.3432
+ _audit_stringContentKit.13353
+ _audit_stringContentKit.18996
+ _audit_stringCoreText.12287
+ _audit_stringIconServices.16617
+ _audit_stringLinkPresentation.13345
+ _audit_stringUIKit.19019
+ _audit_stringUIKit.19515
+ _audit_stringVisionKitCore.14753
+ _block_copy_helper.249
+ _block_copy_helper.253
+ _block_descriptor.251
+ _block_descriptor.255
+ _block_destroy_helper.250
+ _block_destroy_helper.254
+ _getBiomeLibrarySymbolLoc.ptr.20379
+ _getBiomeLibrarySymbolLoc.ptr.3423
+ _getISImageDescriptorClass.softClass.16600
+ _getLPLinkMetadataClass.softClass.13326
+ _getVKCRemoveBackgroundRequestHandlerClass.softClass.14747
+ _getWFContentItemClass.softClass.13323
+ _getWFContentItemClass.softClass.19002
+ _getWFControlMigrationLogObject
+ _getWFControlMigrationLogObject.log
+ _getWFControlMigrationLogObject.onceToken
+ _getWFStringContentItemClass.softClass.18977
+ _getkISImageDescriptorHomeScreenSymbolLoc.ptr.16602
+ _objc_msgSend$bundleWithIdentifier:
+ _objc_msgSend$colorForName:
+ _objc_msgSend$triggerFullContextualActionReindexWithCompletion:
+ _objectdestroy.9Tm
+ _symbolic So28WFAppIntentsMetadataProviderC
+ _symbolic _____ 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O
+ _symbolic _____ 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O10CodingKeys028_7E07E9B612B0F096B9217137183N3A34LLO
+ _symbolic _____ 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O18UseModelCodingKeys028_7E07E9B612B0F096B9217137183P3A34LLO
+ _symbolic _____ 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O22WritingToolsCodingKeys028_7E07E9B612B0F096B9217137183P3A34LLO
+ _symbolic _____ 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O24PhotosMemoriesCodingKeys028_7E07E9B612B0F096B9217137183P3A34LLO
+ _symbolic _____ 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O25ImagePlaygroundCodingKeys028_7E07E9B612B0F096B9217137183P3A34LLO
+ _symbolic _____ 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD0O34VisualIntelligenceCameraCodingKeys028_7E07E9B612B0F096B9217137183Q3A34LLO
+ _symbolic _____ 19VoiceShortcutClient0abC7RequestO7ToolKitO018ActionAvailabilityD10CodingKeys028_7E07E9B612B0F096B9217137183N3A34LLO
+ _symbolic _____ 19VoiceShortcutClient21XPCRapportEventStreamV
+ _symbolic _____ 19VoiceShortcutClient21XPCRapportEventStreamV0E0V
+ _symbolic _____ 19VoiceShortcutClient21XPCRapportEventStreamV0E0V10CodingKeysO
+ _symbolic _____ 19VoiceShortcutClient21XPCRapportEventStreamV0E0V21XPCEventDecodingError33_FABCDDD4239CC45AE632E6ED748D6D13LLO
+ _symbolic _____ 19VoiceShortcutClient35IndividualIdentifiableMetadataCache33_5D7203A1EC670138F68DBD8511AC5F77LLC
+ _symbolic ______pSg s5ErrorP
+ _symbolic _____ySSSDySSSo16LNEntityMetadataCGG s17_NativeDictionaryV
+ _symbolic _____ySSSo16LNEntityMetadataCG s17_NativeDictionaryV
+ _symbolic _____ySo16LNActionMetadataCG 19VoiceShortcutClient35IndividualIdentifiableMetadataCache33_5D7203A1EC670138F68DBD8511AC5F77LLC
+ _symbolic _____ySo16LNEntityMetadataCG 19VoiceShortcutClient35IndividualIdentifiableMetadataCache33_5D7203A1EC670138F68DBD8511AC5F77LLC
+ _symbolic _____y_____G 19VoiceShortcutClient16XPCKeyedDecodingV AA21XPCRapportEventStreamV0G0V10CodingKeysO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG0O10CodingKeys028_7E07E9B612B0F096B9217137183Q3A34LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG0O18UseModelCodingKeys028_7E07E9B612B0F096B9217137183S3A34LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG0O22WritingToolsCodingKeys028_7E07E9B612B0F096B9217137183S3A34LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG0O24PhotosMemoriesCodingKeys028_7E07E9B612B0F096B9217137183S3A34LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG0O25ImagePlaygroundCodingKeys028_7E07E9B612B0F096B9217137183S3A34LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG0O34VisualIntelligenceCameraCodingKeys028_7E07E9B612B0F096B9217137183T3A34LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG10CodingKeys028_7E07E9B612B0F096B9217137183Q3A34LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG0O10CodingKeys028_7E07E9B612B0F096B9217137183Q3A34LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG0O18UseModelCodingKeys028_7E07E9B612B0F096B9217137183S3A34LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG0O22WritingToolsCodingKeys028_7E07E9B612B0F096B9217137183S3A34LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG0O24PhotosMemoriesCodingKeys028_7E07E9B612B0F096B9217137183S3A34LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG0O25ImagePlaygroundCodingKeys028_7E07E9B612B0F096B9217137183S3A34LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG0O34VisualIntelligenceCameraCodingKeys028_7E07E9B612B0F096B9217137183T3A34LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 19VoiceShortcutClient0deF7RequestO7ToolKitO018ActionAvailabilityG10CodingKeys028_7E07E9B612B0F096B9217137183Q3A34LLO
+ _symbolic _____yxG 19VoiceShortcutClient25IdentifiableMetadataCache33_5D7203A1EC670138F68DBD8511AC5F77LLC
+ _timestampDateFormatter.dateFormatter.15450
+ _timestampDateFormatter.onceToken.15448
+ _type_layout_string 19VoiceShortcutClient21XPCRapportEventStreamV0E0V
+ _xpc_dictionary_send_reply
- GCC_except_table1090
- GCC_except_table1116
- GCC_except_table1117
- GCC_except_table1118
- GCC_except_table1127
- GCC_except_table1182
- GCC_except_table1213
- GCC_except_table1252
- GCC_except_table1339
- GCC_except_table1378
- GCC_except_table1391
- GCC_except_table1418
- GCC_except_table1423
- GCC_except_table1429
- GCC_except_table1474
- GCC_except_table1476
- GCC_except_table1479
- GCC_except_table1490
- GCC_except_table1495
- GCC_except_table1560
- GCC_except_table1561
- GCC_except_table1618
- GCC_except_table1694
- GCC_except_table1710
- GCC_except_table1759
- GCC_except_table1780
- GCC_except_table1782
- GCC_except_table1842
- GCC_except_table1844
- GCC_except_table1847
- GCC_except_table1849
- GCC_except_table1858
- GCC_except_table1866
- GCC_except_table1868
- GCC_except_table1889
- GCC_except_table1996
- GCC_except_table2019
- GCC_except_table2056
- GCC_except_table2086
- GCC_except_table2139
- GCC_except_table2150
- GCC_except_table2175
- GCC_except_table2198
- GCC_except_table2203
- GCC_except_table2206
- GCC_except_table2279
- GCC_except_table2344
- GCC_except_table2351
- GCC_except_table2358
- GCC_except_table2568
- GCC_except_table2619
- GCC_except_table2623
- GCC_except_table2628
- GCC_except_table2659
- GCC_except_table2777
- GCC_except_table2780
- GCC_except_table2787
- GCC_except_table2798
- GCC_except_table2817
- GCC_except_table3004
- GCC_except_table3074
- GCC_except_table3086
- GCC_except_table3089
- GCC_except_table3163
- GCC_except_table3170
- GCC_except_table3379
- GCC_except_table3466
- GCC_except_table3484
- GCC_except_table3485
- GCC_except_table3486
- GCC_except_table3487
- GCC_except_table3500
- GCC_except_table3502
- GCC_except_table3542
- GCC_except_table3632
- GCC_except_table3661
- GCC_except_table3662
- GCC_except_table3663
- GCC_except_table3868
- GCC_except_table3875
- GCC_except_table3878
- GCC_except_table3883
- GCC_except_table3891
- GCC_except_table3996
- GCC_except_table4000
- GCC_except_table4013
- GCC_except_table4120
- GCC_except_table4170
- GCC_except_table4199
- GCC_except_table4204
- GCC_except_table4207
- GCC_except_table4221
- GCC_except_table4225
- GCC_except_table4228
- GCC_except_table4230
- GCC_except_table4233
- GCC_except_table4243
- GCC_except_table4248
- GCC_except_table4253
- GCC_except_table4269
- GCC_except_table4273
- GCC_except_table4285
- GCC_except_table4317
- GCC_except_table657
- GCC_except_table817
- GCC_except_table949
- _BiomeLibraryLibraryCore.frameworkLibrary.20336
- _BiomeLibraryLibraryCore.frameworkLibrary.3422
- _ContentKitLibrary.13299
- _ContentKitLibrary.18926
- _ContentKitLibraryCore.frameworkLibrary.13302
- _ContentKitLibraryCore.frameworkLibrary.18937
- _CoreTextLibraryCore.frameworkLibrary.12235
- _IconServicesLibrary.16551
- _IconServicesLibraryCore.frameworkLibrary.16560
- _LinkPresentationLibraryCore.frameworkLibrary.13283
- _UIKitLibrary.19448
- _UIKitLibrary.sLib.12036
- _UIKitLibrary.sOnce.12029
- _UIKitLibraryCore.frameworkLibrary.18962
- _UIKitLibraryCore.frameworkLibrary.19458
- _VisionKitCoreLibraryCore.frameworkLibrary.14702
- __OBJC_$_INSTANCE_METHODS_VCVoiceShortcutClient(DaemonConfig|Spotlight|MenuBar|Sting|AppIntents|TopHitContextual|VoiceShortcuts|AutoShortcuts|Accessibility|Staccato|Automations|ContextualActions|ShareSheet|Suggestions)
- ___BiomeLibraryLibraryCore_block_invoke.20337
- ___BiomeLibraryLibraryCore_block_invoke.3423
- ___Block_byref_object_copy_.10579
- ___Block_byref_object_copy_.13124
- ___Block_byref_object_copy_.14895
- ___Block_byref_object_copy_.16030
- ___Block_byref_object_copy_.18946
- ___Block_byref_object_copy_.20876
- ___Block_byref_object_copy_.2790
- ___Block_byref_object_dispose_.10580
- ___Block_byref_object_dispose_.13125
- ___Block_byref_object_dispose_.14896
- ___Block_byref_object_dispose_.16031
- ___Block_byref_object_dispose_.18947
- ___Block_byref_object_dispose_.20877
- ___Block_byref_object_dispose_.2791
- ___ContentKitLibraryCore_block_invoke.13303
- ___ContentKitLibraryCore_block_invoke.18938
- ___CoreTextLibraryCore_block_invoke.12236
- ___IconServicesLibraryCore_block_invoke.16561
- ___LinkPresentationLibraryCore_block_invoke.13284
- ___UIKitLibraryCore_block_invoke.18963
- ___UIKitLibraryCore_block_invoke.19459
- ___UIKitLibrary_block_invoke.12034
- ___VisionKitCoreLibraryCore_block_invoke.14703
- ___block_literal_global.10602
- ___block_literal_global.11010
- ___block_literal_global.11040
- ___block_literal_global.11657
- ___block_literal_global.12030
- ___block_literal_global.12376
- ___block_literal_global.13385
- ___block_literal_global.14447
- ___block_literal_global.14740
- ___block_literal_global.149.12363
- ___block_literal_global.14918
- ___block_literal_global.15276
- ___block_literal_global.15396
- ___block_literal_global.155.10573
- ___block_literal_global.15719
- ___block_literal_global.16034
- ___block_literal_global.17481
- ___block_literal_global.18116
- ___block_literal_global.18178
- ___block_literal_global.185.20881
- ___block_literal_global.18956
- ___block_literal_global.19006
- ___block_literal_global.19017
- ___block_literal_global.19274
- ___block_literal_global.194.20874
- ___block_literal_global.19535
- ___block_literal_global.200.1974
- ___block_literal_global.20016
- ___block_literal_global.20204
- ___block_literal_global.21027
- ___block_literal_global.3587
- ___block_literal_global.4277
- ___block_literal_global.50.17762
- ___block_literal_global.62.16035
- ___block_literal_global.77.15267
- ___getBiomeLibrarySymbolLoc_block_invoke.20327
- ___getBiomeLibrarySymbolLoc_block_invoke.3418
- ___getISImageDescriptorClass_block_invoke.16548
- ___getLPLinkMetadataClass_block_invoke.13280
- ___getVKCRemoveBackgroundRequestHandlerClass_block_invoke.14701
- ___getWFContentItemClass_block_invoke.13277
- ___getWFContentItemClass_block_invoke.18950
- ___getWFStringContentItemClass_block_invoke.18925
- ___getkISImageDescriptorHomeScreenSymbolLoc_block_invoke.16550
- ___unnamed_16
- _audit_stringBiomeLibrary.20341
- _audit_stringBiomeLibrary.3426
- _audit_stringContentKit.13306
- _audit_stringContentKit.18943
- _audit_stringCoreText.12240
- _audit_stringIconServices.16564
- _audit_stringLinkPresentation.13298
- _audit_stringUIKit.18966
- _audit_stringUIKit.19462
- _audit_stringVisionKitCore.14706
- _block_copy_helper.1
- _block_copy_helper.226
- _block_descriptor.228
- _block_descriptor.3
- _block_destroy_helper.2
- _block_destroy_helper.227
- _getBiomeLibrarySymbolLoc.ptr.20326
- _getBiomeLibrarySymbolLoc.ptr.3417
- _getISImageDescriptorClass.softClass.16547
- _getLPLinkMetadataClass.softClass.13279
- _getVKCRemoveBackgroundRequestHandlerClass.softClass.14700
- _getWFContentItemClass.softClass.13276
- _getWFContentItemClass.softClass.18949
- _getWFStringContentItemClass.softClass.18924
- _getkISImageDescriptorHomeScreenSymbolLoc.ptr.16549
- _objectdestroy.32Tm
- _swift_continuation_resume
- _symbolic SbIeyBy_Sg
- _symbolic SccySb_____G s5NeverO
- _symbolic _____ySo16LNActionMetadataCG 19VoiceShortcutClient25IdentifiableMetadataCache33_5D7203A1EC670138F68DBD8511AC5F77LLC
- _symbolic _____ySo16LNEntityMetadataCG 19VoiceShortcutClient25IdentifiableMetadataCache33_5D7203A1EC670138F68DBD8511AC5F77LLC
- _timestampDateFormatter.dateFormatter.15397
- _timestampDateFormatter.onceToken.15395
CStrings:
+ "%s %@ returned nil"
+ ", reply required: "
+ "-[WFConfiguredSystemWorkflowAction initWithWorkflow:shortcutsMetadata:]"
+ "<Rapport event, name: "
+ "Black"
+ "Brown"
+ "Clear"
+ "ControlMigration"
+ "Failed to load %s for %s in %s from metadata provider due to: %@"
+ "Gray"
+ "Green"
+ "Indigo"
+ "Label"
+ "Loading %s %s from %s"
+ "Mint"
+ "No %s found matching identifier %s from %s"
+ "Not loading %s for identifier %s from %s - cache already present"
+ "Purging cache due to LNMetadataChanged notification"
+ "Purging cache due to Memory Pressure notification"
+ "Purging cache due to cache expiry"
+ "The XPC session could not be created "
+ "White"
+ "Yellow_Accessibility"
+ "actionAvailabilityRequest"
+ "bundleWithIdentifier:"
+ "cacheActivityTransaction"
+ "cacheDebouncerFire"
+ "cacheDebouncerPoke"
+ "colorForName:"
+ "com.apple.WorkflowKit"
+ "com.apple.rapport.matching"
+ "com.apple.shortcuts.appIntentsMetadataProvider.cacheActive"
+ "entityForBundleIdentifier:withEntityIdentifier:error:"
+ "replyRequired"
+ "systemBlueTint"
+ "systemGreenTint"
+ "systemRedTint"
+ "tintedColorForName:"
+ "visualIntelligenceCamera"
- "The XPC session could not be created"
- "Workspace-ForegroundFocal"
- "com.apple.frontboard"
- "v12@?0B8"

```
