## DeviceCheckInternal

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/Versions/A/DeviceCheckInternal`

```diff

-  __TEXT.__text: 0x16aa8
+  __TEXT.__text: 0x1669c
   __TEXT.__objc_methlist: 0x6ec
   __TEXT.__const: 0xbd03
   __TEXT.__cstring: 0xe8e
   __TEXT.__oslogstring: 0x136e
-  __TEXT.__gcc_except_tab: 0x21c
-  __TEXT.__unwind_info: 0x440
+  __TEXT.__gcc_except_tab: 0x218
+  __TEXT.__unwind_info: 0x448
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x1038
   __AUTH_CONST.__auth_got: 0x3e0
-  __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x208
-  __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__objc_data: 0x4b0
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
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
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_37
Functions:
~ -[DCUAFDeviceCheckAsset initWithFilePath:] : 384 -> 372
~ ___23+[DCTaskCreator create]_block_invoke : 1088 -> 1052
~ __23+[DCTaskCreator create]_block_invoke.24 : 600 -> 576
~ -[DCUAFAssetManager subscribeWithCompletion:] : 904 -> 892
~ ___45-[DCUAFAssetManager subscribeWithCompletion:]_block_invoke : 544 -> 532
~ -[DCUAFAssetManager subscribed] : 936 -> 912
~ ___47-[DCUAFAssetManager unsubscribeWithCompletion:]_block_invoke : 768 -> 744
~ ___41-[DCUAFAssetManager fetchWithCompletion:]_block_invoke : 1560 -> 1512
~ -[DCBAASigner signatureForData:completion:] : 784 -> 760
~ ___43-[DCBAASigner signatureForData:completion:]_block_invoke : 1364 -> 1328
~ -[DCBAASigner signaturesForData:completion:] : 748 -> 724
~ ___44-[DCBAASigner signaturesForData:completion:]_block_invoke : 2052 -> 2004
~ __44-[DCBAASigner signaturesForData:completion:]_block_invoke.6 : 916 -> 880
~ -[DCBAASigner _signatureForData:withReferenceKey:error:] : 836 -> 812
~ -[DCBAASigner _attestationWithCertificates:error:] : 1284 -> 1248
~ -[DCEncryptionKeyAsset fetchEncryptionKey] : 1224 -> 1176
~ +[DCCryptoUtilities identityCertificateOptions] : 776 -> 764
~ -[DCCryptoProxyImpl fetchOpaqueBlobWithContext:completion:] : 460 -> 448
~ -[DCCryptoProxyImpl baaSignatureForData:completion:] : 316 -> 304
~ -[DCCryptoProxyImpl baaSignaturesForData:completion:] : 316 -> 304
~ ___37-[DCCryptoProxyImpl _fetchPublicKey:]_block_invoke : 952 -> 916
~ ___36-[DCCryptoProxyImpl fetchAssetInfo:]_block_invoke : 560 -> 536
~ -[NSData(Signing) dc_compressedData:] : 764 -> 728
~ -[DCBGSTaskController registerForTask:] : 644 -> 632
~ ___39-[DCBGSTaskController registerForTask:]_block_invoke : 536 -> 524
~ __39-[DCBGSTaskController registerForTask:]_block_invoke.9 : 332 -> 320
~ -[DCBGSTaskController updateTaskWithIdentifier:withRefreshInterval:] : 1988 -> 1916
~ -[DCBGSTaskController observeValueForKeyPath:ofObject:change:context:] : 632 -> 620
~ -[DCBGSTaskController handleTask:shouldExit:] : 712 -> 700
~ -[DCCertificateGenerator generateCertificateChainWithCompletion:] : 540 -> 528
~ ___65-[DCCertificateGenerator generateCertificateChainWithCompletion:]_block_invoke : 812 -> 776
~ __65-[DCCertificateGenerator generateCertificateChainWithCompletion:]_block_invoke.8 : 572 -> 548
~ -[DCCertificateGenerator createPEMCertificateChainFrom:completion:] : 3112 -> 3044
~ -[DCCertificateGenerator parseDERCertificatesFromChain:] : 772 -> 748
~ -[DCCertificateGenerator encryptData:serverSyncedDate:error:] : 2876 -> 2780
~ _OUTLINED_FUNCTION_16 -> _OUTLINED_FUNCTION_15 : 20 -> 48
~ _OUTLINED_FUNCTION_17 : 48 -> 20
~ _decompressECPublicKey : 424 -> 416
~ _CTGetICDPFederationType : 316 -> 288
~ _X509ChainCheckPathWithOptions : 1580 -> 1584
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheckInternal/Source/Core/Crypto/DCBAASigner.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheckInternal/Source/Core/Crypto/DCCertificateGenerator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheckInternal/Source/Core/Crypto/DCCryptoUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheckInternal/Source/Core/Crypto/NSData+Signing.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCEncryptionKeyAsset.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCUAFAssetManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCUAFDeviceCheckAsset.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheckInternal/Source/Interfaces/DCBGSTaskController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheckInternal/Source/Interfaces/DCCryptoProxyImpl.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheckInternal/Source/Interfaces/DCTaskCreator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheckInternal/Source/Core/Crypto/DCBAASigner.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheckInternal/Source/Core/Crypto/DCCertificateGenerator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheckInternal/Source/Core/Crypto/DCCryptoUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheckInternal/Source/Core/Crypto/NSData+Signing.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCEncryptionKeyAsset.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCUAFAssetManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCUAFDeviceCheckAsset.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheckInternal/Source/Interfaces/DCBGSTaskController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheckInternal/Source/Interfaces/DCCryptoProxyImpl.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheckInternal/Source/Interfaces/DCTaskCreator.m"

```
