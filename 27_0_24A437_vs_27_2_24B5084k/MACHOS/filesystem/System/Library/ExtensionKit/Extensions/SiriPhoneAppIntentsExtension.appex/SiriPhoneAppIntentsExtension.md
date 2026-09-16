## SiriPhoneAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/SiriPhoneAppIntentsExtension.appex/SiriPhoneAppIntentsExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`

```diff

-3600.38.22.11.2
+3605.17.1.1.1
   __TEXT.__text: 0xd380
   __TEXT.__auth_stubs: 0x8f0
   __TEXT.__const: 0x20d8

   __TEXT.__oslogstring: 0x287
   __TEXT.__unwind_info: 0x9a0
   __TEXT.__eh_frame: 0x338
-  __DATA_CONST.__const: 0xbc0
+  __DATA_CONST.__const: 0xbc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x478
   __DATA_CONST.__got: 0xe8

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 765
-  Symbols:   2158
+  Symbols:   2160
   CStrings:  34
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_SiriPhoneAppIntentsExtension
Functions:
~ _$s28SiriPhoneAppIntentsExtension0A18KitStartCallIntentVAC0cD006SystemI0AAWl -> sub_10000aab0 : 84 -> 4
~ sub_10000aabc -> _$s28SiriPhoneAppIntentsExtension0A18KitStartCallIntentVAC0cD006SystemI0AAWl : 4 -> 84
```
