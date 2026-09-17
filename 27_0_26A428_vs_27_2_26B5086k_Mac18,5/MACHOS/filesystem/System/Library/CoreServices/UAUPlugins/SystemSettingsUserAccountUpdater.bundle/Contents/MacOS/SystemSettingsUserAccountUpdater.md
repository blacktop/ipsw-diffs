## SystemSettingsUserAccountUpdater

> `/System/Library/CoreServices/UAUPlugins/SystemSettingsUserAccountUpdater.bundle/Contents/MacOS/SystemSettingsUserAccountUpdater`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-2027.0.10.401.0
-  __TEXT.__text: 0x20f4
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0xc0
+2027.1.4.400.0
+  __TEXT.__text: 0x1418
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_stubs: 0x20
   __TEXT.__objc_methlist: 0x1ac
-  __TEXT.__const: 0x1a2
-  __TEXT.__cstring: 0x63
-  __TEXT.__oslogstring: 0x5b
-  __TEXT.__objc_methname: 0x275
+  __TEXT.__const: 0xba
+  __TEXT.__cstring: 0xd8
+  __TEXT.__oslogstring: 0x1ea
+  __TEXT.__objc_methname: 0x1f3
   __TEXT.__objc_classname: 0x6d
   __TEXT.__objc_methtype: 0xec
-  __TEXT.__constg_swiftt: 0x7c
-  __TEXT.__swift5_typeref: 0x87
-  __TEXT.__swift5_reflstr: 0x1c
-  __TEXT.__swift5_fieldmd: 0x44
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__const: 0x110
+  __TEXT.__constg_swiftt: 0x44
+  __TEXT.__swift5_typeref: 0x47
+  __TEXT.__swift5_reflstr: 0x12
+  __TEXT.__swift5_fieldmd: 0x28
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0xf8
+  __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x238
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__auth_ptr: 0x68
+  __DATA_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0x1e0
-  __DATA.__objc_selrefs: 0x110
+  __DATA.__objc_selrefs: 0xe8
   __DATA.__objc_data: 0xc8
-  __DATA.__data: 0x120
-  __DATA.__common: 0x10
+  __DATA.__data: 0x110
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/UAUPlugin.framework/Versions/A/UAUPlugin

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 39
-  Symbols:   60
-  CStrings:  65
+  Symbols:   50
+  CStrings:  64
 
Symbols:
+ _CFPreferencesCopyValue
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _geteuid
+ _getuid
+ _kCFPreferencesCurrentHost
+ _kCFPreferencesCurrentUser
+ _notify_post
+ _swift_bridgeObjectRelease_n
+ _swift_dynamicCast
+ _swift_once
- _NSURLIsDirectoryKey
- _NSURLIsReadableKey
- _OBJC_CLASS_$_NSBundle
- _OBJC_CLASS_$_NSTask
- ___stack_chk_fail
- ___stack_chk_guard
- __swiftEmptySetSingleton
- _dladdr
- _objc_opt_self
- _objc_retainAutoreleasedReturnValue
- _swift_arrayDestroy
- _swift_errorRelease
- _swift_errorRetain
- _swift_getErrorValue
- _swift_getForeignTypeMetadata
- _swift_getObjCClassFromMetadata
- _swift_getObjCClassMetadata
- _swift_getWitnessTable
- _swift_initStackObject
- _swift_setDeallocating
- _swift_willThrow
CStrings:
+ "PendingFullReindexToken"
+ "Wrote a reindex token for uid %{public}u but read back %{public}s; the request may not be visible to that user's agent."
+ "Wrote reindex token for uid %{public}u and posted the notification. Whether a pass runs is up to that user's agent."
+ "com.apple.Settings.SearchReindexRequest"
+ "com.apple.systemsettings.extensions"
+ "com.apple.systemsettings.search.reindexAll"
+ "notify_post('%{public}s') failed with status %{public}u; relying on the durable token."
+ "updateAccount() has effective uid 0 (real uid %{public}u); expected the per-user phase. Posting the notification without a durable token."
- "Error while running `settings`: %{public}s"
- "URLForResource:withExtension:"
- "`settings` tool was not found in %{public}s."
- "bundleURL"
- "com.apple.Settings"
- "com.apple.systempreferences"
- "initWithURL:"
- "launchedTaskWithExecutableURL:arguments:error:terminationHandler:"
- "mainBundle"
```
