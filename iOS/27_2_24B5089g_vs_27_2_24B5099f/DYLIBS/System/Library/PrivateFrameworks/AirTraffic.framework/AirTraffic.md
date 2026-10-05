## AirTraffic

> `/System/Library/PrivateFrameworks/AirTraffic.framework/AirTraffic`

```diff

-4026.200.7.0.0
-  __TEXT.__text: 0x183c8
+4026.200.21.0.0
+  __TEXT.__text: 0x18540
   __TEXT.__objc_methlist: 0x23d4
-  __TEXT.__const: 0x68
+  __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x578
-  __TEXT.__cstring: 0x1786
-  __TEXT.__oslogstring: 0x1541
+  __TEXT.__cstring: 0x1774
+  __TEXT.__oslogstring: 0x1544
   __TEXT.__unwind_info: 0x920
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1510
+  __DATA_CONST.__objc_selrefs: 0x1528
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__got: 0x2e0
   __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x1da0
+  __AUTH_CONST.__cfstring: 0x1de0
   __AUTH_CONST.__objc_const: 0x3cd0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 808
-  Symbols:   1643
-  CStrings:  427
+  Symbols:   1647
+  CStrings:  425
 
Symbols:
+ _mkdirat
+ _open
+ _renameatx_np
+ _unlinkat
Functions:
~ -[ATAirlock processCompletedAsset:] : 1788 -> 2164
CStrings:
+ "."
+ "/"
+ "Airlock moved %{public}@ to %{public}@ beneath AFC root"
+ "Could not create directory %{public}@ beneath AFC root: %{errno}d"
+ "Could not open AFC root %{public}@: %{errno}d"
+ "Failed to move completed file for asset %{public}@ after retry, error: %{errno}d (path '%{public}@')"
+ "Failed to move completed file for asset %{public}@ beneath AFC root, error: %{errno}d (path '%{public}@')"
+ "Failed to remove completed upload for asset %{public}@, error: %{public}@"
- "Airlock destination directory not present, creating %{public}@"
- "Airlock moved %{public}@ to %{pubic}@"
- "Cannot move asset outside of AFC root: %{public}@"
- "Could not create directory %{public}@, error: %{public}@"
- "Failed ro remove completed upload for asset %{public}@, error: %{public}@"
- "Failed to move completed file for asset %{public}@, error: %{public}@"
- "File already exists at %{public}@, removing"
- "Source %s: %{public}@, Destination %s: %{public}@"
- "does not exist"
- "exists"
```
