## trustd

> `/usr/libexec/trustd`

```diff

-  __TEXT.__text: 0x59e4c
+  __TEXT.__text: 0x5a36c
   __TEXT.__auth_stubs: 0x23a0
   __TEXT.__objc_stubs: 0x3340
   __TEXT.__objc_methlist: 0xe0c

   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xb04
-  __TEXT.__cstring: 0x5d59
-  __TEXT.__oslogstring: 0x590c
-  __TEXT.__unwind_info: 0x1030
+  __TEXT.__cstring: 0x5d3f
+  __TEXT.__oslogstring: 0x5b59
+  __TEXT.__unwind_info: 0x1028
   __DATA_CONST.__const: 0x41a0
-  __DATA_CONST.__cfstring: 0x5a60
+  __DATA_CONST.__cfstring: 0x5a40
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__objc_intobj: 0x108
-  __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__objc_intobj: 0x120
+  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x190
   __DATA_CONST.__auth_got: 0x11e0
-  __DATA_CONST.__got: 0x920
+  __DATA_CONST.__got: 0x930
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x1758
   __DATA.__objc_selrefs: 0xe50
   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x5b8
-  __DATA.__data: 0x450
+  __DATA.__data: 0x458
   __DATA.__bss: 0x520
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 1220
   Symbols:   886
-  CStrings:  2899
+  CStrings:  2904
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
Functions:
~ sub_10000b600 : 580 -> 572
~ sub_10001a554 -> sub_10001a54c : 132 -> 164
~ sub_10001d904 -> sub_10001d91c : 268 -> 300
~ sub_10001e568 -> sub_10001e5a0 : 1424 -> 1680
~ sub_100023c8c -> sub_100023dc4 : 196 -> 324
~ sub_1000392e0 -> sub_100039498 : 116 -> 152
~ sub_100041958 -> sub_100041b34 : 196 -> 612
~ sub_100041a1c -> sub_100041d98 : 52 -> 196
~ sub_100041a50 -> sub_100041e5c : 372 -> 52
~ sub_100041bc4 -> sub_100041e90 : 72 -> 356
~ sub_100041c0c -> sub_100041ff4 : 84 -> 72
~ sub_100041c60 -> sub_10004203c : 584 -> 84
~ sub_100043338 -> sub_100043520 : 572 -> 1308
~ sub_1000436bc -> sub_100043b84 : 6084 -> 6148
~ sub_100046900 -> sub_100046e08 : 1780 -> 1804
CStrings:
+ "CT log has non-date \"expiry\" field; not counting (log=%@)"
+ "CT log has non-date \"frozen\" field; treating as invalid (log=%@)"
+ "CT log has non-date shard window field; treating as invalid (log=%@)"
+ "MobileAssetCompatibilityVersion"
+ "OTATrust: failed to read key from trusted CT log array entry at index %lu"
+ "OTATrust: failed to reset OTAPKIContext after compat change: %@"
+ "OTATrust: trusted CT log entry at index %lu has non-data \"key\" (class=%@); skipping"
+ "OTATrust: trusted CT log entry at index %lu has non-data \"log_id\" (class=%@); skipping"
+ "OTATrust: trusted CT log entry at index %lu has non-date \"%@\" (class=%@); skipping"
+ "com.apple.ValidUpdater.update"
+ "compatibility version changed (disk %@ -> binary %lu); resetting check-in"
+ "no log_id in trusted CT log array entry at index %lu; computing from key"
+ "v16@?0^{__SecRevocationDb=^{__OpaqueSecDb}BBB^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}}8"
+ "validupdate: Failed to create db at \"%@\""
- "%s path"
- "%s path as UTF8 string"
- "com.apple.trustd.valid.db-changed"
- "could not get valid snapshot"
- "failed to read key from trusted CT log array entry at index %lu"
- "failed to read log_id from trusted CT log array entry at index %lu, computing log_id"
- "sqlite3"
- "v16@?0^{__SecRevocationDb=^{__OpaqueSecDb}^{dispatch_queue_s}BBB^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}}8"

```
