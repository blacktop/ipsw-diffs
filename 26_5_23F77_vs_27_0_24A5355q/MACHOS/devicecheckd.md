## devicecheckd

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd`

```diff

-132.2.0.0.0
-  __TEXT.__text: 0x5e98
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_stubs: 0x680
-  __TEXT.__objc_methlist: 0x4c4
-  __TEXT.__objc_classname: 0xab
-  __TEXT.__objc_methname: 0xad2
-  __TEXT.__objc_methtype: 0x546
-  __TEXT.__cstring: 0x544
+151.0.0.0.0
+  __TEXT.__text: 0x6704
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_stubs: 0xa20
+  __TEXT.__objc_methlist: 0x57c
+  __TEXT.__objc_classname: 0xd3
+  __TEXT.__objc_methname: 0xe9c
+  __TEXT.__objc_methtype: 0x56d
+  __TEXT.__cstring: 0x78e
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__oslogstring: 0x676
-  __TEXT.__unwind_info: 0x1c0
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x3b8
-  __DATA_CONST.__cfstring: 0x220
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__gcc_except_tab: 0x224
+  __TEXT.__oslogstring: 0xab7
+  __TEXT.__unwind_info: 0x230
+  __DATA_CONST.__const: 0x2b0
+  __DATA_CONST.__cfstring: 0x340
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x6f0
-  __DATA.__objc_selrefs: 0x310
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__objc_data: 0x190
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x140
+  __DATA.__objc_const: 0xa00
+  __DATA.__objc_selrefs: 0x3f0
+  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_data: 0x280
   __DATA.__data: 0x120
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/DeviceCheckInternal.framework/DeviceCheckInternal
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 56E6039A-D0CF-385C-A5A2-2E9A06F336EB
-  Functions: 104
-  Symbols:   122
-  CStrings:  254
+  UUID: AE218013-C8BC-3246-BC90-E795C9CB24CB
+  Functions: 116
+  Symbols:   134
+  CStrings:  340
 
Symbols:
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_UAFAssetSetManager
+ _OBJC_CLASS_$_UAFAssetSetSubscription
+ ___NSDictionary0__struct
+ _kUAFAssetMetadataAssetVersionKey
+ _mach_task_self_
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _task_info
- _dispatch_async
- _objc_retain_x25
- _objc_retain_x26
CStrings:
+ "%25s:%-5d Created XPC processing queue. { queueName=%s }"
+ "%25s:%-5d Failed to create XPC processing queue."
+ "%25s:%-5d Failed to fetch asset from asset set. { assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Failed to fetch asset location. { assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Failed to fetch asset set. { assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Failed to fetch asset version. { assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Failed to get key."
+ "%25s:%-5d Failed to subscribe to UAF asset. { configuration={ %@ }, error=%@ }"
+ "%25s:%-5d Failed to subscribe to asset. { error=%{public}@, assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Failed to unsubscribe to asset set. { error=%{public}@, assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Subscribed to UAF asset. { configuration={ %@ } }"
+ "%25s:%-5d Subscription to asset set already exists for subscriber. { %{public}@, assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Subscription to asset set already exists for subscriber. { assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Subscription to asset set does not exist for subscriber. { assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Unsubscribed from UAF asset set. { assetConfiguration { %{public}@ } }"
+ "-[DCClientHandler getKeyProxyEndpoint:keyId:teamIdentifier:completion:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCUAFAssetManager.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TwoBit/devicecheckd/Source/Core/DCXPCUtil.m"
+ "1"
+ "@\"DCUAFAssetConfiguration\""
+ "@\"NSDictionary\""
+ "@\"NSString\""
+ "@\"NSURL\""
+ "@40@0:8@16@24@32"
+ "@56@0:8@16@24@32@40@48"
+ "DCUAFAssetConfiguration"
+ "DCUAFAssetInfo"
+ "DCUAFAssetManager"
+ "DCXPCUtil"
+ "Failed to get key."
+ "T@\"DCUAFAssetConfiguration\",R,N,V_configuration"
+ "T@\"NSDictionary\",R,C,N,V_usageType"
+ "T@\"NSString\",R,C,N,V_assetName"
+ "T@\"NSString\",R,C,N,V_assetSetName"
+ "T@\"NSString\",R,C,N,V_name"
+ "T@\"NSString\",R,C,N,V_subscriber"
+ "T@\"NSString\",R,C,N,V_subscriptionName"
+ "T@\"NSString\",R,C,N,V_version"
+ "T@\"NSURL\",R,C,N,V_assetDataURL"
+ "_assetDataURL"
+ "_assetName"
+ "_assetSetName"
+ "_configuration"
+ "_name"
+ "_setQueue:"
+ "_subscriber"
+ "_subscriptionName"
+ "_usageType"
+ "_version"
+ "absoluteString"
+ "appAttestationAssert:keyId:clientDataHash:clientSDKVersionToken:completion:"
+ "appAttestationAssertWithTeamIdentifier:appUUID:keyId:clientDataHash:clientSDKVersionToken:completion:"
+ "appAttestationAttestKey:keyId:clientDataHash:clientSDKVersionToken:completion:"
+ "appAttestationAttestKeyWithTeamIdentifier:appUUID:keyId:clientDataHash:clientSDKVersionToken:completion:"
+ "arrayWithObjects:count:"
+ "assetDataURL"
+ "assetName"
+ "assetNamed:"
+ "assetSetName"
+ "assetSetName=%@, subscriber=%@, subscriptionName=%@"
+ "boolForKey:"
+ "com.apple.devicecheck.two.bit"
+ "com.apple.devicecheck.twobit"
+ "com.apple.devicecheck.uafassetmanager"
+ "com.apple.devicecheck.xpc.processing"
+ "configuration"
+ "copy"
+ "dc"
+ "dci"
+ "devicecheck.twobit"
+ "fetchWithCompletion:"
+ "getSelfAuditToken"
+ "initWithAssetSetName:assetName:subscriber:subscriptionName:usageType:"
+ "initWithConfiguration:"
+ "initWithName:assetDataURL:version:"
+ "initWithName:assetSets:usageAliases:expires:"
+ "location"
+ "metadata"
+ "name"
+ "objectForKeyedSubscript:"
+ "retrieveAssetSet:usages:queue:completion:"
+ "sharedManager"
+ "sharedSerialProcessingQueue"
+ "standardUserDefaults"
+ "subscribe:subscriptions:queue:completion:"
+ "subscribeWithCompletion:"
+ "subscribed"
+ "subscriber"
+ "subscriptionName"
+ "subscriptionsForSubscriber:"
+ "testAuditToken"
+ "twobit.encryption"
+ "unsubscribe:subscriptionNames:queue:completion:"
+ "unsubscribeWithCompletion:"
+ "usageType"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"UAFAssetSet\"8"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32Q40@?<v@?@\"NSData\"@\"NSError\">48"
+ "v56@0:8@16@24@32Q40@?48"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40Q48@?<v@?@\"NSData\"@\"NSError\">56"
+ "v64@0:8@16@24@32@40Q48@?56"
+ "version"
+ "{ name=%@, assetDataURL=%@, version=%@ }"
+ "{?=[8I]}16@0:8"
- "%25s:%-5d Created server processing queue. { queueName=%s }"
- "%25s:%-5d Handling sign data with BAA certificate."
- "<%@: %p - refreshAllowed: %d, ignoreMetadataCache: %d>"
- "B"
- "DCAssetFetcherContext"
- "TB,N,V_allowCatalogRefresh"
- "TB,N,V_ignoreCachedMetadata"
- "_allowCatalogRefresh"
- "_ignoreCachedMetadata"
- "allowCatalogRefresh"
- "appAttestationAssert:keyId:clientDataHash:completion:"
- "appAttestationAssertWithTeamIdentifier:appUUID:keyId:clientDataHash:completion:"
- "appAttestationAttestKey:keyId:clientDataHash:completion:"
- "appAttestationAttestKeyWithTeamIdentifier:appUUID:keyId:clientDataHash:completion:"
- "baaSignatureForData:completion:"
- "baaSignaturesForData:completion:"
- "com.apple.devicecheck.error.baa"
- "com.apple.devicecheck.server.processing"
- "ignoreCachedMetadata"
- "setAllowCatalogRefresh:"
- "setIgnoreCachedMetadata:"
- "v20@0:8B16"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSData\"@\"NSError\">24"
- "v32@?0@\"NSDictionary\"8@\"NSData\"16@\"NSError\"24"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"NSData\"@\"NSError\">48"

```
