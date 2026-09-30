## MobileInstallation

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation`

```diff

-1513.80.6.0.0
-  __TEXT.__text: 0x23cf8
-  __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_methlist: 0x124c
+1513.100.80.0.0
+  __TEXT.__text: 0x25ecc
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x12ac
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x4e81
-  __TEXT.__gcc_except_tab: 0xb64
+  __TEXT.__cstring: 0x4eef
+  __TEXT.__gcc_except_tab: 0xbdc
   __TEXT.__oslogstring: 0x43
-  __TEXT.__unwind_info: 0xbb0
+  __TEXT.__unwind_info: 0xc80
   __TEXT.__objc_classname: 0x17d
-  __TEXT.__objc_methname: 0x4343
-  __TEXT.__objc_methtype: 0x13ba
-  __TEXT.__objc_stubs: 0x2c20
+  __TEXT.__objc_methname: 0x4412
+  __TEXT.__objc_methtype: 0x13e2
+  __TEXT.__objc_stubs: 0x2ca0
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x958
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcf8
+  __DATA_CONST.__objc_selrefs: 0xd18
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x4a8
+  __AUTH_CONST.__auth_got: 0x470
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x29c0
-  __AUTH_CONST.__objc_const: 0x18e0
+  __AUTH_CONST.__objc_const: 0x1900
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x30

   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6D6F6D96-F6B5-30BD-BAF3-6B2B55CA3B50
-  Functions: 762
-  Symbols:   2363
-  CStrings:  1563
+  UUID: E0A0BA00-E5A3-31FD-9711-0D006334FA31
+  Functions: 790
+  Symbols:   2416
+  CStrings:  1570
 
Symbols:
+ -[MIInstallerClient fetchListOfAppsRequiringPreInstallConsent:]
+ -[MIInstallerClient registerContentsOnRoot:deferUntilNextBoot:completion:]
+ -[MIInstallerClient storeListOfAppsRequiringPreInstallConsent:completion:]
+ -[MIInstallerClient unregisterContentsOnRoot:deferUntilNextBoot:completion:]
+ GCC_except_table268
+ GCC_except_table278
+ GCC_except_table281
+ GCC_except_table284
+ GCC_except_table287
+ GCC_except_table290
+ GCC_except_table293
+ GCC_except_table311
+ GCC_except_table318
+ GCC_except_table326
+ GCC_except_table332
+ GCC_except_table334
+ GCC_except_table336
+ GCC_except_table340
+ GCC_except_table347
+ GCC_except_table351
+ GCC_except_table353
+ GCC_except_table355
+ GCC_except_table357
+ GCC_except_table359
+ GCC_except_table361
+ GCC_except_table363
+ GCC_except_table365
+ GCC_except_table368
+ GCC_except_table370
+ GCC_except_table372
+ GCC_except_table374
+ GCC_except_table378
+ GCC_except_table380
+ GCC_except_table384
+ GCC_except_table393
+ GCC_except_table406
+ GCC_except_table410
+ GCC_except_table412
+ GCC_except_table414
+ GCC_except_table416
+ GCC_except_table437
+ GCC_except_table448
+ GCC_except_table450
+ GCC_except_table452
+ GCC_except_table454
+ GCC_except_table456
+ GCC_except_table458
+ GCC_except_table460
+ _MobileInstallationFetchListOfAppsRequiringPreInstallConsent
+ _MobileInstallationRegisterContentsOnRoot
+ _MobileInstallationStoreListOfAppsRequiringPreInstallConsent
+ _MobileInstallationUnregisterContentsOnRoot
+ ___63-[MIInstallerClient fetchListOfAppsRequiringPreInstallConsent:]_block_invoke
+ ___63-[MIInstallerClient fetchListOfAppsRequiringPreInstallConsent:]_block_invoke_2
+ ___63-[MIInstallerClient fetchListOfAppsRequiringPreInstallConsent:]_block_invoke_3
+ ___63-[MIInstallerClient fetchListOfAppsRequiringPreInstallConsent:]_block_invoke_4
+ ___74-[MIInstallerClient registerContentsOnRoot:deferUntilNextBoot:completion:]_block_invoke
+ ___74-[MIInstallerClient registerContentsOnRoot:deferUntilNextBoot:completion:]_block_invoke_2
+ ___74-[MIInstallerClient registerContentsOnRoot:deferUntilNextBoot:completion:]_block_invoke_3
+ ___74-[MIInstallerClient registerContentsOnRoot:deferUntilNextBoot:completion:]_block_invoke_4
+ ___74-[MIInstallerClient storeListOfAppsRequiringPreInstallConsent:completion:]_block_invoke
+ ___74-[MIInstallerClient storeListOfAppsRequiringPreInstallConsent:completion:]_block_invoke_2
+ ___74-[MIInstallerClient storeListOfAppsRequiringPreInstallConsent:completion:]_block_invoke_3
+ ___74-[MIInstallerClient storeListOfAppsRequiringPreInstallConsent:completion:]_block_invoke_4
+ ___76-[MIInstallerClient unregisterContentsOnRoot:deferUntilNextBoot:completion:]_block_invoke
+ ___76-[MIInstallerClient unregisterContentsOnRoot:deferUntilNextBoot:completion:]_block_invoke_2
+ ___76-[MIInstallerClient unregisterContentsOnRoot:deferUntilNextBoot:completion:]_block_invoke_3
+ ___76-[MIInstallerClient unregisterContentsOnRoot:deferUntilNextBoot:completion:]_block_invoke_4
+ ___MobileInstallationFetchListOfAppsRequiringPreInstallConsent_block_invoke
+ ___MobileInstallationRegisterContentsOnRoot_block_invoke
+ ___MobileInstallationStoreListOfAppsRequiringPreInstallConsent_block_invoke
+ ___MobileInstallationUnregisterContentsOnRoot_block_invoke
+ _objc_msgSend$fetchListOfAppsRequiringPreInstallConsent:
+ _objc_msgSend$registerContentsOnRoot:deferUntilNextBoot:completion:
+ _objc_msgSend$storeListOfAppsRequiringPreInstallConsent:completion:
+ _objc_msgSend$unregisterContentsOnRoot:deferUntilNextBoot:completion:
+ _objc_retain_x28
- GCC_except_table248
- GCC_except_table253
- GCC_except_table258
- GCC_except_table261
- GCC_except_table264
- GCC_except_table267
- GCC_except_table270
- GCC_except_table291
- GCC_except_table298
- GCC_except_table300
- GCC_except_table306
- GCC_except_table312
- GCC_except_table314
- GCC_except_table316
- GCC_except_table327
- GCC_except_table331
- GCC_except_table333
- GCC_except_table335
- GCC_except_table337
- GCC_except_table339
- GCC_except_table341
- GCC_except_table343
- GCC_except_table345
- GCC_except_table348
- GCC_except_table350
- GCC_except_table352
- GCC_except_table354
- GCC_except_table356
- GCC_except_table358
- GCC_except_table360
- GCC_except_table362
- GCC_except_table364
- GCC_except_table366
- GCC_except_table369
- GCC_except_table392
- GCC_except_table396
- GCC_except_table398
- GCC_except_table404
- GCC_except_table409
- GCC_except_table426
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "MobileInstallationRegisterContentsOnRoot_block_invoke"
+ "MobileInstallationUnregisterContentsOnRoot_block_invoke"
+ "fetchListOfAppsRequiringPreInstallConsent:"
+ "registerContentsOnRoot:deferUntilNextBoot:completion:"
+ "storeListOfAppsRequiringPreInstallConsent:completion:"
+ "unregisterContentsOnRoot:deferUntilNextBoot:completion:"
+ "v36@0:8@\"NSSet\"16B24@?<v@?@\"NSError\">28"

```
