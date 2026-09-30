## libLaunchServicesSupport.dylib

> `/usr/lib/libLaunchServicesSupport.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-1510.400.0.0.0
-  __TEXT.__text: 0x1fea0
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x454
-  __TEXT.__const: 0x150
-  __TEXT.__cstring: 0xc08
-  __TEXT.__oslogstring: 0x5be2
-  __TEXT.__gcc_except_tab: 0x2e7c
-  __TEXT.__objc_methname: 0xdcc
-  __TEXT.__objc_classname: 0x44
-  __TEXT.__objc_methtype: 0x220
-  __TEXT.__unwind_info: 0xb48
-  __DATA_CONST.__const: 0xee8
-  __DATA_CONST.__cfstring: 0xda0
-  __DATA_CONST.__objc_classlist: 0x18
+1517.0.1.401.0
+  __TEXT.__text: 0x20648
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_stubs: 0xfa0
+  __TEXT.__objc_methlist: 0x4cc
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0xc07
+  __TEXT.__oslogstring: 0x5e1b
+  __TEXT.__gcc_except_tab: 0x2ef4
+  __TEXT.__objc_methname: 0xe30
+  __TEXT.__objc_classname: 0x60
+  __TEXT.__objc_methtype: 0x25f
+  __TEXT.__unwind_info: 0xb98
+  __DATA_CONST.__const: 0xef8
+  __DATA_CONST.__cfstring: 0xde0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a8
-  __DATA_CONST.__auth_got: 0x648
-  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__objc_selrefs: 0x4d0
+  __DATA_CONST.__auth_got: 0x668
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x618
-  __DATA.__objc_classrefs: 0x98
-  __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x40
-  __DATA.__objc_data: 0xf0
+  __DATA.__objc_const: 0x738
+  __DATA.__objc_classrefs: 0xa0
+  __DATA.__objc_superrefs: 0x18
+  __DATA.__objc_ivar: 0x4c
+  __DATA.__objc_data: 0x140
   __DATA.__data: 0xe8
   __DATA.__bss: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libquit.dylib
-  Functions: 449
-  Symbols:   1169
-  CStrings:  629
+  Functions: 460
+  Symbols:   1208
+  CStrings:  648
 
Symbols:
+ +[NSMutableArrayNSErrorLocked new]
+ -[LSApplication setTracked:]
+ -[LSApplication tracked]
+ -[NSMutableArrayNSErrorLocked .cxx_destruct]
+ -[NSMutableArrayNSErrorLocked addError:]
+ -[NSMutableArrayNSErrorLocked addErrors:]
+ -[NSMutableArrayNSErrorLocked array]
+ -[NSMutableArrayNSErrorLocked init]
+ GCC_except_table100
+ GCC_except_table109
+ GCC_except_table122
+ GCC_except_table131
+ GCC_except_table135
+ GCC_except_table139
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table162
+ GCC_except_table169
+ GCC_except_table174
+ GCC_except_table179
+ GCC_except_table188
+ GCC_except_table189
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table193
+ GCC_except_table194
+ GCC_except_table195
+ GCC_except_table196
+ GCC_except_table197
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table27
+ GCC_except_table32
+ GCC_except_table37
+ GCC_except_table49
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table71
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table78
+ OBJC_IVAR_$_LSApplication._tracked
+ OBJC_IVAR_$_NSMutableArrayNSErrorLocked._array
+ OBJC_IVAR_$_NSMutableArrayNSErrorLocked._lock
+ _CFStringCreateWithFormat
+ _OBJC_CLASS_$_NSMutableArrayNSErrorLocked
+ _OBJC_METACLASS_$_NSMutableArrayNSErrorLocked
+ __OBJC_$_CLASS_METHODS_NSMutableArrayNSErrorLocked
+ __OBJC_$_INSTANCE_METHODS_NSMutableArrayNSErrorLocked
+ __OBJC_$_INSTANCE_VARIABLES_NSMutableArrayNSErrorLocked
+ __OBJC_$_PROP_LIST_NSMutableArrayNSErrorLocked
+ __OBJC_CLASS_RO_$_NSMutableArrayNSErrorLocked
+ __OBJC_METACLASS_RO_$_NSMutableArrayNSErrorLocked
+ __Z27applicationCopyParentASNRefPK7__LSASNb
+ __Z46applicationShouldNotBeConsideredAVisibleParentPK7__LSASN
+ __ZL28copyConcatenatedDescriptionsRKNSt3__16vectorIPKvNS_9allocatorIS2_EEEEPK10__CFStringSA_SA_
+ __ZL44scheduleCheckApplicationForExitedApplicationP13LSApplicationS0_
+ __ZL44scheduleCheckApplicationForExitedApplicationP13LSApplicationS0_d
+ __ZL44scheduleCheckApplicationForExitedApplicationPK7__LSASNP13LSApplicationd
+ ___LSForceQuitApplication_block_invoke_2
+ ___ZL44scheduleCheckApplicationForExitedApplicationP13LSApplicationS0__block_invoke
+ ____ZL44scheduleCheckApplicationForExitedApplicationP13LSApplicationS0__block_invoke
+ ____ZL44scheduleCheckApplicationForExitedApplicationP13LSApplicationS0_d_block_invoke
+ ____ZL44scheduleCheckApplicationForExitedApplicationPK7__LSASNP13LSApplicationd_block_invoke
+ ___block_descriptor_44_ea8_32s_e5_v8?0l
+ ___block_descriptor_48_ea8_32s40bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_48_ea8_32s40s_e19_"NSDictionary"8?0l
+ ___block_descriptor_48_ea8_32s_e5_v8?0l
+ ___block_descriptor_52_ea8_32s40s_e5_v8?0l
+ ___block_descriptor_60_ea8_32s40bs48c36_ZTS10CFReleaserIPK14__CFDictionaryE_e5_v8?0l
+ ___block_descriptor_60_ea8_32s40s48c36_ZTS10CFReleaserIPK14__CFDictionaryE_e5_v8?0l
+ ___block_descriptor_60_ea8_32s40s48s_e5_v8?0l
+ ___block_descriptor_69_ea8_32s40s48r56c29_ZTS10CFReleaserIP9__CFArrayE_e25_v32?0"NSNumber"8Q16^B24l
+ ___block_descriptor_76_ea8_32s40s48s56c30_ZTS10CFReleaserIPK9__CFArrayE64c36_ZTS10CFReleaserIPK14__CFDictionaryE_e18_v16?0^{__LSASN=}8l
+ ___copy_helper_block_ea8_32s40b48c36_ZTS10CFReleaserIPK14__CFDictionaryE
+ ___copy_helper_block_ea8_32s40s48c36_ZTS10CFReleaserIPK14__CFDictionaryE
+ ___copy_helper_block_ea8_32s40s48r56c29_ZTS10CFReleaserIP9__CFArrayE
+ ___copy_helper_block_ea8_32s40s48s
+ ___copy_helper_block_ea8_32s40s48s56c30_ZTS10CFReleaserIPK9__CFArrayE64c36_ZTS10CFReleaserIPK14__CFDictionaryE
+ ___destroy_helper_block_ea8_32s40s48c36_ZTS10CFReleaserIPK14__CFDictionaryE
+ ___destroy_helper_block_ea8_32s40s48r56c29_ZTS10CFReleaserIP9__CFArrayE
+ ___destroy_helper_block_ea8_32s40s48s
+ ___destroy_helper_block_ea8_32s40s48s56c30_ZTS10CFReleaserIPK9__CFArrayE64c36_ZTS10CFReleaserIPK14__CFDictionaryE
+ __kLSApplicationDisclaimAsParentApplicationKey
+ __kLSApplicationPossibleForegroundOwnerApplicationsASNsArrayKey
+ _dispatch_group_async
+ _dispatch_group_create
+ _dispatch_group_wait
+ _objc_msgSend$addError:
+ _objc_msgSend$addErrors:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$setTracked:
+ _objc_msgSend$tracked
- GCC_except_table102
- GCC_except_table103
- GCC_except_table107
- GCC_except_table108
- GCC_except_table124
- GCC_except_table126
- GCC_except_table127
- GCC_except_table130
- GCC_except_table142
- GCC_except_table145
- GCC_except_table146
- GCC_except_table150
- GCC_except_table158
- GCC_except_table159
- GCC_except_table173
- GCC_except_table182
- GCC_except_table28
- GCC_except_table29
- GCC_except_table33
- GCC_except_table34
- GCC_except_table39
- GCC_except_table63
- GCC_except_table65
- GCC_except_table72
- GCC_except_table75
- GCC_except_table76
- GCC_except_table88
- GCC_except_table91
- __Z27applicationCopyParentASNRefPK7__LSASN
- __ZL38informBTMAboutAStillRunningApplicationPK7__LSASNP5NSURLb
- __ZL44scheduleCheckApplicationForExitedApplicationP13LSApplication
- __ZL44scheduleCheckApplicationForExitedApplicationP13LSApplicationd
- ___ZL44scheduleCheckApplicationForExitedApplicationP13LSApplication_block_invoke
- ____Z13copySetStringPK7__CFSet_block_invoke
- ____Z15copyArrayStringPK9__CFArray_block_invoke
- ____ZL44scheduleCheckApplicationForExitedApplicationP13LSApplication_block_invoke
- ____ZL44scheduleCheckApplicationForExitedApplicationP13LSApplicationd_block_invoke
- ___block_descriptor_44_e5_v8?0l
- ___block_descriptor_48_ea8_32bs_e20_v20?0B8"NSError"12l
- ___block_descriptor_48_ea8_32s40s_e20_v20?0B8"NSError"12l
- ___block_descriptor_52_ea8_32s_e5_v8?0l
- ___block_descriptor_60_ea8_32bs48c36_ZTS10CFReleaserIPK14__CFDictionaryE_e5_v8?0l
- ___block_descriptor_60_ea8_32s40s_e5_v8?0l
- ___block_descriptor_68_ea8_32s48c30_ZTS10CFReleaserIPK9__CFArrayE_e18_v16?0^{__LSASN=}8l
- ___block_descriptor_69_ea8_32s40r56c29_ZTS10CFReleaserIP9__CFArrayE_e25_v32?0"NSNumber"8Q16^B24l
- ___copy_helper_block_8_32c31_ZTS10CFReleaserIP10__CFStringE
- ___copy_helper_block_ea8_32b48c36_ZTS10CFReleaserIPK14__CFDictionaryE
- ___copy_helper_block_ea8_32s40r56c29_ZTS10CFReleaserIP9__CFArrayE
- ___copy_helper_block_ea8_32s48c30_ZTS10CFReleaserIPK9__CFArrayE
- ___destroy_helper_block_8_32c31_ZTS10CFReleaserIP10__CFStringE
- ___destroy_helper_block_ea8_32s40r56c29_ZTS10CFReleaserIP9__CFArrayE
- ___destroy_helper_block_ea8_32s48c30_ZTS10CFReleaserIPK9__CFArrayE
- ___destroy_helper_block_ea8_32s48c36_ZTS10CFReleaserIPK14__CFDictionaryE
- __kLSApplicationHasAVisibleOwnerApplicationASNsArrayKey
CStrings:
+ ""
+ "%@%@"
+ "0x%llx-0x%llx \"%@\""
+ "@\"NSMutableArray\""
+ "NSMutableArrayNSErrorLocked"
+ "T@\"NSArray\",R,C"
+ "TB,N"
+ "["
+ "[["
+ "]"
+ "]]"
+ "_LSForceQuitApplication, bad block param (session=%x asn=%{public}@ options=%{public}@)"
+ "_LSForceQuitApplication, bad params (session=%x asn=%{public}@ options=%{public}@)"
+ "_LSForceQuitApplication: asn=%{public}@, timed out waiting for force quit of some child application in %{public}@"
+ "_array"
+ "_lock"
+ "_tracked"
+ "addError:"
+ "addErrors:"
+ "application: app=%{public}@ is non-visible but has a visible parent application %{public}@; will recheck again."
+ "applicationDeath: app=%{public}@ has died, is non-foreground and never tracked, so ignoring it from the application list."
+ "applicationDeath: app=%{public}@ is non-foreground application but is allowed to execute without visible UI because of its oslaunch job type."
+ "applicationDeath: app=%{public}@, had non-application coalition pids, %{public}@, but they all appear to have exited already."
+ "applicationDeath: app=%{public}@, has non-application coalition pids %{public}@, so this application stays in the running list."
+ "applicationDeath: app=%{public}@, has non-ignorable loaded jobs %{public}@, so not removing from the application list. "
+ "applicationDeath: app=%{public}@, has related coalition pids %{public}@, so this application stays in the running list."
+ "applicationDeath: app=%{public}@, subprocess %{public}@ is a UI element without a visible window, so scheduling checks in the future to see if we need to alert about it."
+ "applicationDeath: app=%{public}@, subprocess %{public}@ is entitled to run without UI so ignoring it for the purposes of whether this app should stay."
+ "applicationDeath: app=%{public}@, subprocess %{public}@ is non-foreground with a visible window, so scheduling the future to insure it continues to have a UI. "
+ "applicationDeath: app=%{public}@, subprocess %{public}@ is non-foreground/non-uielement without clear visibility, so scheduling another check. "
+ "arrayWithArray:"
+ "schedule: app=%{public}@ checking in %{public}g seconds to confirm it has completed exiting."
+ "schedule: app=%{public}@ has timed out, is still running, with responsible app=%{public}@ and so we should consult BTM for this application."
+ "schedule: app=%{public}@, responsible=%{public}@ unable to determine if this application is allowed to run in the background, error=%{public}@."
+ "schedule: app=%{public}@, responsible=%{public}@, is not allowed to run in background, so killing it and its subordinate proceses unconditionally."
+ "schedule: app=%{public}@, responsible=%{public}@, no longer being tracked."
+ "setTracked:"
+ "tracked"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- " ]"
- ", %@"
- "0x%llu-0x%llu \"%@\""
- "[ %@"
- "[ ]"
- "application: app=%{public}@ is non-foreground application but is allowed to execute without visible UI because of its oslaunch job type."
- "application: app=%{public}@ is non-visible but has a visible parent application; will recheck again."
- "application: app=%{public}@, had non-application coalition pids, %{public}@, but they all appear to have exited already."
- "application: app=%{public}@, has non-application coalition pids %{public}@, so this application stays in the running list."
- "application: app=%{public}@, has non-ignorable loaded jobs %{public}@, so not removing from the application list. "
- "application: app=%{public}@, has related coalition pids %{public}@, so this application stays in the running list."
- "application: app=%{public}@, subprocess %{public}@ is a UI element without a visible window, so scheduling checks in the future to see if we need to alert about it."
- "application: app=%{public}@, subprocess %{public}@ is entitled to run without UI so ignoring it for the purposes of whether this app should stay."
- "application: app=%{public}@, subprocess %{public}@ is non-foreground with a visible window, so scheduling the future to insure it continues to have a UI. "
- "application: app=%{public}@, subprocess %{public}@ is non-foreground/non-uielement without clear visibility, so scheduling another check. "
- "schedule: app=%{public}@ cheking in %{public}g seconds to confirm it has completed exiting."
- "schedule: app=%{public}@ has timed out, is still running, and so we should consult BTM for this application."
- "schedule: app=%{public}@ is not allowed to run in background, so killing it and its subordinate proceses unconditionally."
- "schedule: app=%{public}@ no longer being tracked."
- "schedule: app=%{public}@, unable to determine if this application is allowed to run in the background, error=%{public}@."
```
