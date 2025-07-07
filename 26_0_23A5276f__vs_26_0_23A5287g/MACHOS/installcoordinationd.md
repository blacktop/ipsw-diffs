## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-763.0.0.502.1
-  __TEXT.__text: 0xa3508
-  __TEXT.__auth_stubs: 0x1120
-  __TEXT.__objc_stubs: 0xaf20
-  __TEXT.__objc_methlist: 0x5d2c
+769.0.0.0.0
+  __TEXT.__text: 0xa37b0
+  __TEXT.__auth_stubs: 0x1130
+  __TEXT.__objc_stubs: 0xaf40
+  __TEXT.__objc_methlist: 0x5d3c
   __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x18b3f
-  __TEXT.__objc_methname: 0x10dd0
+  __TEXT.__cstring: 0x18b1d
+  __TEXT.__objc_methname: 0x10dde
   __TEXT.__objc_classname: 0xa21
   __TEXT.__objc_methtype: 0x23a7
-  __TEXT.__oslogstring: 0xdd8b
-  __TEXT.__gcc_except_tab: 0x2b98
+  __TEXT.__oslogstring: 0xddf5
+  __TEXT.__gcc_except_tab: 0x2ab8
   __TEXT.__ustring: 0x1a64
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x2500
-  __DATA_CONST.__auth_got: 0x8a0
+  __TEXT.__unwind_info: 0x2518
+  __DATA_CONST.__auth_got: 0x8a8
   __DATA_CONST.__got: 0x458
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2be8
-  __DATA_CONST.__cfstring: 0x9ca0
+  __DATA_CONST.__const: 0x2bf8
+  __DATA_CONST.__cfstring: 0x9ce0
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xc4b0
-  __DATA.__objc_selrefs: 0x33a8
+  __DATA.__objc_const: 0xc4c0
+  __DATA.__objc_selrefs: 0x33b0
   __DATA.__objc_ivar: 0x4b0
   __DATA.__objc_data: 0x1720
   __DATA.__data: 0x6b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2EC04E9E-3CCC-3CAF-824F-245D880EED9D
-  Functions: 3301
-  Symbols:   428
-  CStrings:  6807
+  UUID: E86D4705-D4F9-3117-BC10-9CF60A414554
+  Functions: 3304
+  Symbols:   429
+  CStrings:  6814
 
Symbols:
+ _CacheDeletePurgeSpaceWithInfoSync
CStrings:
+ "%s: %@ : %llu bytes needed, %llu bytes available.  %llu bytes can be purged, requesting %llu bytes be purged."
+ "%s: Failed to get available space on device for %@: %s"
+ "%s: Not enough space for %@ : %llu bytes needed, %llu bytes available (%llu free, %llu purgable). : %@"
+ "%s: Not enough space for %@ : %llu bytes needed, %llu bytes available (%llu free, purgable unavailable). : %@"
+ "%s: Not enough space for for %@ : %llu bytes needed, %llu bytes available (%llu bytes were purged). : %@"
+ "%s: Path %@ : %llu bytes purged, enough available"
+ "%s: Preflight for %@: %llu bytes needed, %llu bytes available."
+ "%s: Preflight for %@: bytes consumed (%llu) greater than total bytes needed (%llu): space needed cannot be determined."
+ "%s: WARNING: Preflight called on %@ which assumes data will end up on the volume containing %@; this may not be accurate."
+ "-[IXSDataPromise preflightPath]"
+ "03:51:13"
+ "AdditionalDiskSpaceRequired"
+ "IXPreflightWithCacheDelete"
+ "IXPreflightWithCacheDelete_block_invoke"
+ "Jun 27 2025"
+ "Not enough space for %@ : %llu bytes needed, %llu bytes available (%llu free, %llu purgable)."
+ "Not enough space for %@ : %llu bytes needed, %llu bytes available (%llu free, purgable unavailable)."
+ "Not enough space for for %@ : %llu bytes needed, %llu bytes available (%llu bytes were purged)."
+ "TotalDiskSpaceRequired"
+ "preflightPath"
- "%s: %llu bytes purged, enough for promise %@."
- "%s: Failed to get available space on device for promise %@: %s"
- "%s: Not enough space for promise %@: %llu bytes needed, %llu bytes available (%llu bytes were purged). : %@"
- "%s: Not enough space for promise %@: %llu bytes needed, %llu bytes available (%llu free, %llu purgable). : %@"
- "%s: Not enough space for promise %@: %llu bytes needed, %llu bytes available (%llu free, purgable unavailable). : %@"
- "%s: Promise %@: %llu bytes needed, %llu bytes available."
- "%s: Promise %@: %llu bytes needed, %llu bytes available.  %llu bytes can be purged, requesting %llu bytes be purged."
- "%s: Promise %@: bytes consumed (%llu) greater than total bytes needed (%llu): space needed cannot be determined."
- "-[IXSDataPromise(IXSDataPromiseIPCMethods) _remote_preflightWithCompletion:]"
- "-[IXSDataPromise(IXSDataPromiseIPCMethods) _remote_preflightWithCompletion:]_block_invoke"
- "22:31:58"
- "Jun 16 2025"
- "Not enough space for promise %@: %llu bytes needed, %llu bytes available (%llu bytes were purged)."
- "Not enough space for promise %@: %llu bytes needed, %llu bytes available (%llu free, %llu purgable)."
- "Not enough space for promise %@: %llu bytes needed, %llu bytes available (%llu free, purgable unavailable)."

```
