## DeviceCheckInternal

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/DeviceCheckInternal`

```diff

-  __TEXT.__text: 0x15f70
+  __TEXT.__text: 0x15b60
   __TEXT.__objc_methlist: 0x6ec
   __TEXT.__const: 0xbcf3
   __TEXT.__cstring: 0xd12
   __TEXT.__oslogstring: 0x136e
   __TEXT.__gcc_except_tab: 0x218
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__unwind_info: 0x428
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x1038
   __AUTH_CONST.__auth_got: 0x490
-  __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x208
-  __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__objc_data: 0x4b0
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __DATA.__data : content changed
Symbols:
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_36
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_42
Functions:
~ -[DCUAFDeviceCheckAsset initWithFilePath:] : 368 -> 356
~ ___23+[DCTaskCreator create]_block_invoke : 1048 -> 1012
~ ___23+[DCTaskCreator create]_block_invoke.24 : 580 -> 556
~ -[DCUAFAssetManager subscribeWithCompletion:] : 836 -> 824
~ ___45-[DCUAFAssetManager subscribeWithCompletion:]_block_invoke : 516 -> 504
~ -[DCUAFAssetManager subscribed] : 888 -> 864
~ ___47-[DCUAFAssetManager unsubscribeWithCompletion:]_block_invoke : 732 -> 708
~ ___41-[DCUAFAssetManager fetchWithCompletion:]_block_invoke : 1488 -> 1440
~ -[DCBAASigner signatureForData:completion:] : 752 -> 728
~ ___43-[DCBAASigner signatureForData:completion:]_block_invoke : 1300 -> 1264
~ -[DCBAASigner signaturesForData:completion:] : 720 -> 696
~ ___44-[DCBAASigner signaturesForData:completion:]_block_invoke : 1952 -> 1904
~ ___44-[DCBAASigner signaturesForData:completion:]_block_invoke.6 : 872 -> 836
~ -[DCBAASigner _signatureForData:withReferenceKey:error:] : 796 -> 772
~ -[DCBAASigner _attestationWithCertificates:error:] : 1216 -> 1180
~ -[DCEncryptionKeyAsset fetchEncryptionKey] : 1188 -> 1140
~ +[DCCryptoUtilities identityCertificateOptions] : 760 -> 748
~ -[DCCryptoProxyImpl fetchOpaqueBlobWithContext:completion:] : 428 -> 416
~ -[DCCryptoProxyImpl baaSignatureForData:completion:] : 296 -> 284
~ -[DCCryptoProxyImpl baaSignaturesForData:completion:] : 296 -> 284
~ ___37-[DCCryptoProxyImpl _fetchPublicKey:]_block_invoke : 916 -> 880
~ ___36-[DCCryptoProxyImpl fetchAssetInfo:]_block_invoke : 536 -> 512
~ -[NSData(Signing) dc_compressedData:] : 764 -> 728
~ -[DCBGSTaskController registerForTask:] : 600 -> 588
~ ___39-[DCBGSTaskController registerForTask:]_block_invoke : 520 -> 508
~ ___39-[DCBGSTaskController registerForTask:]_block_invoke.9 : 320 -> 308
~ -[DCBGSTaskController updateTaskWithIdentifier:withRefreshInterval:] : 1900 -> 1828
~ -[DCBGSTaskController observeValueForKeyPath:ofObject:change:context:] : 572 -> 560
~ -[DCBGSTaskController handleTask:shouldExit:] : 676 -> 664
~ -[DCCertificateGenerator generateCertificateChainWithCompletion:] : 520 -> 508
~ ___65-[DCCertificateGenerator generateCertificateChainWithCompletion:]_block_invoke : 776 -> 740
~ ___65-[DCCertificateGenerator generateCertificateChainWithCompletion:]_block_invoke.6 : 548 -> 524
~ -[DCCertificateGenerator createPEMCertificateChainFrom:completion:] : 2988 -> 2916
~ -[DCCertificateGenerator parseDERCertificatesFromChain:] : 756 -> 732
~ -[DCCertificateGenerator encryptData:serverSyncedDate:error:] : 2824 -> 2728
~ _decompressECPublicKey : 424 -> 416
~ _CTGetICDPFederationType : 316 -> 288
~ _X509ChainCheckPathWithOptions : 1580 -> 1584

```
