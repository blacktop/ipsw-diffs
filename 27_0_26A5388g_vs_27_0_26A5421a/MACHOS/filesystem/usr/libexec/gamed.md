## gamed

> `/usr/libexec/gamed`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
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
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-821.0.20.0.0
-  __TEXT.__text: 0x3700a0
-  __TEXT.__auth_stubs: 0x45a0
-  __TEXT.__objc_stubs: 0x1b460
+821.0.25.0.0
+  __TEXT.__text: 0x370300
+  __TEXT.__auth_stubs: 0x45b0
+  __TEXT.__objc_stubs: 0x1b480
   __TEXT.__objc_methlist: 0xe154
   __TEXT.__const: 0x6d950
   __TEXT.__objc_classname: 0x29b7
-  __TEXT.__oslogstring: 0x18459
-  __TEXT.__cstring: 0x198d1
-  __TEXT.__objc_methname: 0x23697
+  __TEXT.__oslogstring: 0x18519
+  __TEXT.__cstring: 0x198e1
+  __TEXT.__objc_methname: 0x236b7
   __TEXT.__objc_methtype: 0x71ed
   __TEXT.__gcc_except_tab: 0x2f50
   __TEXT.__swift5_typeref: 0x2b46

   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__unwind_info: 0x8cc8
-  __TEXT.__eh_frame: 0xb958
+  __TEXT.__eh_frame: 0xb948
   __DATA_CONST.__const: 0x1b360
   __DATA_CONST.__cfstring: 0xbfc0
   __DATA_CONST.__objc_classlist: 0x968

   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_arrayobj: 0x138
-  __DATA_CONST.__auth_got: 0x22e8
+  __DATA_CONST.__auth_got: 0x22f0
   __DATA_CONST.__got: 0x20c0
   __DATA_CONST.__auth_ptr: 0xd08
   __DATA.__objc_const: 0x203c8
-  __DATA.__objc_selrefs: 0x80e0
+  __DATA.__objc_selrefs: 0x80e8
   __DATA.__objc_ivar: 0x708
   __DATA.__objc_data: 0x7198
   __DATA.__data: 0x4c90

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12358
-  Symbols:   2425
-  CStrings:  10458
+  Functions: 12363
+  Symbols:   2426
+  CStrings:  10461
 
Symbols:
+ _$s16GameServicesCore18AchievementServiceC20resetAllAchievements5games11belongingToySay0aB03RefVyAG0A0_pGG_SayAIyAG6Player_pGGtYaKFTE
+ _$s16GameServicesCore18AchievementServiceC20resetAllAchievements5games11belongingToySay0aB03RefVyAG0A0_pGG_SayAIyAG6Player_pGGtYaKFTETu
+ _GKPathInsideImageCache
- _$s16GameServicesCore18AchievementServiceC13resetProgress12achievements11belongingToySay0aB03RefVyAG0D0_pGG_SayAIyAG6Player_pGGtYaKFTE
- _$s16GameServicesCore18AchievementServiceC13resetProgress12achievements11belongingToySay0aB03RefVyAG0D0_pGG_SayAIyAG6Player_pGGtYaKFTETu
CStrings:
+ "Refusing to cache image at path outside the image cache: %@"
+ "Unable to generate and restore context for switched persona (retry failed): "
+ "Unable to generate and restore context for switched persona (retry failed): %@ launchType=%lu currentType=%lu"
+ "Unable to generate and restore context for switched persona, retrying once: %@"
+ "userPersonaType"
- "Unable to generate and restore context for switched persona"
- "Unable to generate and restore context for switched persona: %@"
```
