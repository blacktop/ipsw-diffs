## searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

```diff

-  __TEXT.__text: 0x61854
-  __TEXT.__auth_stubs: 0x18c0
-  __TEXT.__objc_stubs: 0xa7c0
-  __TEXT.__objc_methlist: 0x2b38
+  __TEXT.__text: 0x61b60
+  __TEXT.__auth_stubs: 0x1910
+  __TEXT.__objc_stubs: 0xa800
+  __TEXT.__objc_methlist: 0x2b40
   __TEXT.__const: 0x23c
-  __TEXT.__cstring: 0x523b
-  __TEXT.__objc_methname: 0xae8e
+  __TEXT.__cstring: 0x52a2
+  __TEXT.__objc_methname: 0xaebe
   __TEXT.__objc_classname: 0x42e
   __TEXT.__objc_methtype: 0x1822
-  __TEXT.__oslogstring: 0x3663
+  __TEXT.__oslogstring: 0x37a3
   __TEXT.__gcc_except_tab: 0x5344
-  __TEXT.__unwind_info: 0xeb8
-  __DATA_CONST.__const: 0x1f88
-  __DATA_CONST.__cfstring: 0x4ae0
+  __TEXT.__unwind_info: 0xec8
+  __DATA_CONST.__const: 0x1fa8
+  __DATA_CONST.__cfstring: 0x4b00
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arrayobj: 0x120
-  __DATA_CONST.__auth_got: 0xc78
-  __DATA_CONST.__got: 0x11a0
+  __DATA_CONST.__auth_got: 0xca0
+  __DATA_CONST.__got: 0x11d8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x7d10
-  __DATA.__objc_selrefs: 0x3010
+  __DATA.__objc_selrefs: 0x3020
   __DATA.__objc_ivar: 0x384
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x670

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1231
-  Symbols:   975
-  CStrings:  3955
+  Functions: 1238
+  Symbols:   982
+  CStrings:  3964
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _SSAppExclusionsEnabled
+ _SSCopyTCCDisabledBundlesForSiriAccess
+ _SSSubscribeTCCEventsForSiriAccess
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
CStrings:
+ "DisabledBundlesFromSiriTCC"
+ "SSCopyTCCDisabledBundlesForSiriAccess returned nil; feature flag disabled or tccd temporarily unavailable — preserving existing CFPreferences cache"
+ "SSSubscribeTCCEventsForSiriAccess failed to arm — TCC changes will not propagate to search filter this session"
+ "_setupTCCSubscription"
+ "com.apple.searchd.tcc-prefs-write"
+ "com.apple.spotlight.tcc.siriAccessChanged"
+ "notify_post(kSSSiriAccessChangedNotification) failed: %u"
+ "sortedArrayUsingSelector:"

```
