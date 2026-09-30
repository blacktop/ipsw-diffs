## MediaControls

> `/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls`

```diff

-4025.200.14.0.0
-  __TEXT.__text: 0x1e3590
-  __TEXT.__auth_stubs: 0x3900
+4025.210.17.2.0
+  __TEXT.__text: 0x1e388c
+  __TEXT.__auth_stubs: 0x3910
   __TEXT.__objc_methlist: 0x152bc
   __TEXT.__cstring: 0x973d
   __TEXT.__ustring: 0x22
-  __TEXT.__const: 0x9404
+  __TEXT.__const: 0x9424
   __TEXT.__gcc_except_tab: 0x1844
-  __TEXT.__oslogstring: 0x7c29
+  __TEXT.__oslogstring: 0x7c39
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__constg_swiftt: 0x68a0
+  __TEXT.__constg_swiftt: 0x68b0
   __TEXT.__swift5_typeref: 0x2c80
   __TEXT.__swift5_reflstr: 0x3c93
   __TEXT.__swift5_fieldmd: 0x4004
   __TEXT.__swift5_types: 0x4c4
-  __TEXT.__swift5_capture: 0xf20
+  __TEXT.__swift5_capture: 0xf40
   __TEXT.__swift5_protos: 0xa4
-  __TEXT.__swift5_proto: 0x4fc
+  __TEXT.__swift5_proto: 0x500
   __TEXT.__swift5_builtin: 0x2a8
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift5_assocty: 0x2e8
-  __TEXT.__unwind_info: 0x7ab0
+  __TEXT.__unwind_info: 0x7ab8
   __TEXT.__eh_frame: 0x1468
   __TEXT.__objc_classname: 0x267f
-  __TEXT.__objc_methname: 0x3020a
+  __TEXT.__objc_methname: 0x3022f
   __TEXT.__objc_methtype: 0x7ef3
-  __TEXT.__objc_stubs: 0x1bbe0
+  __TEXT.__objc_stubs: 0x1bc20
   __DATA_CONST.__got: 0x16d0
   __DATA_CONST.__const: 0x2f48
   __DATA_CONST.__objc_classlist: 0x948
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x450
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa2b8
+  __DATA_CONST.__objc_selrefs: 0xa2c8
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_arraydata: 0x1b8
-  __AUTH_CONST.__auth_got: 0x1c90
-  __AUTH_CONST.__const: 0x8d78
+  __AUTH_CONST.__auth_got: 0x1c98
+  __AUTH_CONST.__const: 0x8df0
   __AUTH_CONST.__cfstring: 0x4fe0
   __AUTH_CONST.__objc_const: 0x41ab0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH.__objc_data: 0x60d8
+  __AUTH.__objc_data: 0x60e0
   __AUTH.__data: 0xaf8
   __DATA.__objc_ivar: 0x1870
   __DATA.__data: 0x3c58
-  __DATA.__bss: 0x7160
+  __DATA.__bss: 0x71e0
   __DATA.__common: 0x4c0
   __DATA_DIRTY.__objc_data: 0x41f8
-  __DATA_DIRTY.__data: 0x2f08
+  __DATA_DIRTY.__data: 0x2f18
   __DATA_DIRTY.__bss: 0x21c8
   __DATA_DIRTY.__common: 0x9b8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 94915684-6F6E-33B9-A9E0-47020E310BA0
-  Functions: 13102
-  Symbols:   24896
-  CStrings:  11306
+  UUID: A2643FBB-9876-35E5-85EF-8E8BAF532496
+  Functions: 13110
+  Symbols:   24903
+  CStrings:  11308
 
Symbols:
+ -[MRUWaveformViewController updateWaveformWithData:immediately:]
+ ___64-[MRUWaveformViewController updateWaveformWithData:immediately:]_block_invoke
+ ___64-[MRUWaveformViewController updateWaveformWithData:immediately:]_block_invoke_2
+ _objc_msgSend$flush
+ _objc_msgSend$setUpdateDeadline:
+ _objc_msgSend$updateWaveformWithData:immediately:
- -[MRUWaveformViewController updateWaveformWithData:]
- ___52-[MRUWaveformViewController updateWaveformWithData:]_block_invoke
- ___52-[MRUWaveformViewController updateWaveformWithData:]_block_invoke_2
- _objc_msgSend$updateWaveformWithData:
CStrings:
+ "[%s] updateState s:%s p:%{bool}d"
+ "flush"
+ "setUpdateDeadline:"
+ "updateWaveformWithData:immediately:"
- "[%s] state.isPulsing: %{bool}d"
- "updateWaveformWithData:"

```
