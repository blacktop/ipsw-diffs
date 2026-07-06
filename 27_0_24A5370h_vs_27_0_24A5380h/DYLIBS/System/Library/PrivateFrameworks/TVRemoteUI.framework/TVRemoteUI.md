## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

```diff

-  __TEXT.__text: 0xd3584
-  __TEXT.__objc_methlist: 0xb854
+  __TEXT.__text: 0xd3ad0
+  __TEXT.__objc_methlist: 0xb89c
   __TEXT.__const: 0x2624
-  __TEXT.__cstring: 0x4d31
-  __TEXT.__gcc_except_tab: 0x1ccc
-  __TEXT.__oslogstring: 0x5b36
+  __TEXT.__cstring: 0x4d41
+  __TEXT.__gcc_except_tab: 0x1d48
+  __TEXT.__oslogstring: 0x5ba6
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0xa2
   __TEXT.__constg_swiftt: 0x2e90

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x20
-  __TEXT.__unwind_info: 0x2cd8
+  __TEXT.__unwind_info: 0x2ce8
   __TEXT.__eh_frame: 0xa20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b78
+  __DATA_CONST.__objc_selrefs: 0x6b90
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x398
   __DATA_CONST.__objc_arraydata: 0xd8
-  __DATA_CONST.__got: 0xd98
-  __AUTH_CONST.__const: 0x2fb0
+  __DATA_CONST.__got: 0xe10
+  __AUTH_CONST.__const: 0x2fd0
   __AUTH_CONST.__cfstring: 0x3760
-  __AUTH_CONST.__objc_const: 0x151f0
+  __AUTH_CONST.__objc_const: 0x15200
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__auth_got: 0xf20
-  __AUTH.__objc_data: 0x6970
+  __AUTH.__objc_data: 0x6920
   __AUTH.__data: 0x670
   __DATA.__objc_ivar: 0xbac
   __DATA.__data: 0x2590
-  __DATA.__bss: 0x2770
+  __DATA.__bss: 0x2780
   __DATA.__common: 0x4c0
-  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__objc_data: 0x820
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4854
-  Symbols:   13886
-  CStrings:  1672
+  Functions: 4861
+  Symbols:   13904
+  CStrings:  1675
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__data : content changed
Symbols:
+ +[TVRUIFeatures isLandscapeModeEnabled]
+ -[TVRUICoreDevice device:updatedPairedRemoteInfo:]
+ -[TVRUIRemoteViewController device:updatedPairedRemoteInfo:]
+ GCC_except_table122
+ GCC_except_table190
+ GCC_except_table62
+ GCC_except_table69
+ GCC_except_table85
+ GCC_except_table99
+ _OBJC_CLASS_$_UITraitActiveAppearance
+ __TVRUISceneLog
+ ____TVRUISceneLog_block_invoke
+ _objc_msgSend$activeAppearance
+ _objc_msgSend$device:updatedPairedRemoteInfo:
- GCC_except_table121
- GCC_except_table188
- GCC_except_table23
- GCC_except_table39
- GCC_except_table61
- GCC_except_table68
- GCC_except_table84
- GCC_except_table98
CStrings:
+ "ActiveAppearanceTrait changed:%ld, scene activation state:%ld, supportsSiri:%{bool}d"
+ "Deactivating Siri events"
+ "Paired remote info updated: %@"
+ "Scene"
+ "device: '%{public}@' updated paired remote info: %@"
- "%s - %{public}@"
- "Deactivating connection - notification scene object: %@ current scene: %@"

```
