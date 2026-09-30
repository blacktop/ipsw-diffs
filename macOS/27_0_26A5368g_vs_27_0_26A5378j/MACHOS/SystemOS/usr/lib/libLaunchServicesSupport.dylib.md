## libLaunchServicesSupport.dylib

> `/usr/lib/libLaunchServicesSupport.dylib`

```diff

-  __TEXT.__text: 0x1d774
-  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__text: 0x1dea8
+  __TEXT.__auth_stubs: 0xc50
   __TEXT.__objc_stubs: 0xec0
   __TEXT.__objc_methlist: 0x3f4
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0xb8c
-  __TEXT.__oslogstring: 0x504a
-  __TEXT.__gcc_except_tab: 0x2a78
-  __TEXT.__objc_methname: 0xd8c
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0xbb0
+  __TEXT.__oslogstring: 0x5443
+  __TEXT.__gcc_except_tab: 0x2afc
+  __TEXT.__objc_methname: 0xd9c
   __TEXT.__objc_classname: 0x3d
   __TEXT.__objc_methtype: 0x1ff
-  __TEXT.__unwind_info: 0xa50
-  __DATA_CONST.__const: 0xe38
-  __DATA_CONST.__cfstring: 0xc20
+  __TEXT.__unwind_info: 0xa70
+  __DATA_CONST.__const: 0xe88
+  __DATA_CONST.__cfstring: 0xc80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x498
-  __DATA_CONST.__auth_got: 0x5f8
+  __DATA_CONST.__auth_got: 0x638
   __DATA_CONST.__got: 0x220
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x548

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libquit.dylib
-  Functions: 417
-  Symbols:   1197
-  CStrings:  688
+  Functions: 423
+  Symbols:   1214
+  CStrings:  704
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_classrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table10
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table154
+ GCC_except_table158
+ GCC_except_table162
+ GCC_except_table170
+ GCC_except_table171
+ GCC_except_table172
+ GCC_except_table32
+ GCC_except_table37
+ GCC_except_table42
+ GCC_except_table7
+ _CFStringAppend
+ _CFStringAppendFormat
+ _CFStringCreateCopy
+ _CFStringCreateMutable
+ _CFStringCreateMutableCopy
+ _CFStringFind
+ _CFStringFindAndReplace
+ __LSASNToUInt64
+ __Z13copySetStringPK7__CFSet
+ __Z15copyArrayStringPK9__CFArray
+ __Z20copyDictionaryStringPK14__CFDictionary
+ __Z41applicationSupportsSubordinateTerminationPK7__LSASN
+ __ZL38informBTMAboutAStillRunningApplicationP13LSApplicationb
+ __ZL38informBTMAboutAStillRunningApplicationPK7__LSASNP5NSURLb
+ ____Z13copySetStringPK7__CFSet_block_invoke
+ ____Z15copyArrayStringPK9__CFArray_block_invoke
+ ____ZL38informBTMAboutAStillRunningApplicationPK7__LSASNP5NSURLb_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_69_ea8_32s40r56c29_ZTS10CFReleaserIP9__CFArrayE_e25_v32?0"NSNumber"8Q16^B24l
+ ___copy_helper_block_8_32c31_ZTS10CFReleaserIP10__CFStringE
+ ___destroy_helper_block_8_32c31_ZTS10CFReleaserIP10__CFStringE
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
- GCC_except_table131
- GCC_except_table134
- GCC_except_table135
- GCC_except_table138
- GCC_except_table146
- GCC_except_table147
- GCC_except_table157
- GCC_except_table161
- GCC_except_table165
- GCC_except_table20
- GCC_except_table25
- GCC_except_table27
- GCC_except_table56
- GCC_except_table60
- GCC_except_table61
- GCC_except_table63
- __Z11arrayStringP7NSArray
- __Z11arrayStringPK9__CFArray
- __Z16dictionaryStringP12NSDictionary
- __Z16dictionaryStringPK14__CFDictionary
- __ZL38informBTMAboutAStillRunningApplicationPK7__LSASNP5NSURL
- ____Z11arrayStringP7NSArray_block_invoke
- ___block_descriptor_40_ea8_32s_e25_v32?0"NSObject"8Q16^B24l
- ___block_descriptor_77_ea8_32s40r56c29_ZTS10CFReleaserIP9__CFArrayE_e25_v32?0"NSNumber"8Q16^B24l
- _objc_msgSend$appendString:
CStrings:
+ ", %@"
+ "0x%llu-0x%llu \"%@\""
+ "NSSupportsSubordinateTermination"
+ "NULL"
+ "[ %@"
+ "[ ]"
+ "_LSForceQuitApplication: asn=%{public}@ killing coalition pid %{public}d (%{private}@)"
+ "applicationDeath: app=%{public}@ supported subordinate termination, so terminating all remaining subordinate processes now."
+ "applicationDeath: app=%{public}@ supports subordinate termination, so terminating all subordinate processes in %{public}g seconds."
+ "askBTM: app=%{public}@ is unknown to BTM, and so temporarily allowed to run in the background, because record not found."
+ "dateWithTimeIntervalSinceNow:"
+ "enableQuitReally: %{BOOL}d, log version %d."
+ "informBTM: Informing BTM about an application running without visible UI, app=%{public}@ url=%{private}@"
+ "informBTMAboutAStillRunningApplication: app=%{public}@ no longer being tracked, so it must have exited."
+ "informBTMAboutAStillRunningApplication: app=%{public}@ still running."
+ "informBTMAboutAStillRunningApplication: app=%{public}@, currently has a visible window or context, so no longer need to track."
+ "informBTMAboutAStillRunningApplication: app=%{public}@, deferring check for %{public}g seconds until %{public}@"
+ "informBTMAboutAStillRunningApplication: app=%{public}@, entitled to run without ui so no longer need to track."
+ "informBTMAboutAStillRunningApplication: app=%{public}@, has exited but with remaining subprocesses."
+ "informBTMAboutAStillRunningApplication: app=%{public}@, running foreground so no longer need to track."
- "\"%@ \"%@\""
- "_LSForceQuitApplication: killing coalition %{public}lld pid %{public}@"
- "appendString:"
- "askBTM: app=%{public}@ is allowed to run in the background by BTM, because record not found."
- "enableQuitReally: %{BOOL}d"
- "informBTM: Informing BTM about an application which has left subordinate processes or jobs running, app=%{public}@ url=%{private}@"
- "v32@?0@\"NSObject\"8Q16^B24"

```
