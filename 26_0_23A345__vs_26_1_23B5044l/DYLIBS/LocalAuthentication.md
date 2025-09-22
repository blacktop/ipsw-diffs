## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-2005.0.61.0.0
-  __TEXT.__text: 0x35958
+2005.40.31.0.0
+  __TEXT.__text: 0x355a0
   __TEXT.__auth_stubs: 0xaa0
   __TEXT.__objc_methlist: 0x3638
-  __TEXT.__const: 0x2d4
-  __TEXT.__gcc_except_tab: 0x1014
-  __TEXT.__cstring: 0x1849
+  __TEXT.__const: 0x2e4
+  __TEXT.__gcc_except_tab: 0x1008
+  __TEXT.__cstring: 0x1829
   __TEXT.__dlopen_cstrs: 0x1cd
-  __TEXT.__oslogstring: 0x2785
+  __TEXT.__oslogstring: 0x268f
   __TEXT.__swift5_typeref: 0x6e
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x12a8
+  __TEXT.__unwind_info: 0x12a0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x9c6
   __TEXT.__objc_methname: 0x6dcc
   __TEXT.__objc_methtype: 0x1c3a
-  __TEXT.__objc_stubs: 0x4980
-  __DATA_CONST.__got: 0x538
-  __DATA_CONST.__const: 0x1bb8
+  __TEXT.__objc_stubs: 0x4960
+  __DATA_CONST.__got: 0x578
+  __DATA_CONST.__const: 0x1b40
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x1e0
   __AUTH_CONST.__auth_got: 0x560
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x18c0
+  __AUTH_CONST.__cfstring: 0x1880
   __AUTH_CONST.__objc_const: 0x8080
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH.__objc_data: 0x5f0

   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: AEF9C2BF-45E0-3B66-9D7F-EE9E38AD96B5
-  Functions: 1452
-  Symbols:   5182
-  CStrings:  2215
+  UUID: A2586D0B-8DC9-3663-86C3-592358908E9D
+  Functions: 1455
+  Symbols:   5190
+  CStrings:  2212
 
Symbols:
+ -[LAContext _nullCharacterData]
+ GCC_except_table38
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table50
+ GCC_except_table57
+ GCC_except_table59
+ _LACErrorCodeAuthenticationFailed
+ _LACErrorCodeBiometryNotEnrolled
+ _LACErrorCodeDeviceTypeNotSupported
+ _LACErrorCodePasscodeNotSet
+ _LACErrorCodeRequestFailed
+ _LACErrorCodeUserCustomRatchetCancel
+ _LACErrorSubcodeBeforeFirstUnlock
+ _LACErrorSubcodeUnsatisfiable
+ ___36-[LAContext credentialOfType:reply:]_block_invoke.cold.2
+ ___44-[LAStorage objectForKey:completionHandler:]_block_invoke.23
+ ___44-[LAStorage processError:completionHandler:]_block_invoke.30
+ ___50-[LAStorage removeObjectForKey:completionHandler:]_block_invoke.24
+ ___51-[LAStorage exchangeData:forKey:completionHandler:]_block_invoke.28
+ ___60-[LAStorage setObject:forKey:withOptions:completionHandler:]_block_invoke.21
+ ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.103
+ ___block_descriptor_48_e8_32bs_e20_v24?08"NSError"16ls32l8
+ ___block_literal_global.203
- +[LAStorage objectDescription:]
- GCC_except_table43
- GCC_except_table51
- GCC_except_table55
- GCC_except_table58
- GCC_except_table60
- GCC_except_table64
- ___44-[LAStorage objectForKey:completionHandler:]_block_invoke.29
- ___44-[LAStorage processError:completionHandler:]_block_invoke.36
- ___50-[LAStorage removeObjectForKey:completionHandler:]_block_invoke.30
- ___51-[LAStorage exchangeData:forKey:completionHandler:]_block_invoke.34
- ___60-[LAStorage setObject:forKey:withOptions:completionHandler:]_block_invoke.27
- ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.109
- ___block_descriptor_56_e8_32s40bs_e20_v24?08"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs_e20_v24?08"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs_e20_v24?08"NSError"16ls32l8s40l8s48l8s56l8
- ___block_literal_global.211
- _objc_msgSend$objectDescription:
CStrings:
+ "Created LAStorage"
+ "Did reboot successfully"
+ "Encountered XPC error on remote proxy: %{private}@"
+ "Extracting a LACredentialTypeExtractablePassword will require the '%@' entitlement. The operation will be allowed for now. Error: %{public}@"
+ "Failed to reboot with error: %{private}@"
+ "Inconsistent result: both error and credential are valid"
+ "Rebooting for error"
+ "Stashing a LACredentialTypeExtractablePassword will require the '%@' entitlement. The operation will be allowed for now. Error: %{public}@"
+ "Will invoke authentication using policy %d"
+ "_nullCharacterData"
+ "exchangeData forKey:%d"
+ "exchangeData forKey:%d returned error: %{private}@"
+ "exchangeData forKey:%d returned success"
+ "objectForKey:%d"
+ "objectForKey:%d returned error: %{private}@"
+ "objectForKey:%d returned success"
+ "removeObjectForKey:%d"
+ "removeObjectForKey:%d returned error: %{private}@"
+ "removeObjectForKey:%d returned success"
+ "setObject forKey:%d"
+ "setObject forKey:%d returned error: %{private}@"
+ "setObject forKey:%d returned success"
- "%{public}@ has encountered XPC error on remote proxy: %{public}@"
- "%{public}@ will invoke authentication using policy %d"
- "Created %@"
- "Did reboot for %{public}@ on %{public}@"
- "Exchanging data with key %d with %{public}@ on %{public}@"
- "Extracting a LACredentialTypeExtractablePassword will require the '%@' entitlement in Luckier (rdar://140411675). Error: %{public}@"
- "Failed to exchange data for key %d with %{public}@ on %{public}@: %{public}@"
- "Failed to query key %d on %{public}@"
- "Failed to reboot for %{public}@ on %{public}@ with error: %{public}@"
- "Failed to remove key %d on %{public}@"
- "Failed to set key %d with value %{public}@ and options %{public}@ on %{public}@: %{public}@"
- "Key %d data exchanged successfully with %{public}@ on %{public}@"
- "Key %d set successfully with value %{public}@ and options %{public}@ on %{public}@"
- "Query of key %d returned %{public}@ on %{public}@"
- "Querying key %d on %{public}@"
- "Rebooting for %{public}@ on %{public}@"
- "Removed key %d on %{public}@"
- "Removing key %d on %{public}@"
- "Setting key %d with value %{public}@ and options %{public}@ on %{public}@"
- "Stashing a LACredentialTypeExtractablePassword will require the '%@' entitlement in Luckier (rdar://140411675). Error: %{public}@"
- "data[%d]"
- "objectDescription:"
- "unsupported object: %@"

```
