## libPcdDxe.dylib

> `/System/Library/PrivateFrameworks/EfiSupport.framework/Versions/A/libPcdDxe.dylib`

```diff

-  __TEXT.__text: 0x6318
+  __TEXT.__text: 0x6314
   __TEXT.__cstring: 0x126f
   __TEXT.__const: 0x3e0
   __TEXT.__oslogstring: 0x3
Sections:
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ _InternalMemCopyMem : 400 -> 364
~ _BasePrintLibSPrintMarker : 3936 -> 3924
~ _EfiGetSystemConfigurationTable : 236 -> 244
~ _DxePcdGetNextTokenSpace : 604 -> 600
~ _ExGetPcdInfo : 332 -> 344
~ _GetExPcdTokenNumber : 440 -> 464
~ _ExGetNextTokeNumber : 312 -> 316

```
