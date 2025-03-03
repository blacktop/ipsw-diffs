## cryptexd

> `/usr/libexec/cryptexd`

```diff

-475.80.3.0.0
-  __TEXT.__text: 0x41bd8
-  __TEXT.__auth_stubs: 0x1cb0
-  __TEXT.__objc_stubs: 0x15e0
-  __TEXT.__objc_methlist: 0x834
-  __TEXT.__const: 0x710
-  __TEXT.__gcc_except_tab: 0x1424
-  __TEXT.__objc_methname: 0x161f
+493.100.51.0.0
+  __TEXT.__text: 0x4a9a0
+  __TEXT.__auth_stubs: 0x1d30
+  __TEXT.__objc_stubs: 0x1620
+  __TEXT.__objc_methlist: 0x844
+  __TEXT.__const: 0x9d8
+  __TEXT.__gcc_except_tab: 0x18e0
+  __TEXT.__objc_methname: 0x1649
   __TEXT.__objc_classname: 0xf9
-  __TEXT.__objc_methtype: 0x3b8
-  __TEXT.__cstring: 0x2f3c
-  __TEXT.__oslogstring: 0x8789
-  __TEXT.__unwind_info: 0x9c8
-  __DATA_CONST.__auth_got: 0xe68
-  __DATA_CONST.__got: 0x258
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2718
+  __TEXT.__objc_methtype: 0x3c9
+  __TEXT.__cstring: 0x34d5
+  __TEXT.__oslogstring: 0x9859
+  __TEXT.__unwind_info: 0xb98
+  __DATA_CONST.__auth_got: 0xea8
+  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x2a30
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_nlclslist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__subsystem: 0x20
+  __DATA_CONST.__subsystem: 0x18
   __DATA_CONST.__object_init: 0x8
   __DATA.__objc_const: 0x1350
-  __DATA.__objc_selrefs: 0x5f8
+  __DATA.__objc_selrefs: 0x600
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x430
-  __DATA.__bss: 0x4f8
+  __DATA.__bss: 0x528
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
   - /System/Library/PrivateFrameworks/WatchdogServiceManagement.framework/WatchdogServiceManagement
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libcryptex_core.dylib

   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 786
-  Symbols:   556
-  CStrings:  1633
+  Functions: 899
+  Symbols:   564
+  CStrings:  1764
 
Symbols:
+ ___sandbox_ms
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha384_di
+ _cryptex_core_metadata_matches
+ _cryptex_core_metadata_matches_xattrs
+ _cryptex_core_write_metadata_to_xattrs
+ _cryptex_magister_authenticate_f
+ _cryptex_sync
+ _dispatch_block_create_with_qos_class
+ _dispatch_source_set_cancel_handler
+ _dispatch_workloop_create
+ _objc_retainAutoreleasedReturnValue
+ _wd_optin_service_unregister_sync
- ___strcat_chk
- __vproc_set_global_on_demand
- _cryptex_sync_f
- _cryptex_uninstall_unpack
- _objc_retain_x27
- _usleep
CStrings:
+ "%{public}s: %s not deleted because content does not match cryptex"
+ "%{public}s: %s not deleted because metadata does not match cryptex"
+ "%{public}s: All husks cleaned up."
+ "%{public}s: Attaching launch agents for user id %u"
+ "%{public}s: Cryptex with the same name is still bootstrapped."
+ "%{public}s: Failed to attach launch agents for user id %u"
+ "%{public}s: Failed to create %{public}s %{darwin.errno}d"
+ "%{public}s: Failed to delete %{public}s %{darwin.errno}d"
+ "%{public}s: Failed to delete cryptex root dir. %{darwin.errno}d"
+ "%{public}s: Failed to read level of REM support. %{darwin.errno}d"
+ "%{public}s: Failed to remove boot session state directory. %{darwin.errno}d"
+ "%{public}s: Failed to unbootstrap trust cache."
+ "%{public}s: Failed to unregister services with watchdog."
+ "%{public}s: No feature flag file found at %s"
+ "%{public}s: No library symlink found at %s"
+ "%{public}s: No log profile found at %s"
+ "%{public}s: No trampoline found at %s"
+ "%{public}s: Quire has no boot session state directory"
+ "%{public}s: Rescheduling cleanup."
+ "%{public}s: Signature metadata mismatches cryptex."
+ "%{public}s: Skipping authentication of trust cache to be unloaded."
+ "%{public}s: Some husks failed cleanup."
+ "%{public}s: Submitting pending services to launchd"
+ "%{public}s: Too many failed attempts, not rescheduling."
+ "%{public}s: _codex_bootstrap_continue3 bootstrap succeeded"
+ "%{public}s: _codex_bootstrap_continue3 occured"
+ "%{public}s: _opendirat %{darwin.errno}d"
+ "%{public}s: _quire_read_agent: processing agent: %s"
+ "%{public}s: all services fully removed"
+ "%{public}s: begin background husk cleanup, attempt #%d"
+ "%{public}s: bootstrapping agents"
+ "%{public}s: bootstrapping agents done"
+ "%{public}s: copyfile %{public}s to %{public}s: %{darwin.errno}d"
+ "%{public}s: copyfile %{public}s to %{public}s: success"
+ "%{public}s: digest %s %{darwin.errno}d"
+ "%{public}s: faccessat(%s): %{darwin.errno}d"
+ "%{public}s: failed to authenticate trust cache before unloading it"
+ "%{public}s: failed to check SEP ratcheting support"
+ "%{public}s: failed to clear trustcache-loaded flag"
+ "%{public}s: failed to copy %s to %s %{darwin.errno}d"
+ "%{public}s: failed to create directory: %s %{darwin.errno}d"
+ "%{public}s: failed to open feature flag file %{darwin.errno}d"
+ "%{public}s: failed to open ff at %s %{darwin.errno}d"
+ "%{public}s: failed to open logging profile plist %{darwin.errno}d"
+ "%{public}s: failed to open symlink at %s %{darwin.errno}d"
+ "%{public}s: failed to open trampoline at %s %{darwin.errno}d"
+ "%{public}s: failed to open trampoline for %s %{darwin.errno}d"
+ "%{public}s: failed to read agent: %s. %{darwin.errno}d"
+ "%{public}s: failed to set trustcache-loaded flag"
+ "%{public}s: failed to unload authentic trust cache"
+ "%{public}s: failed to unload trust cache"
+ "%{public}s: hdi_detach: %{darwin.errno}d"
+ "%{public}s: hdi_detach: success"
+ "%{public}s: husk cleanup: detach: %{darwin.errno}d"
+ "%{public}s: husk cleanup: detach: success"
+ "%{public}s: husk cleanup: unmount: %{darwin.errno}d"
+ "%{public}s: husk cleanup: unmount: success"
+ "%{public}s: preparing launch agents"
+ "%{public}s: reading agent plist: %s"
+ "%{public}s: rmrfdir: %{darwin.errno}d"
+ "%{public}s: scheduled background husk cleanup in %d seconds"
+ "%{public}s: service fully removed: %{public}s"
+ "%{public}s: submitting jobs to launchd"
+ "%{public}s: trust cache already loaded"
+ "%{public}s: trust cache is not loaded"
+ "%{public}s: unbootstrapping service: %{public}s"
+ "%{public}s: uninstall stale cryptex: %s: %{darwin.errno}d"
+ "%{public}s: uninstall stale cryptex: %s: success"
+ "%{public}s: unlink %s: %{darwin.errno}d"
+ "%{public}s: unlink %s: success"
+ "%{public}s: unloading trust cache"
+ "%{public}s: unloading trust cache is not supported"
+ "%{public}s: unmount failure will not result in a quire husk"
+ "'Ignoring session shutdown for '%s': session gone."
+ ".jobs-loaded"
+ ".registered-for-watchdog"
+ ".trustcache-loaded"
+ "/Library/Caches/com.apple.xbs/Sources/libcryptex_executables/cryptexd/sm/sm.m"
+ "/Library/Caches/com.apple.xbs/Sources/libcryptex_executables/cryptexd/sub/sub_codex_xpc.m"
+ "/Library/Preferences/Logging/Subsystems"
+ "493.100.51"
+ "@(#)VERSION:Darwin Cryptex Manager Version 2.0.0: Tue Feb 25 22:06:17 PST 2025; root:libcryptex_executables-493.100.51~484/cryptexd/RELEASE_ARM64E"
+ "AMFI"
+ "B16@?0^{__CFError=}8"
+ "Bootstrap %{public}s [no error]"
+ "Bootstrap %{public}s: %@"
+ "CODEX_SUB_REQ"
+ "Created job %@ for uid %d: %@ (session: %s)"
+ "Cryptex Session process (uuid %s) monitor event %ld"
+ "Darwin Cryptex Manager Version 2.0.0: Tue Feb 25 22:06:17 PST 2025; root:libcryptex_executables-493.100.51~484/cryptexd/RELEASE_ARM64E"
+ "Destroying the launchd session with uid %d"
+ "Failed to %{public}s job %zu with watchdog"
+ "Failed to batch submit jobs to launchd %{darwin.errno}d"
+ "Failed to create launchd job."
+ "Failed to destroy launchd session: %@"
+ "Failed to extract trust cache: %{public}s"
+ "Failed to find cryptex matching %{public}s"
+ "Failed to find domain for uid %d %{darwin.errno}d"
+ "Failed to get trust cache UUID: %{public}s"
+ "Failed to initiate remove of domain %d %{darwin.errno}d"
+ "Failed to lookup sm service in launchd."
+ "Failed to parse version string '%{public}s'"
+ "Failed to remove sm service from launchd %{darwin.errno}d"
+ "Finished quire detach."
+ "Job has no label %{darwin.errno}d"
+ "Monitor called on job that has already been released"
+ "Monitor event for %@ (session: %s)"
+ "No job found with label '%{public}s' %{darwin.errno}d"
+ "Populating %{public}s in Data volume is unsupported"
+ "Rediscovered job %{public}s (UUID: %{public}s) for uid %d"
+ "Removing %{public}s from Data volume is unsupported"
+ "Session is being torn down already"
+ "Shutting down process monitoring for %{public}@"
+ "Signature metadata does not match cryptex. Was the wrong personalization ticket provided?: %@"
+ "Starting process monitoring for %@ (session: %s)"
+ "TCReturn_t(component: %d, error: %d, uniqueError: %d)"
+ "UNINSTALL"
+ "UNINSTALL:CXID"
+ "UNINSTALL:CXVER"
+ "UNINSTALL:ERROR_DICT"
+ "UNINSTALL:FORCE_UNMOUNT"
+ "Unbootstrap existing %{public}s [no error]"
+ "Unbootstrap existing %{public}s: %@"
+ "Unbootstrap trust cache [no error]"
+ "Unbootstrap trust cache: %@"
+ "Unloading trust cache is not implemented."
+ "Unloading trust cache is not supported on this device."
+ "Unregister jobs from watchdog [no error]"
+ "Unregister jobs from watchdog: %@"
+ "Unregistered job with watchdog: %{public}@"
+ "Unset 'jobs loaded' flag [no error]"
+ "Unset 'jobs loaded' flag: %@"
+ "XPC client <process=%s pid=%d>: Client not authorized to uninstall cryptex. %{darwin.errno}d"
+ "XPC client <process=%s pid=%d>: Invalid value '%{public}s' for key '%{public}s' %{darwin.errno}d"
+ "XPC client <process=%s pid=%d>: Replying to uninstall client: %{public}@"
+ "^{__CFError=}16@?0^{_session_core={_os_object_header=^vii}{_object_proto=**^{os_log_s}}IqqQ^v^v^v***B}8"
+ "_amfi_load_trust_cache"
+ "_amfi_unload_trust_cache"
+ "_codex_bootstrap_continue"
+ "_codex_bootstrap_continue2"
+ "_codex_im4m_matches_cryptex"
+ "_quire_bootstrap_continue2"
+ "_quire_bootstrap_log_plist"
+ "_quire_bootstrap_trust_cache"
+ "_quire_needs_sep_ratcheting"
+ "_quire_parse_watchdog_service_descriptions"
+ "_quire_populate_resource_in_data_volume"
+ "_quire_read_agent"
+ "_quire_remove_resource_from_data_volume"
+ "_quire_unbootstrap_authentic_trust_cache"
+ "_quire_unbootstrap_binary"
+ "_quire_unbootstrap_continue3"
+ "_quire_unbootstrap_feature_flags_domain"
+ "_quire_unbootstrap_library"
+ "_quire_unbootstrap_log_plist"
+ "_quire_unbootstrap_trust_cache_continue"
+ "_quire_unbootstrap_watchdog_registration"
+ "_watchdog_unbootstrap_service"
+ "assertion failure: \"(*__error())\" -> %llu"
+ "assertion failure: \"error\" -> %llu"
+ "assertion failure: \"fcheck_np(cursor, fr, 1)\" -> %llu"
+ "assertion failure: \"manager != ((void*)0)\" -> %llu"
+ "assertion failure: \"munmap(map, len)\" -> %{errno}d"
+ "assertion failure: \"q->q_attachpath != ((void*)0)\" -> %llu"
+ "assertion failure: \"qa->qa_info != ((void*)0)\" -> %llu"
+ "assertion failure: \"realpath_np(q_bootstrap->rootfd, q_bootstrap->rootpath)\" -> %llu"
+ "assertion failure: \"self.sandboxHandles != ((void*)0)\" -> %llu"
+ "boot-session"
+ "codex_sub"
+ "codex_sub_handle_xpc_request"
+ "codex_sub_uninstall_cryptex"
+ "com.apple.security.cryptexd.cryptex.jobmonitor"
+ "could not find AppleMobileFileIntegrity %{darwin.errno}d"
+ "could not resolve mount point for unmount: %{darwin.errno}d"
+ "detach succeeded"
+ "detaching: path = %s, fd = %d"
+ "failed to copy %{public}s to %{public}s %{darwin.errno}d"
+ "failed to map file into memory: %{darwin.errno}d"
+ "failed to stat file: %{darwin.errno}d"
+ "failed to unbootstrap agent: %s: %@"
+ "failed to unbootstrap service: %{public}s: %@"
+ "failed to unload trust cache %{darwin.errno}d"
+ "got EBADF and disk is gone, detach succeeded"
+ "got EBADF but disk still present, retrying detach"
+ "ioctl: DKIOCEJECT: %{darwin.errno}d"
+ "launchd_session_create_job"
+ "launchd_session_destroy"
+ "launchd_session_find_job"
+ "name '%s'"
+ "name '%s' and version '%s'"
+ "quire unbootstrap: %s [no error]"
+ "quire unbootstrap: %s: %@"
+ "quire_attach_launch_agents_block_invoke"
+ "quire_boot_session_set"
+ "register"
+ "security.codesigning.config"
+ "session_list_foreach: passing session %@"
+ "shutdownSession:reason:exitCode:"
+ "sm_submit_pending_services"
+ "sm_unbootstrap_service"
+ "submitAll:error:"
+ "unexpected failure: Failed to register for keybag notifications"
+ "unexpected failure: buffer not large enough for hash: actual = %lu, expected >= %lu"
+ "unexpected failure: quire deallocated with open boot session state dir = %d"
+ "unexpected failure: uninstalled core has no root asset"
+ "unlink %s %{darwin.errno}d"
+ "unmount: %{darwin.errno}d"
+ "unmounting: %s"
+ "unregister"
+ "v16@?0^{__CFError=}8"
+ "v40@0:8*16q24Q32"
+ "v40@?0^{_cryptex_magister={_cryptex_base={_os_object_header=^vii}Q^{dispatch_queue_s}^{dispatch_queue_s}^?i}{_object_proto=**^{os_log_s}}Q^{_cryptex_core}^{_cryptex_signature}^{_cryptex_host}^{_img4_chip}{_img4_nonce=S[48C]I}}8r^{_cryptex_asset_type=Q^?^?qI**}16^{_buff=(?=**^v^v)(?=Qq)^vQ^v^?^?}24^{__CFError=}32"
+ "watchdog_process_service_descriptions"
+ "wd_optin_service_unregister_sync failed for job: %{public}@ %{darwin.errno}d"
+ "wd_optin_service_unregister_sync not supported."
- "%{public}s: %s RunAtLoad jobs by %s global on-demand bit in launchd"
- "%{public}s: Failed to %s vproc global on-demand bit."
- "%{public}s: Failed to bootstrap agent: %s. %{darwin.errno}d"
- "%{public}s: Failed to create cryptex dir in uninstall area. %{darwin.errno}d"
- "%{public}s: Failed to extract cryptex identifier and version.: %{darwin.errno}d"
- "%{public}s: Failed to load trust cache."
- "%{public}s: Finished quire detach."
- "%{public}s: Signature metadata does not match cryptex.: %{darwin.errno}d"
- "%{public}s: Unexpected error during uninstall from live store"
- "%{public}s: Unexpected error during uninstall from persisted store"
- "%{public}s: _codex_bootstrap_continue2 bootstrap succeeded"
- "%{public}s: _codex_bootstrap_continue2 occured"
- "%{public}s: _quire_bootstrap_agents: bootstrapping agent: %s"
- "%{public}s: bootstrapping agent: %s"
- "%{public}s: could not resolve mount point for unmount: %{darwin.errno}d"
- "%{public}s: detach succeeded"
- "%{public}s: detaching: path = %s, fd = %d"
- "%{public}s: device busy"
- "%{public}s: failed to copy %s to /Library/Preferences/FeatureFlags/Domain/ %{darwin.errno}d"
- "%{public}s: failed to copy %s to /Library/Preferences/Logging/Subsystems/ %{darwin.errno}d"
- "%{public}s: failed to create FeatureFlags domain directory %{darwin.errno}d"
- "%{public}s: failed to unbootstrap agent: %s: %{darwin.errno}d"
- "%{public}s: failed to unbootstrap service: %s: %{darwin.errno}d"
- "%{public}s: failed to uninstall stale cryptex: %s: %{darwin.errno}d"
- "%{public}s: im4m identifier mismatches cryptex (actual, expected): (%s, %s): %{darwin.errno}d"
- "%{public}s: im4m version mismatches cryptex (actual, expected): (%s, %s): %{darwin.errno}d"
- "%{public}s: ioctl: DKIOCEJECT: %{darwin.errno}d"
- "%{public}s: launchagent bootstrap failed: %{darwin.errno}d"
- "%{public}s: mount busy [%lu]: %s"
- "%{public}s: quire unbootstrap: %s"
- "%{public}s: renameat failed %{darwin.errno}d"
- "%{public}s: renameat: %{darwin.errno}d"
- "%{public}s: unbootstrapping service: %s"
- "%{public}s: uninstalled stale cryptex: %s"
- "%{public}s: unmounting: %s"
- ".."
- "/Library/Caches/com.apple.xbs/Sources/libcryptex_executables/cryptexd/sm/sm.c"
- "/Library/Preferences/FeatureFlags/Domain/"
- "475.80.3"
- "@(#)VERSION:Darwin Cryptex Manager Version 2.0.0: Fri Dec 20 01:21:46 PST 2024; root:libcryptex_executables-475.80.3~220/cryptexd/RELEASE_ARM64E"
- "CRYPTEX"
- "Darwin Cryptex Manager Version 2.0.0: Fri Dec 20 01:21:46 PST 2024; root:libcryptex_executables-475.80.3~220/cryptexd/RELEASE_ARM64E"
- "Error: couldn't find session for cryptex that exited."
- "Failed to add sm service to launchd."
- "Failed to register job %zu with watchdog"
- "Failed to submit job to launchd with error: %@ %{darwin.errno}d"
- "Initiating removal for domain failed: %@"
- "Shut down process monitoring"
- "Shutting down process monitoring"
- "Submited job %s (UUID: %s) for uid %d"
- "Submitting job for uid %d : %@"
- "Suppressing"
- "Unsuppressing"
- "Waiting for unlock %{darwin.errno}d"
- "_codex_uninstall_location"
- "_quire_bootstrap_agents"
- "_quire_bootstrap_load_trust_cache"
- "_quire_bootstrap_log_plists"
- "_quire_globally_toggle_runatload_jobs"
- "_quire_handle_device_lock"
- "amfi_load_trust_cache"
- "assertion failure: \"(*__error())\" -> %lld"
- "assertion failure: \"error\" -> %lld"
- "assertion failure: \"fcheck_np(cursor, fr, 1)\" -> %lld"
- "assertion failure: \"manager != ((void *)0)\" -> %lld"
- "assertion failure: \"q->q_attachpath != ((void *)0)\" -> %lld"
- "assertion failure: \"qa->qa_info != ((void *)0)\" -> %lld"
- "assertion failure: \"realpath_np(q_bootstrap->rootfd, q_bootstrap->rootpath)\" -> %lld"
- "assertion failure: \"self.sandboxHandles != ((void *)0)\" -> %lld"
- "clear"
- "clearing"
- "com.apple.CryptexIdentifier"
- "com.apple.CryptexVersion"
- "could not find AppleMobileFileIntegrity"
- "launchd_session_add_job"
- "passing session %@"
- "quire mount: %s: %@"
- "set"
- "setting"
- "submit:"
- "uninstalled"
- "v16@?0^{_session_core={_os_object_header=^vii}{_object_proto=**^{os_log_s}}IqqQ^v^v^v***B}8"
- "v24@?0^{_session_core={_os_object_header=^vii}{_object_proto=**^{os_log_s}}IqqQ^v^v^v***B}8^v16"
- "watchdog_bootstrap_service_descriptions"

```
