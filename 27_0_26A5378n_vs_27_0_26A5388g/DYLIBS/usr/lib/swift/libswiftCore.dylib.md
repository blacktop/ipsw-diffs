## libswiftCore.dylib

> `/usr/lib/swift/libswiftCore.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-6.4.0.25.5
-  __TEXT.__text: 0x4983a8
+6.4.0.27.1
+  __TEXT.__text: 0x498bf8
   __TEXT.__lazy_helpers: 0x39c
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x1e1c
-  __TEXT.__cstring: 0x131f9
+  __TEXT.__cstring: 0x13249
   __TEXT.__const: 0xbb71b
   __TEXT.__oslogstring: 0xb7
   __TEXT.__gcc_except_tab: 0xf0

   __TEXT.__swift5_proto: 0x154c
   __TEXT.__swift5_types: 0x948
   __TEXT.__swift5_types2: 0x28
-  __TEXT.__unwind_info: 0xacf0
+  __TEXT.__unwind_info: 0xacf8
   __TEXT.__eh_frame: 0x8a68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__lazy_load_got: 0x48
   __AUTH_CONST.__auth_got: 0x6f0
   __AUTH.__objc_data: 0x1c8
-  __AUTH.__data: 0xe6f8
+  __AUTH.__data: 0xe638
   __DATA.__objc_ivar: 0x38
   __DATA.__crash_info: 0x40
-  __DATA.__data: 0xcd4
+  __DATA.__data: 0xccc
   __DATA.swift5_backtrace: 0xc000
-  __DATA.__bss: 0xf568
+  __DATA.__bss: 0xf388
   __DATA.__common: 0xb8
   __DATA_DIRTY.__objc_data: 0xe08
-  __DATA_DIRTY.__data: 0x3330
-  __DATA_DIRTY.__bss: 0x173f0
+  __DATA_DIRTY.__data: 0x3408
+  __DATA_DIRTY.__bss: 0x175d0
   __DATA_DIRTY.__common: 0x50
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libswiftPrespecialized.dylib
-  Functions: 22300
-  Symbols:   40228
-  CStrings:  2808
+  Functions: 22302
+  Symbols:   40230
+  CStrings:  2810
 
Symbols:
+ __ZN5swift8Demangle9__runtime11TypeDecoderIN12_GLOBAL__N_122DecodedMetadataBuilderEE17decodeMangledTypeEPNS1_4NodeEjbb
+ __ZN5swift8Demangle9__runtime11TypeDecoderIN12_GLOBAL__N_122DecodedMetadataBuilderEE28decodeMangledGenericArgumentEPNS1_4NodeEjb
+ __ZNK12_GLOBAL__N_122DecodedMetadataBuilder23isValueGenericParameterEPKN5swift23TargetContextDescriptorINS1_9InProcessEEEj
+ __ZZN5swift8Demangle9__runtime11TypeDecoderIN12_GLOBAL__N_122DecodedMetadataBuilderEE17decodeMangledTypeEPNS1_4NodeEjbbENKUlNS_19MetadataPackOrValueEE_clES8_
- __ZN5swift8Demangle9__runtime11TypeDecoderIN12_GLOBAL__N_122DecodedMetadataBuilderEE17decodeMangledTypeEPNS1_4NodeEjb
- __ZZN5swift8Demangle9__runtime11TypeDecoderIN12_GLOBAL__N_122DecodedMetadataBuilderEE17decodeMangledTypeEPNS1_4NodeEjbENKUlNS_19MetadataPackOrValueEE_clES8_
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.W8Jpkv/Sources/swiftlang_stdlib_Core/swift/lib/Demangling/Demangler.cpp"
+ "integer value bound to non-value generic parameter"
+ "integer value where a type is required"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vgRN21/Sources/swiftlang_stdlib_Core/swift/lib/Demangling/Demangler.cpp"
```
