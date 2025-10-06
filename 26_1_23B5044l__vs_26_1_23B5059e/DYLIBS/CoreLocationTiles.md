## CoreLocationTiles

> `/System/Library/PrivateFrameworks/CoreLocationTiles.framework/CoreLocationTiles`

```diff

-3060.0.8.0.2
-  __TEXT.__text: 0x1ff0
+3060.0.16.0.0
+  __TEXT.__text: 0x1fec
   __TEXT.__auth_stubs: 0x3d0
   __TEXT.__objc_methlist: 0xf8
   __TEXT.__const: 0xc9
   __TEXT.__cstring: 0x354
-  __TEXT.__oslogstring: 0x89c
+  __TEXT.__oslogstring: 0x899
   __TEXT.__gcc_except_tab: 0x180
   __TEXT.__unwind_info: 0x190
   __TEXT.__objc_classname: 0x32

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2EA7E086-B4A7-36A3-9D21-824B184C3D6B
+  UUID: 47EBB058-D608-359E-A19B-710083A5D497
   Functions: 48
   Symbols:   568
   CStrings:  131
Functions:
~ -[CLTileRemoteDownloader downloadAndDecompressFrom:toDecompressedDestination:withTimeout:withCompletionHandler:] : 1632 -> 1628
CStrings:
+ "{\"msg%{public}.0s\":\"#TileRemoteDownloader - starting request\", \"self\":\"%{public}p\", \"connection\":\"%{public}p\", \"canDownloadOverCellular\":%{public}hhd, \"srcURL\":%{public, location:escape_only}@, \"decompressedDestination\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#TileRemoteDownloader Ignoring new download request with invalid source string\", \"URLString\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#TileRemoteDownloader Ignoring new download request with invalid source url\", \"URL\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#TileRemoteDownloader - starting request\", \"self\":\"%{public}p\", \"connection\":\"%{public}p\", \"canDownloadOverCellular\":%{public}hhd, \"srcURL\":%{private, location:escape_only}@, \"decompressedDestination\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#TileRemoteDownloader Ignoring new download request with invalid source string\", \"URLString\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#TileRemoteDownloader Ignoring new download request with invalid source url\", \"URL\":%{private, location:escape_only}@}"

```
