## CoreRepairLite

> `/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite`

```diff

-921.120.4.0.0
-  __TEXT.__text: 0xb3a8
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x328
+1291.0.0.502.1
+  __TEXT.__text: 0xbe48
+  __TEXT.__objc_methlist: 0x3b0
   __TEXT.__const: 0xc3
-  __TEXT.__oslogstring: 0x17da
   __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__cstring: 0x54a
-  __TEXT.__unwind_info: 0x1c0
-  __TEXT.__objc_classname: 0x49
-  __TEXT.__objc_methname: 0xb42
-  __TEXT.__objc_methtype: 0x1d7
-  __TEXT.__objc_stubs: 0xc60
-  __DATA_CONST.__got: 0x100
+  __TEXT.__cstring: 0x549
+  __TEXT.__oslogstring: 0x18c8
+  __TEXT.__unwind_info: 0x1f8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c0
+  __DATA_CONST.__objc_selrefs: 0x428
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x390
+  __DATA_CONST.__objc_arraydata: 0x98
+  __DATA_CONST.__got: 0x118
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x920
-  __AUTH_CONST.__objc_const: 0x2b0
+  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__objc_const: 0x2f0
   __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__auth_got: 0x3c8
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0xc
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport
+  - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EE74F0B5-DF24-3286-A093-6B8ED1AD7273
-  Functions: 216
-  Symbols:   782
-  CStrings:  500
+  UUID: 58E1A904-2932-3247-9D68-1B62A8446B73
+  Functions: 224
+  Symbols:   164
+  CStrings:  338
 
Symbols:
+ _AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo
+ _AMFDRSealingManifestCopyMultiInstanceAndInfoForClass
+ _AMFDRSealingMapCopyDataClassesInstancesAndInfo
+ _AMFDRSealingMapCopyMultiInstanceAndInfoForClass
+ _OBJC_CLASS_$_CRDeviceMap
+ _kAMFDRSealingMapInfoQueryAttribute
+ _kAMFDRSealingMapInfoQueryComponentType
+ _kAMFDRSealingMapInfoQueryOptionDataClassOnly
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- +[CRAuthRepairInspector _getStatus]
- +[CRAuthRepairInspector getStatus]
- +[CRAuthRepairInspector wasRepaired:]
- +[CRFDRRetryController sharedInstance]
- +[CRFDRRetryController sharedInstance].cold.1
- +[CRFDRUtils _compareSealedAndLiveDataClasses:instances:liveClasses:liveInstances:results:]
- +[CRFDRUtils _compareSealedAndLiveDataClasses:instances:liveClasses:liveInstances:results:].cold.1
- +[CRFDRUtils _compareSerialNumberProperties:missingLiveData:results:]
- +[CRFDRUtils _compareSerialNumberProperties:missingLiveData:results:].cold.1
- +[CRFDRUtils _createFDRLocal]
- +[CRFDRUtils _getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:]
- +[CRFDRUtils _getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:].cold.1
- +[CRFDRUtils _getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:].cold.2
- +[CRFDRUtils _getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:].cold.3
- +[CRFDRUtils _getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:].cold.4
- +[CRFDRUtils _getAllSealedDataAndPropertiesFromManifest:properties:classes:instances:error:]
- +[CRFDRUtils _getAllSealedDataAndPropertiesFromManifest:properties:classes:instances:error:].cold.1
- +[CRFDRUtils _getDataClassesFromSealingManifest]
- +[CRFDRUtils _getDataClassesFromSealingManifest].cold.1
- +[CRFDRUtils _getDataClassesFromSealingManifest].cold.2
- +[CRFDRUtils _getDataClassesFromSealingManifest].cold.3
- +[CRFDRUtils _getDataClassesFromSealingMap]
- +[CRFDRUtils _getDataClassesFromSealingMap].cold.1
- +[CRFDRUtils _getDataClassesFromSealingMap].cold.2
- +[CRFDRUtils _getManifestForDataClass:]
- +[CRFDRUtils _getManifestForDataClass:].cold.1
- +[CRFDRUtils _getManifestForDataClass:].cold.2
- +[CRFDRUtils _getManifestForDataClass:].cold.3
- +[CRFDRUtils _getMesaState]
- +[CRFDRUtils _getPropertiesFromSealingMap]
- +[CRFDRUtils _getPropertiesFromSealingMap].cold.1
- +[CRFDRUtils _getPropertiesFromSealingMap].cold.2
- +[CRFDRUtils _getUnsealedMesaData:mesaState:]
- +[CRFDRUtils _getUnsealedMesaData:mesaState:].cold.1
- +[CRFDRUtils _getUnsealedMesaData:mesaState:].cold.2
- +[CRFDRUtils extractComponentsAndIdentifiers:]
- +[CRFDRUtils findUnsealedDataWithError:]
- +[CRFDRUtils findUnsealedDataWithError:].cold.1
- +[CRFDRUtils findUnsealedDataWithKey:error:]
- +[CRFDRUtils findUnsealedDataWithKey:error:].cold.1
- +[CRFDRUtils findUnsealedDataWithKey:error:].cold.2
- +[CRFDRUtils findUnsealedDataWithKey:error:].cold.3
- +[CRFDRUtils findUnsealedDataWithKey:error:].cold.4
- +[CRFDRUtils getData:instance:]
- +[CRFDRUtils getData:instance:].cold.1
- +[CRFDRUtils getData:instance:].cold.2
- +[CRFDRUtils getDataPayload:instance:]
- +[CRFDRUtils getDataPayload:instance:].cold.1
- +[CRFDRUtils getDataPayload:instance:].cold.2
- +[CRFDRUtils getDataPayload:instance:].cold.3
- +[CRFDRUtils getDataPayloadDictWithClass:instance:]
- +[CRFDRUtils getDataPayloadDictWithClass:instance:].cold.1
- +[CRFDRUtils getLocalSealingManifestWithError:]
- +[CRFDRUtils getLocalSealingManifestWithError:].cold.1
- +[CRFDRUtils getLocalSealingManifest]
- +[CRFDRUtils getMacSupportedSPCs]
- +[CRFDRUtils getSealedInstancesWithClass:error:]
- +[CRFDRUtils getSealedInstancesWithClass:error:].cold.1
- +[CRFDRUtils getStringFromCert:WithTag:AndOID:]
- +[CRFDRUtils isDataClassSupported:]
- +[CRFDRUtils isDcSignedCombinedDataClass:error:]
- +[CRFDRUtils isDcSignedCombinedDataClass:error:].cold.1
- +[CRFDRUtils isDcSignedDataClass:instance:error:]
- +[CRFDRUtils isDcSignedDataClass:instance:error:].cold.1
- +[CRFDRUtils isDcSignedSealingManifest:]
- +[CRFDRUtils isDcSignedSealingManifest:].cold.1
- +[CRFDRUtils isPrimaryDataClassSupported:]
- +[CRFDRUtils isPropertySupported:]
- +[CRFDRUtils isRepairASIDSupported]
- +[CRFDRUtils isRepairASIDSupported].cold.1
- +[CRFDRUtils isRepairASIDSupported].cold.2
- +[CRFDRUtils isRepairASIDSupported].cold.3
- +[CRFDRUtils isServicePartWithError:]
- +[CRFDRUtils isServicePartWithError:].cold.1
- +[CRFDRUtils isServicePartWithError:].cold.2
- +[CRFDRUtils isServicePartWithError:].cold.3
- +[CRFDRUtils localManifestProperties]
- +[CRFDRUtils localManifestProperties].cold.1
- +[CRFDRUtils localManifestProperties].cold.2
- +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:]
- +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:].cold.1
- +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:].cold.2
- +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:].cold.3
- +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:].cold.4
- +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:].cold.5
- +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:].cold.6
- -[CREANController .cxx_destruct]
- -[CREANController _apticketCopyDataObjectPropertyWithTag:property:]
- -[CREANController _apticketCopyDataObjectPropertyWithTag:property:].cold.1
- -[CREANController _apticketCopyDataObjectPropertyWithTag:property:].cold.2
- -[CREANController _apticketCopyDataObjectPropertyWithTag:property:].cold.3
- -[CREANController _getDataClassesToWrite]
- -[CREANController _getDataClassesToWrite].cold.1
- -[CREANController _getDataClassesToWrite].cold.2
- -[CREANController _getQuerykeyFromDataClass:]
- -[CREANController _getQuerykeyFromDataClass:].cold.1
- -[CREANController _ticketCopyHashDataWithNode:]
- -[CREANController _ticketCopyHashDataWithNode:].cold.1
- -[CREANController _ticketCopyHashDataWithNode:].cold.2
- -[CREANController _ticketCopyHashDataWithNode:].cold.3
- -[CREANController _writeDataToEAN:withKey:]
- -[CREANController _writeDataToEAN:withKey:].cold.1
- -[CREANController _writeDataToEAN:withKey:].cold.2
- -[CREANController _writeDataToEAN:withKey:].cold.3
- -[CREANController _writeDataToEAN:withKey:].cold.4
- -[CREANController _writeDataToEAN:withKey:].cold.5
- -[CREANController _writeDataToEAN:withKey:].cold.6
- -[CREANController _writeDataToEAN:withKey:].cold.7
- -[CREANController apticketCopyHashData]
- -[CREANController apticketCopyHashData].cold.1
- -[CREANController apticketCopyHashData].cold.2
- -[CREANController calculateDerLength:actualSize:]
- -[CREANController calculateDerLength:actualSize:].cold.1
- -[CREANController copyCurrentFDREANValuesWithdataDir:error:]
- -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.1
- -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.2
- -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.3
- -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.4
- -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.5
- -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.6
- -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.7
- -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.8
- -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:]
- -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.1
- -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.2
- -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.3
- -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.4
- -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.5
- -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.6
- -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.7
- -[CREANController copyStagedFDREanDataWithdataDir:error:]
- -[CREANController copyStagedFDREanDataWithdataDir:error:].cold.1
- -[CREANController copyStagedFDREanDataWithdataDir:error:].cold.2
- -[CREANController copyStagedFDREanDataWithdataDir:error:].cold.3
- -[CREANController deleteFDRDataFromEANWithDataClass:]
- -[CREANController deleteFDRDataFromEANWithDataClass:].cold.1
- -[CREANController deleteFDRDataFromEANWithDataClass:].cold.2
- -[CREANController deleteFDRDataFromEANWithDataClass:].cold.3
- -[CREANController deleteFDRDataFromEANWithDataClass:].cold.4
- -[CREANController deleteFDRDataFromEANWithDataClass:].cold.5
- -[CREANController isEANSupported]
- -[CREANController isEANSupported].cold.1
- -[CREANController nextEANGenerationCount]
- -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:]
- -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.1
- -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.2
- -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.3
- -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.4
- -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.5
- -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.6
- -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.7
- -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.8
- -[CREANController setupVersionedFDRWithApTicket:]
- -[CREANController setupVersionedFDRWithApTicket:].cold.1
- -[CREANController setupVersionedFDRWithApTicket:].cold.2
- -[CREANController setupVersionedFDRWithApTicket:].cold.3
- -[CREANController setupVersionedFDRWithApTicket:].cold.4
- -[CREANController setupVersionedFDRWithApTicket:].cold.5
- -[CREANController sizeEAN:]
- -[CREANController sizeEAN:].cold.1
- -[CREANController sizeEAN:].cold.2
- -[CREANController sizeEAN:].cold.3
- -[CREANController sizeEAN:].cold.4
- -[CREANController sizeEAN:].cold.5
- -[CREANController sizeEAN:].cold.6
- -[CREANController stageVersionedFDREANWithdataDir:error:]
- -[CREANController stageVersionedFDREANWithdataDir:error:].cold.1
- -[CREANController stageVersionedFDREANWithdataDir:error:].cold.2
- -[CREANController swapEAN:withKey:]
- -[CREANController swapEAN:withKey:].cold.1
- -[CREANController swapEAN:withKey:].cold.2
- -[CREANController swapEAN:withKey:].cold.3
- -[CREANController swapEAN:withKey:].cold.4
- -[CREANController swapEAN:withKey:].cold.5
- -[CREANController swapEAN:withKey:].cold.6
- -[CREANController swapEAN:withKey:].cold.7
- -[CREANController swapEAN:withKey:].cold.8
- -[CREANController swapVersionedFDR]
- -[CREANController swapVersionedFDR].cold.1
- -[CREANController swapVersionedFDR].cold.2
- -[CREANController verifyFDRDataFromEANUsingCache:cachedData:]
- -[CREANController verifyFDRDataFromEANUsingCache:cachedData:].cold.1
- -[CREANController verifyFDRDataFromEANUsingCache:cachedData:].cold.2
- -[CREANController verifyFDRDataFromEANUsingCache:cachedData:].cold.3
- -[CREANController verifyFDRDataFromEANUsingCache:cachedData:].cold.4
- -[CREANController verifyFDRDataFromEANUsingCache:cachedData:].cold.5
- -[CREANController writeEAN:isImg4:]
- -[CREANController writeEAN:isImg4:].cold.1
- -[CREANController writeEAN:isImg4:].cold.2
- -[CREANController writeEAN:isImg4:].cold.3
- -[CREANController writeEAN:isImg4:].cold.4
- -[CREANController writeEAN:isImg4:].cold.5
- -[CREANController writeFDRDataToEANWithdataDir:]
- -[CREANController writeFDRDataToEANWithdataDir:].cold.1
- -[CREANController writeFDRDataToEANWithdataDir:].cold.2
- -[CREANController writeFDRDataToEANWithdataDir:].cold.3
- -[CRFDRRetryController .cxx_destruct]
- -[CRFDRRetryController disableRetry]
- -[CRFDRRetryController disableRetry].cold.1
- -[CRFDRRetryController enableRetry]
- -[CRFDRRetryController enableRetry].cold.1
- -[CRFDRRetryController enableRetry].cold.2
- -[CRFDRRetryController init]
- <redacted>
- GCC_except_table1
- _AMFDRSealingManifestCopyInstanceForClass
- _AMFDRSealingMapCopyDataClassesAndInstancesWithAttribute
- _CRErrorDomain
- _CoreRepairLiteVersionNumber
- _CoreRepairLiteVersionString
- _DERDecodeItemPartialBufferGetLength
- _DERDecodeSeqContentInit
- _DERDecodeSeqNext
- _OBJC_CLASS_$_CREANController
- _OBJC_CLASS_$_CRFDRRetryController
- _OBJC_CLASS_$_CRFDRUtils
- _OBJC_CLASS_$_NSRegularExpression
- _OBJC_IVAR_$_CREANController.apTicket
- _OBJC_IVAR_$_CRFDRRetryController._lock
- _OBJC_IVAR_$_CRFDRRetryController._refCount
- _OBJC_METACLASS_$_CREANController
- _OBJC_METACLASS_$_CRFDRRetryController
- _OBJC_METACLASS_$_CRFDRUtils
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __OBJC_$_CLASS_METHODS_CRAuthRepairInspector
- __OBJC_$_CLASS_METHODS_CRFDRRetryController
- __OBJC_$_CLASS_METHODS_CRFDRUtils
- __OBJC_$_INSTANCE_METHODS_CREANController
- __OBJC_$_INSTANCE_METHODS_CRFDRRetryController
- __OBJC_$_INSTANCE_VARIABLES_CREANController
- __OBJC_$_INSTANCE_VARIABLES_CRFDRRetryController
- __OBJC_CLASS_RO_$_CRAuthRepairInspector
- __OBJC_CLASS_RO_$_CREANController
- __OBJC_CLASS_RO_$_CRFDRRetryController
- __OBJC_CLASS_RO_$_CRFDRUtils
- __OBJC_METACLASS_RO_$_CRAuthRepairInspector
- __OBJC_METACLASS_RO_$_CREANController
- __OBJC_METACLASS_RO_$_CRFDRRetryController
- __OBJC_METACLASS_RO_$_CRFDRUtils
- ___34+[CRFDRUtils isPropertySupported:]_block_invoke
- ___35+[CRFDRUtils isDataClassSupported:]_block_invoke
- ___38+[CRFDRRetryController sharedInstance]_block_invoke
- ___48-[CREANController writeFDRDataToEANWithdataDir:]_block_invoke
- ___48-[CREANController writeFDRDataToEANWithdataDir:]_block_invoke.cold.1
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_48_e8_32s40r_e15_v32?0816^B24ls32l8r40l8
- ___block_literal_global
- ___handleForCategory_block_invoke
- _commonNameOIDBytes
- _handleForCategory
- _handleForCategory.cold.1
- _handleForCategory.logHandles
- _handleForCategory.onceToken
- _isDataClassSupported:.classes
- _isDataClassSupported:.onceToken
- _isPropertySupported:.onceToken
- _isPropertySupported:.properties
- _kAPTKFourCharCode
- _objc_msgSend$URLWithString:
- _objc_msgSend$UTF8String
- _objc_msgSend$_apticketCopyDataObjectPropertyWithTag:property:
- _objc_msgSend$_compareSealedAndLiveDataClasses:instances:liveClasses:liveInstances:results:
- _objc_msgSend$_compareSerialNumberProperties:missingLiveData:results:
- _objc_msgSend$_createFDRLocal
- _objc_msgSend$_getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:
- _objc_msgSend$_getAllSealedDataAndPropertiesFromManifest:properties:classes:instances:error:
- _objc_msgSend$_getDataClassesFromSealingMap
- _objc_msgSend$_getDataClassesToWrite
- _objc_msgSend$_getManifestForDataClass:
- _objc_msgSend$_getMesaState
- _objc_msgSend$_getPropertiesFromSealingMap
- _objc_msgSend$_getQuerykeyFromDataClass:
- _objc_msgSend$_getStatus
- _objc_msgSend$_getUnsealedMesaData:mesaState:
- _objc_msgSend$_ticketCopyHashDataWithNode:
- _objc_msgSend$_writeDataToEAN:withKey:
- _objc_msgSend$addEntriesFromDictionary:
- _objc_msgSend$addObject:
- _objc_msgSend$addObjectsFromArray:
- _objc_msgSend$allKeys
- _objc_msgSend$allObjects
- _objc_msgSend$appendBytes:length:
- _objc_msgSend$apticketCopyHashData
- _objc_msgSend$array
- _objc_msgSend$arrayWithObjects:count:
- _objc_msgSend$bytes
- _objc_msgSend$calculateDerLength:actualSize:
- _objc_msgSend$containsObject:
- _objc_msgSend$convertToHexString
- _objc_msgSend$copy
- _objc_msgSend$copyCurrentFDREANValuesWithdataDir:error:
- _objc_msgSend$copyFDREANValues:outgenerationCount:outManifesthash:
- _objc_msgSend$copyStagedFDREanDataWithdataDir:error:
- _objc_msgSend$count
- _objc_msgSend$countByEnumeratingWithState:objects:count:
- _objc_msgSend$dataWithBytes:length:
- _objc_msgSend$dataWithBytesNoCopy:length:
- _objc_msgSend$dataWithLength:
- _objc_msgSend$deleteFDRDataFromEANWithDataClass:
- _objc_msgSend$dictionary
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$disableRetry
- _objc_msgSend$enableRetry
- _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
- _objc_msgSend$errorWithDomain:code:userInfo:
- _objc_msgSend$filteredArrayUsingPredicate:
- _objc_msgSend$findUnsealedDataWithError:
- _objc_msgSend$firstMatchInString:options:range:
- _objc_msgSend$getData:instance:
- _objc_msgSend$getLocalSealingManifest
- _objc_msgSend$getLocalSealingManifestWithError:
- _objc_msgSend$getStringFromCert:WithTag:AndOID:
- _objc_msgSend$getValue:
- _objc_msgSend$initWithBytes:length:
- _objc_msgSend$initWithData:encoding:
- _objc_msgSend$initWithPattern:options:error:
- _objc_msgSend$isDataClassSupported:
- _objc_msgSend$isDcSignedSealingManifest:
- _objc_msgSend$isEANSupported
- _objc_msgSend$isEqual:
- _objc_msgSend$isEqualToData:
- _objc_msgSend$isEqualToString:
- _objc_msgSend$length
- _objc_msgSend$localManifestProperties
- _objc_msgSend$localizedDescription
- _objc_msgSend$lock
- _objc_msgSend$minusSet:
- _objc_msgSend$mutableBytes
- _objc_msgSend$mutableCopy
- _objc_msgSend$nextEANGenerationCount
- _objc_msgSend$numberOfRanges
- _objc_msgSend$numberWithInt:
- _objc_msgSend$objectAtIndex:
- _objc_msgSend$objectAtIndexedSubscript:
- _objc_msgSend$objectForKey:
- _objc_msgSend$objectForKeyedSubscript:
- _objc_msgSend$predicateWithFormat:
- _objc_msgSend$rangeAtIndex:
- _objc_msgSend$readFDRDataFromEANWithDataClass:outData:stripPadding:
- _objc_msgSend$removeObjectAtIndex:
- _objc_msgSend$set
- _objc_msgSend$setByAddingObject:
- _objc_msgSend$setData:
- _objc_msgSend$setObject:forKey:
- _objc_msgSend$setObject:forKeyedSubscript:
- _objc_msgSend$setWithArray:
- _objc_msgSend$sharedInstance
- _objc_msgSend$sizeEAN:
- _objc_msgSend$stringWithFormat:
- _objc_msgSend$subdataWithRange:
- _objc_msgSend$substringWithRange:
- _objc_msgSend$swapEAN:withKey:
- _objc_msgSend$swapVersionedFDR
- _objc_msgSend$unlock
- _objc_msgSend$valueWithBytes:objCType:
- _objc_msgSend$verifyFDRDataFromEANUsingCache:cachedData:
- _objc_msgSend$wasRepaired:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x28
- _sharedInstance.instance
- _sharedInstance.onceToken
CStrings:
+ "%@-%@"
+ "%@:%@"
+ "-"
+ "ComponentType/"
+ "DISPLAY"
+ "Data classes with type info: %@"
+ "Failed to get %@ data instance: %@"
+ "Invalid type info length in: %@"
+ "Invalid value type in dataClassesWithTypeInfo array: %@"
+ "Invalid value type in info dictionary: %@"
+ "LOGIC BOARD"
+ "No identifier found in: %@"
+ "No type info found in: %@"
+ "info: %@"
+ "missingDataIdentifiers"
- "([a-zA-Z0-9#]{4})-(.*$)"
- ".cxx_destruct"
- "@\"NSData\""
- "@\"NSLock\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8Q16Q24"
- "@48@0:8{?=**}16Q32@40"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B24@0:8^B16"
- "B28@0:8@16B24"
- "B28@0:8B16@20"
- "B28@0:8B16^@20"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8@16^Q24"
- "B36@0:8@16^@24B32"
- "B40@0:8@16@24^@32"
- "B40@0:8@16^I24^@32"
- "B56@0:8@16^@24^@32^@40^@48"
- "B56@0:8^@16^@24@32@40^@48"
- "CRAuthRepairInspector"
- "CREANController"
- "CRFDRRetryController"
- "CRFDRUtils"
- "CmCl"
- "I16@0:8"
- "I24@0:8@16"
- "LCfg"
- "NBCl"
- "PlCl"
- "Q16@0:8"
- "Q24@0:8@16"
- "TBCl"
- "URLWithString:"
- "UTF8String"
- "^{__AMFDR=}16@0:8"
- "_apticketCopyDataObjectPropertyWithTag:property:"
- "_compareSealedAndLiveDataClasses:instances:liveClasses:liveInstances:results:"
- "_compareSerialNumberProperties:missingLiveData:results:"
- "_createFDRLocal"
- "_getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:"
- "_getAllSealedDataAndPropertiesFromManifest:properties:classes:instances:error:"
- "_getDataClassesFromSealingManifest"
- "_getDataClassesFromSealingMap"
- "_getDataClassesToWrite"
- "_getManifestForDataClass:"
- "_getMesaState"
- "_getPropertiesFromSealingMap"
- "_getQuerykeyFromDataClass:"
- "_getStatus"
- "_getUnsealedMesaData:mesaState:"
- "_lock"
- "_refCount"
- "_ticketCopyHashDataWithNode:"
- "_writeDataToEAN:withKey:"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "allKeys"
- "allObjects"
- "apTicket"
- "appendBytes:length:"
- "apticketCopyHashData"
- "array"
- "arrayWithObjects:count:"
- "bcrt"
- "bytes"
- "calculateDerLength:actualSize:"
- "containsObject:"
- "convertToHexString"
- "copy"
- "copyCurrentFDREANValuesWithdataDir:error:"
- "copyFDREANValues:outgenerationCount:outManifesthash:"
- "copyStagedFDREanDataWithdataDir:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dCfg"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:"
- "dataWithLength:"
- "deleteFDRDataFromEANWithDataClass:"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "disableRetry"
- "enableRetry"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "extractComponentsAndIdentifiers:"
- "filteredArrayUsingPredicate:"
- "findUnsealedDataWithError:"
- "findUnsealedDataWithKey:error:"
- "firstMatchInString:options:range:"
- "getData:instance:"
- "getDataPayload:instance:"
- "getDataPayloadDictWithClass:instance:"
- "getLocalSealingManifest"
- "getLocalSealingManifestWithError:"
- "getMacSupportedSPCs"
- "getSealedInstancesWithClass:error:"
- "getStatus"
- "getStringFromCert:WithTag:AndOID:"
- "getValue:"
- "init"
- "initWithBytes:length:"
- "initWithData:encoding:"
- "initWithPattern:options:error:"
- "isDataClassSupported:"
- "isDcSignedCombinedDataClass:error:"
- "isDcSignedDataClass:instance:error:"
- "isDcSignedSealingManifest:"
- "isEANSupported"
- "isEqual:"
- "isEqualToData:"
- "isEqualToString:"
- "isPrimaryDataClassSupported:"
- "isPropertySupported:"
- "isRepairASIDSupported"
- "isServicePartWithError:"
- "length"
- "localManifestProperties"
- "localizedDescription"
- "lock"
- "minusSet:"
- "mutableBytes"
- "mutableCopy"
- "nextEANGenerationCount"
- "number of ranges:%lu"
- "numberOfRanges"
- "numberWithInt:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "predicateWithFormat:"
- "prpc"
- "q"
- "queryDeviceStagedSealedFromEAN:error:"
- "rangeAtIndex:"
- "readFDRDataFromEANWithDataClass:outData:stripPadding:"
- "removeObjectAtIndex:"
- "set"
- "setByAddingObject:"
- "setData:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setWithArray:"
- "setupVersionedFDRWithApTicket:"
- "sharedInstance"
- "sizeEAN:"
- "stageVersionedFDREANWithdataDir:error:"
- "stringWithFormat:"
- "subdataWithRange:"
- "substringWithRange:"
- "swapEAN:withKey:"
- "swapVersionedFDR"
- "tcrt"
- "unlock"
- "v16@0:8"
- "v40@0:8@16@24@32"
- "v56@0:8@16@24@32@40@48"
- "valueWithBytes:objCType:"
- "vcrt"
- "verifyFDRDataFromEANUsingCache:cachedData:"
- "wasRepaired:"
- "wcrt"
- "writeEAN:isImg4:"
- "writeFDRDataToEANWithdataDir:"

```
