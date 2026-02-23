## AVKit

> `/System/Library/Frameworks/AVKit.framework/AVKit`

```diff

-1320.15.1.11.2
-  __TEXT.__text: 0x256368
-  __TEXT.__auth_stubs: 0x39a0
+1320.17.1.0.0
+  __TEXT.__text: 0x2569e0
+  __TEXT.__auth_stubs: 0x39b0
   __TEXT.__objc_methlist: 0x1de84
-  __TEXT.__const: 0x7fe8
+  __TEXT.__const: 0x7ff8
   __TEXT.__constg_swiftt: 0x2684
   __TEXT.__swift5_typeref: 0x7b1e
   __TEXT.__swift5_builtin: 0x1a4
   __TEXT.__swift5_reflstr: 0x1d96
   __TEXT.__swift5_fieldmd: 0x1c74
   __TEXT.__swift5_assocty: 0x870
-  __TEXT.__swift5_capture: 0x1370
-  __TEXT.__cstring: 0x12073
+  __TEXT.__swift5_capture: 0x1384
+  __TEXT.__cstring: 0x12157
   __TEXT.__swift5_proto: 0x2c0
   __TEXT.__swift5_types: 0x230
   __TEXT.__swift5_protos: 0x34
-  __TEXT.__swift_as_entry: 0x2a0
+  __TEXT.__swift_as_entry: 0x2a4
   __TEXT.__swift_as_ret: 0x3f4
-  __TEXT.__oslogstring: 0xa6df
+  __TEXT.__oslogstring: 0xa916
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__gcc_except_tab: 0x43a0
   __TEXT.__dlopen_cstrs: 0x1ef
   __TEXT.__ustring: 0x7a
-  __TEXT.__unwind_info: 0xa4d8
-  __TEXT.__eh_frame: 0x6f94
+  __TEXT.__unwind_info: 0xa4f8
+  __TEXT.__eh_frame: 0x6f8c
   __TEXT.__objc_classname: 0x41ca
   __TEXT.__objc_methname: 0x4b4d8
   __TEXT.__objc_methtype: 0x9b60
   __TEXT.__objc_stubs: 0x2a440
-  __DATA_CONST.__got: 0x1648
+  __DATA_CONST.__got: 0x1650
   __DATA_CONST.__const: 0x3230
   __DATA_CONST.__objc_classlist: 0xa80
   __DATA_CONST.__objc_catlist: 0xe0

   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x7b8
   __DATA_CONST.__objc_arraydata: 0x5c8
-  __AUTH_CONST.__auth_got: 0x1ce0
-  __AUTH_CONST.__const: 0x8078
-  __AUTH_CONST.__cfstring: 0x9040
+  __AUTH_CONST.__auth_got: 0x1ce8
+  __AUTH_CONST.__const: 0x80a0
+  __AUTH_CONST.__cfstring: 0x9060
   __AUTH_CONST.__objc_const: 0x36420
   __AUTH_CONST.__objc_intobj: 0x690
   __AUTH_CONST.__objc_arrayobj: 0x318

   __AUTH.__objc_data: 0x6088
   __AUTH.__data: 0x1878
   __DATA.__objc_ivar: 0x2ec4
-  __DATA.__data: 0x5918
+  __DATA.__data: 0x5928
   __DATA.__bss: 0x5b80
   __DATA.__common: 0x1a8
   __DATA_DIRTY.__objc_data: 0x1618

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2D4B4482-3B0F-3225-A958-64A5C5E1954D
-  Functions: 14101
+  UUID: 1B476F4D-B35D-31BE-838C-86011928F862
+  Functions: 14108
   Symbols:   36116
-  CStrings:  16033
+  CStrings:  16046
 
Symbols:
+ _block_copy_helper.105
+ _block_copy_helper.112
+ _block_copy_helper.119
+ _block_copy_helper.137
+ _block_copy_helper.140
+ _block_copy_helper.155
+ _block_copy_helper.64
+ _block_copy_helper.91
+ _block_copy_helper.98
+ _block_descriptor.100
+ _block_descriptor.107
+ _block_descriptor.114
+ _block_descriptor.121
+ _block_descriptor.139
+ _block_descriptor.142
+ _block_descriptor.157
+ _block_descriptor.66
+ _block_descriptor.93
+ _block_destroy_helper.106
+ _block_destroy_helper.113
+ _block_destroy_helper.120
+ _block_destroy_helper.138
+ _block_destroy_helper.141
+ _block_destroy_helper.156
+ _block_destroy_helper.65
+ _block_destroy_helper.92
+ _block_destroy_helper.99
+ _objectdestroy.61Tm
+ _objectdestroy.83Tm
+ _objectdestroy.95Tm
- _block_copy_helper.101
- _block_copy_helper.108
- _block_copy_helper.115
- _block_copy_helper.133
- _block_copy_helper.136
- _block_copy_helper.151
- _block_copy_helper.60
- _block_copy_helper.87
- _block_copy_helper.94
- _block_descriptor.103
- _block_descriptor.110
- _block_descriptor.117
- _block_descriptor.135
- _block_descriptor.138
- _block_descriptor.153
- _block_descriptor.62
- _block_descriptor.89
- _block_descriptor.96
- _block_destroy_helper.102
- _block_destroy_helper.109
- _block_destroy_helper.116
- _block_destroy_helper.134
- _block_destroy_helper.137
- _block_destroy_helper.152
- _block_destroy_helper.61
- _block_destroy_helper.88
- _block_destroy_helper.95
- _objectdestroy.79Tm
- _objectdestroy.84Tm
- _objectdestroy.91Tm
CStrings:
+ "%s *** Warning: Exit full screen failed due to invalid view hierarchy state."
+ "%s Attempting presentation state recovery after an invalid dismissal."
+ "%s Dismissal failed; view needs layout."
+ "%s Non-interactive dismissal analysis: isViewLoaded=%@ AND (hasSuperview=%@ OR isPresentingDetached=%@) AND isPresentingFromInline=%@ = %@"
+ "%s Presentation state recovery completed successfully."
+ "%s Starting interactive dismissal."
+ "%s Starting non-interactive dismissal."
+ "%s State recovery verification failed."
+ "%s _transitionFromFullScreenAnimated completed - success: %@, error: %@."
+ "-[AVPlayerViewController(AVPlayerViewController_WebKitOnly) exitFullScreenAnimated:completionHandler:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/345FA0F7-D458-4BA1-9114-CC5B23030309/TemporaryDirectory.OsEzG8/Sources/AVKit/Embedded/MobileAVKit/InputPicker/Common/AVRoutingInputController.swift"
+ "Failed to recover from invalid fullscreen state"
+ "MEDIA_OPTIONS_SUBTITLES_NOT_AVAILABLE_OPTION_TITLE"
+ "Not available option title"
- " (Not Available)"
- "/Library/Caches/com.apple.xbs/537E84A8-5AEB-4DBF-96C4-BC51D7EC9B10/TemporaryDirectory.TvFt17/Sources/AVKit/Embedded/MobileAVKit/InputPicker/Common/AVRoutingInputController.swift"

```
