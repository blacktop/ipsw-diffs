## systemsettingsagent

> `/System/Applications/System Settings.app/Contents/Resources/systemsettingsagent`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-2027.0.3.0.0
-  __TEXT.__text: 0xc5b4
-  __TEXT.__auth_stubs: 0x900
+2027.0.6.400.0
+  __TEXT.__text: 0x10c88
+  __TEXT.__auth_stubs: 0xa00
   __TEXT.__objc_stubs: 0x1e0
-  __TEXT.__const: 0x2b2
-  __TEXT.__cstring: 0x486
-  __TEXT.__swift5_typeref: 0x100
-  __TEXT.__objc_methtype: 0x21
-  __TEXT.__swift5_capture: 0xc8
-  __TEXT.__oslogstring: 0xa8b
+  __TEXT.__const: 0x3de
+  __TEXT.__cstring: 0x506
+  __TEXT.__swift5_typeref: 0x169
+  __TEXT.__objc_methtype: 0x2a
+  __TEXT.__swift5_capture: 0xbc
+  __TEXT.__oslogstring: 0xbcb
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x180
-  __TEXT.__swift5_reflstr: 0x168
-  __TEXT.__swift5_fieldmd: 0x104
-  __TEXT.__swift5_types: 0xc
+  __TEXT.__constg_swiftt: 0x1d8
+  __TEXT.__swift5_reflstr: 0x1dc
+  __TEXT.__swift5_fieldmd: 0x160
+  __TEXT.__swift5_types: 0x14
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methname: 0x1ea
-  __TEXT.__swift_as_entry: 0x10
-  __TEXT.__swift_as_ret: 0xc
-  __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x230
-  __TEXT.__eh_frame: 0x238
-  __DATA_CONST.__const: 0x548
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__swift_as_cont: 0x30
+  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__eh_frame: 0x348
+  __DATA_CONST.__const: 0x678
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x488
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__auth_ptr: 0x68
+  __DATA_CONST.__auth_got: 0x508
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__auth_ptr: 0xb0
   __DATA.__objc_const: 0x218
   __DATA.__objc_selrefs: 0x78
-  __DATA.__data: 0x2b8
-  __DATA.__common: 0x70
+  __DATA.__data: 0x320
+  __DATA.__common: 0x90
+  __DATA.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/Frameworks/LocalAuthentication.framework/Versions/A/LocalAuthentication
   - /System/Library/PrivateFrameworks/PreferencePanesSupport.framework/Versions/A/PreferencePanesSupport
   - /System/Library/PrivateFrameworks/SettingsHost.framework/Versions/A/SettingsHost
+  - /System/Library/PrivateFrameworks/SettingsServices.framework/Versions/A/SettingsServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 164
-  Symbols:   216
-  CStrings:  113
+  Functions: 213
+  Symbols:   249
+  CStrings:  125
 
Symbols:
+ _$s12SettingsHost0A13SearchIndexerC21indexSingleOpenIntent14withIdentifier08appValueJ0ySS_SStYaKFTjTu
+ _$sSH13_rawHashValue4seedS2i_tFTq
+ _$sSH4hash4intoys6HasherVz_tFTq
+ _$sSH9hashValueSivgTq
+ _$sSHMp
+ _$sSHSQTb
+ _$sSQ2eeoiySbx_xtFZTq
+ _$sSQMp
+ _$sSS14_fromSubstringySSSshFZ
+ _$sSS5countSivg
+ _$sSS5index5afterSS5IndexVAD_tF
+ _$sSS5index_8offsetBy07limitedC0SS5IndexVSgAE_SiAEtF
+ _$sSSySJSS5IndexVcig
+ _$sSSySsSnySS5IndexVGcig
+ _$sSa10FoundationE34_conditionallyBridgeFromObjectiveC_6resultSbSo7NSArrayC_SayxGSgztFZ
+ _$sSh15minimumCapacityShyxGSi_tcfC
+ _$sSsN
+ _$ss11_SetStorageC4copy8originalAByxGs05__RawaB0C_tFZ
+ _$ss11_SetStorageC6resize8original8capacity4moveAByxGs05__RawaB0C_SiSbtFZ
+ _$ss50ELEMENT_TYPE_OF_SET_VIOLATES_HASHABLE_REQUIREMENTSys5NeverOypXpF
+ _CFPreferencesCopyKeyList
+ _OBJC_CLASS_$_NSArray
+ _kCFPreferencesAnyHost
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRetain_n
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deletedAsyncMethodErrorTu
+ _swift_initStackObject
+ _swift_setDeallocating
CStrings:
+ "AppIntent indexing completed successfully"
+ "AppIntent indexing failed: '%s'"
+ "Beginning AppIntent indexing via SettingsSearchIndexer..."
+ "Beginning targeted reindex of %ld domain(s)"
+ "CRITICAL: privateReindexCS called while indexingCS is true - this should never happen. Ignoring request to prevent CoreSpotlight thrashing."
+ "Detached task started"
+ "Drained %ld target(s) from shared reindexer domain (consumed %ld key(s))"
+ "Found %ld straggler(s) in shared reindexer domain at startup"
+ "Index already in progress, queuing request (queue depth: %ld)"
+ "Indexing complete, CFPrefs synchronized"
+ "No %{public}s* keys in shared reindexer domain"
+ "No pending indexing requests"
+ "Processing queued indexing request (remaining in queue: %ld)"
+ "Recorded start time to CFPrefs"
+ "Recording completion to CFPrefs"
+ "Reindexed %{public}s/%{public}s (attribution: %{public}s)"
+ "Shared reindexer domain empty"
+ "Starting indexing (force: %{bool}d, targeted: %{bool}d, indexingCS now locked)"
+ "Targeted reindex complete"
+ "Targeted reindex failed for %{public}s/%{public}s: %{public}s"
+ "Unparseable shared reindexer key, skipping: %{public}s"
+ "com.apple.SettingsServices.Reindexer"
+ "com.apple.SettingsServices.Reindexer.didEnqueue"
+ "indexingCS lock released (defer)"
+ "reindex requested (force: %{bool}d, targeted: %{bool}d, indexingCS: %{bool}d)"
+ "settingsServices_reindex_"
- "[Indexing] AppIntent indexing completed successfully"
- "[Indexing] AppIntent indexing failed: '%s'"
- "[Indexing] Beginning AppIntent indexing via SettingsSearchIndexer..."
- "[Indexing] CRITICAL: privateReindexCS called while indexingCS is true - this should never happen. Ignoring request to prevent CoreSpotlight thrashing."
- "[Indexing] Detached task started"
- "[Indexing] Index already in progress, queuing request (queue depth: %ld)"
- "[Indexing] Indexing complete, CFPrefs synchronized"
- "[Indexing] No pending indexing requests"
- "[Indexing] Processing queued indexing request (remaining in queue: %ld)"
- "[Indexing] Recorded start time to CFPrefs"
- "[Indexing] Recording completion to CFPrefs"
- "[Indexing] Starting indexing (force: %{bool}d, indexingCS now locked)"
- "[Indexing] indexingCS lock released (defer)"
- "[Indexing] reindexCS called (force: %{bool}d, indexingCS: %{bool}d)"
```
