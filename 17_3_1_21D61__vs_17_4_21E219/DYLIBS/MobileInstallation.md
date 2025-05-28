## MobileInstallation

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation`

```diff

-1270.80.2.0.0
-  __TEXT.__text: 0x1c58c
+1270.102.7.0.0
+  __TEXT.__text: 0x1cd28
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0xc10
-  __TEXT.__cstring: 0x4110
-  __TEXT.__gcc_except_tab: 0x8c0
+  __TEXT.__objc_methlist: 0xc40
+  __TEXT.__cstring: 0x43ee
+  __TEXT.__gcc_except_tab: 0x8d8
   __TEXT.__const: 0x30
   __TEXT.__oslogstring: 0x43
-  __TEXT.__unwind_info: 0x8f8
+  __TEXT.__unwind_info: 0x910
   __TEXT.__objc_classname: 0x167
-  __TEXT.__objc_methname: 0x37f4
-  __TEXT.__objc_methtype: 0xeee
-  __TEXT.__objc_stubs: 0x2880
+  __TEXT.__objc_methname: 0x385c
+  __TEXT.__objc_methtype: 0xf38
+  __TEXT.__objc_stubs: 0x28e0
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x7d0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x15b0
-  __DATA_CONST.__objc_selrefs: 0xb48
+  __DATA_CONST.__objc_const: 0x1640
+  __DATA_CONST.__objc_selrefs: 0xb68
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__cfstring: 0x24c0
+  __AUTH_CONST.__cfstring: 0x2780
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x470
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x100
-  __DATA.__objc_superrefs: 0x38
-  __DATA.__objc_ivar: 0xe0
-  __DATA.__data: 0x258
+  __DATA.__objc_ivar: 0xe8
+  __DATA.__data: 0x278
   __DATA.__bss: 0x38
   __DATA.__common: 0x8
   __DATA_DIRTY.__const: 0xc0
   __DATA_DIRTY.__objc_const: 0x578
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 598
-  Symbols:   1968
-  CStrings:  1077
+  Functions: 613
+  Symbols:   2004
+  CStrings:  1109
 
Symbols:
+ -[MIInstallOptions installIntent]
+ -[MIInstallOptions installTypeSummaryString]
+ -[MIInstallOptions setInstallIntent:]
+ -[MIInstallOptions setSinfDataType:]
+ -[MIInstallOptions sinfDataType]
+ -[MIInstallerClient setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:]
+ -[MIInstallerClient updateiTunesMetadataForIXWithIdentifier:metadata:completion:]
+ GCC_except_table185
+ GCC_except_table198
+ GCC_except_table201
+ GCC_except_table204
+ GCC_except_table207
+ GCC_except_table224
+ GCC_except_table232
+ GCC_except_table241
+ GCC_except_table243
+ GCC_except_table245
+ GCC_except_table247
+ GCC_except_table249
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table255
+ GCC_except_table262
+ GCC_except_table264
+ GCC_except_table266
+ GCC_except_table268
+ GCC_except_table270
+ GCC_except_table280
+ GCC_except_table290
+ GCC_except_table294
+ GCC_except_table3
+ GCC_except_table300
+ GCC_except_table302
+ GCC_except_table304
+ GCC_except_table308
+ GCC_except_table313
+ GCC_except_table323
+ GCC_except_table325
+ GCC_except_table327
+ _MIArrayFilteredToContainOnlyClass
+ _MICopyDataProtectionClassEntitlement
+ _MICopyDataProtectionIfAvailableEntitlement
+ _MICopyMemoryTransferAcceptEntitlement
+ _MICopyMemoryTransferSendEntitlement
+ _MIGetFirstTrueBooleanEntitlement
+ _MIHasAllowJITEntitlement
+ _MIHasBrowserAppInstallationEntitlement
+ _MIHasBrowserEngineContentEntitlement
+ _MIHasBrowserEngineHostEntitlement
+ _MIHasBrowserEngineNetworkingEntitlement
+ _MIHasBrowserEngineRenderingEntitlement
+ _MIHasDefaultBrowserEntitlement
+ _MIHasEmbeddedBrowserEngineEntitlement
+ _MIHasMarketplaceEntitlement
+ _MISetLaunchWarning
+ _OBJC_IVAR_$_MIInstallOptions._installIntent
+ _OBJC_IVAR_$_MIInstallOptions._sinfDataType
+ ___81-[MIInstallerClient updateiTunesMetadataForIXWithIdentifier:metadata:completion:]_block_invoke
+ ___81-[MIInstallerClient updateiTunesMetadataForIXWithIdentifier:metadata:completion:]_block_invoke_2
+ ___81-[MIInstallerClient updateiTunesMetadataForIXWithIdentifier:metadata:completion:]_block_invoke_3
+ ___81-[MIInstallerClient updateiTunesMetadataForIXWithIdentifier:metadata:completion:]_block_invoke_4
+ ___95-[MIInstallerClient setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:]_block_invoke
+ ___95-[MIInstallerClient setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:]_block_invoke_2
+ ___95-[MIInstallerClient setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:]_block_invoke_3
+ ___95-[MIInstallerClient setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:]_block_invoke_4
+ ___MISetLaunchWarning_block_invoke
+ __unnamed_array_storage.175
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$installIntent
+ _objc_msgSend$propertyListDataWithError:
+ _objc_msgSend$setInstallIntent:
+ _objc_msgSend$setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:
+ _objc_msgSend$setSinfDataType:
+ _objc_msgSend$sinfDataType
+ _objc_msgSend$updateiTunesMetadataForIXWithIdentifier:metadata:completion:
- -[MIInstallerClient updateSinfForLSWithIdentifier:withOptions:sinfData:completion:]
- -[MIInstallerClient updateiTunesMetadataForIXWithIdentifier:options:plistData:completion:]
- -[MIInstallerClient updateiTunesMetadataForLSWithIdentifier:options:plistData:completion:]
- GCC_except_table200
- GCC_except_table203
- GCC_except_table206
- GCC_except_table209
- GCC_except_table212
- GCC_except_table234
- GCC_except_table242
- GCC_except_table246
- GCC_except_table248
- GCC_except_table250
- GCC_except_table252
- GCC_except_table254
- GCC_except_table256
- GCC_except_table263
- GCC_except_table265
- GCC_except_table267
- GCC_except_table269
- GCC_except_table271
- GCC_except_table275
- GCC_except_table278
- GCC_except_table298
- GCC_except_table301
- GCC_except_table303
- GCC_except_table307
- GCC_except_table309
- GCC_except_table311
- GCC_except_table315
- GCC_except_table320
- GCC_except_table330
- GCC_except_table332
- _MobileInstallationUpdateSinfForInstallCoordination
- _MobileInstallationUpdateSinfForInstallCoordinationWithWrapperURL
- ___83-[MIInstallerClient updateSinfForLSWithIdentifier:withOptions:sinfData:completion:]_block_invoke
- ___83-[MIInstallerClient updateSinfForLSWithIdentifier:withOptions:sinfData:completion:]_block_invoke_2
- ___83-[MIInstallerClient updateSinfForLSWithIdentifier:withOptions:sinfData:completion:]_block_invoke_3
- ___83-[MIInstallerClient updateSinfForLSWithIdentifier:withOptions:sinfData:completion:]_block_invoke_4
- ___90-[MIInstallerClient updateiTunesMetadataForIXWithIdentifier:options:plistData:completion:]_block_invoke
- ___90-[MIInstallerClient updateiTunesMetadataForIXWithIdentifier:options:plistData:completion:]_block_invoke_2
- ___90-[MIInstallerClient updateiTunesMetadataForIXWithIdentifier:options:plistData:completion:]_block_invoke_3
- ___90-[MIInstallerClient updateiTunesMetadataForIXWithIdentifier:options:plistData:completion:]_block_invoke_4
- ___90-[MIInstallerClient updateiTunesMetadataForLSWithIdentifier:options:plistData:completion:]_block_invoke
- ___90-[MIInstallerClient updateiTunesMetadataForLSWithIdentifier:options:plistData:completion:]_block_invoke_2
- ___90-[MIInstallerClient updateiTunesMetadataForLSWithIdentifier:options:plistData:completion:]_block_invoke_3
- ___90-[MIInstallerClient updateiTunesMetadataForLSWithIdentifier:options:plistData:completion:]_block_invoke_4
- __unnamed_array_storage.176
- _objc_msgSend$dictionaryRepresentation
- _objc_msgSend$legacySinfInfoDictionary
- _objc_msgSend$updateSinfForLSWithIdentifier:withOptions:sinfData:completion:
- _objc_msgSend$updateiTunesMetadataForIXWithIdentifier:options:plistData:completion:
- _objc_msgSend$updateiTunesMetadataForLSWithIdentifier:options:plistData:completion:
CStrings:
+ "ApplicationSINFDataType"
+ "DataProtectionClass"
+ "Intent"
+ "Offload"
+ "Skipping offload of marketplace %@ at %@"
+ "T@\"NSString\",R,N"
+ "TI,N,V_sinfDataType"
+ "TQ,N,V_installIntent"
+ "_installIntent"
+ "_sinfDataType"
+ "arrayWithCapacity:"
+ "com.apple.developer.browser.app-installation"
+ "com.apple.developer.cs.allow-jit"
+ "com.apple.developer.default-data-protection"
+ "com.apple.developer.default-data-protection-if-available"
+ "com.apple.developer.embedded-web-browser-engine"
+ "com.apple.developer.marketplace.app-installation"
+ "com.apple.developer.memory.transfer-accept"
+ "com.apple.developer.memory.transfer-send"
+ "com.apple.developer.web-browser"
+ "com.apple.developer.web-browser-engine.host"
+ "com.apple.developer.web-browser-engine.networking"
+ "com.apple.developer.web-browser-engine.rendering"
+ "com.apple.developer.web-browser-engine.webcontent"
+ "data-protection-class"
+ "installIntent"
+ "installTypeSummaryString"
+ "propertyListDataWithError:"
+ "setInstallIntent:"
+ "setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:"
+ "setSinfDataType:"
+ "sinfDataType"
+ "updateiTunesMetadataForIXWithIdentifier:metadata:completion:"
+ "v20@0:8I16"
+ "v40@0:8@\"NSString\"16@\"MIStoreMetadata\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSURL\"16@\"MIInstallOptions\"24@?<v@?@\"NSURL\"B@\"NSError\">32"
+ "v48@0:8@\"MIAppIdentity\"16@\"NSData\"24@\"NSData\"32@?<v@?@\"NSError\">40"
- "dictionaryRepresentation"
- "legacySinfInfoDictionary"
- "updateSinfForLSWithIdentifier:withOptions:sinfData:completion:"
- "updateiTunesMetadataForIXWithIdentifier:options:plistData:completion:"
- "updateiTunesMetadataForLSWithIdentifier:options:plistData:completion:"
- "v40@0:8@\"NSURL\"16@\"NSDictionary\"24@?<v@?@\"NSURL\"B@\"NSError\">32"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSData\"32@?<v@?@\"NSError\">40"

```
