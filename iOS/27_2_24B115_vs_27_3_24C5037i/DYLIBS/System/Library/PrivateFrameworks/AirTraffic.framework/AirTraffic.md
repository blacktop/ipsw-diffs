## AirTraffic

> `/System/Library/PrivateFrameworks/AirTraffic.framework/AirTraffic`

```diff

-4026.200.21.0.0
-  __TEXT.__text: 0x18540
+4026.300.13.0.0
+  __TEXT.__text: 0x186f0
   __TEXT.__objc_methlist: 0x23d4
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x578
   __TEXT.__cstring: 0x1774
-  __TEXT.__oslogstring: 0x1544
+  __TEXT.__oslogstring: 0x1600
   __TEXT.__unwind_info: 0x920
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1528
+  __DATA_CONST.__objc_selrefs: 0x1540
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x50

   - /usr/lib/libobjc.A.dylib
   Functions: 808
   Symbols:   1647
-  CStrings:  425
+  CStrings:  427
 
Functions:
~ -[ATAirlock purgeAssetWithIdentifier:dataclass:] : 304 -> 736
CStrings:
+ "Refusing to purge %{public}@ with identifier %{public}@: path %{public}@ escapes its dataclass directory"
+ "Refusing to purge asset with invalid dataclass %{public}@ or identifier %{public}@"
```
