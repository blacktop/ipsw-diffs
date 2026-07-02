## trustd

> `/usr/libexec/trustd`

```diff

-  __TEXT.__text: 0x68d14
+  __TEXT.__text: 0x69628
   __TEXT.__auth_stubs: 0x2430
   __TEXT.__objc_stubs: 0x3200
   __TEXT.__objc_methlist: 0xd54
-  __TEXT.__const: 0x5ae1
+  __TEXT.__const: 0x5ae9
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__gcc_except_tab: 0xce0
-  __TEXT.__cstring: 0x7355
-  __TEXT.__oslogstring: 0x68b8
+  __TEXT.__cstring: 0x7377
+  __TEXT.__oslogstring: 0x6afe
   __TEXT.__objc_classname: 0x1b1
   __TEXT.__objc_methname: 0x3082
   __TEXT.__objc_methtype: 0xc75
-  __TEXT.__unwind_info: 0x1158
+  __TEXT.__unwind_info: 0x1160
   __DATA_CONST.__auth_got: 0x1228
   __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__const: 0x4e48
-  __DATA_CONST.__cfstring: 0x6800
+  __DATA_CONST.__cfstring: 0x6820
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_intobj: 0x108
-  __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__objc_intobj: 0x120
+  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x190
   __DATA.__objc_const: 0x16e0
   __DATA.__objc_selrefs: 0xe20

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1329
+  Functions: 1331
   Symbols:   847
-  CStrings:  3229
+  CStrings:  3240
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
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
+ "compatibility version changed (disk %@ -> binary %lu); resetting check-in"
+ "no log_id in trusted CT log array entry at index %lu; computing from key"
- "failed to read key from trusted CT log array entry at index %lu"
- "failed to read log_id from trusted CT log array entry at index %lu, computing log_id"

```
