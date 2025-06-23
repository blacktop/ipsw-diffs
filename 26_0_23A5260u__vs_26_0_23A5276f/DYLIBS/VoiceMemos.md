## VoiceMemos

> `/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos`

```diff

-1325.0.0.0.0
-  __TEXT.__text: 0x48b04
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_methlist: 0x3f0c
+1328.0.0.0.0
+  __TEXT.__text: 0x487f8
+  __TEXT.__auth_stubs: 0xc10
+  __TEXT.__objc_methlist: 0x3f34
   __TEXT.__gcc_except_tab: 0x1850
   __TEXT.__const: 0x218
-  __TEXT.__cstring: 0x6453
-  __TEXT.__oslogstring: 0x2a9d
+  __TEXT.__cstring: 0x63de
+  __TEXT.__oslogstring: 0x29e3
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x1948
-  __TEXT.__objc_classname: 0x83f
-  __TEXT.__objc_methname: 0xc03e
-  __TEXT.__objc_methtype: 0x154f
-  __TEXT.__objc_stubs: 0x9280
-  __DATA_CONST.__got: 0x6a0
+  __TEXT.__unwind_info: 0x1940
+  __TEXT.__objc_classname: 0x856
+  __TEXT.__objc_methname: 0xc069
+  __TEXT.__objc_methtype: 0x156a
+  __TEXT.__objc_stubs: 0x91e0
+  __DATA_CONST.__got: 0x698
   __DATA_CONST.__const: 0x1d28
-  __DATA_CONST.__objc_classlist: 0x1b8
+  __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f00
+  __DATA_CONST.__objc_selrefs: 0x2ee8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x610
+  __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x3360
-  __AUTH_CONST.__objc_const: 0x5e38
+  __AUTH_CONST.__cfstring: 0x3380
+  __AUTH_CONST.__objc_const: 0x5f18
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x32c
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x334
   __DATA.__data: 0x7a0
   __DATA.__bss: 0x180
   __DATA_DIRTY.__objc_data: 0xf00

   - /System/Library/PrivateFrameworks/MediaServices.framework/MediaServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
-  - /System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6B66DDB4-F987-3668-894C-52A266F716F5
-  Functions: 1925
-  Symbols:   6705
-  CStrings:  3516
+  UUID: 5D6F9560-F3F8-3C1D-8C94-3829F912D851
+  Functions: 1924
+  Symbols:   6706
+  CStrings:  3515
 
Symbols:
+ +[FragmentConsolidator consolidateMovieFragmentsForFileAt:error:]
+ -[RCAssetWriter _updateDelegateCount:]
+ -[RCAssetWriter delegate]
+ -[RCAssetWriter setDelegate:]
+ _FigConsolidateMovieFragments
+ _FigMovieUsesFragments
+ _OBJC_CLASS_$_FragmentConsolidator
+ _OBJC_IVAR_$_RCAssetWriter._delegate
+ _OBJC_IVAR_$_RCAssetWriter._didCallRequestMediaDataWhenReadyOnQueue
+ _OBJC_METACLASS_$_FragmentConsolidator
+ __OBJC_$_CLASS_METHODS_FragmentConsolidator
+ __OBJC_CLASS_RO_$_FragmentConsolidator
+ __OBJC_METACLASS_RO_$_FragmentConsolidator
+ ___block_literal_global.217
+ ___block_literal_global.221
+ ___block_literal_global.228
+ ___block_literal_global.233
+ _objc_msgSend$_updateDelegateCount:
+ _objc_msgSend$rcAssetWriterDidUpdateQueuedBufferCount:
- -[RCCloudRecording _copyResourceFromLocation:toDirectory:usingName:andExtension:]
- -[RCCloudRecording _copyResourceFromLocation:toDirectory:usingName:andExtension:].cold.1
- -[RCCloudRecording _copyResourceFromLocation:toDirectory:usingName:andExtension:].cold.2
- -[RCCloudRecording copyResourcesForSharingIntoDirectory:]
- -[RCCloudRecording copyResourcesForSharingIntoDirectory:].cold.1
- _OBJC_CLASS_$_NUPlatform
- ___block_literal_global.194
- ___block_literal_global.215
- ___block_literal_global.219
- ___block_literal_global.222
- ___block_literal_global.231
- _objc_msgSend$_copyResourceFromLocation:toDirectory:usingName:andExtension:
- _objc_msgSend$composedAssetHasMultipleTracks
- _objc_msgSend$currentPlatform
- _objc_msgSend$family
- _objc_msgSend$fileNameForSharing
- _objc_msgSend$mainDevice
- _objc_msgSend$supportsANE
CStrings:
+ "@\"<RCAssetWriterDelegate>\""
+ "DeviceSupportsAudioMix"
+ "FragmentConsolidator"
+ "T@\"<RCAssetWriterDelegate>\",W,N,V_delegate"
+ "_didCallRequestMediaDataWhenReadyOnQueue"
+ "_updateDelegateCount:"
+ "consolidateMovieFragmentsForFileAt:error:"
+ "rcAssetWriterDidUpdateQueuedBufferCount:"
+ "\xd1"
- "%s -- Failed to copy asset for sharing - error = %@"
- "%s -- Failed to remove title metadata - error = %@"
- "%s -- Incorrect file extension for multi layer voice memo. Changing from %@ to %@."
- "-[RCCloudRecording _copyResourceFromLocation:toDirectory:usingName:andExtension:]"
- "-[RCCloudRecording copyResourcesForSharingIntoDirectory:]"
- "_copyResourceFromLocation:toDirectory:usingName:andExtension:"
- "copyResourcesForSharingIntoDirectory:"
- "currentPlatform"
- "family"
- "mainDevice"
- "supportsANE"

```
