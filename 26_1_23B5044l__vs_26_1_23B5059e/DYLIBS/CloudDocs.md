## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-4257.40.32.502.1
-  __TEXT.__text: 0x8b540
+4257.40.57.0.1
+  __TEXT.__text: 0x8b77c
   __TEXT.__auth_stubs: 0x13b0
-  __TEXT.__objc_methlist: 0x6754
+  __TEXT.__objc_methlist: 0x676c
   __TEXT.__const: 0x1c0
   __TEXT.__gcc_except_tab: 0x4c08
-  __TEXT.__cstring: 0xb63a
-  __TEXT.__oslogstring: 0x9518
+  __TEXT.__cstring: 0xb68f
+  __TEXT.__oslogstring: 0x9556
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x8
   __TEXT.__unwind_info: 0x2720
   __TEXT.__objc_classname: 0xdd2
-  __TEXT.__objc_methname: 0x10fab
+  __TEXT.__objc_methname: 0x11051
   __TEXT.__objc_methtype: 0x3c61
   __TEXT.__objc_stubs: 0xb180
-  __DATA_CONST.__got: 0x8b0
-  __DATA_CONST.__const: 0x2680
+  __DATA_CONST.__got: 0x8b8
+  __DATA_CONST.__const: 0x2688
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41f0
+  __DATA_CONST.__objc_selrefs: 0x4208
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0x9e8
   __AUTH_CONST.__const: 0x1120
-  __AUTH_CONST.__cfstring: 0x5ca0
-  __AUTH_CONST.__objc_const: 0xcbc8
+  __AUTH_CONST.__cfstring: 0x5ce0
+  __AUTH_CONST.__objc_const: 0xcbd0
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_intobj: 0x510
+  __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x1540
   __AUTH.__data: 0xa8
   __DATA.__objc_ivar: 0x654
   __DATA.__data: 0xd90
-  __DATA.__bss: 0x3f0
+  __DATA.__bss: 0x3e8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x290
+  __DATA_DIRTY.__bss: 0x298
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: BFBEA251-247C-3697-8271-B3FCFC55631B
-  Functions: 3096
-  Symbols:   10824
-  CStrings:  6243
+  UUID: 3F7D7A06-25A5-3794-AC5A-8633E7FD4CF7
+  Functions: 3099
+  Symbols:   10831
+  CStrings:  6251
 
Symbols:
+ +[BRFileProviderServicesFactory _fetchSynchronousAutomaticErrorProxyFromURL:serviceName:interface:]
+ +[BRPosixOperationsWrapper consumeSandboxExtension:error:].cold.1
+ +[NSError(BRAdditions) brc_errorNetworkUnreachableDueToCellularOverICDDisabled]
+ _BRiCloudIconUTI
+ ____fetchServiceAutomaticErrorProxyFromURL_block_invoke.10
+ ____fetchServiceAutomaticErrorProxyFromURL_block_invoke.11
+ ___block_literal_global.118
+ ___block_literal_global.420
+ ___block_literal_global.432
+ ___block_literal_global.464
+ ___block_literal_global.481
- ____fetchServiceAutomaticErrorProxyFromURL_block_invoke.8
- ____fetchServiceAutomaticErrorProxyFromURL_block_invoke.9
- ___block_literal_global.116
- ___block_literal_global.419
- ___block_literal_global.431
- ___block_literal_global.463
- ___block_literal_global.480
Functions:
~ ___61-[NSError(BRFPAdditions) _br_getFileProviderDomainErrorCode:]_block_invoke : 944 -> 988
~ -[NSError(BRFPAdditions) _isTransientError:code:] : 140 -> 156
+ +[BRFileProviderServicesFactory _fetchSynchronousAutomaticErrorProxyFromURL:serviceName:interface:]
~ +[BRPosixOperationsWrapper consumeSandboxExtension:error:] : 352 -> 692
+ +[NSError(BRAdditions) brc_errorNetworkUnreachable]
~ +[NSJSONSerialization(BRAdditions) jsonStringFromDictionary:options:error:] : 212 -> 216
+ +[BRPosixOperationsWrapper consumeSandboxExtension:error:].cold.1
CStrings:
+ "4257.40.57.0.1"
+ "[CRIT] UNREACHABLE: Trying to consume nil sandbox extension%@"
+ "_fetchSynchronousAutomaticErrorProxyFromURL:serviceName:interface:"
+ "brc_errorNetworkUnreachableDueToCellularOverICDDisabled"
+ "calculateSignatureForItemIdentifier:reply:"
+ "com.apple.application-icon.icloud"
+ "unreachable: Trying to consume nil sandbox extension"
- "4257.40.32.502.1"

```
