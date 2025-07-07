## SoftwareUpdateSettings

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings`

```diff

-492.0.0.0.5
+508.0.1.502.1
   __TEXT.__text: 0x1f054
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_methlist: 0x110c
-  __TEXT.__cstring: 0x1e7a
+  __TEXT.__cstring: 0x1e9a
   __TEXT.__gcc_except_tab: 0x1c4
   __TEXT.__oslogstring: 0x7ad
   __TEXT.__dlopen_cstrs: 0xfe

   __TEXT.__objc_methtype: 0xf46
   __TEXT.__objc_stubs: 0x2e80
   __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x838
+  __DATA_CONST.__const: 0x840
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x538
   __AUTH_CONST.__const: 0x268
-  __AUTH_CONST.__cfstring: 0x1ce0
+  __AUTH_CONST.__cfstring: 0x1d00
   __AUTH_CONST.__objc_const: 0x2ca0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5F9B94F1-01B7-30FD-8608-8322BB4055EB
+  UUID: C598FA7F-F4B2-3EDB-B5EE-77769D538BE0
   Functions: 541
-  Symbols:   1803
-  CStrings:  1395
+  Symbols:   1804
+  CStrings:  1397
 
Symbols:
+ _MA_ASSET_PROPERTY_ALLOW_USER_INTERACTION
+ ___108-[SUSSoftwareUpdateTermsManager presentTermsIfNecessaryForUpdate:overController:showLoadSpinner:completion:]_block_invoke.443
+ ___61-[SUSSoftwareUpdateTermsManager _handleAgreeFromObjectModel:]_block_invoke.558
+ ___66-[SUSSoftwareUpdateTermsManager _loadRemoteUITermsWithCloudAtURL:]_block_invoke.499
- ___108-[SUSSoftwareUpdateTermsManager presentTermsIfNecessaryForUpdate:overController:showLoadSpinner:completion:]_block_invoke.440
- ___61-[SUSSoftwareUpdateTermsManager _handleAgreeFromObjectModel:]_block_invoke.555
- ___66-[SUSSoftwareUpdateTermsManager _loadRemoteUITermsWithCloudAtURL:]_block_invoke.496
CStrings:
+ "%s Overriding the default Coming Soon tip content and returning UserDefaultsBasedComingSoonTip instead.\nForce show: %{bool}d\nForce hide: %{bool}d\nTitle: %s\nMessage: %s\nImageSystemName: %s\nLearn More URL: %s"
+ "Indicates whether the \"Coming Soon\" tip should be forcibly hidden regardless of its Constellation display criterias"
+ "Indicates whether the \"Coming Soon\" tip should be forcibly shown regardless of its "
+ "_AllowUserInteraction"
- "%s Overring the default Coming Soon tip content and returning UserDefaultsBasedComingSoonTip instead.\nForce show: %{bool}d\nForce hide: %{bool}d\nTitle: %s\nMessage: %s\nImageSystemName: %s\nLearn More URL: %s"
- "Indicates whether the \"Coming Soon\" tip should be forcely hidden regardless of its Constellation display criterias"
- "Indicates whether the \"Coming Soon\" tip should be forcely shown regardless of its "

```
