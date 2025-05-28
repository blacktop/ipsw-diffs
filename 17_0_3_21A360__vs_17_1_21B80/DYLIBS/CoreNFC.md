## CoreNFC

> `/System/Library/Frameworks/CoreNFC.framework/CoreNFC`

```diff

-340.36.0.0.0
+341.9.0.0.0
   __TEXT.__text: 0x27f00
   __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_methlist: 0x1484

   __TEXT.__unwind_info: 0x880
   __TEXT.__objc_classname: 0x332
   __TEXT.__objc_methname: 0x34ea
-  __TEXT.__objc_methtype: 0x13b9
+  __TEXT.__objc_methtype: 0x13bf
   __TEXT.__objc_stubs: 0x2360
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x890
Symbols:
+ __OBJC_$_PROP_LIST_NFCFeliCaTag.154
+ __OBJC_$_PROP_LIST_NFCISO15693Tag.202
+ __OBJC_$_PROP_LIST_NFCMiFareTag.116
+ __OBJC_$_PROP_LIST_NFCNDEFTag.141
+ __OBJC_$_PROP_LIST_NFCReaderSession.315
+ __OBJC_$_PROP_LIST_NFCTag.206
+ ___101-[NFCISO15693Tag extendedGetMultipleBlockSecurityStatusWithRequestFlag:blockRange:completionHandler:]_block_invoke.46
+ ___102-[NFCISO15693Tag extendedWriteMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.42
+ ___102-[NFCISO15693Tag extendedWriteMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.43
+ ___102-[NFCISO15693Tag extendedWriteMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.44
+ ___102-[NFCISO15693Tag extendedWriteMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.45
+ ___107-[NFCISO15693Tag customCommandWithRequestFlag:customCommandCode:customRequestParameters:completionHandler:]_block_invoke.36
+ ___36-[NFCReaderSession setAlertMessage:]_block_invoke.12
+ ___43-[NFCReaderSession beginSessionWithConfig:]_block_invoke.54
+ ___47-[NFCTag queryNDEFStatusWithCompletionHandler:]_block_invoke.55
+ ___47-[NFCTag queryNDEFStatusWithCompletionHandler:]_block_invoke.56
+ ___47-[NFCTag queryNDEFStatusWithCompletionHandler:]_block_invoke_2.57
+ ___54-[NFCTagReaderSession connectToTag:completionHandler:]_block_invoke.24
+ ___54-[NFCTagReaderSession connectToTag:completionHandler:]_block_invoke.26
+ ___55-[NFCNDEFReaderSession connectToTag:completionHandler:]_block_invoke.83
+ ___58-[NFCFeliCaTag sendFeliCaCommandPacket:completionHandler:]_block_invoke.41
+ ___65-[NFCFeliCaTag requestServiceWithNodeCodeList:completionHandler:]_block_invoke.21
+ ___65-[NFCFeliCaTag requestServiceWithNodeCodeList:completionHandler:]_block_invoke.22
+ ___67-[NFCFeliCaTag requestServiceV2WithNodeCodeList:completionHandler:]_block_invoke.38
+ ___67-[NFCFeliCaTag requestServiceV2WithNodeCodeList:completionHandler:]_block_invoke.39
+ ___67-[NFCISO15693Tag _wtxRetryWithCommnand:maxRetry:completionHandler:]_block_invoke.48
+ ___77-[NFCFeliCaTag pollingWithSystemCode:requestCode:timeSlot:completionHandler:]_block_invoke.13
+ ___77-[NFCFeliCaTag pollingWithSystemCode:requestCode:timeSlot:completionHandler:]_block_invoke.15
+ ___82-[NFCISO15693Tag extendedLockBlockWithRequestFlags:blockNumber:completionHandler:]_block_invoke.40
+ ___82-[NFCISO15693Tag readMultipleBlocksWithRequestFlags:blockRange:completionHandler:]_block_invoke.23
+ ___85-[NFCFeliCaTag readWithoutEncryptionWithServiceCodeList:blockList:completionHandler:]_block_invoke.25
+ ___85-[NFCFeliCaTag readWithoutEncryptionWithServiceCodeList:blockList:completionHandler:]_block_invoke.26
+ ___85-[NFCFeliCaTag readWithoutEncryptionWithServiceCodeList:blockList:completionHandler:]_block_invoke.28
+ ___85-[NFCISO15693Tag fastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:]_block_invoke.34
+ ___85-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke.155
+ ___85-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke.156
+ ___85-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke.157
+ ___85-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke.159
+ ___88-[NFCISO15693Tag extendedReadSingleBlockWithRequestFlags:blockNumber:completionHandler:]_block_invoke.37
+ ___90-[NFCISO15693Tag extendedReadMultipleBlocksWithRequestFlags:blockRange:completionHandler:]_block_invoke.41
+ ___90-[NFCNDEFReaderSession didDetectNDEFMessages:fromTags:connectedTagIndex:updateUICallback:]_block_invoke.24
+ ___91-[NFCISO15693Tag writeSingleBlockWithRequestFlags:blockNumber:dataBlock:completionHandler:]_block_invoke.20
+ ___93-[NFCISO15693Tag extendedFastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:]_block_invoke.49
+ ___93-[NFCISO15693Tag getMultipleBlockSecurityStatusWithRequestFlag:blockRange:completionHandler:]_block_invoke.33
+ ___94-[NFCISO15693Tag writeMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.26
+ ___94-[NFCISO15693Tag writeMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.28
+ ___94-[NFCISO15693Tag writeMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.29
+ ___94-[NFCISO15693Tag writeMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.31
+ ___96-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke.29
+ ___96-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke.31
+ ___96-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke.33
+ ___96-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke.34
+ ___96-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke.35
+ ___96-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke.37
+ ___99-[NFCISO15693Tag extendedWriteSingleBlockWithRequestFlags:blockNumber:dataBlock:completionHandler:]_block_invoke.38
+ ___99-[NFCISO15693Tag extendedWriteSingleBlockWithRequestFlags:blockNumber:dataBlock:completionHandler:]_block_invoke.39
+ ___block_literal_global.66
+ _interface.interface.63
+ _interface.onceToken.64
- __OBJC_$_PROP_LIST_NFCFeliCaTag.144
- __OBJC_$_PROP_LIST_NFCISO15693Tag.192
- __OBJC_$_PROP_LIST_NFCMiFareTag.106
- __OBJC_$_PROP_LIST_NFCNDEFTag.129
- __OBJC_$_PROP_LIST_NFCReaderSession.303
- __OBJC_$_PROP_LIST_NFCTag.194
- ___101-[NFCISO15693Tag extendedGetMultipleBlockSecurityStatusWithRequestFlag:blockRange:completionHandler:]_block_invoke.36
- ___102-[NFCISO15693Tag extendedWriteMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.32
- ___102-[NFCISO15693Tag extendedWriteMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.33
- ___102-[NFCISO15693Tag extendedWriteMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.34
- ___102-[NFCISO15693Tag extendedWriteMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.35
- ___107-[NFCISO15693Tag customCommandWithRequestFlag:customCommandCode:customRequestParameters:completionHandler:]_block_invoke.26
- ___36-[NFCReaderSession setAlertMessage:]_block_invoke.2
- ___43-[NFCReaderSession beginSessionWithConfig:]_block_invoke.42
- ___47-[NFCTag queryNDEFStatusWithCompletionHandler:]_block_invoke.43
- ___47-[NFCTag queryNDEFStatusWithCompletionHandler:]_block_invoke.44
- ___47-[NFCTag queryNDEFStatusWithCompletionHandler:]_block_invoke_2.45
- ___54-[NFCTagReaderSession connectToTag:completionHandler:]_block_invoke.12
- ___54-[NFCTagReaderSession connectToTag:completionHandler:]_block_invoke.14
- ___55-[NFCNDEFReaderSession connectToTag:completionHandler:]_block_invoke.71
- ___58-[NFCFeliCaTag sendFeliCaCommandPacket:completionHandler:]_block_invoke.31
- ___65-[NFCFeliCaTag requestServiceWithNodeCodeList:completionHandler:]_block_invoke.11
- ___65-[NFCFeliCaTag requestServiceWithNodeCodeList:completionHandler:]_block_invoke.12
- ___67-[NFCFeliCaTag requestServiceV2WithNodeCodeList:completionHandler:]_block_invoke.28
- ___67-[NFCFeliCaTag requestServiceV2WithNodeCodeList:completionHandler:]_block_invoke.29
- ___67-[NFCISO15693Tag _wtxRetryWithCommnand:maxRetry:completionHandler:]_block_invoke.38
- ___77-[NFCFeliCaTag pollingWithSystemCode:requestCode:timeSlot:completionHandler:]_block_invoke.3
- ___77-[NFCFeliCaTag pollingWithSystemCode:requestCode:timeSlot:completionHandler:]_block_invoke.5
- ___82-[NFCISO15693Tag extendedLockBlockWithRequestFlags:blockNumber:completionHandler:]_block_invoke.30
- ___82-[NFCISO15693Tag readMultipleBlocksWithRequestFlags:blockRange:completionHandler:]_block_invoke.13
- ___85-[NFCFeliCaTag readWithoutEncryptionWithServiceCodeList:blockList:completionHandler:]_block_invoke.15
- ___85-[NFCFeliCaTag readWithoutEncryptionWithServiceCodeList:blockList:completionHandler:]_block_invoke.16
- ___85-[NFCFeliCaTag readWithoutEncryptionWithServiceCodeList:blockList:completionHandler:]_block_invoke.18
- ___85-[NFCISO15693Tag fastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:]_block_invoke.24
- ___85-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke.143
- ___85-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke.144
- ___85-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke.145
- ___85-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke.147
- ___88-[NFCISO15693Tag extendedReadSingleBlockWithRequestFlags:blockNumber:completionHandler:]_block_invoke.27
- ___90-[NFCISO15693Tag extendedReadMultipleBlocksWithRequestFlags:blockRange:completionHandler:]_block_invoke.31
- ___90-[NFCNDEFReaderSession didDetectNDEFMessages:fromTags:connectedTagIndex:updateUICallback:]_block_invoke.12
- ___91-[NFCISO15693Tag writeSingleBlockWithRequestFlags:blockNumber:dataBlock:completionHandler:]_block_invoke.10
- ___93-[NFCISO15693Tag extendedFastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:]_block_invoke.39
- ___93-[NFCISO15693Tag getMultipleBlockSecurityStatusWithRequestFlag:blockRange:completionHandler:]_block_invoke.23
- ___94-[NFCISO15693Tag writeMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.16
- ___94-[NFCISO15693Tag writeMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.18
- ___94-[NFCISO15693Tag writeMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.19
- ___94-[NFCISO15693Tag writeMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke.21
- ___96-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke.19
- ___96-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke.21
- ___96-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke.23
- ___96-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke.24
- ___96-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke.25
- ___96-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke.27
- ___99-[NFCISO15693Tag extendedWriteSingleBlockWithRequestFlags:blockNumber:dataBlock:completionHandler:]_block_invoke.28
- ___99-[NFCISO15693Tag extendedWriteSingleBlockWithRequestFlags:blockNumber:dataBlock:completionHandler:]_block_invoke.29
- ___block_literal_global.56
- _interface.interface.53
- _interface.onceToken.54
CStrings:
+ "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSData\"16"

```
