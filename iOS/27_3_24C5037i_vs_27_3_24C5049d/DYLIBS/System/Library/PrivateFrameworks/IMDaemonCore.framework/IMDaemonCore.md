## IMDaemonCore

> `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-1491.300.43.0.0
-  __TEXT.__text: 0x414f14
+1491.300.74.0.0
+  __TEXT.__text: 0x41768c
   __TEXT.__delay_stubs: 0x1c0
   __TEXT.__delay_helper: 0x1bc
-  __TEXT.__objc_methlist: 0x23164
-  __TEXT.__const: 0x9918
-  __TEXT.__cstring: 0x15c36
-  __TEXT.__gcc_except_tab: 0x22f78
-  __TEXT.__oslogstring: 0x5c0a2
+  __TEXT.__objc_methlist: 0x2319c
+  __TEXT.__const: 0x9998
+  __TEXT.__cstring: 0x15b86
+  __TEXT.__gcc_except_tab: 0x230d8
+  __TEXT.__oslogstring: 0x5c402
   __TEXT.__ustring: 0x32c
   __TEXT.__dlopen_cstrs: 0x1ee
-  __TEXT.__swift5_typeref: 0x47d4
+  __TEXT.__swift5_typeref: 0x47fa
   __TEXT.__constg_swiftt: 0x35c0
   __TEXT.__swift5_builtin: 0x244
   __TEXT.__swift5_reflstr: 0x1c5b

   __TEXT.__swift5_assocty: 0x820
   __TEXT.__swift5_proto: 0x4dc
   __TEXT.__swift5_types: 0x2ec
-  __TEXT.__swift5_capture: 0x23c4
+  __TEXT.__swift5_capture: 0x23e4
   __TEXT.__swift_as_entry: 0x4c4
-  __TEXT.__swift_as_ret: 0x58c
-  __TEXT.__swift_as_cont: 0xa24
+  __TEXT.__swift_as_ret: 0x590
+  __TEXT.__swift_as_cont: 0xa30
   __TEXT.__swift5_protos: 0x74
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x12e90
-  __TEXT.__eh_frame: 0xbda0
+  __TEXT.__unwind_info: 0x12f08
+  __TEXT.__eh_frame: 0xbeb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x74a0
+  __DATA_CONST.__const: 0x74d0
   __DATA_CONST.__objc_classlist: 0xd68
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0xc10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11a90
+  __DATA_CONST.__objc_selrefs: 0x11ac8
   __DATA_CONST.__objc_protorefs: 0x3a8
   __DATA_CONST.__objc_superrefs: 0x720
-  __DATA_CONST.__objc_arraydata: 0x1a8
-  __DATA_CONST.__got: 0x3d00
-  __AUTH_CONST.__const: 0xc480
-  __AUTH_CONST.__cfstring: 0xf440
-  __AUTH_CONST.__objc_const: 0x32e48
+  __DATA_CONST.__objc_arraydata: 0x190
+  __DATA_CONST.__got: 0x3d18
+  __AUTH_CONST.__const: 0xc488
+  __AUTH_CONST.__cfstring: 0xf420
+  __AUTH_CONST.__objc_const: 0x32e50
   __AUTH_CONST.__objc_intobj: 0xc48
-  __AUTH_CONST.__objc_arrayobj: 0x1f8
+  __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x3150
+  __AUTH_CONST.__auth_got: 0x3160
   __AUTH.__objc_data: 0x51f8
   __AUTH.__data: 0xa28
   __DATA.__objc_ivar: 0x1434
-  __DATA.__data: 0x88ec
+  __DATA.__data: 0x893c
   __DATA.__common: 0x178
   __DATA_DIRTY.__objc_data: 0x4278
-  __DATA_DIRTY.__data: 0x3840
+  __DATA_DIRTY.__data: 0x3880
   __DATA_DIRTY.__bss: 0x2af0
   __DATA_DIRTY.__common: 0x1f0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/IDSKVStore.framework/IDSKVStore
-  - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
   - /System/Library/PrivateFrameworks/IMCorePipeline.framework/IMCorePipeline
   - /System/Library/PrivateFrameworks/IMDMessageServices.framework/IMDMessageServices
   - /System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence

   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
-  - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /System/Library/PrivateFrameworks/ShareReporting.framework/ShareReporting

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17402
-  Symbols:   3522
-  CStrings:  9157
+  Functions: 17424
+  Symbols:   3525
+  CStrings:  9169
 
Symbols:
+ _IMTransferAgentErrorDomain
+ _IMTransferAgentErrorFZErrorTypeKey
+ _OBJC_CLASS_$_NPSDomainAccessor
+ _kNumberOfTimesRespondedToThreadKey
- _PSIsNanoMirroringDomain
CStrings:
+ "  => Could not mark message %@ as sending; not sending it out"
+ "BPSNanoBulletinShowsCustomSettings"
+ "Bailing, the GUID of message %@ is already used by an item of class %@"
+ "Incoming payload file missing or not written at %@, marking transfer %@ as failed"
+ "Not storing message %@: its GUID is already used by an item of class %@"
+ "PersistentTaskSchedulerExpirationGraceSeconds"
+ "Reloaded transfer %@ from the attachment store for accept, it has a CloudKit record"
+ "Storing new plugin message %{public}@ with no payload data (balloonBundleID %{public}@)"
+ "TelephonyServiceSession (%@): Acquisition failure for message %@; failing send."
+ "Translation is not supported, skipping outgoing translation."
+ "Updating autoDonationBehavior: %ld"
+ "[%{public}s] cancelled while loading tasks, leaving them queued to resume"
+ "[%{public}s] run did not unwind after DAS expiry; abandoning it so DAS is answered"
+ "[TEST] Simulating a 0-byte file for %s due to default force-empty-attachment-acquisition"
+ "com.apple.bulletinboard.apps"
+ "force-empty-attachment-acquisition"
+ "isMMSWithContentForSMSRelay"
- "*** If this is an internal group, please request logs from all participants! ***\n\nChats were found using the provided identifiers %@ and participants %@ that had no matching participants.\n\nChats Found: %@\n\nIdentifiers: %@"
- "Updating chatInfo with autoDonationBehavior: %ld"
- "[FindChat] Found Chat By Identifier With No Matching Participants"
- "[Internal] Chat Inconsistencies"
- "com.apple.MobileSMS.BestCandidateChatAlert"
```
