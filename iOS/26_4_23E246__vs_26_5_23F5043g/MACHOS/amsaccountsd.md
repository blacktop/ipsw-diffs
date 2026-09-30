## amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

-9.4.28.2.1
-  __TEXT.__text: 0x21e5bc
-  __TEXT.__auth_stubs: 0x3e70
-  __TEXT.__objc_stubs: 0xa9e0
-  __TEXT.__objc_methlist: 0x580c
-  __TEXT.__const: 0x1d2c4
-  __TEXT.__objc_methname: 0xfd1b
-  __TEXT.__oslogstring: 0xdc81
-  __TEXT.__cstring: 0xa3b7
-  __TEXT.__objc_classname: 0x15c5
-  __TEXT.__objc_methtype: 0x496f
-  __TEXT.__gcc_except_tab: 0xdec
+9.5.4.0.0
+  __TEXT.__text: 0x221c64
+  __TEXT.__auth_stubs: 0x3eb0
+  __TEXT.__objc_stubs: 0xab00
+  __TEXT.__objc_methlist: 0x58a4
+  __TEXT.__const: 0x1d344
+  __TEXT.__objc_methname: 0xfedb
+  __TEXT.__oslogstring: 0xe061
+  __TEXT.__cstring: 0xa4d7
+  __TEXT.__objc_classname: 0x15e5
+  __TEXT.__objc_methtype: 0x49be
+  __TEXT.__gcc_except_tab: 0xe04
   __TEXT.__dlopen_cstrs: 0x34d
-  __TEXT.__swift5_typeref: 0x6c88
-  __TEXT.__constg_swiftt: 0x522c
+  __TEXT.__swift5_typeref: 0x6cb8
+  __TEXT.__constg_swiftt: 0x5258
   __TEXT.__swift5_reflstr: 0x46fc
-  __TEXT.__swift5_fieldmd: 0x63fc
+  __TEXT.__swift5_fieldmd: 0x640c
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_assocty: 0x8f8
-  __TEXT.__swift5_proto: 0x16b4
-  __TEXT.__swift5_types: 0x678
+  __TEXT.__swift5_proto: 0x16b8
+  __TEXT.__swift5_types: 0x67c
   __TEXT.__swift5_protos: 0x98
   __TEXT.__swift_as_entry: 0x208
   __TEXT.__swift5_mpenum: 0x78
-  __TEXT.__swift5_capture: 0xa3c
+  __TEXT.__swift5_capture: 0xa40
   __TEXT.__swift_as_ret: 0x2b0
   __TEXT.__swift5_types2: 0x8
-  __TEXT.__unwind_info: 0x87f0
-  __TEXT.__eh_frame: 0xf638
-  __DATA_CONST.__auth_got: 0x1f48
-  __DATA_CONST.__got: 0x11b0
+  __TEXT.__unwind_info: 0x8820
+  __TEXT.__eh_frame: 0xf668
+  __DATA_CONST.__auth_got: 0x1f68
+  __DATA_CONST.__got: 0x11d0
   __DATA_CONST.__auth_ptr: 0xca0
-  __DATA_CONST.__const: 0x122e8
-  __DATA_CONST.__cfstring: 0x4140
-  __DATA_CONST.__objc_classlist: 0x368
+  __DATA_CONST.__const: 0x12318
+  __DATA_CONST.__cfstring: 0x4200
+  __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__linkguard: 0x2c
-  __DATA.__objc_const: 0xb470
-  __DATA.__objc_selrefs: 0x3a00
-  __DATA.__objc_ivar: 0x364
-  __DATA.__objc_data: 0x2588
-  __DATA.__data: 0xa270
-  __DATA.__bss: 0x2d1c0
+  __DATA.__objc_const: 0xb5a8
+  __DATA.__objc_selrefs: 0x3a58
+  __DATA.__objc_ivar: 0x370
+  __DATA.__objc_data: 0x25d8
+  __DATA.__data: 0xa2a0
+  __DATA.__bss: 0x2d240
   __DATA.__common: 0x190
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C1B9CEA3-E854-32F7-9B3D-8E5B8963DB35
-  Functions: 13652
-  Symbols:   1887
-  CStrings:  5571
+  UUID: B5D6A1B9-0DF9-3C77-9CC5-C7D3FEE422CA
+  Functions: 13683
+  Symbols:   1894
+  CStrings:  5618
 
Symbols:
+ _$s10Foundation10CocoaErrorV14fileNoSuchFileAC4CodeVvgZ
+ _$s10Foundation10CocoaErrorV4CodeVAA01_cD8ProtocolAAMc
+ _$s10Foundation10CocoaErrorV4CodeVMa
+ _$s10Foundation18_ErrorCodeProtocolPAAE2teoiySbx_s0B0_ptFZ
+ _$s10Foundation3URLVs23CustomStringConvertibleAAMc
+ _$sSo13NSFileManagerC10FoundationE13replaceItemAt_04witheF006backupE4Name7optionsAC3URLVSgAI_AISSSgSo0abE18ReplacementOptionsVtKF
+ _AMSBagKeyUpdatePasscodeSettings
CStrings:
+ "%{public}@%@ account added for type = %{public}@"
+ "%{public}@%@ account already exists for type = %{public}@"
+ "%{public}@%@ account does not exist for type = %{public}@"
+ "%{public}@Calling -[PKInAppPaymentService paymentHardwareStatusWithType:completion:]"
+ "%{public}@Checking for %{public}@ account"
+ "%{public}@Completion handler passed to -[PKInAppPaymentService paymentHardwareStatusWithType:completion:] deallocated without being called."
+ "%{public}@Creating new %@ account for type = %{public}@ | account = %{public}@"
+ "%{public}@Failed to get paymentHardwareStatus"
+ "%{public}@Get payment hardware status. canUseApplePay = %{public}@"
+ "%{public}@Inside keep-alive block, creating PKInAppPaymentService"
+ "%{public}@PKInAppPaymentService creation returned nil"
+ "%{public}@Requesting keep-alive transaction for payment hardware status"
+ "@40@0:8@16@24@?32"
+ "Attempting to migrate database from previous locations..."
+ "Attempting to move contents of %s to the current database location..."
+ "BetaLocalAccount"
+ "Completion Handler Not Called"
+ "Creating a PKInAppPaymentService returned nil"
+ "Database already exists in the current location, not migrating."
+ "Deleting previous database directories..."
+ "Failed to create legacy peristence directory URL, will not be able to migrate any existing data: %@"
+ "Failed to delete previous database directory: %s: %@"
+ "Failed to migrate SQLite database files from %s to %s: %@"
+ "No previous data to migrate."
+ "PKInAppPaymentService dropped the completion handler without calling it"
+ "Successfully migrated SQLite database files from %s to the current database location"
+ "T@\"NSString\",C,N,V_identifier"
+ "T@\"NSString\",C,N,V_mediaType"
+ "T@?,C,N,V_completion"
+ "_AMSPendingLocalAccountRequest"
+ "_buildRequestWithBody:bag:style:"
+ "_completion"
+ "_getOrCreateLocalAccountWithIdentifier:mediaType:error:"
+ "_getOrCreateLocalAccountWithType:mediaType:error:"
+ "_isBetaLocalAccountForMediaType:"
+ "_localAccountWithType:mediaType:"
+ "_mediaType"
+ "_newLocalAccountWithAccountType:mediaType:"
+ "ams_isLocalBetaAccount"
+ "beta local"
+ "biometricState"
+ "completion"
+ "initWithIdentifier:mediaType:completion:"
+ "isBiometricsEnabled"
+ "local-beta"
+ "mediaType"
+ "performCreateLocalAccountWithIdentifier:mediaType:completion:"
+ "previousDatabaseDirectoryURLs currentDatabaseDirectoryURL "
+ "setCompletion:"
+ "setMediaType:"
+ "setMethodOfVerification:"
+ "supportsPasscodePurchaseWithAttestationStyle:"
+ "v32@?0@\"NSString\"8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "%{public}@: [%{public}@] Failed to get paymentHardwareStatus"
- "%{public}@: [%{public}@] Get payment hardware status. canUseApplePay = %{public}@"
- "%{public}@Checking for local account"
- "%{public}@Creating new local account for type = %{public}@ | account = %{public}@"
- "%{public}@Local account added for type = %{public}@"
- "%{public}@Local account already exists for type = %{public}@"
- "%{public}@Local account does not exist for type = %{public}@"
- "_buildRequestWithBody:bag:"
- "_getOrCreateLocalAccountWithIdentifier:error:"
- "_getOrCreateLocalAccountWithType:error:"
- "_localAccountWithType:"
- "_newLocalAccountWithAccountType:"
- "v24@?0@\"NSString\"8@?<v@?B@\"NSError\">16"

```
