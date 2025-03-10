## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary`

```diff

-4024.500.33.0.0
-  __TEXT.__text: 0x27e78c
+4024.500.35.0.0
+  __TEXT.__text: 0x27ea2c
   __TEXT.__auth_stubs: 0x1fc0
   __TEXT.__objc_methlist: 0xe004
-  __TEXT.__const: 0x260c0
+  __TEXT.__const: 0x260a0
   __TEXT.__dlopen_cstrs: 0x277
   __TEXT.__gcc_except_tab: 0x13908
-  __TEXT.__cstring: 0x688f4
+  __TEXT.__cstring: 0x68930
   __TEXT.__oslogstring: 0x1ae82
   __TEXT.__ustring: 0x210
-  __TEXT.__unwind_info: 0x7140
-  __TEXT.__eh_frame: 0x1cb0
+  __TEXT.__unwind_info: 0x7150
+  __TEXT.__eh_frame: 0x1cb8
   __TEXT.__objc_classname: 0x1962
   __TEXT.__objc_methname: 0x1ea67
   __TEXT.__objc_methtype: 0x541e
   __TEXT.__objc_stubs: 0x14b00
-  __DATA_CONST.__got: 0xb48
-  __DATA_CONST.__const: 0x9228
+  __DATA_CONST.__got: 0xb40
+  __DATA_CONST.__const: 0x9230
   __DATA_CONST.__objc_classlist: 0x6f0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_superrefs: 0x520
   __DATA_CONST.__objc_arraydata: 0x10c8
   __AUTH_CONST.__auth_got: 0xff8
-  __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x12428
-  __AUTH_CONST.__cfstring: 0x25540
+  __AUTH_CONST.__auth_ptr: 0x28
+  __AUTH_CONST.__const: 0x123f0
+  __AUTH_CONST.__cfstring: 0x25580
   __AUTH_CONST.__objc_const: 0x151e0
   __AUTH_CONST.__objc_arrayobj: 0x20e8
   __AUTH_CONST.__objc_intobj: 0x1ba8

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0xeac
-  __DATA.__data: 0x1970
+  __DATA.__data: 0x1968
   __DATA.__bss: 0xc00
-  __DATA.__common: 0xa54
+  __DATA.__common: 0xa5c
   __DATA_DIRTY.__objc_data: 0x4470
   __DATA_DIRTY.__data: 0x198
   __DATA_DIRTY.__bss: 0x11c8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8093
-  Symbols:   9916
-  CStrings:  12598
+  Functions: 8095
+  Symbols:   9917
+  CStrings:  12600
 
CStrings:
+ "CREATE INDEX IF NOT EXISTS ItemStatsLikedStateChangedDate ON item_stats (liked_state_changed_date DESC)"
+ "PRAGMA user_version = 2240032;"
+ "SELECT artwork_token, artwork_source_type, relative_path, artwork.artwork_type, artwork.artwork_variant_type FROM artwork LEFT OUTER JOIN best_artwork_token ON (artwork_token = available_artwork_token) WHERE artwork.artwork_type != ? AND available_artwork_token IS NULL"
- "SELECT artwork_token, artwork_source_type, relative_path, artwork.artwork_type, artwork.artwork_variant_type FROM artwork LEFT OUTER JOIN best_artwork_token ON (artwork_token = available_artwork_token AND artwork.artwork_variant_type = best_artwork_token.artwork_variant_type) WHERE artwork.artwork_type != ? AND available_artwork_token IS NULL"

```
