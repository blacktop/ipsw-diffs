## libFaultTolerantWriteDxe.dylib

> `/System/Library/PrivateFrameworks/EfiSupport.framework/Versions/A/libFaultTolerantWriteDxe.dylib`

```diff

-  __TEXT.__text: 0x6004
+  __TEXT.__text: 0x5ffc
   __TEXT.__cstring: 0x12f9
   __TEXT.__const: 0x3e8
   __TEXT.__oslogstring: 0x3
Sections:
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ _GetFvbByAddress : 256 -> 268
~ _JuniperHostFaultTolerantWriteReinit : 688 -> 708
~ _InternalMemCopyMem : 400 -> 364
~ _BasePrintLibSPrintMarker : 3936 -> 3924
~ _EfiGetSystemConfigurationTable : 236 -> 244

```
