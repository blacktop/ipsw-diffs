## cryptexd

> `/usr/libexec/cryptexd`

```diff

-493.122.1.0.0
-  __TEXT.__text: 0x4adf8
+589.0.1.0.0
+  __TEXT.__text: 0x4b7e8
   __TEXT.__auth_stubs: 0x1d30
   __TEXT.__objc_stubs: 0x1620
   __TEXT.__objc_methlist: 0x844

   __TEXT.__objc_methname: 0x1649
   __TEXT.__objc_classname: 0xf9
   __TEXT.__objc_methtype: 0x3c9
-  __TEXT.__cstring: 0x34e2
-  __TEXT.__oslogstring: 0x98ec
-  __TEXT.__unwind_info: 0xba0
+  __TEXT.__cstring: 0x34f6
+  __TEXT.__oslogstring: 0x9c7c
+  __TEXT.__unwind_info: 0xbb0
   __DATA_CONST.__auth_got: 0xea8
   __DATA_CONST.__got: 0x250
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x2a30
-  __DATA_CONST.__cfstring: 0x260
+  __DATA_CONST.__const: 0x2a50
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_nlclslist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
+  - /System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC
   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
+  - /System/Library/PrivateFrameworks/StorageKit.framework/StorageKit
   - /System/Library/PrivateFrameworks/WatchdogServiceManagement.framework/WatchdogServiceManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
+  - /usr/lib/libarchive.2.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libcryptex_core.dylib

   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: E4FC2F8A-C996-324F-956B-1E9E7807015A
+  UUID: BB56F214-168F-30FF-AA9C-EB5DB84CBD40
   Functions: 899
   Symbols:   564
-  CStrings:  1781
+  CStrings:  1797
 
CStrings:
+ "%{public}s: %s (%s) authentication [no error]"
+ "%{public}s: %s (%s) authentication: %@"
+ "%{public}s: %s authentication [no error]"
+ "%{public}s: %s authentication: %@"
+ "%{public}s: Allowing readwrite installation."
+ "%{public}s: Attempted to install cryptex as readwrite outside of internal OS.: %{darwin.errno}d"
+ "%{public}s: Bootstrap %{public}s [no error]"
+ "%{public}s: Bootstrap %{public}s: %@"
+ "%{public}s: Cannot install persist cryptexes as readwrite.: %{darwin.errno}d"
+ "%{public}s: Cryptex readwrite installation not permitted outside of internal OS."
+ "%{public}s: Signature metadata does not match cryptex. Was the wrong personalization ticket provided?: %@"
+ "%{public}s: Unbootstrap existing %{public}s [no error]"
+ "%{public}s: Unbootstrap existing %{public}s: %@"
+ "%{public}s: Unbootstrap trust cache [no error]"
+ "%{public}s: Unbootstrap trust cache: %@"
+ "%{public}s: Unregister jobs from watchdog [no error]"
+ "%{public}s: Unregister jobs from watchdog: %@"
+ "%{public}s: Unset 'jobs loaded' flag [no error]"
+ "%{public}s: Unset 'jobs loaded' flag: %@"
+ "%{public}s: _mkodtempat mntdirfd %{darwin.errno}d"
+ "%{public}s: _mkodtempat shdwdirfd %{darwin.errno}d"
+ "%{public}s: bootstrap failed, unbootstrapping: %@"
+ "%{public}s: failed to bootstrap astro content"
+ "%{public}s: failed to bootstrap diags"
+ "%{public}s: failed to bootstrap factory content"
+ "%{public}s: failed to bootstrap luacore libraries"
+ "%{public}s: failed to bootstrap python libraries"
+ "%{public}s: failed to unbootstrap agent: %s: %@"
+ "%{public}s: failed to unbootstrap service: %{public}s: %@"
+ "%{public}s: forwarded unbootstrap [no error]"
+ "%{public}s: forwarded unbootstrap: %@"
+ "%{public}s: handle resource [no error]"
+ "%{public}s: handle resource: %@"
+ "%{public}s: imported: %s [no error]"
+ "%{public}s: initial cryptex bootstrap: %s [no error]"
+ "%{public}s: initial cryptex bootstrap: %s: %@"
+ "%{public}s: installation failed; cleaning up quire: %@"
+ "%{public}s: iterate '%{public}s' resources for '%{public}s' view [no error]"
+ "%{public}s: iterate '%{public}s' resources for '%{public}s' view: %@"
+ "%{public}s: protex personalization [no error]"
+ "%{public}s: protex personalization: %@"
+ "%{public}s: quire mount: %s [no error]"
+ "%{public}s: quire unbootstrap: %s [no error]"
+ "%{public}s: quire unbootstrap: %s: %@"
+ "%{public}s: unbootstrap [no error]"
+ "%{public}s: unbootstrap: %@"
+ "%{public}s: uninstall [no error]"
+ "%{public}s: uninstall: %@"
+ "%{public}s: unmount [no error]"
+ "%{public}s: unmount: %@"
+ "589.0.1"
+ "@(#)VERSION:Darwin Cryptex Manager Version 2.0.0: Fri May 30 21:09:07 PDT 2025; root:libcryptex_executables-589.0.1~639/cryptexd/RELEASE_ARM64E"
+ "Darwin Cryptex Manager Version 2.0.0: Fri May 30 21:09:07 PDT 2025; root:libcryptex_executables-589.0.1~639/cryptexd/RELEASE_ARM64E"
+ "Library/Apple/System"
+ "Monitor event for %{public}@ (session: %{public}s)"
+ "Unbootstrap quire failed with error code %d, ignoring: %{darwin.errno}d"
+ "_quire_bootstrap_factory_content"
+ "realpath_np hdi_dmgfd: %{darwin.errno}d"
+ "realpath_np shdwfd: %{darwin.errno}d"
+ "shadow"
+ "shadow-path"
+ "shdw"
+ "shdwpath = %s"
- "%s (%s) authentication [no error]"
- "%s (%s) authentication: %@"
- "%s authentication [no error]"
- "%s authentication: %@"
- "%{public}s: Failed to read level of REM support. %{darwin.errno}d"
- "%{public}s: _mkodtempat %{darwin.errno}d"
- "%{public}s: failed to bootstrap astro content: %{darwin.errno}d"
- "%{public}s: failed to bootstrap diags: %{darwin.errno}d"
- "%{public}s: failed to bootstrap factory content %{darwin.errno}d"
- "%{public}s: failed to bootstrap luacore libraries: %{darwin.errno}d"
- "%{public}s: failed to bootstrap python libraries: %{darwin.errno}d"
- "%{public}s: failed to check SEP ratcheting support"
- "493.122.1"
- "@(#)VERSION:Darwin Cryptex Manager Version 2.0.0: Sun Apr 20 21:21:28 PDT 2025; root:libcryptex_executables-493.122.1~5/cryptexd/RELEASE_ARM64E"
- "Bootstrap %{public}s [no error]"
- "Bootstrap %{public}s: %@"
- "Darwin Cryptex Manager Version 2.0.0: Sun Apr 20 21:21:28 PDT 2025; root:libcryptex_executables-493.122.1~5/cryptexd/RELEASE_ARM64E"
- "Monitor event for %@ (session: %s)"
- "Signature metadata does not match cryptex. Was the wrong personalization ticket provided?: %@"
- "Unbootstrap existing %{public}s [no error]"
- "Unbootstrap existing %{public}s: %@"
- "Unbootstrap trust cache [no error]"
- "Unbootstrap trust cache: %@"
- "Unregister jobs from watchdog [no error]"
- "Unregister jobs from watchdog: %@"
- "Unset 'jobs loaded' flag [no error]"
- "Unset 'jobs loaded' flag: %@"
- "_quire_needs_sep_ratcheting"
- "failed to unbootstrap agent: %s: %@"
- "failed to unbootstrap service: %{public}s: %@"
- "forwarded unbootstrap [no error]"
- "forwarded unbootstrap: %@"
- "handle resource [no error]"
- "handle resource: %@"
- "imported: %s [no error]"
- "initial cryptex bootstrap: %s [no error]"
- "initial cryptex bootstrap: %s: %@"
- "installation failed; cleaning up quire: %@"
- "iterate '%{public}s' resources for '%{public}s' view [no error]"
- "iterate '%{public}s' resources for '%{public}s' view: %@"
- "protex personalization [no error]"
- "protex personalization: %@"
- "quire mount: %s [no error]"
- "quire unbootstrap: %s [no error]"
- "quire unbootstrap: %s: %@"
- "security.codesigning.config"
- "unmount [no error]"
- "unmount: %@"

```
