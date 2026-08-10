## gamed

> `/usr/libexec/gamed`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-821.0.20.0.0
-  __TEXT.__text: 0x2a5604
-  __TEXT.__auth_stubs: 0x4ab0
+821.0.25.0.0
+  __TEXT.__text: 0x2a559c
+  __TEXT.__auth_stubs: 0x4ac0
   __TEXT.__objc_stubs: 0x1bbc0
   __TEXT.__objc_methlist: 0xe28c
   __TEXT.__const: 0x13580
   __TEXT.__objc_classname: 0x2a37
-  __TEXT.__oslogstring: 0x19209
+  __TEXT.__oslogstring: 0x19239
   __TEXT.__cstring: 0x196f1
   __TEXT.__objc_methname: 0x23c57
   __TEXT.__objc_methtype: 0x73ea

   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__unwind_info: 0x9580
-  __TEXT.__eh_frame: 0xc7b0
+  __TEXT.__eh_frame: 0xc7a0
   __DATA_CONST.__const: 0x145d8
   __DATA_CONST.__cfstring: 0xc2c0
   __DATA_CONST.__objc_classlist: 0x970

   __DATA_CONST.__objc_arraydata: 0x3e8
   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_arrayobj: 0x168
-  __DATA_CONST.__auth_got: 0x2570
+  __DATA_CONST.__auth_got: 0x2578
   __DATA_CONST.__got: 0x22c0
   __DATA_CONST.__auth_ptr: 0xd20
   __DATA.__objc_const: 0x20ff0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12482
-  Symbols:   2578
-  CStrings:  10606
+  Functions: 12483
+  Symbols:   2579
+  CStrings:  10607
 
Symbols:
+ _$s16GameServicesCore18AchievementServiceC20resetAllAchievements5games11belongingToySay0aB03RefVyAG0A0_pGG_SayAIyAG6Player_pGGtYaKFTE
+ _$s16GameServicesCore18AchievementServiceC20resetAllAchievements5games11belongingToySay0aB03RefVyAG0A0_pGG_SayAIyAG6Player_pGGtYaKFTETu
+ _GKPathInsideImageCache
- _$s16GameServicesCore18AchievementServiceC13resetProgress12achievements11belongingToySay0aB03RefVyAG0D0_pGG_SayAIyAG6Player_pGGtYaKFTE
- _$s16GameServicesCore18AchievementServiceC13resetProgress12achievements11belongingToySay0aB03RefVyAG0D0_pGG_SayAIyAG6Player_pGGtYaKFTETu
CStrings:
+ "Refusing to cache image at path outside the image cache: %@"
```
