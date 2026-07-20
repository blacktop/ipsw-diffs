## musicd

> `/System/Library/Frameworks/MusicKit.framework/Support/musicd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-4026.100.85.0.0
-  __TEXT.__text: 0x29108
-  __TEXT.__auth_stubs: 0x1450
+4026.100.89.0.0
+  __TEXT.__text: 0x2a02c
+  __TEXT.__auth_stubs: 0x1470
   __TEXT.__objc_stubs: 0x3a0
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x15a8
-  __TEXT.__cstring: 0x4a0
+  __TEXT.__const: 0x15c8
+  __TEXT.__cstring: 0x4c0
   __TEXT.__constg_swiftt: 0x404
-  __TEXT.__swift5_typeref: 0x712
+  __TEXT.__swift5_typeref: 0x720
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x312
   __TEXT.__swift5_assocty: 0x120

   __TEXT.__swift5_types: 0x3c
   __TEXT.__objc_methname: 0x637
   __TEXT.__objc_methtype: 0x147
-  __TEXT.__oslogstring: 0x13b7
+  __TEXT.__oslogstring: 0x1427
   __TEXT.__swift5_capture: 0x1d8
   __TEXT.__swift5_fieldmd: 0x2e4
   __TEXT.__swift_as_entry: 0xe0
-  __TEXT.__swift_as_ret: 0x118
-  __TEXT.__swift_as_cont: 0x1a4
+  __TEXT.__swift_as_ret: 0x11c
+  __TEXT.__swift_as_cont: 0x1ac
   __TEXT.__objc_classname: 0x14f
   __TEXT.__swift5_acfuncs: 0xa0
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0xb00
-  __TEXT.__eh_frame: 0x25a0
+  __TEXT.__unwind_info: 0xb08
+  __TEXT.__eh_frame: 0x2610
   __DATA_CONST.__const: 0x880
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0xa30
-  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__auth_got: 0xa40
+  __DATA_CONST.__got: 0x478
   __DATA_CONST.__auth_ptr: 0x368
   __DATA.__objc_const: 0x610
   __DATA.__objc_selrefs: 0x188
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0xb98
+  __DATA.__data: 0xba8
   __DATA.__bss: 0x1300
   __DATA.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 943
-  Symbols:   572
-  CStrings:  189
+  Functions: 978
+  Symbols:   579
+  CStrings:  191
 
Symbols:
+ _$s16MusicKitInternal0A22ConcertsRankingServiceV014recordNotifiedD03foryAC12NotificationV_tYaKF
+ _$s16MusicKitInternal0A22ConcertsRankingServiceV014recordNotifiedD03foryAC12NotificationV_tYaKFTu
+ _$s16MusicKitInternal0A22ConcertsRankingServiceV27pruneScheduledNotificationsyyYaKF
+ _$s16MusicKitInternal0A22ConcertsRankingServiceV27pruneScheduledNotificationsyyYaKFTu
+ _$s16MusicKitInternal0A22ConcertsRankingServiceV29processNotificationCandidates_014forgetNotifiedD0SayAC0H0VGAA0adH7PayloadV_SbtYaKF
+ _$s16MusicKitInternal0A22ConcertsRankingServiceV29processNotificationCandidates_014forgetNotifiedD0SayAC0H0VGAA0adH7PayloadV_SbtYaKFTu
+ _$s16MusicKitInternal0A24ConcertsRankingInterfaceP29processNotificationCandidates_014forgetNotifiedD0AA0A6DaemonV6ResultOy_AG11CodableVoidVGAA0adH7PayloadV_SbtYaFTq
+ _$s16MusicKitInternal0A24ConcertsRankingInterfaceP29processNotificationCandidates_014forgetNotifiedD0AA0A6DaemonV6ResultOy_AG11CodableVoidVGAA0adH7PayloadV_SbtYaKFTqTE
+ _$sSbN
+ _$sSbSEsWP
+ _$sSbSesWP
- _$s16MusicKitInternal0A22ConcertsRankingServiceV29processNotificationCandidatesySayAC0H0VGAA0adH7PayloadVYaKF
- _$s16MusicKitInternal0A22ConcertsRankingServiceV29processNotificationCandidatesySayAC0H0VGAA0adH7PayloadVYaKFTu
- _$s16MusicKitInternal0A24ConcertsRankingInterfaceP29processNotificationCandidatesyAA0A6DaemonV6ResultOy_AF11CodableVoidVGAA0adH7PayloadVYaFTq
- _$s16MusicKitInternal0A24ConcertsRankingInterfaceP29processNotificationCandidatesyAA0A6DaemonV6ResultOy_AF11CodableVoidVGAA0adH7PayloadVYaKFTqTE
CStrings:
+ "[ConcertsRanking] Failed to prune past scheduled notifications: %{public}s."
+ "[ConcertsRanking] Scheduled a notification but failed to record its concerts for dedupe: %{public}s."
+ "forgetNotifiedConcerts"
- "[ConcertsRanking] Re-ranking concerts before processing notifications."
```
