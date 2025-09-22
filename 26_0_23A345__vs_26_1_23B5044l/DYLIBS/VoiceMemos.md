## VoiceMemos

> `/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos`

```diff

-1335.1.0.0.0
-  __TEXT.__text: 0x482f8
+1343.0.0.0.0
+  __TEXT.__text: 0x48724
   __TEXT.__auth_stubs: 0xc10
-  __TEXT.__objc_methlist: 0x3dfc
+  __TEXT.__objc_methlist: 0x3de4
   __TEXT.__gcc_except_tab: 0x1850
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x6389
+  __TEXT.__cstring: 0x6386
   __TEXT.__oslogstring: 0x29e3
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x1980
+  __TEXT.__unwind_info: 0x1988
   __TEXT.__objc_classname: 0x82d
-  __TEXT.__objc_methname: 0xbe61
+  __TEXT.__objc_methname: 0xbe2e
   __TEXT.__objc_methtype: 0x1551
   __TEXT.__objc_stubs: 0x9020
-  __DATA_CONST.__got: 0x688
-  __DATA_CONST.__const: 0x1d28
+  __DATA_CONST.__got: 0x690
+  __DATA_CONST.__const: 0x1d40
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e78
+  __DATA_CONST.__objc_selrefs: 0x2e80
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x32a0
-  __AUTH_CONST.__objc_const: 0x5c18
+  __AUTH_CONST.__cfstring: 0x32c0
+  __AUTH_CONST.__objc_const: 0x5bb8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x318
+  __DATA.__objc_ivar: 0x310
   __DATA.__data: 0x7a0
   __DATA.__bss: 0x180
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7EE4F74-4078-3139-BB8A-63E70B5E77CF
-  Functions: 1902
-  Symbols:   6621
-  CStrings:  3470
+  UUID: 88002F8E-6573-3DAB-8705-6BCA4CC13137
+  Functions: 1900
+  Symbols:   6619
+  CStrings:  3471
 
Symbols:
+ -[AVAsset(RCAdditions) _codecNameForFormatID:]
+ -[AVAsset(RCAdditions) rc_allCodecNames]
+ -[RCVoiceMemoMetadata codecs]
+ -[RCVoiceMemoMetadata setCodecs:]
+ _OBJC_CLASS_$_AVCompositionTrack
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._codecs
+ _RCAudioCodecNameAACLC
+ _RCAudioCodecNameALAC
+ _RCAudioCodecNameAPAC
+ ___block_literal_global.129
+ ___block_literal_global.156
+ ___block_literal_global.162
+ ___block_literal_global.165
+ ___block_literal_global.93
+ _objc_msgSend$_codecNameForFormatID:
+ _objc_msgSend$codecs
+ _objc_msgSend$setCodecs:
+ _objc_msgSend$sourceTrackID
- -[RCVoiceMemoMetadata channelCount]
- -[RCVoiceMemoMetadata codec]
- -[RCVoiceMemoMetadata sampleRate]
- -[RCVoiceMemoMetadata setChannelCount:]
- -[RCVoiceMemoMetadata setCodec:]
- -[RCVoiceMemoMetadata setSampleRate:]
- _OBJC_IVAR_$_RCVoiceMemoMetadata._channelCount
- _OBJC_IVAR_$_RCVoiceMemoMetadata._codec
- _OBJC_IVAR_$_RCVoiceMemoMetadata._sampleRate
- ___block_literal_global.123
- ___block_literal_global.131
- ___block_literal_global.151
- ___block_literal_global.157
- ___block_literal_global.160
- ___block_literal_global.87
- _objc_msgSend$codec
- _objc_msgSend$setChannelCount:
- _objc_msgSend$setCodec:
- _objc_msgSend$setSampleRate:
CStrings:
+ "\r"
+ "T@\"NSArray\",&,N,V_codecs"
+ "_codecNameForFormatID:"
+ "_codecs"
+ "alac"
+ "apac"
+ "codecs"
+ "mp4a.40.2"
+ "rc_allCodecNames"
+ "setCodecs:"
+ "sourceTrackID"
- "T@\"NSNumber\",&,N,V_channelCount"
- "T@\"NSNumber\",&,N,V_sampleRate"
- "T@\"NSString\",&,N,V_codec"
- "_channelCount"
- "_codec"
- "codec"
- "setChannelCount:"
- "setCodec:"
- "setSampleRate:"

```
