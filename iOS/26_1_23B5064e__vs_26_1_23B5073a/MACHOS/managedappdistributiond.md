## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

-3.1.12.6.0
-  __TEXT.__text: 0x65e2a4
-  __TEXT.__auth_stubs: 0x6480
+3.1.14.2.4
+  __TEXT.__text: 0x670b84
+  __TEXT.__auth_stubs: 0x64c0
   __TEXT.__objc_stubs: 0x1a80
   __TEXT.__objc_methlist: 0x21d4
-  __TEXT.__const: 0x3cce4
+  __TEXT.__const: 0x3fb40
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_methname: 0x6437
-  __TEXT.__cstring: 0xdf15
-  __TEXT.__oslogstring: 0x10782
+  __TEXT.__cstring: 0xdf45
+  __TEXT.__oslogstring: 0x10922
   __TEXT.__objc_classname: 0x3e9
   __TEXT.__objc_methtype: 0x150c
   __TEXT.__gcc_except_tab: 0x50c
   __TEXT.__dlopen_cstrs: 0xc8
   __TEXT.__constg_swiftt: 0x6730
-  __TEXT.__swift5_typeref: 0x59e0
+  __TEXT.__swift5_typeref: 0x59d4
   __TEXT.__swift5_proto: 0x1728
   __TEXT.__swift5_types: 0x93c
   __TEXT.__swift_as_entry: 0xa80
-  __TEXT.__swift_as_ret: 0x1458
+  __TEXT.__swift_as_ret: 0x1464
   __TEXT.__swift5_protos: 0xa4
-  __TEXT.__unwind_info: 0x11b00
-  __TEXT.__eh_frame: 0x36924
-  __DATA_CONST.__auth_got: 0x3250
-  __DATA_CONST.__got: 0x1db8
+  __TEXT.__unwind_info: 0x11b58
+  __TEXT.__eh_frame: 0x36bec
+  __DATA_CONST.__auth_got: 0x3270
+  __DATA_CONST.__got: 0x1d98
   __DATA_CONST.__auth_ptr: 0x1820
   __DATA_CONST.__const: 0x2dbd0
   __DATA_CONST.__cfstring: 0xae0

   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x6128
+  __DATA.__objc_const: 0x6148
   __DATA.__objc_selrefs: 0x1ca8
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x1f80
-  __DATA.__data: 0xd298
+  __DATA.__data: 0xd2a8
   __DATA.__bss: 0x2cc50
-  __DATA.__common: 0xcc0
+  __DATA.__common: 0xcc8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit
   - /System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 040B8D90-B48B-38DD-9380-52F0CCD26835
-  Functions: 15266
-  Symbols:   2987
-  CStrings:  3995
+  UUID: D0570B57-265B-3A76-B12D-38AFFC2CBA70
+  Functions: 15286
+  Symbols:   2991
+  CStrings:  4000
 
Symbols:
+ _$s14MarketplaceKit20SetPublicDataRequestV0F0O21confirmPendingInstallyAE10Foundation4UUIDV_SSAG0E0VSgtcAEmFWC
+ _$s29AppleMediaServicesKitInternal10BagServiceV10bagProfile10clientInfo13accountSourceAcA0fI0V_AA06ClientK0VAC07AccountM0VtKcfC
+ _$s29AppleMediaServicesKitInternal10BagServiceV13AccountSourceV013currentActiveH0AEvgZ
+ _$s29AppleMediaServicesKitInternal10BagServiceV13AccountSourceVMa
+ _$ss22KeyedEncodingContainerV15encodeIfPresent_6forKeyySbSg_xtKF
- _$s14MarketplaceKit20SetPublicDataRequestV0F0O21confirmPendingInstallyAE10Foundation4UUIDV_SSAG0E0VSgSbtcAEmFWC
CStrings:
+ "[%@] Age exception found, highest approved rating: %ld, app's rating: %ld, distributorID of exception: %s"
+ "[%@] An exception exists from a different distributor: %s. Allowing the install to continue."
+ "[%@] Checked highest approved age exception rating: %ld. App's minimum age rating rank: %ld. Device age rating rank: %ld. DistributorID of exception: %s"
+ "[%@] Device does not meet age rating, and no age exception was found."
+ "[%@] Device does not meet age rating, but an age exception was found, allowing install."
+ "[%@] Failing install: an exception already exists from this distributor, an exception request is not needed."
+ "[%@] Failing install: device already meets the age rating, an exception request is not needed."
+ "isExceptionRequest"
+ "requestAgeException"
- "[%@] Age exception found, highest approved rating: %ld, app's rating: %ld"
- "[%@] Age exception was found, allowing install."
- "[%@] Checked highest approved age exception rating: %ld. App's minimum age rating rank: %ld. Device age rating rank: %ld."
- "[%@] Rating above max allowed rating, and no age exception was found."

```
