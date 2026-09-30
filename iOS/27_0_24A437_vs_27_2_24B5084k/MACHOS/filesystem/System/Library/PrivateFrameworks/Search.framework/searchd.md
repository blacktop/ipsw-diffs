## searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2459.105.0.0.0
-  __TEXT.__text: 0x60b00
-  __TEXT.__auth_stubs: 0x18c0
-  __TEXT.__objc_stubs: 0xa7a0
-  __TEXT.__objc_methlist: 0x2b38
+2465.1.2.0.0
+  __TEXT.__text: 0x60d90
+  __TEXT.__auth_stubs: 0x1900
+  __TEXT.__objc_stubs: 0xa7e0
+  __TEXT.__objc_methlist: 0x2b40
   __TEXT.__const: 0x23c
-  __TEXT.__cstring: 0x523b
-  __TEXT.__objc_methname: 0xae91
+  __TEXT.__cstring: 0x52a2
+  __TEXT.__objc_methname: 0xaec1
   __TEXT.__objc_classname: 0x42e
   __TEXT.__objc_methtype: 0x1822
-  __TEXT.__oslogstring: 0x3663
+  __TEXT.__oslogstring: 0x37a3
   __TEXT.__gcc_except_tab: 0x5344
-  __TEXT.__unwind_info: 0x1210
-  __DATA_CONST.__const: 0x1f88
-  __DATA_CONST.__cfstring: 0x4ae0
+  __TEXT.__unwind_info: 0x1230
+  __DATA_CONST.__const: 0x1fa8
+  __DATA_CONST.__cfstring: 0x4b00
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arrayobj: 0x120
-  __DATA_CONST.__auth_got: 0xc78
-  __DATA_CONST.__got: 0x11c8
+  __DATA_CONST.__auth_got: 0xc98
+  __DATA_CONST.__got: 0x11e0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x7d10
-  __DATA.__objc_selrefs: 0x3008
+  __DATA.__objc_selrefs: 0x3018
   __DATA.__objc_ivar: 0x384
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x670

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1231
-  Symbols:   975
-  CStrings:  3324
+  Functions: 1238
+  Symbols:   981
+  CStrings:  3332
 
Symbols:
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _SSAppExclusionsEnabled
+ _SSCopyTCCDisabledBundlesForSiriAccess
+ _SSSubscribeTCCEventsForSiriAccess
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
- _MGGetProductType
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
