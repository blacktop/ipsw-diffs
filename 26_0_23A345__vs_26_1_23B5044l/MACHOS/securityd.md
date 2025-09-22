## securityd

> `/usr/libexec/securityd`

```diff

-61901.0.87.0.1
-  __TEXT.__text: 0x258d38
-  __TEXT.__auth_stubs: 0x4280
-  __TEXT.__objc_stubs: 0x1c5e0
-  __TEXT.__objc_methlist: 0x15210
-  __TEXT.__const: 0x879
-  __TEXT.__objc_methname: 0x2c245
-  __TEXT.__cstring: 0x20e30
-  __TEXT.__oslogstring: 0x2cf5f
+61901.40.47.0.1
+  __TEXT.__text: 0x259fac
+  __TEXT.__auth_stubs: 0x4290
+  __TEXT.__objc_stubs: 0x1c640
+  __TEXT.__objc_methlist: 0x15220
+  __TEXT.__const: 0x891
+  __TEXT.__objc_methname: 0x2c31e
+  __TEXT.__cstring: 0x20f0f
+  __TEXT.__oslogstring: 0x2d2ad
   __TEXT.__swift5_typeref: 0x37a
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__constg_swiftt: 0x274

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__gcc_except_tab: 0xb5dc
+  __TEXT.__gcc_except_tab: 0xb5e4
   __TEXT.__objc_classname: 0x2360
-  __TEXT.__objc_methtype: 0xa46d
+  __TEXT.__objc_methtype: 0xa48e
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6780
+  __TEXT.__unwind_info: 0x6790
   __TEXT.__eh_frame: 0xa58
-  __DATA_CONST.__auth_got: 0x2150
+  __DATA_CONST.__auth_got: 0x2158
   __DATA_CONST.__got: 0x1340
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA_CONST.__const: 0x13fd8
-  __DATA_CONST.__cfstring: 0x1b100
+  __DATA_CONST.__cfstring: 0x1b1a0
   __DATA_CONST.__objc_classlist: 0x8b8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x7f8
-  __DATA_CONST.__objc_intobj: 0x12c0
+  __DATA_CONST.__objc_intobj: 0x1350
   __DATA_CONST.__objc_arraydata: 0x3f8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x227d0
-  __DATA.__objc_selrefs: 0x92b8
-  __DATA.__objc_ivar: 0x19ec
+  __DATA.__objc_const: 0x22820
+  __DATA.__objc_selrefs: 0x92d0
+  __DATA.__objc_ivar: 0x19f4
   __DATA.__objc_data: 0x5a28
   __DATA.__data: 0x2320
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0xe50
+  __DATA.__bss: 0xe60
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E102FA55-65BD-3065-A9B3-CB72DF11FB94
-  Functions: 9606
-  Symbols:   1771
-  CStrings:  19496
+  UUID: FAEA432F-3540-3B4F-ACBC-D9F219D52A14
+  Functions: 9610
+  Symbols:   1772
+  CStrings:  19524
 
Symbols:
+ _mach_absolute_time
CStrings:
+ "%@ sync engine finished sending changes"
+ "%@ sync engine received error: %{public}@ while fetching zone changes for: %{private}@"
+ "%@ sync engine received unknown event"
+ "%@ sync engine received zone not found error for zone: %{private}@, treating as zone deletion"
+ "%@ sync engine will fetch changes due to reason: %ld"
+ "%@ sync engine will fetch changes for zone: %{private}@"
+ "%@ sync engine will send changes"
+ "-[CuttlefishXPCWrapper requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:knownFederations:flowID:deviceSessionID:reply:]_block_invoke"
+ "@32@0:8#16^@24"
+ "@72@0:8@16@24@32@40B48B52B56B60B64B68"
+ "@sum.self"
+ "Can't not remove owner: %{private}@ %{private}@; Skipping"
+ "Database incoming changes deletion reason %@ in %@ sync engine"
+ "Database incoming record zone %@ changes reason in %@ sync engine"
+ "Do not have proper participant role for share membership"
+ "Do not have proper participant role for share membership %{private}@"
+ "Error while archiving %@ sync engine state metadata"
+ "Error: %@ (Domain: %@, Code: %ld)"
+ "Erroring out with error: %@ on fetching remote changes during account change notification"
+ "Fetched share participants info for %{private}@, \n %{private}@"
+ "Final counts - Unknown: %@, Passkey: %{private}@, Password: %{private}@, Share: %{private}@, Sum: %lu"
+ "Force-fetch on account change Info: Shares:%lu Items:%lu Time: %llums"
+ "Group participants Info: %{private}@ \n Share Participants Info: %{private}@ \n fetched share participants info: %{private}@"
+ "Group update info for added participants: %{private}@"
+ "No Updates, not posting notification %@"
+ "Old Share: %{private}@ \n New Share: %{private}@ \n Added participants: %{private}@ \n Departed participants: %{private}@"
+ "SELECT %@, COUNT(*) FROM %@ WHERE agrp = ? GROUP BY %@"
+ "Successful Force-fetch remote changes complete during account change notification"
+ "TB,R,V_caesarPeerCleanup"
+ "Trying to add the owner: %{private}@ again %{private}@"
+ "_caesarPeerCleanup"
+ "_caesarPeersCleanup"
+ "caesarPeerCleanup"
+ "checkOctagonHealth:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:reply:"
+ "com.apple.security.keychain.sharing.initialFetch"
+ "countAllSharingGroupAndItems:withError:"
+ "healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:reply:"
+ "initWithDependencies:intendedState:errorState:deviceInfo:skipRateLimitedCheck:reportRateLimitingError:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:"
+ "requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:danglingPeerCleanup:caesarPeerCleanup:updateIdMS:knownFederations:flowID:deviceSessionID:reply:"
+ "stringWithCString:"
+ "v44@0:8B16B20B24B28B32@?36"
+ "v52@0:8@\"OTControlArguments\"16B24B28B32B36B40@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">44"
+ "v52@0:8@16B24B28B32B36B40@?44"
+ "v76@0:8@\"TPSpecificUser\"16B24B28B32B36B40@\"NSArray\"44@\"NSString\"52@\"NSString\"60@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">68"
+ "v76@0:8@16B24B28B32B36B40@44@52@60@?68"
+ "valueForKeyPath:"
- "%@sync engine finished sending changes"
- "%@sync engine received error: %{public}@ while fetching zone changes for: %{private}@"
- "%@sync engine received unknown event"
- "%@sync engine will fetch changes due to reason: %ld"
- "%@sync engine will fetch changes for zone: %{private}@"
- "%@sync engine will send changes"
- "-[CuttlefishXPCWrapper requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:danglingPeerCleanup:updateIdMS:knownFederations:flowID:deviceSessionID:reply:]_block_invoke"
- "@68@0:8@16@24@32@40B48B52B56B60B64"
- "Database incoming changes deletion reason %@ in %@sync engine"
- "Database incoming record zone %@ changes reason in %@sync engine"
- "Error while archiving %@sync engine state metadata"
- "Erroring out on fetching remote changes during the sync engine's account change notification"
- "Force-fetch remote changes complete during the sync engine's account change notification"
- "checkOctagonHealth:repair:danglingPeerCleanup:updateIdMS:reply:"
- "healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:updateIdMS:reply:"
- "initWithDependencies:intendedState:errorState:deviceInfo:skipRateLimitedCheck:reportRateLimitingError:repair:danglingPeerCleanup:updateIdMS:"
- "inviteStatus"
- "requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:danglingPeerCleanup:updateIdMS:knownFederations:flowID:deviceSessionID:reply:"
- "v40@0:8B16B20B24B28@?32"
- "v48@0:8@\"OTControlArguments\"16B24B28B32B36@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">40"
- "v48@0:8@16B24B28B32B36@?40"
- "v72@0:8@\"TPSpecificUser\"16B24B28B32B36@\"NSArray\"40@\"NSString\"48@\"NSString\"56@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">64"
- "v72@0:8@16B24B28B32B36@40@48@56@?64"

```
