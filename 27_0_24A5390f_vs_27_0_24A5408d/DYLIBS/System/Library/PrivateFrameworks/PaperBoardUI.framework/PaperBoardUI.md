## PaperBoardUI

> `/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-350.1.100.0.0
-  __TEXT.__text: 0x77b54
-  __TEXT.__objc_methlist: 0x970c
-  __TEXT.__const: 0x828
-  __TEXT.__cstring: 0x7a98
-  __TEXT.__oslogstring: 0x4363
-  __TEXT.__gcc_except_tab: 0xc30
+355.0.5.0.0
+  __TEXT.__text: 0x78af4
+  __TEXT.__objc_methlist: 0x972c
+  __TEXT.__const: 0x838
+  __TEXT.__cstring: 0x7b16
+  __TEXT.__oslogstring: 0x47a0
+  __TEXT.__gcc_except_tab: 0xc4c
   __TEXT.__dlopen_cstrs: 0x1a6
-  __TEXT.__unwind_info: 0x2898
+  __TEXT.__unwind_info: 0x28b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5140
+  __DATA_CONST.__objc_selrefs: 0x5160
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __DATA_CONST.__got: 0x890
+  __DATA_CONST.__got: 0x898
   __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x5f00
-  __AUTH_CONST.__objc_const: 0x19378
+  __AUTH_CONST.__cfstring: 0x6000
+  __AUTH_CONST.__objc_const: 0x193b8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_intobj: 0x120

   __AUTH_CONST.__auth_got: 0x838
   __AUTH.__objc_data: 0x2030
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x9b4
+  __DATA.__objc_ivar: 0x9bc
   __DATA.__data: 0x16a0
   __DATA.__bss: 0x478
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3751
-  Symbols:   8263
-  CStrings:  1406
+  Functions: 3760
+  Symbols:   8275
+  CStrings:  1425
 
Symbols:
+ -[PBUIPosterVariantViewController _addStateCaptureHandlers]
+ -[PBUIPosterVariantViewController _completePendingProminentColorFetchesAfterFailedSnapshot]
+ -[PBUIPosterWallpaperViewController _activeStylesDescription]
+ GCC_except_table112
+ GCC_except_table127
+ GCC_except_table36
+ GCC_except_table66
+ GCC_except_table96
+ _OBJC_CLASS_$_FBSOrientationObserver
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._stateCaptureHandles
+ _OBJC_IVAR_$_PBUIPosterViewController._homeWallpaperStyle
+ _PBUIInitialOrientationForCurrentDevice
+ ___59-[PBUIPosterVariantViewController _addStateCaptureHandlers]_block_invoke
+ _objc_msgSend$_activeStylesDescription
+ _objc_msgSend$_completePendingProminentColorFetchesAfterFailedSnapshot
+ _objc_msgSend$applyUpdatesLocally:error:
+ _objc_msgSend$copyWithAbortsIfBacklightNotFull:
+ _objc_msgSend$string
- GCC_except_table109
- GCC_except_table56
- GCC_except_table58
- GCC_except_table60
- GCC_except_table93
- _objc_msgSend$synchronouslyApplyUpdates:error:
CStrings:
+ "%@[%@]=%@ "
+ "(none)"
+ "Aug  4 2026 09:38:10"
+ "A\xf0q"
+ "Could not read snapshot: %{public}@ (url=%{public}@)"
+ "PBUIPosterVariant[%@] - %p"
+ "[%{public}@] WIPE cache (orientation rotate -> %ld)"
+ "[%{public}@] WIPE cache (pathProvider rotate): old=%{public}@ new=%{public}@"
+ "[%{public}@] WIPE cache + on-disk RuntimeSnapshots (CLEAR_ALL notification); sender=%{public}@"
+ "[%{public}@] cacheIdentifier ROTATED (new empty cache checked out): %{public}@ -> %{public}@"
+ "[%{public}@] setActiveStyle: %{public}@ -> %{public}@ (contentHidden=%{BOOL}d)"
+ "[%{public}@] snapshot failed; completing %lu pending prominent color fetch(es) with %{public}@"
+ "[home] BLACK-SNAPSHOT-RISK: showsSnapshot=YES but snapshotSourceValid=NO (empty snapshot -> black); reflectsLock=%{BOOL}d portalProvider=%{public}@"
+ "[home] NEAR-BLACK snapshot committed valid (avgColor=%{public}@) -> showing black; please file a radar to SpringBoard"
+ "[home] _updateRotationForOrientation: orientation was Unknown; flooring to Portrait to avoid AlwaysAll scene-update fault"
+ "activeStyles"
+ "contentHidden"
+ "loaded snapshot %{public}@ (%.0f x %.0f)"
+ "setActiveStyle:%{public}@ forVariant:%{public}@ (lockShadow=%{public}@ homeShadow=%{public}@ parentActiveStyle=%{public}@ activeVariant=%{public}@)"
+ "snapshotSource"
+ "snapshotSourceValid"
+ "snapshotViewHidden"
+ "\xf0\xf0a"
- "A\xf0a"
- "Could not read snapshot: %{public}@"
- "Jul 13 2026 21:41:04"
- "\xf0\xf0Q"
```
