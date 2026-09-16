## AssetCacheLocatorService

> `/System/Library/PrivateFrameworks/AssetCacheServices.framework/XPCServices/AssetCacheLocatorService.xpc/AssetCacheLocatorService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
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
-  __TEXT.__text: 0x1fb88
+157.40.2.0.0
+  __TEXT.__text: 0x1fe74
   __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_stubs: 0x3140
-  __TEXT.__objc_methlist: 0xfc4
+  __TEXT.__objc_stubs: 0x31a0
+  __TEXT.__objc_methlist: 0xfdc
   __TEXT.__const: 0x1ff
   __TEXT.__gcc_except_tab: 0x2d0
-  __TEXT.__cstring: 0x230f
-  __TEXT.__objc_methname: 0x39c1
-  __TEXT.__oslogstring: 0x297f
+  __TEXT.__cstring: 0x2381
+  __TEXT.__objc_methname: 0x3a34
+  __TEXT.__oslogstring: 0x2a64
   __TEXT.__objc_classname: 0xf0
   __TEXT.__objc_methtype: 0xf1f
   __TEXT.__unwind_info: 0x5f8
   __DATA_CONST.__const: 0xbe0
-  __DATA_CONST.__cfstring: 0x1f80
+  __DATA_CONST.__cfstring: 0x1fa0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0x330
-  __DATA.__objc_const: 0x19e8
-  __DATA.__objc_selrefs: 0xde0
-  __DATA.__objc_ivar: 0x124
+  __DATA.__objc_const: 0x1a18
+  __DATA.__objc_selrefs: 0xdf8
+  __DATA.__objc_ivar: 0x128
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 496
+  Functions: 498
   Symbols:   358
-  CStrings:  1270
+  CStrings:  1286
 
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
