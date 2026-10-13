## TextToSpeech

> `/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech`

```diff

-727.3.2.0.0
-  __TEXT.__text: 0x326410
+727.3.3.0.0
+  __TEXT.__text: 0x32b2ac
   __TEXT.__objc_methlist: 0x3ca8
-  __TEXT.__const: 0x3fb49
+  __TEXT.__const: 0x3fc89
   __TEXT.__dlopen_cstrs: 0x150
-  __TEXT.__constg_swiftt: 0x85a4
-  __TEXT.__swift5_typeref: 0x7934
-  __TEXT.__swift5_fieldmd: 0x6360
-  __TEXT.__cstring: 0x855d
-  __TEXT.__swift5_types: 0x7b0
-  __TEXT.__swift5_capture: 0x3330
-  __TEXT.__swift5_reflstr: 0x4fd0
+  __TEXT.__constg_swiftt: 0x86f8
+  __TEXT.__swift5_typeref: 0x794e
+  __TEXT.__swift5_fieldmd: 0x645c
+  __TEXT.__cstring: 0x850d
+  __TEXT.__swift5_types: 0x7bc
+  __TEXT.__swift5_capture: 0x3334
+  __TEXT.__swift5_reflstr: 0x5100
   __TEXT.__swift5_assocty: 0x1690
-  __TEXT.__swift5_proto: 0x1348
+  __TEXT.__swift5_proto: 0x1354
   __TEXT.__swift_as_entry: 0xca4
   __TEXT.__swift_as_ret: 0xdd4
   __TEXT.__swift_as_cont: 0x126c
   __TEXT.__swift5_builtin: 0x4b0
-  __TEXT.__oslogstring: 0x2f94
+  __TEXT.__oslogstring: 0x30f4
   __TEXT.__swift5_protos: 0x5c
   __TEXT.__swift5_mpenum: 0x144
   __TEXT.__gcc_except_tab: 0x1e24
   __TEXT.__ustring: 0x2c6
-  __TEXT.__unwind_info: 0xf0d8
-  __TEXT.__eh_frame: 0x17418
+  __TEXT.__unwind_info: 0xf138
+  __TEXT.__eh_frame: 0x17540
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x19b0
-  __DATA_CONST.__objc_classlist: 0x368
+  __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x2980
+  __DATA_CONST.__objc_selrefs: 0x2978
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x12d0
   __DATA_CONST.__got: 0xd90
-  __AUTH_CONST.__const: 0x179f8
+  __AUTH_CONST.__const: 0x17b98
   __AUTH_CONST.__cfstring: 0x5f00
-  __AUTH_CONST.__objc_const: 0xab00
+  __AUTH_CONST.__objc_const: 0xacd8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xed0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x2ae0
-  __AUTH.__objc_data: 0x3258
-  __AUTH.__data: 0x40d0
+  __AUTH_CONST.__auth_got: 0x2af8
+  __AUTH.__objc_data: 0x3360
+  __AUTH.__data: 0x4198
   __DATA.__objc_ivar: 0x32c
-  __DATA.__data: 0x3d48
-  __DATA.__common: 0x518
+  __DATA.__data: 0x3d40
+  __DATA.__common: 0x528
   __DATA_DIRTY.__objc_data: 0x520
   __DATA_DIRTY.__data: 0x12d0
   __DATA_DIRTY.__bss: 0xbc0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16110
-  Symbols:   1372
-  CStrings:  1655
+  Functions: 16140
+  Symbols:   1373
+  CStrings:  1661
 
Symbols:
+ _uscript_getScript
CStrings:
+ "(?<![\\d(])\\+?\\(?\\d{1,4}\\)?(?:[-. ]?\\(?\\d{1,5}\\)?){0,5}(?:\\s?(?:x|ext\\.?)\\s?\\d+)?(?!\\d)"
+ "AudioQueue session timings (%{public}s): ioBufferDuration=%.*fms (requested %.*fms), outputLatency=%.*fms, wirelessTransport=%{bool}d, headroom=%.*fms, bufferDuration=%.*fms, buffersPerIOCycle=%.*f, stagedTarget=%ld, ioCycleFloor=%.*fms, effectivePriming=%.*fms, effectiveMaxBuffered=%.*fms"
+ "Failed to enqueue silence buffer: %d"
+ "PRAGMA journal_mode=TRUNCATE"
+ "Ranged event spans elements with distinct source text; dropped %ld range(s) from consolidation"
+ "Regex cache left in journal mode '%{public}s'; discarding the database file"
+ "Stop wind-down: hardwareDepth=%ld, repaying %ld of %ld deferred enqueue(s) with silence"
+ "Top-up enqueue failed"
+ "test"
- "(?:\\(\\d{3}\\)\\s?|\\d{3}[-. ])\\d{3}[-. ]?\\d{4}(?:\\s?(?:x|ext\\.?)\\s?\\d+)?|\\d{10}(?:\\s?(?:x|ext\\.?)\\s?\\d+)?|\\d{3}[-. ]\\d{4}(?:\\s?(?:x|ext\\.?)\\s?\\d+)?|\\d{7}(?:\\s?(?:x|ext\\.?)\\s?\\d+)?"
- "AudioQueue session timings (%{public}s): ioBufferDuration=%.*fms (requested %.*fms), outputLatency=%.*fms, headroom=%.*fms, otherAudioPlaying=%{bool}d, bufferDuration=%.*fms, buffersPerIOCycle=%.*f, stagedTarget=%ld, ioCycleFloor=%.*fms, effectivePriming=%.*fms, effectiveMaxBuffered=%.*fms"
- "PRAGMA journal_mode=WAL"
```
