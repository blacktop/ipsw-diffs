## PassKitServices

> `/System/Library/PrivateFrameworks/PassKitServices.framework/PassKitServices`

```diff

-1642.6.5.0.0
-  __TEXT.__text: 0x1ffc
-  __TEXT.__auth_stubs: 0x340
+1677.4.0.0.0
+  __TEXT.__text: 0x1ea0
   __TEXT.__objc_methlist: 0x274
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x7c
   __TEXT.__oslogstring: 0xf1
-  __TEXT.__cstring: 0x136
+  __TEXT.__cstring: 0x17d
   __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0xd6
-  __TEXT.__objc_methname: 0x694
-  __TEXT.__objc_methtype: 0x26a
-  __TEXT.__objc_stubs: 0x640
-  __DATA_CONST.__got: 0x78
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x440
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8BF9B7BD-1514-33B2-831C-B72B6EB8B94C
+  UUID: EFFC998B-6794-378E-8041-71F3051CF89A
   Functions: 39
-  Symbols:   257
-  CStrings:  148
+  Symbols:   256
+  CStrings:  24
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x27
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_release_x2
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
Functions:
~ -[PKPassKitServicesXPCService init] : 104 -> 100
~ -[PKPassKitServicesXPCService snapshotDataForPassUniqueIdentifier:size:completion:] : 260 -> 264
~ ___83-[PKPassKitServicesXPCService snapshotDataForPassUniqueIdentifier:size:completion:]_block_invoke : 212 -> 164
~ -[PKPassKitServicesXPCService imageDataForTransaction:size:completion:] : 252 -> 256
~ ___71-[PKPassKitServicesXPCService imageDataForTransaction:size:completion:]_block_invoke : 212 -> 164
~ -[PKPassKitServicesXPCService imageDataForRecurringPaymentMemo:size:completion:] : 252 -> 256
~ ___80-[PKPassKitServicesXPCService imageDataForRecurringPaymentMemo:size:completion:]_block_invoke : 212 -> 164
~ -[PKPassKitServicesXPCService _createConnection] : 412 -> 408
~ ___48-[PKPassKitServicesXPCService _createConnection]_block_invoke : 220 -> 216
~ ___48-[PKPassKitServicesXPCService _createConnection]_block_invoke_2 : 220 -> 216
~ ___52-[PKServicePaymentTransactionImageGenerator dealloc]_block_invoke : 96 -> 100
~ -[PKServicePaymentTransactionImageGenerator setCachedImageData:forKey:] : 704 -> 656
~ -[PKServicePaymentTransactionImageGenerator _nextIndexToUseAndEvictIfNeeded] : 440 -> 364
~ -[PKServicePaymentTransactionImageGenerator _updateNextKeyToEvict] : 316 -> 312
~ ___66-[PKServicePaymentTransactionImageGenerator _updateNextKeyToEvict]_block_invoke : 272 -> 248
~ ___85-[PKServicePaymentTransactionImageGenerator imageDataForTransaction:size:completion:]_block_invoke : 700 -> 672
~ ___85-[PKServicePaymentTransactionImageGenerator imageDataForTransaction:size:completion:]_block_invoke_2 : 240 -> 228
~ ___85-[PKServicePaymentTransactionImageGenerator imageDataForTransaction:size:completion:]_block_invoke_3 : 156 -> 152
~ ___85-[PKServicePaymentTransactionImageGenerator imageDataForTransaction:size:completion:]_block_invoke_4 : 440 -> 420
~ ___85-[PKServicePaymentTransactionImageGenerator imageDataForTransaction:size:completion:]_block_invoke_5 : 232 -> 244
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"PKPassKitServicesXPCService\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "PKCoreSpotlightImageGenerator"
- "PKPassKitServicesXPCService"
- "PKServicePaymentTransactionImageGenerator"
- "PassKitServicesXPCServiceProtocol"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URLByStandardizingPath"
- "Vv16@0:8"
- "[500{?=\"bytes\"^v\"length\"Q}]"
- "^{_NSZone=}16@0:8"
- "_cleanMappedFile:"
- "_connection"
- "_createConnection"
- "_evictionHitCount"
- "_hasSetupTempDir"
- "_invalidate"
- "_keysHitCounts"
- "_lock"
- "_mappedFiles"
- "_mappedFilesIndices"
- "_nextIndexToUseAndEvictIfNeeded"
- "_nextKeyToEvict"
- "_remoteObjectProxyWithErrorHandler:"
- "_updateNextKeyToEvict"
- "_xpcService"
- "absoluteString"
- "addOperation:"
- "autorelease"
- "cachedDataForURL:"
- "cachedImageDataForKey:"
- "class"
- "conformsToProtocol:"
- "constraintsWithMaxSize:"
- "count"
- "dealloc"
- "debugDescription"
- "description"
- "downloadFromUrl:completionHandler:"
- "enumerateKeysAndObjectsUsingBlock:"
- "evaluateWithInput:completion:"
- "fileSystemRepresentation"
- "hash"
- "iconTypeForTransaction:ignoreLogoURL:"
- "imageData"
- "imageDataForPassUniqueIdentifier:size:completion:"
- "imageDataForRecurringPaymentMemo:size:completion:"
- "imageDataForTransaction:size:completion:"
- "init"
- "initWithBytes:length:"
- "initWithData:scale:"
- "initWithPassKitServicesXPCService:"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "logoImageURL"
- "merchant"
- "null"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "resizedImageWithConstraints:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setCachedImageData:forKey:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKey:"
- "setRemoteObjectInterface:"
- "sharedImageAssetDownloader"
- "snapshotDataForPassUniqueIdentifier:size:completion:"
- "staticIconNameForTransaction:"
- "stringWithFormat:"
- "superclass"
- "transitType"
- "uniqueIdentifier"
- "unsignedIntegerValue"
- "v16@0:8"
- "v32@0:8@16@24"
- "v32@0:8{?=^vQ}16"
- "v48@0:8@\"NSString\"16{CGSize=dd}24@?<v@?@\"NSData\">40"
- "v48@0:8@\"PKPaymentTransaction\"16{CGSize=dd}24@?<v@?@\"NSData\">40"
- "v48@0:8@\"PKPeerPaymentRecurringPaymentMemo\"16{CGSize=dd}24@?<v@?@\"NSData\">40"
- "v48@0:8@16{CGSize=dd}24@?40"
- "writeToURL:atomically:"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
