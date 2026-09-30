## DiskImages

> `/System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages`

```diff

-683.160.3.0.0
-  __TEXT.__text: 0x89694
+683.160.3.701.2
+  __TEXT.__text: 0x896e0
   __TEXT.__auth_stubs: 0x2430
   __TEXT.__objc_methlist: 0x364
-  __TEXT.__cstring: 0x248c6
+  __TEXT.__cstring: 0x24908
   __TEXT.__gcc_except_tab: 0x2104
   __TEXT.__const: 0x181b
   __TEXT.__oslogstring: 0x72f

   - /usr/lib/libz.1.dylib
   Functions: 2458
   Symbols:   3770
-  CStrings:  3604
+  CStrings:  3605
 
Functions:
~ __ZN14CUDIFDiskImage11isValidBLKXEPP10UDIFBlocksx : 1724 -> 1668
~ __ZN14CUDIFDiskImage31generateGlobalBLKXFromBLKXTableEv : 812 -> 880
~ __ZN20CDARTRLEDecompressor14decompressDataEPKviPvi : 200 -> 264
CStrings:
+ "error: chunk %d uncompressed size %qd exceeds limit %lu\n"
+ "error: compressed run uncompressed size %qd exceeds limit %lu\n"
- "error: chunk %d has too many blocks %qd expected %ld\n"
```
