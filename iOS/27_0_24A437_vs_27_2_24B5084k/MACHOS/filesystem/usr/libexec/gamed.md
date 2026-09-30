## gamed

> `/usr/libexec/gamed`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_classname`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-821.0.25.0.0
-  __TEXT.__text: 0x29148c
-  __TEXT.__auth_stubs: 0x4ac0
-  __TEXT.__objc_stubs: 0x1bbc0
-  __TEXT.__objc_methlist: 0xe28c
-  __TEXT.__const: 0x13580
+821.1.8.0.0
+  __TEXT.__text: 0x29211c
+  __TEXT.__auth_stubs: 0x4ad0
+  __TEXT.__objc_stubs: 0x1bcc0
+  __TEXT.__objc_methlist: 0xe2ec
+  __TEXT.__const: 0x13590
   __TEXT.__objc_classname: 0x2a37
-  __TEXT.__oslogstring: 0x19239
-  __TEXT.__cstring: 0x196f1
-  __TEXT.__objc_methname: 0x23c57
+  __TEXT.__oslogstring: 0x19319
+  __TEXT.__cstring: 0x19801
+  __TEXT.__objc_methname: 0x23dd7
   __TEXT.__objc_methtype: 0x73ea
-  __TEXT.__gcc_except_tab: 0x30d0
+  __TEXT.__gcc_except_tab: 0x30e4
   __TEXT.__swift5_typeref: 0x2cd0
   __TEXT.__constg_swiftt: 0x1c2c
   __TEXT.__swift5_reflstr: 0x1289

   __TEXT.__swift5_assocty: 0x108
   __TEXT.__swift5_proto: 0x288
   __TEXT.__swift5_types: 0x1ec
-  __TEXT.__swift5_capture: 0x1b50
-  __TEXT.__swift_as_entry: 0x568
-  __TEXT.__swift_as_ret: 0x690
+  __TEXT.__swift5_capture: 0x1b64
+  __TEXT.__swift_as_entry: 0x570
+  __TEXT.__swift_as_ret: 0x694
   __TEXT.__swift_as_cont: 0x9ac
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0xb260
-  __TEXT.__eh_frame: 0xc7a8
-  __DATA_CONST.__const: 0x145d8
+  __TEXT.__unwind_info: 0xb2b0
+  __TEXT.__eh_frame: 0xc7f0
+  __DATA_CONST.__const: 0x14708
   __DATA_CONST.__cfstring: 0xc2c0
   __DATA_CONST.__objc_classlist: 0x970
   __DATA_CONST.__objc_catlist: 0x158

   __DATA_CONST.__objc_arraydata: 0x3e8
   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_arrayobj: 0x168
-  __DATA_CONST.__auth_got: 0x2578
-  __DATA_CONST.__got: 0x22c0
+  __DATA_CONST.__auth_got: 0x2580
+  __DATA_CONST.__got: 0x22c8
   __DATA_CONST.__auth_ptr: 0xd20
-  __DATA.__objc_const: 0x20ff0
-  __DATA.__objc_selrefs: 0x8288
+  __DATA.__objc_const: 0x21000
+  __DATA.__objc_selrefs: 0x82c8
   __DATA.__objc_ivar: 0x71c
   __DATA.__objc_data: 0x71e8
   __DATA.__data: 0x4e10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12494
-  Symbols:   2579
-  CStrings:  10607
+  Functions: 12527
+  Symbols:   2581
+  CStrings:  10621
 
Symbols:
+ _$s12GameServices16DataRefreshScopeO7missingyA2CmFWC
+ _$s16GameServicesCore0aB12DataProviderC14syncAllPendingyyYaF
+ _$s16GameServicesCore0aB12DataProviderC14syncAllPendingyyYaFTu
+ _$s16GameServicesCore0aB7SupportP11sendRequest4data7headers2to10Foundation4DataVAE_Sd8cacheTTLtAJ_SDyS2SGSStYaKFTq
- _$s12GameServices16DataRefreshScopeO3allyA2CmFWC
- _$s16GameServicesCore0aB7SupportP11sendRequest4data7headers2to10Foundation4DataVAJ_SDyS2SGSStYaKFTq
CStrings:
+ "-[GKGameServicePrivate loadGamesPlayedSummariesForPlayerID:limit:withinSecs:handler:]_block_invoke"
+ "-[GamesPlayedSummaryList(GKQuery) gkCoversRequestWithinSecs:]"
+ "-[GamesPlayedSummaryList(GKQuery) gkHasServeableCache]"
+ "A games played summaries refresh is already in flight for : %@"
+ "Games played summaries cache does not satisfy request (withinSecs: %@); cached withinSecs: %@, fetchedAt: %@. Going to server for : %@"
+ "Returning expired games played descriptors for %@ and refreshing in the background"
+ "beginBackgroundGamesPlayedSummariesRefreshForPlayerID:"
+ "com.apple.gamed.GKGameService.gamesPlayedSummaries.refresh"
+ "endBackgroundGamesPlayedSummariesRefreshForPlayerID:"
+ "gamesPlayedSummariesRefreshQueue"
+ "gkCoversRequestWithinSecs:"
+ "gkHasServeableCache"
+ "loadGamesPlayedSummariesForPlayerID:limit:withinSecs:handler:"
+ "networkManagerIgnoreCache is set. Going to server for : %@"
+ "refreshGamesPlayedSummariesInBackgroundForPlayerID:limit:withinSecs:"
+ "syncAllPendingWithCompletionHandler:"
- "Encountered a fetch error while trying to lookup a game list: %@"
- "Going to server for games played descriptors for : %@"
```
