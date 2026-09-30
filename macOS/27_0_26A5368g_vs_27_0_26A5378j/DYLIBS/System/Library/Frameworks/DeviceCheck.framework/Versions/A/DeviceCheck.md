## DeviceCheck

> `/System/Library/Frameworks/DeviceCheck.framework/Versions/A/DeviceCheck`

```diff

-  __TEXT.__text: 0xb9d4
+  __TEXT.__text: 0xb780
   __TEXT.__objc_methlist: 0x67c
   __TEXT.__const: 0xb0
   __TEXT.__cstring: 0xbd7

   __DATA_CONST.__objc_selrefs: 0x480
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__got: 0x150
   __AUTH_CONST.__const: 0x6a0
   __AUTH_CONST.__cfstring: 0x6a0
   __AUTH_CONST.__objc_const: 0xae0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x1e0
-  __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
Functions:
~ -[DCAppAttestController isSupported] : 332 -> 320
~ ___66-[DCAppAttestController generateKeyWithTeamIdentifier:completion:]_block_invoke : 984 -> 972
~ ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke : 1680 -> 1632
~ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke : 1324 -> 1288
~ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2 : 2272 -> 2236
~ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_3 : 368 -> 356
~ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.65 : 368 -> 356
~ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.77 : 2068 -> 2036
~ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.78 : 372 -> 360
~ __99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.81 : 372 -> 360
~ ___91-[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]_block_invoke : 1516 -> 1480
~ ___71-[DCAppAttestController sign:withKey:teamIdentifier:completionHandler:]_block_invoke : 900 -> 876
~ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke : 772 -> 748
~ __80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.101 : 1128 -> 1080
~ ___46-[DCAppAttestController isSupportedWithError:]_block_invoke : 340 -> 328
~ -[DCAppAttestController rewrapAsDCError:] : 412 -> 400
~ -[DCAppAttestController dispatchCompletionHandler:ontoQueue:] : 584 -> 572
~ -[DCDeviceMetadataDaemonConnection connection] : 768 -> 756
~ -[DCAnalytics sendPayload:forEvent:withError:] : 544 -> 532
~ -[DCAnalytics sendPerformanceForCategory:eventType:] : 2680 -> 2644
~ -[DCAppAttestDeviceService isSupported] : 280 -> 268
~ -[DCAppAttestDeviceService attestKey:clientDataHash:options:completionHandler:] : 808 -> 784
~ -[DCAppAttestDeviceService hasEntitlement] : 756 -> 744
~ ___40+[DCXPCUtil sharedSerialProcessingQueue]_block_invoke : 512 -> 488
~ ___39-[DCDevice _isSupportedReturningError:]_block_invoke : 444 -> 432
~ -[DCDevice isSupported] : 332 -> 320
~ -[DCAppAttestWebAuthService isSupported] : 280 -> 268
~ -[DCAppAttestWebAuthService attestKey:clientDataHash:authData:completionHandler:] : 808 -> 784
~ -[DCAppAttestWebAuthService hasEntitlement] : 756 -> 744
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheck/Source/Core/DCAnalytics.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheck/Source/Core/DCAppAttestController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheck/Source/Core/DCDeviceMetadataDaemonConnection.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheck/Source/Interfaces/Private/DCAppAttestDeviceService.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheck/Source/Interfaces/Private/DCAppAttestWebAuthService.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/DeviceCheck/Source/Interfaces/Public/DCDevice.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/devicecheckd/Source/Core/DCXPCUtil.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheck/Source/Core/DCAnalytics.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheck/Source/Core/DCAppAttestController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheck/Source/Core/DCDeviceMetadataDaemonConnection.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheck/Source/Interfaces/Private/DCAppAttestDeviceService.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheck/Source/Interfaces/Private/DCAppAttestWebAuthService.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/DeviceCheck/Source/Interfaces/Public/DCDevice.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/devicecheckd/Source/Core/DCXPCUtil.m"

```
