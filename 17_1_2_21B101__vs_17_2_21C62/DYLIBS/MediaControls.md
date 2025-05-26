## MediaControls

> `/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls`

```diff

-4023.210.1.0.0
-  __TEXT.__text: 0xd1d2c
+4023.310.5.0.0
+  __TEXT.__text: 0xd1e9c
   __TEXT.__auth_stubs: 0x1220
-  __TEXT.__objc_methlist: 0x103c0
-  __TEXT.__cstring: 0x43aa
+  __TEXT.__objc_methlist: 0x10420
+  __TEXT.__cstring: 0x4485
   __TEXT.__ustring: 0x30
   __TEXT.__const: 0xcb0
-  __TEXT.__gcc_except_tab: 0x11f4
+  __TEXT.__gcc_except_tab: 0x1220
   __TEXT.__oslogstring: 0x56ab
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x35fc
+  __TEXT.__unwind_info: 0x3604
   __TEXT.__objc_classname: 0x2448
-  __TEXT.__objc_methname: 0x2bbcd
+  __TEXT.__objc_methname: 0x2bd3b
   __TEXT.__objc_methtype: 0x7a33
-  __TEXT.__objc_stubs: 0x1a1c0
+  __TEXT.__objc_stubs: 0x1a300
   __DATA_CONST.__got: 0x530
   __DATA_CONST.__const: 0x2ca8
   __DATA_CONST.__objc_classlist: 0x630
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x37578
-  __DATA_CONST.__objc_selrefs: 0x8a18
+  __DATA_CONST.__objc_const: 0x37648
+  __DATA_CONST.__objc_selrefs: 0x8a68
   __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__cfstring: 0x48a0
+  __AUTH_CONST.__cfstring: 0x4960
   __AUTH_CONST.__const: 0xb40
   __AUTH_CONST.__objc_const: 0x4410
   __AUTH_CONST.__objc_intobj: 0x1e0

   __AUTH_CONST.__auth_got: 0x920
   __AUTH.__objc_data: 0x1338
   __AUTH.__data: 0x8
-  __DATA.__objc_classrefs: 0xca0
+  __DATA.__objc_classrefs: 0xca8
   __DATA.__objc_superrefs: 0x5a0
-  __DATA.__objc_ivar: 0x16e4
+  __DATA.__objc_ivar: 0x16e8
   __DATA.__data: 0x2968
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x2aa8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6133
-  Symbols:   21417
-  CStrings:  9135
+  Functions: 6142
+  Symbols:   21444
+  CStrings:  9155
 
Symbols:
+ +[MRUStringsProvider audioSessionRenderingModeDolbyAtmos]
+ +[MRUStringsProvider audioSessionRenderingModeDolbyAudio]
+ +[MRUStringsProvider audioSessionRenderingModeMonoStereo]
+ +[MRUStringsProvider audioSessionRenderingModeSpatialAudio]
+ +[MRUStringsProvider audioSessionRenderingModeSurround]
+ -[MRURecommendation isCallToAction]
+ -[MRURecommendation setCallToAction:]
+ -[MRUSpatialAudioController localizedStringForRenderingMode:]
+ GCC_except_table30
+ _OBJC_IVAR_$_MRURecommendation._callToAction
+ ___55-[MRURouteRecommender initializeSessionWhenAppropriate]_block_invoke.132
+ ___block_literal_global.127
+ ___block_literal_global.153
+ ___block_literal_global.269
+ _objc_msgSend$audioSessionRenderingModeDolbyAtmos
+ _objc_msgSend$audioSessionRenderingModeDolbyAudio
+ _objc_msgSend$audioSessionRenderingModeMonoStereo
+ _objc_msgSend$audioSessionRenderingModeSpatialAudio
+ _objc_msgSend$audioSessionRenderingModeSurround
+ _objc_msgSend$effectiveIdentifier
+ _objc_msgSend$localizedStringForRenderingMode:
+ _objc_msgSend$renderingMode
+ _objc_msgSend$setDecrementImage:
+ _objc_msgSend$setIncrementImage:
- ___55-[MRURouteRecommender initializeSessionWhenAppropriate]_block_invoke.124
- ___block_literal_global.119
- ___block_literal_global.145
- ___block_literal_global.261
CStrings:
+ "AUDIO_SESSION_RENDERING_MODE_DOLBY_ATMOS"
+ "AUDIO_SESSION_RENDERING_MODE_DOLBY_AUDIO"
+ "AUDIO_SESSION_RENDERING_MODE_MONO_STEREO"
+ "AUDIO_SESSION_RENDERING_MODE_SPATIAL_AUDIO"
+ "AUDIO_SESSION_RENDERING_MODE_SURROUND"
+ "Not Applicable"
+ "TB,N,GisCallToAction"
+ "TB,N,GisCallToAction,V_callToAction"
+ "_callToAction"
+ "audioSessionRenderingModeDolbyAtmos"
+ "audioSessionRenderingModeDolbyAudio"
+ "audioSessionRenderingModeMonoStereo"
+ "audioSessionRenderingModeSpatialAudio"
+ "audioSessionRenderingModeSurround"
+ "callToAction"
+ "effectiveIdentifier"
+ "isCallToAction"
+ "localizedStringForRenderingMode:"
+ "renderingMode"
+ "setCallToAction:"

```
