## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-304.2.6.100.0
-  __TEXT.__text: 0x4b064
+304.3.3.0.0
+  __TEXT.__text: 0x4be20
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0x3c1c
+  __TEXT.__objc_methlist: 0x3c94
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x481a
+  __TEXT.__cstring: 0x4944
   __TEXT.__gcc_except_tab: 0x90c
   __TEXT.__oslogstring: 0x2867
   __TEXT.__dlopen_cstrs: 0x244
-  __TEXT.__unwind_info: 0x1060
+  __TEXT.__unwind_info: 0x1080
   __TEXT.__objc_classname: 0x89a
-  __TEXT.__objc_methname: 0xa5f6
-  __TEXT.__objc_methtype: 0x1b71
-  __TEXT.__objc_stubs: 0x60c0
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__const: 0x11c8
+  __TEXT.__objc_methname: 0xa945
+  __TEXT.__objc_methtype: 0x1c38
+  __TEXT.__objc_stubs: 0x6200
+  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__const: 0x1218
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f08
+  __DATA_CONST.__objc_selrefs: 0x1f68
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f8
   __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x3740
-  __AUTH_CONST.__objc_const: 0xc240
+  __AUTH_CONST.__cfstring: 0x37a0
+  __AUTH_CONST.__objc_const: 0xc2e8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xb40
-  __DATA.__objc_ivar: 0x42c
+  __DATA.__objc_ivar: 0x430
   __DATA.__data: 0x5c0
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0xa00

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1B843D39-3D90-3EDA-940B-2425EA7007E9
-  Functions: 1720
-  Symbols:   6103
-  CStrings:  2935
+  UUID: 8382078E-5578-356A-9643-D299C28F8EA7
+  Functions: 1734
+  Symbols:   6150
+  CStrings:  2963
 
Symbols:
+ -[PRSPosterGallerySection associatedAppBundleIdentifier]
+ -[PRSPosterGallerySection initWithType:localizedTitle:localizedSubtitle:localizedDescriptiveText:associatedAppBundleIdentifier:symbolImageName:symbolColorName:unityDescription:items:]
+ -[PRSServer augmentDownloadablePosterMetadataForApp:sandboxExtendedBundleURL:bundleIdentifierOverride:completion:]
+ -[PRSServer fetchAvailableExtensionIdentifiers:]
+ -[PRSServer fetchExtensionAuditTokenWithError:]
+ -[PRSService augmentDownloadablePosterMetadataForApp:bundleURL:bundleIdentifierOverride:completion:]
+ -[PRSService augmentDownloadablePosterMetadataForApp:bundleURL:bundleIdentifierOverride:completion:].cold.1
+ -[PRSService augmentDownloadablePosterMetadataForApp:bundleURL:bundleIdentifierOverride:completion:].cold.2
+ -[PRSService augmentDownloadablePosterMetadataForApp:bundleURL:bundleIdentifierOverride:completion:].cold.3
+ -[PRSService fetchAvailableExtensionIdentifiers:]
+ -[PRSService fetchAvailableExtensionIdentifiers:].cold.1
+ _OBJC_CLASS_$_CHSWidget
+ _OBJC_CLASS_$_PFSandboxExtendedURL
+ _OBJC_IVAR_$_PRSPosterGallerySection._associatedAppBundleIdentifier
+ ___100-[PRSService augmentDownloadablePosterMetadataForApp:bundleURL:bundleIdentifierOverride:completion:]_block_invoke
+ ___100-[PRSService augmentDownloadablePosterMetadataForApp:bundleURL:bundleIdentifierOverride:completion:]_block_invoke.cold.1
+ ___35-[PRSPosterGallerySection isEqual:]_block_invoke_9
+ ___49-[PRSService fetchAvailableExtensionIdentifiers:]_block_invoke
+ ___49-[PRSService fetchAvailableExtensionIdentifiers:]_block_invoke.cold.1
+ ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.141
+ ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.141.cold.1
+ ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.137
+ ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.139
+ ___block_descriptor_56_e8_32s40bs_e27_v24?0"NSSet"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8
+ _objc_msgSend$associatedAppBundleIdentifier
+ _objc_msgSend$augmentDownloadablePosterMetadataForApp:sandboxExtendedBundleURL:bundleIdentifierOverride:completion:
+ _objc_msgSend$fetchAvailableExtensionIdentifiers:
+ _objc_msgSend$fetchExtensionAuditTokenWithError:
+ _objc_msgSend$initWithExtensionIdentity:kind:family:intent:activityIdentifier:
+ _objc_msgSend$initWithType:localizedTitle:localizedSubtitle:localizedDescriptiveText:associatedAppBundleIdentifier:symbolImageName:symbolColorName:unityDescription:items:
+ _objc_msgSend$intentReference
+ _objc_msgSend$sandboxExtendedURLForURL:options:auditToken:error:
+ _objc_msgSend$server:augmentDownloadablePosterMetadataForApp:sandboxExtendedBundleURL:bundleIdentifierOverride:completion:
+ _objc_msgSend$server:fetchAvailableExtensionIdentifiers:
+ _objc_msgSend$setAssociatedAppBundleIdentifier:
- ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.140
- ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.140.cold.1
- ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.136
- ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.138
- _objc_msgSend$initWithType:localizedTitle:localizedSubtitle:localizedDescriptiveText:symbolImageName:symbolColorName:unityDescription:items:
CStrings:
+ "-[PRSServer augmentDownloadablePosterMetadataForApp:sandboxExtendedBundleURL:bundleIdentifierOverride:completion:]"
+ "-[PRSServer fetchAvailableExtensionIdentifiers:]"
+ "-[PRSServer fetchExtensionAuditTokenWithError:]"
+ "@\"BSAuditToken\"24@0:8o^@16"
+ "@88@0:8q16@24@32@40@48@56@64@72@80"
+ "Failed to fetch audit token"
+ "T@\"NSString\",R,C,N,V_associatedAppBundleIdentifier"
+ "Vv24@0:8@?<v@?@\"NSSet<__NSString__>\"@\"NSError\">16"
+ "Vv48@0:8@\"NSString\"16@\"PFSandboxExtendedURL\"24@\"NSString\"32@?<v@?@\"NSURL\"@\"NSError\">40"
+ "_associatedAppBundleIdentifier"
+ "appBundleIdentifier"
+ "associatedAppBundleIdentifier"
+ "augmentDownloadablePosterMetadataForApp:bundleURL:bundleIdentifierOverride:completion:"
+ "augmentDownloadablePosterMetadataForApp:sandboxExtendedBundleURL:bundleIdentifierOverride:completion:"
+ "bundleURL"
+ "fetchAvailableExtensionIdentifiers:"
+ "fetchExtensionAuditTokenWithError:"
+ "initWithExtensionIdentity:kind:family:intent:activityIdentifier:"
+ "initWithType:localizedTitle:localizedSubtitle:localizedDescriptiveText:associatedAppBundleIdentifier:symbolImageName:symbolColorName:unityDescription:items:"
+ "intentReference"
+ "sandboxExtendedURLForURL:options:auditToken:error:"
+ "server:augmentDownloadablePosterMetadataForApp:sandboxExtendedBundleURL:bundleIdentifierOverride:completion:"
+ "server:fetchAvailableExtensionIdentifiers:"
+ "setAssociatedAppBundleIdentifier:"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"

```
