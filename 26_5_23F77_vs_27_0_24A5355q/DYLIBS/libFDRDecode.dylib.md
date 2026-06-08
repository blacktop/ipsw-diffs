## libFDRDecode.dylib

> `/usr/lib/libFDRDecode.dylib`

```diff

-1499.100.48.0.0
-  __TEXT.__text: 0xafbc
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__const: 0x8cc
-  __TEXT.__cstring: 0x4d36
-  __TEXT.__unwind_info: 0x1c0
-  __DATA_CONST.__got: 0x10
+1624.0.0.0.0
+  __TEXT.__text: 0xb510
+  __TEXT.__const: 0x8dc
+  __TEXT.__cstring: 0x4f3e
+  __TEXT.__unwind_info: 0x1d0
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x180
-  __AUTH_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xf8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x18
   __DATA_DIRTY.__bss: 0x8
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
-  UUID: 83CC21D2-C0A7-3FAE-90CF-92126E99D8BB
-  Functions: 238
-  Symbols:   551
-  CStrings:  430
+  UUID: 655F6143-C71A-3E8F-9ED0-3AB4D6A4F50E
+  Functions: 249
+  Symbols:   565
+  CStrings:  443
 
Symbols:
+ _AMFDRDecodeFindSubCCAndReturnAsPayload
+ _AMFDRDecodeManifestBodyInfoCreate
+ _AMFDRDecodeManifestBodyInfoDestroy
+ _AMFDRDecodeManifestBodyInfoGetComponentType
+ _AMFDRDecodeManifestBodyInfoGetDataClass
+ _AMFDRDecodeManifestBodyInfoGetDataInstance
+ _AMFDRDecodeManifestBodyInfoNext
+ _AMFDRDecodeManifestBodyInfoNext.cold.1
+ _AMFDRDecodeManifestBodyInfoNext.cold.2
+ _AMFDRDecodeManifestBodyInfoNext.cold.3
+ __AMFDRDecodeGetDataInfoCallback
+ _calloc
- __AMFDRDecodeGetDataInstCallback
CStrings:
+ "%s: Failed to find subCC %c%c%c%c"
+ "%s: Found subCC %c%c%c%c"
+ "%s: Img4DecodeGetPropertyData(0x%x) failed."
+ "%s: Img4DecodeGetPropertyData(kFDRTag_cptp) failed."
+ "%s: Invalid out pointers"
+ "%s: Skip verifying type info"
+ "%s: _AMFDRDecodeManifestBodyNext failed"
+ "%s: failed to find corresponding component type"
+ "%s: kFDRTag_cptp property != fdrDecode->componentType"
+ "%s: kFDRTag_cptp property length != fdrDecode->componentType.length"
+ "%s: pManifestBodyInfo is NULL"
+ "AMFDRDecodeFindSubCCAndReturnAsPayload"
+ "AMFDRDecodeManifestBodyInfoNext"
+ "_AMFDRDecodeGetDataInfoCallback"
- "_AMFDRDecodeGetDataInstCallback"

```
