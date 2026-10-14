## MobileSafari

> `/System/Library/DataClassMigrators/MobileSafari.migrator/MobileSafari`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-7625.2.7.1.0
-  __TEXT.__text: 0x5d24
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_stubs: 0x14e0
-  __TEXT.__objc_methlist: 0x3c0
+7625.2.8.10.4
+  __TEXT.__text: 0x5e74
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_stubs: 0x15a0
+  __TEXT.__objc_methlist: 0x3d0
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__cstring: 0xd77
   __TEXT.__oslogstring: 0x120e
   __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methname: 0x14cc
+  __TEXT.__objc_methname: 0x158b
   __TEXT.__objc_methtype: 0x19e
   __TEXT.__unwind_info: 0x208
   __DATA_CONST.__const: 0x338

   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0x150
   __DATA_CONST.__objc_arrayobj: 0x108
-  __DATA_CONST.__auth_got: 0x230
-  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0x2c0
   __DATA.__objc_const: 0x2e8
-  __DATA.__objc_selrefs: 0x640
+  __DATA.__objc_selrefs: 0x670
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 113
-  Symbols:   218
-  CStrings:  445
+  Functions: 114
+  Symbols:   220
+  CStrings:  451
 
Symbols:
+ _OBJC_CLASS_$_SFDeviceUtilities
+ _SFSeedCloudTabsRestorationUUIDIfAbsent
CStrings:
+ "deviceUUID"
+ "isLockedSync"
+ "migratePebblePinnedSuggestionsToBookmarkCollection:"
+ "migratePebblePinnedSuggestionsToBookmarksDatabase"
+ "pebblePinnedSuggestionsFolderIDIfExists"
+ "safariBookmarkCollection"
```
