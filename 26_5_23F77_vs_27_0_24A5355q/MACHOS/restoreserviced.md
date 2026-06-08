## restoreserviced

> `/usr/libexec/restoreserviced`

```diff

 46.0.0.0.0
-  __TEXT.__text: 0x14230
-  __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_stubs: 0x17a0
-  __TEXT.__objc_methlist: 0xcc4
+  __TEXT.__text: 0x142ec
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_stubs: 0x17c0
+  __TEXT.__objc_methlist: 0xcdc
   __TEXT.__const: 0xb7c
-  __TEXT.__cstring: 0x799b
+  __TEXT.__cstring: 0x7cf3
   __TEXT.__oslogstring: 0x3a5
-  __TEXT.__gcc_except_tab: 0x204
-  __TEXT.__objc_methname: 0x1823
+  __TEXT.__gcc_except_tab: 0x1ac
+  __TEXT.__objc_methname: 0x1865
   __TEXT.__objc_classname: 0x10f
-  __TEXT.__objc_methtype: 0x789
-  __TEXT.__unwind_info: 0x570
-  __DATA_CONST.__auth_got: 0x740
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0xcb8
-  __DATA_CONST.__cfstring: 0x3aa0
+  __TEXT.__objc_methtype: 0x77c
+  __TEXT.__unwind_info: 0x540
+  __DATA_CONST.__const: 0xcd8
+  __DATA_CONST.__cfstring: 0x3fe0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x770
+  __DATA_CONST.__got: 0x180
   __DATA.__objc_const: 0x1370
-  __DATA.__objc_selrefs: 0x740
+  __DATA.__objc_selrefs: 0x758
   __DATA.__objc_ivar: 0xe4
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x648
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A69D75ED-E5DC-32A5-9F00-47E69BE2BFD2
-  Functions: 554
-  Symbols:   290
-  CStrings:  1900
+  UUID: 32000E59-3808-3C89-83B6-A85589E1FA45
+  Functions: 549
+  Symbols:   292
+  CStrings:  1990
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x27
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x21
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x8
- _OBJC_CLASS_$_NSFileManager
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSURL
- ___NSArray0__
- _objc_retain_x20
- _objc_retain_x22
CStrings:
+ "%@:%@"
+ "40A0DDD2-77F8-4392-B4A3-1E7304206516"
+ "B48@0:8*16^{__CFDictionary=}24@32^^{__CFError}40"
+ "IODTNVRAMVariables"
+ "IONameMatch"
+ "IS"
+ "NOT"
+ "SystemAudioVolume"
+ "SystemAudioVolumeExtension"
+ "boot-args"
+ "boot-volume"
+ "bootdelay"
+ "chassis-disable-throttle"
+ "chassis-platform-id"
+ "chassis-slot-id"
+ "debug-uarts"
+ "iboot-failure-reason"
+ "options-system"
+ "ota-brain-version"
+ "ota-breadcrumbs"
+ "ota-context"
+ "ota-controllerVersion"
+ "ota-failure-reason"
+ "ota-forced-reset-uptime"
+ "ota-initial-failure-reason"
+ "ota-initial-forced-reset-uptime"
+ "ota-initial-result"
+ "ota-install-tonight"
+ "ota-reboot-retry-enabled"
+ "ota-result"
+ "ota-retry-failure-reason"
+ "ota-retry-result"
+ "ota-snapshot-update"
+ "ota-updateType"
+ "ramrod-kickstart-aces"
+ "ramrod_NVRAM_has_system_namespace: system namespace %s present\n"
+ "recovery-boot-mode"
+ "recovery-breadcrumbs"
+ "removeAllObjects"
+ "restore-retry-enabled"
+ "restored-host-timeout"
+ "root-live-fs"
+ "snap-provisional-nonces"
+ "snap-supports-precommit"
+ "supportsProvisionalNonces"
+ "supportsiBootPrecommit"
+ "target-uuid"
+ "update-volume"
+ "upgrade-fallback-boot-command"
+ "upgrade-manifest-hash"
- "%s: segment_data_array failed to allocate"
- "B48@0:8*16^{__CFDictionary=}24r^^{__CFArray}32^^{__CFError}40"

```
