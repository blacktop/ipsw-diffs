## com.apple.driver.DiskImages

> `com.apple.driver.DiskImages`

```diff

-710.0.0.0.0
-  __TEXT.__cstring: 0xda8
-  __TEXT_EXEC.__text: 0x9220
+710.60.2.0.0
+  __TEXT.__cstring: 0xe76
+  __TEXT_EXEC.__text: 0x927c
   __TEXT_EXEC.__auth_stubs: 0x470
   __DATA.__data: 0xc8
   __DATA.__common: 0x128

   __DATA_CONST.__got: 0xa0
   Functions: 265
   Symbols:   0
-  CStrings:  153
+  CStrings:  155
 
Functions:
~ __ZN13IOHDIXHDDrive19processPropertyListEv : 884 -> 976
CStrings:
+ "710.60.2"
+ "IOHDIXHDDrive::processPropertyList: rejecting attach, bad block-size multiple %llu (rdar://185717528)\n"
+ "IOHDIXHDDrive::processPropertyList: rejecting attach, non-512 block size %lld (rdar://185717528)\n"
- "710"
```
