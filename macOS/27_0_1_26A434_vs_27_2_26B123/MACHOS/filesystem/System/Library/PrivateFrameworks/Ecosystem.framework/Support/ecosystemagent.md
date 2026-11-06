## ecosystemagent

> `/System/Library/PrivateFrameworks/Ecosystem.framework/Support/ecosystemagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__info_plist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-56.0.0.0.0
-  __TEXT.__text: 0x40580
+59.3.0.0.0
+  __TEXT.__text: 0x40e0c
   __TEXT.__auth_stubs: 0x15e0
-  __TEXT.__objc_stubs: 0x8e0
+  __TEXT.__objc_stubs: 0x940
   __TEXT.__objc_methlist: 0x164
-  __TEXT.__const: 0x2e62
-  __TEXT.__cstring: 0x2bb6
+  __TEXT.__const: 0x2e72
+  __TEXT.__cstring: 0x2c16
   __TEXT.__swift5_typeref: 0xf86
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x1e5
-  __TEXT.__objc_methname: 0xce9
-  __TEXT.__objc_methtype: 0x2cf
+  __TEXT.__objc_methname: 0xd29
+  __TEXT.__objc_methtype: 0x2af
   __TEXT.__constg_swiftt: 0xdd8
   __TEXT.__swift5_reflstr: 0xb39
   __TEXT.__swift5_fieldmd: 0xebc
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_capture: 0x2c0
-  __TEXT.__oslogstring: 0x1121
+  __TEXT.__oslogstring: 0x1251
   __TEXT.__swift5_proto: 0x284
   __TEXT.__swift5_types: 0x104
   __TEXT.__swift_as_entry: 0x14

   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__info_plist: 0x3ec
-  __TEXT.__unwind_info: 0xf18
-  __TEXT.__eh_frame: 0xee0
-  __DATA_CONST.__const: 0x20e0
+  __TEXT.__unwind_info: 0xf28
+  __TEXT.__eh_frame: 0xf10
+  __DATA_CONST.__const: 0x2108
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__auth_got: 0xaf8
-  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__got: 0x380
   __DATA_CONST.__auth_ptr: 0x308
   __DATA.__objc_const: 0xbe0
-  __DATA.__objc_selrefs: 0x300
+  __DATA.__objc_selrefs: 0x318
   __DATA.__objc_data: 0x200
   __DATA.__data: 0x14a0
   __DATA.__common: 0x48

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1076
-  Symbols:   551
-  CStrings:  452
+  Functions: 1080
+  Symbols:   554
+  CStrings:  458
 
Symbols:
+ _$s10Foundation4DateV13distantFutureACvgZ
+ _$s10Foundation4DateV20timeIntervalSinceNowSdvg
+ _$sSis7CVarArgsWP
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSTimer
- _$sSo13os_log_type_ta0A0E4infoABvgZ
- _dispatch_main
CStrings:
+ "<PathParser> Could not create AppProxy for bundle ID %{public}s"
+ "<ecosystemd: PathParsers>: handleSanitizedPath: Path escapes /Applications/: %{public}s"
+ "<ecosystemd: PathParsers>: handleSanitizedPath: Unable to find: %{public}s"
+ "ecosystemagent: Added Rosetta app to cache: %{public}s (%{public}ld total)"
+ "ecosystemagent: Bundle no longer exists at %{public}s, pruning from results"
+ "ecosystemagent: Cache refresh complete (%{public}ld apps, unchanged)"
+ "ecosystemagent: Cache refresh complete (%{public}ld apps, was %{public}ld)"
+ "ecosystemagent: Daemon returned error: %{public}s"
+ "ecosystemagent: Rosetta app not in cache, extracting: %{public}s"
+ "ecosystemagent: Unknown action identifier: %{public}@"
+ "ecosystemagent: Updated lastOpenedDate for cached Rosetta app: %{public}s"
+ "ecosystemagent: [APPS_LIST] lsAppsSent=%{public}ld lsComplete=%{bool,public}d daemonReturned=%{public}ld prunedStale=%{public}ld returned=%{public}ld"
+ "ecosystemagent: [INIT] uiEnabled=%d mdmAllowed=%d userPrefEnabled=%d"
+ "ecosystemagent: ensureCached: app already cached at %{public}s, updating lastOpenedDate (was %{public}s)"
+ "ecosystemagent: ensureCached: cache has %{public}ld entries"
+ "ecosystemagent: ensureCached: could not extract app info for: %{public}s"
+ "ecosystemagent: ensureCached: path not in cache, matched by bundleID %{public}s → %{public}s"
+ "ecosystemagent: malformed customURL in notification userInfo: %{public}s"
+ "mainRunLoop"
+ "run"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "v16@?0@\"NSTimer\"8"
- "<PathParser> Could not create AppProxy for bundle ID %s"
- "<ecosystemd: PathParsers>: handleSanitizedPath: Path escapes /Applications/: %s"
- "<ecosystemd: PathParsers>: handleSanitizedPath: Unable to find: %s"
- "ecosystemagent: Added Rosetta app to cache: %s (%ld total)"
- "ecosystemagent: Bundle no longer exists at %s, pruning from results"
- "ecosystemagent: Cache refresh complete (%ld apps)"
- "ecosystemagent: Daemon returned %ld apps"
- "ecosystemagent: Daemon returned error: %s"
- "ecosystemagent: Rosetta app not in cache, extracting: %s"
- "ecosystemagent: Unknown action identifier: %@"
- "ecosystemagent: Updated lastOpenedDate for cached Rosetta app: %s"
- "ecosystemagent: ensureCached: app already cached at %s, updating lastOpenedDate (was %s)"
- "ecosystemagent: ensureCached: cache has %ld entries"
- "ecosystemagent: ensureCached: could not extract app info for: %s"
- "ecosystemagent: ensureCached: path not in cache, matched by bundleID %s → %s"
- "ecosystemagent: malformed customURL in notification userInfo: %s"
```
