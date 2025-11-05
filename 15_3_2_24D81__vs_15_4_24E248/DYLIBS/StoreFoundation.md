## StoreFoundation

> `/System/Library/PrivateFrameworks/StoreFoundation.framework/Versions/A/StoreFoundation`

```diff

-715.2.3.0.0
-  __TEXT.__text: 0x3c6d4
+715.4.5.0.0
+  __TEXT.__text: 0x3b7a4
   __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x4a18
+  __TEXT.__objc_methlist: 0x55e0
   __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0xa6c
-  __TEXT.__cstring: 0x87e0
+  __TEXT.__gcc_except_tab: 0xa3c
+  __TEXT.__cstring: 0x847c
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xf90
+  __TEXT.__unwind_info: 0xf48
   __TEXT.__objc_classname: 0x7fb
-  __TEXT.__objc_methname: 0xdb82
+  __TEXT.__objc_methname: 0xdb6d
   __TEXT.__objc_methtype: 0x2278
-  __TEXT.__objc_stubs: 0x8660
+  __TEXT.__objc_stubs: 0x8520
   __DATA_CONST.__got: 0x568
-  __DATA_CONST.__const: 0x9f8
+  __DATA_CONST.__const: 0x9d8
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3178
+  __DATA_CONST.__objc_selrefs: 0x3588
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x188
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x458
-  __AUTH_CONST.__const: 0xff0
-  __AUTH_CONST.__cfstring: 0x8260
-  __AUTH_CONST.__objc_const: 0xc4b8
+  __AUTH_CONST.__const: 0xf60
+  __AUTH_CONST.__cfstring: 0x7ec0
+  __AUTH_CONST.__objc_const: 0xaed0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __DATA.__objc_ivar: 0x6c4
   __DATA.__data: 0xb30

   - /System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Versions/A/AppleMediaServicesUI
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/A/AuthKitUI
-  - /System/Library/PrivateFrameworks/BiometricKit.framework/Versions/A/BiometricKit
   - /System/Library/PrivateFrameworks/CommerceKit.framework/Versions/A/Frameworks/CommerceCore.framework/Versions/A/CommerceCore
   - /System/Library/PrivateFrameworks/FamilyControls.framework/Versions/A/FamilyControls
   - /System/Library/PrivateFrameworks/Install.framework/Frameworks/DistributionKit.framework/Versions/A/DistributionKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 975FD1CA-E82F-37B1-A8E0-A7E600445A0E
-  Functions: 1763
-  Symbols:   4858
-  CStrings:  5168
+  UUID: 8A3BCAAB-D07B-35AA-BF38-DC36AB5CF30B
+  Functions: 1777
+  Symbols:   4862
+  CStrings:  5104
 
Symbols:
+ +[CKBook _imageFetchQueue].cold.1
+ +[CKDockMessaging sharedInstance].cold.1
+ +[CKRootHelper sharedInstance].cold.1
+ +[ISDevice eosDeviceType].cold.1
+ +[ISDevice guid].cold.1
+ +[ISDevice isBootedFromRecoveryPartition].cold.1
+ +[ISDevice osVersionReturningMajor:minor:point:].cold.1
+ +[ISOperationQueue mainQueue].cold.1
+ +[ISServiceProxy genericSharedProxy].cold.1
+ +[ISServiceProxy initialize].cold.1
+ +[ISStoreURLOperation addITunesStoreHeadersToRequest:withStoreClient:storeAccount:].cold.1
+ +[NSURL(ISAdditions) _macOSXBuildString].cold.1
+ +[NSURL(ISAdditions) _macOSXVersionString].cold.1
+ +[NSURL(ISAdditions) _userVisibleWebKitVersionString].cold.1
+ +[SSLogManager dateFormatter].cold.1
+ +[SSLogManager sharedManager].cold.1
+ +[SSLogManager useSyslog].cold.1
+ -[CKDockMessaging _xpcDispatchQueue].cold.1
+ -[NSURL(ISAdditions) isSafeExternalURL].cold.1
+ CKAppStoreVersion.cold.1
+ CKOnRecoveryPartition.cold.1
+ GetPathToDaemonUserCacheFolder.cold.1
+ _GetSystemVersion.cold.1
+ _OBJC_CLASS_$_AMSBiometrics
+ __42+[NSURL(ISAdditions) _macOSXVersionString]_block_invoke.cold.1
+ firenzeApplicationSupportDirectoryPath.cold.1
- GCC_except_table6
- _OBJC_CLASS_$_BiometricKit
- ___55+[CKSoftwareProduct createSoftwareProductForAppAtPath:]_block_invoke
- ___55+[CKSoftwareProduct createSoftwareProductForAppAtPath:]_block_invoke_2
- ___81+[CKSoftwareProduct productPathToUpgradeForBundleIdentifier:versionNumberString:]_block_invoke
- ___81+[CKSoftwareProduct productPathToUpgradeForBundleIdentifier:versionNumberString:]_block_invoke_2
- ___block_descriptor_48_e8_32s40r_e27_v16?0"CKSoftwareProduct"8l
- ___block_descriptor_48_e8_32s40r_e62_v24?0"<ISAssetService>"8"NSObject<OS_dispatch_semaphore>"16l
- ___block_descriptor_56_e8_32s40s48r_e62_v24?0"<ISAssetService>"8"NSObject<OS_dispatch_semaphore>"16l
- _objc_msgSend$assetServiceSynchronousBlock:
- _objc_msgSend$createSoftwareProductForAppAtPath:replyBlock:
- _objc_msgSend$isTouchIDCapable
- _objc_msgSend$isVPPLicensed
- _objc_msgSend$manager
- _objc_msgSend$mdItemRef
- _objc_msgSend$pointerValue
- _objc_msgSend$productPathToUpgradeForBundleIdentifier:versionNumberString:replyBlock:
- _objc_msgSend$source
- _objc_msgSend$versionIdentifier
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/CKUpdate.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/Store Services Framework/SSDownloadMetadata.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/Store Services Framework/SSDownloadPhase.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/Store Services Framework/SSDownloadStatus.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/Store Services Framework/SSOperationProgress.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/Store Services Framework/SSPurchase.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/ISCertificate.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/ISDevice.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/ISOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/ISStoreURLOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/ISURLOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/ISURLRequest.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/NSURL_ISAdditions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/CKBook.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/CKBookFetchCoverImageOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/CKDockMessaging.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/CKRootHelper.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/CKUtilities.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISAppleIDLookupOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISCodeSignatureOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISDialog.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISDialogButton.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISDialogOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISJSONProvider.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISPropertyListProvider.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISServerAuthenticationOperation.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISServiceClientInterface.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISServiceDelegate.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISServiceProxy.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISSignInPrompt.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISStoreClient.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/NSFileManager_ISAdditions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/NSString+Sandbox.m"
- "%@: (%@, %@, %@:%@ VPP:%@ md:%p %@) "
- "%@: copyWithZone(zone %@) returning nil"
- "-[CKSoftwareProduct copyWithZone:]"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/CKUpdate.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/Store Services Framework/SSDownloadMetadata.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/Store Services Framework/SSDownloadPhase.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/Store Services Framework/SSDownloadStatus.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/Store Services Framework/SSOperationProgress.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/Store Services Framework/SSPurchase.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/CKSoftwareProduct.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/ISCertificate.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/ISDevice.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/ISOperation.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/ISStoreURLOperation.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/ISURLOperation.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/ISURLRequest.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/NSURL_ISAdditions.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/CKBook.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/CKBookFetchCoverImageOperation.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/CKDockMessaging.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/CKRootHelper.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/CKUtilities.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISAppleIDLookupOperation.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISCodeSignatureOperation.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISDialog.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISDialogButton.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISDialogOperation.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISJSONProvider.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISPropertyListProvider.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISServerAuthenticationOperation.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISServiceClientInterface.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISServiceDelegate.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISServiceProxy.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISSignInPrompt.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/ISStoreClient.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/NSFileManager_ISAdditions.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreFoundation/StoreFoundation/NSString+Sandbox.m"
- "LaunchPad"
- "LaunchServices"
- "LegacyApp"
- "Spotlight"
- "Unknown"
- "manager"
- "pointerValue"
- "v16@?0@\"CKSoftwareProduct\"8"
- "v24@?0@\"<ISAssetService>\"8@\"NSObject<OS_dispatch_semaphore>\"16"

```
