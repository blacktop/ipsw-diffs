## ACCMediaLibraryFeature

> `/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/XPCServices/ACCMediaLibraryFeature.xpc/ACCMediaLibraryFeature`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1203.0.0.0.0
-  __TEXT.__text: 0x2a520
+1210.0.0.502.1
+  __TEXT.__text: 0x2a470
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_stubs: 0x4100
-  __TEXT.__objc_methlist: 0x2160
+  __TEXT.__objc_stubs: 0x40e0
+  __TEXT.__objc_methlist: 0x2150
   __TEXT.__cstring: 0x16bc
   __TEXT.__const: 0x150
   __TEXT.__gcc_except_tab: 0x560
-  __TEXT.__objc_methname: 0x5291
+  __TEXT.__objc_methname: 0x5265
   __TEXT.__oslogstring: 0x5a1b
   __TEXT.__objc_classname: 0x33c
   __TEXT.__objc_methtype: 0xe7d

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x420
   __DATA_CONST.__got: 0x260
-  __DATA.__objc_const: 0x3e10
-  __DATA.__objc_selrefs: 0x1348
-  __DATA.__objc_ivar: 0x278
+  __DATA.__objc_const: 0x3de0
+  __DATA.__objc_selrefs: 0x1340
+  __DATA.__objc_ivar: 0x274
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x530
   __DATA.__bss: 0xd8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 859
-  Symbols:   2118
-  CStrings:  1541
+  Functions: 858
+  Symbols:   2115
+  CStrings:  1539
 
Symbols:
+ -[ACCMediaLibraryShim _computeRadioEnabled]
+ _objc_msgSend$_computeRadioEnabled
- -[MediaLibraryHelper _updateITunesRadioEnabled]
- -[MediaLibraryHelper iTunesRadioEnabled]
- OBJC_IVAR_$_MediaLibraryHelper._iTunesRadioEnabled
- _objc_msgSend$_updateITunesRadioEnabled
- _objc_msgSend$iTunesRadioEnabled
CStrings:
+ "_computeRadioEnabled"
- "_iTunesRadioEnabled"
- "_updateITunesRadioEnabled"
- "iTunesRadioEnabled"
```
