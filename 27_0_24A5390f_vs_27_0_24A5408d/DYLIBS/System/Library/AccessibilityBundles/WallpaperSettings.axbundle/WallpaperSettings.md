## WallpaperSettings

> `/System/Library/AccessibilityBundles/WallpaperSettings.axbundle/WallpaperSettings`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x18d8
+3048.0.0.0.0
+  __TEXT.__text: 0x1c44
   __TEXT.__objc_methlist: 0x150
-  __TEXT.__const: 0x20
+  __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__cstring: 0xaa1
-  __TEXT.__oslogstring: 0x3e
+  __TEXT.__oslogstring: 0x3be
   __TEXT.__unwind_info: 0xd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 32
-  Symbols:   167
-  CStrings:  212
+  Symbols:   169
+  CStrings:  219
 
Symbols:
+ _AXAIWhiteGloveLoggingEnabled
+ __os_log_error_impl
+ _objc_retain_x24
- _objc_retain_x19
Functions:
~ _AXWallpaperLabel : 848 -> 1176
~ -[SwiftUIAccessibilityNode__WallpaperSettings__SwiftUI _axWallpaperDescription] : 524 -> 776
~ -[SwiftUIAccessibilityNode__WallpaperSettings__SwiftUI accessibilityLabel] : 332 -> 628
CStrings:
+ "rdar://168563356 AXWallpaperLabel called with nil filename, returning nil"
+ "rdar://168563356 AXWallpaperLabel return-localized rawFilename=%{public}@ stripped=%{public}@ key=%{public}@ axDesc=%{public}@"
+ "rdar://168563356 AXWallpaperLabel return-raw-filename rawFilename=%{public}@ stripped=%{public}@ key=%{public}@ (no localized string found)"
+ "rdar://168563356 WallpaperSwiftUIAccessibilityNode _axWallpaperDescription enter identifier=%{public}@ superLabel=%{public}@"
+ "rdar://168563356 WallpaperSwiftUIAccessibilityNode _axWallpaperDescription return identifier=%{public}@ wallpaper=%{public}@"
+ "rdar://168563356 WallpaperSwiftUIAccessibilityNode accessibilityLabel enter identifier=%{public}@ superLabel=%{public}@ traits=%lu"
+ "rdar://168563356 WallpaperSwiftUIAccessibilityNode accessibilityLabel return identifier=%{public}@ label=%{public}@ (axWallpaperDescription=%{public}@ superLabel=%{public}@)"
```
