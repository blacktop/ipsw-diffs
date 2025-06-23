## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-413.0.0.0.0
-  __TEXT.__text: 0x689fc
-  __TEXT.__auth_stubs: 0x18a0
-  __TEXT.__objc_methlist: 0x6a7c
+415.0.0.0.0
+  __TEXT.__text: 0x69140
+  __TEXT.__auth_stubs: 0x18f0
+  __TEXT.__objc_methlist: 0x6adc
   __TEXT.__gcc_except_tab: 0x1878
   __TEXT.__const: 0x698
-  __TEXT.__cstring: 0x54c8
-  __TEXT.__oslogstring: 0x1ddb
+  __TEXT.__cstring: 0x5568
+  __TEXT.__oslogstring: 0x1ebb
   __TEXT.__ustring: 0x64
   __TEXT.__swift5_typeref: 0x336
   __TEXT.__constg_swiftt: 0x238

   __TEXT.__swift5_proto: 0x18
   __TEXT.__unwind_info: 0x1d80
   __TEXT.__eh_frame: 0x608
-  __TEXT.__objc_classname: 0xa81
-  __TEXT.__objc_methname: 0xf142
+  __TEXT.__objc_classname: 0xa98
+  __TEXT.__objc_methname: 0xf205
   __TEXT.__objc_methtype: 0x2231
-  __TEXT.__objc_stubs: 0xce60
-  __DATA_CONST.__got: 0x558
-  __DATA_CONST.__const: 0xc00
-  __DATA_CONST.__objc_classlist: 0x288
+  __TEXT.__objc_stubs: 0xcf20
+  __DATA_CONST.__got: 0x578
+  __DATA_CONST.__const: 0xc08
+  __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c40
+  __DATA_CONST.__objc_selrefs: 0x3c70
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x2c0
-  __AUTH_CONST.__auth_got: 0xc60
+  __AUTH_CONST.__auth_got: 0xc88
   __AUTH_CONST.__const: 0x10f0
-  __AUTH_CONST.__cfstring: 0x4cc0
-  __AUTH_CONST.__objc_const: 0xe860
+  __AUTH_CONST.__cfstring: 0x4d40
+  __AUTH_CONST.__objc_const: 0xe920
   __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xb80
+  __AUTH.__objc_data: 0xbd0
   __AUTH.__data: 0x348
-  __DATA.__objc_ivar: 0x808
+  __DATA.__objc_ivar: 0x80c
   __DATA.__data: 0x1028
   __DATA.__common: 0x28
   __DATA.__bss: 0x508

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B2B9AFF8-4A86-38E8-9E7B-898B491214D1
-  Functions: 2689
-  Symbols:   8844
-  CStrings:  4556
+  UUID: 6C470023-ECF9-3BC4-8857-C47E47F909E4
+  Functions: 2697
+  Symbols:   8873
+  CStrings:  4577
 
Symbols:
+ +[SCROBrailleUIUtilities tryDownloadingIfNeededForURL:]
+ -[SCROBrailleUIFinderApp _closeDeleteConfirmView]
+ -[SCROBrailleUIFinderApp _handleActionInDeleteConfirmView:]
+ -[SCROBrailleUIFinderApp _isShowingDeleteConfirmView]
+ -[SCROBrailleUIFinderApp _openDeleteConfirmView]
+ -[SCROBrailleUIFinderApp deleteConfirmView]
+ -[SCROBrailleUIFinderApp setDeleteConfirmView:]
+ _AXPidForLaunchLabel
+ _NSURLIsUbiquitousItemKey
+ _NSURLUbiquitousItemDownloadingStatusKey
+ _NSURLUbiquitousItemDownloadingStatusNotDownloaded
+ _OBJC_CLASS_$_NSFileCoordinator
+ _OBJC_CLASS_$_SCROBrailleUIUtilities
+ _OBJC_IVAR_$_SCROBrailleUIFinderApp._deleteConfirmView
+ _OBJC_METACLASS_$_SCROBrailleUIUtilities
+ __OBJC_$_CLASS_METHODS_SCROBrailleUIUtilities
+ __OBJC_CLASS_RO_$_SCROBrailleUIUtilities
+ __OBJC_METACLASS_RO_$_SCROBrailleUIUtilities
+ ___55+[SCROBrailleUIUtilities tryDownloadingIfNeededForURL:]_block_invoke
+ ___block_descriptor_40_e8_32s_e15_v16?0"NSURL"8ls32l8
+ ___block_literal_global.106
+ ___block_literal_global.329
+ ___block_literal_global.70
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$coordinateReadingItemAtURL:options:error:byAccessor:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$initWithFilePresenter:
+ _objc_msgSend$startDownloadingUbiquitousItemAtURL:error:
+ _objc_msgSend$tryDownloadingIfNeededForURL:
- ___block_literal_global.102
- ___block_literal_global.335
- ___block_literal_global.67
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_ScreenReaderOutput
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ScreenReaderOutput
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ScreenReaderOutput
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ScreenReaderOutput
CStrings:
+ "Braille UI Finder: Failed to get contents at path %@"
+ "Braille UI: Failed to start downloading iCloud file %@: %@"
+ "Braille UI: Starting download for iCloud file %@"
+ "Braille UI: Timeout waiting for iCloud file to download %@"
+ "SCROBrailleUIUtilities"
+ "URLWithString:"
+ "com.apple.VoiceOver"
+ "coordinateReadingItemAtURL:options:error:byAccessor:"
+ "finder.delete.confirm"
+ "finder.delete.confirm.delete"
+ "finder.delete.confirm.format"
+ "finder.delete.confirm.message"
+ "getResourceValue:forKey:error:"
+ "initWithFilePresenter:"
+ "startDownloadingUbiquitousItemAtURL:error:"
+ "tryDownloadingIfNeededForURL:"
+ "v16@?0@\"NSURL\"8"

```
