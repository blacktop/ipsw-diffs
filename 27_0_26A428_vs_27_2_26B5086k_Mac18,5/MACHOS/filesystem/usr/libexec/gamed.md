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
-  __TEXT.__text: 0x35c894
-  __TEXT.__auth_stubs: 0x45b0
-  __TEXT.__objc_stubs: 0x1b480
-  __TEXT.__objc_methlist: 0xe154
-  __TEXT.__const: 0x6d950
+821.1.8.0.0
+  __TEXT.__text: 0x35d594
+  __TEXT.__auth_stubs: 0x45c0
+  __TEXT.__objc_stubs: 0x1b580
+  __TEXT.__objc_methlist: 0xe1b4
+  __TEXT.__const: 0x6d960
   __TEXT.__objc_classname: 0x29b7
-  __TEXT.__oslogstring: 0x18519
-  __TEXT.__cstring: 0x198e1
-  __TEXT.__objc_methname: 0x236b7
+  __TEXT.__oslogstring: 0x185e9
+  __TEXT.__cstring: 0x19a01
+  __TEXT.__objc_methname: 0x23837
   __TEXT.__objc_methtype: 0x71ed
-  __TEXT.__gcc_except_tab: 0x2f50
+  __TEXT.__gcc_except_tab: 0x2f64
   __TEXT.__swift5_typeref: 0x2b46
   __TEXT.__constg_swiftt: 0x1bbc
   __TEXT.__swift5_reflstr: 0x1299

   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0x2a8
   __TEXT.__swift5_types: 0x1e8
-  __TEXT.__swift5_capture: 0x19f4
-  __TEXT.__swift_as_entry: 0x50c
-  __TEXT.__swift_as_ret: 0x60c
+  __TEXT.__swift5_capture: 0x1a08
+  __TEXT.__swift_as_entry: 0x514
+  __TEXT.__swift_as_ret: 0x610
   __TEXT.__swift_as_cont: 0x8c0
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0xabd8
-  __TEXT.__eh_frame: 0xb950
-  __DATA_CONST.__const: 0x1b360
+  __TEXT.__unwind_info: 0xac28
+  __TEXT.__eh_frame: 0xb998
+  __DATA_CONST.__const: 0x1b3d0
   __DATA_CONST.__cfstring: 0xbfc0
   __DATA_CONST.__objc_classlist: 0x968
   __DATA_CONST.__objc_catlist: 0x158

   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_arrayobj: 0x138
-  __DATA_CONST.__auth_got: 0x22f0
-  __DATA_CONST.__got: 0x20c0
+  __DATA_CONST.__auth_got: 0x22f8
+  __DATA_CONST.__got: 0x20c8
   __DATA_CONST.__auth_ptr: 0xd08
-  __DATA.__objc_const: 0x203c8
-  __DATA.__objc_selrefs: 0x80e8
+  __DATA.__objc_const: 0x203d8
+  __DATA.__objc_selrefs: 0x8128
   __DATA.__objc_ivar: 0x708
   __DATA.__objc_data: 0x7198
   __DATA.__data: 0x4c90

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12373
-  Symbols:   2426
-  CStrings:  10461
+  Functions: 12406
+  Symbols:   2428
+  CStrings:  10475
 
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
