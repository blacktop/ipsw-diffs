## libCoreFSCache.dylib

> `/System/Library/Frameworks/OpenGLES.framework/libCoreFSCache.dylib`

```diff

-352.2.0.0.0
-  __TEXT.__text: 0x5e10 sha256:5052c01c04b218d301cbddd7f705bcf9fd101d48130e8917da53483de5f0a350
-  __TEXT.__auth_stubs: 0x350 sha256:78886e409b35099a106c9e2a683d66acdb369ffb072f2420af57832c8d88fbcb
-  __TEXT.__const: 0xb0 sha256:dd78910ea081b3c37649b9cf1e623017084db265b99adbf28351e851b418d606
-  __TEXT.__cstring: 0x29a sha256:bb4e51e8e2415875ddee93d7e20d11d10daca99867d9a52981d873f79694e230
-  __TEXT.__oslogstring: 0xb9a sha256:014b07cf5c88adc1738bc2cf4e5a4a203289129410fa2256bf01707a958e2af8
-  __TEXT.__unwind_info: 0x140 sha256:c157990c00427718291eadc3db16e7289d6d043cd1f185aa59097656a6858798
+352.3.0.0.0
+  __TEXT.__text: 0x6084 sha256:f9b1d04c7998a648b5bea0b99bc4fbd4c868fed3d3d290f6795b831899ee874a
+  __TEXT.__auth_stubs: 0x350 sha256:55fa58dbbf5106e73cc5a20351f3fabf75875e056af54a37944bfaeaa404dce3
+  __TEXT.__const: 0xc0 sha256:f5e61b303ba03cb8905c97b1be0682a2ff966ff6d75c6b9d73226844f07dc263
+  __TEXT.__cstring: 0x29c sha256:1befd5246ef5b556e960c8edcf80222a946646fb85e1f6dd9b5973329609e654
+  __TEXT.__oslogstring: 0xcbd sha256:830ac249422cab8cb9752478c369488457390a026a97a3a6fb00adfa27572490
+  __TEXT.__unwind_info: 0x138 sha256:362b59a3b7985230d508a43f4e65eacacfd03d95bd3183cd938867ddd2292284
   __DATA_CONST.__got: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
-  __DATA_CONST.__const: 0x58 sha256:5f7ef6caa254147447de6393354385ec3de4298ae87b1d0c6a7d0736f710b8e5
+  __DATA_CONST.__const: 0x58 sha256:399bbe6f815eec4560e0fc40244d11d4d47f5759db1f2b3e5ab02a7f7f5fcfb3
   __AUTH_CONST.__auth_got: 0x1a8 sha256:e6a4dd1cc11fe045554f993bb765eba87d46248a8b85a7c8dbaa5c40594e0214
-  __AUTH_CONST.__const: 0x30 sha256:9ed517c081791c0c518afef86d96881537c3e46daf1d4c880064142b76483868
-  __AUTH_CONST.__cfstring: 0x20 sha256:ee9011647d25bf36a1858d8d5e0b9b552a91157581f5522836df66c4e31b6bcc
+  __AUTH_CONST.__const: 0x30 sha256:263ee04e0960e40b50a8f212f54ba24d8a0228247e0ddec21c8e650ba9831424
+  __AUTH_CONST.__cfstring: 0x20 sha256:3041dd834d00403aa14aec38d027909c33fdea041e2f4d9df05617e934313718
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 7D362A25-C038-35F5-BEC4-B6FC6E09C771
-  Functions: 122
-  Symbols:   293
-  CStrings:  84
+  UUID: D3FD7F81-5A77-361A-946A-4D8ED1EAD044
+  Functions: 127
+  Symbols:   303
+  CStrings:  89
 
Symbols:
+ _OUTLINED_FUNCTION_9
+ ___block_descriptor_tmp.26
+ _fscache_open_worker.cold.19
+ _heap_alloc.cold.3
+ _open_data_file.cold.7
+ _reset_cache.cold.4
- ___block_descriptor_tmp.25
CStrings:
+ "Unexpected: in-memory page-aligned size: %zu is larger than read-only on-disk file size: %zu by more than a page. Page size is %zu."
+ "fopen for resetting cache not permitted on read-only cache file."
+ "r"
+ "read-only cache is invalid or missing; not reinitializing"
+ "refusing to reset a read-only cache"

```
