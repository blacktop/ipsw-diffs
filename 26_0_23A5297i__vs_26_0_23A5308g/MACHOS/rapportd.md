## rapportd

> `/usr/libexec/rapportd`

```diff

-712.100.1.0.0
-  __TEXT.__text: 0x10e4d8
-  __TEXT.__auth_stubs: 0x3190
-  __TEXT.__objc_stubs: 0x102a0
-  __TEXT.__objc_methlist: 0x831c
-  __TEXT.__const: 0x4548
-  __TEXT.__gcc_except_tab: 0x1fc8
-  __TEXT.__cstring: 0x2cc51
+714.100.1.0.0
+  __TEXT.__text: 0x111218
+  __TEXT.__auth_stubs: 0x3220
+  __TEXT.__objc_stubs: 0x102c0
+  __TEXT.__objc_methlist: 0x832c
+  __TEXT.__const: 0x4568
+  __TEXT.__gcc_except_tab: 0x1fdc
+  __TEXT.__cstring: 0x2cfc1
   __TEXT.__objc_classname: 0xa62
-  __TEXT.__objc_methtype: 0x3b88
-  __TEXT.__objc_methname: 0x170c6
-  __TEXT.__oslogstring: 0x15d2
-  __TEXT.__swift5_typeref: 0xd8e
-  __TEXT.__swift5_capture: 0x620
+  __TEXT.__objc_methtype: 0x3b9c
+  __TEXT.__objc_methname: 0x17184
+  __TEXT.__oslogstring: 0x1592
+  __TEXT.__swift5_typeref: 0xdbc
+  __TEXT.__swift5_capture: 0x624
   __TEXT.__constg_swiftt: 0x830
-  __TEXT.__swift5_reflstr: 0x764
-  __TEXT.__swift5_fieldmd: 0x8b8
+  __TEXT.__swift5_reflstr: 0x7a4
+  __TEXT.__swift5_fieldmd: 0x8d0
   __TEXT.__swift5_proto: 0x160
   __TEXT.__swift5_types: 0xb4
-  __TEXT.__swift_as_entry: 0xec
-  __TEXT.__swift_as_ret: 0xec
+  __TEXT.__swift_as_entry: 0xf0
+  __TEXT.__swift_as_ret: 0xf4
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_assocty: 0xe8
   __TEXT.__swift5_acfuncs: 0x28
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3e30
-  __TEXT.__eh_frame: 0x1fd4
-  __DATA_CONST.__auth_got: 0x18d8
+  __TEXT.__unwind_info: 0x3ec0
+  __TEXT.__eh_frame: 0x2064
+  __DATA_CONST.__auth_got: 0x1920
   __DATA_CONST.__got: 0x840
   __DATA_CONST.__auth_ptr: 0x520
-  __DATA_CONST.__const: 0x6400
-  __DATA_CONST.__cfstring: 0x5d80
+  __DATA_CONST.__const: 0x64d8
+  __DATA_CONST.__cfstring: 0x5e20
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xe198
-  __DATA.__objc_selrefs: 0x4f50
-  __DATA.__objc_ivar: 0xe4c
-  __DATA.__objc_data: 0x1fe8
-  __DATA.__data: 0x2bf8
-  __DATA.__bss: 0x3560
+  __DATA.__objc_const: 0xe208
+  __DATA.__objc_selrefs: 0x4f78
+  __DATA.__objc_ivar: 0xe50
+  __DATA.__objc_data: 0x1ff8
+  __DATA.__data: 0x2c18
+  __DATA.__bss: 0x3570
   __DATA.__common: 0xc0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
-  - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 852581B4-D487-3301-9957-720213FE9380
-  Functions: 6230
-  Symbols:   1234
-  CStrings:  9855
+  UUID: 6AE29BDF-CB11-33B6-8B8C-2A9F85F590D6
+  Functions: 6259
+  Symbols:   1243
+  CStrings:  9890
 
Symbols:
+ _$s10Foundation4DataV4hash4intoys6HasherVz_tF
+ _$s10Foundation4DateV18addingTimeIntervalyACSdF
+ _$s10Foundation4DateV1goiySbAC_ACtFZ
+ _$s10Foundation4DateVACycfC
+ _$sSSs23CustomStringConvertiblesWP
+ _$sSh15minimumCapacityShyxGSi_tcfC
+ _$ss15ContiguousArrayV034_makeUniqueAndReserveCapacityIfNotD0yyFyXl_Ts5
+ _$ss15ContiguousArrayV12_endMutationyyFyXl_Ts5
+ _$ss15ContiguousArrayV36_reserveCapacityAssumingUniqueBuffer8oldCountySi_tFyXl_Ts5
+ _$ss15ContiguousArrayV37_appendElementAssumeUniqueAndCapacity_03newD0ySi_xntFyXl_Ts5
+ _OBJC_CLASS_$_IDSAccount
- _$s10Foundation4DataVs23CustomStringConvertibleAAMc
- _OBJC_CLASS_$_SDRDiagnosticReporter
CStrings:
+ "-[RPAutoBugCapture reportIssueOfType:issueContext:processName:triggerThresholdValues:]_block_invoke"
+ "-[RPAutoBugCapture reportIssueOfType:issueContext:processName:triggerThresholdValues:]_block_invoke_2"
+ "-[RPCloudDaemon idsAccountSet]"
+ "-[RPCompanionLinkXPCConnection companionLinkSendRequestID:request:destinationID:options:nwActivityToken:responseHandler:]_block_invoke"
+ "-[RPCompanionLinkXPCConnection receivedEventID:event:options:]"
+ "-[RPCompanionLinkXPCConnection receivedRequestID:request:options:responseHandler:]"
+ "-[RPPeopleDaemon sendFriendRequest:nonWakingRequest:sendersKnownAlias:]_block_invoke"
+ "@\"OS_dispatch_queue\""
+ "AuthTag doesn't match identity %@ - %s needs identity share"
+ "Get IDSAccounts\n"
+ "LargeReceive"
+ "LargeSend"
+ "Loaded validated handles %s"
+ "Mising BT data"
+ "Missing BT data"
+ "No authTag to verify identity - matching identities %ld - attempted sync previously %{bool}d"
+ "Received Large Event: %zu bytes for '%@' being handled by '%@'\n"
+ "Received Large Request: %zu bytes for '%@' being handled by '%@'\n"
+ "Received Large Response: %zu bytes for '%@' being handled by '%@'\n"
+ "SDRDiagnosticReporter"
+ "SFAppleIDClient"
+ "Sending identity share request to %s from %s"
+ "T@\"NSSet\",R"
+ "Unable to fetch AppleID account info %@"
+ "Unable to fetch friend device identities"
+ "_idsAccountSet"
+ "_rP"
+ "attemptedSyncPeers"
+ "contactInfo"
+ "idsAccountSet"
+ "len:%zu,check:%d"
+ "myAccountWithCompletion:"
+ "receivedEventID"
+ "receivedRequestID"
+ "receivedResponse"
+ "reportIssueOfType:issueContext:processName:triggerThresholdValues:"
+ "sendFriendRequest:nonWakingRequest:sendersKnownAlias:"
+ "v24@?0@\"SFAppleIDAccount\"8@\"NSError\"16"
+ "v48@0:8Q16@24@32@40"
+ "validatedAppleIDHandles"
+ "validatedEmailAddresses"
+ "validatedPhoneNumbers"
- "-[RPAutoBugCapture reportIssueOfType:issueContext:processName:]_block_invoke"
- "-[RPAutoBugCapture reportIssueOfType:issueContext:processName:]_block_invoke_2"
- "-[RPPeopleDaemon sendFriendRequest:nonWakingRequest:]_block_invoke"
- "Checking handle for identity share %s"
- "Matching identity found %@ for handle %s"
- "No authTag in advertisement - skipping identity share for identity %@"
- "No matching identity found - needs identity share"
- "Sending identity share request to %s"
- "Unable to fetch friend identities"
- "Verification of authTag failed - needs identity share due to rolled identity or unknown device"
- "sendFriendRequest:"
- "sendFriendRequest:nonWakingRequest:"

```
