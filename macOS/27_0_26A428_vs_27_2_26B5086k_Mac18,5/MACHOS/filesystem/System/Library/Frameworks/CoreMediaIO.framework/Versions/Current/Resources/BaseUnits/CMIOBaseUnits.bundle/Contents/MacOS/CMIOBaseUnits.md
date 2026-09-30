## CMIOBaseUnits

> `/System/Library/Frameworks/CoreMediaIO.framework/Versions/Current/Resources/BaseUnits/CMIOBaseUnits.bundle/Contents/MacOS/CMIOBaseUnits`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-5634.0.0.0.0
-  __TEXT.__text: 0xf4fd0
-  __TEXT.__auth_stubs: 0x1fd0
+5634.40.2.0.0
+  __TEXT.__text: 0xf5050
+  __TEXT.__auth_stubs: 0x1fc0
   __TEXT.__objc_stubs: 0x1140
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1a0
-  __TEXT.__cstring: 0xa296
+  __TEXT.__cstring: 0xa202
   __TEXT.__const: 0x128e
-  __TEXT.__oslogstring: 0x19913
-  __TEXT.__gcc_except_tab: 0xa3ec
-  __TEXT.__objc_methname: 0x1318
+  __TEXT.__oslogstring: 0x19929
+  __TEXT.__gcc_except_tab: 0xa468
+  __TEXT.__objc_methname: 0x1301
   __TEXT.__objc_classname: 0x4c
   __TEXT.__objc_methtype: 0x3fd
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x41e8
+  __TEXT.__unwind_info: 0x41f0
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__const: 0x7da0
-  __DATA_CONST.__cfstring: 0x25e0
+  __DATA_CONST.__cfstring: 0x2500
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x1000
+  __DATA_CONST.__auth_got: 0xff8
   __DATA_CONST.__got: 0x738
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0xb18
+  __DATA.__objc_const: 0xaf8
   __DATA.__objc_selrefs: 0x470
-  __DATA.__objc_ivar: 0x114
+  __DATA.__objc_ivar: 0x110
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x40
   __DATA.__common: 0x6a

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3761
-  Symbols:   779
-  CStrings:  2852
+  Functions: 3763
+  Symbols:   778
+  CStrings:  2846
 
Symbols:
- _CFPreferencesGetAppBooleanValue
CStrings:
+ "%s:%d:%s Error during ConvertTokens frame insertion: %d"
+ "%s:%d:%s Error during ConvertTokens: %d"
+ "%s:%d:%s General Exception caught in ConvertTokens"
+ "%s:%d:%s General Exception caught in ConvertTokens frame insertion"
- "%s:%d:%s Sensitive content analyzer unavailable because SensitiveContentAnalysis/conferencing_detection is disabled."
- "%s:%d:%s effect quality override %d"
- "%s:%d:%s effect quality override %d %d"
- "AEAverage"
- "AETarget"
- "CMIO_Unit_Helpers_PortraitBlur.EffectQualityOverride"
- "CMIO_Unit_Helpers_PortraitBlur.facesForReactions"
- "DebugMetadataSEI"
- "_effectQualityOverride"
- "debug_sei"
```
