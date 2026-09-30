## libFDRDecode.dylib

> `/usr/lib/libFDRDecode.dylib`

```diff

-1499.100.48.0.0
-  __TEXT.__text: 0xafbc sha256:48b6e79cf8fc23d692b784fb3824b22766f290ed7ae19f54a10f4a45898bc932
-  __TEXT.__auth_stubs: 0x240 sha256:d53445450e5040a244c53bf45dfae573d1e20f17d7e35c343749ee8afffcb790
-  __TEXT.__const: 0x8cc sha256:78258182199df7d98c8c68af5cdf0a659d24ae378f18023012afe5d6bc5c0797
-  __TEXT.__cstring: 0x4d36 sha256:a14995b8c41da0837cf67a16a89d3c59766b86a2acd1f10aa73d75a70a5b0956
-  __TEXT.__unwind_info: 0x1c0 sha256:1122b24c2b5ea5e188b25a4ab36c2e1cd58f1cced863ac4c89a07b267d11d4c2
-  __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__const: 0x180 sha256:1cb447b33fba117abaecd6305083a3faa89a87bb178925ca86b343f096e515ff
-  __AUTH_CONST.__auth_got: 0x120 sha256:2d5565fb483d8ea4525a7a9229677d1038ad34b6e22c8d5152e1d7f7b9817597
-  __AUTH_CONST.__const: 0xf8 sha256:c4bf3483ddd4ec696a342dbe42918ad34cd77c27a1cbf5ea97b4b30e0a48d624
-  __DATA.__data: 0x18 sha256:92d92dd1d65e5512e3445ac50686a75430712eae880a429c7214d1a7aa0f43f3
+1624.0.0.0.0
+  __TEXT.__text: 0xb510 sha256:4a17a6f2ad043df312c43dec4d8abd068c325723a39920c728bb11ec089a6eed
+  __TEXT.__const: 0x8dc sha256:e8c3461e59aec12235fe09b5e501569bf4d659544a2169c0c9d592cd4a4bb2a9
+  __TEXT.__cstring: 0x4f3e sha256:7cc00ba4ca47e60b25fba5c8f534dc7694beb637f9332f619485a9e50c184adf
+  __TEXT.__unwind_info: 0x1d0 sha256:e031478531e4c0574eeb09b1c824a33f0dc92dd8de7df7d6f2fc8e3e9e52a35a
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x180 sha256:9b8e6dcf6c0c74b28e1386cf4cd1b03da9cd7b19434ed3a39f38dcb758227864
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xf8 sha256:ec321895994fa072b487c6b71c40fd5627b6efcb49b3c6ada655f07936c221a7
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x18 sha256:9e4a0be75111ef85ecc41487075aeb0fedc635c6858b44e25c52776e3bfc8b33
   __DATA_DIRTY.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
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
