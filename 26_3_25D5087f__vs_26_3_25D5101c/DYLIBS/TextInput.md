## TextInput

> `/System/Library/PrivateFrameworks/TextInput.framework/Versions/A/TextInput`

```diff

-3532.3.2.1.0
-  __TEXT.__text: 0x88458
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0xb248
+3532.3.2.2.0
+  __TEXT.__text: 0x8952c
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__objc_methlist: 0xb390
   __TEXT.__dlopen_cstrs: 0x24a
   __TEXT.__const: 0x4e8
-  __TEXT.__cstring: 0x47f91
+  __TEXT.__cstring: 0x47fea
   __TEXT.__ustring: 0xc7b68
   __TEXT.__oslogstring: 0x974
-  __TEXT.__unwind_info: 0x1e50
-  __TEXT.__objc_classname: 0x1584
-  __TEXT.__objc_methname: 0x192aa
-  __TEXT.__objc_methtype: 0x3627
-  __TEXT.__objc_stubs: 0xcd00
-  __DATA_CONST.__got: 0x5c8
+  __TEXT.__unwind_info: 0x1e78
+  __TEXT.__objc_classname: 0x15a0
+  __TEXT.__objc_methname: 0x196a6
+  __TEXT.__objc_methtype: 0x3704
+  __TEXT.__objc_stubs: 0xce00
+  __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__const: 0x1550
-  __DATA_CONST.__objc_classlist: 0x5a8
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5470
+  __DATA_CONST.__objc_selrefs: 0x54f8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x3f8
+  __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0xf5bc8
-  __AUTH_CONST.__auth_got: 0x668
-  __AUTH_CONST.__const: 0x1ec0
-  __AUTH_CONST.__cfstring: 0x24c380
-  __AUTH_CONST.__objc_const: 0x11708
+  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__const: 0x1ef0
+  __AUTH_CONST.__cfstring: 0x24c400
+  __AUTH_CONST.__objc_const: 0x118d8
   __AUTH_CONST.__objc_arrayobj: 0x4380
   __AUTH_CONST.__objc_dictobj: 0xcc38
   __AUTH_CONST.__objc_intobj: 0xca8
   __AUTH_CONST.__objc_doubleobj: 0xc0
-  __AUTH.__objc_data: 0x2490
-  __DATA.__objc_ivar: 0xb54
+  __AUTH.__objc_data: 0x24e0
+  __DATA.__objc_ivar: 0xb68
   __DATA.__data: 0xc30
   __DATA.__bss: 0x730
   __DATA_DIRTY.__objc_data: 0x1400

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/InternationalSupport.framework/Versions/A/InternationalSupport

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B98F444A-9E63-3957-BFA9-C9E8CA83584E
-  Functions: 3942
-  Symbols:   9240
-  CStrings:  106811
+  UUID: 9ADB639A-7199-34B2-834C-9045B2DFFA29
+  Functions: 3969
+  Symbols:   9299
+  CStrings:  106853
 
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
+ OBJC_IVAR_$_TILexiconEntry._focusedSecureLabel
+ OBJC_IVAR_$_TILexiconEntry._slotID
+ OBJC_IVAR_$_TILexiconEntry._unfocusedSecureLabel
+ OBJC_IVAR_$_TIRecentInputsSecureContext._focusedLabelRenderTraits
+ OBJC_IVAR_$_TIRecentInputsSecureContext._unfocusedLabelRenderTraits
+ _CFDataCreateMutable
+ _CGDataProviderCreateWithCFData
+ _CGImageCreateWithPNGDataProvider
+ _CGImageDestinationAddImage
+ _CGImageDestinationCreateWithData
+ _CGImageDestinationFinalize
+ _CGImageRelease
+ _OBJC_CLASS_$_TIRecentInputsSecureContext
+ _OBJC_METACLASS_$_TIRecentInputsSecureContext
+ _UTTypePNG
+ __Block_byref_object_copy_.1011
+ __Block_byref_object_copy_.11778
+ __Block_byref_object_copy_.13273
+ __Block_byref_object_copy_.2112
+ __Block_byref_object_copy_.3097
+ __Block_byref_object_copy_.7301
+ __Block_byref_object_copy_.9217
+ __Block_byref_object_dispose_.1012
+ __Block_byref_object_dispose_.11779
+ __Block_byref_object_dispose_.13274
+ __Block_byref_object_dispose_.2113
+ __Block_byref_object_dispose_.3098
+ __Block_byref_object_dispose_.7302
+ __Block_byref_object_dispose_.9218
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
+ ___block_descriptor_48_8_32s40r_e18_v16?0"NSString"8l
+ __block_literal_global.10048
+ __block_literal_global.10231
+ __block_literal_global.1113
+ __block_literal_global.1180
+ __block_literal_global.12455
+ __block_literal_global.12742
+ __block_literal_global.12801
+ __block_literal_global.13052
+ __block_literal_global.13561
+ __block_literal_global.14014
+ __block_literal_global.171
+ __block_literal_global.176
+ __block_literal_global.2128
+ __block_literal_global.221
+ __block_literal_global.2558
+ __block_literal_global.2752
+ __block_literal_global.32.12734
+ __block_literal_global.38.12728
+ __block_literal_global.4.5074
+ __block_literal_global.4.8916
+ __block_literal_global.4252
+ __block_literal_global.4258
+ __block_literal_global.4537
+ __block_literal_global.5072
+ __block_literal_global.5162
+ __block_literal_global.5212
+ __block_literal_global.5688
+ __block_literal_global.6168
+ __block_literal_global.7.8919
+ __block_literal_global.7.9316
+ __block_literal_global.7036
+ __block_literal_global.7366
+ __block_literal_global.75.1150
+ __block_literal_global.7888
+ __block_literal_global.8030
+ __block_literal_global.8343
+ __block_literal_global.8893
+ __block_literal_global.8912
+ __block_literal_global.9286
+ __block_literal_global.9312
+ __block_literal_global.954
+ __block_literal_global.9878
+ _objc_msgSend$focusedSecureLabel
+ _objc_msgSend$identifierIsSecureSystemIdentifier:
+ _objc_msgSend$recentInputForIdentifier:completionHandler:
+ _objc_msgSend$requestSecureLexiconLabelsForRecentInputIdentifier:context:completionHandler:
+ _objc_msgSend$requestSecureLexiconStringForRecentInputIdentifier:slotID:completionHandler:
+ _objc_msgSend$setFocusedLabelRenderTraits:
+ _objc_msgSend$setUnfocusedLabelRenderTraits:
+ _objc_msgSend$unfocusedSecureLabel
+ generateIdentifier.count.10139
+ sharedInstance.instance.13562
+ sharedInstance.instance.8894
+ sharedInstance.onceToken.13560
+ sharedInstance.onceToken.8029
+ sharedInstance.onceToken.8892
- __Block_byref_object_copy_.11715
- __Block_byref_object_copy_.13207
- __Block_byref_object_copy_.2064
- __Block_byref_object_copy_.3046
- __Block_byref_object_copy_.7237
- __Block_byref_object_copy_.9155
- __Block_byref_object_copy_.979
- __Block_byref_object_dispose_.11716
- __Block_byref_object_dispose_.13208
- __Block_byref_object_dispose_.2065
- __Block_byref_object_dispose_.3047
- __Block_byref_object_dispose_.7238
- __Block_byref_object_dispose_.9156
- __Block_byref_object_dispose_.980
- __block_literal_global.10172
- __block_literal_global.104
- __block_literal_global.1078
- __block_literal_global.109.9988
- __block_literal_global.1142
- __block_literal_global.12390
- __block_literal_global.12676
- __block_literal_global.12735
- __block_literal_global.12986
- __block_literal_global.13495
- __block_literal_global.13948
- __block_literal_global.2080
- __block_literal_global.2509
- __block_literal_global.2703
- __block_literal_global.32.12668
- __block_literal_global.38.12662
- __block_literal_global.4.5011
- __block_literal_global.4.8853
- __block_literal_global.4189
- __block_literal_global.4195
- __block_literal_global.4474
- __block_literal_global.5009
- __block_literal_global.5100
- __block_literal_global.5150
- __block_literal_global.5626
- __block_literal_global.6105
- __block_literal_global.6973
- __block_literal_global.7.8856
- __block_literal_global.7.9254
- __block_literal_global.7302
- __block_literal_global.75.1115
- __block_literal_global.7823
- __block_literal_global.7965
- __block_literal_global.8277
- __block_literal_global.85.2495
- __block_literal_global.8830
- __block_literal_global.8849
- __block_literal_global.9224
- __block_literal_global.9250
- __block_literal_global.929
- __block_literal_global.9816
- __block_literal_global.9985
- generateIdentifier.count.10080
- sharedInstance.instance.13496
- sharedInstance.instance.8831
- sharedInstance.onceToken.13494
- sharedInstance.onceToken.7964
- sharedInstance.onceToken.8829
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
