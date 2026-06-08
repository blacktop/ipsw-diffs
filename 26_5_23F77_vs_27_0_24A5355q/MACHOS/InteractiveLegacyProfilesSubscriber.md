## InteractiveLegacyProfilesSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/InteractiveLegacyProfilesSubscriber.xpc/InteractiveLegacyProfilesSubscriber`

```diff

-585.120.2.0.0
-  __TEXT.__text: 0x7940
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_stubs: 0x1e0
-  __TEXT.__objc_methlist: 0x2f0
-  __TEXT.__const: 0x468
-  __TEXT.__swift5_typeref: 0x244
+621.0.0.502.1
+  __TEXT.__text: 0x9664
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_stubs: 0x280
+  __TEXT.__objc_methlist: 0x380
+  __TEXT.__const: 0x4a8
+  __TEXT.__swift5_typeref: 0x286
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x124
+  __TEXT.__constg_swiftt: 0x144
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x10
-  __TEXT.__objc_methname: 0x75c
-  __TEXT.__oslogstring: 0x14c
-  __TEXT.__cstring: 0x231
-  __TEXT.__objc_classname: 0xf9
-  __TEXT.__objc_methtype: 0x46c
-  __TEXT.__swift5_reflstr: 0xb7
-  __TEXT.__swift5_fieldmd: 0x78
+  __TEXT.__objc_classname: 0x129
+  __TEXT.__objc_methname: 0xbb4
+  __TEXT.__objc_methtype: 0x956
+  __TEXT.__oslogstring: 0x1bc
+  __TEXT.__cstring: 0x461
+  __TEXT.__swift5_reflstr: 0x117
+  __TEXT.__swift5_fieldmd: 0x9c
   __TEXT.__swift5_capture: 0x170
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__swift_as_entry: 0x44
-  __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__unwind_info: 0x2b0
-  __TEXT.__eh_frame: 0x5f8
-  __DATA_CONST.__auth_got: 0x3e8
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__auth_ptr: 0xd0
-  __DATA_CONST.__const: 0x408
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x48
+  __TEXT.__swift_as_cont: 0x48
+  __TEXT.__unwind_info: 0x2f0
+  __TEXT.__eh_frame: 0x780
+  __DATA_CONST.__const: 0x458
   __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA.__objc_const: 0x2e8
-  __DATA.__objc_selrefs: 0x1c0
-  __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x2b0
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__auth_got: 0x460
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__auth_ptr: 0xd0
+  __DATA.__objc_const: 0x360
+  __DATA.__objc_selrefs: 0x238
+  __DATA.__objc_data: 0x208
+  __DATA.__data: 0x320
   __DATA.__common: 0x18
   __DATA.__bss: 0x200
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 34267A75-11B0-3A63-A90A-FD82F1644406
-  Functions: 160
-  Symbols:   108
-  CStrings:  131
+  UUID: 7B98F1E0-A636-31E9-B939-82BF6AF469A9
+  Functions: 179
+  Symbols:   121
+  CStrings:  177
 
Symbols:
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_RMAssetResolverController
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _objc_release
+ _objc_retain_x22
+ _objc_retain_x27
+ _swift_getObjCClassFromMetadata
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain_x21
- _objc_retain_x24
- _swift_retain
CStrings:
+ "%s: downloading asset to: %{public}s"
+ "%s: failed to resolve asset: %@"
+ "%s: invalid configuration: %s"
+ "Asset resolution failed: "
+ "Asset resolution returned false without error"
+ "Both payloadProfileURL and payloadProfileAssetReference are present - only one is allowed"
+ "InteractiveLegacyProfiles.AssetResolutionFailed"
+ "InteractiveLegacyProfiles.InvalidConfiguration"
+ "Invalid configuration: "
+ "Neither payloadProfileURL nor payloadProfileAssetReference is present - exactly one is required"
+ "RMAssetResolverControllerProtocol"
+ "assetResolverController"
+ "declarationKeyForReference:"
+ "defaultManager"
+ "extractUserIdentityAsset:assetIdentifier:completionHandler:"
+ "installProfileAtPath:store:declarationKey:completionHandler:"
+ "installProfileFromAsset(_:declaration:)"
+ "payloadProfileAssetReference"
+ "payloadProfileAssetReference is unexpectedly nil"
+ "payloadProfileURL is unexpectedly nil"
+ "removeItemAtURL:error:"
+ "resolveDataAsset:assetIdentifier:downloadURL:completionHandler:"
+ "resolveDataAssetWithAssetIdentifier:configurationIdentifier:downloadURL:subscriberStore:scope:completionHandler:"
+ "resolveDataAssetWithAssetIdentifier:downloadURL:storeIdentifier:scope:completionHandler:"
+ "resolveKeychainAsset:assetIdentifier:accessGroup:completionHandler:"
+ "resolveKeychainAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:"
+ "resolveKeychainAssets:assetIdentifiers:accessGroup:completionHandler:"
+ "resolveKeychainAssetsWithAssetIdentifiers:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:"
+ "resolveKeychainPasswordAsset:assetIdentifier:accessGroup:completionHandler:"
+ "resolveKeychainPasswordAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:"
+ "resolveUserNameAndPasswordAsset:assetIdentifier:completionHandler:"
+ "v20@?0B8@\"NSError\"12"
+ "v40@0:8@\"RMSubscribedConfigurationReference\"16@\"NSString\"24@?<v@?@\"RMModelAssetUserIdentityDeclaration\"@\"NSError\">32"
+ "v40@0:8@\"RMSubscribedConfigurationReference\"16@\"NSString\"24@?<v@?@\"RMModelUserNameAndPasswordCredentialDeclaration\"@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "v48@0:8@\"RMSubscribedConfigurationReference\"16@\"NSArray\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@\"RMSubscribedConfigurationReference\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v48@0:8@\"RMSubscribedConfigurationReference\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSString\"@\"NSError\">40"
+ "v48@0:8@\"RMSubscribedConfigurationReference\"16@\"NSString\"24@\"NSURL\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
+ "v56@0:8@\"NSString\"16@\"NSURL\"24@\"NSString\"32q40@?<v@?B@\"NSError\">48"
+ "v56@0:8@16@24@32q40@?48"
+ "v64@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"RMSubscriberStore\"40q48@?<v@?@\"NSArray\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"RMSubscriberStore\"40q48@?<v@?@\"NSData\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"RMSubscriberStore\"40q48@?<v@?@\"NSData\"@\"NSString\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32@\"RMSubscriberStore\"40q48@?<v@?B@\"NSError\">56"
+ "v64@0:8@16@24@32@40q48@?56"
- "declarationKeyForStore:declaration:"

```
