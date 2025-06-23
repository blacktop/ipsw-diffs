## cryptexd

> `/usr/libexec/cryptexd`

```diff

-589.0.1.0.0
-  __TEXT.__text: 0x4b7e8
-  __TEXT.__auth_stubs: 0x1d30
-  __TEXT.__objc_stubs: 0x1620
-  __TEXT.__objc_methlist: 0x844
-  __TEXT.__const: 0x9d8
-  __TEXT.__gcc_except_tab: 0x18e0
-  __TEXT.__objc_methname: 0x1649
-  __TEXT.__objc_classname: 0xf9
-  __TEXT.__objc_methtype: 0x3c9
-  __TEXT.__cstring: 0x34f6
-  __TEXT.__oslogstring: 0x9c7c
-  __TEXT.__unwind_info: 0xbb0
-  __DATA_CONST.__auth_got: 0xea8
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x2a50
+589.0.9.0.0
+  __TEXT.__text: 0x52010
+  __TEXT.__auth_stubs: 0x20c0
+  __TEXT.__objc_stubs: 0x16c0
+  __TEXT.__objc_methlist: 0x994
+  __TEXT.__const: 0xa88
+  __TEXT.__gcc_except_tab: 0x1c14
+  __TEXT.__objc_methname: 0x17d5
+  __TEXT.__objc_classname: 0x110
+  __TEXT.__objc_methtype: 0x45e
+  __TEXT.__cstring: 0x3da1
+  __TEXT.__oslogstring: 0xa0fd
+  __TEXT.__swift5_typeref: 0x98
+  __TEXT.__constg_swiftt: 0x58
+  __TEXT.__swift5_reflstr: 0x7
+  __TEXT.__swift5_fieldmd: 0x1c
+  __TEXT.__swift5_capture: 0x88
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__unwind_info: 0xd50
+  __TEXT.__eh_frame: 0x268
+  __DATA_CONST.__auth_got: 0x1070
+  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__auth_ptr: 0x40
+  __DATA_CONST.__const: 0x3690
   __DATA_CONST.__cfstring: 0x280
-  __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_nlclslist: 0x40
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__subsystem: 0x18
   __DATA_CONST.__object_init: 0x8
-  __DATA.__objc_const: 0x1350
-  __DATA.__objc_selrefs: 0x600
+  __DATA.__objc_const: 0x14c0
+  __DATA.__objc_selrefs: 0x6b0
   __DATA.__objc_ivar: 0xb8
-  __DATA.__objc_data: 0x5a0
-  __DATA.__data: 0x430
-  __DATA.__bss: 0x528
+  __DATA.__objc_data: 0x670
+  __DATA.__data: 0x540
+  __DATA.__bss: 0x560
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
+  - /System/Library/PrivateFrameworks/CryptexKit.framework/CryptexKit
+  - /System/Library/PrivateFrameworks/CryptexServer.framework/CryptexServer
   - /System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery

   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: BB56F214-168F-30FF-AA9C-EB5DB84CBD40
-  Functions: 899
-  Symbols:   564
-  CStrings:  1797
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSystem.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 86ACAC70-5A18-3D17-8525-8637C71B3550
+  Functions: 1040
+  Symbols:   6581
+  CStrings:  1965
 
Symbols:
+ 
+ $sIeAgH_ytIeAgHr_TRTA.34
+ $sIeAgH_ytIeAgHr_TRTA.34TQ0_
+ $sIeAgH_ytIeAgHr_TRTA.34Tu
+ $sIeghH_IeAgH_TRTA.29
+ $sIeghH_IeAgH_TRTA.29TQ0_
+ $sIeghH_IeAgH_TRTA.29Tu
+ +[CollationMap addEntryForUser:fromQuire:]
+ +[CollationMap createCollationForUser:]
+ +[CollationMap getMap]
+ +[CollationMap lookupEntryForUser:withBundleID:minVersion:]
+ +[CollationMap removeEntryForUser:withValue:]
+ +[CryptexSessionList createCryptexSessionList]
+ +[CryptexSessionList sharedList]
+ +[CryptexSessionList sharedList].cold.1
+ +[SandboxManager getManager]
+ +[UpgradeSequencer getSharedInstance]
+ +[UpgradeSequencer getSharedInstance].cold.1
+ -[CollationMap .cxx_destruct]
+ -[CollationMap coll_map]
+ -[CollationMap dq]
+ -[CollationMap init]
+ -[CollationMap init].cold.1
+ -[CollationMap log]
+ -[CollationMap setColl_map:]
+ -[CollationMap setDq:]
+ -[CollationMap setLog:]
+ -[CryptexPathMap .cxx_destruct]
+ -[CryptexPathMap dict]
+ -[CryptexPathMap init]
+ -[CryptexSession .cxx_destruct]
+ -[CryptexSession activate]
+ -[CryptexSession cancelPeerConnections]
+ -[CryptexSession copySessionName]
+ -[CryptexSession cs]
+ -[CryptexSession dq]
+ -[CryptexSession error]
+ -[CryptexSession exit_code]
+ -[CryptexSession getDispatchQueue]
+ -[CryptexSession initWithCore:]
+ -[CryptexSession listener]
+ -[CryptexSession log]
+ -[CryptexSession name]
+ -[CryptexSession parseCommandFromMessage:fromPeer:]
+ -[CryptexSession parseCommandFromMessage:fromPeer:].cold.1
+ -[CryptexSession parseCommandFromMessage:fromPeer:].cold.2
+ -[CryptexSession peer_array]
+ -[CryptexSession quire_array]
+ -[CryptexSession sessionAddCptxWithBundleID:withType:dmgFd:trustCacheFD:manifestFD:volumeHashFD:infoPlistFd:cx1Properties:]
+ -[CryptexSession sessionAddParseXPC:]
+ -[CryptexSession sessionEventNotify:]
+ -[CryptexSession sessionMessageReply:]
+ -[CryptexSession sessionMessageReply:].cold.1
+ -[CryptexSession sessionStart]
+ -[CryptexSession sessionStopWithReason:exitCode:]
+ -[CryptexSession session_removal_begun]
+ -[CryptexSession session_work_group]
+ -[CryptexSession setCs:]
+ -[CryptexSession setDq:]
+ -[CryptexSession setError:]
+ -[CryptexSession setExitReason:withCode:]
+ -[CryptexSession setExit_code:]
+ -[CryptexSession setListener:]
+ -[CryptexSession setLog:]
+ -[CryptexSession setName:]
+ -[CryptexSession setPeer_array:]
+ -[CryptexSession setQuire_array:]
+ -[CryptexSession setSession_removal_begun:]
+ -[CryptexSession setSession_work_group:]
+ -[CryptexSession setStop_reason:]
+ -[CryptexSession setupHandler]
+ -[CryptexSession stop_reason]
+ -[CryptexSessionList .cxx_destruct]
+ -[CryptexSessionList addCryptexSession:]
+ -[CryptexSessionList findCryptexSession:]
+ -[CryptexSessionList list]
+ -[CryptexSessionList log_handle]
+ -[CryptexSessionList removeCryptexSession:]
+ -[CryptexSessionList setList:]
+ -[CryptexSessionList setLog_handle:]
+ -[CryptexSessionList shutdownSession:reason:exitCode:]
+ -[EventClient .cxx_destruct]
+ -[EventClient clientName]
+ -[EventClient eventMask]
+ -[EventClient initWithToken:name:eventMask:]
+ -[EventClient token]
+ -[EventServer .cxx_destruct]
+ -[EventServer activate]
+ -[EventServer broadcastEvent:forCryptex:withInfo:]
+ -[EventServer broadcastEvent:forCryptex:withInfo:toClients:]
+ -[EventServer clients]
+ -[EventServer handlePublisherAddToken:descriptor:]
+ -[EventServer handlePublisherError:]
+ -[EventServer handlePublisherInitialBarrier]
+ -[EventServer handlePublisherRemoveToken:]
+ -[EventServer initWithEventStream:]
+ -[EventServer log]
+ -[EventServer publisher]
+ -[EventServer sendAlreadyInstalledCryptexesToClient:]
+ -[EventServer withInstalledCryptexList:]
+ -[OS_codex dealloc]
+ -[OS_cryptex_base dealloc]
+ -[OS_daemon dealloc]
+ -[OS_proc dealloc]
+ -[OS_protex dealloc]
+ -[OS_quire dealloc]
+ -[OS_resource dealloc]
+ -[OS_view dealloc]
+ -[SandboxManager .cxx_destruct]
+ -[SandboxManager init]
+ -[SandboxManager init].cold.1
+ -[SandboxManager log_handle]
+ -[SandboxManager sandboxHandles]
+ -[SandboxManager setLog_handle:]
+ -[SandboxManager setSandboxHandles:]
+ -[UpgradeClient .cxx_destruct]
+ -[UpgradeClient _handleInterfaceLockMessage:]
+ -[UpgradeClient activate]
+ -[UpgradeClient cancelHandler]
+ -[UpgradeClient conn]
+ -[UpgradeClient cred]
+ -[UpgradeClient dealloc]
+ -[UpgradeClient initWithConn:log:]
+ -[UpgradeClient initWithConn:log:].cold.1
+ -[UpgradeClient logHandle]
+ -[UpgradeClient onCancel:]
+ -[UpgradeClient transaction]
+ -[UpgradeOperation .cxx_destruct]
+ -[UpgradeOperation completeUpgrade]
+ -[UpgradeOperation cryptexName]
+ -[UpgradeOperation error]
+ -[UpgradeOperation graftPath]
+ -[UpgradeOperation group]
+ -[UpgradeOperation initWithCryptexName:graftPath:]
+ -[UpgradeOperation logHandle]
+ -[UpgradeOperation onComplete:withQueue:]
+ -[UpgradeOperation setError:]
+ -[UpgradeOperation startUpgrade]
+ -[UpgradeOperation terminateJobsWithCompletion:]
+ -[UpgradeOperation workQueue]
+ -[UpgradeSequencer .cxx_destruct]
+ -[UpgradeSequencer _abort]
+ -[UpgradeSequencer _completeUpgradeSession]
+ -[UpgradeSequencer _completeUpgradeWithError:]
+ -[UpgradeSequencer _disableInterfaceLockTimeout]
+ -[UpgradeSequencer _handleInterfaceLockCancel]
+ -[UpgradeSequencer _isInterfaceLocked]
+ -[UpgradeSequencer _restartInterfaceLockTimeout]
+ -[UpgradeSequencer _setKernelUpgradeOngoing:]
+ -[UpgradeSequencer _startUpgradeForCryptex:withGraftPath:killingJobs:withCompletion:]
+ -[UpgradeSequencer _timeout]
+ -[UpgradeSequencer _unlockInterface]
+ -[UpgradeSequencer abortWithCompletion:]
+ -[UpgradeSequencer completeUpgradeWithCompletion:]
+ -[UpgradeSequencer init]
+ -[UpgradeSequencer lockAcquireQueue]
+ -[UpgradeSequencer lockInterfaceForClient:withCompletion:]
+ -[UpgradeSequencer lockIsHeldByClient:]
+ -[UpgradeSequencer lockTimer]
+ -[UpgradeSequencer lockingClient]
+ -[UpgradeSequencer logHandle]
+ -[UpgradeSequencer onUpgradeCompleteForCryptex:withCompletion:]
+ -[UpgradeSequencer onUpgradeSessionComplete:]
+ -[UpgradeSequencer registrationQueue]
+ -[UpgradeSequencer sessionCompleteCallback]
+ -[UpgradeSequencer setLockTimer:]
+ -[UpgradeSequencer setLockingClient:]
+ -[UpgradeSequencer setSessionCompleteCallback:]
+ -[UpgradeSequencer startUpgradeForCryptexes:killingJobs:withCompletion:]
+ -[UpgradeSequencer upgradesUnderway]
+ -[UpgradeSequencer workQueue]
+ /AppleInternal/Library/BuildRoots/4~B3CyugCD4u_BvzkhBcktw-ZufrZdMEQydYPLyO8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/dyld/libamfi.a(libamfi.o)
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex.build/cryptexd.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex.build/cryptexd.build/DerivedSources/arm64e/normal/
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/InventoryXPC.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/aks.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/amfi.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/apfs.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/authinstall.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/bin_trampoline.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/cf-316a06a69bc7d03e2939bfafee35da15.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/codex.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/collation_map.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/cryptexd.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/cryptexd.swiftmodule
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/cryptexd_objc.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/cryptexd_vers.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/daemon.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/darwin_version.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/devmode_sysctl.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/dyld_shared_region.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/event_server.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/fs.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/hdi-0e07362251748ee0c7cba088b5a1274e.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/img4.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/img4_xpc.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/inventory_xpc.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/iokit.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/launch_util.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/launchd_session.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/path.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/proc.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/protex.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/python.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/quire.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/resource.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/restricted_exec_mode_sysctl.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sandboxing.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/session.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sm.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sub.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sub_codex.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sub_codex_xpc.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sub_collation.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sub_daemon.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sub_endpoint_lookup.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sub_mount.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sub_pipeline.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sub_remote_service.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sub_session.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sub_upgrade_lock.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/sub_upgrade_trampoline.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/upgrade_sequencer.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/upgrade_sysctl.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/usermanager.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/view.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/watchdog.o
+ /Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/TempContent/Objects/libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E/xpc_entitlements.o
+ /Library/Caches/com.apple.xbs/Sources/AppleMobileFileIntegrity_libs/libamfi/
+ /Library/Caches/com.apple.xbs/Sources/libcryptex_executables/cryptexd/
+ /Library/Caches/com.apple.xbs/Sources/libcryptex_executables/cryptexd/sm/
+ /Library/Caches/com.apple.xbs/Sources/libcryptex_executables/cryptexd/sub/
+ /Library/Caches/com.apple.xbs/Sources/libcryptex_executables/hlutil/
+ GCC_except_table0
+ GCC_except_table1
+ GCC_except_table11
+ GCC_except_table14
+ GCC_except_table15
+ GCC_except_table16
+ GCC_except_table18
+ GCC_except_table19
+ GCC_except_table2
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table23
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table3
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table4
+ GCC_except_table46
+ GCC_except_table5
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table59
+ GCC_except_table6
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table7
+ GCC_except_table71
+ GCC_except_table8
+ GCC_except_table9
+ InventoryXPC.swift
+ OBJC_IVAR_$_CollationMap._coll_map
+ OBJC_IVAR_$_CollationMap._dq
+ OBJC_IVAR_$_CollationMap._log
+ OBJC_IVAR_$_CryptexPathMap._dict
+ OBJC_IVAR_$_CryptexSession._cs
+ OBJC_IVAR_$_CryptexSession._dq
+ OBJC_IVAR_$_CryptexSession._error
+ OBJC_IVAR_$_CryptexSession._exit_code
+ OBJC_IVAR_$_CryptexSession._listener
+ OBJC_IVAR_$_CryptexSession._log
+ OBJC_IVAR_$_CryptexSession._name
+ OBJC_IVAR_$_CryptexSession._peer_array
+ OBJC_IVAR_$_CryptexSession._quire_array
+ OBJC_IVAR_$_CryptexSession._session_removal_begun
+ OBJC_IVAR_$_CryptexSession._session_work_group
+ OBJC_IVAR_$_CryptexSession._stop_reason
+ OBJC_IVAR_$_CryptexSessionList._list
+ OBJC_IVAR_$_CryptexSessionList._log_handle
+ OBJC_IVAR_$_CryptexSessionList.rw_lock
+ OBJC_IVAR_$_EventClient._clientName
+ OBJC_IVAR_$_EventClient._eventMask
+ OBJC_IVAR_$_EventClient._token
+ OBJC_IVAR_$_EventServer._clients
+ OBJC_IVAR_$_EventServer._log
+ OBJC_IVAR_$_EventServer._publisher
+ OBJC_IVAR_$_SandboxManager._log_handle
+ OBJC_IVAR_$_SandboxManager._sandboxHandles
+ OBJC_IVAR_$_UpgradeClient._cancelHandler
+ OBJC_IVAR_$_UpgradeClient._conn
+ OBJC_IVAR_$_UpgradeClient._cred
+ OBJC_IVAR_$_UpgradeClient._logHandle
+ OBJC_IVAR_$_UpgradeClient._transaction
+ OBJC_IVAR_$_UpgradeOperation._cryptexName
+ OBJC_IVAR_$_UpgradeOperation._error
+ OBJC_IVAR_$_UpgradeOperation._graftPath
+ OBJC_IVAR_$_UpgradeOperation._group
+ OBJC_IVAR_$_UpgradeOperation._logHandle
+ OBJC_IVAR_$_UpgradeOperation._workQueue
+ OBJC_IVAR_$_UpgradeSequencer._lockAcquireQueue
+ OBJC_IVAR_$_UpgradeSequencer._lockTimer
+ OBJC_IVAR_$_UpgradeSequencer._lockingClient
+ OBJC_IVAR_$_UpgradeSequencer._logHandle
+ OBJC_IVAR_$_UpgradeSequencer._registrationQueue
+ OBJC_IVAR_$_UpgradeSequencer._sessionCompleteCallback
+ OBJC_IVAR_$_UpgradeSequencer._upgradesUnderway
+ OBJC_IVAR_$_UpgradeSequencer._workQueue
+ _$s10CryptexKit10Image4AuthVAA26AssetAuthenticatorProtocolAAWP
+ _$s10CryptexKit10Image4AuthVACycfC
+ _$s10CryptexKit10Image4AuthVMa
+ _$s10CryptexKit14SendableXPCObjC5valueSo13OS_xpc_object_pvg
+ _$s10Foundation22_convertErrorToNSErrorySo0E0Cs0C0_pF
+ _$s13CryptexServer0B0C14createEndpoint0A3Kit14SendableXPCObjCyYaFTjTu
+ _$s13CryptexServer0B0C15createAnonymous5queue19persistentInventory09ephemeralG0ACXDSo012OS_dispatch_E7_serialC_AA0G0CSgALtKFZ
+ _$s13CryptexServer0B0C5startyyYaKFTjTu
+ _$s13CryptexServer0B0CMa
+ _$s13CryptexServer0B0CMn
+ _$s13CryptexServer16VirtualEnvConfigVMa
+ _$s13CryptexServer16VirtualEnvConfigVMn
+ _$s13CryptexServer16VirtualEnvConfigVSgMD
+ _$s13CryptexServer9InventoryC4name16runtimeDirectory14cryptexStorage13authenticator10venvConfigACSS_6System8FilePathVAKSg0A3Kit26AssetAuthenticatorProtocol_pAA010VirtualEnvK0VSgtKcfC
+ _$s13CryptexServer9InventoryCMa
+ _$s6System8FilePathVMa
+ _$s6System8FilePathVMn
+ _$s6System8FilePathVSgMD
+ _$s6System8FilePathVyACSScfC
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKF
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFTQ1_
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFTY0_
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFTY2_
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFTo
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFTq
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFTu
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFyyYacfU_To
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFyyYacfU_ToTA
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFyyYacfU_ToTATQ0_
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFyyYacfU_ToTATu
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFyyYacfU_ToTQ1_
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFyyYacfU_ToTY0_
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFyyYacfU_ToTY2_
+ _$s8cryptexd12InventoryXPCC14createEndpointSo13OS_xpc_object_pyYaKFyyYacfU_ToTu
+ _$s8cryptexd12InventoryXPCC5queueACSo012OS_dispatch_D7_serialC_tKcfC
+ _$s8cryptexd12InventoryXPCC5queueACSo012OS_dispatch_D7_serialC_tKcfCTq
+ _$s8cryptexd12InventoryXPCC5queueACSo012OS_dispatch_D7_serialC_tKcfc
+ _$s8cryptexd12InventoryXPCC5queueACSo012OS_dispatch_D7_serialC_tKcfcTo
+ _$s8cryptexd12InventoryXPCC5startyyYaKF
+ _$s8cryptexd12InventoryXPCC5startyyYaKFTQ1_
+ _$s8cryptexd12InventoryXPCC5startyyYaKFTY0_
+ _$s8cryptexd12InventoryXPCC5startyyYaKFTo
+ _$s8cryptexd12InventoryXPCC5startyyYaKFTq
+ _$s8cryptexd12InventoryXPCC5startyyYaKFTu
+ _$s8cryptexd12InventoryXPCC5startyyYaKFyyYacfU_To
+ _$s8cryptexd12InventoryXPCC5startyyYaKFyyYacfU_ToTA
+ _$s8cryptexd12InventoryXPCC5startyyYaKFyyYacfU_ToTATQ0_
+ _$s8cryptexd12InventoryXPCC5startyyYaKFyyYacfU_ToTATu
+ _$s8cryptexd12InventoryXPCC5startyyYaKFyyYacfU_ToTQ1_
+ _$s8cryptexd12InventoryXPCC5startyyYaKFyyYacfU_ToTY0_
+ _$s8cryptexd12InventoryXPCC5startyyYaKFyyYacfU_ToTY2_
+ _$s8cryptexd12InventoryXPCC5startyyYaKFyyYacfU_ToTu
+ _$s8cryptexd12InventoryXPCC6server13CryptexServer0F0Cvg
+ _$s8cryptexd12InventoryXPCC6server13CryptexServer0F0CvpMV
+ _$s8cryptexd12InventoryXPCC6server13CryptexServer0F0CvpWvd
+ _$s8cryptexd12InventoryXPCCACycfC
+ _$s8cryptexd12InventoryXPCCACycfc
+ _$s8cryptexd12InventoryXPCCACycfcTo
+ _$s8cryptexd12InventoryXPCCMF
+ _$s8cryptexd12InventoryXPCCMa
+ _$s8cryptexd12InventoryXPCCMf
+ _$s8cryptexd12InventoryXPCCMn
+ _$s8cryptexd12InventoryXPCCN
+ _$s8cryptexd12InventoryXPCCfD
+ _$s8cryptexd12InventoryXPCCfETo
+ _$s8cryptexdMXM
+ _$sBOWV
+ _$sIeAgH_ytIeAgHr_TR
+ _$sIeAgH_ytIeAgHr_TRTA
+ _$sIeAgH_ytIeAgHr_TRTATQ0_
+ _$sIeAgH_ytIeAgHr_TRTATu
+ _$sIeAgH_ytIeAgHr_TRTQ0_
+ _$sIeAgH_ytIeAgHr_TRTu
+ _$sIeghH_IeAgH_TR
+ _$sIeghH_IeAgH_TRTA
+ _$sIeghH_IeAgH_TRTATQ0_
+ _$sIeghH_IeAgH_TRTATu
+ _$sIeghH_IeAgH_TRTQ0_
+ _$sIeghH_IeAgH_TRTu
+ _$sScA15unownedExecutorScevgTj
+ _$sScP8rawValues5UInt8Vvg
+ _$sScPMa
+ _$sScPSgMD
+ _$sScPSgWOh
+ _$sScTss5NeverORs_rlE8priority9operationScTyxABGScPSg_xyYaYAcntcfCyt_Tt1gq5
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TATQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TATu
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5Tu
+ _$sytN
+ _CFCreateAssertImpl.cold.1
+ _CFNumberGetUInt32.cold.1
+ _CFNumberGetUInt32.cold.2
+ _CFStringCopyUTF8String.cold.1
+ _CFStringGetUTF8String.cold.1
+ _DERDecodeItem
+ _DERDecodeItemPartialBufferGetLength
+ _DERDecodeSeqNext
+ _DERImg4CompressionItemSpecs
+ _DERImg4Decode
+ _DERImg4DecodeManifest
+ _DERImg4DecodeManifestCommon
+ _DERImg4DecodePayload
+ _DERImg4DecodePayloadCompression
+ _DERImg4DecodePayloadProperties
+ _DERImg4DecodePayloadWithProperties
+ _DERImg4DecodeRestoreInfo
+ _DERImg4DecodeTagCompare
+ _DERImg4ItemSpecs
+ _DERImg4ManifestItemSpecs
+ _DERImg4PayloadItemSpecs
+ _DERImg4PayloadPropertiesItemSpecs
+ _DERImg4PayloadWithPropertiesItemSpecs
+ _DERImg4RestoreInfoItemSpecs
+ _DERParseInteger
+ _DERParseInteger64
+ _DERParseSequenceContentToObject
+ _DERParseSequenceToObject
+ _Img4DecodeInit
+ _Img4DecodeInitPayload
+ _OBJC_CLASS_$_CollationMap
+ _OBJC_CLASS_$_CryptexPathMap
+ _OBJC_CLASS_$_CryptexSession
+ _OBJC_CLASS_$_CryptexSessionList
+ _OBJC_CLASS_$_EventClient
+ _OBJC_CLASS_$_EventServer
+ _OBJC_CLASS_$_OS_codex
+ _OBJC_CLASS_$_OS_cryptex_base
+ _OBJC_CLASS_$_OS_daemon
+ _OBJC_CLASS_$_OS_proc
+ _OBJC_CLASS_$_OS_protex
+ _OBJC_CLASS_$_OS_quire
+ _OBJC_CLASS_$_OS_resource
+ _OBJC_CLASS_$_OS_view
+ _OBJC_CLASS_$_SandboxManager
+ _OBJC_CLASS_$_UpgradeClient
+ _OBJC_CLASS_$_UpgradeOperation
+ _OBJC_CLASS_$_UpgradeSequencer
+ _OBJC_CLASS_$__TtC8cryptexd12InventoryXPC
+ _OBJC_METACLASS_$_CollationMap
+ _OBJC_METACLASS_$_CryptexPathMap
+ _OBJC_METACLASS_$_CryptexSession
+ _OBJC_METACLASS_$_CryptexSessionList
+ _OBJC_METACLASS_$_EventClient
+ _OBJC_METACLASS_$_EventServer
+ _OBJC_METACLASS_$_OS_codex
+ _OBJC_METACLASS_$_OS_cryptex_base
+ _OBJC_METACLASS_$_OS_daemon
+ _OBJC_METACLASS_$_OS_proc
+ _OBJC_METACLASS_$_OS_protex
+ _OBJC_METACLASS_$_OS_quire
+ _OBJC_METACLASS_$_OS_resource
+ _OBJC_METACLASS_$_OS_view
+ _OBJC_METACLASS_$_SandboxManager
+ _OBJC_METACLASS_$_UpgradeClient
+ _OBJC_METACLASS_$_UpgradeOperation
+ _OBJC_METACLASS_$_UpgradeSequencer
+ _OBJC_METACLASS_$__TtC8cryptexd12InventoryXPC
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _TCTypeConfig
+ __22+[CollationMap getMap]_block_invoke.cold.1
+ __28+[SandboxManager getManager]_block_invoke.cold.1
+ __30-[CryptexSession setupHandler]_block_invoke.16
+ __35-[EventServer initWithEventStream:]_block_invoke.27
+ __37-[CryptexSession sessionAddParseXPC:]_block_invoke.cold.1
+ __37-[CryptexSession sessionAddParseXPC:]_block_invoke.cold.2
+ __37-[CryptexSession sessionAddParseXPC:]_block_invoke.cold.3
+ __37-[CryptexSession sessionAddParseXPC:]_block_invoke.cold.4
+ __37-[CryptexSession sessionAddParseXPC:]_block_invoke.cold.5
+ __39+[CollationMap createCollationForUser:]_block_invoke.8
+ __42+[CollationMap addEntryForUser:fromQuire:]_block_invoke.cold.1
+ __45+[CollationMap removeEntryForUser:withValue:]_block_invoke.cold.1
+ __45+[CollationMap removeEntryForUser:withValue:]_block_invoke.cold.2
+ __45+[CollationMap removeEntryForUser:withValue:]_block_invoke.cold.3
+ __45+[CollationMap removeEntryForUser:withValue:]_block_invoke.cold.4
+ __59+[CollationMap lookupEntryForUser:withBundleID:minVersion:]_block_invoke_2.cold.1
+ __72-[UpgradeSequencer startUpgradeForCryptexes:killingJobs:withCompletion:]_block_invoke.110
+ __72-[UpgradeSequencer startUpgradeForCryptexes:killingJobs:withCompletion:]_block_invoke_2.108
+ __AMAuthInstallSetCryptex1ApParamsFromHost
+ __Block_byref_object_copy_.30
+ __Block_byref_object_dispose_.31
+ __Block_copy
+ __Block_release
+ __CFCreateAssertImpl
+ __CFDictionaryCreateMutableForCFTypes
+ __CFDictionarySetBool
+ __CFDictionarySetString
+ __CFDictionarySetUInt32
+ __CFErrorCopyTopLevelErrorWithDomain
+ __CFErrorGetTopLevelPosixError
+ __CFErrorHasDomainAndCode
+ __CFErrorIterUnderlying
+ __CFNumberCreateFromInt32
+ __CFNumberGetUInt32
+ __CFStringCopyUTF8String
+ __CFStringCreateFromUTF8String
+ __CFStringGetUTF8String
+ __CFURLCreateFromFileDescriptor
+ __DATA__TtC8cryptexd12InventoryXPC
+ __INSTANCE_METHODS__TtC8cryptexd12InventoryXPC
+ __IOErrorGetErrno
+ __IORegistryExchangeWithFirstChildOfClass
+ __IVARS__TtC8cryptexd12InventoryXPC
+ __METACLASS_DATA__TtC8cryptexd12InventoryXPC
+ __OBJC_$_CLASS_METHODS_CollationMap
+ __OBJC_$_CLASS_METHODS_CryptexSessionList
+ __OBJC_$_CLASS_METHODS_SandboxManager
+ __OBJC_$_CLASS_METHODS_UpgradeSequencer
+ __OBJC_$_INSTANCE_METHODS_CollationMap
+ __OBJC_$_INSTANCE_METHODS_CryptexPathMap
+ __OBJC_$_INSTANCE_METHODS_CryptexSession
+ __OBJC_$_INSTANCE_METHODS_CryptexSessionList
+ __OBJC_$_INSTANCE_METHODS_EventClient
+ __OBJC_$_INSTANCE_METHODS_EventServer
+ __OBJC_$_INSTANCE_METHODS_OS_codex
+ __OBJC_$_INSTANCE_METHODS_OS_cryptex_base
+ __OBJC_$_INSTANCE_METHODS_OS_daemon
+ __OBJC_$_INSTANCE_METHODS_OS_proc
+ __OBJC_$_INSTANCE_METHODS_OS_protex
+ __OBJC_$_INSTANCE_METHODS_OS_quire
+ __OBJC_$_INSTANCE_METHODS_OS_resource
+ __OBJC_$_INSTANCE_METHODS_OS_view
+ __OBJC_$_INSTANCE_METHODS_SandboxManager
+ __OBJC_$_INSTANCE_METHODS_UpgradeClient
+ __OBJC_$_INSTANCE_METHODS_UpgradeOperation
+ __OBJC_$_INSTANCE_METHODS_UpgradeSequencer
+ __OBJC_$_INSTANCE_VARIABLES_CollationMap
+ __OBJC_$_INSTANCE_VARIABLES_CryptexPathMap
+ __OBJC_$_INSTANCE_VARIABLES_CryptexSession
+ __OBJC_$_INSTANCE_VARIABLES_CryptexSessionList
+ __OBJC_$_INSTANCE_VARIABLES_EventClient
+ __OBJC_$_INSTANCE_VARIABLES_EventServer
+ __OBJC_$_INSTANCE_VARIABLES_SandboxManager
+ __OBJC_$_INSTANCE_VARIABLES_UpgradeClient
+ __OBJC_$_INSTANCE_VARIABLES_UpgradeOperation
+ __OBJC_$_INSTANCE_VARIABLES_UpgradeSequencer
+ __OBJC_$_PROP_LIST_CollationMap
+ __OBJC_$_PROP_LIST_CryptexPathMap
+ __OBJC_$_PROP_LIST_CryptexSession
+ __OBJC_$_PROP_LIST_CryptexSessionList
+ __OBJC_$_PROP_LIST_EventClient
+ __OBJC_$_PROP_LIST_EventServer
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_SandboxManager
+ __OBJC_$_PROP_LIST_UpgradeClient
+ __OBJC_$_PROP_LIST_UpgradeOperation
+ __OBJC_$_PROP_LIST_UpgradeSequencer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_OS_xpc_object
+ __OBJC_CLASS_RO_$_CollationMap
+ __OBJC_CLASS_RO_$_CryptexPathMap
+ __OBJC_CLASS_RO_$_CryptexSession
+ __OBJC_CLASS_RO_$_CryptexSessionList
+ __OBJC_CLASS_RO_$_EventClient
+ __OBJC_CLASS_RO_$_EventServer
+ __OBJC_CLASS_RO_$_OS_codex
+ __OBJC_CLASS_RO_$_OS_cryptex_base
+ __OBJC_CLASS_RO_$_OS_daemon
+ __OBJC_CLASS_RO_$_OS_proc
+ __OBJC_CLASS_RO_$_OS_protex
+ __OBJC_CLASS_RO_$_OS_quire
+ __OBJC_CLASS_RO_$_OS_resource
+ __OBJC_CLASS_RO_$_OS_view
+ __OBJC_CLASS_RO_$_SandboxManager
+ __OBJC_CLASS_RO_$_UpgradeClient
+ __OBJC_CLASS_RO_$_UpgradeOperation
+ __OBJC_CLASS_RO_$_UpgradeSequencer
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_OS_xpc_object
+ __OBJC_METACLASS_RO_$_CollationMap
+ __OBJC_METACLASS_RO_$_CryptexPathMap
+ __OBJC_METACLASS_RO_$_CryptexSession
+ __OBJC_METACLASS_RO_$_CryptexSessionList
+ __OBJC_METACLASS_RO_$_EventClient
+ __OBJC_METACLASS_RO_$_EventServer
+ __OBJC_METACLASS_RO_$_OS_codex
+ __OBJC_METACLASS_RO_$_OS_cryptex_base
+ __OBJC_METACLASS_RO_$_OS_daemon
+ __OBJC_METACLASS_RO_$_OS_proc
+ __OBJC_METACLASS_RO_$_OS_protex
+ __OBJC_METACLASS_RO_$_OS_quire
+ __OBJC_METACLASS_RO_$_OS_resource
+ __OBJC_METACLASS_RO_$_OS_view
+ __OBJC_METACLASS_RO_$_SandboxManager
+ __OBJC_METACLASS_RO_$_UpgradeClient
+ __OBJC_METACLASS_RO_$_UpgradeOperation
+ __OBJC_METACLASS_RO_$_UpgradeSequencer
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_OS_xpc_object
+ ___22+[CollationMap getMap]_block_invoke
+ ___24-[UpgradeSequencer init]_block_invoke
+ ___25-[UpgradeClient activate]_block_invoke
+ ___28+[SandboxManager getManager]_block_invoke
+ ___30-[CryptexSession setupHandler]_block_invoke
+ ___32+[CryptexSessionList sharedList]_block_invoke
+ ___35-[EventServer initWithEventStream:]_block_invoke
+ ___35-[UpgradeOperation completeUpgrade]_block_invoke
+ ___37+[UpgradeSequencer getSharedInstance]_block_invoke
+ ___37-[CryptexSession sessionAddParseXPC:]_block_invoke
+ ___39+[CollationMap createCollationForUser:]_block_invoke
+ ___39-[UpgradeSequencer lockIsHeldByClient:]_block_invoke
+ ___40-[UpgradeSequencer abortWithCompletion:]_block_invoke
+ ___41-[CryptexSessionList findCryptexSession:]_block_invoke
+ ___41-[UpgradeOperation onComplete:withQueue:]_block_invoke
+ ___42+[CollationMap addEntryForUser:fromQuire:]_block_invoke
+ ___45+[CollationMap removeEntryForUser:withValue:]_block_invoke
+ ___45-[UpgradeSequencer onUpgradeSessionComplete:]_block_invoke
+ ___46-[UpgradeSequencer _completeUpgradeWithError:]_block_invoke
+ ___48-[UpgradeOperation terminateJobsWithCompletion:]_block_invoke
+ ___49-[CryptexSession sessionStopWithReason:exitCode:]_block_invoke
+ ___50-[UpgradeSequencer completeUpgradeWithCompletion:]_block_invoke
+ ___53-[EventServer sendAlreadyInstalledCryptexesToClient:]_block_invoke
+ ___53-[EventServer sendAlreadyInstalledCryptexesToClient:]_block_invoke_2
+ ___58-[UpgradeSequencer lockInterfaceForClient:withCompletion:]_block_invoke
+ ___58-[UpgradeSequencer lockInterfaceForClient:withCompletion:]_block_invoke_2
+ ___58-[UpgradeSequencer lockInterfaceForClient:withCompletion:]_block_invoke_3
+ ___59+[CollationMap lookupEntryForUser:withBundleID:minVersion:]_block_invoke
+ ___59+[CollationMap lookupEntryForUser:withBundleID:minVersion:]_block_invoke_2
+ ___63-[UpgradeSequencer onUpgradeCompleteForCryptex:withCompletion:]_block_invoke
+ ___72-[UpgradeSequencer startUpgradeForCryptexes:killingJobs:withCompletion:]_block_invoke
+ ___72-[UpgradeSequencer startUpgradeForCryptexes:killingJobs:withCompletion:]_block_invoke_2
+ ___72-[UpgradeSequencer startUpgradeForCryptexes:killingJobs:withCompletion:]_block_invoke_3
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ____CFErrorCopyTopLevelErrorWithDomain_block_invoke
+ ____CFErrorHasDomainAndCode_block_invoke
+ ____bt_log_block_invoke
+ ____codex_schedule_husk_cleanup_block_invoke
+ ____codex_schedule_husk_cleanup_onq_block_invoke
+ ____codex_schedule_husk_cleanup_onq_block_invoke_2
+ ____codex_sub_log_block_invoke
+ ____codex_unbootstrap_continue2_block_invoke
+ ____daemon_init_remote_xpc_listener_block_invoke
+ ____daemon_init_xpc_listener_block_invoke
+ ____daemon_setup_connection_mux_block_invoke
+ ____eplu_sub_log_block_invoke
+ ____fs_log_block_invoke
+ ____mount_sub_log_block_invoke
+ ____quire_attr_parse_bootstrap_contents_block_invoke
+ ____quire_bootstrap_abort_with_error_block_invoke
+ ____quire_bootstrap_abort_with_error_block_invoke_2
+ ____quire_bootstrap_continue_block_invoke
+ ____quire_bootstrap_launch_agents_block_invoke
+ ____quire_handle_device_lock_block_invoke
+ ____quire_handle_device_lock_block_invoke_2
+ ____quire_reset_rsd_devices_block_invoke
+ ____quire_unbootstrap_continue2_block_invoke
+ ____quire_unbootstrap_continue3_block_invoke
+ ____quire_unbootstrap_continue_block_invoke
+ ____quire_unbootstrap_services_block_invoke
+ ____quire_unbootstrap_trust_cache_block_invoke
+ ____quire_unbootstrap_trust_cache_continue_block_invoke
+ ____remote_service_copy_installed_block_invoke
+ ____remote_service_get_queue_block_invoke
+ ____remote_service_install_block_invoke
+ ____remote_service_install_cryptex_continue2_block_invoke
+ ____remote_service_install_cryptex_continue_block_invoke
+ ____remote_service_install_cryptex_failure_uninstall_callback_block_invoke
+ ____remote_service_install_file_recv_block_invoke
+ ____remote_service_list_continue_block_invoke
+ ____remote_service_list_continue_block_invoke_2
+ ____remote_service_list_continue_block_invoke_3
+ ____remote_service_list_continue_block_invoke_4
+ ____remote_service_log_block_invoke
+ ____remote_service_uninstall_block_invoke
+ ____remote_service_uninstall_continue2_block_invoke
+ ____session_rpc_list_block_invoke
+ ____upgrade_sub_lock_osl_block_invoke
+ ____upgrade_sub_trampoline_osl_block_invoke
+ ____xpc_log_block_invoke
+ ____xpc_plist_merge_block_invoke
+ ___block_descriptor_100_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e15_B32?08Q16^B24l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e37_v24?0"<OS_xpc_object>"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e26_B16?0"CollationElement"8ls32l8
+ ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_descriptor_40_e8_32s_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8
+ ___block_descriptor_40_e8_32s_e39_v28?0I8Q12"NSObject<OS_xpc_object>"20ls32l8
+ ___block_descriptor_40_e8_32s_e43_v32?0"NSString"8"UpgradeOperation"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e8_v12?0i8ls32l8
+ ___block_descriptor_40_e8_32w_e33_v16?0"NSObject<OS_xpc_object>"8lw32l8
+ ___block_descriptor_44_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32bs40r_e8_v12?0i8lr40l8s32l8
+ ___block_descriptor_48_e8_32r40r_e8_v12?0i8lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0i8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e35_v32?0"NSString"8"NSString"16^B24lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e36_B24?0Q8"NSObject<OS_xpc_object>"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e28_B16?0"NSObject<OS_quire>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e36_v20?0i8"NSObject<OS_xpc_object>"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_52_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_52_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32r_e20_B40?0q8r*16r*24r*32lr32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_57_e8_32s40s48r_e35_v32?0"NSString"8"NSString"16^B24ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e17_v16?0"NSError"8ls32l8s40l8r56l8s48l8
+ ___block_descriptor_68_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_72_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_80_e8_32s40s48s56r64r_e29_v20?0"OSLaunchdJobInfo"8i16ls32l8r56l8s40l8r64l8s48l8
+ ___block_descriptor_88_e8_32s40s48r_e23_v32?0i8i12i16i20i24i28ls32l8r48l8s40l8
+ ___block_descriptor_tmp
+ ___block_literal_global
+ ___codex_sub_handle_xpc_request_block_invoke
+ ___codex_unbootstrap_continue2_block_invoke.cold.1
+ ___copy_constructor_8_8_t0w24_s24_t32w88_s120_s128_s136_t144w2
+ ___daemon_setup_connection_mux_block_invoke.cold.1
+ ___daemon_setup_connection_mux_block_invoke.cold.2
+ ___darwin_build_inc_version
+ ___darwin_builder_build
+ ___darwin_builder_version
+ ___darwin_debug_binary
+ ___darwin_info_plist
+ ___darwin_variant
+ ___darwin_version_string
+ ___darwin_version_string_heywhat
+ ___destructor_8_s24_s120_s128_s136
+ ___destructor_8_s8_s48_s56
+ ___dg
+ ___endpoint_lookup_sub_handle_xpc_request_block_invoke
+ ___event_server_copy_system_block_invoke
+ ___inventory_xpc_create_endpoint_block_invoke
+ ___inventory_xpc_init_block_invoke
+ ___inventory_xpc_queue_block_invoke
+ ___launch_cryptex_terminate_with_timeout_block_invoke
+ ___launch_cryptex_terminate_with_timeout_block_invoke_2
+ ___log_util_block_invoke
+ ___os_cleanup_close
+ ___os_cleanup_fclose
+ ___path_is_parent_block_invoke
+ ___python_get_site_packages_path_block_invoke
+ ___quire_attach_launch_agents_block_invoke
+ ___quire_detach_launch_agents_block_invoke
+ ___quire_unbootstrap_services_block_invoke.44
+ ___quire_unbootstrap_trust_cache_block_invoke.58
+ ___quire_unbootstrap_trust_cache_block_invoke.61
+ ___remote_service_install_file_recv_block_invoke.34
+ ___remote_service_install_file_recv_block_invoke.35
+ ___remote_service_install_file_recv_block_invoke.36
+ ___remote_service_install_file_recv_block_invoke.37
+ ___remote_service_install_file_recv_block_invoke.38
+ ___remote_service_uninstall_block_invoke.74
+ ___set___object_init_sym_codex_init
+ ___set___subsystem_sym__codex_sub
+ ___set___subsystem_sym__daemon_sub
+ ___set___subsystem_sym__session_sub
+ ___sm_monitor_service_block_invoke
+ ___sm_monitoring_queue_block_invoke
+ ___sub_remote_xpc_message_recv_block_invoke
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_reflection_version
+ ___upgrade_cryptex_set_complete_callback_block_invoke
+ ___upgrade_lock_interface_block_invoke
+ ___watchdog_create_service_descriptions_block_invoke
+ ___watchdog_log_block_invoke
+ ___xpc_plist_merge_block_invoke.2
+ ___xpc_plist_merge_block_invoke.cold.1
+ __amfi_load_trust_cache
+ __amfi_unload_trust_cache
+ __block_descriptor_tmp.13
+ __block_descriptor_tmp.19
+ __block_descriptor_tmp.20
+ __block_descriptor_tmp.21
+ __block_descriptor_tmp.35
+ __block_descriptor_tmp.37
+ __block_descriptor_tmp.39
+ __block_descriptor_tmp.4
+ __block_descriptor_tmp.41
+ __block_descriptor_tmp.42
+ __block_descriptor_tmp.43
+ __block_descriptor_tmp.45
+ __block_descriptor_tmp.48
+ __block_descriptor_tmp.57
+ __block_descriptor_tmp.60
+ __block_descriptor_tmp.62
+ __block_descriptor_tmp.63
+ __block_descriptor_tmp.73
+ __block_descriptor_tmp.74
+ __block_descriptor_tmp.75
+ __block_descriptor_tmp.77
+ __block_descriptor_tmp.78
+ __block_descriptor_tmp.79
+ __block_descriptor_tmp.80
+ __block_literal_global.3
+ __block_literal_global.4
+ __block_literal_global.45
+ __bt_log
+ __buff_destructor_free
+ __buff_destructor_munmap
+ __bundle_bootstrap_contents
+ __bundle_command
+ __bundle_command_args
+ __bundle_env
+ __bundle_identifier
+ __bundle_version
+ __chflags_flags
+ __codex_activate
+ __codex_alloc
+ __codex_authenticate_dmg_notify
+ __codex_authenticate_info_notify
+ __codex_barrier_continue
+ __codex_bootstrap_callback
+ __codex_bootstrap_continue
+ __codex_bootstrap_continue2
+ __codex_bootstrap_continue3
+ __codex_broadcast_event
+ __codex_cleanup_stale_continue
+ __codex_deactivate
+ __codex_dealloc
+ __codex_demux
+ __codex_find
+ __codex_import_core_continue
+ __codex_import_core_impl
+ __codex_import_initial_continue
+ __codex_import_initial_continue2
+ __codex_import_initial_done
+ __codex_import_initial_prep
+ __codex_init
+ __codex_insert_installed
+ __codex_install_callback
+ __codex_install_continue
+ __codex_install_continue2
+ __codex_install_continue3
+ __codex_install_continue4
+ __codex_install_continue5
+ __codex_install_cryptex_continue
+ __codex_list_installed_callback
+ __codex_list_installed_continue
+ __codex_list_installed_continue2
+ __codex_list_installed_quire_continue
+ __codex_list_installed_quire_continue2
+ __codex_lockdown_continue
+ __codex_lockdown_continue2
+ __codex_lockdown_continue3
+ __codex_manifest_check_data_only
+ __codex_mount_callback
+ __codex_mount_continue
+ __codex_mount_continue2
+ __codex_mount_continue3
+ __codex_mount_continue4
+ __codex_mount_continue5
+ __codex_remove_installed
+ __codex_rpc_install_continue2
+ __codex_rpc_install_continue3
+ __codex_rpc_install_failure_unbootstrap_callback
+ __codex_rpc_install_failure_uninstall_callback
+ __codex_rpc_list_reply
+ __codex_rpc_lockdown_continue
+ __codex_schedule_husk_cleanup_onq
+ __codex_state
+ __codex_state_boot_session
+ __codex_state_bootstrap
+ __codex_state_cryptex
+ __codex_state_live
+ __codex_state_mnt
+ __codex_state_remote_stage
+ __codex_state_run
+ __codex_state_shdw
+ __codex_state_stage
+ __codex_sub
+ __codex_sub_log
+ __codex_sub_uninstall_cryptex_continue
+ __codex_sub_uninstall_cryptex_continue2
+ __codex_sub_uninstall_cryptex_reply
+ __codex_unbootstrap_callback
+ __codex_unbootstrap_continue
+ __codex_unbootstrap_continue2
+ __codex_uninstall_callback
+ __codex_uninstall_continue
+ __codex_uninstall_continue2
+ __codex_unmount_callback
+ __codex_unmount_continue
+ __codex_unmount_continue2
+ __codex_unmount_continue3
+ __codex_unset_initial_keepalive
+ __cryptex_base_alloc
+ __csblob_copy
+ __daemon
+ __daemon_alloc
+ __daemon_authinstall_log
+ __daemon_dealloc
+ __daemon_demux
+ __daemon_find
+ __daemon_init_state_directory
+ __daemon_mach_cancel
+ __daemon_mach_recv
+ __daemon_opts
+ __daemon_rpc_open_mountable_continue
+ __daemon_sigterm
+ __daemon_sigterm_continue
+ __daemon_sub
+ __data_only
+ __developer_mode_required
+ __dg
+ __digest_file
+ __eplu_sub_log
+ __find_error
+ __frobnicate_identifier
+ __frobnicate_machservices_apply
+ __frobnicate_path
+ __fs_log
+ __generic_error
+ __generic_errors
+ __hdi_copy_device_nodes
+ __hdi_mount_slow
+ __http_errors
+ __http_internal_error
+ __img4_chip_ap_software_ff00
+ __img4_chip_ap_software_ff01
+ __img4_chip_ap_software_ff06
+ __img4_chip_ap_supplemental
+ __img4_chip_cryptex1_asset
+ __img4_chip_cryptex1_boot_reduced
+ __img4_chip_cryptex1_generic_supplemental
+ __img4_get_nonce_domain_from_index
+ __invoke_flags
+ __mkdir
+ __mkodtempat
+ __mount_sub_authorize
+ __mount_sub_log
+ __mount_sub_mount_cryptex_continue
+ __mount_sub_mount_cryptex_reply
+ __mount_sub_unmount_cryptex_continue
+ __mount_sub_unmount_cryptex_reply
+ __nocode_mount_paths
+ __opendirat
+ __os_cleanup_close.cold.1
+ __os_cleanup_fclose.cold.1
+ __proc_alloc
+ __proc_dealloc
+ __protex_alloc
+ __protex_dealloc
+ __protex_init
+ __protex_stage_callback
+ __protex_stage_continue
+ __protex_stage_install_callback
+ __quire_activate
+ __quire_alloc
+ __quire_attach_launch_agents
+ __quire_bootstrap_abort_with_error
+ __quire_bootstrap_astro
+ __quire_bootstrap_binary
+ __quire_bootstrap_callback
+ __quire_bootstrap_continue
+ __quire_bootstrap_continue2
+ __quire_bootstrap_continue3
+ __quire_bootstrap_diags
+ __quire_bootstrap_feature_flags_domain
+ __quire_bootstrap_library
+ __quire_bootstrap_log_plist
+ __quire_bootstrap_luacore_lib
+ __quire_bootstrap_python_lib
+ __quire_bootstrap_service
+ __quire_bootstrap_trust_cache
+ __quire_bootstrap_watchdog_registration
+ __quire_deactivate
+ __quire_deactivate_launch_agent
+ __quire_dealloc
+ __quire_free_and_drop_strings
+ __quire_iter_binaries
+ __quire_iter_feature_flags
+ __quire_iter_libraries
+ __quire_iter_log_profiles
+ __quire_iter_resource_for_views
+ __quire_iter_resource_for_views_best_effort
+ __quire_mount_callback
+ __quire_mount_continue
+ __quire_parse_watchdog_service_descriptions
+ __quire_pending_services_state_destroy
+ __quire_pending_services_submit
+ __quire_populate_resource_in_data_volume
+ __quire_read_agent
+ __quire_remove_resource_from_data_volume
+ __quire_reset_rsd_devices
+ __quire_unbootstrap_binary
+ __quire_unbootstrap_continue
+ __quire_unbootstrap_diags
+ __quire_unbootstrap_feature_flags_domain
+ __quire_unbootstrap_library
+ __quire_unbootstrap_log_plist
+ __quire_unbootstrap_services
+ __quire_unbootstrap_trust_cache
+ __quire_unbootstrap_trust_cache_continue
+ __quire_unlink_launch_agents
+ __quire_unmount_continue
+ __quire_validate_watchdog_service_labels
+ __read_file
+ __remote_service_copy_installed
+ __remote_service_get_queue
+ __remote_service_install_cryptex_continue
+ __remote_service_install_cryptex_continue2
+ __remote_service_install_cryptex_failure_unbootstrap_callback
+ __remote_service_install_cryptex_failure_uninstall_callback
+ __remote_service_list_continue
+ __remote_service_log
+ __remote_service_read_personalization_identifiers
+ __remote_service_send_reply
+ __remote_service_uninstall_continue
+ __remote_service_uninstall_continue2
+ __required_mount_path
+ __resource_agent
+ __resource_alloc
+ __resource_astro
+ __resource_bin
+ __resource_daemon
+ __resource_dealloc
+ __resource_diags
+ __resource_feature_flags
+ __resource_framework
+ __resource_lib
+ __resource_log_profile
+ __resource_luacore_lib
+ __resource_private_framework
+ __resource_python_lib
+ __rmrfdir
+ __rmrfdirat
+ __session_bootstrap_codex_callback
+ __session_demux
+ __session_find
+ __session_install_codex_callback
+ __session_sub
+ __session_unbootstrap_codex_callback
+ __session_uncork_launchd
+ __session_uninstall_codex_callback
+ __sm_monitor_service_block_invoke.27
+ __sm_monitor_service_block_invoke.27.cold.1
+ __sm_monitor_service_block_invoke.27.cold.2
+ __sscandgst
+ __states
+ __streq_optional
+ __sub_remote_service_demux
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_cryptexd
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_cryptexd
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_cryptexd
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_cryptexd
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_cryptexd
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_cryptexd
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_cryptexd
+ __swift_stdlib_reportUnimplementedInitializer
+ __system
+ __tss_declined_error
+ __tss_error
+ __unknown_error
+ __unmountat
+ __upgrade_sub_lock_for_client_continue
+ __upgrade_sub_lock_osl
+ __upgrade_sub_trampoline_osl
+ __upgrade_sub_trampoline_unblock_client
+ __validator_bundle
+ __validators
+ __view_alloc
+ __view_application
+ __view_create_resource
+ __view_dealloc
+ __view_factory
+ __view_internal
+ __view_platform
+ __watchdog_bootstrap_service
+ __watchdog_unbootstrap_service
+ __xferfd_unguarded
+ __xpc_cferr_to_dictionary
+ __xpc_create_reply
+ __xpc_create_reply_with_cferr
+ __xpc_dictionary_key_with_type_exists
+ __xpc_dictionary_to_cferr
+ __xpc_dictionary_try_get_bool
+ __xpc_dictionary_try_get_cferr
+ __xpc_dictionary_try_get_string
+ __xpc_dictionary_try_get_uint64
+ __xpc_object_has_string
+ __xpc_object_has_string_for_key
+ __xpc_object_set_string_if_absent
+ __xpc_plist_merge
+ __xpc_plist_value_copy
+ __xpc_request_get_argv
+ __zip_errors
+ _acquireHead
+ _addLinkAtHead
+ _aks_create_bag
+ _aks_load_bag
+ _aks_open_bag_for_uid_at_path
+ _aks_save_bag
+ _aks_set_system
+ _aks_unload_bag
+ _amfi_check_dyld_policy_for_pid
+ _amfi_check_dyld_policy_self
+ _amfi_load_trust_cache
+ _amfi_load_trust_cache.cold.1
+ _amfi_load_trust_cache.cold.2
+ _amfi_load_trust_cache.cold.3
+ _amfi_load_trust_cache.cold.4
+ _amfi_unload_trust_cache
+ _apfs_volume_copy_formatter
+ _apfs_volume_create
+ _apfs_volume_delete
+ _apfs_volume_mount
+ _apfs_volume_role_exists
+ _bin_trampoline_write
+ _bt_log.cold.1
+ _bt_log.onceToken
+ _bt_log.osl
+ _buff_destroy
+ _buff_destructor_munmap.cold.1
+ _buff_fopen
+ _buff_init
+ _buff_xfer
+ _buff_xfer_subrange
+ _codex_activate.cold.1
+ _codex_alloc.cold.1
+ _codex_barrier
+ _codex_bootstrap
+ _codex_bootstrap_launch_agents_to_session
+ _codex_cleanup_stale_continue.cold.1
+ _codex_copy_quire
+ _codex_copy_system
+ _codex_create
+ _codex_deactivate.cold.1
+ _codex_dealloc.cold.1
+ _codex_do_once_initialized
+ _codex_import_initial_prep.cold.1
+ _codex_import_initial_prep.cold.2
+ _codex_init
+ _codex_init.cold.1
+ _codex_init.cold.2
+ _codex_insert_installed.cold.1
+ _codex_insert_installed.cold.2
+ _codex_install
+ _codex_install_continue2.cold.1
+ _codex_install_cryptex
+ _codex_installed_cryptex_apply
+ _codex_list_installed
+ _codex_lockdown
+ _codex_lockdown_continue2.cold.1
+ _codex_lockdown_continue2.cold.2
+ _codex_mkodtempat
+ _codex_mount
+ _codex_openat
+ _codex_sub_handle_xpc_request
+ _codex_sub_log.cold.1
+ _codex_sub_log.logHandle
+ _codex_sub_log.onceToken
+ _codex_unbootstrap
+ _codex_unbootstrap_launch_agents_from_session
+ _codex_uninstall
+ _codex_uninstall_continue.cold.1
+ _codex_unmount
+ _codex_unset_initial_keepalive.cold.1
+ _codex_unset_initial_keepalive.cold.2
+ _collation_get_id_for_user
+ _collation_map_add
+ _collation_map_get_endpoint_for_user
+ _collation_map_initialize_for_user
+ _collation_map_lookup_cryptex_with_attributes
+ _collation_map_remove
+ _collation_sub_new_client
+ _copy_homedir_for_user
+ _createError
+ _createSandboxHandleFromFile
+ _create_new_user
+ _cryptex_base_alloc.cold.1
+ _cryptex_path_map_append
+ _cryptex_path_map_create
+ _cryptex_xpc_connection_is_entitled
+ _cryptexdVersionNumber
+ _cryptexdVersionString
+ _csblob_copy.cold.1
+ _ctx_destroy
+ _ctx_new
+ _daemon_alloc.cold.1
+ _daemon_assert_main_queue
+ _daemon_copy
+ _daemon_create
+ _daemon_get_main_queue
+ _daemon_get_xpc_queue
+ _daemon_init
+ _daemon_init_state_directory.cold.1
+ _daemon_init_state_directory.cold.2
+ _daemon_init_state_directory.cold.3
+ _daemon_post_multithreaded_hack
+ _developer_mode_get
+ _digest_file.cold.1
+ _digest_file.cold.2
+ _digest_file.cold.3
+ _digest_file.cold.4
+ _digest_file.cold.5
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dyld_shared_region_increment
+ _dyld_shared_region_read
+ _endpoint_lookup_sub_handle_xpc_request
+ _eplu_sub_log.cold.1
+ _eplu_sub_log.logHandle
+ _eplu_sub_log.onceToken
+ _event_server_activate
+ _event_server_broadcast
+ _event_server_copy_system
+ _extractImage4Payload
+ _ferror
+ _fflush
+ _firmwareExecuteCallback
+ _firmwareFlagsDTRS
+ _firmwareFlagsSplat
+ _flat unique So13OS_xpc_object_p
+ _fopen
+ _fread
+ _fs_log.cold.1
+ _fs_log.onceToken
+ _fs_log.osl
+ _fs_symlink
+ _fs_symlinkat
+ _ftell
+ _getLaunchdDomainForUser
+ _get_session_type_for_domain
+ _get_user_sandbox_params
+ _hash_init
+ _hash_insert
+ _hash_lookup
+ _hash_lookup_cstr
+ _hash_lookup_node
+ _hash_node_init_cstr
+ _hash_remove
+ _hdi_attach
+ _hdi_copy_device_nodes.cold.1
+ _hdi_copy_device_nodes.cold.2
+ _hdi_copy_device_nodes.cold.3
+ _hdi_copy_device_nodes.cold.4
+ _hdi_copy_device_nodes.cold.5
+ _hdi_copy_device_nodes.cold.6
+ _hdi_copy_mounted
+ _hdi_detach
+ _hdi_find_attached
+ _hdi_mount
+ _hfs_mnt_encodinglist
+ _img4ChipEnvironmentCategorized
+ _img4ChipEnvironmentCryptex1Boot
+ _img4ChipEnvironmentCryptex1BootReduced
+ _img4ChipEnvironmentCryptex1Generic
+ _img4ChipEnvironmentCryptex1GenericSupplemental
+ _img4ChipEnvironmentCryptex1PreBoot
+ _img4ChipEnvironmentGlobalFF00
+ _img4ChipEnvironmentGlobalFF01
+ _img4ChipEnvironmentGlobalFF06
+ _img4ChipEnvironmentMobileAsset
+ _img4ChipEnvironmentPersonalized
+ _img4ChipEnvironmentSupplemental
+ _img4NonceDomainCryptex
+ _img4NonceDomainDDI
+ _img4NonceDomainEphemeralCryptex
+ _img4NonceDomainPDI
+ _img4NonceDomainTrustCache
+ _img4_chip_instance_from_xpc
+ _img4_chip_instance_to_xpc
+ _img4_chip_select_categorized_ap
+ _img4_chip_select_cryptex1_boot
+ _img4_chip_select_cryptex1_preboot
+ _img4_firmware_attach_manifest
+ _img4_firmware_destroy
+ _img4_firmware_execute
+ _img4_firmware_init
+ _img4_firmware_init_from_buff
+ _img4_image_get_bytes
+ _inventoryXPC
+ _inventory_xpc_create_endpoint
+ _inventory_xpc_init
+ _kAMAuthInstallApParameterBoardID
+ _kAMAuthInstallApParameterChipID
+ _kAMAuthInstallApParameterProductionMode
+ _kAMAuthInstallApParameterSecurityDomain
+ _kAMAuthInstallTagCryptex1UseProductClass
+ _launch_cryptex_terminate_with_timeout
+ _launchd_session_create_for_uid
+ _launchd_session_create_job
+ _launchd_session_destroy
+ _launchd_session_find_job
+ _launchd_session_remove_job
+ _launchd_session_uncork
+ _main
+ _mkdir.cold.1
+ _module0UUID
+ _module1EntryFlags
+ _module1EntryHashType
+ _module1UUID
+ _module2EntryConstraintCategory
+ _module2EntryFlags
+ _module2EntryHashType
+ _module2UUID
+ _moduleCapabilities
+ _moduleEntryConstraintCategory
+ _moduleEntryFlags
+ _moduleEntryHashType
+ _moduleUUID
+ _mount_sub_handle_request
+ _mount_sub_log.cold.1
+ _mount_sub_log.logHandle
+ _mount_sub_log.onceToken
+ _objc_allocWithZone
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$UTF8String
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_abort
+ _objc_msgSend$_completeUpgradeSession
+ _objc_msgSend$_completeUpgradeWithError:
+ _objc_msgSend$_disableInterfaceLockTimeout
+ _objc_msgSend$_handleInterfaceLockCancel
+ _objc_msgSend$_handleInterfaceLockMessage:
+ _objc_msgSend$_isInterfaceLocked
+ _objc_msgSend$_restartInterfaceLockTimeout
+ _objc_msgSend$_setKernelUpgradeOngoing:
+ _objc_msgSend$_startUpgradeForCryptex:withGraftPath:killingJobs:withCompletion:
+ _objc_msgSend$_timeout
+ _objc_msgSend$_unlockInterface
+ _objc_msgSend$activate
+ _objc_msgSend$addCryptexSession:
+ _objc_msgSend$addEntryForUser:fromQuire:
+ _objc_msgSend$addObject:
+ _objc_msgSend$appendCollationElement:
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$broadcastEvent:forCryptex:withInfo:
+ _objc_msgSend$broadcastEvent:forCryptex:withInfo:toClients:
+ _objc_msgSend$bytes
+ _objc_msgSend$cancelHandler
+ _objc_msgSend$cancelMonitor
+ _objc_msgSend$cancelPeerConnections
+ _objc_msgSend$clientName
+ _objc_msgSend$clients
+ _objc_msgSend$code
+ _objc_msgSend$coll_map
+ _objc_msgSend$completeUpgrade
+ _objc_msgSend$conn
+ _objc_msgSend$containsObject:
+ _objc_msgSend$copy
+ _objc_msgSend$copyJobWithLabel:domain:
+ _objc_msgSend$copySessionName
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createCollationForUser:
+ _objc_msgSend$createCryptexSessionList
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createEndpoint
+ _objc_msgSend$createEndpointWithCompletionHandler:
+ _objc_msgSend$createSymbolicLinkAtPath:withDestinationPath:error:
+ _objc_msgSend$cred
+ _objc_msgSend$cryptexName
+ _objc_msgSend$cs
+ _objc_msgSend$currentDomain
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dict
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$domainForRoleAccountUser:
+ _objc_msgSend$dq
+ _objc_msgSend$enumerateCollationElements:
+ _objc_msgSend$enumerateElements:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$error
+ _objc_msgSend$eventMask
+ _objc_msgSend$exit_code
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$findCryptexSession:
+ _objc_msgSend$getDispatchQueue
+ _objc_msgSend$getMap
+ _objc_msgSend$getSharedInstance
+ _objc_msgSend$group
+ _objc_msgSend$handle
+ _objc_msgSend$handlePublisherAddToken:descriptor:
+ _objc_msgSend$handlePublisherError:
+ _objc_msgSend$handlePublisherInitialBarrier
+ _objc_msgSend$handlePublisherRemoveToken:
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$initWithBundle:version:atPath:withScope:withCommand:withCommandArgs:withEnv:
+ _objc_msgSend$initWithConn:log:
+ _objc_msgSend$initWithCore:
+ _objc_msgSend$initWithCryptexName:graftPath:
+ _objc_msgSend$initWithEventStream:
+ _objc_msgSend$initWithID:
+ _objc_msgSend$initWithPlist:domain:
+ _objc_msgSend$initWithQueue:error:
+ _objc_msgSend$initWithToken:name:eventMask:
+ _objc_msgSend$initiateRemoval:
+ _objc_msgSend$intValue
+ _objc_msgSend$isEmpty
+ _objc_msgSend$isEqual:
+ _objc_msgSend$keyEnumerator
+ _objc_msgSend$lastExitStatus
+ _objc_msgSend$lastSpawnError
+ _objc_msgSend$length
+ _objc_msgSend$list
+ _objc_msgSend$listener
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$lockAcquireQueue
+ _objc_msgSend$lockInterfaceForClient:withCompletion:
+ _objc_msgSend$lockTimer
+ _objc_msgSend$lockingClient
+ _objc_msgSend$log
+ _objc_msgSend$logHandle
+ _objc_msgSend$log_handle
+ _objc_msgSend$lookupEntryForUser:withBundleID:minVersion:
+ _objc_msgSend$monitorOnQueue:withHandler:
+ _objc_msgSend$name
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$onCancel:
+ _objc_msgSend$onComplete:withQueue:
+ _objc_msgSend$onUpgradeCompleteForCryptex:withCompletion:
+ _objc_msgSend$parseCommandFromMessage:fromPeer:
+ _objc_msgSend$path
+ _objc_msgSend$pathComponents
+ _objc_msgSend$peer_array
+ _objc_msgSend$publisher
+ _objc_msgSend$quire_array
+ _objc_msgSend$registrationQueue
+ _objc_msgSend$remove:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeCollationElementWithPath:
+ _objc_msgSend$removeCryptexSession:
+ _objc_msgSend$removeEntryForUser:withValue:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$sandboxHandles
+ _objc_msgSend$sendAlreadyInstalledCryptexesToClient:
+ _objc_msgSend$sessionAddCptxWithBundleID:withType:dmgFd:trustCacheFD:manifestFD:volumeHashFD:infoPlistFd:cx1Properties:
+ _objc_msgSend$sessionAddParseXPC:
+ _objc_msgSend$sessionCompleteCallback
+ _objc_msgSend$sessionEventNotify:
+ _objc_msgSend$sessionMessageReply:
+ _objc_msgSend$sessionStart
+ _objc_msgSend$sessionStopWithReason:exitCode:
+ _objc_msgSend$session_removal_begun
+ _objc_msgSend$session_work_group
+ _objc_msgSend$setAttributes:ofItemAtPath:error:
+ _objc_msgSend$setColl_map:
+ _objc_msgSend$setCs:
+ _objc_msgSend$setDq:
+ _objc_msgSend$setError:
+ _objc_msgSend$setExitReason:withCode:
+ _objc_msgSend$setExit_code:
+ _objc_msgSend$setListener:
+ _objc_msgSend$setLockingClient:
+ _objc_msgSend$setLog:
+ _objc_msgSend$setLog_handle:
+ _objc_msgSend$setName:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setPeer_array:
+ _objc_msgSend$setQuire_array:
+ _objc_msgSend$setSandboxHandles:
+ _objc_msgSend$setSessionCompleteCallback:
+ _objc_msgSend$setSession_removal_begun:
+ _objc_msgSend$setSession_work_group:
+ _objc_msgSend$setStop_reason:
+ _objc_msgSend$setupHandler
+ _objc_msgSend$sharedList
+ _objc_msgSend$shutdownSession:reason:exitCode:
+ _objc_msgSend$startUpgrade
+ _objc_msgSend$startWithCompletionHandler:
+ _objc_msgSend$state
+ _objc_msgSend$stop_reason
+ _objc_msgSend$stringByResolvingSymlinksInPath
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$submitAll:error:
+ _objc_msgSend$terminateJobsWithCompletion:
+ _objc_msgSend$token
+ _objc_msgSend$unpendLaunches:
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$upgradesUnderway
+ _objc_msgSend$wait4Status
+ _objc_msgSend$withInstalledCryptexList:
+ _objc_msgSend$workQueue
+ _objc_msgSend$writeToFile:atomically:encoding:error:
+ _objc_opt_self
+ _object_proto_destroy
+ _object_proto_init
+ _object_set_name
+ _object_set_name_nocopy
+ _objectdestroyTm
+ _path_is_parent
+ _pipeline_start_state_alloc
+ _pipeline_start_state_destroy
+ _proc_alloc.cold.1
+ _proc_create
+ _proc_entitled
+ _proc_resolve
+ _protex_alloc.cold.1
+ _protex_create
+ _protex_init.cold.1
+ _protex_init.cold.2
+ _protex_skip_staging
+ _protex_stage
+ _protex_stage_continue.cold.1
+ _protex_stage_continue.cold.2
+ _protex_stage_continue.cold.3
+ _protex_stage_continue.cold.4
+ _protex_stage_continue.cold.5
+ _puts
+ _python_get_site_packages_path
+ _queryModule
+ _queryModule0
+ _queryModule1
+ _queryModule2
+ _quire_activate.cold.1
+ _quire_alloc.cold.1
+ _quire_apply_overrides
+ _quire_attach_launch_agents
+ _quire_attr_disallow_code
+ _quire_attr_populate_dependencies
+ _quire_boot_session_set
+ _quire_boot_session_test
+ _quire_bootstrap
+ _quire_bootstrap_binary.cold.1
+ _quire_bootstrap_binary.cold.2
+ _quire_bootstrap_continue2.cold.1
+ _quire_bootstrap_diags.cold.1
+ _quire_bootstrap_feature_flags_domain.cold.1
+ _quire_bootstrap_library.cold.1
+ _quire_bootstrap_log_plist.cold.1
+ _quire_bootstrap_trust_cache.cold.1
+ _quire_bootstrap_trust_cache.cold.2
+ _quire_create
+ _quire_deactivate.cold.1
+ _quire_dealloc.cold.1
+ _quire_destroy_attr
+ _quire_detach_launch_agents
+ _quire_get_attr
+ _quire_get_bundle
+ _quire_get_env
+ _quire_get_main_command
+ _quire_get_main_command_args
+ _quire_get_mntpath
+ _quire_get_user
+ _quire_get_version
+ _quire_make_attr
+ _quire_mount
+ _quire_mount_callback.cold.1
+ _quire_mount_continue.cold.1
+ _quire_mount_continue.cold.10
+ _quire_mount_continue.cold.11
+ _quire_mount_continue.cold.12
+ _quire_mount_continue.cold.2
+ _quire_mount_continue.cold.3
+ _quire_mount_continue.cold.4
+ _quire_mount_continue.cold.5
+ _quire_mount_continue.cold.6
+ _quire_mount_continue.cold.7
+ _quire_mount_continue.cold.8
+ _quire_mount_continue.cold.9
+ _quire_pending_services_submit.cold.1
+ _quire_pending_services_submit.cold.2
+ _quire_read_agent.cold.1
+ _quire_set_watchdog_registered
+ _quire_unbootstrap
+ _quire_unbootstrap_binary.cold.1
+ _quire_unbootstrap_binary.cold.2
+ _quire_unbootstrap_feature_flags_domain.cold.1
+ _quire_unbootstrap_library.cold.1
+ _quire_unbootstrap_log_plist.cold.1
+ _quire_unbootstrap_services.cold.1
+ _quire_unmount
+ _quire_unmount_continue.cold.1
+ _quire_unmount_continue.cold.2
+ _quire_watchdog_registered
+ _read_file.cold.1
+ _read_file.cold.2
+ _read_file.cold.3
+ _read_file.cold.4
+ _read_file.cold.5
+ _read_file.cold.6
+ _remote_service_get_queue.cold.1
+ _remote_service_get_queue.onceToken
+ _remote_service_get_queue.queue
+ _remote_service_log.cold.1
+ _remote_service_log.onceToken
+ _remote_service_log.osl
+ _resource_alloc.cold.1
+ _resource_create
+ _resource_open
+ _rmrfdir.cold.1
+ _rmrfdirat.cold.1
+ _rmrfdirat.cold.10
+ _rmrfdirat.cold.11
+ _rmrfdirat.cold.12
+ _rmrfdirat.cold.13
+ _rmrfdirat.cold.14
+ _rmrfdirat.cold.15
+ _rmrfdirat.cold.16
+ _rmrfdirat.cold.17
+ _rmrfdirat.cold.18
+ _rmrfdirat.cold.19
+ _rmrfdirat.cold.2
+ _rmrfdirat.cold.20
+ _rmrfdirat.cold.21
+ _rmrfdirat.cold.22
+ _rmrfdirat.cold.23
+ _rmrfdirat.cold.24
+ _rmrfdirat.cold.25
+ _rmrfdirat.cold.3
+ _rmrfdirat.cold.4
+ _rmrfdirat.cold.5
+ _rmrfdirat.cold.6
+ _rmrfdirat.cold.7
+ _rmrfdirat.cold.8
+ _rmrfdirat.cold.9
+ _rpc_copy
+ _rpc_cred_init_with_audit_token
+ _rpc_creds_equal
+ _rpc_destroy
+ _rpc_init_local
+ _rpc_init_remote
+ _rpc_init_reply
+ _rpc_reply
+ _rpc_reply_with_cferr
+ _searchChainForUUID
+ _searchRuntimeForUUID
+ _session_list_elem_add
+ _session_list_foreach
+ _session_list_get_queue
+ _session_list_shutdown
+ _sm_bootstrap_service
+ _sm_monitor_service
+ _sm_pending_service_create
+ _sm_pending_service_destroy
+ _sm_pending_services_cleanup
+ _sm_service_create
+ _sm_service_destroy
+ _sm_service_on_unload
+ _sm_submit_pending_services
+ _sm_unbootstrap_service
+ _sscandgst.cold.1
+ _sub_get_subsystem_from_msg
+ _sub_log_invoke
+ _sub_recv
+ _sub_remote_xpc_message_recv
+ _sub_reply_and_consume
+ _sub_reply_and_consume_with_cferr
+ _sub_state_alloc
+ _swift_allocBox
+ _swift_allocObject
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_errorRelease
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic So7NSErrorCSgIeyBy_
+ _symbolic So8NSObjectC
+ _symbolic _____ 13CryptexServer0B0C
+ _symbolic _____ 8cryptexd12InventoryXPCC
+ _symbolic _____Sg 13CryptexServer16VirtualEnvConfigV
+ _symbolic _____Sg 6System8FilePathV
+ _symbolic ______pSgSo7NSErrorCSgIeyByy_ So13OS_xpc_objectP
+ _symbolic ytIeAgHr_
+ _sysctl_upgrade_is_ongoing
+ _sysctl_upgrade_set
+ _system_supports_restricted_exec_mode
+ _trustCacheCheckRuntimeForUUID
+ _trustCacheConstructInvalid
+ _trustCacheExtractModule
+ _trustCacheGetCapabilities
+ _trustCacheGetModule
+ _trustCacheGetUUID
+ _trustCacheLoad
+ _trustCacheLoadModule
+ _trustCacheLoadModuleRange
+ _trustCacheLoadRange
+ _trustCacheUnload
+ _unmountat.cold.1
+ _unmountat.cold.2
+ _unmountat.cold.3
+ _upgrade_cryptex_set_complete_callback
+ _upgrade_lock_interface
+ _upgrade_lock_resume
+ _upgrade_sub_lock_for_client
+ _upgrade_sub_lock_osl.cold.1
+ _upgrade_sub_lock_osl.lock_log
+ _upgrade_sub_lock_osl.onceToken
+ _upgrade_sub_trampoline_block_client
+ _upgrade_sub_trampoline_osl.cold.1
+ _upgrade_sub_trampoline_osl.onceToken
+ _upgrade_sub_trampoline_osl.trampoline_log
+ _validateImage4
+ _validateModule
+ _validateModule0
+ _validateModule1
+ _validateModule2
+ _view_alloc.cold.1
+ _view_create
+ _view_iterate_resource
+ _watchdog_available
+ _watchdog_bootstrap_service_descriptions
+ _watchdog_copy_service_description_labels
+ _watchdog_create_service_descriptions
+ _watchdog_log
+ _watchdog_process_service_descriptions
+ _watchdog_unbootstrap_service_descriptions
+ _xpc_cferr_to_dictionary.cold.1
+ _xpc_cferr_to_dictionary.cold.2
+ _xpc_cferr_to_dictionary.cold.3
+ _xpc_cferr_to_dictionary.cold.4
+ _xpc_create_reply.cold.1
+ _xpc_create_reply_with_cferr.cold.1
+ _xpc_dictionary_key_with_type_exists.cold.1
+ _xpc_dictionary_key_with_type_exists.cold.2
+ _xpc_dictionary_to_cferr.cold.1
+ _xpc_dictionary_to_cferr.cold.2
+ _xpc_dictionary_to_cferr.cold.3
+ _xpc_dictionary_to_cferr.cold.4
+ _xpc_dictionary_to_cferr.cold.5
+ _xpc_dictionary_to_cferr.cold.6
+ _xpc_log.onceToken
+ _xpc_log.osl
+ _xpc_plist_value_copy.cold.1
+ aks.m
+ aks_open_bag_for_uid_at_path.cold.1
+ aks_open_bag_for_uid_at_path.cold.2
+ aks_open_bag_for_uid_at_path.cold.3
+ amfi.c
+ apfs.c
+ apfs_volume_copy_formatter.cold.1
+ apfs_volume_copy_formatter.cold.2
+ authinstall.c
+ bin_trampoline.m
+ buff_destroy.cold.1
+ buff_fopen.cold.1
+ buff_fopen.cold.2
+ buff_fopen.cold.3
+ buff_init.cold.1
+ cf.c
+ codex.c
+ collation_map.m
+ cryptex_path_map_append.cold.1
+ cryptex_path_map_append.cold.2
+ cryptexd.c
+ cryptexd_objc.m
+ cryptexd_vers.c
+ ctx_new.cold.1
+ ctx_new.cold.2
+ daemon.c
+ daemon_init.cold.1
+ daemon_init.cold.10
+ daemon_init.cold.11
+ daemon_init.cold.12
+ daemon_init.cold.13
+ daemon_init.cold.14
+ daemon_init.cold.2
+ daemon_init.cold.3
+ daemon_init.cold.4
+ daemon_init.cold.5
+ daemon_init.cold.6
+ daemon_init.cold.7
+ daemon_init.cold.8
+ daemon_init.cold.9
+ daemon_post_multithreaded_hack.cold.1
+ daemon_post_multithreaded_hack.cold.2
+ daemon_post_multithreaded_hack.cold.3
+ darwin_version.c
+ devmode_sysctl.c
+ dyld_shared_region.c
+ event_server.m
+ event_server_copy_system.cold.1
+ event_server_copy_system.onceToken
+ event_server_copy_system.server
+ fs.m
+ getLaunchdDomainForUser.cold.1
+ getManager.manager
+ getManager.once_token
+ getMap.map
+ getMap.once_token
+ getSharedInstance.gUpsq
+ getSharedInstance.onceToken
+ hash_insert.cold.1
+ hash_insert.cold.2
+ hash_insert.cold.3
+ hash_remove.cold.1
+ hdi.c
+ hdi_attach.cold.1
+ hdi_attach.cold.2
+ hdi_attach.cold.3
+ hdi_copy_mounted.cold.1
+ hdi_copy_mounted.cold.2
+ hdi_copy_mounted.cold.3
+ hdi_copy_mounted.cold.4
+ hdi_copy_mounted.cold.5
+ hdi_copy_mounted.cold.6
+ hdi_copy_mounted.cold.7
+ hdi_copy_mounted.cold.8
+ hdi_find_attached.cold.1
+ hdi_find_attached.cold.2
+ hdi_find_attached.cold.3
+ hdi_find_attached.cold.4
+ hdi_mount.cold.1
+ hdi_mount.cold.2
+ hdi_mount.cold.3
+ hdi_mount.cold.4
+ hdi_mount.cold.5
+ hdi_mount.cold.6
+ hdi_mount.cold.7
+ hdi_mount.cold.8
+ img4.c
+ img4_xpc.m
+ inventory_xpc.m
+ inventory_xpc_init.cold.1
+ inventory_xpc_queue.onceToken
+ inventory_xpc_queue.queue
+ iokit.c
+ launch_util.m
+ launchd_session.m
+ launchd_session_uncork.cold.1
+ launchd_session_uncork.cold.2
+ libamfi.cpp
+ log_util.log
+ log_util.onceToken
+ mount_sub_handle_request.cold.1
+ mount_sub_handle_request.cold.2
+ mount_sub_handle_request.cold.3
+ mount_sub_handle_request.cold.4
+ mount_sub_handle_request.cold.5
+ mount_sub_handle_request.cold.6
+ object_set_name.cold.1
+ objectdestroy.7Tm
+ path.m
+ pipeline_start_state_destroy.cold.1
+ proc.c
+ proc_resolve.cold.1
+ proc_resolve.cold.2
+ protex.c
+ python.m
+ python_get_site_packages_path.cold.1
+ python_get_site_packages_path.onceToken
+ python_get_site_packages_path.site_packages_path
+ quire.c
+ quire_attr_populate_dependencies.cold.1
+ quire_attr_populate_dependencies.cold.2
+ quire_attr_populate_dependencies.cold.3
+ quire_attr_populate_dependencies.cold.4
+ quire_attr_populate_dependencies.cold.5
+ quire_boot_session_set.cold.1
+ quire_bootstrap.cold.1
+ quire_bootstrap.cold.2
+ quire_create.cold.1
+ quire_create.cold.2
+ quire_create.cold.3
+ quire_unbootstrap.cold.1
+ quire_unbootstrap.cold.2
+ resource.c
+ resource_create.cold.1
+ resource_open.cold.1
+ restricted_exec_mode_sysctl.c
+ rpc_copy.cold.1
+ rpc_copy.cold.2
+ rpc_reply.cold.1
+ rpc_reply.cold.2
+ rpc_reply_with_cferr.cold.1
+ rpc_reply_with_cferr.cold.2
+ sandboxing.m
+ session.m
+ session_list_foreach.cold.1
+ sharedList.once_token
+ sharedList.shared_list
+ sm.m
+ sm_bootstrap_service.cold.1
+ sm_monitor_service.cold.1
+ sm_monitoring_queue.onceToken
+ sm_monitoring_queue.queue
+ sm_pending_service_create.cold.1
+ sm_service_create.cold.1
+ sub.c
+ sub_codex.c
+ sub_codex_xpc.m
+ sub_collation.m
+ sub_daemon.c
+ sub_endpoint_lookup.m
+ sub_get_subsystem_from_msg.cold.1
+ sub_log_invoke.cold.1
+ sub_log_invoke.cold.2
+ sub_log_invoke.cold.3
+ sub_mount.m
+ sub_pipeline.c
+ sub_recv.cold.1
+ sub_remote_service.m
+ sub_session.c
+ sub_upgrade_lock.m
+ sub_upgrade_trampoline.m
+ upgrade_sequencer.m
+ upgrade_sysctl.c
+ usermanager.m
+ view.c
+ view_iterate_resource.cold.1
+ view_iterate_resource.cold.2
+ view_iterate_resource.cold.3
+ watchdog.m
+ watchdog_log.cold.1
+ watchdog_log.log
+ watchdog_log.onceToken
+ xpc_entitlements.m
- radr://5614542
CStrings:
+ "#16@0:8"
+ "/private/var/db/com.apple.security.cryptexd"
+ "589.0.9"
+ "@\"NSString\"16@0:8"
+ "@(#)VERSION:Darwin Cryptex Manager Version 2.0.0: Sat Jun 14 01:16:02 PDT 2025; root:libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@32@0:8@16^@24"
+ "@40@0:8:16@24@32"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "Darwin Cryptex Manager Version 2.0.0: Sat Jun 14 01:16:02 PDT 2025; root:libcryptex_executables-589.0.9~251/cryptexd/RELEASE_ARM64E"
+ "ENDPOINT"
+ "ENDPOINT_INDEX"
+ "ENDPOINT_LOOKUP"
+ "Failed to create Inventory XPC server: %@"
+ "Failed to get Inventory XPC endpoint: %@"
+ "Failed to read keybag from disk: %{darwin.errno}d"
+ "Failed to start Inventory XPC server: %@"
+ "Invalid chip instance XPC object."
+ "Invalid endpoint index (%llu)"
+ "Invalid input(s)."
+ "Invalid value (%llu) for key: %s"
+ "Missing key: %s"
+ "NSObject"
+ "OS_xpc_object"
+ "Returning endpoint to inventory"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,R"
+ "Unable to open %s for reading: %{darwin.errno}d"
+ "Unable to open %s for writing: %{darwin.errno}d"
+ "Unable to write %s: %{darwin.errno}d"
+ "Unexpected message: %{public}s"
+ "Vv16@0:8"
+ "[no error]"
+ "^{_NSZone=}16@0:8"
+ "_TtC8cryptexd12InventoryXPC"
+ "ack provisioning failure"
+ "aks_create_bag: %{mach.errno}x"
+ "aks_load_bag() failed with kAKSReturnBadDeviceKey, destroying the existing keybag"
+ "aks_load_bag: %{mach.errno}x"
+ "aks_save_bag: %{mach.errno}x"
+ "aks_set_system kb_handle: %d uid: %d: %{mach.errno}x"
+ "aks_unload_bag: %{mach.errno}x"
+ "allocation failure"
+ "apple connect auth failure"
+ "apple connect canceled"
+ "apple connect not found"
+ "assertion failure: \"CFGetTypeID(graft_path) == CFStringGetTypeID()\" -> %llu"
+ "assertion failure: \"CFGetTypeID(name) == CFStringGetTypeID()\" -> %llu"
+ "autorelease"
+ "bad build identity"
+ "bad parameter"
+ "bad response"
+ "bad zip file"
+ "baseband provisioning failure"
+ "class"
+ "conformsToProtocol:"
+ "conversion failure"
+ "createEndpointWithCompletionHandler:"
+ "cryptex1.boot.app"
+ "cryptex1.boot.os"
+ "cryptex1.generic"
+ "cryptex1.generic.supplemental"
+ "cryptex1.preboot.app"
+ "cryptex1.preboot.os"
+ "cryptex1.safari-downlevel"
+ "cryptex_base"
+ "cryptexd.InventoryXPC"
+ "crypto error"
+ "debugDescription"
+ "description"
+ "endpoint_lookup_sub"
+ "entry not found"
+ "failed to write keybag to disk: %{darwin.errno}d"
+ "file error"
+ "fread %s: %{darwin.errno}d"
+ "fseek SEEK_END: %{darwin.errno}d"
+ "fseek SEEK_SET: %{darwin.errno}d"
+ "ftell: %{darwin.errno}d"
+ "fusing failure"
+ "generic error"
+ "global.bootability-brain"
+ "global.install-assistant"
+ "global.ota-update-brain"
+ "global.pdi"
+ "hash"
+ "hash error"
+ "http forbidden"
+ "http internal server error"
+ "http not found"
+ "http proxy auth needed"
+ "http unauthorized"
+ "img4_chip_instance_from_xpc"
+ "init routine called after transition to multithreaded"
+ "init()"
+ "initWithQueue:error:"
+ "internal error"
+ "invalid baseband firmware"
+ "invalid fls object"
+ "invalid img3 object"
+ "invalid img4 object"
+ "inventory-ephemeral"
+ "inventory-persistent"
+ "inventory-server"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "libCS: failed AppleImage4 callback: Decode Error"
+ "libCS: failed AppleImage4 callback: Manifest Violation"
+ "libCS: failed AppleImage4 callback: Payload Violation"
+ "libCS: failed AppleImage4 callback: Stale Nonce"
+ "libCS: failed AppleImage4 callback: Unknown Error"
+ "libCS: failed AppleImage4 callback: Unknown Format"
+ "libCS: failed AppleImage4 callback: Wrong Crypto"
+ "libCS: failed AppleImage4 callback: Wrong Object"
+ "network error"
+ "not implemented"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "personalized.cryptex-research"
+ "personalized.ddi"
+ "personalized.engineering-root"
+ "personalized.ephemeral-cryptex"
+ "personalized.mobile-asset-brain"
+ "personalized.pdi"
+ "personalized.supplemental-ephemeral"
+ "personalized.supplemental-persistent"
+ "personalized.trust-cache"
+ "rb"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "security.codesigning.config"
+ "self"
+ "server"
+ "server not reachable"
+ "server timed out"
+ "startWithCompletionHandler:"
+ "superclass"
+ "tss declined"
+ "tss error"
+ "unknown error"
+ "unlink(\"%s\"): %{darwin.errno}d"
+ "updater not found"
+ "updater operation failure"
+ "upgrade_lock_error"
+ "upgrade_sub_lock"
+ "v24@0:8@?<v@?@\"<OS_xpc_object>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@?0@\"<OS_xpc_object>\"8@\"NSError\"16"
+ "vm.shared_region_control"
+ "wb"
+ "zip buffer error"
+ "zip close failure"
+ "zip data error"
+ "zip internal error"
+ "zip memory error"
+ "zip open failure"
+ "zip parameter error"
+ "zip stream error"
+ "zip version error"
+ "zip write failure"
+ "zone"
- "589.0.1"
- "@(#)VERSION:Darwin Cryptex Manager Version 2.0.0: Fri May 30 21:09:07 PDT 2025; root:libcryptex_executables-589.0.1~639/cryptexd/RELEASE_ARM64E"
- "Darwin Cryptex Manager Version 2.0.0: Fri May 30 21:09:07 PDT 2025; root:libcryptex_executables-589.0.1~639/cryptexd/RELEASE_ARM64E"
- "unexpected failure: init routine called after transition to multithreaded"

```
