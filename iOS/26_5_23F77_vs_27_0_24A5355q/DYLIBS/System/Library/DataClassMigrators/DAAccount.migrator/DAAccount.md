## DAAccount

> `/System/Library/DataClassMigrators/DAAccount.migrator/DAAccount`

```diff

-2691.4.6.0.0
-  __TEXT.__text: 0xe4 sha256:389725e12bc7c3e48cacdaf224cf65c109b4abbc88ad8ae13eebcdc4ba8871b3
-  __TEXT.__auth_stubs: 0x50 sha256:b4b0e984aa0193812cccb13967c2aed9eaf27450a052968d25790ab044491b8c
-  __TEXT.__objc_methlist: 0x38 sha256:d9fe13fcc498a7011c771c126f68ebc8b859c00d5d4cb5f0a1987821fc935461
+2703.0.0.0.0
+  __TEXT.__text: 0xe0 sha256:50595e3a7ef9a4c73f024e8c0d4e24b8d0d5d7c90d2049db0b34d198b6b073b3
+  __TEXT.__objc_methlist: 0x38 sha256:79c20e8dfc8e219defcf8e63b34c5aabada0cc38cac021d794abbb22d3ddcbbc
   __TEXT.__const: 0x4 sha256:fb360f7241a770dc32cade9a1d1273c92b13bd4959b1c130931312b7fe95e63f
   __TEXT.__cstring: 0xc sha256:7c025a28aea1e34899aa4269dea07052b7d1a64d82528bafb6d4afbb88b2d8c4
   __TEXT.__oslogstring: 0x3e sha256:fcb4d19fc3bb8941b583c474257ed9ab2ddbb9b5d90c3e4a7744fab674c78431
-  __TEXT.__unwind_info: 0x60 sha256:ce97fdf377b6a141f74e41e434b7fac39342452c4e5c73c1179e41ebb91c9268
-  __TEXT.__objc_classname: 0x12 sha256:996470f78aff9a53b9e0a1141a8214e8b67d5930033b5ae9fc3ef73ca81cd7c3
-  __TEXT.__objc_methname: 0x98 sha256:4951535350d37c79f0e2949e040b5722f706fecffc82ca3f4d9359403cd3572a
-  __TEXT.__objc_methtype: 0x18 sha256:6404870a6dbab538b4bdad51c08745b53e39f57fc4e93f7b87c1fbbc52729c46
-  __TEXT.__objc_stubs: 0x80 sha256:6312a7b225664e3e9765ffde96b293aa768d91f2add23bf3a0ff3076ad774c0f
-  __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__objc_classlist: 0x8 sha256:2885f218a29a93abaae37def09f43569b5e6c239f88cf92039a8cadc5fce3c78
+  __TEXT.__unwind_info: 0x60 sha256:fdeb41f997ce4eca733aa8f03eada3aea915a43b5632dda8c873bab58c5855f7
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__objc_classlist: 0x8 sha256:f9ebf413711bbb666b9309cb3c07e2deb2947554f0abc68116024c36369a67d6
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x40 sha256:583508e9f595161eff40bf24330e1316001964c13456cc744b10bc05092abd39
-  __AUTH_CONST.__auth_got: 0x30 sha256:17b0761f87b081d5cf10757ccc89f12be355c70e2e29df288b65b30710dcbcd1
-  __AUTH_CONST.__cfstring: 0x20 sha256:b51ac9e575c169cdb96db47fa3cf96083d898c57b10b4cedd85f9d5c948b4379
-  __AUTH_CONST.__objc_const: 0x90 sha256:64d65c4f6cec9000b2c125fc8186a969e57798bc9f9ce258e8b931981eefb8cb
-  __AUTH.__objc_data: 0x50 sha256:c1d34e85e4c0c9bea5fd731b083dd39b45646d26f30ec106811e7f5aff0ed730
+  __DATA_CONST.__objc_selrefs: 0x40 sha256:55254397d1db446d8f6470decf41f25757232acf590c823aa5227426bb3a6bd4
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x20 sha256:9e4402953d503745e41119360d3c78847c79b715cf45723b92a7af516b6a1896
+  __AUTH_CONST.__objc_const: 0x90 sha256:f6ba84dd7d2f1447982f51519e7a89ed01750fc2b29be504a44118660a5f5f71
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x50 sha256:d5df8e0ca130cb210bd22fd8476a9490931b733a3f5dee66533b787d06dde0a4
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00A843DA-2A59-31BF-834E-72196FC97C65
+  UUID: FB375DEA-0ED5-3DFD-93AE-87360990EB52
   Functions: 4
   Symbols:   30
-  CStrings:  15
+  CStrings:  3
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[DAAccountMigrator dataClassName] : sha256 38e72cfa1efdd23bb53fcbe61bdb29eb618b471115bcf4286a52558b9b2af535 -> 8c9c3c8f1967540ecb751ee75985dd35efc77572179007bb79e90d2988d7a30a
~ -[DAAccountMigrator performMigration] : 196 -> 192
~ -[DAAccountMigrator estimatedDuration] : sha256 5b471d6ec321b404544ebdfffbe6795765b8d7d588bf44b955121d0686537405 -> f216ae2adae00c51d4a2f4795c89c6a9816089ae13fdd2ef94df6854434fe762
CStrings:
- "@16@0:8"
- "B16@0:8"
- "DAAccountMigrator"
- "dataClassName"
- "didMigrateBackupFromDifferentDevice"
- "didRestoreFromBackup"
- "didUpgrade"
- "estimatedDuration"
- "f16@0:8"
- "migrationProgress"
- "performMigration"
- "upgradeAccounts:"

```
