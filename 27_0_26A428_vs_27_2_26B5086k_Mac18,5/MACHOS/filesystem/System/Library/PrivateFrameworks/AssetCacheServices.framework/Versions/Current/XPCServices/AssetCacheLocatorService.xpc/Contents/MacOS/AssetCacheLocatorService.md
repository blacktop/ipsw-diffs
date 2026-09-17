## AssetCacheLocatorService

> `/System/Library/PrivateFrameworks/AssetCacheServices.framework/Versions/Current/XPCServices/AssetCacheLocatorService.xpc/Contents/MacOS/AssetCacheLocatorService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-157.0.0.0.0
-  __TEXT.__text: 0x26138
+157.40.2.0.0
+  __TEXT.__text: 0x264c0
   __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_stubs: 0x33e0
-  __TEXT.__objc_methlist: 0x10c4
+  __TEXT.__objc_stubs: 0x3440
+  __TEXT.__objc_methlist: 0x10dc
   __TEXT.__const: 0x21d
-  __TEXT.__cstring: 0x252a
+  __TEXT.__cstring: 0x259c
   __TEXT.__objc_classname: 0xfe
   __TEXT.__objc_methtype: 0xf81
   __TEXT.__gcc_except_tab: 0x4c8
-  __TEXT.__objc_methname: 0x3da6
-  __TEXT.__oslogstring: 0x2ef8
-  __TEXT.__unwind_info: 0x738
+  __TEXT.__objc_methname: 0x3e19
+  __TEXT.__oslogstring: 0x2fdd
+  __TEXT.__unwind_info: 0x740
   __DATA_CONST.__const: 0xf08
-  __DATA_CONST.__cfstring: 0x2120
+  __DATA_CONST.__cfstring: 0x2140
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__auth_got: 0x638
   __DATA_CONST.__got: 0x310
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x1ae8
-  __DATA.__objc_selrefs: 0xea0
-  __DATA.__objc_ivar: 0x134
+  __DATA.__objc_const: 0x1b18
+  __DATA.__objc_selrefs: 0xeb8
+  __DATA.__objc_ivar: 0x138
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 593
+  Functions: 596
   Symbols:   339
-  CStrings:  1353
+  CStrings:  1369
 
CStrings:
+ " [LONG-TTL negative]"
+ "#%08x [%s] %@ hit: %@ (from cache, %.0fs validity remaining)"
+ "#%08x [%s] locate outcome: http=%lu reason=%{public}s servers=%ld->%ld validity=%.0f%s retryAfter=%{public}s"
+ "#%08x [%s] locate outcome: transport-error=%ld (%{public}@) — no HTTP response"
+ "Retry-After"
+ "T@\"NSString\",C,V_locateRetryAfter"
+ "_locateRetryAfter"
+ "empty-200"
+ "http-503"
+ "http-error"
+ "locateRetryAfter"
+ "parse-error"
+ "parsed"
+ "server-cert-untrusted"
+ "setLocateRetryAfter:"
+ "valueForHTTPHeaderField:"
+ "zero-byte"
- "#%08x [%s] %@ hit: %@"
```
