## com.apple.VoiceMemos.SpotlightIndexExtension

> `/System/Applications/VoiceMemos.app/Contents/PlugIns/com.apple.VoiceMemos.SpotlightIndexExtension.appex/Contents/MacOS/com.apple.VoiceMemos.SpotlightIndexExtension`

```diff

-1252.0.0.0.0
-  __TEXT.__text: 0x1b58
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0x960
-  __TEXT.__objc_methlist: 0x1e0
+1272.0.0.0.0
+  __TEXT.__text: 0x68c
+  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__objc_stubs: 0x1c0
+  __TEXT.__objc_methlist: 0x58
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x252
-  __TEXT.__objc_classname: 0x81
-  __TEXT.__objc_methname: 0x910
-  __TEXT.__objc_methtype: 0xca
-  __TEXT.__oslogstring: 0x27
-  __TEXT.__unwind_info: 0x120
-  __DATA_CONST.__auth_got: 0x1a8
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x260
-  __DATA_CONST.__cfstring: 0x1a0
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_catlist: 0x30
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x1a
+  __TEXT.__objc_classname: 0x4a
+  __TEXT.__objc_methname: 0x256
+  __TEXT.__objc_methtype: 0x55
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x3a8
-  __DATA.__objc_selrefs: 0x2f8
-  __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0xa0
-  - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
+  __DATA.__objc_const: 0xf8
+  __DATA.__objc_selrefs: 0x90
+  __DATA.__objc_ivar: 0x4
+  __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/iOSSupport/System/Library/PrivateFrameworks/VoiceMemos.framework/Versions/A/VoiceMemos
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8298549E-3034-3537-9C4B-D08130F69666
-  Functions: 48
-  Symbols:   105
-  CStrings:  164
+  UUID: A539BBBC-2ED7-39E1-B57D-711695FE67B6
+  Functions: 12
+  Symbols:   47
+  CStrings:  30
 
Symbols:
- _AVFileTypeAppleM4A
- _AVFileTypeQuickTimeMovie
- _AVFormatIDKey
- _AVMediaTypeAudio
- _AVMetadataCommonKeyCreationDate
- _AVMetadataKeySpaceCommon
- _AVMetadataKeySpaceISOUserData
- _AVMetadataKeySpaceQuickTimeMetadata
- _AVMetadataKeySpaceiTunes
- _AVMetadataKeySpaceiTunesLong
- _AVMetadataiTunesMetadataKeySongName
- _AVURLAssetPreferPreciseDurationAndTimingKey
- _CMAudioFormatDescriptionGetStreamBasicDescription
- _CMTimeGetSeconds
- _NSLocalizedFailureReasonErrorKey
- _OBJC_CLASS_$_AVAsset
- _OBJC_CLASS_$_AVAssetTrack
- _OBJC_CLASS_$_AVAudioFile
- _OBJC_CLASS_$_AVAudioFormat
- _OBJC_CLASS_$_AVMetadataItem
- _OBJC_CLASS_$_AVMovie
- _OBJC_CLASS_$_AVMutableMetadataItem
- _OBJC_CLASS_$_AVMutableMovie
- _OBJC_CLASS_$_AVURLAsset
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSFileManager
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_RCCaptureFormat
- _OBJC_METACLASS_$_AVMutableMovie
- _OSLogForCategory
- _RCAudioFileExtensionQT
- _RCAudioFileExtensionQTA
- _RCTimeRangeFromCMTimeRange
- _RCVoiceMemosErrorDomain
- __NSConcreteGlobalBlock
- ___CFConstantStringClassReference
- ___kCFBooleanTrue
- __os_log_error_impl
- _kCMMetadataBaseDataType_RawData
- _kVMLogCategoryDefault
- _objc_alloc_init
- _objc_autorelease
- _objc_autoreleaseReturnValue
- _objc_getAssociatedObject
- _objc_msgSendSuper2
- _objc_opt_class
- _objc_opt_new
- _objc_opt_respondsToSelector
- _objc_release_x24
- _objc_release_x25
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_retain_x2
- _objc_setAssociatedObject
- _os_log_type_enabled
CStrings:
- "%s -- writeMovieHeaderToURL error = %@"
- "+[AVURLAsset(RCAdditions) rc_updateFile:withTranscriptionData:error:]"
- "@\"NSData\"16@?0@\"AVMetadataItem\"8"
- "@\"NSDate\"16@?0@\"AVMetadataItem\"8"
- "@\"NSNumber\"16@?0@\"AVMetadataItem\"8"
- "@\"NSString\"16@?0@\"AVMetadataItem\"8"
- "@\"NSURL\""
- "@24@0:8^@16"
- "@32@0:8@16^@24"
- "AVAssetAuthoringMetadataWithRecordingMetadata:"
- "AVAssetRCAdditionsUtilities"
- "B16@0:8"
- "B16@?0@\"AVAssetTrack\"8"
- "B16@?0@\"AVMovieTrack\"8"
- "B16@?0@\"AVMutableMovieTrack\"8"
- "B32@0:8Q16^@24"
- "B40@0:8@16@24^@32"
- "I16@0:8"
- "No audio tracks exist"
- "RCAdditions"
- "RCMutableMovie"
- "T@\"NSDictionary\",R,N"
- "T@\"NSURL\",&,N,Src_setComposedAVURL:"
- "T@\"NSURL\",&,N,V_linkURL"
- "TB,R"
- "TI,R,N"
- "Td,R,N"
- "T{?=dd},R,N"
- "URL"
- "URLByAppendingPathComponent:"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "_AVAssetRCComposedAVURLKey"
- "_linkURL"
- "com.apple.VoiceMemos.tsrp"
- "com.apple.iTunes.music-memo-note"
- "com.apple.iTunes.music-memo-rating"
- "com.apple.iTunes.music-memo-tags"
- "com.apple.iTunes.voice-memo-uuid"
- "containsObject:"
- "count"
- "d16@0:8"
- "dataValue"
- "date"
- "dateValue"
- "dealloc"
- "defaultManager"
- "dictionaryWithObjects:forKeys:count:"
- "duration"
- "errorWithDomain:code:userInfo:"
- "fileFormat"
- "firstObject"
- "formatDescriptions"
- "identifier"
- "identifierForKey:keySpace:"
- "initStandardFormatWithSampleRate:channels:"
- "initWithURL:options:"
- "isEnabled"
- "isEqualToString:"
- "isQuickTime"
- "keyForIdentifier:"
- "keySpaceForIdentifier:"
- "lastPathComponent"
- "length"
- "linkItemAtURL:toURL:error:"
- "linkURL"
- "metadata"
- "metadataItemsFromArray:filteredByIdentifier:"
- "metadataItemsFromArray:withKey:keySpace:"
- "movieWithURL:error:"
- "movieWithURL:options:"
- "musicMemoStarRating"
- "musicMemoTags"
- "musicMemoTextNote"
- "na_filter:"
- "na_map:"
- "numberValue"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "pathExtension"
- "processingFormat"
- "rc_URLByReplacingPathExtensionWithExtension:"
- "rc_audioFormat"
- "rc_audioTracks"
- "rc_composedAVURL"
- "rc_durationInSeconds"
- "rc_playbackFormat"
- "rc_preciseTimingAssetWithURL:"
- "rc_recordingMetadata"
- "rc_sampleRate"
- "rc_setComposedAVURL:"
- "rc_timeRange"
- "rc_transcriptionData"
- "rc_transcriptionDataExists"
- "rc_transcriptionDataForURL:"
- "rc_updateFile:withTranscriptionData:error:"
- "rc_updateMetadataInFile:withMetadata:error:"
- "rc_updateMetadataInFile:withRecordingMetadata:error:"
- "rc_writeMovieHeaderWithOptions:error:"
- "removeItemAtURL:error:"
- "sampleRate"
- "setDataType:"
- "setIdentifier:"
- "setKey:"
- "setKeySpace:"
- "setLinkURL:"
- "setMetadata:"
- "setObject:forKeyedSubscript:"
- "setValue:"
- "setWithObjects:count:"
- "settings"
- "stringValue"
- "temporaryMovieLink:"
- "timeRange"
- "title"
- "tracksWithMediaType:"
- "tsrp"
- "uniqueID"
- "unsignedIntValue"
- "v24@0:8@16"
- "writeMovieHeaderToURL:fileType:options:error:"
- "{?=dd}16@0:8"

```
