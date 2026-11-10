## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Versions/A/Transparency`

```diff

-1766.0.60.0.0
-  __TEXT.__text: 0x82e1c
-  __TEXT.__objc_methlist: 0x4a90
-  __TEXT.__cstring: 0x308c
-  __TEXT.__const: 0x4a80
-  __TEXT.__gcc_except_tab: 0x4fc
-  __TEXT.__oslogstring: 0x1e5b
-  __TEXT.__swift5_typeref: 0x1050
-  __TEXT.__swift5_reflstr: 0x95a
+1766.40.58.0.0
+  __TEXT.__text: 0x87eec
+  __TEXT.__objc_methlist: 0x4b70
+  __TEXT.__cstring: 0x318c
+  __TEXT.__const: 0x4ee0
+  __TEXT.__gcc_except_tab: 0x528
+  __TEXT.__oslogstring: 0x229b
+  __TEXT.__swift5_typeref: 0x10e4
+  __TEXT.__swift5_reflstr: 0x9ca
   __TEXT.__swift5_assocty: 0x260
-  __TEXT.__constg_swiftt: 0xad8
+  __TEXT.__constg_swiftt: 0xb44
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_proto: 0x3a8
-  __TEXT.__swift5_types: 0xf0
-  __TEXT.__swift_as_entry: 0x120
-  __TEXT.__swift_as_ret: 0xfc
-  __TEXT.__swift_as_cont: 0x200
-  __TEXT.__swift5_fieldmd: 0xcb0
+  __TEXT.__swift5_proto: 0x3c4
+  __TEXT.__swift5_types: 0xf8
+  __TEXT.__swift_as_entry: 0x148
+  __TEXT.__swift_as_ret: 0x11c
+  __TEXT.__swift_as_cont: 0x248
+  __TEXT.__swift5_fieldmd: 0xd90
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift5_acfuncs: 0x168
+  __TEXT.__swift5_acfuncs: 0x1b8
   __TEXT.__swift5_capture: 0x2c4
-  __TEXT.__unwind_info: 0x2bb0
-  __TEXT.__eh_frame: 0x3628
+  __TEXT.__unwind_info: 0x2d00
+  __TEXT.__eh_frame: 0x38e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2030
+  __DATA_CONST.__objc_selrefs: 0x20b8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x180
-  __DATA_CONST.__got: 0x650
-  __AUTH_CONST.__const: 0x4ea8
-  __AUTH_CONST.__cfstring: 0x3aa0
-  __AUTH_CONST.__objc_const: 0x8020
+  __DATA_CONST.__got: 0x668
+  __AUTH_CONST.__const: 0x5228
+  __AUTH_CONST.__cfstring: 0x3ae0
+  __AUTH_CONST.__objc_const: 0x8140
   __AUTH_CONST.__objc_intobj: 0x1e0
-  __AUTH_CONST.__auth_got: 0xb50
+  __AUTH_CONST.__auth_got: 0xb78
   __AUTH_CONST.__auth_ptr: 0x390
-  __AUTH.__objc_data: 0x2d8
-  __AUTH.__data: 0x378
-  __DATA.__objc_ivar: 0x3b0
-  __DATA.__data: 0xfd8
-  __DATA.__bss: 0x6960
+  __AUTH.__data: 0x98
+  __DATA.__objc_ivar: 0x3c8
+  __DATA.__data: 0x928
+  __DATA.__bss: 0x6d10
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1af8
-  __DATA_DIRTY.__data: 0x4a8
-  __DATA_DIRTY.__bss: 0x11e0
+  __DATA_DIRTY.__objc_data: 0x1dd0
+  __DATA_DIRTY.__data: 0xf20
+  __DATA_DIRTY.__bss: 0x11f0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3830
-  Symbols:   4488
-  CStrings:  772
+  Functions: 3961
+  Symbols:   4562
+  CStrings:  797
 
Symbols:
+ +[TransparencyXPCConnection nowNs]
+ -[KTQueryOptions queryReason]
+ -[KTQueryOptions setQueryReason:]
+ -[KTVerifierResult showsTreeResetWarning]
+ -[KTVerifierResult updateTreeResetInProgress:]
+ -[KTVerifierResult updateWithStaticKeyEnforcedPeerEnforcement:isFailureIgnoredForDate:]
+ -[TransparencyAnalytics fuzzyDaysSinceDate:]
+ -[TransparencyXPCConnection dropConnectionForGeneration:]
+ -[TransparencyXPCConnection firstSuppressedNs]
+ -[TransparencyXPCConnection flushSuppressedPeerExits:]
+ -[TransparencyXPCConnection generation]
+ -[TransparencyXPCConnection lastPeerExitLogNs]
+ -[TransparencyXPCConnection lastSuppressedNs]
+ -[TransparencyXPCConnection logPeerExit:]
+ -[TransparencyXPCConnection setFirstSuppressedNs:]
+ -[TransparencyXPCConnection setGeneration:]
+ -[TransparencyXPCConnection setLastPeerExitLogNs:]
+ -[TransparencyXPCConnection setLastSuppressedNs:]
+ -[TransparencyXPCConnection setSuppressedPeerExits:]
+ -[TransparencyXPCConnection suppressedPeerExits]
+ GCC_except_table103
+ GCC_except_table12
+ GCC_except_table162
+ GCC_except_table197
+ GCC_except_table236
+ GCC_except_table25
+ GCC_except_table36
+ GCC_except_table9
+ OBJC_IVAR_$_KTQueryOptions._queryReason
+ OBJC_IVAR_$_TransparencyXPCConnection._firstSuppressedNs
+ OBJC_IVAR_$_TransparencyXPCConnection._generation
+ OBJC_IVAR_$_TransparencyXPCConnection._lastPeerExitLogNs
+ OBJC_IVAR_$_TransparencyXPCConnection._lastSuppressedNs
+ OBJC_IVAR_$_TransparencyXPCConnection._suppressedPeerExits
+ _NSDebugDescriptionErrorKey
+ _NSInvalidArchiveOperationException
+ _OBJC_CLASS_$_NSException
+ __27-[KTIDSData initWithCoder:]_block_invoke
+ __29-[KTIDSData encodeWithCoder:]_block_invoke
+ __30-[KTIDSDataURI initWithCoder:]_block_invoke
+ __41-[TransparencyXPCConnection logPeerExit:]_block_invoke
+ __51-[SoftwareTransparency sysdiagnoseInfo:completion:]_block_invoke
+ __54-[TransparencyXPCConnection flushSuppressedPeerExits:]_block_invoke
+ __87-[KTVerifierResult updateWithStaticKeyEnforcedPeerEnforcement:isFailureIgnoredForDate:]_block_invoke
+ __88-[SoftwareTransparency verifyExpiringProofs:forDigest:configuration:counter:completion:]_block_invoke
+ ___27-[KTIDSData initWithCoder:]_block_invoke
+ ___29-[KTIDSData encodeWithCoder:]_block_invoke
+ ___30-[KTIDSDataURI initWithCoder:]_block_invoke
+ ___32-[KTIDSDataURI encodeWithCoder:]_block_invoke
+ ___41-[TransparencyXPCConnection logPeerExit:]_block_invoke
+ ___43-[KTIDSDataURI initWithIDSData:ktResponse:]_block_invoke
+ ___46-[KTVerifierResult updateTreeResetInProgress:]_block_invoke
+ ___51-[SoftwareTransparency sysdiagnoseInfo:completion:]_block_invoke_2
+ ___54-[TransparencyXPCConnection flushSuppressedPeerExits:]_block_invoke
+ ___87-[KTVerifierResult updateWithStaticKeyEnforcedPeerEnforcement:isFailureIgnoredForDate:]_block_invoke
+ ___88-[SoftwareTransparency verifyExpiringProofs:forDigest:configuration:counter:completion:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40w_e5_v8?0l
+ ___block_descriptor_56_e8_32s40w_e5_v8?0l
+ ___copy_helper_block_e8_32s40w
+ ___destroy_helper_block_e8_32s40w
+ _associated conformance 12Transparency15CKVLastRanEntryV10CodingKeys33_5CE8840853DFFCDC7F035A4955177193LLOSHAASQ
+ _associated conformance 12Transparency15CKVLastRanEntryV10CodingKeys33_5CE8840853DFFCDC7F035A4955177193LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 12Transparency15CKVLastRanEntryV10CodingKeys33_5CE8840853DFFCDC7F035A4955177193LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _clock_gettime_nsec_np
+ _dispatch_after
+ _dispatch_time
+ _kTransparencyStaticKeyStoreContactExternalURI
+ _objc_msgSend$dropConnectionForGeneration:
+ _objc_msgSend$firstSuppressedNs
+ _objc_msgSend$flushSuppressedPeerExits:
+ _objc_msgSend$generation
+ _objc_msgSend$lastPeerExitLogNs
+ _objc_msgSend$lastSuppressedNs
+ _objc_msgSend$logPeerExit:
+ _objc_msgSend$nowNs
+ _objc_msgSend$queryReason
+ _objc_msgSend$raise:format:
+ _objc_msgSend$setFirstSuppressedNs:
+ _objc_msgSend$setGeneration:
+ _objc_msgSend$setLastPeerExitLogNs:
+ _objc_msgSend$setLastSuppressedNs:
+ _objc_msgSend$setQueryReason:
+ _objc_msgSend$setSuppressedPeerExits:
+ _objc_msgSend$showsTreeResetWarning
+ _objc_msgSend$suppressedPeerExits
+ _objc_msgSend$updateWithStaticKeyEnforcedPeerEnforcement:isFailureIgnoredForDate:
+ _symbolic Say_____G 12Transparency15CKVLastRanEntryV
+ _symbolic _____ 12Transparency15CKVLastRanEntryV
+ _symbolic _____ 12Transparency15CKVLastRanEntryV10CodingKeys33_5CE8840853DFFCDC7F035A4955177193LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12Transparency15CKVLastRanEntryV10CodingKeys33_5CE8840853DFFCDC7F035A4955177193LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12Transparency15CKVLastRanEntryV10CodingKeys33_5CE8840853DFFCDC7F035A4955177193LLO
+ _symbolic xSay_____G______p_____Rz_____RzlIetMHgozo_ 12Transparency15CKVLastRanEntryV s5ErrorP 11Distributed01_F9ActorStubP AA21CKVDiagnosticsServiceP
+ _symbolic xSay_____G______p_____RzlIetWHgozo_ 12Transparency15CKVLastRanEntryV s5ErrorP AA21CKVDiagnosticsServiceP
- -[KTVerifierResult updateWithStaticKeyEnforcedPeerEnforcement:]
- -[SoftwareTransparency verifyExpiringProofs:for:counter:completion:]
- GCC_except_table101
- GCC_except_table156
- GCC_except_table191
- GCC_except_table230
- GCC_except_table29
- GCC_except_table3
- GCC_except_table8
- _KTIDStaticKeyStoreEntryChanged
- _KTIDStaticKeyStoreEntryIdentifier
- __45-[TransparencyXPCConnection createConnection]_block_invoke_2
- __63-[KTVerifierResult updateWithStaticKeyEnforcedPeerEnforcement:]_block_invoke
- ___63-[KTVerifierResult updateWithStaticKeyEnforcedPeerEnforcement:]_block_invoke
- ___68-[SoftwareTransparency verifyExpiringProofs:for:counter:completion:]_block_invoke
- __swift_get_extra_inhabitant_index.13Tm
- __swift_store_extra_inhabitant_index.14Tm
- _objc_msgSend$initWithDomain:code:userInfo:
- _objc_msgSend$updateWithStaticKeyEnforcedPeerEnforcement:
CStrings:
+ "<KTQueryOptions: flags: %08x timeout: %f reason: %ld>"
+ "KTIDSData: decoded without application, dropping"
+ "KTIDSData: decoded without ktAccountKey for %@, dropping"
+ "KTIDSData: decoded without uri, dropping"
+ "KTIDSData: encoding without application for %@"
+ "KTIDSData: encoding without ktAccountKey for %@ %@"
+ "KTIDSData: encoding without uri"
+ "KTIDSDataURI has no idsData or ktResponse"
+ "KTIDSDataURI: created with idsData: %@ ktResponse: %@"
+ "KTIDSDataURI: decoded without idsData, dropping"
+ "KTIDSDataURI: decoded without ktResponse for %@, dropping"
+ "KTIDSDataURI: encoding with idsData: %@ ktResponse: %@"
+ "eventNotYetTransparent"
+ "kTransparencyStaticKeyStoreContactExternalURI"
+ "lastMilestoneFetch"
+ "lastRanFailures()"
+ "minimumIntervalSeconds"
+ "queryReason"
+ "swtransparencyd did not answer after %d attempts"
+ "sysdiagnoseInfo attempt %d hit %{public}@ %ld, retrying"
+ "sysdiagnoseInfo failed on attempt %d: %{public}@"
+ "sysdiagnoseInfo giving up after %d attempts"
+ "updateTreeResetInProgress: %{mask.hash}@ was computed with treeReset=%{BOOL}d, no tree reset is in progress now, uiStatus %{public}@ is stale"
+ "verifyExpiringProofs attempt %d hit %{public}@ %ld, retrying"
+ "verifyExpiringProofs failed on attempt %d: %{public}@"
+ "verifyExpiringProofs giving up after %d attempts"
+ "xpc connection invalidated, it will not reconnect: %{public}@"
+ "xpc peer exited, next call reopens: %{public}@"
+ "xpc peer exited: %{public}@ (%lu more suppressed at once)"
+ "xpc peer exited: %{public}@ (%lu more suppressed over %llums)"
- "<KTQueryOptions: flags: %08x>"
- "KTIDStaticKeyStoreEntryIdentifier"
- "TransparancyKTIDStaticKeyStoreEntry"
- "server connection exited or crashed: %@"
- "xpc connection cannot be formed or has been terminated: %@"
```
