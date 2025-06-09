## UserManagement

> `/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement`

```diff

-417.100.1.0.0
-  __TEXT.__text: 0x247c8
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x1ca4
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x4430
-  __TEXT.__oslogstring: 0x5cf
-  __TEXT.__gcc_except_tab: 0xa70
+452.0.0.0.0
+  __TEXT.__text: 0x27964
+  __TEXT.__auth_stubs: 0xa40
+  __TEXT.__objc_methlist: 0x1e1c
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x470b
+  __TEXT.__oslogstring: 0x8f4
+  __TEXT.__gcc_except_tab: 0xc58
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0xb28
+  __TEXT.__unwind_info: 0xc08
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x40a
-  __TEXT.__objc_methname: 0x453b
-  __TEXT.__objc_methtype: 0x13b7
-  __TEXT.__objc_stubs: 0x2ac0
+  __TEXT.__objc_classname: 0x428
+  __TEXT.__objc_methname: 0x4a59
+  __TEXT.__objc_methtype: 0x1502
+  __TEXT.__objc_stubs: 0x2c00
   __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x838
+  __DATA_CONST.__const: 0x868
   __DATA_CONST.__objc_classlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf10
+  __DATA_CONST.__objc_selrefs: 0xfb8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x528
-  __AUTH_CONST.__const: 0x6c0
-  __AUTH_CONST.__cfstring: 0x3a20
-  __AUTH_CONST.__objc_const: 0x4390
+  __AUTH_CONST.__auth_got: 0x530
+  __AUTH_CONST.__const: 0x6a0
+  __AUTH_CONST.__cfstring: 0x3ca0
+  __AUTH_CONST.__objc_const: 0x4458
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x234
-  __DATA.__data: 0xbe0
-  __DATA.__bss: 0x180
+  __DATA.__objc_ivar: 0x238
+  __DATA.__data: 0xc48
+  __DATA.__bss: 0x179
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 22B5BB04-7486-3DA4-87A2-F63012284145
-  Functions: 1010
-  Symbols:   359
-  CStrings:  1934
+  UUID: BB19C72E-7EAD-3418-84B3-CC2EDD7FB197
+  Functions: 1065
+  Symbols:   362
+  CStrings:  2020
 
Symbols:
+ _kUMUserPersonaDisabledNotificationToken
+ _kUMUserPersonaDisablementReasonKey
+ _kpersona_pidinfo
CStrings:
+ " voucherCacheRepo with umpcontext"
+ "Adopted cached Voucher for personaUniqStr:%@"
+ "Adopting Voucher for personaUniqStr:%@"
+ "Adopting new persona %{public}@ (current voucher persona: %u)"
+ "B32@0:8@\"NSData\"16^@24"
+ "B40@0:8@\"NSData\"16@\"NSData\"24^@32"
+ "Cached personaVocuherDictionary set for  :%@"
+ "Changing Bootstrap Token"
+ "Changing Bootstrap token Successful"
+ "Changing Bootstrap token failed with error:%@"
+ "Check Bootstrap Token Exists"
+ "Check Bootstrap Token exists"
+ "Check Bootstrap Token failed with error:%@"
+ "Could not get launch persona Info for current pid:%d with error:%s"
+ "Creating Bootstrap Token"
+ "Creating Bootstrap token Successful"
+ "Creating Bootstrap token failed with error:%@"
+ "Deleting Bootstrap Token"
+ "Deleting Bootstrap Token Successful"
+ "Deleting Bootstrap Token failed with error:%@"
+ "Failed to fetch persona list for all users: %{public}@"
+ "Failed to fetch persona list for all users: error from remote proxy: %{public}@"
+ "Failed to fetch persona list for current user (sync): %{public}@"
+ "Failed to fetch persona list for current user (sync): error from remote proxy: %{public}@"
+ "Failed to fetch persona list for current user: %{public}@"
+ "Failed to fetch persona list for current user: error from remote proxy: %{public}@"
+ "Fetched %lu personas for all users"
+ "Fetched %lu personas for current user"
+ "Fetched %lu personas for current user (sync)"
+ "T@\"NSString\",C,N,V_disablementReason"
+ "UMUserBootStrapUserManagement"
+ "UserPersonaDisablementReason"
+ "Validate bootstrapToken"
+ "Validating Bootstrap Token"
+ "Validating Bootstrap Token failed with error:%@"
+ "ValidatingBootstrap Token Successful"
+ "_disablementReason"
+ "change bootstrapToken"
+ "changeBootstrapTokenWithOldSecret:oldSize:withNewSecret:newSize:withReply:"
+ "changeBootstrapTokenWithOldSecret:withNewSecret:withReply:"
+ "changeBootstrapUserTokenFromOldToken:toNewToken:withError:"
+ "changeBootstrapUserTokenFromOldTokenInACMCredential:toNewTokenInACMCredential:withError:"
+ "check bootstrapToken"
+ "checkBootstrapTokenExistsWithReply:"
+ "checkBootstrapUserExistsWithError:"
+ "com.apple.mobile.usermanagerd.userpersona_disabled"
+ "create bootstrapToken"
+ "createBootstrapTokenWithSecret:secretSize:withDeviceSecretHandle:deviceSecretSize:withReply:"
+ "createBootstrapTokenWithSecret:withDevicePasscode:withReply:"
+ "createBootstrapUserWithToken:withDevicePasscode:withError:"
+ "createBootstrapUserWithTokenInACMCredential:withDevicePasscodeInACMCredential:withError:"
+ "createPersona:withSecret:secretSize:forPid:completionHandler:"
+ "createPersona:withSecret:secretSize:passcodeDataType:forPid:completionHandler:"
+ "delete bootstrapToken"
+ "deleteBootstrapTokenWithSecret:secretSize:withDeviceSecretHandle:deviceSecretSize:withReply:"
+ "deleteBootstrapTokenWithSecret:withDevicePasscode:withReply:"
+ "deleteBootstrapUserWithToken:withDevicePasscode:withError:"
+ "deleteBootstrapUserWithTokenInACMCredential:withDevicePasscodeInACMCredential:withError:"
+ "directSwitchToUser:withSecret:secretSize:context:preferences:pid:completionHandler:"
+ "disablementReason"
+ "got error from remote changeBootstrapToken: %@"
+ "got error from remote checkBootstrapExists: %@"
+ "got error from remote createBootstrapToken: %@"
+ "got error from remote deleteBootstrapToken: %@"
+ "got error from remote validateBootstrapToken: %@"
+ "has Cache key for personaUniqStr:%@"
+ "launchPersona"
+ "replacePersonaPortVoucher failed: called with null targetPortPtr"
+ "retrieveReplacementVoucher failed: got error from remote proxy: %{public}@"
+ "setDisablementReason:"
+ "switchToUser:withSecret:secretSize:context:pid:completionHandler:"
+ "switchToUser:withSecret:secretSize:context:preferences:pid:completionHandler:"
+ "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSFileHandle\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@16Q24@?32"
+ "v52@0:8@\"NSDictionary\"16@\"NSFileHandle\"24Q32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
+ "v56@0:8@\"NSFileHandle\"16Q24@\"NSFileHandle\"32Q40@?<v@?@\"NSError\">48"
+ "v56@0:8@16Q24@32Q40@?48"
+ "v60@0:8@\"NSDictionary\"16@\"NSFileHandle\"24Q32@\"NSData\"40i48@?<v@?@\"NSError\">52"
+ "v60@0:8@\"NSDictionary\"16@\"NSFileHandle\"24Q32Q40i48@?<v@?@\"NSDictionary\"@\"NSError\">52"
+ "v60@0:8@16@24Q32@40i48@?52"
+ "v60@0:8@16@24Q32Q40i48@?52"
+ "v68@0:8@\"NSDictionary\"16@\"NSFileHandle\"24Q32@\"NSData\"40@\"NSDictionary\"48i56@?<v@?@\"NSError\">60"
+ "v68@0:8@16@24Q32@40@48i56@?60"
+ "validateBootstrapTokenWithSecret:secretSize:withReply:"
+ "validateBootstrapTokenWithSecret:withReply:"
+ "validateBootstrapUserWithToken:withError:"
+ "validateBootstrapUserWithTokenInACMCredential:withError:"
- " voucherCacheRepo with umpcontext "
- "Adopted cached Voucher for accountID:%@"
- "Adopting Voucher for accountID:%@"
- "Cached personaVocuherDictionary is :%@"
- "Failed to fetch persona list: "
- "Failed to fetch persona list: %@"
- "Failed to fetch persona list: got error from remote proxy: %@"
- "Failed to persona list for all users: "
- "INVALID CALLBACK from replacePersonaPortVoucher with null targetPortPtr"
- "createPersona:passcodeData:forPid:completionHandler:"
- "createPersona:passcodeData:passcodeDataType:forPid:completionHandler:"
- "directSwitchToUser:passcodeData:context:preferences:pid:completionHandler:"
- "has Cache key and its value is:%@"
- "switchToUser:passcodeData:context:pid:completionHandler:"
- "switchToUser:passcodeData:context:preferences:pid:completionHandler:"
- "v44@0:8@\"NSDictionary\"16@\"NSData\"24i32@?<v@?@\"NSDictionary\"@\"NSError\">36"
- "v52@0:8@\"NSDictionary\"16@\"NSData\"24@\"NSData\"32i40@?<v@?@\"NSError\">44"
- "v52@0:8@\"NSDictionary\"16@\"NSData\"24Q32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
- "v52@0:8@16@24@32i40@?44"
- "v60@0:8@\"NSDictionary\"16@\"NSData\"24@\"NSData\"32@\"NSDictionary\"40i48@?<v@?@\"NSError\">52"
- "v60@0:8@16@24@32@40i48@?52"
- "voucherCacheRepo is :%@"

```
