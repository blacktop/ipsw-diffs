## libSavageUpdater_iOS.dylib

> `/usr/lib/updaters/libSavageUpdater_iOS.dylib`

```diff

 6.19.0.0.0
-  __TEXT.__text: 0x108a8
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__cstring: 0x36e7
+  __TEXT.__text: 0x11b58
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__cstring: 0x3873
   __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__oslogstring: 0x4e5
+  __TEXT.__oslogstring: 0x6bb
   __TEXT.__unwind_info: 0x1cc
   __TEXT.__eh_frame: 0x74
   __TEXT.__objc_methname: 0x17c
   __TEXT.__objc_stubs: 0x200
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
+  __DATA_CONST.__objc_classrefs: 0x30
   __AUTH_CONST.__cfstring: 0xb00
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2c8
-  __DATA.__objc_classrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x2d0
   __DATA.__common: 0x30
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
-  UUID: 8E080C56-6D27-3E64-9A5E-D727CD731BFC
-  Functions: 123
-  Symbols:   459
-  CStrings:  449
+  UUID: 0F619A43-C5CA-3388-8E22-3A57D9138C0A
+  Functions: 125
+  Symbols:   464
+  CStrings:  484
 
Symbols:
+ _allocateAndMapObjectS3C1
+ _calloc
+ _fwrite
+ _malloc
+ _mapScheme3ObjectToISPANE
- _malloc_type_calloc
- _malloc_type_malloc
CStrings:
+ "\x1b[31mFAIL\x1b[0m"
+ "\x1b[32mSUCCESS\x1b[0m"
+ "Results of Allocation and Mapping Object Scheme3 Context1:\n"
+ "allocateAndMapObjectS3C1 -> 0x%x\n"
+ "allocateAndMapObjectS3C1: fourcc:%.4s mapObj:%d unmapObj:%d\n\n"
+ "aneMapFunction:\t\t%s\n"
+ "aneUnmapFunction:\t%s\n"
+ "dvaOffset:\t\t0x%X\n"
+ "ispMapFunction:\t\t%s\n"
+ "ispUnmapFunction:\t%s\n"
+ "mapScheme3Object -> 0x%x\n"
+ "mapScheme3Object: fourcc:%.4s\n\n"
+ "mappedToANE:\t\t%s\n"
+ "mappedToISP:\t\t%s\n"
+ "mappedToSEP:\t\t%s\n"
+ "objectFound:\t\t%s\n"
+ "objectSize:\t\t%d\n"
+ "replySize >= sizeof(cmd_alloc_map_s3c1_out_v1_t)"
+ "unmappedFromANE:\t%s\n"
+ "unmappedFromISP:\t%s\n"
+ "unmappedFromSEP:\t%s\n"

```
