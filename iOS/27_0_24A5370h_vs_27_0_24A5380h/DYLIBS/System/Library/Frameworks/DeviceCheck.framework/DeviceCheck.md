## DeviceCheck

> `/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck`

```diff

-  __TEXT.__text: 0xa6f0
+  __TEXT.__text: 0xa4a4
   __TEXT.__objc_methlist: 0x674
   __TEXT.__const: 0xa8
   __TEXT.__cstring: 0x9c0
-  __TEXT.__gcc_except_tab: 0x470
+  __TEXT.__gcc_except_tab: 0x468
   __TEXT.__oslogstring: 0xcbc
   __TEXT.__unwind_info: 0x2d8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x468
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__got: 0x160
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x640
   __AUTH_CONST.__objc_const: 0xae0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x290
-  __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
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
~ -[DCAppAttestController isSupported] : 320 -> 308
~ ___66-[DCAppAttestController generateKeyWithTeamIdentifier:completion:]_block_invoke : 952 -> 940
~ ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke : 1648 -> 1600
~ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke : 1264 -> 1228
~ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2 : 2164 -> 2128
~ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_3 : 356 -> 344
~ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.57 : 356 -> 344
~ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.67 : 1984 -> 1960
~ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.68 : 360 -> 348
~ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.69 : 360 -> 348
~ ___91-[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]_block_invoke : 1484 -> 1448
~ ___71-[DCAppAttestController sign:withKey:teamIdentifier:completionHandler:]_block_invoke : 884 -> 860
~ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke : 752 -> 728
~ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.84 : 1096 -> 1048
~ ___46-[DCAppAttestController isSupportedWithError:]_block_invoke : 328 -> 316
~ -[DCAppAttestController loadAppUUID] : 456 -> 444
~ -[DCAppAttestController rewrapAsDCError:] : 400 -> 388
~ -[DCAppAttestController dispatchCompletionHandler:ontoQueue:] : 552 -> 540
~ -[DCAnalytics sendPayload:forEvent:withError:] : 504 -> 492
~ -[DCAnalytics sendPerformanceForCategory:eventType:] : 2640 -> 2604
~ -[DCAppAttestDeviceService isSupported] : 276 -> 264
~ -[DCAppAttestDeviceService attestKey:clientDataHash:options:completionHandler:] : 756 -> 732
~ -[DCAppAttestDeviceService hasEntitlement] : 736 -> 724
~ ___40+[DCXPCUtil sharedSerialProcessingQueue]_block_invoke : 504 -> 480
~ ___39-[DCDevice _isSupportedReturningError:]_block_invoke : 412 -> 400
~ -[DCDevice isSupported] : 320 -> 308
~ -[DCAppAttestWebAuthService isSupported] : 276 -> 264
~ -[DCAppAttestWebAuthService attestKey:clientDataHash:authData:completionHandler:] : 756 -> 732
~ -[DCAppAttestWebAuthService hasEntitlement] : 736 -> 724

```
