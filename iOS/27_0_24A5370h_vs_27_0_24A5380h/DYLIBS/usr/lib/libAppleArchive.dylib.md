## libAppleArchive.dylib

> `/usr/lib/libAppleArchive.dylib`

```diff

-  __TEXT.__text: 0x832a0
+  __TEXT.__text: 0x832cc
   __TEXT.__cstring: 0x13398
   __TEXT.__const: 0x920
   __TEXT.__oslogstring: 0x31
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
Functions:
~ _rawimg_get_digests : 3192 -> 3172
~ _AEAAuthDataGetEntry : 344 -> 348
~ _aeaChecksum : 500 -> 504
~ _BXPatch5StreamWithFlags : 2940 -> 2936
~ _BXPatch5InPlace : 2908 -> 2904
~ _OArchiveFileStreamWrite : 788 -> 768
~ _chunkAsyncProcess : 476 -> 488
~ _RawImageDiff : 6816 -> 6824
~ _resizeStream : 960 -> 976
~ _streamPWrite : 1860 -> 1904
~ _workerProc : 8104 -> 8076
~ _AAEntryXATBlobGetEntry : 344 -> 348
~ _loadAndDecodeHeader_Ustar : 4476 -> 4504
~ _isZero : 112 -> 100
~ _writerProc : 1208 -> 1220

```
