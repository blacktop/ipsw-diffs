## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-619.1.22.4.0
-  __TEXT.__text: 0x84db4
-  __TEXT.__auth_stubs: 0x1890
-  __TEXT.__objc_methlist: 0x6508
-  __TEXT.__const: 0x1484
-  __TEXT.__gcc_except_tab: 0x1128
-  __TEXT.__cstring: 0x6426
-  __TEXT.__oslogstring: 0x3025
+619.1.26.20.1
+  __TEXT.__text: 0x884a4
+  __TEXT.__auth_stubs: 0x18d0
+  __TEXT.__objc_methlist: 0x6578
+  __TEXT.__const: 0x14c4
+  __TEXT.__gcc_except_tab: 0x1148
+  __TEXT.__cstring: 0x6406
+  __TEXT.__oslogstring: 0x309f
   __TEXT.__dlopen_cstrs: 0x2a8
   __TEXT.__ustring: 0x8b64
-  __TEXT.__swift5_typeref: 0x81c
-  __TEXT.__constg_swiftt: 0x570
+  __TEXT.__swift5_typeref: 0x86a
+  __TEXT.__constg_swiftt: 0x57c
   __TEXT.__swift5_reflstr: 0x908
-  __TEXT.__swift5_fieldmd: 0x8bc
+  __TEXT.__swift5_fieldmd: 0x8e0
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_assocty: 0x318
   __TEXT.__swift5_proto: 0xe4
   __TEXT.__swift5_types: 0x9c
   __TEXT.__swift5_mpenum: 0x40
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x2748
+  __TEXT.__unwind_info: 0x27e0
   __TEXT.__eh_frame: 0x498
   __TEXT.__objc_classname: 0x1eac
-  __TEXT.__objc_methname: 0x17e74
-  __TEXT.__objc_methtype: 0x4bc7
-  __TEXT.__objc_stubs: 0xf700
-  __DATA_CONST.__got: 0xe10
-  __DATA_CONST.__const: 0x1e70
+  __TEXT.__objc_methname: 0x17eb6
+  __TEXT.__objc_methtype: 0x4bab
+  __TEXT.__objc_stubs: 0xf6c0
+  __DATA_CONST.__got: 0xe08
+  __DATA_CONST.__const: 0x1ed0
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x228

   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x158
-  __AUTH_CONST.__auth_got: 0xc60
-  __AUTH_CONST.__auth_ptr: 0x2b0
-  __AUTH_CONST.__const: 0x2250
+  __AUTH_CONST.__auth_got: 0xc80
+  __AUTH_CONST.__auth_ptr: 0x2a8
+  __AUTH_CONST.__const: 0x21d0
   __AUTH_CONST.__cfstring: 0x4f80
-  __AUTH_CONST.__objc_const: 0x10120
+  __AUTH_CONST.__objc_const: 0x101c0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2ab0
-  __AUTH.__data: 0x568
-  __DATA.__objc_ivar: 0x77c
-  __DATA.__data: 0x1b88
+  __AUTH.__data: 0x5f0
+  __DATA.__objc_ivar: 0x780
+  __DATA.__data: 0x1bd8
   __DATA.__bss: 0xf40
   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3454
-  Symbols:   3528
-  CStrings:  4796
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 3500
+  Symbols:   3535
+  CStrings:  4795
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _OBJC_CLASS_$_WBSSavedAccountMatchCriteria
CStrings:
+ "\x04\x11\x1a"
+ "\a\x11."
+ "\x1c\x13"
+ "Could not parse registration attestationObject."
+ "Could not parse registration authdata %!{(MISSING)public}s."
+ "_domainToNextIconDownloadRetryDate"
+ "_handleIconFetchFailureWithDomain:options:requestID:response:responseHandler:"
+ "_updateLastUsedDateForPasskeySavedAccountWithAssertion:relyingParty:context:"
+ "cachedIconForDomain:resizedToSize:"
+ "initWithInputValues:"
+ "initWithUser:password:site:creationDate:externalProviderBundleIdentifier:"
+ "nextIconDownloadRetryDate"
+ "performMaintenanceWork"
+ "providerBundleID"
+ "safari_setLastUsedDate:forPasskeyWithUserHandle:relyingPartyID:groupID:context:"
+ "shouldSendRequestEvenIfIconWasAlreadyRequestedForDomain"
+ "v56@0:8@16Q24@32@40@?48"
+ "\x92"
+ "\xf0!"
- "\x04\x11\x1b"
- "\x06\x11."
- "\x1c\x12"
- "@\"WBSSavedAccountStore\""
- "@48@0:8@16{CGSize=dd}24@?40"
- "T@\"WBSSavedAccountStore\",R,N,V_partialAccountStore"
- "_partialAccountStore"
- "_updateLastUsedDateForPasskeySavedAccountWithCredential:operation:"
- "cachedIconForDomain:resizedToSize:responseHandler:"
- "criteriaForNonAutofillablePasskeyWithCredentialIdentifier:"
- "exactMatches"
- "initPartialStoreForDomains:"
- "initWithUser:password:site:creationDate:isExternal:"
- "partialAccountStore"
- "savedAccount"
- "savedAccountsMatchingCriteria:withCompletionHandler:"
- "setLastUsedDate:forContext:"
- "v16@?0@\"WBSSavedAccountMatchResult\"8"
- "\x82"
- "\xf0\x11"

```
