## seserviced

> `/usr/libexec/seserviced`

```diff

-64.20.2.0.0
-  __TEXT.__text: 0x4343a8
+64.22.0.0.0
+  __TEXT.__text: 0x437c98
   __TEXT.__auth_stubs: 0x4b70
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x33c
   __TEXT.__objc_stubs: 0xd5e0
-  __TEXT.__objc_methlist: 0x681c
-  __TEXT.__const: 0x119c8
-  __TEXT.__gcc_except_tab: 0x358c
-  __TEXT.__objc_methname: 0x1733b
-  __TEXT.__oslogstring: 0x2b690
-  __TEXT.__cstring: 0x1e539
-  __TEXT.__objc_classname: 0x2bca
-  __TEXT.__objc_methtype: 0x766f
-  __TEXT.__swift5_typeref: 0x4eb2
-  __TEXT.__constg_swiftt: 0x5164
-  __TEXT.__swift5_reflstr: 0x569a
-  __TEXT.__swift5_fieldmd: 0x5658
+  __TEXT.__objc_methlist: 0x6804
+  __TEXT.__const: 0x11a98
+  __TEXT.__gcc_except_tab: 0x346c
+  __TEXT.__objc_methname: 0x17359
+  __TEXT.__oslogstring: 0x2b7e0
+  __TEXT.__cstring: 0x1e5e9
+  __TEXT.__objc_classname: 0x2bba
+  __TEXT.__objc_methtype: 0x765f
+  __TEXT.__swift5_typeref: 0x4fd4
+  __TEXT.__constg_swiftt: 0x5198
+  __TEXT.__swift5_reflstr: 0x56ea
+  __TEXT.__swift5_fieldmd: 0x56bc
   __TEXT.__swift5_builtin: 0x348
   __TEXT.__swift5_assocty: 0x798
-  __TEXT.__swift5_capture: 0x248c
+  __TEXT.__swift5_capture: 0x2520
   __TEXT.__swift5_proto: 0x8d4
-  __TEXT.__swift5_types: 0x574
+  __TEXT.__swift5_types: 0x578
   __TEXT.__swift_as_entry: 0x398
-  __TEXT.__swift_as_ret: 0x53c
+  __TEXT.__swift_as_ret: 0x540
   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift5_mpenum: 0xa0
-  __TEXT.__unwind_info: 0x9cf8
-  __TEXT.__eh_frame: 0x12e84
+  __TEXT.__unwind_info: 0x9910
+  __TEXT.__eh_frame: 0x12f3c
   __DATA_CONST.__auth_got: 0x25d0
-  __DATA_CONST.__got: 0x1d48
+  __DATA_CONST.__got: 0x1d58
   __DATA_CONST.__auth_ptr: 0xe88
-  __DATA_CONST.__const: 0x124e8
+  __DATA_CONST.__const: 0x126a0
   __DATA_CONST.__cfstring: 0x7ec0
   __DATA_CONST.__objc_classlist: 0x7b0
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_intobj: 0x840
-  __DATA.__objc_const: 0x163e0
+  __DATA.__objc_const: 0x16468
   __DATA.__objc_selrefs: 0x4588
   __DATA.__objc_ivar: 0xb7c
-  __DATA.__objc_data: 0x6750
-  __DATA.__data: 0xc214
+  __DATA.__objc_data: 0x6758
+  __DATA.__data: 0xc244
   __DATA.__bss: 0xfd90
-  __DATA.__common: 0x718
+  __DATA.__common: 0x710
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftRegexBuilder.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5F0444E6-C7AF-375D-B065-D84E071E04FA
-  Functions: 11890
-  Symbols:   2366
-  CStrings:  11824
+  UUID: 6C22E07C-37E0-3F6F-8478-EAA99A1E10B0
+  Functions: 11920
+  Symbols:   2368
+  CStrings:  11837
 
Symbols:
+ _$sS2cEycfC
+ _$sScEs5ErrorsMc
+ __swift_FORCE_LOAD_$_swiftSpatial
- _$s8Dispatch0A3QoSV7utilityACvgZ
CStrings:
+ "/Library/Caches/com.apple.xbs/BFFB2279-F3E0-47A0-BD38-A44DAD2DFC5B/TemporaryDirectory.pT4o9R/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/BFFB2279-F3E0-47A0-BD38-A44DAD2DFC5B/TemporaryDirectory.pT4o9R/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "81d292e4-16d8-4630-82ed-bdf62b05e334"
+ "Cancelling cleanupTask as we are about to delete bad SP applets"
+ "Cleanup task was cancelled"
+ "Ended admin session after credential deletion"
+ "Ended admin session due to cleanup task cancellation"
+ "Ended admin session due to error %s"
+ "Error during admin delete: %s"
+ "Error during credential deletion: %s"
+ "FFFFFFFFFFFFFFFF"
+ "Failed to create endpoint in DB"
+ "No session provided and no error"
+ "Presenter deallocated"
+ "Request not found"
+ "Retries exhausted for fatal error"
+ "Retry %ld for fatal error"
+ "SECleanup preflight result: cleanup possible = %{bool}d"
+ "Skipping NFRemoteAdminManager cleanup - no cleanup possible"
+ "Started admin session %s"
+ "Unable to initialize shared client"
+ "Unable to initialize shared client for %s"
+ "biolockoutEventSent"
+ "c4f6386a-780d-40e5-9900-0a26c16273a1"
+ "cleanupState"
+ "clientConnection"
+ "com.apple.seserviced.default.app.change"
+ "com.apple.seserviced.spaceManagementClientQueue"
+ "endpointWithPublicKeyIdentifier:appletIdentifier:revocationAttestation:error:"
+ "iOS (26.4) - SecureElementService-64.22"
+ "launchRemoteConnection:"
+ "queueAdminSession()"
- "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "81D292E4-332F-481C-B7DE-7E80973B07BF"
- "C4F6386A-332F-481C-B7DE-7E80973B07BF"
- "Couldn't get entity for subjectIdentifier %@ : %@"
- "Ended admin session %s"
- "Error %s encountered when deleting credential"
- "Error %s while deleting credentials %s"
- "Failed to create revoked endpoint"
- "Finished deleting all orphaned credentials"
- "Found %u CAs in the DB not present on SE"
- "Removing dangling DB CA %@ with %u endpoints "
- "Start admin session %s"
- "T@\"BSServiceConnection<BSServiceConnectionClient>\",&,N,V_connection"
- "Unable to construct admin session"
- "While listing CA subject ids (DB) in %@"
- "com.apple.seserviced.invalidation"
- "iOS (26.4) - SecureElementService-64.20.2"
- "launchRemote"
- "revokedEndpointWithPublicKeyIdentifier:appletIdentifier:revocationAttestation:error:"

```
