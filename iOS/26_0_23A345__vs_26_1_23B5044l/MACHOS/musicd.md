## musicd

> `/System/Library/Frameworks/MusicKit.framework/Support/musicd`

```diff

-4025.110.2.0.0
-  __TEXT.__text: 0x1b788
-  __TEXT.__auth_stubs: 0xed0
+4025.200.12.0.0
+  __TEXT.__text: 0x1ccfc
+  __TEXT.__auth_stubs: 0xf10
   __TEXT.__objc_methlist: 0x104
   __TEXT.__const: 0x6ac
-  __TEXT.__cstring: 0x547
-  __TEXT.__constg_swiftt: 0x374
-  __TEXT.__swift5_typeref: 0x44f
-  __TEXT.__swift5_reflstr: 0x18c
-  __TEXT.__swift5_fieldmd: 0x198
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__oslogstring: 0x10ca
-  __TEXT.__swift5_capture: 0x1b4
-  __TEXT.__objc_methname: 0x2f3
+  __TEXT.__cstring: 0x517
+  __TEXT.__constg_swiftt: 0x36c
+  __TEXT.__swift5_typeref: 0x4ef
+  __TEXT.__swift5_reflstr: 0x19c
+  __TEXT.__swift5_fieldmd: 0x1a0
+  __TEXT.__oslogstring: 0x123a
+  __TEXT.__objc_methname: 0x3a7
+  __TEXT.__swift5_capture: 0x1c8
+  __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x98
   __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift5_types: 0x28
   __TEXT.__objc_classname: 0x47
   __TEXT.__objc_methtype: 0xad
-  __TEXT.__swift_as_entry: 0x44
-  __TEXT.__swift_as_ret: 0x5c
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x618
-  __TEXT.__eh_frame: 0xfe0
-  __DATA_CONST.__auth_got: 0x768
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__auth_ptr: 0x238
-  __DATA_CONST.__const: 0x740
+  __TEXT.__unwind_info: 0x6b8
+  __TEXT.__eh_frame: 0x11b8
+  __DATA_CONST.__auth_got: 0x788
+  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__auth_ptr: 0x230
+  __DATA_CONST.__const: 0x7c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA.__objc_const: 0x430
-  __DATA.__objc_selrefs: 0x130
+  __DATA.__objc_const: 0x450
+  __DATA.__objc_selrefs: 0x150
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x838
+  __DATA.__data: 0x890
   __DATA.__common: 0x48
   __DATA.__bss: 0x780
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A4C543ED-34B8-3A89-97F7-4BED66B84299
-  Functions: 592
-  Symbols:   413
-  CStrings:  168
+  UUID: 57B0216F-FDA6-32FA-A644-A294E47A0CB1
+  Functions: 624
+  Symbols:   420
+  CStrings:  176
 
Symbols:
+ _$s10Foundation4DateV19_bridgeToObjectiveCSo6NSDateCyF
+ _$s10Foundation4DateVACycfC
+ _$s10Foundation4DateVMa
+ _$s10Foundation4DateVs23CustomStringConvertibleAAMc
+ _$s10Foundation4UUIDV10uuidStringSSvg
+ _$s3XPC11XPCListenerC7service11targetQueue7options11requirement22incomingSessionHandlerACSS_So17OS_dispatch_queueCSgAC21InitializationOptionsVAA18XPCPeerRequirementVAC08IncomingI7RequestC8DecisionVAQctKcfC
+ _$s8MusicKit10UnfairLockC6lockedyxxyKXEKlF
+ _$s8MusicKit10UnfairLockCACycfc
+ _$s8MusicKit10UnfairLockCMa
+ _$s8MusicKit10UnfairLockCMn
+ _ML3TrackPropertyLikedStateChangedDate
+ _OBJC_CLASS_$_ICCloudContentTasteRequestListener
+ _OBJC_CLASS_$_ICConnectionConfiguration
+ _OBJC_CLASS_$_NSThread
+ _objc_release_x27
+ _objc_retain_x28
+ _swift_continuation_resume
+ _swift_weakAssign
- _$s16MusicKitInternal0A6DaemonV5ErrorO26failedToValidateAuditTokenyA2EmFWC
- _$s3XPC11XPCListenerC22IncomingSessionRequestC6reject6reasonAE8DecisionVSS_tFTj
- _$s3XPC11XPCListenerC22IncomingSessionRequestC9satisfies11requirementSbAA18XPCPeerRequirementV_tF
- _$s3XPC11XPCListenerC7service11targetQueue7options22incomingSessionHandlerACSS_So17OS_dispatch_queueCSgAC21InitializationOptionsVAC08IncomingH7RequestC8DecisionVANctKcfc
- _$s3XPC18XPCReceivedMessageV10auditTokenSo0D8_token_tavg
- _$ss6UInt32VMn
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retain_x23
- _objc_retain_x26
- _objc_retain_x27
CStrings:
+ " │   %{public}ld. %{public}s"
+ " │   thread: %s"
+ " ╭ Daemon server: %{public}ld active session(s):"
+ " ╰─"
+ "SELECT item_pid, subscription_store_item_id, store_item_id FROM item JOIN item_store USING (item_pid) WHERE "
+ "currentThread"
+ "initWithUserIdentity:"
+ "lock"
+ "server"
+ "setContentTaste:forMediaItem:storeIdentifier:persistentID:timeStamp:configuration:withCompletionHandler:"
+ "sharedCloudContentTasteRequestListener"
+ "| database row fetched with itemPersistentID: %{public}lld, storeID: %{public}lld."
+ "| failed to set values to entity with pid: %{public}lld."
+ "| setting content taste for storeID: %{public}lld, persistentID: %{public}lld, likedState: %{public}s"
+ "| successfully set content taste for entity with pid: %{public}lld and store ID: %{public}lld"
+ "| updating content taste for entity with pid: %{public}lld and store ID: %{public}lld to %{public}s."
+ "| updating liked_state_changed_date for entity with pid: %{public}lld to %{public}s."
- "Missing entitlement"
- "SELECT item_pid FROM item JOIN item_stats USING (item_pid) JOIN item_store USING (item_pid) WHERE "
- "activeSessions count: %ld."
- "failed to validate message audit token."
- "rejecting session request: missing entitlement."
- "validatedToken"
- "| database row fetched with itemPersistentID: %{public}lld."
- "| failed to update liked_state for entity with pid: %{public}lld."
- "| successfully updated the liked_state for entity with pid: %{public}lld."

```
