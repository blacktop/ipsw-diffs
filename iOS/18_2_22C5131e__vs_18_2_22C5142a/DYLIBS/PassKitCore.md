## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1591.3.9.1.0
-  __TEXT.__text: 0x7d9f78
-  __TEXT.__auth_stubs: 0x4990
-  __TEXT.__objc_methlist: 0x627e0
+1591.3.11.0.0
+  __TEXT.__text: 0x7da144
+  __TEXT.__auth_stubs: 0x49a0
+  __TEXT.__objc_methlist: 0x627f0
   __TEXT.__const: 0x20128
-  __TEXT.__cstring: 0x6678e
+  __TEXT.__cstring: 0x667e7
   __TEXT.__swift5_typeref: 0x5138
   __TEXT.__swift5_capture: 0x3590
-  __TEXT.__oslogstring: 0x3345a
+  __TEXT.__oslogstring: 0x33333
   __TEXT.__constg_swiftt: 0x48cc
   __TEXT.__swift5_fieldmd: 0x4d38
   __TEXT.__swift5_reflstr: 0x3e3d

   __TEXT.__swift5_types: 0x4dc
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0xe8
-  __TEXT.__gcc_except_tab: 0x740c
+  __TEXT.__gcc_except_tab: 0x7424
   __TEXT.__ustring: 0x1ed6
-  __TEXT.__unwind_info: 0x1b918
+  __TEXT.__unwind_info: 0x1b930
   __TEXT.__eh_frame: 0x5368
   __TEXT.__objc_classname: 0xf579
-  __TEXT.__objc_methname: 0xc43fa
+  __TEXT.__objc_methname: 0xc440f
   __TEXT.__objc_methtype: 0x16bdc
-  __TEXT.__objc_stubs: 0x56de0
+  __TEXT.__objc_stubs: 0x56dc0
   __DATA_CONST.__got: 0x44b8
-  __DATA_CONST.__const: 0x1f8b0
+  __DATA_CONST.__const: 0x1f8d8
   __DATA_CONST.__objc_classlist: 0x38a0
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x5a0

   __DATA_CONST.__objc_protorefs: 0x240
   __DATA_CONST.__objc_superrefs: 0x2ce8
   __DATA_CONST.__objc_arraydata: 0x3068
-  __AUTH_CONST.__auth_got: 0x24d8
-  __AUTH_CONST.__auth_ptr: 0x9f8
+  __AUTH_CONST.__auth_got: 0x24e0
+  __AUTH_CONST.__auth_ptr: 0xa18
   __AUTH_CONST.__const: 0x1c718
-  __AUTH_CONST.__cfstring: 0x6c880
-  __AUTH_CONST.__objc_const: 0xca7d0
+  __AUTH_CONST.__cfstring: 0x6c840
+  __AUTH_CONST.__objc_const: 0xca800
   __AUTH_CONST.__objc_arrayobj: 0xac8
   __AUTH_CONST.__objc_intobj: 0x1140
   __AUTH_CONST.__objc_dictobj: 0x1db0

   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x634c
-  __DATA.__data: 0x85d8
+  __DATA.__data: 0x8628
   __DATA.__bss: 0x16ed0
   __DATA.__common: 0x220
-  __DATA_DIRTY.__objc_ivar: 0x24ec
+  __DATA_DIRTY.__objc_ivar: 0x24f0
   __DATA_DIRTY.__objc_data: 0x57d0
   __DATA_DIRTY.__data: 0x168
-  __DATA_DIRTY.__bss: 0x1160
+  __DATA_DIRTY.__bss: 0x1180
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 48831
-  Symbols:   50676
-  CStrings:  51426
+  Functions: 48837
+  Symbols:   50682
+  CStrings:  51428
 
Symbols:
+ _PKGetLastProductCacheUpdateTimestamp
+ _PKLastProductCacheUpdateTimestampKey
+ _PKPaymentPreflightRequirementsImpactProducts
+ _PKSetLastProductCacheUpdateTimestamp
+ _SecTaskCopySigningIdentifier
CStrings:
+ "ConsumerContext: pass entries are not a valid entity class"
+ "ConsumerContext: pass entries is not a valid data structure"
+ "Ex<%@>: ConsumerContext: Proceeding with provisioning without fairplay data: %d for identifier: %@ and teamID: %{public}@"
+ "Ex<%@>: ConsumerContext: teamID is invalid"
+ "Ex<%@>: ConsumerContext: timeout trying to generate request with entry identifier: %@ for teamID: %{public}@"
+ "Ex<%@>: ConsumerContext: timeout trying to get pass entries with extension for teamID: %{public}@"
+ "Ex<%@>: ConsumerContext: timeout trying to get remote pass entries with extension for teamID: %{public}@"
+ "Ex<%@>: ConsumerContext: timeout trying to get status with extension for teamID: %{public}@"
+ "Ex<%@>: PKIssuerProvisioningExtensionConsumerCoordinator: failed to begin extension request with error %@."
+ "Ex<%@>: extension did not connect in time...timing out."
+ "Express.Mode"
+ "Express.State"
+ "Express.Transaction"
+ "PKLastProductCacheUpdateTimestampKey"
+ "Provisioning.Extension"
+ "Unable to generate personal vehicle identifier because required credential identifier is missing"
+ "_extensionIdentifier"
- "%@:%@-%@"
- "Falling back to hardcoded time interval for update Payment Setup Features %@"
- "PKIssuerProvisioningExtensionConsumerContext: Proceeding with provisioning without fairplay data: %d for identifier: %@ and teamID: %{public}@"
- "PKIssuerProvisioningExtensionConsumerContext: pass entries are not a valid entity class"
- "PKIssuerProvisioningExtensionConsumerContext: pass entries is not a valid data structure"
- "PKIssuerProvisioningExtensionConsumerContext: teamID is invalid"
- "PKIssuerProvisioningExtensionConsumerContext: timeout trying to generate request with entry identier: %@ for teamID: %{public}@"
- "PKIssuerProvisioningExtensionConsumerContext: timeout trying to get pass entries with extension for teamID: %{public}@"
- "PKIssuerProvisioningExtensionConsumerContext: timeout trying to get remote pass entries with extension for teamID: %{public}@"
- "PKIssuerProvisioningExtensionConsumerContext: timeout trying to get status with extension for teamID: %{public}@"
- "PKIssuerProvisioningExtensionConsumerCoordinator: extension did not connect in time...timing out."
- "PKIssuerProvisioningExtensionConsumerCoordinator: failed to begin extension request with error %@."
- "Unable to generate personal vehicle identifier because required credential identifiers are missing"
- "keyId"
- "sharedKeyID"

```
