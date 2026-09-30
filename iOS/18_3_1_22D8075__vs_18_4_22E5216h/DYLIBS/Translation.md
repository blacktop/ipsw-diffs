## Translation

> `/System/Library/Frameworks/Translation.framework/Translation`

```diff

-300.2.0.0.0
-  __TEXT.__text: 0x45190
-  __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_methlist: 0x4500
-  __TEXT.__const: 0x548
-  __TEXT.__cstring: 0x285e
-  __TEXT.__oslogstring: 0x3d86
+300.8.0.0.0
+  __TEXT.__text: 0x43030
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_methlist: 0x4aa0
+  __TEXT.__const: 0x4fc
+  __TEXT.__cstring: 0x283e
+  __TEXT.__oslogstring: 0x3ed6
   __TEXT.__gcc_except_tab: 0xa04
-  __TEXT.__swift5_typeref: 0x219
+  __TEXT.__swift5_typeref: 0x24f
   __TEXT.__swift5_capture: 0xb0
   __TEXT.__constg_swiftt: 0x1fc
   __TEXT.__swift5_reflstr: 0x1f2
   __TEXT.__swift5_fieldmd: 0x1fc
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x28
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__unwind_info: 0x1570
+  __TEXT.__unwind_info: 0x1508
   __TEXT.__eh_frame: 0x3e8
-  __TEXT.__objc_classname: 0xa05
-  __TEXT.__objc_methname: 0x9b49
+  __TEXT.__objc_classname: 0xa08
+  __TEXT.__objc_methname: 0x9b85
   __TEXT.__objc_methtype: 0x178b
-  __TEXT.__objc_stubs: 0x55a0
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x19e8
+  __TEXT.__objc_stubs: 0x55e0
+  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__const: 0x19b8
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f58
+  __DATA_CONST.__objc_selrefs: 0x1ff8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x6b0
+  __AUTH_CONST.__auth_got: 0x6c8
   __AUTH_CONST.__auth_ptr: 0x170
-  __AUTH_CONST.__const: 0x9b0
-  __AUTH_CONST.__cfstring: 0x2a60
-  __AUTH_CONST.__objc_const: 0xa020
+  __AUTH_CONST.__const: 0xa00
+  __AUTH_CONST.__cfstring: 0x2a80
+  __AUTH_CONST.__objc_const: 0x9618
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x158
-  __DATA.__objc_ivar: 0x6bc
-  __DATA.__data: 0x920
+  __DATA.__objc_ivar: 0x6c4
+  __DATA.__data: 0x948
   __DATA.__bss: 0x570
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x16d0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2179
-  Symbols:   2279
-  CStrings:  2683
+  Functions: 2156
+  Symbols:   2310
+  CStrings:  2698
 
Symbols:
+ _NSInvalidArgumentException
+ __os_signpost_emit_with_name_impl
+ _arc4random
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _memcpy
- _swift_arrayDestroy
- _swift_bridgeObjectRelease_n
- _swift_initStructMetadata
- _swift_isUniquelyReferenced_nonNull_native
CStrings:
+ "\x06\""
+ "Finished preflight checks with error"
+ "Got Task.CancellationError, no need to convert it"
+ "Null value for locale when encoding LTTranslationResult"
+ "PreflightChecks"
+ "Received result for input item %zu after completion handler was already called, likely because an error previously occurred; early returning"
+ "ResolvedSourceLocale"
+ "ResolvedTargetLocale"
+ "Successfully translated first item"
+ "Translating first item finished with error"
+ "Translation"
+ "Translation finished successfully"
+ "Translation finished with error"
+ "TranslationFirstItem"
+ "_hasReceivedFirstItem"
+ "_signpostID"
+ "didStartTranslating"
+ "raise"
- "Received result for input item %zu after completion handler was already called, likely because an error previously ocurred; early returning"
- "Swift/UnsafePointer.swift"
- "UnsafeMutablePointer.initialize overlapping range"

```
