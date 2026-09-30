## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-1112.0.3.0.0
-  __TEXT.__text: 0x670cc
+1114.40.9.0.0
+  __TEXT.__text: 0x67374
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0x7064
+  __TEXT.__objc_methlist: 0x708c
   __TEXT.__const: 0x5aa
   __TEXT.__gcc_except_tab: 0xc34
-  __TEXT.__cstring: 0x15491
+  __TEXT.__cstring: 0x15531
   __TEXT.__oslogstring: 0x93c
   __TEXT.__swift5_typeref: 0x205
   __TEXT.__swift5_capture: 0x124

   __TEXT.__swift_as_entry: 0x58
   __TEXT.__swift_as_ret: 0x84
   __TEXT.__swift_as_cont: 0xa0
-  __TEXT.__unwind_info: 0x2630
+  __TEXT.__unwind_info: 0x2640
   __TEXT.__eh_frame: 0xc18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4038
+  __DATA_CONST.__objc_selrefs: 0x4050
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x7c8
   __AUTH_CONST.__const: 0x990
-  __AUTH_CONST.__cfstring: 0xdf60
-  __AUTH_CONST.__objc_const: 0xdf18
+  __AUTH_CONST.__cfstring: 0xdfc0
+  __AUTH_CONST.__objc_const: 0xdf58
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x8b0
   __AUTH.__objc_data: 0xfd0
   __AUTH.__data: 0x128
-  __DATA.__objc_ivar: 0x6cc
+  __DATA.__objc_ivar: 0x6d0
   __DATA.__data: 0xa14
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xd98

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2907
-  Symbols:   6376
-  CStrings:  2222
+  Functions: 2912
+  Symbols:   6384
+  CStrings:  2225
 
Symbols:
+ -[SUDownloadOptions personalizationServerURL]
+ -[SUDownloadOptions setPersonalizationServerURL:]
+ -[SUPreferences overridePersonalizationURL]
+ _OBJC_IVAR_$_SUDownloadOptions._personalizationServerURL
+ ___45-[SUDownloadOptions personalizationServerURL]_block_invoke
+ ___49-[SUDownloadOptions setPersonalizationServerURL:]_block_invoke
+ _objc_msgSend$personalizationServerURL
+ _objc_msgSend$setPersonalizationServerURL:
CStrings:
+ "\n            ClientName: %@\n            downloadOnly: %@\n            autoDownload: %@\n            userUpdateTonight: %@\n            allowUnrestrictedCellularDownload: %@\n            downloadFeeAgreementStatus: %@\n            termsAndConditionsAgreementStatus: %@\n            activeDownloadPolicyType: %@\n            enabledForCellular: %@\n            enabledForWifi: %@\n            enabledOnBatteryPower: %@\n            enabledForCellularRoaming: %@\n            personalizationServerURL: %@\n            descriptor: %@\n"
+ "!$"
+ "Override Tatsu personalization URL; used when the client does not supply one"
+ "SUOverridePersonalizationURL"
+ "[Auto download] Beta: Downloading every 1 day"
+ "personalizationServerURL"
- "\n            ClientName: %@\n            downloadOnly: %@\n            autoDownload: %@\n            userUpdateTonight: %@\n            allowUnrestrictedCellularDownload: %@\n            downloadFeeAgreementStatus: %@\n            termsAndConditionsAgreementStatus: %@\n            activeDownloadPolicyType: %@\n            enabledForCellular: %@\n            enabledForWifi: %@\n            enabledOnBatteryPower: %@\n            enabledForCellularRoaming: %@\n            descriptor: %@\n"
- "!#"
- "[Auto download] Customer: Downloading every 5 days"
```
