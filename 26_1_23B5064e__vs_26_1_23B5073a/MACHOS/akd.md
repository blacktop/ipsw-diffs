## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-525.126.5.1.0
-  __TEXT.__text: 0x2706f0
+525.127.1.0.0
+  __TEXT.__text: 0x272f78
   __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_stubs: 0x191a0
-  __TEXT.__objc_methlist: 0xb4fc
-  __TEXT.__const: 0x45d0
-  __TEXT.__cstring: 0xcf93
+  __TEXT.__objc_stubs: 0x19280
+  __TEXT.__objc_methlist: 0xb564
+  __TEXT.__const: 0x4b90
+  __TEXT.__cstring: 0xcf63
   __TEXT.__objc_classname: 0x1a02
-  __TEXT.__objc_methtype: 0x6129
-  __TEXT.__gcc_except_tab: 0x3d64
-  __TEXT.__objc_methname: 0x23aa5
-  __TEXT.__oslogstring: 0x22f58
+  __TEXT.__objc_methtype: 0x6149
+  __TEXT.__gcc_except_tab: 0x3d80
+  __TEXT.__objc_methname: 0x23bd5
+  __TEXT.__oslogstring: 0x23158
   __TEXT.__dlopen_cstrs: 0x15f
-  __TEXT.__swift5_typeref: 0x258f
-  __TEXT.__swift5_fieldmd: 0xf30
-  __TEXT.__constg_swiftt: 0x17f8
-  __TEXT.__swift5_reflstr: 0xde0
-  __TEXT.__swift5_builtin: 0xf0
+  __TEXT.__swift5_typeref: 0x25b5
+  __TEXT.__swift5_fieldmd: 0xf58
+  __TEXT.__constg_swiftt: 0x1820
+  __TEXT.__swift5_reflstr: 0xe30
+  __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_capture: 0x1700
   __TEXT.__swift5_proto: 0x19c
-  __TEXT.__swift5_types: 0x144
+  __TEXT.__swift5_types: 0x148
   __TEXT.__swift_as_entry: 0x3d8
   __TEXT.__swift_as_ret: 0x4bc
   __TEXT.__swift5_protos: 0x3c
-  __TEXT.__unwind_info: 0x5c20
-  __TEXT.__eh_frame: 0xad98
+  __TEXT.__unwind_info: 0x5c40
+  __TEXT.__eh_frame: 0xadc8
   __DATA_CONST.__auth_got: 0xff0
-  __DATA_CONST.__got: 0x18d0
-  __DATA_CONST.__auth_ptr: 0x530
-  __DATA_CONST.__const: 0x112a8
-  __DATA_CONST.__cfstring: 0x7d40
+  __DATA_CONST.__got: 0x18f8
+  __DATA_CONST.__auth_ptr: 0x550
+  __DATA_CONST.__const: 0x113b8
+  __DATA_CONST.__cfstring: 0x7cc0
   __DATA_CONST.__objc_classlist: 0x780
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x338

   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__objc_intobj: 0x360
+  __DATA_CONST.__objc_intobj: 0x348
   __DATA_CONST.__objc_arraydata: 0x368
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__linkguard: 0x3e
-  __DATA.__objc_const: 0x26580
-  __DATA.__objc_selrefs: 0x7aa8
+  __DATA.__objc_const: 0x265a8
+  __DATA.__objc_selrefs: 0x7ae0
   __DATA.__objc_ivar: 0xa74
-  __DATA.__objc_data: 0x5a88
-  __DATA.__data: 0x3f08
+  __DATA.__objc_data: 0x5a98
+  __DATA.__data: 0x3f38
   __DATA.__bss: 0x3140
   __DATA.__common: 0x121
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 602DF275-E905-3CD6-BBD6-BA0F249A88B1
-  Functions: 7542
-  Symbols:   1457
-  CStrings:  11255
+  UUID: ECFEE605-89C4-340F-A6AA-0268EB85E481
+  Functions: 7560
+  Symbols:   1465
+  CStrings:  11265
 
Symbols:
+ _$s2os21OSAllocatedUnfairLockVMn
+ _$ss13ManagedBufferCMn
+ _$ss6UInt32VMn
+ _AKBAAExclusionProcessBagConfigKey
+ _AKBAAExclusionVIPsBagConfigKey
+ _AKBAAOnlyAllowedProcessBagConfigKey
+ _AKBAAOnlyAllowedVIPsBagConfigKey
+ _AKUserInfoADPBlockModeUnenrollContextKey
CStrings:
+ "Attestation map does not contain the cert attestation. Skipping device token fetch."
+ "BAA exclusion: Config allows process '%@' but not URL host '%@'"
+ "BAA exclusion: Invalid configuration - AKBAAOnlyAllowedVIPsBagConfigKey is empty"
+ "BAA operations not yet successful, aborting device token request"
+ "Checking for device token feature status in URL bag."
+ "Excluding [%@] for request [%@]"
+ "Failed to fetch device token. Proceeding with cert headers. Error: %@"
+ "Refreshing BAA device token"
+ "Trying to heal UCRT with credentials."
+ "_attemptUCRTHealingWithResponse:"
+ "_doesHostVIPMatch:vipList:"
+ "_handleAllowListLogicForProcess:requestHost:processName:completion:"
+ "_handleExclusionLogicForProcessName:requestHostName:completion:"
+ "_healUCRTWithAppleID:passwordPET:"
+ "_isProcessAllowed:completion:"
+ "_isProcessExcluded:completion:"
+ "_isURLHostVIPAllowed:completion:"
+ "_isURLHostVIPExcluded:completion:"
+ "_shouldExcludeBAAForProcessName:requestHostName:completion:"
+ "com.apple.authkit.heal-ucrt"
+ "haveBAAOperationsSucceeded"
+ "healUCRTWithUsername:passwordPET:"
+ "markBAAOperationSuccessful"
+ "service:account:inviteDroppedForSessionID:fromID:context:error:"
+ "v44@0:8B16@20@28@?36"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
- "ADP Block Mode parameter must be exactly 1"
- "Failed to fetch BAA device token %@"
- "_isHostExcludedForRequestVIP:excludedVIPList:"
- "_shouldExcludeBAAForProcess:completion:"
- "_shouldExcludeBAAForRequest:completion:"
- "_shouldExcludeBAAForURL:completion:"
- "baa-attestation-exclusion-vip"
- "baa-exclusion-process"
- "baa-exclusion-vip"
- "isEqualToNumber:"
- "service:account:inviteDroppedForSessionID:fromID:error:"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"

```
