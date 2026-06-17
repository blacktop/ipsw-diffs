## com.apple.security.quarantine

> `com.apple.security.quarantine`

```diff

-215.0.0.501.1
+196.160.2.0.0
   __TEXT.__const: 0x71 sha256:96cfcddf2aacb10150f499632ed05bb22cdcae128fe9dee0c99b3d77920073f3
-  __TEXT.__cstring: 0x7e6 sha256:da80863779a3c8f011d911ade53b812a3ccf4a8e4d80f2e25723b5fd93ea4d72
-  __TEXT.__os_log: 0x3ba sha256:10fb562a182d8275b8f90b9379d6980ae911c963f09db8e35251d0788b36b5da
-  __TEXT_EXEC.__text: 0x98f8 sha256:f8c15c866ec4b0e053baadbd8e7943246b7d07ececc2327e95fbe840b9b1d2df
+  __TEXT.__cstring: 0x649 sha256:72f38f61f3853d48334fdadf89ad24fb5de91da228b2265e9031700b9a4a181c
+  __TEXT.__os_log: 0x2a7 sha256:a77d4bf960fcb149452ea156d9c23ffdee723de76729b3f8a2b54466b6c75db7
+  __TEXT_EXEC.__text: 0x8d88 sha256:030454fbebe5a5ab1bc169b0e0481b29361b525c5cde32b1a038b6406eb939f2
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xcfb sha256:ec7eddf99b0ab1238e894bdf912f93c8ee3779a1fa041b6b349deb5e240da144
+  __DATA.__data: 0xcc3 sha256:397dd1d609da33e203a2ad3738cb7a161b9a65c1d0f63a71e83a6b83c6d1f5eb
   __DATA.__common: 0x24 sha256:6db65fd59fd356f6729140571b5bcd6bb3b83492a16e1bf0a3884442fc3c8a0e
-  __DATA.__bss: 0x348 sha256:16d0edc8b7ad7705b23a14058f366ff1c0dfa16a0ad14f741924c308754cf8d1
-  __DATA_CONST.__const: 0xc8 sha256:344b55c61aabd95ac3218d6ed6a0560ea3974a201e82b831a09bc4b8cb0606f0
-  __DATA_CONST.__kalloc_type: 0x280 sha256:9724b765dca7ff6a12060e36fc75f6f82680bc2ffcd22dd76ad20645ce559f93
-  __DATA_CONST.__auth_got: 0x480 sha256:7b0e7c7af62671eca42bb5566dc23cb3832996915e93692c6456ccfecbeed6e3
-  __DATA_CONST.__got: 0x58 sha256:b144a2e82cf800c0a854fd7127449868d7a1a50376a24d1f887b2e6b661fa089
-  UUID: 95952C34-B29F-340E-BE8B-569AA78FF654
-  Functions: 143
-  Symbols:   422
-  CStrings:  109
+  __DATA.__bss: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
+  __DATA_CONST.__auth_got: 0x430 sha256:f131c60322c90d2b40c2043b664b5631a890872348a5bab292b5a1df516bba2e
+  __DATA_CONST.__got: 0x48 sha256:55d0109c7da4e999971253ec0fce2adb86e686fd741f2d970c95b9f7f9218147
+  __DATA_CONST.__const: 0xc8 sha256:fdd97d26987ed53c924f77afc37d77218dd95a5a4caca9a65e5fdf5ae42aeb6d
+  __DATA_CONST.__kalloc_type: 0x280 sha256:0918f653ada7c2ae5a669f36cd5156efdfe0056b6e57b5d47fad0621e27c8417
+  UUID: 39C40DB4-120D-3C91-B9CC-91511EBB3AC2
+  Functions: 137
+  Symbols:   388
+  CStrings:  83
 
Symbols:
+ __block_descriptor_tmp.68
+ cred_label_alloc.kalloc_type_view_889
+ cred_label_destroy.kalloc_type_view_976
+ hook_vnode_notify_swap._os_log_fmt.55
+ identity_alloc.kalloc_type_view_366
+ identity_destroy.kalloc_type_view_401
+ qtnstate_alloc.kalloc_type_view_176
+ qtnstate_destroy.kalloc_type_view_281
+ responsibility_alloc.kalloc_type_view_780
+ responsibility_destroy.kalloc_type_view_851
+ responsibility_set._os_log_fmt
+ responsibility_set.cold.2
+ responsibility_set.cold.3
+ syscall_responsibility_set._os_log_fmt.65
- __ZL22core_analytics_service
- __ZL29attach_core_analytics_servicePvS_P9IOServiceP10IONotifier
- __ZN12OSDictionary12withCapacityEj
- __ZN16CoreAnalyticsHub22analyticsSendEventLazyEP8OSStringP8OSObject
- __ZN16CoreAnalyticsHub9metaClassE
- __ZN8OSString11withCStringEPKc
- __ZN9IOService23addMatchingNotificationEPK8OSSymbolP12OSDictionaryPFbPvS5_PS_P10IONotifierES5_S5_i
- __ZZ14analytics_initE11_os_log_fmt
- __ZZ39send_security_policy_mismatch_analyticsE11_os_log_fmt
- __ZZ39send_security_policy_mismatch_analyticsE11_os_log_fmt_0
- __ZZ39send_security_policy_mismatch_analyticsE11_os_log_fmt_1
- __ZZ39send_security_policy_mismatch_analyticsE11_os_log_fmt_2
- __ZZ39send_security_policy_mismatch_analyticsE11_os_log_fmt_3
- __ZZ39send_security_policy_mismatch_analyticsE11_os_log_fmt_4
- __ZZL29attach_core_analytics_servicePvS_P9IOServiceP10IONotifierE11_os_log_fmt
- __block_descriptor_tmp.74
- __responsibility_set
- _analytics_init
- _current_proc
- _gIOPublishNotification
- _hook_proc_notify_exit
- _identity_cache
- _identity_cache_lock
- _is_string_in_list
- _lck_mtx_init
- _lck_mtx_lock
- _lck_mtx_unlock
- _responsibility_set._os_log_fmt
- _responsibility_set.cold.1
- _responsibility_set.cold.2
- _send_security_policy_mismatch_analytics
- _strlcat
- _strncasecmp
- cred_label_alloc.kalloc_type_view_945
- cred_label_destroy.kalloc_type_view_1032
- hook_policy_syscall.cold.23
- hook_policy_syscall.cold.24
- hook_proc_notify_exit.cold.1
- hook_vnode_notify_swap._os_log_fmt.61
- identity_alloc.kalloc_type_view_422
- identity_cache_update.index
- identity_destroy.kalloc_type_view_457
- qtnstate_alloc.kalloc_type_view_232
- qtnstate_destroy.kalloc_type_view_337
- responsibility_alloc.kalloc_type_view_836
- responsibility_destroy.kalloc_type_view_907
- should_collect_policy_mismatch_analytics_for_signing_id.signing_ids
- syscall_responsibility_set._os_log_fmt.71
CStrings:
+ "%s[%lu] Unable to quarantine `%s': %d (error suppressed)"
+ "responsibility for %s[%u] set to that of %s[%u]: %s"
- "%s: failed set bundle subpath"
- "%s: failed to get path: %{darwin.errno}d"
- "%s: failed to set policy"
- "%s: failed to set process name"
- "%s: failed to set process signing id"
- "%s: failed to set result"
- "%s[%d] unable to quarantine '%s': %d (error suppressed)"
- ".app"
- "/"
- "/usr/bin/osascript"
- "CoreAnalyticsHub"
- "bundleSubpath"
- "com.apple.ClassKit.pdtool"
- "com.apple.CloudDocs.iCloudDriveFileProvider"
- "com.apple.CloudDocs.iCloudDriveFileProviderManaged"
- "com.apple.Safari"
- "com.apple.WorkflowKit.BackgroundShortcutRunner"
- "com.apple.nsurlsessiond"
- "com.apple.osascript"
- "com.apple.quarantine.SecurityPolicyMismatch"
- "failed to allocate IOKit matching directory for %s"
- "failed to attach core analytics service"
- "policy"
- "processName"
- "processSigningId"
- "responsibility for %s[%u] set to that of %s[%u]"
- "result"
- "send_security_policy_mismatch_analytics"

```
