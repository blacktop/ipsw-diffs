## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1007.227.1.0.0
-  __TEXT.__text: 0xc2a88
+1007.229.4.0.0
+  __TEXT.__text: 0xc3514
   __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x8eb4
+  __TEXT.__objc_methlist: 0x8ee4
   __TEXT.__const: 0x19f0
-  __TEXT.__cstring: 0xc3ef
-  __TEXT.__oslogstring: 0xdd6a
-  __TEXT.__gcc_except_tab: 0x21f4
+  __TEXT.__cstring: 0xc5d2
+  __TEXT.__oslogstring: 0xde0e
+  __TEXT.__gcc_except_tab: 0x2200
   __TEXT.__dlopen_cstrs: 0x2d9
-  __TEXT.__unwind_info: 0x24f8
-  __TEXT.__objc_classname: 0x1c32
-  __TEXT.__objc_methname: 0x13621
-  __TEXT.__objc_methtype: 0x2abe
-  __TEXT.__objc_stubs: 0xb100
-  __DATA_CONST.__got: 0xc18
-  __DATA_CONST.__const: 0x3310
-  __DATA_CONST.__objc_classlist: 0x728
+  __TEXT.__unwind_info: 0x2508
+  __TEXT.__objc_classname: 0x1c62
+  __TEXT.__objc_methname: 0x136b0
+  __TEXT.__objc_methtype: 0x2b85
+  __TEXT.__objc_stubs: 0xb160
+  __DATA_CONST.__got: 0xc20
+  __DATA_CONST.__const: 0x3350
+  __DATA_CONST.__objc_classlist: 0x730
   __DATA_CONST.__objc_catlist: 0x98
-  __DATA_CONST.__objc_protolist: 0x158
+  __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4530
+  __DATA_CONST.__objc_selrefs: 0x4540
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x510
   __DATA_CONST.__objc_arraydata: 0xc0
   __AUTH_CONST.__auth_got: 0x560
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x55a0
-  __AUTH_CONST.__cfstring: 0xb660
-  __AUTH_CONST.__objc_const: 0x21af0
+  __AUTH_CONST.__const: 0x55c0
+  __AUTH_CONST.__cfstring: 0xb6a0
+  __AUTH_CONST.__objc_const: 0x21f18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH.__objc_data: 0x1e0
+  __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0xad0
-  __DATA.__data: 0x1300
-  __DATA.__bss: 0x350
+  __DATA.__data: 0x1360
+  __DATA.__bss: 0x360
   __DATA.__common: 0x69
   __DATA_DIRTY.__objc_data: 0x45b0
   __DATA_DIRTY.__data: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3900
-  Symbols:   5478
-  CStrings:  6578
+  Functions: 3915
+  Symbols:   5499
+  CStrings:  6595
 
Symbols:
+ _AAPrefsInformationCacheDomain
+ _ACErrorDomain
+ _OBJC_CLASS_$_AAAccountStoreProxy
+ _OBJC_METACLASS_$_AAAccountStoreProxy
+ __AAAccountStoreLogSystem
+ _kAAAnalyticsEventCustodianRecoveryExperimentalRecoveryInfoNotFoundFetchFromCloud
+ _kAAProtocolPrefSkipRecoveryInfoRecordStorage
- _kCFBooleanFalse
CStrings:
+ "-[AAAccountStoreProxy saveAccount:onAccountStore:withCompletionHandler:]"
+ "-[AAAccountStoreProxy saveAccount:onAccountStore:withCompletionHandler:]_block_invoke"
+ "-[AAAccountStoreProxy saveAccount:onAccountStore:withDataclassActions:doVerify:completion:]"
+ "-[AAAccountStoreProxy saveAccount:onAccountStore:withDataclassActions:doVerify:completion:]_block_invoke"
+ "@\"<AAAccountStoreProxyProtocol>\""
+ "AAAccountStoreProxy"
+ "AAAccountStoreProxyProtocol"
+ "AASkipRecoveryInfoRecordStorage"
+ "Attempting to perform %s"
+ "Connection error (10002) from Accounts Daemon while performing %s. Will retry only once after 1/3 sec delay."
+ "Error while performing %s: %@"
+ "T@\"<AAAccountStoreProxyProtocol>\",&,N,V_storeProxy"
+ "_isAccountDaemonConnectionError:"
+ "_storeProxy"
+ "accountstore"
+ "com.apple.appleaccount.custodian.recovery.experimental.recoveryInfoNotFoundFetchFromCloud"
+ "com.apple.appleaccount.informationcache"
+ "minimizedLanguagesFromLanguages:"
+ "saveAccount:onAccountStore:withCompletionHandler:"
+ "saveAccount:onAccountStore:withDataclassActions:doVerify:completion:"
+ "setStoreProxy:"
+ "shouldSkipRecoveryInfoRecordStorage"
+ "storeProxy"
+ "v40@0:8@\"ACAccount\"16@\"ACAccountStore\"24@?<v@?B@\"NSError\">32"
+ "v52@0:8@\"ACAccount\"16@\"ACAccountStore\"24@\"NSDictionary\"32B40@?<v@?B@\"NSError\">44"
+ "v52@0:8@16@24@32B40@?44"
- "AddImagePlaygroundDataclass"
- "DiscoDonutDataclass"
- "T@\"NSString\",R,N,V_accountUsername"
- "_accountUsername"
- "accountUsername"
- "addDiscoDonutDataclass"
- "isDiscoDonutDataclassAvailable"
- "isRCUpsellEnabled"
- "setAddDiscoDonutDataclass:"

```
