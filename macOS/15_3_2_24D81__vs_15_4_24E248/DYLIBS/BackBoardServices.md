## BackBoardServices

> `/System/Library/PrivateFrameworks/BackBoardServices.framework/Versions/A/BackBoardServices`

```diff

-668.4.1.0.0
-  __TEXT.__text: 0x419d0
+668.5.29.0.0
+  __TEXT.__text: 0x4296c
   __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x3988
+  __TEXT.__objc_methlist: 0x3e24
   __TEXT.__const: 0xac
   __TEXT.__gcc_except_tab: 0x100
-  __TEXT.__cstring: 0x6482
+  __TEXT.__cstring: 0x65b6
   __TEXT.__oslogstring: 0x75b
   __TEXT.__ustring: 0x14
   __TEXT.__dlopen_cstrs: 0x96
-  __TEXT.__unwind_info: 0xe68
-  __TEXT.__objc_classname: 0xcc2
-  __TEXT.__objc_methname: 0x640e
-  __TEXT.__objc_methtype: 0xe17
-  __TEXT.__objc_stubs: 0x33e0
-  __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0x570
+  __TEXT.__unwind_info: 0xe80
+  __TEXT.__objc_classname: 0xcc4
+  __TEXT.__objc_methname: 0x662c
+  __TEXT.__objc_methtype: 0xebf
+  __TEXT.__objc_stubs: 0x3520
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x5d8
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14c8
+  __DATA_CONST.__objc_selrefs: 0x15c0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x378
-  __AUTH_CONST.__const: 0xf10
-  __AUTH_CONST.__cfstring: 0x5f20
-  __AUTH_CONST.__objc_const: 0x8700
+  __AUTH_CONST.__const: 0xfc0
+  __AUTH_CONST.__cfstring: 0x6060
+  __AUTH_CONST.__objc_const: 0x8098
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x1540
-  __DATA.__objc_ivar: 0x3d8
+  __DATA.__objc_ivar: 0x3dc
   __DATA.__data: 0x7e0
   __DATA.__bss: 0x408
   __DATA_DIRTY.__objc_data: 0x550

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 33FC89DA-740C-306C-AC64-81BFE4268657
-  Functions: 1459
-  Symbols:   3355
-  CStrings:  3189
+  UUID: 908455E1-650A-3990-8991-C0083D31336C
+  Functions: 1473
+  Symbols:   3396
+  CStrings:  3233
 
Symbols:
+ +[BKSHIDEventDescriptor appendDescriptorArray:toDescriptionStream:]
+ +[BKSHIDEventKeyCommand _appendDescriptionOfKeyCommandCollection:toStream:]
+ -[BKSHIDEventBiometricDescriptor appendDescriptionToStream:]
+ -[BKSHIDEventDeliveryManager resolutionDescriptionForEventDescriptor:sender:]
+ -[BKSHIDEventDeliveryManager resolutionDescriptionForKeyCommand:sender:]
+ -[BKSHIDEventDeliveryRuleChangeTransaction appendDescriptionToStream:]
+ -[BKSHIDEventDeliveryRuleWrapper appendDescriptionToStream:]
+ -[BKSHIDEventDescriptor appendDescriptionToStream:]
+ -[BKSHIDEventDescriptor compare:]
+ -[BKSHIDEventDiscreteDispatchingPredicate appendDescriptionToStream:]
+ -[BKSHIDEventGenericGestureDescriptor appendDescriptionToStream:]
+ -[BKSHIDEventKeyCommandsRegistration appendDescriptionToStream:]
+ -[BKSHIDEventSenderSpecificDescriptor appendDescriptionToStream:]
+ -[BKSHIDEventUsagePairDescriptor appendDescriptionToStream:]
+ -[BKSHIDEventUsagePairDescriptor compare:]
+ -[BKSHIDKeyboardDevice platformInputModeConfiguration]
+ -[BKSHIDKeyboardDeviceProperties platformInputModeConfiguration]
+ -[BKSMutableHIDKeyboardDeviceProperties setPlatformInputModeConfiguration:]
+ -[_BKSHIDKeyboardDeviceClientProxy platformInputModeConfiguration]
+ GCC_except_table1364
+ GCC_except_table1373
+ GCC_except_table861
+ GCC_except_table868
+ OBJC_IVAR_$_BKSHIDKeyboardDeviceProperties._platformInputModeConfiguration
+ QuartzCoreLibraryCore.frameworkLibrary.5905
+ _BKSHIDEventUsagePairDescriptorOmitNameStyleKey
+ __45-[BKSHIDKeyboardService _initWithConnection:]_block_invoke.133
+ __45-[BKSHIDKeyboardService _initWithConnection:]_block_invoke.148
+ __55-[BKSHIDEventDeliveryManager _initWithRemoteConnection]_block_invoke.77
+ __62-[BKSMutableHIDEventDiscreteDispatchingPredicate setDisplays:]_block_invoke.150
+ __75+[BKSHIDEventKeyCommand _appendDescriptionOfKeyCommandCollection:toStream:]_block_invoke.67
+ __QuartzCoreLibraryCore_block_invoke.5906
+ ___60-[BKSHIDEventDeliveryRuleWrapper appendDescriptionToStream:]_block_invoke
+ ___60-[BKSHIDEventUsagePairDescriptor appendDescriptionToStream:]_block_invoke
+ ___64-[BKSHIDEventKeyCommandsRegistration appendDescriptionToStream:]_block_invoke
+ ___67+[BKSHIDEventDescriptor appendDescriptorArray:toDescriptionStream:]_block_invoke
+ ___67+[BKSHIDEventDescriptor appendDescriptorArray:toDescriptionStream:]_block_invoke_2
+ ___67+[BKSHIDEventDescriptor appendDescriptorArray:toDescriptionStream:]_block_invoke_3
+ ___67+[BKSHIDEventDescriptor appendDescriptorArray:toDescriptionStream:]_block_invoke_4
+ ___67+[BKSHIDEventDescriptor appendDescriptorArray:toDescriptionStream:]_block_invoke_5
+ ___69-[BKSHIDEventDiscreteDispatchingPredicate appendDescriptionToStream:]_block_invoke
+ ___70-[BKSHIDEventDeliveryRuleChangeTransaction appendDescriptionToStream:]_block_invoke
+ ___70-[BKSHIDEventDeliveryRuleChangeTransaction appendDescriptionToStream:]_block_invoke_2
+ ___70-[BKSHIDEventDeliveryRuleChangeTransaction appendDescriptionToStream:]_block_invoke_3
+ ___70-[BKSHIDEventDeliveryRuleChangeTransaction appendDescriptionToStream:]_block_invoke_4
+ ___70-[BKSHIDEventDeliveryRuleChangeTransaction appendDescriptionToStream:]_block_invoke_5
+ ___70-[BKSHIDEventDeliveryRuleChangeTransaction appendDescriptionToStream:]_block_invoke_6
+ ___75+[BKSHIDEventKeyCommand _appendDescriptionOfKeyCommandCollection:toStream:]_block_invoke
+ ___75+[BKSHIDEventKeyCommand _appendDescriptionOfKeyCommandCollection:toStream:]_block_invoke_2
+ ___75+[BKSHIDEventKeyCommand _appendDescriptionOfKeyCommandCollection:toStream:]_block_invoke_3
+ ___75+[BKSHIDEventKeyCommand _appendDescriptionOfKeyCommandCollection:toStream:]_block_invoke_4
+ ___75+[BKSHIDEventKeyCommand _appendDescriptionOfKeyCommandCollection:toStream:]_block_invoke_5
+ ___75+[BKSHIDEventKeyCommand _appendDescriptionOfKeyCommandCollection:toStream:]_block_invoke_6
+ ___block_descriptor_32_e34_16?0"BKSHIDEventDeferringRule"8l
+ ___block_descriptor_32_e44_"<NSCopying>"16?0"BKSHIDEventDescriptor"8l
+ ___block_descriptor_32_e44_16?0"BKSHIDEventDiscreteDispatchingRoot"8l
+ ___block_descriptor_40_e8_32s_e34_v32?0"NSNumber"8"NSArray"16^B24l
+ __block_literal_global.107
+ __block_literal_global.1272
+ __block_literal_global.146
+ __block_literal_global.157
+ __block_literal_global.16.4108
+ __block_literal_global.162
+ __block_literal_global.165
+ __block_literal_global.171
+ __block_literal_global.178
+ __block_literal_global.1795
+ __block_literal_global.18.5613
+ __block_literal_global.182
+ __block_literal_global.2120
+ __block_literal_global.22.4610
+ __block_literal_global.23
+ __block_literal_global.2324
+ __block_literal_global.2707
+ __block_literal_global.3057
+ __block_literal_global.31.5596
+ __block_literal_global.3424
+ __block_literal_global.3741
+ __block_literal_global.4016
+ __block_literal_global.4099
+ __block_literal_global.4286
+ __block_literal_global.4433
+ __block_literal_global.4629
+ __block_literal_global.4795
+ __block_literal_global.5067
+ __block_literal_global.5268
+ __block_literal_global.5428
+ __block_literal_global.5615
+ __block_literal_global.6182
+ __block_literal_global.6415
+ __block_literal_global.855
+ __block_literal_global.955
+ _objc_msgSend$_appendDescriptionOfKeyCommandCollection:toStream:
+ _objc_msgSend$appendDescriptionToStream:
+ _objc_msgSend$appendDescriptorArray:toDescriptionStream:
+ _objc_msgSend$collectionLineBreakNoneStyle
+ _objc_msgSend$hasSuccinctStyle
+ _objc_msgSend$platformInputModeConfiguration
+ _objc_msgSend$reason
+ _objc_msgSend$resolutionDescriptionForEventDescriptor:senderDescriptor:
+ _objc_msgSend$resolutionDescriptionForKeyCommand:senderDescriptor:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$succinctStyle
+ audit_stringQuartzCore.5921
+ protobufSchema.onceToken.1270
+ protobufSchema.onceToken.2118
+ protobufSchema.onceToken.3738
+ protobufSchema.onceToken.5593
+ protobufSchema.onceToken.6173
+ protobufSchema.onceToken.953
+ protobufSchema.schema.1271
+ protobufSchema.schema.2119
+ protobufSchema.schema.3739
+ protobufSchema.schema.5594
+ protobufSchema.schema.6174
+ protobufSchema.schema.954
+ sharedInstance.onceToken.1816
+ sharedInstance.onceToken.6403
- -[BKSHIDEventBiometricDescriptor appendDescriptionToFormatter:]
- -[BKSHIDEventDeliveryRuleChangeTransaction appendDescriptionToFormatter:]
- -[BKSHIDEventDeliveryRuleWrapper appendDescriptionToFormatter:]
- -[BKSHIDEventDescriptor appendDescriptionToFormatter:]
- -[BKSHIDEventDiscreteDispatchingPredicate appendDescriptionToFormatter:]
- -[BKSHIDEventGenericGestureDescriptor appendDescriptionToFormatter:]
- -[BKSHIDEventKeyCommandsRegistration descriptionBuilderWithMultilinePrefix:]
- -[BKSHIDEventKeyCommandsRegistration descriptionWithMultilinePrefix:]
- -[BKSHIDEventKeyCommandsRegistration succinctDescriptionBuilder]
- -[BKSHIDEventSenderSpecificDescriptor appendDescriptionToFormatter:]
- -[BKSHIDEventUsagePairDescriptor appendDescriptionToFormatter:]
- GCC_except_table1344
- GCC_except_table1353
- GCC_except_table853
- GCC_except_table860
- QuartzCoreLibraryCore.frameworkLibrary.5815
- __45-[BKSHIDKeyboardService _initWithConnection:]_block_invoke.129
- __45-[BKSHIDKeyboardService _initWithConnection:]_block_invoke.144
- __55-[BKSHIDEventDeliveryManager _initWithRemoteConnection]_block_invoke.72
- __61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke.67
- __62-[BKSMutableHIDEventDiscreteDispatchingPredicate setDisplays:]_block_invoke.151
- __QuartzCoreLibraryCore_block_invoke.5816
- ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke
- ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke_2
- ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke_3
- ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke_4
- ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke_5
- ___61+[BKSHIDEventKeyCommand _descriptionForKeyCommandCollection:]_block_invoke_6
- ___63-[BKSHIDEventDeliveryRuleWrapper appendDescriptionToFormatter:]_block_invoke
- ___73-[BKSHIDEventDeliveryRuleChangeTransaction appendDescriptionToFormatter:]_block_invoke
- __block_literal_global.102
- __block_literal_global.1269
- __block_literal_global.147
- __block_literal_global.154
- __block_literal_global.16.4049
- __block_literal_global.163
- __block_literal_global.169
- __block_literal_global.173
- __block_literal_global.174
- __block_literal_global.18.5524
- __block_literal_global.1832
- __block_literal_global.2149
- __block_literal_global.22.4529
- __block_literal_global.2353
- __block_literal_global.3055
- __block_literal_global.31.5507
- __block_literal_global.3380
- __block_literal_global.3693
- __block_literal_global.3956
- __block_literal_global.4040
- __block_literal_global.4207
- __block_literal_global.4353
- __block_literal_global.4548
- __block_literal_global.4710
- __block_literal_global.4983
- __block_literal_global.5340
- __block_literal_global.5526
- __block_literal_global.6097
- __block_literal_global.6328
- __block_literal_global.841
- __block_literal_global.951
- _objc_msgSend$debugDescription
- audit_stringQuartzCore.5831
- protobufSchema.onceToken.1267
- protobufSchema.onceToken.2147
- protobufSchema.onceToken.3690
- protobufSchema.onceToken.5504
- protobufSchema.onceToken.6087
- protobufSchema.onceToken.949
- protobufSchema.schema.1268
- protobufSchema.schema.2148
- protobufSchema.schema.3691
- protobufSchema.schema.5505
- protobufSchema.schema.6088
- protobufSchema.schema.950
- sharedInstance.onceToken.1853
- sharedInstance.onceToken.6315
CStrings:
+ "(%X, %X)"
+ "(%X, *)"
+ "(*)"
+ "@\"<NSCopying>\"16@?0@\"BKSHIDEventDescriptor\"8"
+ "@\"NSData\"16@0:8"
+ "@\"NSString\"32@0:8@\"BKSHIDEventDescriptor\"16@\"BKSHIDEventSenderDescriptor\"24"
+ "@\"NSString\"32@0:8@\"BKSHIDEventKeyCommand\"16@\"BKSHIDEventSenderDescriptor\"24"
+ "@16@?0@\"BKSHIDEventDeferringRule\"8"
+ "@16@?0@\"BKSHIDEventDiscreteDispatchingRoot\"8"
+ "Biometric"
+ "GenericGesture"
+ "OmitName"
+ "T@\"NSData\",C,D,N"
+ "T@\"NSData\",R,C,D,N"
+ "T@\"NSData\",R,C,N"
+ "VendorDefined"
+ "_appendDescriptionOfKeyCommandCollection:toStream:"
+ "_platformInputModeConfiguration"
+ "appendDescriptorArray:toDescriptionStream:"
+ "backboardd-attr-cache-17000013"
+ "collectionLineBreakNoneStyle"
+ "compare:"
+ "eventDescriptor"
+ "hasSuccinctStyle"
+ "platformInputModeConfiguration"
+ "resolutionDescriptionForEventDescriptor:sender:"
+ "resolutionDescriptionForEventDescriptor:senderDescriptor:"
+ "resolutionDescriptionForKeyCommand:sender:"
+ "resolutionDescriptionForKeyCommand:senderDescriptor:"
+ "setPlatformInputModeConfiguration:"
+ "sortedArrayUsingSelector:"
+ "succinctStyle"
+ "v32@?0@\"NSNumber\"8@\"NSArray\"16^B24"
- "backboardd-attr-cache-16000026"

```
