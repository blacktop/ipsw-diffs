## ParrotAudioPlugin

> `/System/Library/Templates/Data/Library/Audio/Plug-Ins/HAL/ParrotAudioPlugin.driver/Contents/MacOS/ParrotAudioPlugin`

```diff

-  __TEXT.__text: 0x24c08
-  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__text: 0x24464
+  __TEXT.__auth_stubs: 0x7c0
   __TEXT.__objc_stubs: 0x25c0
-  __TEXT.__objc_methlist: 0xe9c
-  __TEXT.__gcc_except_tab: 0x338c
-  __TEXT.__objc_methname: 0x2ba6
+  __TEXT.__objc_methlist: 0xea4
+  __TEXT.__gcc_except_tab: 0x32c8
+  __TEXT.__objc_methname: 0x2ba9
   __TEXT.__objc_classname: 0x32e
-  __TEXT.__objc_methtype: 0x92c
-  __TEXT.__cstring: 0x1700
-  __TEXT.__const: 0x582
-  __TEXT.__oslogstring: 0x2126
-  __TEXT.__unwind_info: 0xf70
+  __TEXT.__objc_methtype: 0x91e
+  __TEXT.__cstring: 0x1768
+  __TEXT.__const: 0x592
+  __TEXT.__oslogstring: 0x1fcd
+  __TEXT.__unwind_info: 0xf80
   __DATA_CONST.__const: 0x1060
   __DATA_CONST.__cfstring: 0x880
   __DATA_CONST.__objc_classlist: 0xf8

   __DATA_CONST.__objc_floatobj: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x3f8
+  __DATA_CONST.__auth_got: 0x3f0
   __DATA_CONST.__got: 0x198
   __DATA.__objc_const: 0x1e68
   __DATA.__objc_selrefs: 0xb98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 821
-  Symbols:   470
-  CStrings:  1055
+  Functions: 819
+  Symbols:   469
+  CStrings:  1052
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
- _malloc_type_calloc
CStrings:
+ "%s: MAT tap %s, format=%s ch=%u"
+ "%s: tap pair set to %s"
+ "-[ParrotTVAudioDevice updateTapStreamForDSPFormat:]"
+ "-[ParrotTapStream applyDSPFormat:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BBxugu/Sources/ParrotAudio/Plugin/Common/Device/ParrotAudioDevice.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BBxugu/Sources/ParrotAudio/Plugin/Utils/ParrotFormatUtil.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BBxugu/Sources/ParrotAudio/Plugin/macOS/Codec/ParrotMacAudioCodec.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BBxugu/Sources/ParrotAudio/Plugin/macOS/Device/ParrotMacAudioDevice.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BBxugu/Sources/ParrotAudio/Plugin/macOS/Device/ParrotMacHDMIAudioDevice.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BBxugu/Sources/ParrotAudio/Plugin/macOS/FormatController/ParrotMacAudioFormatController.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BBxugu/Sources/ParrotAudio/Plugin/tvOS/Device/ParrotTVAudioDevice.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BBxugu/Sources/ParrotAudio/Plugin/tvOS/Device/ParrotTVAudioDeviceFactory.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BBxugu/Sources/ParrotAudio/Plugin/tvOS/Device/ParrotTVHDMIAudioDevice.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BBxugu/Sources/ParrotAudio/Plugin/tvOS/ParrotSystemSettingsManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BBxugu/Sources/ParrotAudio/Plugin/tvOS/Stream/ParrotTapStream.mm"
+ "AUMATDecoder: first MAT render frames=%u, Pa/Pb at byte %u (frame %u)"
+ "AUMATDecoder: sync lost at expected byte %u after %llu render(s), re-syncing"
+ "applyDSPFormat:"
+ "dspFormat != nil"
+ "updateTapStreamForDSPFormat:"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDu0gu/Sources/ParrotAudio/Plugin/Common/Device/ParrotAudioDevice.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDu0gu/Sources/ParrotAudio/Plugin/Utils/ParrotFormatUtil.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDu0gu/Sources/ParrotAudio/Plugin/macOS/Codec/ParrotMacAudioCodec.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDu0gu/Sources/ParrotAudio/Plugin/macOS/Device/ParrotMacAudioDevice.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDu0gu/Sources/ParrotAudio/Plugin/macOS/Device/ParrotMacHDMIAudioDevice.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDu0gu/Sources/ParrotAudio/Plugin/macOS/FormatController/ParrotMacAudioFormatController.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDu0gu/Sources/ParrotAudio/Plugin/tvOS/Device/ParrotTVAudioDevice.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDu0gu/Sources/ParrotAudio/Plugin/tvOS/Device/ParrotTVAudioDeviceFactory.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDu0gu/Sources/ParrotAudio/Plugin/tvOS/Device/ParrotTVHDMIAudioDevice.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDu0gu/Sources/ParrotAudio/Plugin/tvOS/ParrotSystemSettingsManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDu0gu/Sources/ParrotAudio/Plugin/tvOS/Stream/ParrotTapStream.mm"
- "AUMATDecoder: backward timeline jump, resetting anchor and sync"
- "AUMATDecoder: burst sync at byte offset %u (frame offset %lld)"
- "AUMATDecoder: failed to disable prime method after reset err=%d"
- "AUMATDecoder: first MAT render frames=%u byteSize=%u"
- "AUMATDecoder: timeline discontinuity (gap=%lld frames), resetting sync"
- "ParrotTapStream: no PCM formats available"
- "firstObject"
- "updateAudioDeviceStreamFormat: MAT branch — tap %s, format=%s ch=%u"
- "updateAudioDeviceStreamFormat: PCM branch — format=%s ch=%u"
- "updateAudioDeviceStreamFormat: tap stream set to %s ch=%u"
- "updateFormats:withSampleRate:"
- "v32@0:8@16d24"

```
