## ManagedAppDistribution

> `/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution`

```diff

-3.3.3.0.0
-  __TEXT.__text: 0x87554
-  __TEXT.__auth_stubs: 0x1300
+3.4.15.1.0
+  __TEXT.__text: 0x86ce0
+  __TEXT.__auth_stubs: 0x1320
   __TEXT.__objc_methlist: 0x324
-  __TEXT.__const: 0xee24
-  __TEXT.__cstring: 0x14a6
-  __TEXT.__swift5_typeref: 0x2613
-  __TEXT.__constg_swiftt: 0x25c4
-  __TEXT.__swift5_proto: 0xe08
-  __TEXT.__swift5_types: 0x40c
-  __TEXT.__swift_as_entry: 0x118
-  __TEXT.__swift_as_ret: 0x164
-  __TEXT.__oslogstring: 0x66d
+  __TEXT.__const: 0xec14
+  __TEXT.__cstring: 0xf3b
+  __TEXT.__swift5_typeref: 0x25bf
+  __TEXT.__constg_swiftt: 0x2558
+  __TEXT.__swift5_proto: 0xdec
+  __TEXT.__swift5_types: 0x400
+  __TEXT.__swift_as_entry: 0x110
+  __TEXT.__swift_as_ret: 0x158
+  __TEXT.__oslogstring: 0x63d
   __TEXT.__unwind_info: 0x2d48
-  __TEXT.__eh_frame: 0x4970
-  __TEXT.__objc_methname: 0xa01
-  __DATA_CONST.__got: 0x330
-  __DATA_CONST.__const: 0x110
+  __TEXT.__eh_frame: 0x4d20
+  __TEXT.__objc_classname: 0x2a6
+  __TEXT.__objc_methname: 0xb11
+  __TEXT.__objc_methtype: 0x24b
+  __TEXT.__objc_stubs: 0x7c0
+  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x310
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x980
-  __AUTH_CONST.__const: 0x8720
+  __AUTH_CONST.__auth_got: 0x998
+  __AUTH_CONST.__const: 0x8590
   __AUTH_CONST.__objc_const: 0x860
   __AUTH.__objc_data: 0x158
-  __AUTH.__data: 0x8d8
-  __DATA.__data: 0x2468
-  __DATA.__bss: 0x18a80
+  __AUTH.__data: 0x858
+  __DATA.__data: 0x2230
+  __DATA.__bss: 0x18480
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x150
-  __DATA_DIRTY.__data: 0xc40
-  __DATA_DIRTY.__bss: 0x3680
+  __DATA_DIRTY.__data: 0xe10
+  __DATA_DIRTY.__bss: 0x3900
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A376D304-155B-3399-9B17-18382266ECE5
-  Functions: 4235
-  Symbols:   1598
+  UUID: 4C6ACCBB-BF8C-375F-91A4-07CCE0B333D8
+  Functions: 4141
+  Symbols:   1640
   CStrings:  320
 
Symbols:
+ __PROTOCOLS__TtC22ManagedAppDistribution9XPCClient.7
+ _block_copy_helper.182
+ _block_descriptor.184
+ _block_destroy_helper.183
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$addMessageRegistrations:reply:
+ _objc_msgSend$addOrUpdateManagedApp:reply:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$bundleID
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$cancelManagedApp:reply:
+ _objc_msgSend$cancelManagedPackage:reply:
+ _objc_msgSend$composedIdentifier
+ _objc_msgSend$copySIMIdentity:completion:
+ _objc_msgSend$copySIMIdentity:error:
+ _objc_msgSend$currentDeclarationKeysWithReply:
+ _objc_msgSend$daemonInstanceIdentifierWithReply:
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$dictionaryForKey:
+ _objc_msgSend$getCGImageForImageDescriptor:completion:
+ _objc_msgSend$getCurrentDataSubscriptionContext:
+ _objc_msgSend$getCurrentDataSubscriptionContextSync:
+ _objc_msgSend$getDataStatus:completion:
+ _objc_msgSend$getDataStatus:error:
+ _objc_msgSend$getDeclarationStatus:reply:
+ _objc_msgSend$handleDiagnostics:reply:
+ _objc_msgSend$handleLaunchAppRequest:reply:
+ _objc_msgSend$handleMessages:
+ _objc_msgSend$handleRestore:reply:
+ _objc_msgSend$inHomeCountry
+ _objc_msgSend$init
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$initWithSize:scale:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithURL:
+ _objc_msgSend$installManagedApp:reply:
+ _objc_msgSend$installManagedAppInternal:reply:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isiOSAppOnMac
+ _objc_msgSend$localizations
+ _objc_msgSend$mainBundle
+ _objc_msgSend$newComposedIdentifier:
+ _objc_msgSend$newComposedIdentifierWithBundleID:
+ _objc_msgSend$oauthAuthorize:reply:
+ _objc_msgSend$oauthInvalidate:reply:
+ _objc_msgSend$pollForMediaAPIUpdates:reply:
+ _objc_msgSend$preferredLocalizationsFromArray:forPreferences:
+ _objc_msgSend$processInfo
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$removeManagedAppWithDeclarationIdentifier:reply:
+ _objc_msgSend$removeMessageRegistrations:reply:
+ _objc_msgSend$resetManagedAppInstallHistoryWithReply:
+ _objc_msgSend$resume
+ _objc_msgSend$screenScale
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setRestoreControl:reply:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_release_x25
+ _objc_release_x27
+ _objc_retain_x24
+ _objectdestroy.3Tm
+ _swift_bridgeObjectRelease_n
- __PROTOCOLS__TtC22ManagedAppDistribution9XPCClient.2
- ___swift_memcpy4_4
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_ManagedAppDistribution
- _associated conformance 22ManagedAppDistribution32InstallEnterpriseManifestRequestV10CodingKeys33_572DD348673B0D090A1375D851B839EFLLOSHAASQ
- _associated conformance 22ManagedAppDistribution32InstallEnterpriseManifestRequestV10CodingKeys33_572DD348673B0D090A1375D851B839EFLLOs0H3KeyAAs23CustomStringConvertible
- _associated conformance 22ManagedAppDistribution32InstallEnterpriseManifestRequestV10CodingKeys33_572DD348673B0D090A1375D851B839EFLLOs0H3KeyAAs28CustomDebugStringConvertible
- _block_copy_helper.187
- _block_copy_helper.192
- _block_copy_helper.29
- _block_copy_helper.36
- _block_copy_helper.42
- _block_descriptor.189
- _block_descriptor.194
- _block_descriptor.31
- _block_descriptor.38
- _block_descriptor.44
- _block_destroy_helper.188
- _block_destroy_helper.193
- _block_destroy_helper.30
- _block_destroy_helper.37
- _block_destroy_helper.43
- _objectdestroy.21Tm
- _symbolic _____y_____G 22ManagedAppDistribution8XPCValue33_4F6B231E3DB4CA07E0E06CD491AEAB13LLV AA32InstallEnterpriseManifestRequestV
- _symbolic _____y_____G s22KeyedDecodingContainerV 22ManagedAppDistribution32InstallEnterpriseManifestRequestV10CodingKeys33_572DD348673B0D090A1375D851B839EFLLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 22ManagedAppDistribution32InstallEnterpriseManifestRequestV10CodingKeys33_572DD348673B0D090A1375D851B839EFLLO
- _symbolic _____y__________G s13ManagedBufferCsRi__rlE 0A15AppDistribution9XPCClientC7Storage33_34555067A5432633D15E503CF11FCBECLLV So16os_unfair_lock_sV
- _type_layout_string So16os_unfair_lock_sV
CStrings:
+ "MPK"
+ "MarketplaceKit"
+ "fetchNonEntitledDataRequest:reply:"
+ "networkConnection"
+ "versionUnavailable"
- "Deduplicating app catalog results"
- "installEnterpriseManifest:reply:"

```
