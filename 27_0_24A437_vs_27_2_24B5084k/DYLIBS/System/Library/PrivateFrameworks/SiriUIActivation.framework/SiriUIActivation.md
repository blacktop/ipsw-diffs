## SiriUIActivation

> `/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation`

```diff

-3600.55.37.11.4
-  __TEXT.__text: 0x2e0e4
-  __TEXT.__objc_methlist: 0x26e8
+3605.22.2.0.0
+  __TEXT.__text: 0x2e41c
+  __TEXT.__objc_methlist: 0x2720
   __TEXT.__const: 0x8dc
   __TEXT.__gcc_except_tab: 0x6d0
-  __TEXT.__cstring: 0x4c5b
-  __TEXT.__oslogstring: 0x4e2b
+  __TEXT.__cstring: 0x4d5b
+  __TEXT.__oslogstring: 0x4edb
   __TEXT.__swift5_typeref: 0x51e
   __TEXT.__constg_swiftt: 0x468
   __TEXT.__swift5_reflstr: 0x342

   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x40
   __TEXT.__swift_as_cont: 0x34
-  __TEXT.__unwind_info: 0x1080
+  __TEXT.__unwind_info: 0x1090
   __TEXT.__eh_frame: 0x668
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fe8
+  __DATA_CONST.__objc_selrefs: 0x2020
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x5d0
+  __DATA_CONST.__got: 0x5d8
   __AUTH_CONST.__const: 0xd40
-  __AUTH_CONST.__cfstring: 0x8e0
-  __AUTH_CONST.__objc_const: 0x2938
+  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__objc_const: 0x2968
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0xab0
   __AUTH.__objc_data: 0x268
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x1bc
+  __DATA.__objc_ivar: 0x1c0
   __DATA.__data: 0xa10
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x6f8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1077
-  Symbols:   2451
-  CStrings:  623
+  Functions: 1082
+  Symbols:   2463
+  CStrings:  631
 
Symbols:
+ -[SASUICampoSessionCoordinator initWithResumptionGracePeriod:]
+ -[SASUICampoSessionCoordinator init]
+ -[SASUICampoSessionCoordinator resumptionGracePeriod]
+ -[SiriPresentationViewController _isForPreprocessedCarPlayBannerTap:newSiriRequestOptions:]
+ -[SiriPresentationViewController noteWillBeginTearDownForDismissalReason:withOriginalDismissalOptions:]
+ GCC_except_table100
+ GCC_except_table105
+ GCC_except_table108
+ GCC_except_table121
+ GCC_except_table122
+ GCC_except_table128
+ GCC_except_table132
+ GCC_except_table141
+ GCC_except_table147
+ GCC_except_table156
+ GCC_except_table171
+ GCC_except_table176
+ GCC_except_table197
+ GCC_except_table221
+ GCC_except_table222
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table251
+ GCC_except_table277
+ GCC_except_table278
+ GCC_except_table285
+ GCC_except_table290
+ GCC_except_table306
+ GCC_except_table314
+ GCC_except_table34
+ GCC_except_table37
+ GCC_except_table44
+ GCC_except_table46
+ GCC_except_table53
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table64
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table82
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table95
+ _OBJC_CLASS_$_SISchemaUEICarPlayBannerPreprocessedTapped
+ _OBJC_IVAR_$_SASUICampoSessionCoordinator._resumptionGracePeriod
+ ___block_descriptor_65_e8_32s40s48s56w_e20_v20?0B8"NSError"12lw56l8s32l8s40l8s48l8
+ _objc_msgSend$_isForPreprocessedCarPlayBannerTap:newSiriRequestOptions:
+ _objc_msgSend$doubleForKey:
+ _objc_msgSend$initWithResumptionGracePeriod:
+ _objc_msgSend$isPreprocessRequest:
+ _objc_msgSend$setNeedsUpdateOfSupportedInterfaceOrientations
- GCC_except_table104
- GCC_except_table106
- GCC_except_table118
- GCC_except_table119
- GCC_except_table126
- GCC_except_table130
- GCC_except_table131
- GCC_except_table145
- GCC_except_table154
- GCC_except_table169
- GCC_except_table174
- GCC_except_table193
- GCC_except_table217
- GCC_except_table220
- GCC_except_table228
- GCC_except_table229
- GCC_except_table249
- GCC_except_table275
- GCC_except_table276
- GCC_except_table283
- GCC_except_table288
- GCC_except_table300
- GCC_except_table312
- GCC_except_table33
- GCC_except_table36
- GCC_except_table43
- GCC_except_table45
- GCC_except_table52
- GCC_except_table57
- GCC_except_table59
- GCC_except_table62
- GCC_except_table72
- GCC_except_table76
- GCC_except_table81
- GCC_except_table90
- GCC_except_table92
- GCC_except_table94
- GCC_except_table99
- ___block_descriptor_49_e8_32s40w_e20_v20?0B8"NSError"12lw40l8s32l8
CStrings:
+ "%s #Campo Resumption grace period is %f seconds"
+ "%s #Preprocessing #CarPlay emitting preprocessed banner tapped event."
+ "%s #Preprocessing #CarPlay isForPreprocessedCarPlayBannerTap %d"
+ "-[SASUICampoSessionCoordinator initWithResumptionGracePeriod:]"
+ "-[SiriPresentationViewController _isForPreprocessedCarPlayBannerTap:newSiriRequestOptions:]"
+ "-[SiriPresentationViewController _startRequestWithOptions:]_block_invoke_2"
+ "com.apple.campo"
+ "sessionResumptionTimeout"
```
