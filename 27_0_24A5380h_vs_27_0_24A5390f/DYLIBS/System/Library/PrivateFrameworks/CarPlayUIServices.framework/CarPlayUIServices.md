## CarPlayUIServices

> `/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-577.2.0.0.0
-  __TEXT.__text: 0x38d18
+580.0.0.0.0
+  __TEXT.__text: 0x38e4c
   __TEXT.__objc_methlist: 0x398c
-  __TEXT.__const: 0xe94
-  __TEXT.__oslogstring: 0x1778
+  __TEXT.__const: 0xea4
+  __TEXT.__oslogstring: 0x1818
   __TEXT.__cstring: 0x1ad2
   __TEXT.__gcc_except_tab: 0x4a4
   __TEXT.__constg_swiftt: 0x7a4

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1696
   Symbols:   3561
-  CStrings:  395
+  CStrings:  397
 
Functions:
~ -[CRSUIWallpaperPreferences setVehicle:] : 476 -> 600
~ -[CRSUIWallpaperPreferences setCurrentWallpaper:requiresDarkAppearanceHandler:] : 840 -> 1024
CStrings:
+ "[CRSUIWallpaperPreferences] -setCurrentWallpaper: vehicle=%p displayID=%{public}@ dataProvider=%p"
+ "[CRSUIWallpaperPreferences] -setVehicle: %p -> %p (self=%p)"
```
