## CacheDelete

> `/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete`

```diff

-660.60.3.0.0
-  __TEXT.__text: 0x3276c
+660.102.1.0.0
+  __TEXT.__text: 0x326c8
   __TEXT.__auth_stubs: 0xc80
   __TEXT.__objc_methlist: 0x13c0
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x225a
-  __TEXT.__oslogstring: 0x5722
+  __TEXT.__cstring: 0x2254
+  __TEXT.__oslogstring: 0x5633
   __TEXT.__gcc_except_tab: 0xa4c
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0x990
   __TEXT.__objc_classname: 0x277
-  __TEXT.__objc_methname: 0x396d
+  __TEXT.__objc_methname: 0x3981
   __TEXT.__objc_methtype: 0xa0e
   __TEXT.__objc_stubs: 0x3760
   __DATA_CONST.__got: 0x70

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2a70
   __DATA_CONST.__objc_selrefs: 0x1020
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x188
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x1a0
   __AUTH_CONST.__cfstring: 0x1e80
   __AUTH_CONST.__objc_arrayobj: 0xa8

   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__auth_got: 0x650
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x188
-  __DATA.__objc_superrefs: 0x70
   __DATA.__objc_ivar: 0x14c
   __DATA.__data: 0x498
   __DATA.__bss: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 740
   Symbols:   2595
-  CStrings:  1696
+  CStrings:  1693
 
Symbols:
+ ___66-[CacheDeleteRemoteExtensionContext servicePurge:info:replyBlock:]_block_invoke.73
+ ___69-[CacheDeleteRemoteExtensionContext servicePeriodic:info:replyBlock:]_block_invoke.82
+ ___70-[CacheDeleteRemoteExtensionContext servicePurgeable:info:replyBlock:]_block_invoke.61
+ ___CallBlockWithProxy_block_invoke.299
+ ___block_descriptor_2208_e8_32r_e37_v32?0"NSTextCheckingResult"8Q16^B24lr32l8
+ ___block_literal_global.117
+ ___block_literal_global.42
+ ___block_literal_global.64
+ ___block_literal_global.75
+ ___block_literal_global.81
+ ___block_literal_global.84
+ ___block_literal_global.93
+ __unnamed_array_storage.72
+ __unnamed_array_storage.87
- ___66-[CacheDeleteRemoteExtensionContext servicePurge:info:replyBlock:]_block_invoke.72
- ___69-[CacheDeleteRemoteExtensionContext servicePeriodic:info:replyBlock:]_block_invoke.81
- ___70-[CacheDeleteRemoteExtensionContext servicePurgeable:info:replyBlock:]_block_invoke.60
- ___CallBlockWithProxy_block_invoke.297
- ___block_descriptor_2216_e8_32s40r_e37_v32?0"NSTextCheckingResult"8Q16^B24lr40l8s32l8
- ___block_literal_global.115
- ___block_literal_global.63
- ___block_literal_global.74
- ___block_literal_global.80
- ___block_literal_global.83
- ___block_literal_global.88
- __unnamed_array_storage.71
- __unnamed_array_storage.85
CStrings:
+ "%d CDRecentVolumeInfo _recentInfoAtUrgency, service: %@, amount: %@"
+ "%d updateServiceInfoAmount NO CHANGE for %{public}@ at %d on %{public}@"
+ "CacheDeleteVolume disk for %@ : %@"
+ "FSKit: (%s)"
+ "T@\"NSString\",?,R,C"
+ "[%s] no test parameters in info"
+ "apfs"
+ "multi volume:"
- " (%@)"
- "%d CDRecentVolumeInfo _recentInfoAtUrgency, volume: %@, urgency: %d, mdict: %@"
- "%d CDRecentVolumeInfo _recentInfoAtUrgency, volume: %@, urgency: %d, service: %@, amount: %@, recentServiceInfo %@"
- "%d updateServiceInfoAmount NO CHANGE for %{public}@ at %d on %{public}@, info: %{public}@"
- "%{public}@ : %{public}@%{public}@"
- "AppCache: returning existing AppCache object: %@"
- "CacheDeleteVolume disk for %@ : %@ : %@"
- "[%s] no test parameters in info: %@"
- "fstype: (%s)"
- "lifs"
- "multi volume %@"

```
