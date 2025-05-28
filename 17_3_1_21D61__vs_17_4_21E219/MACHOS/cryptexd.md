## cryptexd

> `/usr/libexec/cryptexd`

```diff

-369.60.3.0.0
-  __TEXT.__text: 0x39a24
-  __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_stubs: 0x1520
+369.100.36.0.0
+  __TEXT.__text: 0x3e148
+  __TEXT.__auth_stubs: 0x1c20
+  __TEXT.__objc_stubs: 0x1540
   __TEXT.__objc_methlist: 0x838
-  __TEXT.__const: 0x628
-  __TEXT.__gcc_except_tab: 0xa2c
-  __TEXT.__objc_methname: 0x15ae
-  __TEXT.__objc_classname: 0xf8
-  __TEXT.__objc_methtype: 0x3ae
-  __TEXT.__cstring: 0x2218
-  __TEXT.__oslogstring: 0x7278
-  __TEXT.__unwind_info: 0x910
-  __DATA_CONST.__auth_got: 0xe08
-  __DATA_CONST.__got: 0x198
+  __TEXT.__const: 0x618
+  __TEXT.__gcc_except_tab: 0xa74
+  __TEXT.__objc_methname: 0x15b8
+  __TEXT.__objc_classname: 0xf9
+  __TEXT.__objc_methtype: 0x3b5
+  __TEXT.__cstring: 0x282f
+  __TEXT.__oslogstring: 0x7581
+  __TEXT.__unwind_info: 0x930
+  __DATA_CONST.__auth_got: 0xe20
+  __DATA_CONST.__got: 0x190
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2570
+  __DATA_CONST.__const: 0x2618
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_nlclslist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__subsystem: 0x20
   __DATA_CONST.__object_init: 0x8
   __DATA.__objc_const: 0x1350
-  __DATA.__objc_selrefs: 0x5c8
-  __DATA.__objc_classrefs: 0xf0
-  __DATA.__objc_superrefs: 0x88
+  __DATA.__objc_selrefs: 0x5d0
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x430

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libcryptex_core.dylib
   - /usr/lib/libcryptex_interface.dylib
-  - /usr/lib/libimg4.dylib
+  - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 903
-  Symbols:   534
-  CStrings:  1450
+  Functions: 909
+  Symbols:   536
+  CStrings:  1530
 
Symbols:
+ __img4_chip_cryptex1_generic
+ _cryptex_core_image_authapfs_enabled
+ _img4_nonce_domain_get_from_handle
+ _objc_retain_x26
+ _pthread_rwlock_init
+ _pthread_rwlock_rdlock
+ _pthread_rwlock_unlock
+ _pthread_rwlock_wrlock
- _SMJobRemove
- _kSMDomainSystemLaunchd
- _kSMDomainUserLaunchd
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _os_variant_is_darwinos
CStrings:
+ "%s: AuthAPFS disabled because quire lacks an im4m."
+ "%s: AuthAPFS enabled, skip up-front dmg authentication."
+ "%s: Cryptex is missing a volume root hash."
+ "%s: Cryptex was never bootstrapped."
+ "%s: Disallow unbootstrap of quire with active dependent quires."
+ "%s: Disallow unbootstrap of system quire."
+ "%s: Failed to attach launch agent %s. for user id %d"
+ "%s: Failed to bootstrap agent: %s. %{darwin.errno}d"
+ "%s: Failed to bootstrap plist: %s. %{darwin.errno}d"
+ "%s: Failed to bootstrap quire contents."
+ "%s: Failed to bootstrap quire contents. %{darwin.errno}d"
+ "%s: Failed to bootstrap quire libraries. %{darwin.errno}d"
+ "%s: Failed to bootstrap quire."
+ "%s: Failed to bootstrap services."
+ "%s: Failed to load jetsam properties. %{darwin.errno}d"
+ "%s: Failed to load trust cache. %{darwin.errno}d"
+ "%s: Failed to read developer mode status %{darwin.errno}d"
+ "%s: Failed to unmount quire"
+ "%s: Installing cryptex %{public}s is disallowed because developer mode is not enabled."
+ "%s: Invalid combination of flags."
+ "%s: Mount path isn't absolute. %{darwin.errno}d"
+ "%s: _mkodtempat %{darwin.errno}d"
+ "%s: _opendir %{darwin.errno}d"
+ "%s: already mounted %{darwin.errno}d"
+ "%s: collation add %{darwin.errno}d"
+ "%s: collation remove %{darwin.errno}d"
+ "%s: detach %{darwin.errno}d"
+ "%s: failed to associate with forerunner"
+ "%s: failed to bootstrap astro content: %{darwin.errno}d"
+ "%s: failed to bootstrap service: %s."
+ "%s: failed to create symlink for %s %{darwin.errno}d"
+ "%s: failed to create trampoline for %s %{darwin.errno}d"
+ "%s: failed to create trampoline for %s under root %{darwin.errno}d"
+ "%s: failed to get abs path for %s %{darwin.errno}d"
+ "%s: failed to load trust cache %{darwin.errno}d"
+ "%s: forerunner not a block device: %s %{darwin.errno}d"
+ "%s: hdi_mount %{darwin.errno}d"
+ "%s: invalid value for key: %s: %@: %{darwin.errno}d"
+ "%s: launchagent bootstrap failed: %{darwin.errno}d"
+ "%s: mount [hdi]"
+ "%s: not currently mounted %{darwin.errno}d"
+ "%s: open forerunner device: %s %{darwin.errno}d"
+ "%s: open forerunner mount: %s %{darwin.errno}d"
+ "%s: open mount: %s %{darwin.errno}d"
+ "%s: quire bootstrap succeeded"
+ "%s: quire bootstrap: %s"
+ "%s: quire unbootstrap: %s"
+ "%s: realpath_np %{darwin.errno}d"
+ "%s: staging failed %{darwin.errno}d"
+ "%s: stat forerunner device: %s %{darwin.errno}d"
+ "%s: unmount %{darwin.errno}d"
+ "%s: using NO signing service"
+ "/Library/Caches/com.apple.xbs/Sources/libcryptex_executables/cryptexd/quire.c"
+ "/Library/Caches/com.apple.xbs/Sources/libcryptex_executables/cryptexd/sm/launchd_session.m"
+ "/Library/Caches/com.apple.xbs/Sources/libcryptex_executables/cryptexd/sm/sm.c"
+ "/Library/Caches/com.apple.xbs/Sources/libcryptex_executables/cryptexd/sub/sub_remote_service.m"
+ "/Library/Caches/com.apple.xbs/Sources/libcryptex_executables/hlutil/img4_xpc.m"
+ "369.100.36"
+ "@(#)VERSION:Darwin Cryptex Manager Version 2.0.0: Wed Feb 21 20:36:44 PST 2024; root:libcryptex_executables-369.100.36~292/cryptexd/RELEASE_ARM64E"
+ "Darwin Cryptex Manager Version 2.0.0: Wed Feb 21 20:36:44 PST 2024; root:libcryptex_executables-369.100.36~292/cryptexd/RELEASE_ARM64E"
+ "DeveloperModeRequired"
+ "Failed to add sm service to launchd."
+ "Failed to encode AppleImage4 chip instance.: %@"
+ "Failed to find targetDomain %d %{darwin.errno}d"
+ "Failed to initialize AppleImage4 chip instance. %{darwin.errno}d"
+ "Failed to start session %@: %{darwin.errno}d"
+ "Failed to submit job to launchd with error: %@ %{darwin.errno}d"
+ "Invalid chip instance."
+ "Library/Astro"
+ "Removed launchd job"
+ "Removing launchd job"
+ "_codex_unbootstrap_continue"
+ "_protex_stage_install_callback"
+ "_quire_attach_launch_agents"
+ "_quire_bootstrap_agents"
+ "_quire_bootstrap_astro"
+ "_quire_bootstrap_binary"
+ "_quire_bootstrap_contents"
+ "_quire_bootstrap_continue"
+ "_quire_bootstrap_diags"
+ "_quire_bootstrap_library"
+ "_quire_bootstrap_luacore_lib"
+ "_quire_bootstrap_python_lib"
+ "_quire_bootstrap_service"
+ "_quire_keybag_source_fire"
+ "_quire_mount_continue"
+ "_quire_mount_forerunner"
+ "_quire_mount_hdi"
+ "_quire_unbootstrap_continue"
+ "_quire_unmount_continue"
+ "_remote_service_get_nonce"
+ "_remote_service_read_personalization_identifiers"
+ "_remote_service_roll_nonce"
+ "astro libraries"
+ "bootstrap failed, unbootstrapping: %@"
+ "cferr"
+ "copy nonce failed %{darwin.errno}d"
+ "failed to frob plist: %@. %{darwin.errno}d"
+ "failed to get argv from request %{darwin.errno}d"
+ "forwarded unbootstrap [no error]"
+ "forwarded unbootstrap: %@"
+ "img4_chip_bord"
+ "img4_chip_cepo"
+ "img4_chip_chip"
+ "img4_chip_clas"
+ "img4_chip_cpro"
+ "img4_chip_csec"
+ "img4_chip_ecid"
+ "img4_chip_epro"
+ "img4_chip_esdm"
+ "img4_chip_esec"
+ "img4_chip_euou"
+ "img4_chip_fchp"
+ "img4_chip_fpgt"
+ "img4_chip_instance_to_xpc"
+ "img4_chip_iuou"
+ "img4_chip_omit"
+ "img4_chip_rsch"
+ "img4_chip_sdom"
+ "img4_chip_styp"
+ "img4_chip_type"
+ "initial cryptex bootstrap: %s [no error]"
+ "initial cryptex bootstrap: %s: %@"
+ "installation failed: %@"
+ "invalid plist. %{darwin.errno}d"
+ "launchd_session_add_job"
+ "nonce domain doesn't exist for handle: %u"
+ "nonce domain doesn't exist for index: %llu"
+ "nonce-domain-handle"
+ "quire mount: %s [no error]"
+ "quire mount: %s: %@"
+ "quire_bootstrap"
+ "read-personalization-id"
+ "remove:"
+ "required key missing or with wrong type: %s or %s"
+ "roll nonce failed %{darwin.errno}d"
+ "rw_lock"
+ "security.mac.amfi.developer_mode_status"
+ "sm_bootstrap_service"
+ "subsystem root paths (dependency mount points) exceed available space. %{darwin.errno}d"
+ "unbootstrap: %@"
+ "unmount [no error]"
+ "unmount: %@"
+ "using NO signing service"
+ "v24@?0^{_session_core={_os_object_header=^vii}{_object_proto=**^{os_log_s}}IqqQ^v^v^v***B}8^v16"
+ "{_opaque_pthread_rwlock_t=\"__sig\"q\"__opaque\"[192c]}"
+ "\xf0\xa2"
- "\x12"
- "%s: Attempted to add a Launch Agent that wasn't installed in a system cryptex."
- "%s: AuthAPFS disabled because quire lacks an im4m and/or a volume hash."
- "%s: Disallow unbootstrap of quire with active dependent quires.: %{darwin.errno}d"
- "%s: Disallow unbootstrap of system quire.: %{darwin.errno}d"
- "%s: Failed to bootstrap quire. %{darwin.errno}d"
- "%s: Failed to unmount quire %{darwin.errno}d"
- "%s: Invalid combination of flags.: %{darwin.errno}d"
- "%s: Mount path isn't absolute.: %{darwin.errno}d"
- "%s: _mkodtempat: %{darwin.errno}d"
- "%s: _opendir: %{darwin.errno}d"
- "%s: already mounted"
- "%s: bootstrap failed, unbootstrapping: %{darwin.errno}d"
- "%s: collation add: %{darwin.errno}d"
- "%s: collation remove: %{darwin.errno}d"
- "%s: detach: %{darwin.errno}d"
- "%s: failed to associate with forerunner: %{darwin.errno}d"
- "%s: failed to bootstrap launch agent: %{darwin.errno}d"
- "%s: failed to bootstrap service: %s: %{darwin.errno}d"
- "%s: failed to create symlink for %s: %{darwin.errno}d"
- "%s: failed to create trampoline for %s under root: %{darwin.errno}d"
- "%s: failed to create trampoline for %s: %{darwin.errno}d"
- "%s: failed to get abs path for %s: %{darwin.errno}d"
- "%s: forerunner not a block device: %s: %{darwin.errno}d"
- "%s: forwarded unbootstrap: %{darwin.errno}d"
- "%s: forwarded unbootstrap: success"
- "%s: hdi_mount: %{darwin.errno}d"
- "%s: initial cryptex bootstrap: %s: %{darwin.errno}d"
- "%s: initial cryptex bootstrap: %s: success"
- "%s: mount [hdi]: %{darwin.errno}d"
- "%s: not currently mounted"
- "%s: open forerunner device: %s: %{darwin.errno}d"
- "%s: open forerunner mount: %s: %{darwin.errno}d"
- "%s: open mount: %s: %{darwin.errno}d"
- "%s: quire bootstrap: %s: %{darwin.errno}d"
- "%s: quire bootstrap: %s: success"
- "%s: quire bootstrap: %{darwin.errno}d"
- "%s: quire bootstrap: success"
- "%s: quire mount: %s: %{darwin.errno}d"
- "%s: quire mount: %s: success"
- "%s: quire unbootstrap: %s: %{darwin.errno}d"
- "%s: quire unbootstrap: %s: success"
- "%s: staging failed: %{darwin.errno}d"
- "%s: stat forerunner device: %s: %{darwin.errno}d"
- "%s: unbootstrap: %{darwin.errno}d"
- "%s: unbootstrap: success"
- "%s: unmount: success"
- "369.60.3"
- "@(#)VERSION:Darwin Cryptex Manager Version 2.0.0: Wed Dec 20 22:33:47 PST 2023; root:libcryptex_executables-369.60.3~532/cryptexd/RELEASE_ARM64E"
- "Darwin Cryptex Manager Version 2.0.0: Wed Dec 20 22:33:47 PST 2023; root:libcryptex_executables-369.60.3~532/cryptexd/RELEASE_ARM64E"
- "Failed to submit job. %@"
- "SMJobSubmit: %s: %@"
- "_codex_rpc_install_continue2 context error: %{darwin.errno}d"
- "bootstrap failed, unbootstrapping: %{darwin.errno}d"
- "copy nonce failed: %{darwin.errno}d"
- "failed to frob plist: %@: %{darwin.errno}d"
- "installation failed: %{darwin.errno}d"
- "invalid plist"
- "lock"
- "nonce domain doesn't exist for index: %llu: %{darwin.errno}d"
- "plist too large: %lu bytes"
- "required key missing or with wrong type: %s"
- "roll nonce failed: %{darwin.errno}d"
- "subsystem root paths (dependency mount points) exceed available space"
- "unbootstrap: %{darwin.errno}d"
- "unexpected failure: cryptexd unsupported in this environment"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
