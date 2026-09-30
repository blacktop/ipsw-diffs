## SiriFindMy

> `/System/Library/PrivateFrameworks/SiriFindMy.framework/Versions/A/SiriFindMy`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3530.1.1.0.0
-  __TEXT.__text: 0x1a1f64
-  __TEXT.__auth_stubs: 0x4aa0
+3530.1.1.1.0
+  __TEXT.__text: 0x1a94d4
+  __TEXT.__auth_stubs: 0x4ae0
   __TEXT.__objc_methlist: 0x17c8
-  __TEXT.__const: 0x13e18
-  __TEXT.__swift5_typeref: 0x7978
+  __TEXT.__const: 0x13e48
+  __TEXT.__swift5_typeref: 0x7972
   __TEXT.__swift5_fieldmd: 0x4dc8
-  __TEXT.__constg_swiftt: 0x5afc
+  __TEXT.__constg_swiftt: 0x5b0c
   __TEXT.__swift5_builtin: 0x294
   __TEXT.__swift5_reflstr: 0x3a58
   __TEXT.__swift5_assocty: 0xb58
-  __TEXT.__oslogstring: 0x7085
+  __TEXT.__oslogstring: 0x7585
   __TEXT.__swift5_protos: 0x118
   __TEXT.__swift5_proto: 0xe0c
   __TEXT.__swift5_types: 0x5e4
   __TEXT.__cstring: 0x27b2
-  __TEXT.__swift5_capture: 0x1540
+  __TEXT.__swift5_capture: 0x1570
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__swift_as_entry: 0x58c
-  __TEXT.__swift_as_ret: 0x908
-  __TEXT.__unwind_info: 0x6dc0
-  __TEXT.__eh_frame: 0xd604
+  __TEXT.__swift_as_entry: 0x590
+  __TEXT.__swift_as_ret: 0x928
+  __TEXT.__unwind_info: 0x6e50
+  __TEXT.__eh_frame: 0xd84c
   __TEXT.__objc_classname: 0xc21
-  __TEXT.__objc_methname: 0x6507
+  __TEXT.__objc_methname: 0x6577
   __TEXT.__objc_methtype: 0xfba
-  __TEXT.__objc_stubs: 0x2880
-  __DATA_CONST.__got: 0xcb0
+  __TEXT.__objc_stubs: 0x28c0
+  __DATA_CONST.__got: 0xcb8
   __DATA_CONST.__const: 0x518
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13e8
+  __DATA_CONST.__objc_selrefs: 0x13f8
   __DATA_CONST.__objc_protorefs: 0x58
-  __AUTH_CONST.__auth_got: 0x2558
-  __AUTH_CONST.__const: 0xcff0
+  __AUTH_CONST.__auth_got: 0x2578
+  __AUTH_CONST.__const: 0xd070
   __AUTH_CONST.__objc_const: 0x4c58
   __AUTH.__objc_data: 0x1e18
   __AUTH.__data: 0x2960
-  __DATA.__data: 0x5070
+  __DATA.__data: 0x5080
   __DATA.__bss: 0x18380
-  __DATA.__common: 0x4f8
+  __DATA.__common: 0x510
   __DATA_DIRTY.__objc_data: 0xa8
-  __DATA_DIRTY.__data: 0xc98
+  __DATA_DIRTY.__data: 0xc90
   __DATA_DIRTY.__common: 0x60
   __DATA_DIRTY.__bss: 0x1380
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10691
-  Symbols:   3335
-  CStrings:  2078
+  Functions: 10745
+  Symbols:   3336
+  CStrings:  2090
 
Symbols:
+ _objc_msgSend$containerURLForSecurityApplicationGroupIdentifier:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
- _symbolic _____ 10Foundation3URLV
CStrings:
+ "Cache file %{public}s does not exist"
+ "Could not parse %{public}s using PropertyListDecoder"
+ "Could not read data from cache file at %{public}s"
+ "Deleted old cache file at %{public}s"
+ "Device is not a watch or a home accessory, sending empty pre handle intent output."
+ "Device is on a home accessory. We will not speak the failure message because we have opened up the person module on the accessory"
+ "DiskCacher.evict: Could not delete the cache file at %{public}s due to %{public}s"
+ "DiskCacher.evict: No cache location available for this process; nothing to do"
+ "DiskCacher.getEntry: No cache location available for this process; reporting a cache miss"
+ "DiskCacher.getOldSystemCacheURL: Could not find cache directory"
+ "DiskCacher.getSystemCacheURL: Failed to get container URL for app group '%{public}s'. Disk caching is disabled for this process. This can happen if the running binary is not a member of the app group (missing/unsigned entitlement), the process is not running in a per-user sandboxed context, or the group container has not been provisioned."
+ "DiskCacher.removeOldCacheFile: Old cache file to delete: %{public}s"
+ "DiskCacher.setEntry: Could not write cache file %{public}s due to %{public}s"
+ "DiskCacher.setEntry: No cache location available for this process; skipping disk write"
+ "DiskCacher.setEntry: Wrote cache to %{public}s"
+ "Failed to delete old cache file at %{public}s due to %{public}s"
+ "Request originated from personal request device (HomeAccessory/HomePod), skipping unlock check."
+ "beats_powerbeats_snap"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "group.com.apple.siri.findmy"
- "Cache file %s does not exist"
- "Could not delete the cache file at %s due to %{public}s"
- "Could not find cache directory"
- "Could not parse %s using PropertyListDecoder"
- "Could not read data from cache file at %s"
- "Could not write cache file %s due to %{public}s"
- "Device is not a watch, sending empty pre handle intent output."
- "SiriFindMy/Caching.swift"
- "Wrote cache to %s"
```
