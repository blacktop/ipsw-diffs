## trustd

> `/usr/libexec/trustd`

```diff

-  __TEXT.__text: 0x5d7d4
+  __TEXT.__text: 0x5dd38
   __TEXT.__auth_stubs: 0x2340
   __TEXT.__objc_stubs: 0x33a0
   __TEXT.__objc_methlist: 0xe0c

   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xc0c
-  __TEXT.__cstring: 0x59a2
-  __TEXT.__oslogstring: 0x5a44
-  __TEXT.__unwind_info: 0x1070
+  __TEXT.__cstring: 0x5988
+  __TEXT.__oslogstring: 0x5c91
+  __TEXT.__unwind_info: 0x1078
   __DATA_CONST.__const: 0x47c8
-  __DATA_CONST.__cfstring: 0x5720
+  __DATA_CONST.__cfstring: 0x5700
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__objc_intobj: 0x120
-  __DATA_CONST.__objc_arraydata: 0xe0
+  __DATA_CONST.__objc_intobj: 0x138
+  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__auth_got: 0x11b0
-  __DATA_CONST.__got: 0x8f0
+  __DATA_CONST.__got: 0x900
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x1758
   __DATA.__objc_selrefs: 0xe68
   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x5b8
-  __DATA.__data: 0x480
+  __DATA.__data: 0x488
   __DATA.__bss: 0x538
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 1292
   Symbols:   874
-  CStrings:  2860
+  CStrings:  2865
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
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
+ "com.apple.security.file./AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ih6abw/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
+ "compatibility version changed (disk %@ -> binary %lu); resetting check-in"
+ "no log_id in trusted CT log array entry at index %lu; computing from key"
+ "v16@?0^{__SecRevocationDb=^{__OpaqueSecDb}BBB^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}}8"
+ "validupdate: Failed to create db at \"%@\""
- "%s path"
- "%s path as UTF8 string"
- "com.apple.security.file./AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XZI2X/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
- "com.apple.trustd.valid.db-changed"
- "could not get valid snapshot"
- "failed to read key from trusted CT log array entry at index %lu"
- "failed to read log_id from trusted CT log array entry at index %lu, computing log_id"
- "sqlite3"
- "v16@?0^{__SecRevocationDb=^{__OpaqueSecDb}^{dispatch_queue_s}BBB^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}}8"

```
