## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-240.5.2.0.0
-  __TEXT.__text: 0x1c27dc
+240.6.1.0.0
+  __TEXT.__text: 0x1c2c08
   __TEXT.__auth_stubs: 0x1f40
   __TEXT.__objc_methlist: 0x4d5c
-  __TEXT.__cstring: 0x2a1fb
+  __TEXT.__cstring: 0x2a246
   __TEXT.__const: 0x1af8
   __TEXT.__gcc_except_tab: 0x1f98
-  __TEXT.__oslogstring: 0x3524d
+  __TEXT.__oslogstring: 0x3535e
   __TEXT.__dlopen_cstrs: 0x5bd
   __TEXT.__unwind_info: 0x4468
   __TEXT.__objc_classname: 0x506
-  __TEXT.__objc_methname: 0x129b6
+  __TEXT.__objc_methname: 0x12a21
   __TEXT.__objc_methtype: 0x1c8b
   __TEXT.__objc_stubs: 0xb6c0
   __DATA_CONST.__got: 0xa18

   __AUTH_CONST.__auth_got: 0xfb8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x3b58
-  __AUTH_CONST.__cfstring: 0x177e0
-  __AUTH_CONST.__objc_const: 0x74d8
+  __AUTH_CONST.__cfstring: 0x17800
+  __AUTH_CONST.__objc_const: 0x74f8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x500
   __AUTH.__data: 0x510
-  __DATA.__objc_ivar: 0x754
+  __DATA.__objc_ivar: 0x758
   __DATA.__data: 0xf2c
   __DATA.__bss: 0x15d8
   __DATA.__common: 0x500

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 5917
-  Symbols:   19775
-  CStrings:  10149
+  Symbols:   19776
+  CStrings:  10153
 
Symbols:
+ -[MXNowPlayingAppManager populateNowPlayingAppStack:hostProcessAttributionBundleID:]
+ -[MXNowPlayingAppManager pushToNowPlayingAppStack:hostProcessAttributionBundleID:]
+ _OBJC_IVAR_$_MXNowPlayingAppManager.mNowPlayingAppHostProcessAttributionBundleID
+ _objc_msgSend$populateNowPlayingAppStack:hostProcessAttributionBundleID:
+ _objc_msgSend$pushToNowPlayingAppStack:hostProcessAttributionBundleID:
- -[MXNowPlayingAppManager populateNowPlayingAppStack:]
- -[MXNowPlayingAppManager pushToNowPlayingAppStack:]
- _objc_msgSend$populateNowPlayingAppStack:
- _objc_msgSend$pushToNowPlayingAppStack:
CStrings:
+ "-MXNowPlayingAppManager- %s: \t-------------------------- NowPlayingAppHostProcessAttributionBundleID Dictionary --------------------------"
+ "-MXNowPlayingAppManager- %s: Now Playing App HostProcessAttributionBundle on disk is NULL"
+ "-MXNowPlayingAppManager- %s: Pushing displayID='%{public}@' hostProcessAttributionBundleID='%{public}@' to NowPlayingAppStack, existing size = %lu, new size = %lu"
+ "-[MXNowPlayingAppManager pushToNowPlayingAppStack:hostProcessAttributionBundleID:]"
+ "22:35:19"
+ "Apr 13 2025"
+ "mNowPlayingAppHostProcessAttributionBundleID"
+ "nowPlayingAppHostProcessAttributionBundleID"
+ "populateNowPlayingAppStack:hostProcessAttributionBundleID:"
+ "pushToNowPlayingAppStack:hostProcessAttributionBundleID:"
- "-MXNowPlayingAppManager- %s: Pushing displayID='%{public}@' to NowPlayingAppStack, existing size = %lu, new size = %lu"
- "-[MXNowPlayingAppManager pushToNowPlayingAppStack:]"
- "02:13:36"
- "Apr  7 2025"
- "populateNowPlayingAppStack:"
- "pushToNowPlayingAppStack:"

```
