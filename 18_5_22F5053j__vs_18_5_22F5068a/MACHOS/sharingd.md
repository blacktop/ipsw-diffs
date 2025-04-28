## sharingd

> `/usr/libexec/sharingd`

```diff

-2060.60.31.0.0
-  __TEXT.__text: 0x6ad238
+2060.60.41.2.3
+  __TEXT.__text: 0x6ad4a0
   __TEXT.__auth_stubs: 0x9470
-  __TEXT.__objc_stubs: 0x34980
-  __TEXT.__objc_methlist: 0x1f7b4
-  __TEXT.__cstring: 0x47413
-  __TEXT.__objc_methname: 0x49e24
+  __TEXT.__objc_stubs: 0x349c0
+  __TEXT.__objc_methlist: 0x1f7c4
+  __TEXT.__cstring: 0x474e3
+  __TEXT.__objc_methname: 0x49e60
   __TEXT.__objc_classname: 0x2dd6
   __TEXT.__objc_methtype: 0xa393
   __TEXT.__const: 0x14668

   __DATA_CONST.__got: 0x3300
   __DATA_CONST.__auth_ptr: 0x2390
   __DATA_CONST.__const: 0x1d2d8
-  __DATA_CONST.__cfstring: 0x198e0
+  __DATA_CONST.__cfstring: 0x19900
   __DATA_CONST.__objc_classlist: 0xee0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x6d8

   __DATA_CONST.__objc_dictobj: 0x16f8
   __DATA_CONST.__objc_arrayobj: 0x6f0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x3afa8
-  __DATA.__objc_selrefs: 0x11058
-  __DATA.__objc_ivar: 0x2ad0
+  __DATA.__objc_const: 0x3afc8
+  __DATA.__objc_selrefs: 0x11068
+  __DATA.__objc_ivar: 0x2ad4
   __DATA.__objc_data: 0xae30
   __DATA.__data: 0x1a4a0
   __DATA.__bss: 0x14bb8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 26950
+  Functions: 26952
   Symbols:   4294
-  CStrings:  28134
+  CStrings:  28142
 
CStrings:
+ "\x11\x12)\x12A\x14!\x11A\x12"
+ "-[SDHotspotAgent _discoveryCachedDeviceFor:]"
+ "Found device without hotspot info and without recently cached info: %@"
+ "Found valid cached device: %@"
+ "Handoff active for %@, using cached device: %@"
+ "Stale hotspot info cache seconds overridden: %d -> %d\n"
+ "Using cached device found for %@: %@"
+ "_discoveryCachedDeviceFor:"
+ "_prefStaleCacheInfoSecs"
+ "hsStaleCacheSecs"
+ "lastSeen"
- "\x11\x12)\x12A\x14!\x111\x12"
- "Found device without hotspot info: %@"
- "Using cached info for %@ due to handoff advertisement: %@"

```
