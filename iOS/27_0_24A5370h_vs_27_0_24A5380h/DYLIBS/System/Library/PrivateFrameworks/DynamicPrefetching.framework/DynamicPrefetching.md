## DynamicPrefetching

> `/System/Library/PrivateFrameworks/DynamicPrefetching.framework/DynamicPrefetching`

```diff

-  __TEXT.__text: 0x17fe4
+  __TEXT.__text: 0x18abc
   __TEXT.__objc_methlist: 0x29c
-  __TEXT.__const: 0x4ae
-  __TEXT.__gcc_except_tab: 0x11f4
-  __TEXT.__cstring: 0x86c
-  __TEXT.__oslogstring: 0x24ea
-  __TEXT.__unwind_info: 0x830
+  __TEXT.__const: 0x4b6
+  __TEXT.__gcc_except_tab: 0x12ec
+  __TEXT.__cstring: 0x87e
+  __TEXT.__oslogstring: 0x2774
+  __TEXT.__unwind_info: 0x868
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0x310
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__auth_got: 0x3c0
+  __AUTH_CONST.__auth_got: 0x3f0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0xe8
-  __DATA.__bss: 0x228
+  __DATA.__bss: 0x248
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 483
-  Symbols:   169
-  CStrings:  271
+  Functions: 492
+  Symbols:   175
+  CStrings:  281
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
+ _localtime_r
+ _objc_retain_x21
+ _stat
+ _strftime
+ _utimensat
CStrings:
+ "%Y-%m-%d %H:%M:%S"
+ "end_scenario_internal: first launch after boot for bundleid %@ scenario %s — discarded %zu pageins, refreshed profile mtime"
+ "is_first_launch_after_boot: boot time unavailable, discarding pageins"
+ "mark_profile_seen_this_boot: Caught exception for bundleid %{public}s : %{public}s"
+ "mark_profile_seen_this_boot: Caught unknown exception for bundleid %{public}s"
+ "mark_profile_seen_this_boot: exists() failed for \"%s\": %{public}s"
+ "mark_profile_seen_this_boot: utimensat failed for \"%s\": %{darwin.errno}d"
+ "system_boot_time: boot time %lld.%09lld (epoch s)"
+ "system_boot_time: boot time %{public}s"
+ "system_boot_time: sysctl(KERN_BOOTTIME) failed: %{darwin.errno}d"

```
