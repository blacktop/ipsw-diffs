## securityd

> `/usr/libexec/securityd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__thread_vars`

```diff

-62460.40.78.0.0
-  __TEXT.__text: 0x26d64c
-  __TEXT.__auth_stubs: 0x43f0
-  __TEXT.__objc_stubs: 0x1dde0
-  __TEXT.__objc_methlist: 0x15fe0
+62460.60.42.502.1
+  __TEXT.__text: 0x26e438
+  __TEXT.__auth_stubs: 0x4400
+  __TEXT.__objc_stubs: 0x1dec0
+  __TEXT.__objc_methlist: 0x16048
   __TEXT.__const: 0x920
-  __TEXT.__cstring: 0x230c7
-  __TEXT.__objc_methname: 0x2ecbf
-  __TEXT.__oslogstring: 0x30404
+  __TEXT.__cstring: 0x2328b
+  __TEXT.__objc_methname: 0x2edcc
+  __TEXT.__oslogstring: 0x304fa
   __TEXT.__swift5_typeref: 0x372
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__objc_classname: 0x2584
-  __TEXT.__objc_methtype: 0xb1b4
+  __TEXT.__objc_methtype: 0xb18f
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_reflstr: 0xc3
   __TEXT.__swift5_capture: 0x1bc

   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x48
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__gcc_except_tab: 0xa104
+  __TEXT.__gcc_except_tab: 0xa1f8
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x7d40
+  __TEXT.__unwind_info: 0x7db8
   __TEXT.__eh_frame: 0xa60
-  __DATA_CONST.__const: 0x14b58
-  __DATA_CONST.__cfstring: 0x1cfa0
+  __DATA_CONST.__const: 0x14be8
+  __DATA_CONST.__cfstring: 0x1d120
   __DATA_CONST.__objc_classlist: 0x918
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x818
-  __DATA_CONST.__objc_intobj: 0x1470
+  __DATA_CONST.__objc_intobj: 0x1488
   __DATA_CONST.__objc_arraydata: 0x408
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA_CONST.__auth_got: 0x2208
-  __DATA_CONST.__got: 0x1560
+  __DATA_CONST.__auth_got: 0x2210
+  __DATA_CONST.__got: 0x1550
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA.__objc_const: 0x23ef0
-  __DATA.__objc_selrefs: 0x99b8
-  __DATA.__objc_ivar: 0x1b04
+  __DATA.__objc_const: 0x23f20
+  __DATA.__objc_selrefs: 0x99f0
+  __DATA.__objc_ivar: 0x1b08
   __DATA.__objc_data: 0x5de8
   __DATA.__data: 0x3158
   __DATA.__thread_vars: 0xc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9957
-  Symbols:   1907
-  CStrings:  16579
+  Functions: 9974
+  Symbols:   1906
+  CStrings:  16607
 
Symbols:
+ _dispatch_assert_queue_not$V2
- _kSecurityRTCEventNameFetchStableTrustedDeviceID
- _kSecurityRTCFieldIsDemoAccount
CStrings:
+ "-[CuttlefishXPCWrapper fetchEgoStableTrustedDeviceIDWithSpecificUser:reply:]_block_invoke"
+ "CK account credentials are invalid; pausing without local reset"
+ "CloudKit account credentials are invalid."
+ "CloudKit account credentials are invalid; push will not succeed."
+ "CloudKit account credentials are valid again."
+ "CloudKit account credentials valid again; resuming"
+ "CloudKit account present, but credentials are invalid. Pausing."
+ "Cuttlefish adapter not available"
+ "Cuttlefish adapter not present"
+ "No cached stableTrustedDeviceID: %@"
+ "No stableTrustedDeviceID available; skipping reroll check"
+ "T@\"NSOperation\",&,V_stableTrustedDeviceIDResolution"
+ "TDID cache miss, fetching trusted device list"
+ "Unable to fetch cached stableTrustedDeviceID from TPH: %@"
+ "User may not be signed into iCloud; account status is %ld"
+ "_stableTrustedDeviceIDResolution"
+ "ck-account-credentials-invalid"
+ "ck-account-credentials-valid"
+ "ck-credentials-invalid"
+ "ck-credentials-restored"
+ "ck_credentials_invalid"
+ "ck_credentials_valid"
+ "credentials invalid"
+ "errorForAccountStatus:"
+ "fail-creds-unavailable"
+ "fetchCachedStableTrustedDeviceIDFromTPHWithError:"
+ "fetchEgoStableTrustedDeviceIDWithSpecificUser:reply:"
+ "fetchLocalStableTrustedDeviceIDWithError:"
+ "fetchStableTrustedDeviceIDWithReply:"
+ "handleCKCredentialsInvalid"
+ "handleCKCredentialsValid"
+ "octagon-resolve-stable-id"
+ "octagon-stable-device-id: timed out waiting for trusted device list fetch"
+ "received a notification of CK credentials becoming invalid"
+ "received a notification of CK credentials becoming valid again"
+ "setStableTrustedDeviceIDResolution:"
+ "stableTrustedDeviceIDResolution"
+ "stableTrustedDeviceIDResolutionOperation:"
+ "trusted device list fetch complete: %@, stableTrustedDeviceID: %@"
+ "v24@?0@\"TPStableTrustedDeviceID\"8@\"NSError\"16"
+ "v32@0:8@\"TPSpecificUser\"16@?<v@?@\"TPStableTrustedDeviceID\"@\"NSError\">24"
+ "wait_for_ck_credentials"
- "@\"TPStableTrustedDeviceID\"56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40B44^@48"
- "@56@0:8@16@24@32B40B44^@48"
- "Rejecting PCS Identity requests since we don't have an iCloud account: %@"
- "Successfully fetched stableTrustedDeviceID: %@"
- "Unable to fetch AuthKit account for altDSID %@: %@"
- "fetchStableTrustedDeviceID: demo-account lookup failed: %@"
- "fetchStableTrustedDeviceID:flowID:deviceSessionID:canSendMetrics:stableTrustedDeviceIDInUse:error:"
- "fetchStableTrustedDeviceIDWithSessionMetrics:reply:"
- "octagon: Unable to fetch stableTrustedDeviceID: %@"
- "stableTrustedDeviceID for account doesn't have all the required fields"
- "stableTrustedDeviceID for account returned nil or empty"
- "trustedDeviceIdentifierForAccount doesn't have all the fields for altDSID %@"
- "trustedDeviceIdentifierForAccount returned nil or empty string for altDSID %@"
- "trustedDeviceIdentifierForAccount:"
```
