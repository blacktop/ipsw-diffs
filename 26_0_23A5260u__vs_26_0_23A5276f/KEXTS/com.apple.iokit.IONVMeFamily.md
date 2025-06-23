## com.apple.iokit.IONVMeFamily

> `com.apple.iokit.IONVMeFamily`

```diff

-815.0.0.0.1
+818.0.0.0.0
   __TEXT.__const: 0x6f8
-  __TEXT.__cstring: 0xe200
-  __TEXT_EXEC.__text: 0x5e558
+  __TEXT.__cstring: 0xe218
+  __TEXT_EXEC.__text: 0x5e88c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4e4
   __DATA.__common: 0x528

   __DATA_CONST.__got: 0x188
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
-  __DATA_CONST.__const: 0xce18
+  __DATA_CONST.__const: 0xce58
   __DATA_CONST.__kalloc_type: 0x7c0
   __DATA_CONST.__kalloc_var: 0x690
-  UUID: A8820A08-CEB6-38F8-90B5-AB90EBE0C070
-  Functions: 3189
+  UUID: C2CBE851-A4B8-3A78-9676-9508D330E752
+  Functions: 3193
   Symbols:   0
-  CStrings:  1606
+  CStrings:  1607
 
CStrings:
+ "%s::%d:linkStatus: 0x%X\n"
+ "( ( fHeader->imageCount + 1 ) <= 150 )"
+ "( ( fHeader->totalBytesWritten + ( size_t ) ( inImageSize - fHeader->image[inImageIndex].imageSize ) ) <= fHeader->totalSize )"
+ "( ( fHeader->totalBytesWritten + inImageSize ) <= fHeader->totalSize )"
+ "( 0 != fHeader )"
+ "( imageCRC32 == fHeader->image[imageIndex].checksum )"
+ "( inImageSize == fHeader->image[imageIndex].imageSize )"
+ "( isKeyAllowed == true )"
+ "High Throughput Options"
- "%s::%d:linkStatus: %d\n"
- "( ( header->imageCount + 1 ) <= 150 )"
- "( ( header->totalBytesWritten + ( size_t ) ( inImageSize - header->image[inImageIndex].imageSize ) ) <= header->totalSize )"
- "( ( header->totalBytesWritten + inImageSize ) <= header->totalSize )"
- "( 0 != fHeaderBuffer )"
- "( imageCRC32 == header->image[imageIndex].checksum )"
- "( inImageSize == header->image[imageIndex].imageSize )"
- "( isKeyOnAllowList == true )"

```
