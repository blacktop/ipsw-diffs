## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

```diff

-474.2.0.0.0
-  __TEXT.__text: 0x150ab0
+474.2.0.5.0
+  __TEXT.__text: 0x15164c
   __TEXT.__auth_stubs: 0xfe0
   __TEXT.__delay_helper: 0x540
-  __TEXT.__objc_methlist: 0xbe7c
-  __TEXT.__const: 0xe60
-  __TEXT.__cstring: 0x1582e
-  __TEXT.__oslogstring: 0x1d27e
-  __TEXT.__gcc_except_tab: 0x9a94
-  __TEXT.__unwind_info: 0x4398
-  __TEXT.__objc_classname: 0x288b
-  __TEXT.__objc_methname: 0x1e893
-  __TEXT.__objc_methtype: 0x572d
-  __TEXT.__objc_stubs: 0x15540
+  __TEXT.__objc_methlist: 0xbfa4
+  __TEXT.__const: 0xe70
+  __TEXT.__cstring: 0x15abc
+  __TEXT.__oslogstring: 0x1d0d1
+  __TEXT.__gcc_except_tab: 0x9a9c
+  __TEXT.__unwind_info: 0x43e0
+  __TEXT.__objc_classname: 0x2894
+  __TEXT.__objc_methname: 0x1eb82
+  __TEXT.__objc_methtype: 0x5756
+  __TEXT.__objc_stubs: 0x157c0
   __DATA_CONST.__got: 0x1370
-  __DATA_CONST.__const: 0x6b30
+  __DATA_CONST.__const: 0x6b40
   __DATA_CONST.__objc_classlist: 0x918
-  __DATA_CONST.__objc_catlist: 0x70
+  __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6170
+  __DATA_CONST.__objc_selrefs: 0x6228
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x5e8
-  __DATA_CONST.__objc_arraydata: 0x338
+  __DATA_CONST.__objc_arraydata: 0x350
   __AUTH_CONST.__auth_got: 0x800
   __AUTH_CONST.__const: 0x12a0
-  __AUTH_CONST.__cfstring: 0xd8a0
-  __AUTH_CONST.__objc_const: 0x169c0
+  __AUTH_CONST.__cfstring: 0xd9e0
+  __AUTH_CONST.__objc_const: 0x16a70
   __AUTH_CONST.__objc_intobj: 0x9f0
-  __AUTH_CONST.__objc_arrayobj: 0x318
+  __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1838
   __AUTH.__data: 0x690
-  __DATA.__objc_ivar: 0x904
+  __DATA.__objc_ivar: 0x90c
   __DATA.__data: 0x2680
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D011260B-BC7A-3EF1-B99E-D577297C8F85
-  Functions: 4851
-  Symbols:   17534
-  CStrings:  10652
+  UUID: 5A19C72B-C4E7-354A-979E-BA422CA087AB
+  Functions: 4877
+  Symbols:   17613
+  CStrings:  10701
 
Symbols:
+ +[TRIExternalConfigurationChangeProcessor _processConfigChangeWithServerContext:withTaskQueue:]
+ +[TRIExternalConfigurationChangeProcessor processAdsBucketIdChangeIfNecessaryForBucketId:withServerContext:withTaskQueue:]
+ +[TRIExternalConfigurationChangeProcessor processMapsBucketIdChangeIfNecessaryForBucketId:withServerContext:withTaskQueue:]
+ +[TRIExternalConfigurationChangeProcessor processStorefrontChangeIfNecessaryForStorefront:withServerContext:withTaskQueue:]
+ +[TRISystemInfo _adsBucketId:]
+ +[TRISystemInfo _storefront:]
+ -[NSData(TRIFunctions) tri_initWithEncodedString:]
+ -[NSString(TRIFunctions) tri_containsEncodedInteger:]
+ -[NSString(TRIFunctions) tri_intersectsEncodedIntegers:]
+ -[TRIPersistentUserSettings _persistArchivableObject:forKey:]
+ -[TRIPersistentUserSettings _persistedArchivableObjectForKey:ofClasses:]
+ -[TRIPersistentUserSettings persistAdsBucketId:]
+ -[TRIPersistentUserSettings persistStorefront:]
+ -[TRIPersistentUserSettings persistedAdsBucketId]
+ -[TRIPersistentUserSettings persistedStorefront]
+ -[TRISystemConfiguration adsBucketId]
+ -[TRISystemConfiguration storefront]
+ -[TRISystemInfo adsBucketId]
+ -[TRISystemInfo setAdsBucketId:]
+ -[TRISystemInfo setStorefront:]
+ -[TRISystemInfo storefront]
+ -[TRIXPCCovariateFetcher adsBucketIDWithNamespace:]
+ -[TRIXPCCovariateFetcher storefront]
+ _OBJC_CLASS_$_TRIExternalConfigurationChangeProcessor
+ _OBJC_IVAR_$_TRISystemInfo._adsBucketId
+ _OBJC_IVAR_$_TRISystemInfo._storefront
+ _OBJC_METACLASS_$_TRIExternalConfigurationChangeProcessor
+ _TRIPersistentAdsBucket
+ _TRIPersistentStorefront
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSData_$_TRIFunctions
+ __OBJC_$_CATEGORY_NSData_$_TRIFunctions
+ __OBJC_$_CLASS_METHODS_TRIExternalConfigurationChangeProcessor
+ __OBJC_CLASS_RO_$_TRIExternalConfigurationChangeProcessor
+ __OBJC_METACLASS_RO_$_TRIExternalConfigurationChangeProcessor
+ ___115-[TRIRemoteAssetExtractor extractArchiveFromFile:withArchiveName:toEmptyDirectory:postExtractionCompression:error:]_block_invoke.32
+ ___36-[TRIXPCCovariateFetcher storefront]_block_invoke
+ ___36-[TRIXPCCovariateFetcher storefront]_block_invoke_2
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.446
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.461
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.494
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.497
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.498
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.447
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.462
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.499
+ ___51-[TRIXPCCovariateFetcher adsBucketIDWithNamespace:]_block_invoke
+ ___51-[TRIXPCCovariateFetcher adsBucketIDWithNamespace:]_block_invoke_2
+ ___52-[TRIXPCCovariateFetcher sendMessageToRemoteObject:]_block_invoke.40
+ ___60-[TRIXPCCovariateFetcher setupArchivingServiceXPCConnection]_block_invoke.31
+ ___78-[NSFileManager(TRIServer) triRemoveCachedANEBinariesForModelsFromPath:error:]_block_invoke.42
+ ___87+[TRIRemoteAssetDecrypter decryptAssetWithURL:destinationFilename:namespaceName:error:]_block_invoke.37
+ ___block_literal_global.103
+ ___block_literal_global.113
+ ___block_literal_global.120
+ ___block_literal_global.122
+ ___block_literal_global.33
+ ___block_literal_global.39
+ ___block_literal_global.464
+ ___block_literal_global.576
+ ___block_literal_global.579
+ _objc_msgSend$_adsBucketId:
+ _objc_msgSend$_persistArchivableObject:forKey:
+ _objc_msgSend$_persistedArchivableObjectForKey:ofClasses:
+ _objc_msgSend$_processConfigChangeWithServerContext:withTaskQueue:
+ _objc_msgSend$_storefront:
+ _objc_msgSend$adsBucketIDWithNamespace:
+ _objc_msgSend$adsBucketIDWithNamespace:completion:
+ _objc_msgSend$adsBucketId
+ _objc_msgSend$decompressedDataUsingAlgorithm:error:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$persistAdsBucketId:
+ _objc_msgSend$persistStorefront:
+ _objc_msgSend$persistedAdsBucketId
+ _objc_msgSend$persistedStorefront
+ _objc_msgSend$processAdsBucketIdChangeIfNecessaryForBucketId:withServerContext:withTaskQueue:
+ _objc_msgSend$processStorefrontChangeIfNecessaryForStorefront:withServerContext:withTaskQueue:
+ _objc_msgSend$storefront
+ _objc_msgSend$storefront:
+ _objc_msgSend$tri_initWithEncodedString:
+ _objc_msgSend$tri_intersectsEncodedIntegers:
- +[TRIMapsBucketIdChangeProcessor processMapsBucketIdChangeIfNecessaryForBucketId:withServerContext:withTaskQueue:]
- _OBJC_CLASS_$_TRIMapsBucketIdChangeProcessor
- _OBJC_METACLASS_$_TRIMapsBucketIdChangeProcessor
- __OBJC_$_CLASS_METHODS_TRIMapsBucketIdChangeProcessor
- __OBJC_CLASS_RO_$_TRIMapsBucketIdChangeProcessor
- __OBJC_METACLASS_RO_$_TRIMapsBucketIdChangeProcessor
- ___115-[TRIRemoteAssetExtractor extractArchiveFromFile:withArchiveName:toEmptyDirectory:postExtractionCompression:error:]_block_invoke.29
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.437
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.450
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.483
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.486
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.487
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.438
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.451
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.488
- ___52-[TRIXPCCovariateFetcher sendMessageToRemoteObject:]_block_invoke.37
- ___60-[TRIXPCCovariateFetcher setupArchivingServiceXPCConnection]_block_invoke.28
- ___78-[NSFileManager(TRIServer) triRemoveCachedANEBinariesForModelsFromPath:error:]_block_invoke.39
- ___87+[TRIRemoteAssetDecrypter decryptAssetWithURL:destinationFilename:namespaceName:error:]_block_invoke.34
- ___block_literal_global.111
- ___block_literal_global.114
- ___block_literal_global.116
- ___block_literal_global.30
- ___block_literal_global.36
- ___block_literal_global.453
- ___block_literal_global.565
- ___block_literal_global.568
- ___block_literal_global.97
CStrings:
+ "+[TRIExternalConfigurationChangeProcessor processAdsBucketIdChangeIfNecessaryForBucketId:withServerContext:withTaskQueue:]"
+ "+[TRIExternalConfigurationChangeProcessor processMapsBucketIdChangeIfNecessaryForBucketId:withServerContext:withTaskQueue:]"
+ "+[TRIExternalConfigurationChangeProcessor processStorefrontChangeIfNecessaryForStorefront:withServerContext:withTaskQueue:]"
+ "APPSTORE"
+ "Ads: Storefront: %@"
+ "Ads: bucket id: %@"
+ "AdsBucketId"
+ "Data to be persisted for key: %{public}@ was nil"
+ "Decompressed data size (%d) does not match expected size (%d)"
+ "Failed to decompress data %{public}@"
+ "No persisted value found for key: %{public}@"
+ "Oct 18 2025"
+ "Persisted Ads Bucket Id: %@"
+ "Persisted Storefront: %@"
+ "Storefront"
+ "T@\"NSNumber\",&,N,V_adsBucketId"
+ "T@\"NSString\",&,N,V_storefront"
+ "TRIDServer: external Bucket ID changed, queueing retargeting"
+ "TRIDServer: notification received - %@"
+ "TRIExternalConfigurationChangeProcessor"
+ "TRIExternalConfigurationChangeProcessor.m"
+ "TrialXP-474.2.0.5"
+ "Unable to archive value from Trial persisted storage, encountered: %@"
+ "Unable to fetch Ads Bucket Id."
+ "Unable to fetch Storefront."
+ "Unable to unarchive %@ from Trial persisted storage, encountered: %@"
+ "_adsBucketId"
+ "_adsBucketId:"
+ "_persistArchivableObject:forKey:"
+ "_persistedArchivableObjectForKey:ofClasses:"
+ "_processConfigChangeWithServerContext:withTaskQueue:"
+ "_storefront"
+ "_storefront:"
+ "adsBucketIDWithNamespace:"
+ "adsBucketIDWithNamespace:completion:"
+ "adsBucketId"
+ "adsBucketId != nil"
+ "com.apple.ap.adprivacyd.iTunesActiveStorefrontDidChangeNotification"
+ "com.apple.ap.bucketIdRotated"
+ "com.apple.triald.persisted.Ads.BucketId"
+ "com.apple.triald.persisted.storefront"
+ "decompressedDataUsingAlgorithm:error:"
+ "encoded string has no data %{public}@"
+ "initWithData:"
+ "obj != nil"
+ "persistAdsBucketId:"
+ "persistStorefront:"
+ "persistedAdsBucketId"
+ "persistedStorefront"
+ "processAdsBucketIdChangeIfNecessaryForBucketId:withServerContext:withTaskQueue:"
+ "processStorefrontChangeIfNecessaryForStorefront:withServerContext:withTaskQueue:"
+ "setAdsBucketId:"
+ "setStorefront:"
+ "storefront"
+ "storefront:"
+ "tri_containsEncodedInteger:"
+ "tri_initWithEncodedString:"
+ "tri_intersectsEncodedIntegers:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\">24"
- "Data to be persisted for Maps country code was nil, encountered: %@"
- "Data to be persisted for dictation locales was nil"
- "Data to be persisted for maps bucket id was nil"
- "Data to be persisted for siri locale was nil"
- "No persisted Maps Bucket ID found for key: %{public}@"
- "No persisted Maps country code found"
- "No persisted dictation locales found"
- "No persisted siri locale found"
- "Oct 10 2025"
- "TRIDServer: Maps Bucket ID changed, queueing retargeting"
- "TRIDServer: Maps Experiments Change Notification received"
- "TRIMapsBucketIdChangeProcessor"
- "TrialXP-474.2"
- "Unable to archive dictation locales from Trial persisted storage, encountered: %@"
- "Unable to archive maps bucket id from Trial persisted storage, encountered: %@"
- "Unable to archive siri locale from Trial persisted storage, encountered: %@"
- "Unable to unarchive Maps country code from Trial persisted storage, encountered: %@"
- "Unable to unarchive dictation locales from Trial persisted storage, encountered: %@"
- "Unable to unarchive maps bucket id from Trial persisted storage, encountered: %@"
- "Unable to unarchive siri locale from Trial persisted storage, encountered: %@"
- "siriLocale"

```
