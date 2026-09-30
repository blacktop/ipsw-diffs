## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64572.146.1.0.0
-  __TEXT.__text: 0xb0f30
+64572.149.1.0.0
+  __TEXT.__text: 0xb1054
   __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_methlist: 0x65d8
-  __TEXT.__const: 0x2b6
+  __TEXT.__objc_methlist: 0x65e8
+  __TEXT.__const: 0x2c6
   __TEXT.__cstring: 0x10048
   __TEXT.__gcc_except_tab: 0x4ed8
-  __TEXT.__oslogstring: 0x17ac
+  __TEXT.__oslogstring: 0x185c
   __TEXT.__ustring: 0x24
   __TEXT.__swift5_typeref: 0x402
   __TEXT.__swift5_capture: 0x120

   __TEXT.__swift5_types: 0x14
   __TEXT.__unwind_info: 0x2948
   __TEXT.__objc_classname: 0x83a
-  __TEXT.__objc_methname: 0xf51d
-  __TEXT.__objc_methtype: 0x5e83
-  __TEXT.__objc_stubs: 0x9a20
+  __TEXT.__objc_methname: 0xf537
+  __TEXT.__objc_methtype: 0x5e91
+  __TEXT.__objc_stubs: 0x9a40
   __DATA_CONST.__got: 0x458
   __DATA_CONST.__const: 0x35f8
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3570
+  __DATA_CONST.__objc_selrefs: 0x3578
   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x870
   __AUTH_CONST.__auth_got: 0x1220

   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x4f0
+  __AUTH.__objc_data: 0x4c8
   __AUTH.__data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8

   __DATA.__data: 0xd58
   __DATA.__bss: 0x558
   __DATA.__common: 0xf9
-  __DATA_DIRTY.__objc_data: 0x1770
+  __DATA_DIRTY.__objc_data: 0x1798
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: AA84FDAD-0E76-3AAA-81B2-435C5808081C
-  Functions: 3127
-  Symbols:   10558
-  CStrings:  7761
+  UUID: 3A1AE7C3-E525-3DC7-BDEC-B0AE2369ADA8
+  Functions: 3128
+  Symbols:   10561
+  CStrings:  7765
 
Symbols:
+ -[VMUSampler sampleThread:withOptions:]
+ _objc_msgSend$sampleThread:withOptions:
Functions:
~ _getRegionData : 880 -> 1060
~ _recordRegions : 11504 -> 11596
~ _recursivelyListAllRegions : 352 -> 356
~ _copySamplingResultToCallstack : 188 -> 196
~ -[VMUSampler sampleThread:] : 180 -> 24
+ -[VMUSampler sampleThread:withOptions:]
CStrings:
+ "@24@0:8I16i20"
+ "VM region enumeration timed out after %u seconds - not returning any regions\n"
+ "VM region enumeration wrapped around - requested address was %#llx, returned address %#llx, nestingDepth %u\n"
+ "sampleThread:withOptions:"

```
