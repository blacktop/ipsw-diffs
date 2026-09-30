## libFontWorkerAccess.dylib

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/Current/Frameworks/ATS.framework/Versions/A/Resources/libFontWorkerAccess.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-421.0.0.0.0
-  __TEXT.__text: 0xe1c0
+424.0.0.0.0
+  __TEXT.__text: 0xe24c
   __TEXT.__objc_methlist: 0x130
-  __TEXT.__gcc_except_tab: 0xe78
-  __TEXT.__cstring: 0x1046
+  __TEXT.__gcc_except_tab: 0xe9c
+  __TEXT.__cstring: 0x107e
   __TEXT.__const: 0x78
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x930
+  __TEXT.__unwind_info: 0x938
   __TEXT.__objc_stubs: 0x780
-  __TEXT.__auth_stubs: 0xe90
+  __TEXT.__auth_stubs: 0xe80
   __TEXT.__objc_classname: 0x26
   __TEXT.__objc_methname: 0x69d
   __TEXT.__objc_methtype: 0x230
-  __DATA_CONST.__const: 0x358
+  __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x1d0
   __AUTH_CONST.__const: 0x5b8
-  __AUTH_CONST.__cfstring: 0x1080
+  __AUTH_CONST.__cfstring: 0x10a0
   __AUTH_CONST.__objc_const: 0x120
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x748
+  __AUTH_CONST.__auth_got: 0x740
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x138

   - /usr/lib/libobjc.A.dylib
   Functions: 404
   Symbols:   1016
-  CStrings:  280
+  CStrings:  281
 
Symbols:
+ _kXTFontPropertyPreciseUnicodeRanges
- _geteuid
Functions:
~ _XTConsumeSandboxExtension : 272 -> 292
~ __ZN19TCFResurrectContextC2EPKhm : 44 -> 48
~ __ZN19TCFResurrectContextC1EPKhm : 44 -> 48
~ __ZN19TCFResurrectContextC2Emm : 44 -> 48
~ __ZN19TCFResurrectContextC1Emm : 44 -> 48
~ __ZN19TCFResurrectContext16ResurrectCFArrayEv : 476 -> 500
~ __ZN19TCFResurrectContext14ResurrectCFSetEv : 476 -> 500
~ __ZN19TCFResurrectContext9ResurrectE7TCFType : 960 -> 984
~ __ZN18TSessionManagerImpC2Ev : 92 -> 112
~ __ZN18TSessionManagerImp15InitSessionInfoEv : 80 -> 76
~ _segmentAtPosition : 68 -> 96
~ _parentOfSegment : 64 -> 8
~ _readStack : 64 -> 8
~ _writeStack : 64 -> 8
~ _writeSegmentAtPosition : 196 -> 200
~ _XTDataStreamCreateStream : 96 -> 100
~ _XTDataStreamWithData : 156 -> 172
~ _XTDataStreamShow : 400 -> 356
~ _XTDataStreamResetStream : 104 -> 140
~ _XTDataStreamCloseReadSegment : 88 -> 92
~ _XTDataStreamResetReadSegment : 52 -> 40
~ _XTDataStreamOpenReadSegment : 76 -> 132
~ _XTDataStreamSkipReadSegment : 84 -> 76
~ _XTDataStreamCurrentReadSegment : 64 -> 8
~ _XTDataStreamReadBytes : 116 -> 164
~ _XTDataStreamBytesLeftToRead : 88 -> 64
~ _XTDataStreamBytesLeftToReadInCurrentSegment : 64 -> 48
~ _XTDataStreamClearStream : 100 -> 136
~ _XTDataStreamCloseWriteSegment : 132 -> 112
~ _XTDataStreamClearToStartOfSegment : 80 -> 76
~ _XTDataStreamOpenWriteSegment : 72 -> 80
~ _XTDataStreamAppendEmptySegments : 104 -> 76
~ _XTDataStreamCurrentWriteSegment : 64 -> 8
~ _XTDataStreamAppendBytes : 128 -> 160
~ _XTDataStreamReadString : 176 -> 252
~ _XTDataStreamAppendString : 96 -> 92
~ _XTDataStreamReadCString : 212 -> 236
~ _XTCreateCompressedBitmapRepresentation : 320 -> 324
~ _XTCopyUncompressedBitmapRepresentation : 372 -> 452
CStrings:
+ "XTFontPreciseUnicodeRangesProperty"
+ "recursion depth exceeded"
- "hi\n"
```
