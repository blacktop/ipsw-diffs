## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3404.58.2.0.0
-  __TEXT.__text: 0x689a0
+3404.60.1.1.1
+  __TEXT.__text: 0x68ddc
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x34d8
+  __TEXT.__objc_methlist: 0x34f8
   __TEXT.__const: 0xf8
   __TEXT.__dlopen_cstrs: 0x296
   __TEXT.__gcc_except_tab: 0x1358
-  __TEXT.__cstring: 0x9e5d
-  __TEXT.__oslogstring: 0xbbc1
-  __TEXT.__unwind_info: 0x1158
+  __TEXT.__cstring: 0x9f04
+  __TEXT.__oslogstring: 0xbca0
+  __TEXT.__unwind_info: 0x1168
   __TEXT.__objc_classname: 0x424
-  __TEXT.__objc_methname: 0x9f26
+  __TEXT.__objc_methname: 0x9fb2
   __TEXT.__objc_methtype: 0xfe4
-  __TEXT.__objc_stubs: 0x8100
+  __TEXT.__objc_stubs: 0x8180
   __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__const: 0x1b40
+  __DATA_CONST.__const: 0x1b60
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26f0
+  __DATA_CONST.__objc_selrefs: 0x2710
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x5b0
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x40a0
+  __AUTH_CONST.__cfstring: 0x40e0
   __AUTH_CONST.__objc_const: 0x42d0
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0xd8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1408
-  Symbols:   2009
-  CStrings:  3616
+  Functions: 1411
+  Symbols:   2012
+  CStrings:  3627
 
CStrings:
+ "%s Could not parse atomic instance from '%{public}@': uuid: '%{public}@'"
+ "%s Latest atomic instance for '%{public}@': %{public}@"
+ "%s No destination for current lock for asset set '%{public}@' at path '%{public}@': %{public}@"
+ "+[UAFAutoAssetManager atomicInstanceFromLockPath:]"
+ "+[UAFAutoAssetManager latestAtomicInstanceForClients:]"
+ "+[UAFAutoAssetManager setBackgroundNeedPolicy:configuration:]"
+ "atomicInstanceFromLockPath:"
+ "atomic_instance_"
+ "atomic_instance_latest.locker"
+ "currentLockURLForAssetSet:"
+ "destinationOfSymbolicLinkAtPath:error:"
+ "latestAtomicInstanceForClients:"
+ "setBackgroundNeedPolicy:configuration:"
- "+[UAFAutoAssetManager setBackgroundNeedPolicy:]"
- "setBackgroundNeedPolicy:"

```
