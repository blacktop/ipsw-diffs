## systemsettingsagent

> `/System/Applications/System Settings.app/Contents/Resources/systemsettingsagent`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_selrefs`

```diff

-2027.0.10.401.0
-  __TEXT.__text: 0x10564
-  __TEXT.__auth_stubs: 0xa10
+2027.1.4.400.0
+  __TEXT.__text: 0x1187c
+  __TEXT.__auth_stubs: 0xa20
   __TEXT.__objc_stubs: 0x1e0
-  __TEXT.__const: 0x3de
-  __TEXT.__cstring: 0x536
-  __TEXT.__swift5_typeref: 0x169
-  __TEXT.__objc_methtype: 0x2a
-  __TEXT.__swift5_capture: 0xbc
-  __TEXT.__oslogstring: 0xbdb
+  __TEXT.__const: 0x4c8
+  __TEXT.__cstring: 0x586
+  __TEXT.__swift5_typeref: 0x17a
+  __TEXT.__objc_methtype: 0x21
+  __TEXT.__swift5_capture: 0xd0
+  __TEXT.__oslogstring: 0xe3b
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1d8
-  __TEXT.__swift5_reflstr: 0x1dc
-  __TEXT.__swift5_fieldmd: 0x160
-  __TEXT.__swift5_types: 0x14
+  __TEXT.__constg_swiftt: 0x244
+  __TEXT.__swift5_reflstr: 0x23f
+  __TEXT.__swift5_fieldmd: 0x1ac
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift5_proto: 0xc
   __TEXT.__objc_classname: 0x2b
-  __TEXT.__objc_methname: 0x1ea
-  __TEXT.__swift5_proto: 0x8
+  __TEXT.__objc_methname: 0x24a
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__unwind_info: 0x358
-  __TEXT.__eh_frame: 0x370
-  __DATA_CONST.__const: 0x678
+  __TEXT.__unwind_info: 0x370
+  __TEXT.__eh_frame: 0x398
+  __DATA_CONST.__const: 0x720
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x510
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__auth_ptr: 0xb0
-  __DATA.__objc_const: 0x218
+  __DATA_CONST.__auth_got: 0x518
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__auth_ptr: 0xc0
+  __DATA.__objc_const: 0x278
   __DATA.__objc_selrefs: 0x78
-  __DATA.__data: 0x320
+  __DATA.__data: 0x388
   __DATA.__common: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 213
-  Symbols:   250
-  CStrings:  126
+  Functions: 220
+  Symbols:   253
+  CStrings:  137
 
Symbols:
+ _$s12SettingsHost0A13SearchIndexerC13IndexingErrorO18indexingIncompleteyAESS_S4itcAEmFWC
+ _$s12SettingsHost0A13SearchIndexerC13IndexingErrorOMa
+ _$ss5ErrorMp
CStrings:
+ "AppIntent indexing incomplete for %{public}s: processed %{public}ld, incomplete %{public}ld, severe %{public}ld, important %{public}ld"
+ "Claiming full-reindex request token"
+ "Full reindex requested via %{public}s"
+ "Full-reindex request already being served; not starting another pass"
+ "Index already in progress; merged into the pending request (force: %{bool}d, targeted: %{bool}d)"
+ "Pass did not satisfy its full-reindex request; leaving the token for a retry"
+ "Pass served its full-reindex request; clearing the token"
+ "PendingFullReindexToken"
+ "Processing the pending indexing request (force: %{bool}d, targeted: %{bool}d)"
+ "Running as role account, so skip the startup drain."
+ "Running as uid %u; is role account: %{bool}d"
+ "Starting indexing (force: %{bool}d, targeted: %{bool}d, servingRequestToken: %{bool}d, indexingCS now locked)"
+ "com.apple.systemsettings.search.reindexAll"
+ "fullReindexRequests"
+ "inFlightRequestToken"
+ "pendingReindex"
+ "pendingRequestToken"
- "Checking user ID: %u"
- "Index already in progress, queuing request (queue depth: %ld)"
- "Is role account: %{bool}d"
- "Processing queued indexing request (remaining in queue: %ld)"
- "Starting indexing (force: %{bool}d, targeted: %{bool}d, indexingCS now locked)"
- "indexCSRequests"
```
