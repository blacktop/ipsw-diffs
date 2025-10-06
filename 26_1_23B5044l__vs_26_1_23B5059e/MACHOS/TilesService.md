## TilesService

> `/System/Library/PrivateFrameworks/CoreLocationTiles.framework/XPCServices/TilesService.xpc/TilesService`

```diff

-3060.0.8.0.2
-  __TEXT.__text: 0x6508
+3060.0.16.0.0
+  __TEXT.__text: 0x6530
   __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0x640
+  __TEXT.__objc_stubs: 0x660
   __TEXT.__objc_methlist: 0x2f4
-  __TEXT.__const: 0x1a0
+  __TEXT.__const: 0x198
   __TEXT.__gcc_except_tab: 0x3e8
   __TEXT.__cstring: 0x6fb
-  __TEXT.__oslogstring: 0x19d2
+  __TEXT.__oslogstring: 0x19fc
   __TEXT.__objc_classname: 0x84
-  __TEXT.__objc_methname: 0x91b
+  __TEXT.__objc_methname: 0x92a
   __TEXT.__objc_methtype: 0x5d2
-  __TEXT.__unwind_info: 0x378
+  __TEXT.__unwind_info: 0x380
   __DATA_CONST.__auth_got: 0x2b8
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x378

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x4c0
-  __DATA.__objc_selrefs: 0x2c0
+  __DATA.__objc_selrefs: 0x2c8
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x9f0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B1B93724-2622-3FD8-A250-E10EC04E9388
+  UUID: CE5D070E-88F6-3A73-A178-3803AC5E561F
   Functions: 139
   Symbols:   147
-  CStrings:  287
+  CStrings:  288
 
Functions:
~ __ZN14CLTilesService21handleDownloadRequestENSt3__110shared_ptrI12CLConnectionEENS1_I19CLConnectionMessageEE : 1248 -> 1288
CStrings:
+ "absoluteString"
+ "{\"msg%{public}.0s\":\"#TilesService starting download request\", \"connection\":\"%{public}p\", \"timeout\":\"%{public}f\", \"allowsCellular\":%{public}hhd, \"source\":%{public, location:escape_only}s, \"request\":%{public, location:escape_only}@, \"destination\":%{private, location:escape_only}@, \"numCurrentDownloads\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#TilesService starting download request\", \"connection\":\"%{public}p\", \"timeout\":\"%{public}f\", \"allowsCellular\":%{public}hhd, \"request\":%{private, location:escape_only}@, \"destination\":%{private, location:escape_only}@, \"numCurrentDownloads\":%{public}lu}"

```
