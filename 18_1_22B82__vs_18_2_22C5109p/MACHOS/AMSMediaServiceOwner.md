## AMSMediaServiceOwner

> `/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner`

```diff

-6.1.20.2.4
-  __TEXT.__text: 0x12b44
-  __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_stubs: 0x920
-  __TEXT.__objc_methlist: 0x17c
-  __TEXT.__const: 0x472
-  __TEXT.__objc_methname: 0x8f1
-  __TEXT.__cstring: 0xafa
-  __TEXT.__oslogstring: 0x400
-  __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methtype: 0x258
-  __TEXT.__constg_swiftt: 0x174
-  __TEXT.__swift5_typeref: 0x336
-  __TEXT.__swift5_reflstr: 0x86
-  __TEXT.__swift5_fieldmd: 0x98
+6.2.8.0.0
+  __TEXT.__text: 0x10968
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_methlist: 0x8c
+  __TEXT.__const: 0x654
+  __TEXT.__constg_swiftt: 0x2bc
+  __TEXT.__swift5_typeref: 0x503
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_reflstr: 0xc5
+  __TEXT.__swift5_fieldmd: 0xc8
+  __TEXT.__swift5_assocty: 0xb8
+  __TEXT.__swift5_proto: 0x48
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__objc_classname: 0x3a
+  __TEXT.__objc_methname: 0x400
+  __TEXT.__objc_methtype: 0x1ff
+  __TEXT.__swift5_protos: 0x10
+  __TEXT.__cstring: 0x96a
   __TEXT.__swift5_capture: 0x248
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_proto: 0x34
-  __TEXT.__swift5_types: 0x10
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x478
+  __TEXT.__unwind_info: 0x460
   __TEXT.__eh_frame: 0xb18
-  __DATA_CONST.__auth_got: 0x488
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__auth_ptr: 0x130
-  __DATA_CONST.__const: 0x430
-  __DATA_CONST.__cfstring: 0x1c0
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_ptr: 0x188
+  __DATA_CONST.__const: 0x318
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x6c0
-  __DATA.__objc_selrefs: 0x288
-  __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0x110
-  __DATA.__data: 0x4b0
-  __DATA.__bss: 0x680
+  __DATA.__objc_const: 0x550
+  __DATA.__objc_selrefs: 0xe8
+  __DATA.__objc_data: 0xc0
+  __DATA.__data: 0x548
+  __DATA.__bss: 0x900
   - /System/Library/Frameworks/Accounts.framework/Accounts
-  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 406
-  Symbols:   154
-  CStrings:  235
+  Functions: 394
+  Symbols:   126
+  CStrings:  143
 
Symbols:
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getAtKeyPath
+ _swift_getKeyPath
- _AKAuthenticationPasswordKey
- _AMSHashIfNeeded
- _AMSLogableError
- _AMSSetLogKey
- _NSStringFromSelector
- _OBJC_CLASS_$_AMSBinaryPromise
- _OBJC_CLASS_$_AMSLogConfig
- _OBJC_CLASS_$_MediaServiceOwner
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSLock
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSPersonNameComponents
- _OBJC_CLASS_$_NSString
- _OBJC_METACLASS_$_MediaServiceOwner
- __NSConcreteGlobalBlock
- __NSConcreteStackBlock
- ___CFConstantStringClassReference
- ___stack_chk_fail
- ___stack_chk_guard
- __os_feature_enabled_impl
- __os_log_impl
- _objc_alloc
- _objc_alloc_init
- _objc_claimAutoreleasedReturnValue
- _objc_enumerationMutation
- _objc_opt_class
- _objc_opt_isKindOfClass
- _objc_retain_x1
- _objc_retain_x28
- _objc_retain_x3
- _objc_storeStrong
- _os_log_type_enabled
CStrings:
- "\x02"
- "%!@(MISSING): "
- "%!@(MISSING): [%!@(MISSING)] "
- "%!{(MISSING)public}@%!{(MISSING)public}@ - context = %!{(MISSING)public}@"
- "%!{(MISSING)public}@%!{(MISSING)public}@ - context = %!{(MISSING)public}@ | amsContext = %!{(MISSING)public}@ | inactiveMediaTypes = %!{(MISSING)public}@"
- "%!{(MISSING)public}@Failed to set the account as active. error = %!{(MISSING)public}@"
- "%!{(MISSING)public}@Failed to sign-out of one or more media types. error = %!{(MISSING)public}@"
- "%!{(MISSING)public}@Refusing to set the account as active. canMakeAccountActive is false"
- "%!{(MISSING)public}@Setting the account as active without authenticating it."
- "%!{(MISSING)public}@Signing out of a media type. mediaType = %!{(MISSING)public}@ | account = %!{(MISSING)public}@"
- "%!{(MISSING)public}@Successfully set the account as active."
- "%!{(MISSING)public}@Successfully signed out of all media types."
- "%!{(MISSING)public}@The account doesn't exist on the device."
- "%!{(MISSING)public}@There are no active media types."
- "%!{(MISSING)public}@There's already an active account for the media type %!{(MISSING)public}@."
- "%!{(MISSING)public}@mediaType = %!{(MISSING)public}@"
- "@\"ACAccountStore\""
- "@\"AMSBinaryPromise\"16@?0@\"NSString\"8"
- "@\"AMSPromise\"16@?0@\"ACAccount\"8"
- "@\"_TtC20AMSMediaServiceOwner20AMSMediaServiceOwner\""
- "@20@0:8B16"
- "AMSMediaServiceOwner: [%!{(MISSING)public}@] Failed to authenticate for an inactive media type. error = %!{(MISSING)public}@"
- "AMSMediaServiceOwner: [%!{(MISSING)public}@] Successfully authenticated for all inactive media types."
- "AppleMediaServices"
- "B16@?0@\"NSString\"8"
- "MediaServiceOwner"
- "MediaServiceOwner _configureAuthenticateTaskWithContext:mediaType:"
- "No Account"
- "OSLogObject"
- "Platform Not Supported"
- "SwiftMediaServiceOwner"
- "T@\"ACAccountStore\",&,N,V_accountStore"
- "T@\"_TtC20AMSMediaServiceOwner20AMSMediaServiceOwner\",&,N,V_swiftMediaServiceOwner"
- "_accountStore"
- "_configureAuthenticateTaskWithContext:mediaType:"
- "_enqueueNextAuthenticationTaskInArray:collectingAuthenticationErrors:completion:"
- "_supportedMediaTypesForSignIn:"
- "_swiftMediaServiceOwner"
- "_unsupportedPlatformError"
- "_useSwiftMediaServiceOwner"
- "accountStore"
- "addErrorBlock:"
- "addFinishBlock:"
- "addObject:"
- "addSuccessBlock:"
- "ams_DSID"
- "ams_activeiTunesAccount"
- "ams_activeiTunesAccountForMediaType:"
- "ams_altDSID"
- "ams_filterUsingTest:"
- "ams_firstName"
- "ams_iTunesAccountWithAltDSID:DSID:username:"
- "ams_lastName"
- "ams_mapWithTransform:"
- "ams_saveAccount:"
- "ams_setActive:forMediaType:"
- "ams_sharedAccountStoreForMediaType:"
- "arrayWithObjects:count:"
- "binaryPromiseAdapter"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "firstObject"
- "iTunes accounts are not supported on this platform."
- "initWithAccount:options:"
- "lock"
- "mutableCopy"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "performAuthentication"
- "promiseAdapter"
- "promiseWithFlattenedPromises:"
- "removeObjectAtIndex:"
- "setAccountStore:"
- "setAltDSID:"
- "setFamilyName:"
- "setGivenName:"
- "setPassword:"
- "setSwiftMediaServiceOwner:"
- "setUsername:"
- "sharedConfig"
- "sharedMediaServiceOwnerConfig"
- "stringValue"
- "stringWithFormat:"
- "swiftMediaServiceOwner"
- "thenWithBlock:"
- "unlock"
- "v16@?0@\"NSError\"8"
- "v24@?0@\"AMSAuthenticateResult\"8@\"NSError\"16"
- "v24@?0@8@\"NSError\"16"
- "v8@?0"

```
