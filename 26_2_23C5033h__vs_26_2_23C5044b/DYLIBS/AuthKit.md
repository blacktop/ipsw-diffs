## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.250.5.0.0
-  __TEXT.__text: 0x185044
-  __TEXT.__auth_stubs: 0xc10
-  __TEXT.__objc_methlist: 0xe494
+525.250.9.0.0
+  __TEXT.__text: 0x1858d4
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_methlist: 0xe4ec
   __TEXT.__const: 0x69f8
-  __TEXT.__cstring: 0xfc0e
-  __TEXT.__gcc_except_tab: 0xa06c
-  __TEXT.__oslogstring: 0x128aa
+  __TEXT.__cstring: 0xfcbb
+  __TEXT.__gcc_except_tab: 0xa084
+  __TEXT.__oslogstring: 0x129ea
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x300
-  __TEXT.__unwind_info: 0x4260
+  __TEXT.__unwind_info: 0x4278
   __TEXT.__objc_classname: 0x1d7c
-  __TEXT.__objc_methname: 0x235c8
+  __TEXT.__objc_methname: 0x236f0
   __TEXT.__objc_methtype: 0x47c0
-  __TEXT.__objc_stubs: 0xff40
+  __TEXT.__objc_stubs: 0xffe0
   __DATA_CONST.__got: 0xa98
-  __DATA_CONST.__const: 0xa318
+  __DATA_CONST.__const: 0xa348
   __DATA_CONST.__objc_classlist: 0x680
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7370
+  __DATA_CONST.__objc_selrefs: 0x7398
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x2e8
-  __AUTH_CONST.__auth_got: 0x618
+  __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0x1400
-  __AUTH_CONST.__cfstring: 0x10460
-  __AUTH_CONST.__objc_const: 0x26648
+  __AUTH_CONST.__cfstring: 0x10500
+  __AUTH_CONST.__objc_const: 0x266e8
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH.__objc_data: 0x2c10
-  __DATA.__objc_ivar: 0x1068
+  __DATA.__objc_ivar: 0x1074
   __DATA.__data: 0x1900
   __DATA.__bss: 0x6f0
   __DATA_DIRTY.__objc_data: 0x14f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8D50AF9D-86C8-30FC-AC87-9A14E0F1F933
-  Functions: 5539
-  Symbols:   20951
-  CStrings:  12153
+  UUID: 4169B580-354F-3F77-B4CA-9F88973C69DC
+  Functions: 5545
+  Symbols:   20977
+  CStrings:  12178
 
Symbols:
+ -[AKAppleIDAuthenticationContext _shouldSendSigningHeadersForServerUI]
+ -[AKAppleIDAuthenticationContext set_shouldSendSigningHeadersForServerUI:]
+ -[AKAuthenticatableResource customShieldAssetID]
+ -[AKAuthenticatableResource setCustomShieldAssetID:]
+ -[AKFeatureManager refreshServerConfiguration]
+ _AKAppleAccountConsentShownKey
+ _AKURLBagKeyConsentRepromptDisabled
+ _OBJC_IVAR_$_AKAppleIDAuthenticationContext._shouldSendSigningHeadersForServerUI
+ _OBJC_IVAR_$_AKAuthenticatableResource._customShieldAssetID
+ _OBJC_IVAR_$_AKFeatureManager._cachedServerControlConsentRepromptDisabled
+ ___46-[AKFeatureManager refreshServerConfiguration]_block_invoke
+ ___block_descriptor_40_e8_32s_e20_v24?08"NSError"16ls32l8
+ ___block_descriptor_72_e8_32s40s48bs56bs64r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24lr64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.439
+ _objc_moveWeak
+ _objc_msgSend$_shouldSendSigningHeadersForServerUI
+ _objc_msgSend$configurationValueForKey:completion:
+ _objc_msgSend$refreshServerConfiguration
+ _objc_msgSend$setTeenRequiredToConnectToFamily:
+ _objc_msgSend$teenRequiredToConnectToFamily
+ _os_eligibility_fetch_newest_policies
- ___block_descriptor_72_e8_32s40s48bs56bs64r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8s40l8r64l8s48l8s56l8
- ___block_literal_global.436
CStrings:
+ "Failed to fetch server configuration for consent reprompt: %@"
+ "Failed to refresh OSEligibility policies, error code: %llu"
+ "Failed to refresh eligibility policies"
+ "OSEligibility API returned error code: %llu"
+ "Privacy version saving disabled by server configuration"
+ "Refreshing OSEligibility policies"
+ "Successfully refreshed OSEligibility policies"
+ "T@\"NSString\",C,N,V_customShieldAssetID"
+ "TB,N,V_shouldSendSigningHeadersForServerUI"
+ "Updated server configuration for consent reprompt disabled: %@"
+ "X-Apple-I-PrivacyConsent-Shown"
+ "_cachedServerControlConsentRepromptDisabled"
+ "_customShieldAssetID"
+ "_shouldSendSigningHeadersForServerUI"
+ "customShieldAssetID"
+ "disableConsentReprompt"
+ "refreshServerConfiguration"
+ "resourceType: %ld, resourceName: %@, customShieldTitle: %@, customShieldDetailText: %@, customShieldAssetID: %@"
+ "setCustomShieldAssetID:"
+ "set_shouldSendSigningHeadersForServerUI:"
- "refreshPolicies method is not yet implemented"
- "resourceType: %ld, resourceName: %@, customShieldTitle: %@, customShieldDetailText: %@"

```
