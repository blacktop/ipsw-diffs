## WiFiKit

> `/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`

```diff

-885.19.0.0.0
-  __TEXT.__text: 0x8f840
+890.2.0.0.0
+  __TEXT.__text: 0x8f9c8
   __TEXT.__auth_stubs: 0x14c0
   __TEXT.__objc_methlist: 0x7e44
   __TEXT.__const: 0x188
-  __TEXT.__oslogstring: 0xa132
+  __TEXT.__oslogstring: 0xa16d
   __TEXT.__cstring: 0xa5d8
-  __TEXT.__gcc_except_tab: 0x1878
+  __TEXT.__gcc_except_tab: 0x18a0
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x1a48
+  __TEXT.__unwind_info: 0x1a88
   __TEXT.__objc_classname: 0xe17
-  __TEXT.__objc_methname: 0x1466e
+  __TEXT.__objc_methname: 0x14680
   __TEXT.__objc_methtype: 0x29f5
-  __TEXT.__objc_stubs: 0xdca0
+  __TEXT.__objc_stubs: 0xdcc0
   __DATA_CONST.__got: 0x550
   __DATA_CONST.__const: 0x2090
   __DATA_CONST.__objc_classlist: 0x338

   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x181d0
-  __DATA_CONST.__objc_selrefs: 0x4700
+  __DATA_CONST.__objc_selrefs: 0x4708
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x658
   __DATA_CONST.__objc_superrefs: 0x288

   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__const: 0x3a0
   __AUTH_CONST.__auth_got: 0xa70
-  __AUTH.__objc_data: 0x15e0
+  __AUTH.__objc_data: 0x1590
   __DATA.__objc_ivar: 0xb74
   __DATA.__data: 0x1290
   __DATA.__bss: 0xc8
-  __DATA_DIRTY.__objc_data: 0xa50
+  __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__bss: 0x98
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystemHealth.dylib
   - /usr/lib/libnetquality.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B64C1A38-4490-34BB-8D1E-641F6C799D12
+  UUID: 137CF252-EAB5-304E-9D97-C2D00BD06ABF
   Functions: 3121
-  Symbols:   11125
-  CStrings:  7248
+  Symbols:   11126
+  CStrings:  7250
 
Symbols:
+ ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.159
+ ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.160
+ ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.164
+ ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.165
+ ___57-[WFNetworkListController _canStartAssociationToNetwork:]_block_invoke.240
+ ___57-[WFNetworkListController _canStartAssociationToNetwork:]_block_invoke.241
+ ___59-[WFNetworkListController _associateToUserSuppliedNetwork:]_block_invoke.213
+ ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.125
+ ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.138
+ ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke.499
+ ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke.502
+ ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke_2.500
+ ___62-[WFNetworkListController _scanNetworkForAssociation:profile:]_block_invoke.249
+ ___63-[WFNetworkListController _associationDidFinish:error:network:]_block_invoke.246
+ ___63-[WFNetworkListController _refreshKnownHiddenNetworkNamesCache]_block_invoke.509
+ ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.228
+ ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.229
+ ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.235
+ ___69-[WFNetworkListController _canStartAssociationToUserSuppliedNetwork:]_block_invoke.243
+ ___71-[WFNetworkListController networkListViewControllerDidTapOtherNetwork:]_block_invoke.291
+ ___74-[WFNetworkListController _associateToUserSuppliedNetworkHelper:networks:]_block_invoke.216
+ ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.317
+ ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.371
+ ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.378
+ ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke.218
+ ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke.219
+ ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke_2.221
+ ___block_literal_global.224
+ ___block_literal_global.311
+ ___block_literal_global.437
+ ___block_literal_global.491
+ ___block_literal_global.497
+ _objc_msgSend$networkListVisible
- ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.157
- ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.158
- ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.162
- ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.163
- ___57-[WFNetworkListController _canStartAssociationToNetwork:]_block_invoke.237
- ___57-[WFNetworkListController _canStartAssociationToNetwork:]_block_invoke.238
- ___59-[WFNetworkListController _associateToUserSuppliedNetwork:]_block_invoke.209
- ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.123
- ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.134
- ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke.497
- ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke.500
- ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke_2.498
- ___62-[WFNetworkListController _scanNetworkForAssociation:profile:]_block_invoke.247
- ___63-[WFNetworkListController _associationDidFinish:error:network:]_block_invoke.244
- ___63-[WFNetworkListController _refreshKnownHiddenNetworkNamesCache]_block_invoke.507
- ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.226
- ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.227
- ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.233
- ___69-[WFNetworkListController _canStartAssociationToUserSuppliedNetwork:]_block_invoke.241
- ___71-[WFNetworkListController networkListViewControllerDidTapOtherNetwork:]_block_invoke.289
- ___74-[WFNetworkListController _associateToUserSuppliedNetworkHelper:networks:]_block_invoke.214
- ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.313
- ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.366
- ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.367
- ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke.216
- ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke.217
- ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke_2.219
- ___block_literal_global.222
- ___block_literal_global.309
- ___block_literal_global.435
- ___block_literal_global.489
- ___block_literal_global.495
CStrings:
+ "%s: Skipping scanning for setup until wifi page is visible"
+ "networkListVisible"

```
