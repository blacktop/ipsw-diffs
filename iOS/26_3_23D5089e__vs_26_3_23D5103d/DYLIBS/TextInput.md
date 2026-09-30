## TextInput

> `/System/Library/PrivateFrameworks/TextInput.framework/TextInput`

```diff

-3532.3.2.1.0
-  __TEXT.__text: 0x7f22c
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0xb2a0
+3532.3.2.2.0
+  __TEXT.__text: 0x801ec
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__objc_methlist: 0xb3e8
   __TEXT.__dlopen_cstrs: 0x4b9
   __TEXT.__const: 0x4d8
-  __TEXT.__cstring: 0x4801b
+  __TEXT.__cstring: 0x48074
   __TEXT.__ustring: 0xc7b68
   __TEXT.__oslogstring: 0x974
-  __TEXT.__unwind_info: 0x1f08
-  __TEXT.__objc_classname: 0x1587
-  __TEXT.__objc_methname: 0x195ff
-  __TEXT.__objc_methtype: 0x3650
-  __TEXT.__objc_stubs: 0xd0c0
-  __DATA_CONST.__got: 0x5e0
-  __DATA_CONST.__const: 0x23e0
-  __DATA_CONST.__objc_classlist: 0x5a8
+  __TEXT.__unwind_info: 0x1f48
+  __TEXT.__objc_classname: 0x15a3
+  __TEXT.__objc_methname: 0x199fb
+  __TEXT.__objc_methtype: 0x372d
+  __TEXT.__objc_stubs: 0xd1c0
+  __DATA_CONST.__got: 0x5f0
+  __DATA_CONST.__const: 0x2408
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5538
+  __DATA_CONST.__objc_selrefs: 0x55c0
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x3f8
+  __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0xf5bc8
-  __AUTH_CONST.__auth_got: 0x7b0
+  __AUTH_CONST.__auth_got: 0x7e8
   __AUTH_CONST.__const: 0xd60
-  __AUTH_CONST.__cfstring: 0x24c580
-  __AUTH_CONST.__objc_const: 0x11760
+  __AUTH_CONST.__cfstring: 0x24c600
+  __AUTH_CONST.__objc_const: 0x11930
   __AUTH_CONST.__objc_arrayobj: 0x4380
   __AUTH_CONST.__objc_dictobj: 0xcc38
   __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_doubleobj: 0xc0
-  __AUTH.__objc_data: 0x2580
-  __DATA.__objc_ivar: 0xb5c
+  __AUTH.__objc_data: 0x25d0
+  __DATA.__objc_ivar: 0xb70
   __DATA.__data: 0xc30
   __DATA.__bss: 0x768
   __DATA_DIRTY.__objc_data: 0x1310

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1FBD19AF-AF2E-3B98-9CFB-3E6106D70E2D
-  Functions: 3932
-  Symbols:   13103
-  CStrings:  106885
+  UUID: C964E91F-2716-3CAE-B869-CF85FBA277FB
+  Functions: 3959
+  Symbols:   13189
+  CStrings:  106927
 
Symbols:
+ +[TILexiconEntry entryWithFocusedSecureLabel:unfocusedSecureLabel:slotID:]
+ +[TIRecentInputs identifierIsSecureSystemIdentifier:]
+ +[TIRecentInputs requestSecureLexiconLabelsForRecentInputIdentifier:context:completionHandler:]
+ +[TIRecentInputs requestSecureLexiconStringForRecentInputIdentifier:slotID:completionHandler:]
+ +[TIRecentInputs secureInputEntryForIdentifier:slotID:]
+ +[TIRecentInputs secureInputEntryForIdentifier:slotID:completionHandler:]
+ +[TIRecentInputs secureRecentInputForIdentifier:context:]
+ +[TIRecentInputs secureRecentInputForIdentifier:context:completionHandler:]
+ +[TIRecentInputsSecureContext contextWithFocusedTraits:unfocusedTraits:]
+ +[TIRecentInputsSecureContext supportsSecureCoding]
+ -[TILexiconEntry dealloc]
+ -[TILexiconEntry focusedSecureLabel]
+ -[TILexiconEntry setFocusedSecureLabel:]
+ -[TILexiconEntry setUnfocusedSecureLabel:]
+ -[TILexiconEntry slotID]
+ -[TILexiconEntry unfocusedSecureLabel]
+ -[TIRecentInputsSecureContext .cxx_destruct]
+ -[TIRecentInputsSecureContext encodeWithCoder:]
+ -[TIRecentInputsSecureContext focusedLabelRenderTraits]
+ -[TIRecentInputsSecureContext initWithCoder:]
+ -[TIRecentInputsSecureContext setFocusedLabelRenderTraits:]
+ -[TIRecentInputsSecureContext setUnfocusedLabelRenderTraits:]
+ -[TIRecentInputsSecureContext unfocusedLabelRenderTraits]
+ _CFDataCreateMutable
+ _CGDataProviderCreateWithCFData
+ _CGImageCreateWithPNGDataProvider
+ _CGImageDestinationAddImage
+ _CGImageDestinationCreateWithData
+ _CGImageDestinationFinalize
+ _CGImageRelease
+ _InputAnalyticsLibraryCore.12634
+ _InputAnalyticsLibraryCore.frameworkLibrary.12641
+ _OBJC_CLASS_$_TIRecentInputsSecureContext
+ _OBJC_IVAR_$_TILexiconEntry._focusedSecureLabel
+ _OBJC_IVAR_$_TILexiconEntry._slotID
+ _OBJC_IVAR_$_TILexiconEntry._unfocusedSecureLabel
+ _OBJC_IVAR_$_TIRecentInputsSecureContext._focusedLabelRenderTraits
+ _OBJC_IVAR_$_TIRecentInputsSecureContext._unfocusedLabelRenderTraits
+ _OBJC_METACLASS_$_TIRecentInputsSecureContext
+ _SecurityLibrary.12941
+ _SecurityLibraryCore.frameworkLibrary.12952
+ _UTTypePNG
+ __OBJC_$_CLASS_METHODS_TIRecentInputsSecureContext
+ __OBJC_$_CLASS_PROP_LIST_TIRecentInputsSecureContext
+ __OBJC_$_INSTANCE_METHODS_TIRecentInputsSecureContext
+ __OBJC_$_INSTANCE_VARIABLES_TIRecentInputsSecureContext
+ __OBJC_$_PROP_LIST_TIRecentInputsSecureContext
+ __OBJC_CLASS_PROTOCOLS_$_TIRecentInputsSecureContext
+ __OBJC_CLASS_RO_$_TIRecentInputsSecureContext
+ __OBJC_METACLASS_RO_$_TIRecentInputsSecureContext
+ ___55+[TIRecentInputs secureInputEntryForIdentifier:slotID:]_block_invoke
+ ___57+[TIRecentInputs secureRecentInputForIdentifier:context:]_block_invoke
+ ___94+[TIRecentInputs requestSecureLexiconStringForRecentInputIdentifier:slotID:completionHandler:]_block_invoke
+ ___95+[TIRecentInputs requestSecureLexiconLabelsForRecentInputIdentifier:context:completionHandler:]_block_invoke
+ ___Block_byref_object_copy_.11625
+ ___Block_byref_object_copy_.13144
+ ___Block_byref_object_copy_.2034
+ ___Block_byref_object_copy_.3022
+ ___Block_byref_object_copy_.7205
+ ___Block_byref_object_copy_.9063
+ ___Block_byref_object_copy_.993
+ ___Block_byref_object_dispose_.11626
+ ___Block_byref_object_dispose_.13145
+ ___Block_byref_object_dispose_.2035
+ ___Block_byref_object_dispose_.3023
+ ___Block_byref_object_dispose_.7206
+ ___Block_byref_object_dispose_.9064
+ ___Block_byref_object_dispose_.994
+ ___InputAnalyticsLibraryCore_block_invoke.12642
+ ___SecurityLibraryCore_block_invoke.12953
+ ___block_descriptor_48_8_32s40r_e18_v16?0"NSString"8lr40l8s32l8
+ ___block_literal_global.10058
+ ___block_literal_global.1087
+ ___block_literal_global.1154
+ ___block_literal_global.12306
+ ___block_literal_global.12583
+ ___block_literal_global.12646
+ ___block_literal_global.12894
+ ___block_literal_global.13438
+ ___block_literal_global.13899
+ ___block_literal_global.169
+ ___block_literal_global.174
+ ___block_literal_global.2050
+ ___block_literal_global.219
+ ___block_literal_global.22.12935
+ ___block_literal_global.24.5078
+ ___block_literal_global.2477
+ ___block_literal_global.2672
+ ___block_literal_global.4.4989
+ ___block_literal_global.4.8762
+ ___block_literal_global.4157
+ ___block_literal_global.4164
+ ___block_literal_global.4453
+ ___block_literal_global.4987
+ ___block_literal_global.5080
+ ___block_literal_global.5125
+ ___block_literal_global.5600
+ ___block_literal_global.6081
+ ___block_literal_global.6946
+ ___block_literal_global.7.8765
+ ___block_literal_global.7.9157
+ ___block_literal_global.7267
+ ___block_literal_global.75.1124
+ ___block_literal_global.7737
+ ___block_literal_global.7883
+ ___block_literal_global.8187
+ ___block_literal_global.8739
+ ___block_literal_global.8758
+ ___block_literal_global.9129
+ ___block_literal_global.9153
+ ___block_literal_global.935
+ ___block_literal_global.9722
+ ___block_literal_global.9878
+ ___getSecTaskCopySigningIdentifierSymbolLoc_block_invoke.12947
+ ___getSecTaskCreateFromSelfSymbolLoc_block_invoke.12943
+ _audit_stringInputAnalytics.12644
+ _audit_stringSecurity.12955
+ _generateIdentifier.count.9970
+ _getSecTaskCopySigningIdentifierSymbolLoc.ptr.12946
+ _getSecTaskCreateFromSelfSymbolLoc.ptr.12942
+ _objc_msgSend$focusedSecureLabel
+ _objc_msgSend$identifierIsSecureSystemIdentifier:
+ _objc_msgSend$recentInputForIdentifier:completionHandler:
+ _objc_msgSend$requestSecureLexiconLabelsForRecentInputIdentifier:context:completionHandler:
+ _objc_msgSend$requestSecureLexiconStringForRecentInputIdentifier:slotID:completionHandler:
+ _objc_msgSend$setFocusedLabelRenderTraits:
+ _objc_msgSend$setUnfocusedLabelRenderTraits:
+ _objc_msgSend$unfocusedSecureLabel
+ _sharedInstance.instance.13439
+ _sharedInstance.instance.8740
+ _sharedInstance.onceToken.13437
+ _sharedInstance.onceToken.7882
+ _sharedInstance.onceToken.8738
- _InputAnalyticsLibraryCore.12556
- _InputAnalyticsLibraryCore.frameworkLibrary.12563
- _SecurityLibrary.12859
- _SecurityLibraryCore.frameworkLibrary.12870
- ___Block_byref_object_copy_.11547
- ___Block_byref_object_copy_.13062
- ___Block_byref_object_copy_.1988
- ___Block_byref_object_copy_.2972
- ___Block_byref_object_copy_.7145
- ___Block_byref_object_copy_.9003
- ___Block_byref_object_copy_.963
- ___Block_byref_object_dispose_.11548
- ___Block_byref_object_dispose_.13063
- ___Block_byref_object_dispose_.1989
- ___Block_byref_object_dispose_.2973
- ___Block_byref_object_dispose_.7146
- ___Block_byref_object_dispose_.9004
- ___Block_byref_object_dispose_.964
- ___InputAnalyticsLibraryCore_block_invoke.12564
- ___SecurityLibraryCore_block_invoke.12871
- ___block_literal_global.104
- ___block_literal_global.1065
- ___block_literal_global.109
- ___block_literal_global.1129
- ___block_literal_global.12228
- ___block_literal_global.12505
- ___block_literal_global.12568
- ___block_literal_global.12812
- ___block_literal_global.13356
- ___block_literal_global.13816
- ___block_literal_global.2004
- ___block_literal_global.22.12853
- ___block_literal_global.24.5018
- ___block_literal_global.2430
- ___block_literal_global.2625
- ___block_literal_global.4.4928
- ___block_literal_global.4.8703
- ___block_literal_global.4099
- ___block_literal_global.4106
- ___block_literal_global.4394
- ___block_literal_global.4926
- ___block_literal_global.5020
- ___block_literal_global.5065
- ___block_literal_global.5541
- ___block_literal_global.6021
- ___block_literal_global.6886
- ___block_literal_global.7.8706
- ___block_literal_global.7.9096
- ___block_literal_global.7207
- ___block_literal_global.75.1102
- ___block_literal_global.7677
- ___block_literal_global.7823
- ___block_literal_global.8126
- ___block_literal_global.85.2416
- ___block_literal_global.8680
- ___block_literal_global.8699
- ___block_literal_global.9069
- ___block_literal_global.9092
- ___block_literal_global.911
- ___block_literal_global.9661
- ___block_literal_global.9817
- ___block_literal_global.9999
- ___getSecTaskCopySigningIdentifierSymbolLoc_block_invoke.12865
- ___getSecTaskCreateFromSelfSymbolLoc_block_invoke.12861
- _audit_stringInputAnalytics.12566
- _audit_stringSecurity.12873
- _generateIdentifier.count.9911
- _getSecTaskCopySigningIdentifierSymbolLoc.ptr.12864
- _getSecTaskCreateFromSelfSymbolLoc.ptr.12860
- _sharedInstance.instance.13357
- _sharedInstance.instance.8681
- _sharedInstance.onceToken.13355
- _sharedInstance.onceToken.7822
- _sharedInstance.onceToken.8679
CStrings:
+ "@36@0:8^{CGImage=}16^{CGImage=}24I32"
+ "T@\"TIKeyboardSecureCandidateRenderTraits\",&,N,V_focusedLabelRenderTraits"
+ "T@\"TIKeyboardSecureCandidateRenderTraits\",&,N,V_unfocusedLabelRenderTraits"
+ "TI,R,N,V_slotID"
+ "TIRecentInputsSecureContext"
+ "T^{CGImage=},R,N,V_focusedSecureLabel"
+ "T^{CGImage=},R,N,V_unfocusedSecureLabel"
+ "^{CGImage=}"
+ "^{CGImage=}16@0:8"
+ "_focusedLabelRenderTraits"
+ "_focusedSecureLabel"
+ "_unfocusedLabelRenderTraits"
+ "_unfocusedSecureLabel"
+ "contextWithFocusedTraits:unfocusedTraits:"
+ "entryWithFocusedSecureLabel:unfocusedSecureLabel:slotID:"
+ "focusedLabelRenderTraits"
+ "focusedSecureLabel"
+ "focusedTraits"
+ "identifierIsSecureSystemIdentifier:"
+ "requestSecureLexiconLabelsForRecentInputIdentifier:context:completionHandler:"
+ "requestSecureLexiconStringForRecentInputIdentifier:slotID:completionHandler:"
+ "secureInputEntryForIdentifier:slotID:"
+ "secureInputEntryForIdentifier:slotID:completionHandler:"
+ "secureRecentInputForIdentifier:context:"
+ "secureRecentInputForIdentifier:context:completionHandler:"
+ "setFocusedLabelRenderTraits:"
+ "setFocusedSecureLabel:"
+ "setUnfocusedLabelRenderTraits:"
+ "setUnfocusedSecureLabel:"
+ "unfocusedLabelRenderTraits"
+ "unfocusedSecureLabel"
+ "unfocusedTraits"
+ "v16@?0@\"NSString\"8"
+ "v24@0:8^{CGImage=}16"
+ "v40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?@\"NSString\">32"
+ "v40@0:8@\"NSString\"16@\"TIRecentInputsSecureContext\"24@?<v@?@\"TIRecentInputs\">32"

```
