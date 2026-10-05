## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1626.200.65.0.0
-  __TEXT.__text: 0x1ad1f4
-  __TEXT.__objc_methlist: 0x1ba80
-  __TEXT.__cstring: 0x14616
-  __TEXT.__const: 0x4adc
-  __TEXT.__oslogstring: 0x14877
+1626.200.84.0.0
+  __TEXT.__text: 0x1b28e8
+  __TEXT.__objc_methlist: 0x1bb30
+  __TEXT.__cstring: 0x14716
+  __TEXT.__const: 0x4b6c
+  __TEXT.__oslogstring: 0x14bea
   __TEXT.__gcc_except_tab: 0x183c
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8a5
-  __TEXT.__constg_swiftt: 0xeb0
-  __TEXT.__swift5_typeref: 0x13a1
+  __TEXT.__constg_swiftt: 0xec4
+  __TEXT.__swift5_typeref: 0x1443
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_reflstr: 0xc89
-  __TEXT.__swift5_fieldmd: 0x1354
+  __TEXT.__swift5_fieldmd: 0x1320
   __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__swift5_proto: 0x3e0
-  __TEXT.__swift5_types: 0x150
-  __TEXT.__swift5_capture: 0x2b8
-  __TEXT.__swift_as_entry: 0xb4
-  __TEXT.__swift_as_ret: 0xcc
-  __TEXT.__swift_as_cont: 0x194
+  __TEXT.__swift5_proto: 0x3d8
+  __TEXT.__swift5_types: 0x14c
+  __TEXT.__swift5_capture: 0x38c
+  __TEXT.__swift_as_entry: 0xec
+  __TEXT.__swift_as_ret: 0x104
+  __TEXT.__swift_as_cont: 0x1e4
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x9640
-  __TEXT.__eh_frame: 0x2a78
+  __TEXT.__unwind_info: 0x9850
+  __TEXT.__eh_frame: 0x31e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3910
+  __DATA_CONST.__const: 0x3918
   __DATA_CONST.__objc_classlist: 0x8a8
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb8c0
+  __DATA_CONST.__objc_selrefs: 0xb900
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x6e8
   __DATA_CONST.__objc_arraydata: 0xac0
-  __DATA_CONST.__got: 0x10b0
-  __AUTH_CONST.__const: 0x4dd8
-  __AUTH_CONST.__cfstring: 0x12820
-  __AUTH_CONST.__objc_const: 0x2b648
+  __DATA_CONST.__got: 0x10a8
+  __AUTH_CONST.__const: 0x4ee0
+  __AUTH_CONST.__cfstring: 0x12900
+  __AUTH_CONST.__objc_const: 0x2b6d0
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x2e8
-  __AUTH_CONST.__auth_got: 0x1690
+  __AUTH_CONST.__auth_got: 0x1678
   __AUTH.__objc_data: 0x2b70
-  __AUTH.__data: 0xde0
-  __DATA.__objc_ivar: 0x194c
-  __DATA.__data: 0x3f20
+  __AUTH.__data: 0xe00
+  __DATA.__objc_ivar: 0x1954
+  __DATA.__data: 0x3f40
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x2da8
   __DATA_DIRTY.__data: 0x78

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11979
-  Symbols:   16252
-  CStrings:  4673
+  Functions: 12076
+  Symbols:   16279
+  CStrings:  4687
 
Symbols:
+ +[NSPredicate(TUManagedConversationLinkDescriptor) tu_predicateForConversationLinkDescriptorsIsAccessibilityLink:]
+ +[NSPredicate(TUManagedConversationLinkDescriptor) tu_predicateForConversationLinkDescriptorsWithPseudonyms:]
+ -[TUContinuityConversationLink groupUUID]
+ -[TUContinuityConversationLink initWithTUConversationLink:displayName:date:uniqueId:groupUUID:]
+ -[TUConversationLink isAccessibilityLink]
+ -[TUConversationManager accessibilityLinkPseudonymsAmongPseudonyms:completionHandler:]
+ -[TUConversationManager interpreterRequestWithID:debugSendLink:toHandle:]
+ -[TUConversationManagerXPCClient accessibilityLinkPseudonymsAmongPseudonyms:completionHandler:]
+ -[TUConversationManagerXPCClient interpreterRequestWithID:debugSendLink:toHandle:]
+ -[TUJoinConversationRequest handlesToAddAfterHandoff]
+ -[TUJoinConversationRequest setHandlesToAddAfterHandoff:]
+ GCC_except_table151
+ GCC_except_table177
+ GCC_except_table88
+ GCC_except_table91
+ _OBJC_IVAR_$_TUContinuityConversationLink._groupUUID
+ _OBJC_IVAR_$_TUJoinConversationRequest._handlesToAddAfterHandoff
+ _TUSimulatedModeEnabledKey
+ ___73-[TUConversationManager interpreterRequestWithID:debugSendLink:toHandle:]_block_invoke
+ ___73-[TUConversationManager interpreterRequestWithID:debugSendLink:toHandle:]_block_invoke_2
+ ___82-[TUConversationManagerXPCClient interpreterRequestWithID:debugSendLink:toHandle:]_block_invoke
+ ___95-[TUConversationManagerXPCClient accessibilityLinkPseudonymsAmongPseudonyms:completionHandler:]_block_invoke
+ _swift_deletedAsyncMethodErrorTu
+ _symbolic Scgyyt______pG s5ErrorP
+ _symbolic ShySSG
+ _symbolic ShySSGIeAgHr_
+ _symbolic _____ySSSaySo8TUHandleCGG s18_DictionaryStorageC
+ _symbolic _____yShySSGG 2os21OSAllocatedUnfairLockV
+ _symbolic _____yShySSG_G ScG8IteratorV
+ _symbolic _____yShySSG_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____ySo8TUHandleCSbG s18_DictionaryStorageC
+ _symbolic _____y_____y_____GG 2os21OSAllocatedUnfairLockV 18TelephonyUtilities23CancellableContinuationO AD15ResponseWrapperV
+ _symbolic yt______pIeghHrzo_ s5ErrorP
- -[TUContinuityConversationLink initWithTUConversationLink:displayName:date:uniqueId:]
- GCC_except_table149
- GCC_except_table175
- GCC_except_table87
- _associated conformance 18TelephonyUtilities17TUCallContextCardV4ItemO8BirthdayV15TUBirthdayStateOSHAASQ
- _symbolic _____ 18TelephonyUtilities17TUCallContextCardV4ItemO8BirthdayV15TUBirthdayStateO
CStrings:
+ " handlesToAddAfterHandoff=%@"
+ "Asked which of %lu pseudonym(s) are accessibility links"
+ "Companion Lockdown Mode Enabled"
+ "Error in retrieving accessibility link pseudonyms: %@"
+ "FaceTimeServiceAvailabilityHelper: Cannot generate IDS destination for handle, reporting false for handle: %@"
+ "FaceTimeServiceAvailabilityHelper: Every destination is FaceTime available, no need to wait for the remaining services"
+ "FaceTimeServiceAvailabilityHelper: Got %{public}s back for availability of service %s: %@"
+ "FaceTimeServiceAvailabilityHelper: Querying availability of FaceTime services for %ld handles across %ld destinations with timeout: %s"
+ "FaceTimeServiceAvailabilityHelper: The ID status cache reported every destination valid for service %s, skipping the network lookup"
+ "FaceTimeServiceAvailabilityHelper: Timeout reached querying batch availability of FaceTime, returning the results gathered so far"
+ "SimulatedModeEnabled"
+ "The companion device could not complete the operation because it has Lockdown Mode enabled."
+ "accessibilityReqUUID != NULL"
+ "accessibilityReqUUID == NULL"
+ "idStatus(for:service:fromNetwork:)"
+ "pseudonym IN %@"
- "requiredIDStatus(for:service:)"
- "simulatedMode"
```
