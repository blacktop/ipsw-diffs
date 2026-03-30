## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-1224.102.3.0.0
-  __TEXT.__text: 0x704e24
-  __TEXT.__auth_stubs: 0x5f30
-  __TEXT.__objc_methlist: 0x6d34
-  __TEXT.__const: 0x35c90
-  __TEXT.__oslogstring: 0xf0bc
-  __TEXT.__cstring: 0x15a41
-  __TEXT.__gcc_except_tab: 0x1590
-  __TEXT.__constg_swiftt: 0xdc7c
-  __TEXT.__swift5_typeref: 0xacd9
-  __TEXT.__swift5_builtin: 0x2d0
-  __TEXT.__swift5_reflstr: 0xb302
-  __TEXT.__swift5_fieldmd: 0xc6f8
-  __TEXT.__swift5_assocty: 0x1ef8
-  __TEXT.__swift5_proto: 0x20e8
-  __TEXT.__swift5_types: 0xbd4
-  __TEXT.__swift_as_entry: 0x10c0
-  __TEXT.__swift_as_ret: 0x13f8
-  __TEXT.__swift5_capture: 0x2af8
-  __TEXT.__swift5_protos: 0x13c
-  __TEXT.__swift5_mpenum: 0xd0
-  __TEXT.__unwind_info: 0x14e98
-  __TEXT.__eh_frame: 0x3a1a4
-  __TEXT.__objc_classname: 0x3e31
-  __TEXT.__objc_methname: 0x138e6
-  __TEXT.__objc_methtype: 0x44ce
-  __TEXT.__objc_stubs: 0xf9c0
-  __DATA_CONST.__got: 0x21f0
-  __DATA_CONST.__const: 0xaa8
-  __DATA_CONST.__objc_classlist: 0xb78
+1224.120.85.502.1
+  __TEXT.__text: 0x729eec
+  __TEXT.__auth_stubs: 0x61b0
+  __TEXT.__objc_methlist: 0x6ce4
+  __TEXT.__const: 0x361f8
+  __TEXT.__oslogstring: 0xf4cc
+  __TEXT.__cstring: 0x15a51
+  __TEXT.__gcc_except_tab: 0x1788
+  __TEXT.__constg_swiftt: 0xde14
+  __TEXT.__swift5_typeref: 0xafc5
+  __TEXT.__swift5_builtin: 0x2f8
+  __TEXT.__swift5_reflstr: 0xba22
+  __TEXT.__swift5_fieldmd: 0xcbf8
+  __TEXT.__swift5_assocty: 0x2018
+  __TEXT.__swift5_proto: 0x2180
+  __TEXT.__swift5_types: 0xc00
+  __TEXT.__swift_as_entry: 0x10f8
+  __TEXT.__swift_as_ret: 0x145c
+  __TEXT.__swift5_capture: 0x2a90
+  __TEXT.__swift5_protos: 0x144
+  __TEXT.__swift5_mpenum: 0xd8
+  __TEXT.__unwind_info: 0x15248
+  __TEXT.__eh_frame: 0x3ac38
+  __TEXT.__objc_classname: 0x3ee1
+  __TEXT.__objc_methname: 0x13ae6
+  __TEXT.__objc_methtype: 0x446e
+  __TEXT.__objc_stubs: 0xfb60
+  __DATA_CONST.__got: 0x2268
+  __DATA_CONST.__const: 0xb08
+  __DATA_CONST.__objc_classlist: 0xb88
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b48
+  __DATA_CONST.__objc_selrefs: 0x4b90
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0x318
+  __DATA_CONST.__objc_superrefs: 0x330
   __DATA_CONST.__objc_arraydata: 0x488
-  __AUTH_CONST.__auth_got: 0x2fb0
-  __AUTH_CONST.__const: 0x15378
-  __AUTH_CONST.__cfstring: 0x5b20
-  __AUTH_CONST.__objc_const: 0x1a158
+  __AUTH_CONST.__auth_got: 0x30f0
+  __AUTH_CONST.__const: 0x15c30
+  __AUTH_CONST.__cfstring: 0x5620
+  __AUTH_CONST.__objc_const: 0x1a440
   __AUTH_CONST.__objc_intobj: 0xcc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x210
-  __AUTH.__objc_data: 0x7738
-  __AUTH.__data: 0x151c0
-  __DATA.__objc_ivar: 0x7ac
-  __DATA.__data: 0xca68
-  __DATA.__bss: 0x39e70
-  __DATA.__common: 0x14e0
+  __AUTH.__objc_data: 0x77b8
+  __AUTH.__data: 0x14ef8
+  __DATA.__objc_ivar: 0x7bc
+  __DATA.__data: 0xcd20
+  __DATA.__bss: 0x3ada0
+  __DATA.__common: 0x1550
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5F410AF8-46DD-3243-8DB4-E09E6B20FA49
-  Functions: 21836
-  Symbols:   15530
-  CStrings:  9124
+  UUID: DDCBC871-88C8-3990-A1A0-E19F8811BA1E
+  Functions: 22034
+  Symbols:   15766
+  CStrings:  9154
 
Symbols:
+ +[MKHPMInterface create]
+ +[MKIOIterator forServicesMatching:]
+ +[MKIOIterator forServicesMatching:].cold.1
+ +[MKIOIterator forServicesMatching:].cold.2
+ +[MKIOObject forServiceMatching:]
+ +[MKIOObject forServiceMatching:].cold.1
+ +[MKIOObject forServiceMatching:].cold.2
+ +[MKUSBDeviceController create]
+ -[MKHPMInterface .cxx_destruct]
+ -[MKHPMInterface _allowDefaultModeWithError:]
+ -[MKHPMInterface _allowDefaultModeWithError:].cold.1
+ -[MKHPMInterface _forceDeviceModeWithError:]
+ -[MKHPMInterface _forceDeviceModeWithError:].cold.1
+ -[MKHPMInterface _forceDeviceModeWithError:].cold.2
+ -[MKHPMInterface _forceDeviceModeWithError:].cold.3
+ -[MKHPMInterface allowDefaultModeWithError:]
+ -[MKHPMInterface dealloc]
+ -[MKHPMInterface forceDeviceModeWithCompletion:]
+ -[MKHPMInterface initInternal]
+ -[MKHPMInterface initInternal].cold.1
+ -[MKHPMInterface initInternal].cold.2
+ -[MKHPMInterface initInternal].cold.3
+ -[MKIOIterator dealloc]
+ -[MKIOIterator initWithIterator:]
+ -[MKIOIterator next]
+ -[MKIOObject children]
+ -[MKIOObject children].cold.1
+ -[MKIOObject className]
+ -[MKIOObject className].cold.1
+ -[MKIOObject dealloc]
+ -[MKIOObject firstDescendantOfClass:]
+ -[MKIOObject initWithObject:]
+ -[MKIOObject initWithUnownedObject:]
+ -[MKIOObject initWithUnownedObject:].cold.1
+ -[MKIOObject name]
+ -[MKIOObject name].cold.1
+ -[MKIOObject object]
+ -[MKIOObject propertyForKey:]
+ -[MKMessage isFailed]
+ -[MKMessage setIsFailed:]
+ -[MKUSBDeviceController .cxx_destruct]
+ -[MKUSBDeviceController _configureNCMWithError:]
+ -[MKUSBDeviceController _configureNCMWithError:].cold.1
+ -[MKUSBDeviceController _configureNCMWithError:].cold.10
+ -[MKUSBDeviceController _configureNCMWithError:].cold.11
+ -[MKUSBDeviceController _configureNCMWithError:].cold.2
+ -[MKUSBDeviceController _configureNCMWithError:].cold.3
+ -[MKUSBDeviceController _configureNCMWithError:].cold.4
+ -[MKUSBDeviceController _configureNCMWithError:].cold.5
+ -[MKUSBDeviceController _configureNCMWithError:].cold.6
+ -[MKUSBDeviceController _configureNCMWithError:].cold.7
+ -[MKUSBDeviceController _configureNCMWithError:].cold.8
+ -[MKUSBDeviceController _configureNCMWithError:].cold.9
+ -[MKUSBDeviceController _restorePreviousConfigurationWithError:]
+ -[MKUSBDeviceController _restorePreviousConfigurationWithError:].cold.1
+ -[MKUSBDeviceController _restorePreviousConfigurationWithError:].cold.2
+ -[MKUSBDeviceController _restorePreviousConfigurationWithError:].cold.3
+ -[MKUSBDeviceController configureNCMWithCompletion:]
+ -[MKUSBDeviceController dealloc]
+ -[MKUSBDeviceController initInternal]
+ -[MKUSBDeviceController initInternal].cold.1
+ -[MKUSBDeviceController interfaceName]
+ -[MKUSBDeviceController restorePreviousConfigurationWithCompletion:]
+ _CFDictionaryCreateMutableCopy
+ _CNContactImageDataAvailableKey
+ _IOObjectConformsTo
+ _IOObjectGetClass
+ _IOServiceGetMatchingService
+ _IOUSBDeviceControllerGetService
+ _OBJC_CLASS_$_MKHPMInterface
+ _OBJC_CLASS_$_MKIOIterator
+ _OBJC_CLASS_$_MKIOObject
+ _OBJC_CLASS_$_MKTransferResourceResult
+ _OBJC_CLASS_$_MKTransferResult
+ _OBJC_CLASS_$_MKUSBDeviceController
+ _OBJC_CLASS_$__TtC12MigrationKit17SubOptionViewCell
+ _OBJC_IVAR_$_MKHPMInterface._deviceAddress
+ _OBJC_IVAR_$_MKHPMInterface._interface
+ _OBJC_IVAR_$_MKHPMInterface._queue
+ _OBJC_IVAR_$_MKIOIterator._iterator
+ _OBJC_IVAR_$_MKIOObject._object
+ _OBJC_IVAR_$_MKMessage._isFailed
+ _OBJC_IVAR_$_MKUSBDeviceController._interfaceName
+ _OBJC_IVAR_$_MKUSBDeviceController._previousDescription
+ _OBJC_IVAR_$_MKUSBDeviceController._queue
+ _OBJC_IVAR_$_MKUSBDeviceController._usbController
+ _OBJC_METACLASS_$_MKHPMInterface
+ _OBJC_METACLASS_$_MKIOIterator
+ _OBJC_METACLASS_$_MKIOObject
+ _OBJC_METACLASS_$_MKTransferResourceResult
+ _OBJC_METACLASS_$_MKTransferResult
+ _OBJC_METACLASS_$_MKUSBDeviceController
+ _OBJC_METACLASS_$__TtC12MigrationKit17SubOptionViewCell
+ __CLASS_METHODS_MKTransferResourceResult
+ __CLASS_METHODS_MKTransferResult
+ __CLASS_PROPERTIES_MKTransferResourceResult
+ __CLASS_PROPERTIES_MKTransferResult
+ __DATA_MKTransferResourceResult
+ __DATA_MKTransferResult
+ __DATA__TtC12MigrationKit13EsimAnalytics
+ __DATA__TtC12MigrationKit15IODeviceMonitor
+ __DATA__TtC12MigrationKit17SubOptionViewCell
+ __DATA__TtC12MigrationKit17TransferAnalytics
+ __DATA__TtC12MigrationKit21DataTransferAnalytics
+ __DATA__TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E16AnalyticsPayload
+ __DATA__TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E20EsimAnalyticsPayload
+ __DATA__TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E26AppContentAnalyticsPayload
+ __DATA__TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E28DataTransferAnalyticsPayload
+ __INSTANCE_METHODS_MKTransferResourceResult
+ __INSTANCE_METHODS_MKTransferResult
+ __INSTANCE_METHODS__TtC12MigrationKit17SubOptionViewCell
+ __IVARS_MKTransferResourceResult
+ __IVARS_MKTransferResult
+ __IVARS__TtC12MigrationKit13EsimAnalytics
+ __IVARS__TtC12MigrationKit15IODeviceMonitor
+ __IVARS__TtC12MigrationKit17SubOptionViewCell
+ __IVARS__TtC12MigrationKit17TransferAnalytics
+ __IVARS__TtC12MigrationKit21DataTransferAnalytics
+ __IVARS__TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E16AnalyticsPayload
+ __IVARS__TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E20EsimAnalyticsPayload
+ __IVARS__TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E26AppContentAnalyticsPayload
+ __IVARS__TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E28DataTransferAnalyticsPayload
+ __METACLASS_DATA_MKTransferResourceResult
+ __METACLASS_DATA_MKTransferResult
+ __METACLASS_DATA__TtC12MigrationKit13EsimAnalytics
+ __METACLASS_DATA__TtC12MigrationKit15IODeviceMonitor
+ __METACLASS_DATA__TtC12MigrationKit17SubOptionViewCell
+ __METACLASS_DATA__TtC12MigrationKit17TransferAnalytics
+ __METACLASS_DATA__TtC12MigrationKit21DataTransferAnalytics
+ __METACLASS_DATA__TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E16AnalyticsPayload
+ __METACLASS_DATA__TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E20EsimAnalyticsPayload
+ __METACLASS_DATA__TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E26AppContentAnalyticsPayload
+ __METACLASS_DATA__TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E28DataTransferAnalyticsPayload
+ __OBJC_$_CLASS_METHODS_MKHPMInterface
+ __OBJC_$_CLASS_METHODS_MKIOIterator
+ __OBJC_$_CLASS_METHODS_MKIOObject
+ __OBJC_$_CLASS_METHODS_MKUSBDeviceController
+ __OBJC_$_INSTANCE_METHODS_MKHPMInterface
+ __OBJC_$_INSTANCE_METHODS_MKIOIterator
+ __OBJC_$_INSTANCE_METHODS_MKIOObject
+ __OBJC_$_INSTANCE_METHODS_MKUSBDeviceController
+ __OBJC_$_INSTANCE_VARIABLES_MKHPMInterface
+ __OBJC_$_INSTANCE_VARIABLES_MKIOIterator
+ __OBJC_$_INSTANCE_VARIABLES_MKIOObject
+ __OBJC_$_INSTANCE_VARIABLES_MKUSBDeviceController
+ __OBJC_$_PROP_LIST_MKIOObject
+ __OBJC_$_PROP_LIST_MKUSBDeviceController
+ __OBJC_CLASS_RO_$_MKHPMInterface
+ __OBJC_CLASS_RO_$_MKIOIterator
+ __OBJC_CLASS_RO_$_MKIOObject
+ __OBJC_CLASS_RO_$_MKUSBDeviceController
+ __OBJC_METACLASS_RO_$_MKHPMInterface
+ __OBJC_METACLASS_RO_$_MKIOIterator
+ __OBJC_METACLASS_RO_$_MKIOObject
+ __OBJC_METACLASS_RO_$_MKUSBDeviceController
+ __PROTOCOLS_MKTransferResourceResult
+ __PROTOCOLS_MKTransferResourceResult.11
+ __PROTOCOLS_MKTransferResult
+ __PROTOCOLS_MKTransferResult.17
+ __ZL10_errorWithP7NSErrorP8NSStringS2_S2_i
+ ___44-[MKHPMInterface allowDefaultModeWithError:]_block_invoke
+ ___48-[MKHPMInterface forceDeviceModeWithCompletion:]_block_invoke
+ ___52-[MKUSBDeviceController configureNCMWithCompletion:]_block_invoke
+ ___68-[MKUSBDeviceController restorePreviousConfigurationWithCompletion:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___swift_get_extra_inhabitant_index.125Tm
+ ___swift_memcpy104_8
+ ___swift_memcpy65_8
+ ___swift_store_extra_inhabitant_index.126Tm
+ __errorWith
+ _associated conformance 12MigrationKit10NCMNetworkC4Role33_3BA067702B300DD38960BF92B24C4A5DLLOSHAASQ
+ _associated conformance 12MigrationKit14TransferResultV5StateOSHAASQ
+ _associated conformance 12MigrationKit14TransferResultV5StateOs12CaseIterableAA8AllCasessAFP_Sl
+ _associated conformance 12MigrationKit16TransferEndStateOSHAASQ
+ _associated conformance 12MigrationKit17OriginatingUIFlowOSHAASQ
+ _associated conformance 12MigrationKit22TransferResourceResultV10CodingKeys33_FF6C04413AC1AF3E06A31E473EE27722LLOSHAASQ
+ _associated conformance 12MigrationKit22TransferResourceResultV10CodingKeys33_FF6C04413AC1AF3E06A31E473EE27722LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 12MigrationKit22TransferResourceResultV10CodingKeys33_FF6C04413AC1AF3E06A31E473EE27722LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 12MigrationKit24OSMigrationResourceEntryV21InternalSwiftProtobuf26_MessageImplementationBaseAASH
+ _associated conformance 12MigrationKit24OSMigrationResourceEntryV21InternalSwiftProtobuf26_MessageImplementationBaseAaD0I0
+ _associated conformance 12MigrationKit24OSMigrationResourceEntryV21InternalSwiftProtobuf7MessageAAs28CustomDebugStringConvertible
+ _associated conformance 12MigrationKit24OSMigrationResourceEntryVSHAASQ
+ _associated conformance 12MigrationKit24OSMigrationUserSelectionO21InternalSwiftProtobuf4EnumAASH
+ _associated conformance 12MigrationKit24OSMigrationUserSelectionO21InternalSwiftProtobuf4EnumAASY
+ _associated conformance 12MigrationKit24OSMigrationUserSelectionOSHAASQ
+ _associated conformance 12MigrationKit24OSMigrationUserSelectionOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 12MigrationKit27OSMigrationFileContentStateO21InternalSwiftProtobuf4EnumAASH
+ _associated conformance 12MigrationKit27OSMigrationFileContentStateO21InternalSwiftProtobuf4EnumAASY
+ _associated conformance 12MigrationKit27OSMigrationFileContentStateOSHAASQ
+ _associated conformance 12MigrationKit27OSMigrationFileContentStateOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 12MigrationKit31OSMigrationConversationCategoryO21InternalSwiftProtobuf4EnumAASH
+ _associated conformance 12MigrationKit31OSMigrationConversationCategoryO21InternalSwiftProtobuf4EnumAASY
+ _associated conformance 12MigrationKit31OSMigrationConversationCategoryOSHAASQ
+ _associated conformance 12MigrationKit31OSMigrationConversationCategoryOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 12MigrationKit33OSMigrationCloudFileContentUpdateV21InternalSwiftProtobuf26_MessageImplementationBaseAASH
+ _associated conformance 12MigrationKit33OSMigrationCloudFileContentUpdateV21InternalSwiftProtobuf26_MessageImplementationBaseAaD0K0
+ _associated conformance 12MigrationKit33OSMigrationCloudFileContentUpdateV21InternalSwiftProtobuf7MessageAAs28CustomDebugStringConvertible
+ _associated conformance 12MigrationKit33OSMigrationCloudFileContentUpdateVSHAASQ
+ _associated conformance 12MigrationKit9FieldName33_703A8D8B92D72B2764A7A61BBD4D883ELLOSHAASQ
+ _associated conformance 12MigrationKit9WiFiBandsVs10SetAlgebraAASQ
+ _associated conformance 12MigrationKit9WiFiBandsVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 12MigrationKit9WiFiBandsVs9OptionSetAASY
+ _associated conformance 12MigrationKit9WiFiBandsVs9OptionSetAAs0G7Algebra
+ _block_copy_helper.151
+ _block_copy_helper.17
+ _block_copy_helper.2
+ _block_copy_helper.33
+ _block_copy_helper.37
+ _block_copy_helper.41
+ _block_copy_helper.51
+ _block_copy_helper.71
+ _block_copy_helper.74
+ _block_copy_helper.77
+ _block_copy_helper.86
+ _block_copy_helper.89
+ _block_copy_helper.93
+ _block_descriptor.153
+ _block_descriptor.19
+ _block_descriptor.35
+ _block_descriptor.39
+ _block_descriptor.4
+ _block_descriptor.43
+ _block_descriptor.53
+ _block_descriptor.73
+ _block_descriptor.76
+ _block_descriptor.79
+ _block_descriptor.88
+ _block_descriptor.91
+ _block_descriptor.95
+ _block_destroy_helper.152
+ _block_destroy_helper.18
+ _block_destroy_helper.3
+ _block_destroy_helper.34
+ _block_destroy_helper.38
+ _block_destroy_helper.42
+ _block_destroy_helper.52
+ _block_destroy_helper.72
+ _block_destroy_helper.75
+ _block_destroy_helper.78
+ _block_destroy_helper.87
+ _block_destroy_helper.90
+ _block_destroy_helper.94
+ _get_enum_tag_for_layout_string 12MigrationKit10NCMNetworkC5State33_3BA067702B300DD38960BF92B24C4A5DLLO
+ _get_enum_tag_for_layout_string Iegh_Sg
+ _getegid
+ _geteuid
+ _mach_error_string
+ _objc_msgSend$_allowDefaultModeWithError:
+ _objc_msgSend$_configureNCMWithError:
+ _objc_msgSend$_forceDeviceModeWithError:
+ _objc_msgSend$_restorePreviousConfigurationWithError:
+ _objc_msgSend$allowDefaultModeWithError:
+ _objc_msgSend$beginUpdates
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$children
+ _objc_msgSend$configureNCMWithCompletion:
+ _objc_msgSend$constraintGreaterThanOrEqualToAnchor:constant:
+ _objc_msgSend$constraintLessThanOrEqualToAnchor:constant:
+ _objc_msgSend$deleteRowsAtIndexPaths:withRowAnimation:
+ _objc_msgSend$dictionaryWithObjectsAndKeys:
+ _objc_msgSend$endUpdates
+ _objc_msgSend$firstDescendantOfClass:
+ _objc_msgSend$forServicesMatching:
+ _objc_msgSend$forceDeviceModeWithCompletion:
+ _objc_msgSend$imageDataAvailable
+ _objc_msgSend$initInternal
+ _objc_msgSend$initWithIterator:
+ _objc_msgSend$initWithObject:
+ _objc_msgSend$initWithUnownedObject:
+ _objc_msgSend$insertRowsAtIndexPaths:withRowAnimation:
+ _objc_msgSend$isFailed
+ _objc_msgSend$next
+ _objc_msgSend$object
+ _objc_msgSend$propertyForKey:
+ _objc_msgSend$reloadRowsAtIndexPaths:withRowAnimation:
+ _objc_msgSend$restorePreviousConfigurationWithCompletion:
+ _objc_msgSend$setIsFailed:
+ _objc_msgSend$setSeparatorInset:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$terminateDataSession:completionHandler:
+ _objc_msgSend$valueForKey:
+ _objc_release_x10
+ _object_getClass
+ _objectdestroy.136Tm
+ _objectdestroy.169Tm
+ _objectdestroy.16Tm
+ _objectdestroy.178Tm
+ _objectdestroy.28Tm
+ _objectdestroy.31Tm
+ _objectdestroy.9Tm
+ _setegid
+ _seteuid
+ _strerror
+ _symbolic $s12MigrationKit15IODeviceMonitorC8DelegateP
+ _symbolic $s12MigrationKit21AnalyticsEventSendingP
+ _symbolic $s12MigrationKit25TransferAnalyticsProtocolP
+ _symbolic Iegh_
+ _symbolic SDySSSo8NSObjectCGIegho_
+ _symbolic SDy__________G 12MigrationKit20OSMigrationDataClassO AA22AppDataclassPropertiesV
+ _symbolic SS4info_t
+ _symbolic SaySo10MKIOObjectCG
+ _symbolic SaySo10MKIOObjectCG______pSgIegHgg_ 12MigrationKit15IODeviceMonitorC8DelegateP
+ _symbolic Say_____G 12MigrationKit14TransferResultV
+ _symbolic Say_____G 12MigrationKit14TransferResultV5StateO
+ _symbolic Say_____G 12MigrationKit22TransferResourceResultV
+ _symbolic Say_____G 12MigrationKit22TransferResourceResultV9XPCHelperC
+ _symbolic Say_____G 12MigrationKit23SelectionViewControllerC6Choice33_68D94C0EE10F5D81245B7C362B34A061LLV
+ _symbolic Say_____G 12MigrationKit24OSMigrationResourceEntryV
+ _symbolic Say_____G 12MigrationKit24OSMigrationUserSelectionO
+ _symbolic Say_____G 12MigrationKit27OSMigrationFileContentStateO
+ _symbolic Say_____G 12MigrationKit31OSMigrationConversationCategoryO
+ _symbolic ScCy__________G So12WiFiP2PErrorV s5NeverO
+ _symbolic ScTy___________pG 12MigrationKit9SpeedTestV11Measurement33_1B003AA40772EC22D3A9EF5991FE1CA7LLV s5ErrorP
+ _symbolic So14MKHPMInterfaceCSg
+ _symbolic So21MKUSBDeviceControllerC
+ _symbolic So35WiFiAwarePublisherDataSessionHandleC
+ _symbolic So35WiFiAwarePublisherDataSessionHandleCSg
+ _symbolic _____ 12MigrationKit10NCMNetworkC4Role33_3BA067702B300DD38960BF92B24C4A5DLLO
+ _symbolic _____ 12MigrationKit10NCMNetworkC5State33_3BA067702B300DD38960BF92B24C4A5DLLO
+ _symbolic _____ 12MigrationKit13EsimAnalyticsC
+ _symbolic _____ 12MigrationKit13XPCConnectionC5State33_F6D2DC05EBDB05BDA5BDFC737745D0D7LLV
+ _symbolic _____ 12MigrationKit14TransferResultV
+ _symbolic _____ 12MigrationKit14TransferResultV5StateO
+ _symbolic _____ 12MigrationKit14TransferResultV9XPCHelperC
+ _symbolic _____ 12MigrationKit15IODeviceMonitorC
+ _symbolic _____ 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC
+ _symbolic _____ 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV
+ _symbolic _____ 12MigrationKit16TransferEndStateO
+ _symbolic _____ 12MigrationKit17OriginatingUIFlowO
+ _symbolic _____ 12MigrationKit17SubOptionViewCellC
+ _symbolic _____ 12MigrationKit17TransferAnalyticsC
+ _symbolic _____ 12MigrationKit20EsimAnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC
+ _symbolic _____ 12MigrationKit21DataTransferAnalyticsC
+ _symbolic _____ 12MigrationKit22TransferResourceResultV
+ _symbolic _____ 12MigrationKit22TransferResourceResultV10CodingKeys33_FF6C04413AC1AF3E06A31E473EE27722LLO
+ _symbolic _____ 12MigrationKit22TransferResourceResultV9XPCHelperC
+ _symbolic _____ 12MigrationKit23SelectionViewControllerC6Choice33_68D94C0EE10F5D81245B7C362B34A061LLV
+ _symbolic _____ 12MigrationKit24CoreAnalyticsEventSenderV
+ _symbolic _____ 12MigrationKit24OSMigrationResourceEntryV
+ _symbolic _____ 12MigrationKit24OSMigrationUserSelectionO
+ _symbolic _____ 12MigrationKit26AppContentAnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC
+ _symbolic _____ 12MigrationKit27OSMigrationFileContentStateO
+ _symbolic _____ 12MigrationKit28DataTransferAnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC
+ _symbolic _____ 12MigrationKit31OSMigrationConversationCategoryO
+ _symbolic _____ 12MigrationKit33OSMigrationCloudFileContentUpdateV
+ _symbolic _____ 12MigrationKit9FieldName33_703A8D8B92D72B2764A7A61BBD4D883ELLO
+ _symbolic _____ 12MigrationKit9SpeedTestV11Measurement33_1B003AA40772EC22D3A9EF5991FE1CA7LLV
+ _symbolic _____ 12MigrationKit9WiFiBandsV
+ _symbolic _____ So12WiFiP2PErrorV
+ _symbolic _____10identifier______y___________pGt 10Foundation4DataV s6ResultOsRi_zRi0_zrlE 12MigrationKit17HashedFileContentO s5ErrorP
+ _symbolic _____4role_SSSg10generationAC8dataRatet 12MigrationKit10NCMNetworkC4Role33_3BA067702B300DD38960BF92B24C4A5DLLO
+ _symbolic _____6result_t 12MigrationKit14TransferResultV
+ _symbolic _____9selection______10estimationt 12MigrationKit9SelectionO AA10EstimationV
+ _symbolic _____Sg 12MigrationKit11PersistenceV
+ _symbolic _____Sg 12MigrationKit16TransferEndStateO
+ _symbolic _____Sg 12MigrationKit22TransferResourceResultV
+ _symbolic _____Sg 12MigrationKit24OSMigrationUserSelectionO
+ _symbolic _____Sg 12MigrationKit27OSMigrationFileContentStateO
+ _symbolic _____Sg 12MigrationKit33OSMigrationCloudFileContentUpdateV
+ _symbolic _____Sg 12MigrationKit5ProxyC
+ _symbolic _____Sg 15AppMigrationKit03DevA15MappingOverrideV
+ _symbolic _____Sg 6IMCore12ImportExportO010AttachmentC8IteratorC0E0C5BatchV
+ _symbolic _____Sg 6IMCore12ImportExportO7StickerV
+ _symbolic _____Sg So18CFRunLoopSourceRefa
+ _symbolic _____Sg s13OpaquePointerV
+ _symbolic _____SgXwz_Xx 12MigrationKit5ProxyC
+ _symbolic ___________t 12MigrationKit20OSMigrationDataClassO AA14TransferResultV
+ _symbolic ___________t 12MigrationKit20OSMigrationDataClassO AA22AppDataclassPropertiesV
+ _symbolic ______p 12MigrationKit21AnalyticsEventSendingP
+ _symbolic ______pSg 12MigrationKit25TransferAnalyticsProtocolP
+ _symbolic ______pSgXw 12MigrationKit15IODeviceMonitorC8DelegateP
+ _symbolic ______pXp 12MigrationKit8ExporterP
+ _symbolic _____y_SSG 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV
+ _symbolic _____y_SbG 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV
+ _symbolic _____y_SdG 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV
+ _symbolic _____y_SiG 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 12MigrationKit13XPCConnectionC5State33_F6D2DC05EBDB05BDA5BDFC737745D0D7LLV
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 12MigrationKit14XPCDaemonStateO
+ _symbolic _____y_____G s11_SetStorageC 12MigrationKit9FieldName33_703A8D8B92D72B2764A7A61BBD4D883ELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12MigrationKit22TransferResourceResultV10CodingKeys33_FF6C04413AC1AF3E06A31E473EE27722LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12MigrationKit22TransferResourceResultV10CodingKeys33_FF6C04413AC1AF3E06A31E473EE27722LLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation9IndexPathV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit14TransferResultV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit14TransferResultV5StateO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit22TransferResourceResultV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit23SelectionViewControllerC6Choice33_68D94C0EE10F5D81245B7C362B34A061LLV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit24OSMigrationResourceEntryV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit31OSMigrationConversationCategoryO
+ _symbolic _____y_____GSg s9UnmanagedV 12MigrationKit15IODeviceMonitorC
+ _symbolic _____y______G 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV 03AppaB013ArchiveFormatO
+ _symbolic _____y______G 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV AA0A4ModeO
+ _symbolic _____y______G 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV AA0A9DirectionO
+ _symbolic _____y______G 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV AA13TelemetryTypeO
+ _symbolic _____y______G 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV AA16TransferEndStateO
+ _symbolic _____y______G 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV AA17OriginatingUIFlowO
+ _symbolic _____y______G 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV s6UInt16V
+ _symbolic _____y______G 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV s6UInt64V
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 12MigrationKit13XPCConnectionC5State33_F6D2DC05EBDB05BDA5BDFC737745D0D7LLV So16os_unfair_lock_sV
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 12MigrationKit14XPCDaemonStateO So16os_unfair_lock_sV
+ _symbolic _____y__________G s18_DictionaryStorageC 12MigrationKit20OSMigrationDataClassO AC14TransferResultV
+ _symbolic _____y__________G s18_DictionaryStorageC 12MigrationKit20OSMigrationDataClassO AC22AppDataclassPropertiesV
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC 12MigrationKit20OSMigrationDataClassO AC14TransferResultV
+ _symbolic y_____YbcSg 10Foundation3URLV
+ _symbolic ytIeghr_
+ _symbolic yyc
+ _type_layout_string 12MigrationKit10NCMNetworkC5State33_3BA067702B300DD38960BF92B24C4A5DLLO
+ _type_layout_string 12MigrationKit13XPCConnectionC5State33_F6D2DC05EBDB05BDA5BDFC737745D0D7LLV
+ _type_layout_string 12MigrationKit14TransferResultV
+ _type_layout_string 12MigrationKit22TransferResourceResultV
+ _type_layout_string 12MigrationKit23SelectionViewControllerC6Choice33_68D94C0EE10F5D81245B7C362B34A061LLV
+ _type_layout_string 12MigrationKit9WiFiBandsV
- +[MKUSBRoleSwap configureNCM]
- +[MKUSBRoleSwap destroyHPMLibInterface:]
- +[MKUSBRoleSwap disableDeviceModeAndNCM]
- +[MKUSBRoleSwap enableDeviceModeAndNCM]
- +[MKUSBRoleSwap getCurrentUSBDataRole]
- +[MKUSBRoleSwap getDeviceAddressFromHPMService:]
- +[MKUSBRoleSwap getHPMLibInterface:]
- +[MKUSBRoleSwap isUSBConnected]
- +[MKUSBRoleSwap restorePreviousUSBConfiguration]
- +[MKUSBRoleSwap setUSBDeviceModeAndNCM:error:]
- +[MKUSBRoleSwap startMonitoringUSBStateWithCallback:]
- +[MKUSBRoleSwap stopMonitoringUSBState]
- -[MKUSBMonitoringState .cxx_destruct]
- -[MKUSBMonitoringState callbackQueue]
- -[MKUSBMonitoringState callback]
- -[MKUSBMonitoringState checkAndInvokeCallbackForService:]
- -[MKUSBMonitoringState dealloc]
- -[MKUSBMonitoringState handleServiceMatched:]
- -[MKUSBMonitoringState init]
- -[MKUSBMonitoringState interestNotifier]
- -[MKUSBMonitoringState notificationPort]
- -[MKUSBMonitoringState service]
- -[MKUSBMonitoringState setCallback:]
- -[MKUSBMonitoringState setCallbackQueue:]
- -[MKUSBMonitoringState setInterestNotifier:]
- -[MKUSBMonitoringState setNotificationPort:]
- -[MKUSBMonitoringState setService:]
- -[MKUSBMonitoringState setStateNotifier:]
- -[MKUSBMonitoringState stateNotifier]
- GCC_except_table29
- GCC_except_table30
- _CFGetTypeID
- _CFNumberGetTypeID
- _CFNumberGetValue
- _IOServiceAddInterestNotification
- _NSLog
- _OBJC_CLASS_$_MKMigratorContext
- _OBJC_CLASS_$_MKResourceContext
- _OBJC_CLASS_$_MKUSBMonitoringState
- _OBJC_CLASS_$_MKUSBRoleSwap
- _OBJC_IVAR_$_MKUSBMonitoringState._callback
- _OBJC_IVAR_$_MKUSBMonitoringState._callbackQueue
- _OBJC_IVAR_$_MKUSBMonitoringState._interestNotifier
- _OBJC_IVAR_$_MKUSBMonitoringState._notificationPort
- _OBJC_IVAR_$_MKUSBMonitoringState._service
- _OBJC_IVAR_$_MKUSBMonitoringState._stateNotifier
- _OBJC_METACLASS_$_MKMigratorContext
- _OBJC_METACLASS_$_MKResourceContext
- _OBJC_METACLASS_$_MKUSBMonitoringState
- _OBJC_METACLASS_$_MKUSBRoleSwap
- __CLASS_METHODS_MKMigratorContext
- __CLASS_METHODS_MKResourceContext
- __CLASS_PROPERTIES_MKMigratorContext
- __CLASS_PROPERTIES_MKResourceContext
- __DATA_MKMigratorContext
- __DATA_MKResourceContext
- __DATA__TtC12MigrationKit11ClientProxy
- __DATA__TtC12MigrationKit11ServerProxy
- __DATA__TtC12MigrationKit15EsimOnlyPayload
- __DATA__TtC12MigrationKit17EsimOnlyAnalytics
- __DATA__TtC12MigrationKit18OSMigrationPayload
- __DATA__TtC12MigrationKit20OSMigrationAnalytics
- __DATA__TtC12MigrationKit23FullDataTransferPayload
- __DATA__TtC12MigrationKit25FullDataTransferAnalytics
- __DATA__TtC12MigrationKit28OSMigrationAppContentPayload
- __INSTANCE_METHODS_MKMigratorContext
- __INSTANCE_METHODS_MKResourceContext
- __INSTANCE_METHODS__TtC12MigrationKit11ClientProxy
- __INSTANCE_METHODS__TtC12MigrationKit11ServerProxy
- __INSTANCE_METHODS__TtC12MigrationKit24WaitExportViewController
- __INSTANCE_METHODS__TtC12MigrationKit24WaitImportViewController
- __IVARS_MKMigratorContext
- __IVARS_MKResourceContext
- __IVARS__TtC12MigrationKit15EsimOnlyPayload
- __IVARS__TtC12MigrationKit17EsimOnlyAnalytics
- __IVARS__TtC12MigrationKit18OSMigrationPayload
- __IVARS__TtC12MigrationKit20OSMigrationAnalytics
- __IVARS__TtC12MigrationKit23FullDataTransferPayload
- __IVARS__TtC12MigrationKit25FullDataTransferAnalytics
- __IVARS__TtC12MigrationKit28OSMigrationAppContentPayload
- __METACLASS_DATA_MKMigratorContext
- __METACLASS_DATA_MKResourceContext
- __METACLASS_DATA__TtC12MigrationKit11ClientProxy
- __METACLASS_DATA__TtC12MigrationKit11ServerProxy
- __METACLASS_DATA__TtC12MigrationKit15EsimOnlyPayload
- __METACLASS_DATA__TtC12MigrationKit17EsimOnlyAnalytics
- __METACLASS_DATA__TtC12MigrationKit18OSMigrationPayload
- __METACLASS_DATA__TtC12MigrationKit20OSMigrationAnalytics
- __METACLASS_DATA__TtC12MigrationKit23FullDataTransferPayload
- __METACLASS_DATA__TtC12MigrationKit25FullDataTransferAnalytics
- __METACLASS_DATA__TtC12MigrationKit28OSMigrationAppContentPayload
- __OBJC_$_CLASS_METHODS_MKUSBRoleSwap
- __OBJC_$_INSTANCE_METHODS_MKUSBMonitoringState
- __OBJC_$_INSTANCE_VARIABLES_MKUSBMonitoringState
- __OBJC_$_PROP_LIST_MKUSBMonitoringState
- __OBJC_CLASS_RO_$_MKUSBMonitoringState
- __OBJC_CLASS_RO_$_MKUSBRoleSwap
- __OBJC_METACLASS_RO_$_MKUSBMonitoringState
- __OBJC_METACLASS_RO_$_MKUSBRoleSwap
- __PROTOCOLS_MKMigratorContext
- __PROTOCOLS_MKMigratorContext.18
- __PROTOCOLS_MKResourceContext
- __PROTOCOLS_MKResourceContext.12
- __ZL13_hpmInterface
- __ZL14_deviceAddress
- __ZL14_usbController
- __ZL16_didConfigureNCM
- __ZL16_monitoringState
- __ZL19_didPerformRoleSwap
- __ZL20_previousDescription
- __ZL21usb_interest_callbackPvjjS_
- __ZL26usb_state_changed_callbackPvj
- ___57-[MKUSBMonitoringState checkAndInvokeCallbackForService:]_block_invoke
- ___block_descriptor_41_ea8_32bs_e5_v8?0ls32l8
- ___swift_get_extra_inhabitant_index.119Tm
- ___swift_memcpy57_8
- ___swift_memcpy89_8
- ___swift_store_extra_inhabitant_index.120Tm
- _associated conformance 12MigrationKit12TransferTypeOSHAASQ
- _associated conformance 12MigrationKit15MigratorContextV6ResultOSHAASQ
- _associated conformance 12MigrationKit15ResourceContextV10CodingKeys33_55B37BD01B7D4E643A20DBFF17B25A54LLOSHAASQ
- _associated conformance 12MigrationKit15ResourceContextV10CodingKeys33_55B37BD01B7D4E643A20DBFF17B25A54LLOs0E3KeyAAs23CustomStringConvertible
- _associated conformance 12MigrationKit15ResourceContextV10CodingKeys33_55B37BD01B7D4E643A20DBFF17B25A54LLOs0E3KeyAAs28CustomDebugStringConvertible
- _associated conformance 12MigrationKit17CompressionSchemeOSHAASQ
- _associated conformance 12MigrationKit17OriginatingUiFlowOSHAASQ
- _associated conformance 12MigrationKit19OSMigrationEndStateOSHAASQ
- _associated conformance 12MigrationKit19OSMigrationResourceV21InternalSwiftProtobuf26_MessageImplementationBaseAASH
- _associated conformance 12MigrationKit19OSMigrationResourceV21InternalSwiftProtobuf26_MessageImplementationBaseAaD0H0
- _associated conformance 12MigrationKit19OSMigrationResourceV21InternalSwiftProtobuf7MessageAAs28CustomDebugStringConvertible
- _associated conformance 12MigrationKit19OSMigrationResourceVSHAASQ
- _block_copy_helper.182
- _block_copy_helper.31
- _block_copy_helper.35
- _block_copy_helper.49
- _block_copy_helper.61
- _block_copy_helper.64
- _block_copy_helper.66
- _block_copy_helper.69
- _block_copy_helper.72
- _block_copy_helper.75
- _block_copy_helper.76
- _block_copy_helper.84
- _block_copy_helper.87
- _block_copy_helper.88
- _block_copy_helper.91
- _block_descriptor.184
- _block_descriptor.33
- _block_descriptor.37
- _block_descriptor.51
- _block_descriptor.63
- _block_descriptor.66
- _block_descriptor.68
- _block_descriptor.71
- _block_descriptor.74
- _block_descriptor.77
- _block_descriptor.78
- _block_descriptor.86
- _block_descriptor.89
- _block_descriptor.90
- _block_descriptor.93
- _block_destroy_helper.183
- _block_destroy_helper.32
- _block_destroy_helper.36
- _block_destroy_helper.50
- _block_destroy_helper.62
- _block_destroy_helper.65
- _block_destroy_helper.67
- _block_destroy_helper.70
- _block_destroy_helper.73
- _block_destroy_helper.76
- _block_destroy_helper.77
- _block_destroy_helper.85
- _block_destroy_helper.88
- _block_destroy_helper.89
- _block_destroy_helper.92
- _objc_msgSend$checkAndInvokeCallbackForService:
- _objc_msgSend$configureNCM
- _objc_msgSend$createSymbolicLinkAtURL:withDestinationURL:error:
- _objc_msgSend$destroyHPMLibInterface:
- _objc_msgSend$disableDeviceModeAndNCM
- _objc_msgSend$disassociateWithReason:
- _objc_msgSend$enableDeviceModeAndNCM
- _objc_msgSend$getCurrentUSBDataRole
- _objc_msgSend$getDeviceAddressFromHPMService:
- _objc_msgSend$getHPMLibInterface:
- _objc_msgSend$handleServiceMatched:
- _objc_msgSend$notificationPort
- _objc_msgSend$restorePreviousUSBConfiguration
- _objc_msgSend$setCallback:
- _objc_msgSend$setCallbackQueue:
- _objc_msgSend$setNotificationPort:
- _objc_msgSend$setStateNotifier:
- _objc_msgSend$setUSBDeviceModeAndNCM:error:
- _objc_msgSend$startMonitoringUSBStateWithCallback:
- _objc_msgSend$stateNotifier
- _objc_msgSend$stopMonitoringUSBState
- _objc_retainBlock
- _objectdestroy.15Tm
- _objectdestroy.197Tm
- _objectdestroy.230Tm
- _objectdestroy.239Tm
- _objectdestroy.26Tm
- _objectdestroy.29Tm
- _objectdestroy.36Tm
- _objectdestroy.38Tm
- _objectdestroy.8Tm
- _symbolic $s12MigrationKit0A17AnalyticsProtocolP
- _symbolic Ig_
- _symbolic SDySS_____G 12MigrationKit14FeaturePayloadC
- _symbolic SDy__________G 12MigrationKit9SelectionO AA22AppDataclassPropertiesV
- _symbolic SayScCySb_____GG s5NeverO
- _symbolic Say_____G 12MigrationKit15MigratorContextV
- _symbolic Say_____G 12MigrationKit15ResourceContextV
- _symbolic Say_____G 12MigrationKit15ResourceContextV9XPCHelperC
- _symbolic Say_____G 12MigrationKit19OSMigrationResourceV
- _symbolic Say_____GSg 12MigrationKit10EstimationV
- _symbolic Say_____GSg 12MigrationKit15MigratorContextV
- _symbolic Say_____GSg 12MigrationKit9SelectionO
- _symbolic SbIeAgHr_
- _symbolic ScCySSSg______pG s5ErrorP
- _symbolic ScGySbG
- _symbolic ScTy_____Sg_____GSg 12MigrationKit10NCMNetworkC s5NeverO
- _symbolic ScTy___________pG s6UInt64V s5ErrorP
- _symbolic _____ 12MigrationKit11ClientProxyC
- _symbolic _____ 12MigrationKit11ServerProxyC
- _symbolic _____ 12MigrationKit12TransferTypeO
- _symbolic _____ 12MigrationKit15EsimOnlyPayloadC
- _symbolic _____ 12MigrationKit15MigratorContextV
- _symbolic _____ 12MigrationKit15MigratorContextV6ResultO
- _symbolic _____ 12MigrationKit15MigratorContextV9XPCHelperC
- _symbolic _____ 12MigrationKit15ResourceContextV
- _symbolic _____ 12MigrationKit15ResourceContextV10CodingKeys33_55B37BD01B7D4E643A20DBFF17B25A54LLO
- _symbolic _____ 12MigrationKit15ResourceContextV9XPCHelperC
- _symbolic _____ 12MigrationKit17CompressionSchemeO
- _symbolic _____ 12MigrationKit17EsimOnlyAnalyticsC
- _symbolic _____ 12MigrationKit17OriginatingUiFlowO
- _symbolic _____ 12MigrationKit18OSMigrationPayloadC
- _symbolic _____ 12MigrationKit18OSMigrationPayloadC5FieldV
- _symbolic _____ 12MigrationKit19OSMigrationEndStateO
- _symbolic _____ 12MigrationKit19OSMigrationResourceV
- _symbolic _____ 12MigrationKit20OSMigrationAnalyticsC
- _symbolic _____ 12MigrationKit23FullDataTransferPayloadC
- _symbolic _____ 12MigrationKit25FullDataTransferAnalyticsC
- _symbolic _____ 12MigrationKit28OSMigrationAppContentPayloadC
- _symbolic _____ 12MigrationKit9SpeedTestV11MeasurementV
- _symbolic _____10estimation_t 12MigrationKit10EstimationV
- _symbolic _____7context_t 12MigrationKit15MigratorContextV
- _symbolic _____Sg 12MigrationKit10NCMNetworkC
- _symbolic _____Sg 12MigrationKit11ClientProxyC
- _symbolic _____Sg 12MigrationKit11ServerProxyC
- _symbolic _____Sg 12MigrationKit15MigratorContextV
- _symbolic _____Sg 12MigrationKit15ResourceContextV
- _symbolic _____Sg 12MigrationKit17OriginatingUiFlowO
- _symbolic _____Sg 12MigrationKit19OSMigrationEndStateO
- _symbolic _____SgIeAgHr_ 12MigrationKit10NCMNetworkC
- _symbolic _____SgXw 12MigrationKit11ServerProxyC
- _symbolic ______pSg 12MigrationKit0A17AnalyticsProtocolP
- _symbolic _____ySSSg______pG 12MigrationKit25TimeSensitiveContinuationV s5ErrorP
- _symbolic _____ySS_____G s18_DictionaryStorageC 12MigrationKit14FeaturePayloadC
- _symbolic _____yScCySb_____GG s23_ContiguousArrayStorageC s5NeverO
- _symbolic _____y_SSG 12MigrationKit18OSMigrationPayloadC5FieldV
- _symbolic _____y_SbG 12MigrationKit18OSMigrationPayloadC5FieldV
- _symbolic _____y_SdG 12MigrationKit18OSMigrationPayloadC5FieldV
- _symbolic _____y_SiG 12MigrationKit18OSMigrationPayloadC5FieldV
- _symbolic _____y_____G s22KeyedDecodingContainerV 12MigrationKit15ResourceContextV10CodingKeys33_55B37BD01B7D4E643A20DBFF17B25A54LLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 12MigrationKit15ResourceContextV10CodingKeys33_55B37BD01B7D4E643A20DBFF17B25A54LLO
- _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit10EstimationV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit15MigratorContextV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit15MigratorContextV6ResultO
- _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit15ResourceContextV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit19OSMigrationResourceV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 6IMCore12ImportExportO12MessageStateV
- _symbolic _____y______G 12MigrationKit18OSMigrationPayloadC5FieldV 03AppaB013ArchiveFormatO
- _symbolic _____y______G 12MigrationKit18OSMigrationPayloadC5FieldV AA0A4ModeO
- _symbolic _____y______G 12MigrationKit18OSMigrationPayloadC5FieldV AA0A9DirectionO
- _symbolic _____y______G 12MigrationKit18OSMigrationPayloadC5FieldV AA0C8EndStateO
- _symbolic _____y______G 12MigrationKit18OSMigrationPayloadC5FieldV AA12TransferTypeO
- _symbolic _____y______G 12MigrationKit18OSMigrationPayloadC5FieldV AA13TelemetryTypeO
- _symbolic _____y______G 12MigrationKit18OSMigrationPayloadC5FieldV AA17CompressionSchemeO
- _symbolic _____y______G 12MigrationKit18OSMigrationPayloadC5FieldV AA17OriginatingUiFlowO
- _symbolic _____y______G 12MigrationKit18OSMigrationPayloadC5FieldV s6UInt16V
- _symbolic _____y______G 12MigrationKit18OSMigrationPayloadC5FieldV s6UInt64V
- _symbolic _____y__________G s18_DictionaryStorageC 12MigrationKit9SelectionO AC15MigratorContextV
- _symbolic _____y__________G s18_DictionaryStorageC 12MigrationKit9SelectionO AC22AppDataclassPropertiesV
- _type_layout_string 12MigrationKit15MessageExporterV
- _type_layout_string 12MigrationKit15MigratorContextV
- _type_layout_string 12MigrationKit15ResourceContextV
- _type_layout_string 12MigrationKit9SpeedTestV11MeasurementV
CStrings:
+ " does not have a required entitlement value"
+ " network connection lost"
+ " state, shutting down"
+ "\" state, notifying UI that daemon crashed"
+ "-[MKHPMInterface _allowDefaultModeWithError:]"
+ "-[MKHPMInterface _forceDeviceModeWithError:]"
+ "-[MKUSBDeviceController _configureNCMWithError:]"
+ "-[MKUSBDeviceController _restorePreviousConfigurationWithError:]"
+ "@20@0:8I16"
+ "App Store"
+ "App Store apps API host"
+ "App Store apps API path prefix before {storefront}/apps"
+ "Attachment has invalid negative total_bytes=%{public}lld: %s"
+ "Attempting role swap"
+ "B24@0:8^@16"
+ "BSD Name"
+ "Bluetooth connection lost while in "
+ "Can't get attachment duration for a non-Messages selection"
+ "Cannot convert data class "
+ "CloudFileContentUpdate"
+ "CompletionViewController init - button_enabled=%{bool}d, auto_complete=%{bool}d"
+ "CompletionViewController viewDidAppear - auto-completing"
+ "CompletionViewController viewDidAppear - enabling continue button for manual tap"
+ "Config disabled export for "
+ "Config disabled import for "
+ "Configured USB NCM. "
+ "Could not find peer's mDNS service on NCM interface"
+ "Couldn't construct a date 1 year ago"
+ "Couldn't construct a date 30 days ago"
+ "Current role is: "
+ "CurrentState"
+ "Data transfer took "
+ "DataRateDescription"
+ "Deleting existing "
+ "Developer mapping enabled but no dev properties in PreflightInfo"
+ "Device not ready. ("
+ "Device plugged in"
+ "Device unplugged"
+ "DeviceAddress"
+ "ESIM transfer took "
+ "Empty com.apple.private.migrationkit.system-dataclass entitlement"
+ "Enabled USB device mode and NCM. Press Enter to restore previous configuration."
+ "Enables dumping of serialized and deserialized protobuf messages into the local files debug directory"
+ "Enables overriding defaults from an `overrides.plist` file in the Files app"
+ "Enables showing implicit data classes"
+ "Enables skipping ASC mapping. To export, mapping details must be provided in app Info.plist. For import, this implicitly trusts the bundleID from `targetPlatformIdentifiers` exported by Android."
+ "Error fetching contact IDs with photos"
+ "Expected a %s %s but found %s: %s local value"
+ "Failed configuring NCM"
+ "Failed creating HPMInterface"
+ "Failed creating USB device controller"
+ "Failed creating USBDeviceController"
+ "Failed creating exporter for selection: "
+ "Failed evaluating FCI support for unknown data class: "
+ "Failed excluding from backup"
+ "Failed getting BSD Name property from IOEthernetInterface"
+ "Failed sending %s telemetry to CoreAnalytics"
+ "Failed to allow USB to return to default mode"
+ "Failed to append AppleUSBNCMControl interface: %d"
+ "Failed to append AppleUSBNCMData interface: %d"
+ "Failed to bring up NCM network"
+ "Failed to create NCM description"
+ "Failed to create data class from entitlement "
+ "Failed to create matching dict"
+ "Failed to create port"
+ "Failed to export: "
+ "Failed to obtain XPCDaemon proxy from migrationd"
+ "Failed to restart monitoring USB state"
+ "Failed to restore USB description: %d"
+ "Failed to restore previous USB configuration"
+ "Failed to save previous USB description"
+ "Failed to setegid to mobile: "
+ "Failed to seteuid to mobile: "
+ "Failed to start monitoring USB state"
+ "Failed to terminate data session. error="
+ "Failed to trigger bus re-enumeration: %d"
+ "Failure ingesting file content part "
+ "Feature"
+ "ForceMode(enable=0) failed: 0x%x"
+ "ForceMode(enable=1) failed: 0x%x"
+ "ForceUSBDeviceMode(enable=0) failed: 0x%x"
+ "ForceUSBDeviceMode(enable=1) failed: 0x%x"
+ "Found %{public}ld contacts with photos"
+ "GenerationDescription"
+ "IO service not found"
+ "IOEthernetInterface"
+ "IOEthernetInterface object not found; unable to get BSD name"
+ "IOServiceTerminate"
+ "IOUSBDeviceControllerGetService failed"
+ "IOUSBDeviceControllerGoOffAndOnBus failed: %d"
+ "IOUSBDeviceControllerSetDescription failed: %d"
+ "IOUSBDeviceDescriptionAppendConfiguration failed: %d"
+ "MESSAGE_OPTION_ALL_ATTACHMENTS"
+ "MESSAGE_OPTION_NO_ATTACHMENTS"
+ "MESSAGE_OPTION_ONE_YEAR"
+ "MESSAGE_OPTION_THIRTY_DAYS"
+ "MKHPMInterface"
+ "MKHPMInterface.mm"
+ "MKIOIterator"
+ "MKIOObject"
+ "MKTransferResourceResult"
+ "MKTransferResult"
+ "MKUSBDeviceController"
+ "MKUSBDeviceController.m"
+ "Manual override disabled export for "
+ "Manual override disabled import for "
+ "Messages (1 year of attachments)"
+ "Messages (30 days of attachments)"
+ "Messages (All attachments)"
+ "Messages (No attachments)"
+ "MigrationKit/IODeviceMonitor.swift"
+ "MigrationKit/LocalFilesPersistence.swift"
+ "MigrationKit/Selection+Message.swift"
+ "MigrationKit/SubOptionViewCell.swift"
+ "MigrationKit/Trace.swift"
+ "MigrationKit/TransferAnalyticsPayload.swift"
+ "Mutually supported bands: %s"
+ "NCM fallback failed"
+ "NCM not supported"
+ "NOT_A_MESSAGE_OPTION"
+ "Network doesn't exist"
+ "No TTR persistence dir"
+ "No error context for state: "
+ "No failure context"
+ "No interface name for NCM network"
+ "No pairing parameters"
+ "OnBus"
+ "Received daemon interruption while in \""
+ "Received remote failure for file content part "
+ "Remote cloud file not downloaded"
+ "Restored previous configuration"
+ "Result for AppContent result is .unknown"
+ "Runs a speed test against the server, requesting chunks of this many MB of random data."
+ "Self-participant with ID %s not found in database"
+ "Sending %s telemetry to CoreAnalytics: %s"
+ "Server confirmed ACK for %s"
+ "Skipping import of currently associated network. ssid=%{private}s"
+ "Skipping import of network without password. ssid=%{private}s %{private}s"
+ "Source dev identity %s"
+ "Static config disabled export for "
+ "Static config disabled import for "
+ "SubOptionViewCell"
+ "Successfully sent %s telemetry to CoreAnalytics"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_interfaceName"
+ "TB,N,V_isFailed"
+ "Terminating data session"
+ "Timed out"
+ "Timed out waiting for device to become ready"
+ "Unable to determine role"
+ "Unable to perform role swap: HPMInterface is nil. Check earlier logs for error details"
+ "Will start monitoring device %s"
+ "Will stop monitoring device %s"
+ "[%s]:%d Failed getting BSD Name property from IOEthernetInterface"
+ "[%s]:%d Failed to append AppleUSBNCMControl interface: %d"
+ "[%s]:%d Failed to append AppleUSBNCMData interface: %d"
+ "[%s]:%d Failed to create NCM description"
+ "[%s]:%d Failed to restore USB description: %d"
+ "[%s]:%d Failed to save previous USB description"
+ "[%s]:%d Failed to trigger bus re-enumeration: %d"
+ "[%s]:%d ForceMode(enable=0) failed: 0x%x"
+ "[%s]:%d ForceMode(enable=1) failed: 0x%x"
+ "[%s]:%d ForceUSBDeviceMode(enable=0) failed: 0x%x"
+ "[%s]:%d ForceUSBDeviceMode(enable=1) failed: 0x%x"
+ "[%s]:%d IOEthernetInterface object not found; unable to get BSD name"
+ "[%s]:%d IOUSBDeviceControllerGetService failed"
+ "[%s]:%d IOUSBDeviceControllerGoOffAndOnBus failed: %d"
+ "[%s]:%d IOUSBDeviceControllerSetDescription failed: %d"
+ "[%s]:%d IOUSBDeviceDescriptionAppendConfiguration failed: %d"
+ "[%s]:%d Timed out waiting for device to become ready"
+ "[MKHPMInterface] Brief delay between ForceUSBDeviceMode and replug"
+ "[MKHPMInterface] Brief delay between forceMode and ForceUSBDeviceMode"
+ "[MKHPMInterface] Calling ForceUSBDeviceMode to switch to device mode"
+ "[MKHPMInterface] Calling forceMode(device=0x%llx, enable=0) to replug USB port"
+ "[MKHPMInterface] Calling forceMode(device=0x%llx, enable=1) to unplug USB port"
+ "[MKHPMInterface] Failed to find device address"
+ "[MKHPMInterface] Failed to get matching services for AppleHPMARM"
+ "[MKHPMInterface] Failed to obtain AppleHPMLibInterface"
+ "[MKHPMInterface] Found device address: 0x%llx"
+ "[MKHPMInterface] IOCreatePlugInInterfaceForService failed with result: 0x%x"
+ "[MKHPMInterface] QueryInterface failed with result: 0x%x"
+ "[MKHPMInterface] Successfully disabled ForceUSBDeviceMode (enable=0)"
+ "[MKHPMInterface] Successfully enabled USB device mode"
+ "[MKHPMInterface] Successfully obtained AppleHPMLibInterface"
+ "[MKIOIterator] Failed to get iterator for service '%@': %s"
+ "[MKIOIterator] Failed to get matching dictionary for '%@'"
+ "[MKIOObject] Failed to get child iterator for '%@': %s"
+ "[MKIOObject] Failed to get class name for '%@': %s"
+ "[MKIOObject] Failed to get entry name: %s"
+ "[MKIOObject] Failed to get matching dictionary for '%@'"
+ "[MKIOObject] Failed to get service '%@'"
+ "[MKIOObject] Failed to retain object: %s"
+ "[MKUSBDeviceController] Added AppleUSBNCMControl at interface index %d"
+ "[MKUSBDeviceController] Added AppleUSBNCMData at interface index %d"
+ "[MKUSBDeviceController] Adding NCM interfaces"
+ "[MKUSBDeviceController] IOUSBDeviceControllerCreate failed: 0x%x"
+ "[MKUSBDeviceController] No previous USB configuration to restore"
+ "[MKUSBDeviceController] Reconfiguring USB for NCM"
+ "[MKUSBDeviceController] Restoring previous USB configuration"
+ "[MKUSBDeviceController] Saved previous USB description"
+ "[MKUSBDeviceController] Successfully configured USB for NCM (interface=%@)"
+ "[MKUSBDeviceController] Successfully restored previous USB configuration"
+ "[MKUSBDeviceController] Waiting for device to become ready..."
+ "^^{AppleHPMLibInterfaceStructV3}"
+ "_TtC12MigrationKit13EsimAnalytics"
+ "_TtC12MigrationKit15IODeviceMonitor"
+ "_TtC12MigrationKit17SubOptionViewCell"
+ "_TtC12MigrationKit17TransferAnalytics"
+ "_TtC12MigrationKit21DataTransferAnalytics"
+ "_TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E16AnalyticsPayload"
+ "_TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E20EsimAnalyticsPayload"
+ "_TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E26AppContentAnalyticsPayload"
+ "_TtC12MigrationKitP33_703A8D8B92D72B2764A7A61BBD4D883E28DataTransferAnalyticsPayload"
+ "_allowDefaultModeWithError:"
+ "_checked"
+ "_configureNCMWithError:"
+ "_deviceAddress"
+ "_estimationOverride"
+ "_forceDeviceModeWithError:"
+ "_interfaceName"
+ "_isFailed"
+ "_isSpam"
+ "_iterator"
+ "_notifyAttestation(status:)"
+ "_object"
+ "_repliedToMessageID"
+ "_restorePreviousConfigurationWithError:"
+ "_selfParticipantID"
+ "_selfParticipantIDs"
+ "_senderParticipantID"
+ "_server"
+ "_sizeInCloud"
+ "_transferResourceResult"
+ "_usbController"
+ "activationSemaphore"
+ "add()"
+ "addedIterator"
+ "allowDefaultModeWithError:"
+ "appStoreApiHost"
+ "appStoreApiPathPrefix"
+ "app_name"
+ "apple/expired-message"
+ "archive_format"
+ "attemptNCMFallback(capability:)"
+ "beginUpdates"
+ "ble_used"
+ "cStringUsingEncoding:"
+ "children"
+ "choices"
+ "className"
+ "cleanBluetooth()"
+ "client accessed before run()"
+ "com.apple.HPMInterface"
+ "com.apple.MigrationKit-dev"
+ "com.apple.USBDevice"
+ "com.apple.massStorage.crossPlatformTransfer_DataTransfer"
+ "com.apple.massStorage.crossPlatformTransfer_DataTransfer_3p"
+ "complete()"
+ "configureNCMWithCompletion:"
+ "constraintGreaterThanOrEqualToAnchor:constant:"
+ "constraintLessThanOrEqualToAnchor:constant:"
+ "consumeMultipart(response:start:)"
+ "consumeSinglePart(response:start:)"
+ "contact with photo: %s"
+ "converted a participant. seq_i=%lld, uncanonicalized_uri=%s, service_name=%s"
+ "currentState"
+ "dataClassToProperties"
+ "data_class"
+ "deleteRowsAtIndexPaths:withRowAnimation:"
+ "deviceMonitor"
+ "dictionaryWithObjectsAndKeys:"
+ "didEstimateWithSelection:bytesOnDisk:bytesInCloud:items:"
+ "didTransfer result: %{public}s"
+ "didTransferWithResult:"
+ "directory_count"
+ "doAsMobile(_:)"
+ "enableLocalFilesDefaultsOverride"
+ "enableNCM()"
+ "endUpdates"
+ "estimated. message_count=%llu, conversation_count=%llu, participants_count=%llu, attachment_count=%llu, attachment_on_disk_size=%llu, attachment_in_cloud_size=%llu"
+ "estimated. selection=%hhu, bytes_on_disk=%llu, bytes_in_cloud=%llu items=%llu"
+ "export files for "
+ "failed ingesting part "
+ "failed to parse self participant %s error %@, will use empty participant"
+ "finished waiting for eSIM. sim_set=true"
+ "firstDescendantOfClass:"
+ "forServiceMatching:"
+ "forServicesMatching:"
+ "forceDeviceModeWithCompletion:"
+ "hpmInterface"
+ "imageDataAvailable"
+ "includeAttachmentsSince"
+ "infra_wifi_used"
+ "init(result:)"
+ "initInternal"
+ "initWithIterator:"
+ "initWithObject:"
+ "initWithUnownedObject:"
+ "insertRowsAtIndexPaths:withRowAnimation:"
+ "isFailed"
+ "isLastSubOption"
+ "is_failed"
+ "lastSelectedMessageOption"
+ "migration_mode"
+ "nan_used"
+ "networkLost(_:_:)"
+ "next"
+ "no photo for contact: %s"
+ "nonStandardContentType"
+ "non_standard_content_type"
+ "notifyPort"
+ "object"
+ "pauseBackgroundActivity()"
+ "peekMultipartResponse(response:method:path:summary:)"
+ "peerSupportedSelections()"
+ "peer_brand"
+ "peer_locale"
+ "peer_model"
+ "peer_os_version"
+ "pendingInterruption"
+ "populate data class entry for "
+ "populateDataclassProperties(dataClass:)"
+ "preflightSelection(selections:)"
+ "propertyForKey:"
+ "radioCheckButton"
+ "reloadRowsAtIndexPaths:withRowAnimation:"
+ "remove(cancelled:)"
+ "removedIterator"
+ "response is empty, returning 204 No Content, "
+ "restorePreviousConfigurationWithCompletion:"
+ "result"
+ "resumeBackgroundActivity()"
+ "retainedSelf"
+ "run(scheme:)"
+ "runLoopSource"
+ "selfParticipantIDs"
+ "self_participant_ids"
+ "send(data:)"
+ "sendNotification(data:)"
+ "server accessed before run()"
+ "server did shutdown. had_sim=%{bool}d"
+ "server shut down while sim was set — dispatching disconnected error"
+ "session_id"
+ "setIsFailed:"
+ "setSeparatorInset:"
+ "shutdown(state:error:notify:updateState:)"
+ "size_in_cloud"
+ "startMonitoring()"
+ "stop(cancelled:)"
+ "stringWithCString:encoding:"
+ "supportedSelections()"
+ "symlink_count"
+ "target dev properties %s"
+ "telemetry_id"
+ "telemetry_type"
+ "terminateDataSession:completionHandler:"
+ "transferResourceResults"
+ "updated %{public}s. checked=%{bool}d"
+ "usbController"
+ "usb_ncm_used"
+ "v24@0:8@\"MKTransferResult\"16"
+ "v44@0:8C16Q20Q28Q36"
+ "valueForKey:"
+ "waitForActivation()"
+ "will create a conversation. id=%s, service_type=%s, group_id=%s, group_name=%s, rcs_group_id=%s, rcs_group_uri=%s, is_pinned=%{bool}d, participants=%s, accountParticipant=%s"
+ "writeHeaders(connection:response:method:path:summary:)"
+ "writeNonEmptyResponse(connection:response:firstPart:iterator:method:path:summary:)"
+ "⎩  did %{public}s"
+ "⏻ shutting down in non-failure/non-success state: "
+ "💥 Received daemon interruption while in \""
- "  [%{public}ld] %{public}s: %{public}s"
- "  interface: %s, type: %s, name: %s"
- " download directory"
- "%{public}s %{public}s did write a body. bytes=%{public}ld"
- "%{public}s %{public}s did write a response. bytes=%ld"
- "%{public}s %{public}s did write headers. bytes=%{public}ld"
- "%{public}s %{public}s parts sent: %{public}ld"
- "%{public}s %{public}s response is empty, returning 204 No Content"
- "@?"
- "@?16@0:8"
- "B24@0:8@?16"
- "Cannot convert selection type "
- "Client is not initialized"
- "Comma-separated list of data classes to force support of FCI-only file transfers"
- "Comma-separated list of data classes to force support of legacy-only file transfers"
- "Config disabled export for %{public}s"
- "Config disabled import for %{public}s"
- "Data transfer took"
- "DataRole"
- "Device"
- "Disassociated from network"
- "Discovering NCM interface..."
- "ESIM transfer took"
- "Enables dumping of serialized and deserialized protobuf messages to disk for debugging"
- "Error fetching all contact IDs"
- "Expected a %s %s but found %s: %s stored value"
- "Failed to convert "
- "Failed to convert data class to selection"
- "Failed to create proto dumper"
- "Failed to create selection from entitlement %s for %s"
- "Failed to disable USB device mode and restore configuration"
- "Failed to enable USB device mode and NCM"
- "Failed to enable USB device mode and NCM configuration"
- "Failed to enable USB device mode and configure NCM"
- "Failed to export voice memo: %@"
- "Failed to get default account for service %{public}s"
- "Failed to get estimation for entry"
- "Failed to process request: path="
- "Failed to send OSMigration Event Payload to CoreAnalytics"
- "Failed to start USB state monitoring"
- "Failed to write dump file %s: %@"
- "File Content Depot"
- "Force enables TTRs"
- "Force failing attestation without contacting service"
- "Force passing attestation without contacting service"
- "Host"
- "IOGeneralInterest"
- "IOServiceMatched"
- "If enabled, data used to compute transfer rate and ETA will be stored for debugging purposes."
- "If enabled, skips ASC mapping. To export, mapping details must be provided in app Info.plist. For import, this implicitly trusts the bundleID from `targetPlatformIdentifiers` exported by Android."
- "If enabled, the implicit data classes can be individually selected/deselected for debugging purposes."
- "MKMigratorContext"
- "MKResourceContext"
- "MKUSBMonitoringState"
- "MKUSBRoleSwap"
- "Manual override disabled export for %{public}s"
- "Manual override disabled import for %{public}s"
- "MigrationKit/DataClassEntry+Additions.swift"
- "MigrationKit/DataClassResult+Additions.swift"
- "MigrationKit/ImportResult.swift"
- "MigrationKit/OSMigrationAnalytics.swift"
- "MigrationKit/OSMigrationPayload.swift"
- "MigrationKit/WaitExportViewController.swift"
- "MigrationKit/WaitImportViewController.swift"
- "Missing error signature"
- "NCM activated successfully"
- "NCM activation completed successfully"
- "NCM activation failed - continuing without NCM"
- "NCM activation wait timed out - continuing without NCM"
- "NCM interface discovery failed"
- "NCM interface is not up - cannot activate as current network"
- "NCM was not started"
- "NO"
- "Network connection lost"
- "No failure description"
- "None"
- "On the client, runs a speed test against the server, requesting chunks of this many MB of random data."
- "Populated data class entry for %{public}s in %{public}s; %s"
- "Prevents Google Play Integrity challenges from being sent to the Andata service"
- "Q20@0:8I16"
- "Received failure for file content part "
- "Result for AppContent context is .unknown"
- "Sending OSMigration Event Payload to CoreAnalytics: %s, eventName: %s"
- "Server acknowledged the ACK for %s"
- "Skipping import of network without password. ssid=%s %s"
- "Starting NCM monitoring"
- "Starting USB state monitoring..."
- "Static config disabled export for %{public}s"
- "Static config disabled import for %{public}s"
- "Stopped USB state monitoring"
- "Successfully disabled USB device mode and restored configuration"
- "Successfully enabled NCM as current network."
- "Successfully enabled USB device mode and NCM"
- "Successfully sent OSMigration Event Payload to CoreAnalytics"
- "Successfully started USB state monitoring"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_callbackQueue"
- "T@?,C,N,V_callback"
- "TI,N,V_interestNotifier"
- "TI,N,V_service"
- "TI,N,V_stateNotifier"
- "T^{IONotificationPort=},N,V_notificationPort"
- "Tearing down NCM network"
- "USB already configured"
- "USB connected - configuring device mode and NCM"
- "USB disconnected"
- "USB re-enumeration wait completed"
- "Unable to connect to daemon"
- "Unable to convert data class "
- "Waiting for USB re-enumeration to complete..."
- "Waiting up to %lld seconds for USB configuration"
- "Will delete existing %{public}s: %s"
- "Will import network. ssid=%s %s"
- "YES"
- "[Internal Only] skip button event is not implemented in the current view controller."
- "[MKUSBMonitoringState] Failed to register interest notification: 0x%x"
- "[MKUSBMonitoringState] Successfully registered interest notification"
- "[MKUSBMonitoringState] USB service matched - setting up interest notification"
- "[MKUSBMonitoringState] USB state check: DataRole=%d (%s), Connected=%s"
- "[MKUSBRoleSwap] Added AppleUSBNCMControl at interface index %d"
- "[MKUSBRoleSwap] Added AppleUSBNCMData at interface index %d"
- "[MKUSBRoleSwap] Adding NCM interfaces"
- "[MKUSBRoleSwap] Already in device mode, just configuring NCM"
- "[MKUSBRoleSwap] Brief delay between ForceUSBDeviceMode and NCM configuration"
- "[MKUSBRoleSwap] Brief delay between forceMode and ForceUSBDeviceMode"
- "[MKUSBRoleSwap] Callback cannot be nil"
- "[MKUSBRoleSwap] Calling ForceUSBDeviceMode to switch to device mode"
- "[MKUSBRoleSwap] Calling forceMode(device=0x%llx, enable=0) to replug USB port"
- "[MKUSBRoleSwap] Calling forceMode(device=0x%llx, enable=1) to unplug USB port"
- "[MKUSBRoleSwap] Cleaning up HPM interface (no role swap was performed)"
- "[MKUSBRoleSwap] Cleanup completed with some errors - check logs above"
- "[MKUSBRoleSwap] Cleanup: didPerformRoleSwap=%s, didConfigureNCM=%s"
- "[MKUSBRoleSwap] Configuring NCM interfaces"
- "[MKUSBRoleSwap] Currently in host mode, performing full PD role switch sequence"
- "[MKUSBRoleSwap] DataRole property not found in IOPortTransportStateUSB2 service"
- "[MKUSBRoleSwap] Failed to append AppleUSBNCMControl: %d"
- "[MKUSBRoleSwap] Failed to append AppleUSBNCMData: %d"
- "[MKUSBRoleSwap] Failed to configure NCM"
- "[MKUSBRoleSwap] Failed to create NCM description"
- "[MKUSBRoleSwap] Failed to create matching dictionary"
- "[MKUSBRoleSwap] Failed to create matching dictionary for IOPortTransportStateUSB2"
- "[MKUSBRoleSwap] Failed to create notification port"
- "[MKUSBRoleSwap] Failed to get HPM interface: 0x%x"
- "[MKUSBRoleSwap] Failed to get child iterator for AppleHPMARM: 0x%x"
- "[MKUSBRoleSwap] Failed to restore USB description: 0x%x"
- "[MKUSBRoleSwap] Failed to restore previous USB configuration"
- "[MKUSBRoleSwap] Failed to save previous USB description"
- "[MKUSBRoleSwap] Failed to trigger bus re-enumeration: 0x%x"
- "[MKUSBRoleSwap] ForceMode(enable=0) failed: 0x%x"
- "[MKUSBRoleSwap] ForceMode(enable=1) failed: 0x%x"
- "[MKUSBRoleSwap] ForceUSBDeviceMode(enable=0) failed: 0x%x"
- "[MKUSBRoleSwap] ForceUSBDeviceMode(enable=1) failed: 0x%x"
- "[MKUSBRoleSwap] Found device Address: 0x%llx"
- "[MKUSBRoleSwap] IOServiceAddMatchingNotification failed: 0x%x"
- "[MKUSBRoleSwap] IOServiceGetMatchingServices failed with error: 0x%x"
- "[MKUSBRoleSwap] IOServiceGetMatchingServices failed: 0x%x"
- "[MKUSBRoleSwap] IOUSBDeviceControllerCreate failed: 0x%x"
- "[MKUSBRoleSwap] IOUSBDeviceControllerGoOffAndOnBus failed: 0x%x"
- "[MKUSBRoleSwap] IOUSBDeviceControllerSetDescription failed: 0x%x"
- "[MKUSBRoleSwap] IOUSBDeviceDescriptionAppendConfiguration failed: %d"
- "[MKUSBRoleSwap] No IOPortTransportStateUSB2 service found"
- "[MKUSBRoleSwap] No previous USB configuration to restore"
- "[MKUSBRoleSwap] QueryInterface failed with result: 0x%x"
- "[MKUSBRoleSwap] Reconfiguring USB for NCM"
- "[MKUSBRoleSwap] Released AppleHPMLib interface"
- "[MKUSBRoleSwap] Restoring previous USB configuration"
- "[MKUSBRoleSwap] Saved previous USB description"
- "[MKUSBRoleSwap] Stopped USB state monitoring"
- "[MKUSBRoleSwap] Successfully configured NCM"
- "[MKUSBRoleSwap] Successfully configured USB for NCM"
- "[MKUSBRoleSwap] Successfully disabled ForceUSBDeviceMode (enable=0)"
- "[MKUSBRoleSwap] Successfully disabled USB device mode and restored USB configuration"
- "[MKUSBRoleSwap] Successfully enabled USB device mode and NCM"
- "[MKUSBRoleSwap] Successfully obtained AppleHPMLib interface"
- "[MKUSBRoleSwap] Successfully restored previous USB configuration"
- "[MKUSBRoleSwap] Successfully started USB state monitoring"
- "[MKUSBRoleSwap] USB connection check: DataRole=%d (%s), Connected=%s"
- "[MKUSBRoleSwap] USB monitoring is already active"
- "^{IONotificationPort=}"
- "^{IONotificationPort=}16@0:8"
- "_TtC12MigrationKit11ClientProxy"
- "_TtC12MigrationKit11ServerProxy"
- "_TtC12MigrationKit15EsimOnlyPayload"
- "_TtC12MigrationKit17EsimOnlyAnalytics"
- "_TtC12MigrationKit18OSMigrationPayload"
- "_TtC12MigrationKit20OSMigrationAnalytics"
- "_TtC12MigrationKit23FullDataTransferPayload"
- "_TtC12MigrationKit25FullDataTransferAnalytics"
- "_TtC12MigrationKit28OSMigrationAppContentPayload"
- "_callback"
- "_callbackQueue"
- "_compressedSize"
- "_compressionScheme"
- "_interestNotifier"
- "_notificationPort"
- "_resourceContext"
- "_stateNotifier"
- "_transferType"
- "account is required"
- "asMigratorContext()"
- "attestationForceSkipService"
- "bringUp()"
- "browser received .cancelled state."
- "browser received .failed state"
- "browser received .ready state."
- "browser received .setup state."
- "browser received .waiting state"
- "browser received an unexpected state."
- "callback"
- "callbackQueue"
- "checkAndInvokeCallbackForService:"
- "com.apple.MigrationKit.MKUSBRoleSwap"
- "com.apple.MigrationKit.NCM"
- "com.apple.MigrationKit.NCMNetwork.waiters"
- "com.apple.MigrationKit.USBStateMonitor"
- "configureNCM"
- "consumeMultipart(response:)"
- "consumeSinglePart(response:)"
- "contexts"
- "converted a participant. seq_i=%lld, uncanonicalized_uri=%s, service_name=%s, country_code=%s"
- "could not find any usb ncm interface."
- "createSymbolicLinkAtURL:withDestinationURL:error:"
- "destroyHPMLibInterface:"
- "didEstimateWithSelection:bytes:items:"
- "didTransfer context: %{public}s"
- "didTransferWithContext:"
- "disableDeviceModeAndNCM"
- "disassociateWithReason:"
- "enableDeviceModeAndNCM"
- "enableETADiagnostics"
- "estimated. message_count=%llu, conversation_count=%llu, participants_count=%llu, attachment_count=%llu, attachment_size=%llu"
- "estimated. selection=%hhu, bytes=%llu, items=%llu"
- "eventName"
- "exporting files for "
- "failed to establish xpc"
- "featurePayloads"
- "finished waiting for eSIM"
- "found a service. name=%s, type=%s, domain=%s), interfaces=%s"
- "found usb ncm interface. interface=%s"
- "getCurrentUSBDataRole"
- "getDeviceAddressFromHPMService:"
- "getHPMLibInterface:"
- "handleServiceMatched:"
- "i24@0:8^^^{AppleHPMLibInterfaceStructV3}16"
- "init(context:)"
- "init(conversation:participants:message:)"
- "init(dataClass:)"
- "initialSSID"
- "interestNotifier"
- "interruptionHandler"
- "isActive"
- "isMonitoring"
- "isUSBConnected"
- "massStorage.crossPlatformTransfer_DataTransfer"
- "massStorage.crossPlatformTransfer_DataTransfer_3p"
- "migrationd-protodump"
- "ncmNetwork"
- "ncmTask"
- "notificationPort"
- "overrideFCIOnlySupportedDataClasses"
- "overrideFCIUnsupportedDataClasses"
- "peekMultipartResponse(response:method:path:)"
- "peerSelections"
- "populateDataclassProperties(selection:)"
- "received a code from Settings and will connect soon"
- "resourceContexts"
- "restorePreviousUSBConfiguration"
- "selection"
- "selectionToProperties"
- "server did shutdown"
- "setCallback:"
- "setCallbackQueue:"
- "setInterestNotifier:"
- "setNotificationPort:"
- "setStateNotifier:"
- "setUSBDeviceModeAndNCM:error:"
- "skip"
- "startMonitoringUSBStateWithCallback:"
- "stateNotifier"
- "stopMonitoringUSBState"
- "tapToRadarForceEnable"
- "toContext()"
- "toEstimation()"
- "updated %{public}s. selected=%{bool}d"
- "usbConfigurationWaiters"
- "usbConfigured"
- "v20@0:8I16"
- "v24@0:8@\"MKMigratorContext\"16"
- "v24@0:8^{IONotificationPort=}16"
- "v36@0:8C16Q20Q28"
- "waitForNCMActivation(timeout:)"
- "waiterQueue"
- "will create a conversation. account=%s, id=%s, service_type=%s, group_id=%s, group_name=%s, rcs_group_id=%s, rcs_group_uri=%s, is_pinned=%{bool}d, participants=%s"
- "writeHeaders(connection:response:method:path:)"
- "writeNonEmptyResponse(connection:response:firstPart:iterator:method:path:)"
- "⎩  did %{public}s in %{public}s"
- "⏻ shutting down"
- "💥 connection to migrationd interrupted, sending disconnect to UI"

```
