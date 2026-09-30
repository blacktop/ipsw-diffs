## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-1487.122.1.0.0
-  __TEXT.__text: 0x82dbc
+1487.140.25.0.0
+  __TEXT.__text: 0x82a00
   __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x63e4
+  __TEXT.__objc_methlist: 0x63dc
   __TEXT.__const: 0x298
   __TEXT.__gcc_except_tab: 0xbd8
-  __TEXT.__cstring: 0x10682
-  __TEXT.__oslogstring: 0xa1ca
+  __TEXT.__cstring: 0x10586
+  __TEXT.__oslogstring: 0xa164
   __TEXT.__unwind_info: 0x1af0
   __TEXT.__objc_classname: 0x889
-  __TEXT.__objc_methname: 0x15004
+  __TEXT.__objc_methname: 0x14f5d
   __TEXT.__objc_methtype: 0x1768
-  __TEXT.__objc_stubs: 0x81c0
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x1ff8
+  __TEXT.__objc_stubs: 0x8100
+  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__const: 0x1fe8
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30c8
+  __DATA_CONST.__objc_selrefs: 0x3090
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x2f0
   __AUTH_CONST.__auth_got: 0x500
   __AUTH_CONST.__const: 0x6e0
-  __AUTH_CONST.__cfstring: 0xda80
+  __AUTH_CONST.__cfstring: 0xd980
   __AUTH_CONST.__objc_const: 0x98f0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA022FEE-EB35-3AD7-B2E3-B29D175AE589
-  Functions: 2797
-  Symbols:   8399
-  CStrings:  6856
+  UUID: 137C1D1A-2BBF-3160-9DCC-D0914EB66897
+  Functions: 2795
+  Symbols:   8386
+  CStrings:  6832
 
Symbols:
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1058
+ ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1059
+ ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1084
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1053
+ ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1057
+ ___Block_byref_object_copy_.1221
+ ___Block_byref_object_dispose_.1222
+ ____MAensureExtension_block_invoke.1228
+ ____MAsendDownloadAsset_block_invoke.1130
+ ____MAsendPMVCancelDownload_block_invoke.1148
+ ____MAsendPMVDownload_block_invoke.1136
+ ___block_literal_global.1042
+ ___block_literal_global.1052
+ ___block_literal_global.1053
+ ___block_literal_global.1088
+ ___block_literal_global.1094
+ ___block_literal_global.1104
+ ___block_literal_global.1109
+ ___block_literal_global.1133
+ ___block_literal_global.1279
+ ___block_literal_global.1284
+ ___block_literal_global.1286
+ ___block_literal_global.1324
+ ___block_literal_global.1346
+ ___block_literal_global.2710
+ ___block_literal_global.2712
+ ___block_literal_global.2714
+ ___block_literal_global.2716
+ _objc_msgSend$isThirdPartyAssetType:
- +[MAThirdPartyCompatibility _sanitizedURLPathComponentFor:]
- _OBJC_CLASS_$_SUCoreDevice
- __MAPreferencesCopyNSStringValue
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1055
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke.1056
- ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1081
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1050
- ___95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1051
- ___Block_byref_object_copy_.1218
- ___Block_byref_object_dispose_.1219
- ____MAensureExtension_block_invoke.1225
- ____MAsendDownloadAsset_block_invoke.1127
- ____MAsendPMVCancelDownload_block_invoke.1145
- ____MAsendPMVDownload_block_invoke.1133
- ___block_literal_global.1039
- ___block_literal_global.1049
- ___block_literal_global.1050
- ___block_literal_global.1085
- ___block_literal_global.1091
- ___block_literal_global.1101
- ___block_literal_global.1106
- ___block_literal_global.1130
- ___block_literal_global.1270
- ___block_literal_global.1275
- ___block_literal_global.1277
- ___block_literal_global.1321
- ___block_literal_global.1343
- ___block_literal_global.2707
- ___block_literal_global.2709
- ___block_literal_global.2711
- ___block_literal_global.2713
- _kMobileAssetPreferencesThirdPartyStagingBucketPathComponent
- _kMobileAssetPreferencesThirdPartyStagingPathComponent
- _objc_msgSend$_sanitizedURLPathComponentFor:
- _objc_msgSend$addCharactersInString:
- _objc_msgSend$alphanumericCharacterSet
- _objc_msgSend$isBootedOSSecureInternal
- _objc_msgSend$precomposedStringWithCanonicalMapping
- _objc_msgSend$sharedDevice
- _objc_msgSend$stringValue
Functions:
~ -[MAAsset commonAssetDownload:options:then:] : 988 -> 1028
- __MAPreferencesCopyNSStringValue
~ +[MAThirdPartyCompatibility defaultThirdPartyServerURLForAssetType:] : 692 -> 308
- +[MAThirdPartyCompatibility _sanitizedURLPathComponentFor:]
CStrings:
+ "Failed to retrieve server url for:(%@) from daemon. %ld"
+ "Using caching server for %{public}@ %{public}@ is enabled: %d"
- "-_"
- "MAThirdPartyCompatibility: %@ override (%@) provided, with illegal characters."
- "The cache server is: %d"
- "ThirdPartyStagingBucketPathComponent"
- "ThirdPartyStagingPathComponent"
- "[MA_PREFS] {_MAPreferencesCopyNSStringValue} invalid type for key:%{public}@ | expecting string or number or boolean"
- "_sanitizedURLPathComponentFor:"
- "addCharactersInString:"
- "alphanumericCharacterSet"
- "https://mesu.apple.com/3p/%@/%@/assets/%@/%@/"
- "https://mesu.apple.com/3p/%@/assets/%@/%@/"
- "https://mesu.apple.com/3p/assets/%@/%@/"
- "https://mesu.apple.com/3p/staging/assets/%@/%@/"
- "ios"
- "isBootedOSSecureInternal"
- "precomposedStringWithCanonicalMapping"
- "sharedDevice"
- "stringValue"

```
