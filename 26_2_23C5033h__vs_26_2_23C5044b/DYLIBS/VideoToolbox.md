## VideoToolbox

> `/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`

```diff

-3290.4.2.11.1
-  __TEXT.__text: 0x52aafc
-  __TEXT.__auth_stubs: 0x38c0
+3290.6.1.3.0
+  __TEXT.__text: 0x52b394
+  __TEXT.__auth_stubs: 0x38d0
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0xe54
   __TEXT.__const: 0x41b0
-  __TEXT.__cstring: 0xd6c2
-  __TEXT.__oslogstring: 0x4e93
+  __TEXT.__cstring: 0xd6f8
+  __TEXT.__oslogstring: 0x4fb6
   __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__dlopen_cstrs: 0x9b
   __TEXT.__unwind_info: 0x5990

   __TEXT.__objc_methtype: 0x967
   __TEXT.__objc_stubs: 0x1900
   __DATA_CONST.__got: 0xdc0
-  __DATA_CONST.__const: 0x3bd0
+  __DATA_CONST.__const: 0x3c10
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x820
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x1c70
+  __AUTH_CONST.__auth_got: 0x1c78
   __AUTH_CONST.__const: 0x426d0
   __AUTH_CONST.__cfstring: 0xa2a0
   __AUTH_CONST.__objc_const: 0x33c0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8879DA42-528F-3A91-901B-6E53124BB116
-  Functions: 8431
-  Symbols:   20371
-  CStrings:  3843
+  UUID: 44A9EE8C-A0FA-39CD-9371-301A7C41C168
+  Functions: 8433
+  Symbols:   20378
+  CStrings:  3846
 
Symbols:
+ _CFHash
+ ___VTParavirtualizationHostEncoderSessionCompleteInvalidate_block_invoke
+ ___VTParavirtualizationHostEncoderSessionCompleteInvalidate_block_invoke.12
CStrings:
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p) WARNING: waited %u seconds for pending frames %{public}@, calling CleanUpAfterDecode"
+ "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p) WARNING: waited %u seconds for pending tiles %{public}@, calling CleanUpAfterTileDecode"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p) WARNING: waited %u seconds but EmitEncodedFrame calls are still pending for %{public}@"
+ "<<<< VTParavirtualizationHostEncoder >>>> %s: (%p) WARNING: waited %u seconds but EmitEncodedTile calls are still pending for %{public}@"
+ "VTParavirtualizationHostEncoderSessionCompleteInvalidate"
+ "description=CoreMedia_VideoToolbox-3290.6.1.3"
- "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p) WARNING: waited %u seconds for pending frames %@, calling CleanUpAfterDecode"
- "<<<< VTParavirtualizationHostDecoder >>>> %s: (%p) WARNING: waited %u seconds for pending tiles %@, calling CleanUpAfterTileDecode"
- "description=CoreMedia_VideoToolbox-3290.4.2.11.1"

```
